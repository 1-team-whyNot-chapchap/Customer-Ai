"""Controlled local search variants. No question labels or gold answers are inputs."""

import json
import math
import re
from collections import Counter

POLICY_RE = re.compile(r"(?<![\w-])(?:AUTH-|CS-|DLV-)?POL-[A-Z]+-\d{3}")
METHODS = ("R1", "R2", "R3", "R4")


def policy_id(chunk):
    matches = POLICY_RE.findall(" / ".join(chunk["section_path"]))
    return matches[-1] if matches else None


class BM25:
    def __init__(self, documents, tokenizer):
        self.tokenizer = tokenizer
        self.tokens = [Counter(tokenizer.encode(text, add_special_tokens=False))
                       for text in documents]
        self.lengths = [sum(row.values()) for row in self.tokens]
        self.average = sum(self.lengths) / len(documents)
        frequency = Counter(term for row in self.tokens for term in row)
        n = len(documents)
        self.idf = {term: math.log(1 + (n - df + 0.5) / (df + 0.5))
                    for term, df in frequency.items()}

    def scores(self, query):
        terms = set(self.tokenizer.encode(query, add_special_tokens=False))
        output = []
        for row, length in zip(self.tokens, self.lengths, strict=True):
            score = 0.0
            for term in terms:
                frequency = row.get(term, 0)
                if frequency:
                    score += self.idf[term] * frequency * 2.2 / (
                        frequency + 1.2 * (0.25 + 0.75 * length / self.average)
                    )
            output.append(score)
        return output


class LocalSearchEngine:
    def __init__(self, collection, chunks, tokenizer, heading_vectors=None):
        self.collection = collection
        self.chunks = {c["chunk_id"]: c for c in chunks}
        self.ordered = list(chunks)
        self.tokenizer = tokenizer
        self.heading_vectors = heading_vectors
        self.bm25 = BM25([" / ".join(c["section_path"]) + "\n" + c["text"]
                          for c in chunks], tokenizer)
        self.groups = {}
        for chunk in chunks:
            self.groups.setdefault(self.group_key(chunk), []).append(chunk)
        for members in self.groups.values():
            members.sort(key=lambda c: c["ordinal"])

    @staticmethod
    def group_key(chunk):
        return (chunk["knowledge_version_id"], chunk["document_key"],
                policy_id(chunk) or chunk["chunk_id"])

    def count(self, text):
        return len(self.tokenizer.encode(text, add_special_tokens=False))

    def dense(self, vector, allowed, count):
        if not allowed or any(type(x) is not int or x <= 0 for x in allowed):
            raise ValueError("Positive allowed version IDs required")
        found = self.collection.query(
            query_embeddings=[list(vector)], n_results=count,
            where={"knowledgeVersionId": {"$in": list(allowed)}},
            include=["documents", "metadatas", "distances"],
        )
        rows = []
        for cid, distance in zip(found["ids"][0], found["distances"][0], strict=True):
            score = max(0.0, min(1.0, 1.0 - float(distance)))
            chunk = self.chunks[cid]
            if chunk["knowledge_version_id"] not in allowed:
                raise ValueError("Disallowed version returned")
            if score >= 0.70:
                rows.append({"chunkId": cid, "denseScore": score, "score": score})
        return rows

    def search(self, query, vector, method, allowed):
        if method not in METHODS or not query.strip():
            raise ValueError("Unsupported method or blank query")
        dense = self.dense(vector, allowed, 5 if method in {"R1", "R2"} else 20)
        components = {"dense": dense}
        if method in {"R1", "R2"}:
            candidates = dense
        else:
            lexical = sorted([
                {"chunkId": c["chunk_id"], "bm25Score": score}
                for c, score in zip(self.ordered, self.bm25.scores(query), strict=True)
                if score > 0 and c["knowledge_version_id"] in allowed
            ], key=lambda x: (-x["bm25Score"], x["chunkId"]))[:20]
            components["bm25"] = lexical
            merged = {}
            for ranking in (dense, lexical):
                for rank, entry in enumerate(ranking, 1):
                    cid = entry["chunkId"]
                    row = merged.setdefault(cid, {"chunkId": cid, "score": 0.0})
                    row.update({k: v for k, v in entry.items() if k != "score"})
                    row["score"] += 1 / (60 + rank)
            fused = sorted(merged.values(), key=lambda x: (-x["score"], x["chunkId"]))
            components["rrf"] = [dict(row) for row in fused]
            candidates = fused[:20]
            if method == "R4":
                if self.heading_vectors is None:
                    raise ValueError("Heading embeddings required for R4")
                # Score the union candidates on the original body and title vectors.
                stored = self.collection.get(ids=[x["chunkId"] for x in candidates],
                                             include=["embeddings"])
                embeddings = dict(zip(stored["ids"], stored["embeddings"], strict=True))
                for row in candidates:
                    cid = row["chunkId"]
                    body = sum(float(a) * float(b) for a, b in zip(
                        vector, embeddings[cid], strict=True))
                    title = sum(float(a) * float(b) for a, b in zip(
                        vector, self.heading_vectors[cid], strict=True))
                    row.update(rrfScore=row["score"], denseScore=body, titleScore=title,
                               score=0.7 * body + 0.3 * title)
                candidates.sort(key=lambda x: (-x["score"], x["chunkId"]))
        hits = candidates[:5]
        context, omitted = self.context(hits, allowed, expand=method != "R1")
        return {"hits": hits, "candidates": candidates, "components": components,
                "context": context, "omittedChunkIds": omitted,
                "contextTokens": self.count("\n\n".join(x["text"] for x in context)),
                "decision": "CANDIDATES_ONLY" if hits else "NO_EVIDENCE"}

    def context(self, hits, allowed, *, expand):
        if not expand:
            return [{**self.chunks[h["chunkId"]], "originHit": h["chunkId"]} for h in hits], []
        context, omitted, seen, used_groups = [], [], set(), set()
        budget = 6000
        for hit in hits:
            chunk = self.chunks[hit["chunkId"]]
            if chunk["knowledge_version_id"] not in allowed:
                raise ValueError("Expansion cannot cross the allowed version boundary")
            key = self.group_key(chunk)
            if key in used_groups:
                continue
            if len(used_groups) >= 3:
                omitted.extend(c["chunk_id"] for c in self.groups[key])
                continue
            used_groups.add(key)
            for member in self.groups[key]:
                cid = member["chunk_id"]
                if cid in seen:
                    continue
                seen.add(cid)
                candidate = "\n\n".join([*(x["text"] for x in context), member["text"]])
                if self.count(candidate) > budget:
                    omitted.append(cid)
                    continue
                context.append({**member, "originHit": hit["chunkId"]})
        return context, list(dict.fromkeys(omitted))


def read_chunks(path):
    return json.loads(path.read_text(encoding="utf-8"))
