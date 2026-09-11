"""Run development comparisons, freeze selection, then evaluate the held-out split."""

import argparse
import ctypes
import hashlib
import json
import os
import statistics
import time
from datetime import datetime, timedelta, timezone

from benchmark_retrieval_engine import LocalSearchEngine, policy_id
from build_policy_corpus import ROOT
from build_retrieval_benchmark import BENCH, norm


def save(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def memory():
    if os.name != "nt":
        return {"rssBytes": None, "peakRssBytes": None}

    class Counters(ctypes.Structure):
        _fields_ = [("cb", ctypes.c_ulong), ("faults", ctypes.c_ulong)] + [
            (key, ctypes.c_size_t)
            for key in (
                "peak",
                "rss",
                "paged_peak",
                "paged",
                "nonpaged_peak",
                "nonpaged",
                "pagefile",
                "pagefile_peak",
            )
        ]

    data = Counters()
    data.cb = ctypes.sizeof(data)
    kernel = ctypes.windll.kernel32
    kernel.GetCurrentProcess.restype = ctypes.c_void_p
    ok = ctypes.windll.psapi.GetProcessMemoryInfo(
        ctypes.c_void_p(kernel.GetCurrentProcess()), ctypes.byref(data), data.cb
    )
    return {"rssBytes": data.rss if ok else None, "peakRssBytes": data.peak if ok else None}


def evaluate(row, found):
    policies = {policy_id(c) for c in found["context"]}
    checks = []
    for gold in row["gold"]:
        text = norm(
            "\n\n".join(c["text"] for c in found["context"] if policy_id(c) == gold["policyId"])
        )
        checks.append(
            {
                "policyId": gold["policyId"],
                "anchor": gold["anchor"],
                "policyHit": gold["policyId"] in policies,
                "anchorHit": norm(gold["anchor"]) in text,
                "sourceClauseHit": any(norm(s["quote"]) in text for s in gold["sources"]),
            }
        )
    answerable = row["expectedRoute"] == "POLICY"
    relevant = {g["policyId"] for g in row["gold"]}
    hit_policies = [policy_id(c) for c in found["context"]]
    return {
        "answerable": answerable,
        "checks": checks,
        "allPolicies": all(c["policyHit"] for c in checks) if answerable else None,
        "allAnchors": all(c["anchorHit"] for c in checks) if answerable else None,
        "allSourceClauses": all(c["sourceClauseHit"] for c in checks) if answerable else None,
        "nonGoldContextChunks": sum(p not in relevant for p in hit_policies)
        if answerable
        else None,
        "nonPolicyQuestionReturnedCandidates": bool(found["hits"]) if not answerable else None,
        "routeCorrectness": "NOT_EVALUATED_NO_ROUTER",
        "answerCorrectness": "NOT_EVALUATED_NO_GENERATOR",
    }


def summarize(rows):
    good = [r for r in rows if r.get("evaluation", {}).get("answerable")]
    other = [r for r in rows if r.get("evaluation") and not r["evaluation"]["answerable"]]
    times = sorted(r["retrievalMs"] for r in rows if "retrievalMs" in r)
    return {
        "rows": len(rows),
        "errors": sum("error" in r for r in rows),
        "answerable": len(good),
        "nonPolicy": len(other),
        **{
            key: sum(r["evaluation"][key] for r in good)
            for key in ("allPolicies", "allAnchors", "allSourceClauses")
        },
        "nonPolicyReturnedCandidates": sum(
            r["evaluation"]["nonPolicyQuestionReturnedCandidates"] for r in other
        ),
        "meanContextTokens": statistics.mean(
            r["contextTokens"] for r in rows if "contextTokens" in r
        ),
        "medianRetrievalMs": statistics.median(times),
        "p95RetrievalMs": times[min(len(times) - 1, int(len(times) * 0.95))],
    }


def main(phase):
    os.environ["HF_HUB_OFFLINE"] = "1"
    os.environ["TRANSFORMERS_OFFLINE"] = "1"
    os.environ["HF_HUB_DISABLE_IMPLICIT_TOKEN"] = "1"
    os.environ["ANONYMIZED_TELEMETRY"] = "False"
    import chromadb
    from chromadb.config import Settings

    from chapchap_customer_ai.rag.embeddings import MultilingualE5SmallEmbedder

    lock = json.loads((BENCH / "DATASET-LOCK.json").read_text())
    assert digest(BENCH / "questions.json") == lock["sha256"]
    data = json.loads((BENCH / "questions.json").read_text(encoding="utf-8"))
    for name, expected in data["sourceHashes"].items():
        assert digest(ROOT.parent / "chapchap-docs" / name) == expected
    if phase == "development":
        methods = ["R1", "R2", "R3", "R4"]
    else:
        chosen = json.loads((BENCH / "SELECTION.json").read_text(encoding="utf-8"))
        assert chosen["datasetSha256"] == lock["sha256"]
        assert chosen["engineSha256"] == digest(ROOT / "scripts/benchmark_retrieval_engine.py")
        methods = list(dict.fromkeys(["R1", chosen["method"]]))
    destination = BENCH / "runs" / phase
    destination.mkdir(parents=True, exist_ok=True)
    if any((destination / f"{method}.jsonl").exists() for method in methods):
        raise ValueError("Run outputs already exist; do not overwrite a recorded experiment")
    start = time.perf_counter()
    embedder = MultilingualE5SmallEmbedder.from_pretrained()
    model_load_ms = (time.perf_counter() - start) * 1000
    tokenizer = embedder.encoder.tokenizer
    local = json.loads((ROOT / "reports/local-rag/latest.json").read_text(encoding="utf-8"))
    from pathlib import Path

    old_dir = Path(local["directory"])
    chunks = json.loads((old_dir / "chunks.json").read_text(encoding="utf-8"))
    settings = Settings(anonymized_telemetry=False)
    original_client = chromadb.PersistentClient(path=str(old_dir / "chroma"), settings=settings)
    original = original_client.get_collection("local_policy_review_v1")
    stored = original.get(include=["embeddings", "documents", "metadatas"])
    cache_dir = ROOT / "reports/retrieval-benchmark-20260908" / lock["sha256"][:16]
    cache_dir.mkdir(parents=True, exist_ok=True)
    client = chromadb.PersistentClient(path=str(cache_dir / "chroma"), settings=settings)
    clone = client.get_or_create_collection(
        "benchmark_policy_v1", metadata={"hnsw:space": "cosine"}
    )
    if clone.count() == 0:
        clone.upsert(
            ids=stored["ids"],
            embeddings=stored["embeddings"],
            documents=stored["documents"],
            metadatas=stored["metadatas"],
        )
    assert clone.count() == original.count() == len(chunks) == 146
    clone_data = clone.get(include=["documents"])
    assert dict(zip(clone_data["ids"], clone_data["documents"], strict=True)) == {
        c["chunk_id"]: c["text"] for c in chunks
    }
    title_start = time.perf_counter()
    titles = {c["chunk_id"]: " / ".join(c["section_path"]) for c in chunks}
    title_vectors = embedder.embed_passages(list(titles.values()))
    heading = dict(zip(titles, title_vectors, strict=True))
    title_ms = (time.perf_counter() - title_start) * 1000
    engine = LocalSearchEngine(clone, chunks, tokenizer, heading)
    allowed = sorted({c["knowledge_version_id"] for c in chunks})
    questions = [q for q in data["questions"] if q["split"] == phase]
    assert len(questions) == (200 if phase == "development" else 100)
    embeddings, embedding_ms = {}, {}
    for index, row in enumerate(questions):
        now = time.perf_counter()
        embeddings[row["id"]] = embedder.embed_query(row["question"])
        embedding_ms[row["id"]] = (time.perf_counter() - now) * 1000
        if (index + 1) % 25 == 0:
            print(f"{phase}: encoded {index + 1}/{len(questions)}", flush=True)
    metrics = {}
    for method in methods:
        rows = []
        path = destination / f"{method}.jsonl"
        with path.open("x", encoding="utf-8") as handle:
            for row in questions:
                now = time.perf_counter()
                try:
                    found = engine.search(row["question"], embeddings[row["id"]], method, allowed)
                    elapsed = (time.perf_counter() - now) * 1000
                    result = {
                        "id": row["id"],
                        "group": row["group"],
                        "question": row["question"],
                        "method": method,
                        "split": phase,
                        "queryEmbeddingMs": embedding_ms[row["id"]],
                        "retrievalMs": elapsed,
                        **found,
                        "evaluation": evaluate(row, found),
                    }
                except Exception as error:
                    result = {
                        "id": row["id"],
                        "method": method,
                        "split": phase,
                        "error": type(error).__name__,
                        "message": str(error),
                    }
                rows.append(result)
                handle.write(json.dumps(result, ensure_ascii=False) + "\n")
                handle.flush()
        metrics[method] = summarize(rows)
        print(json.dumps({"phase": phase, "method": method, **metrics[method]}), flush=True)
    environment = {
        "datasetSha256": lock["sha256"],
        "phase": phase,
        "completedAt": datetime.now(timezone(timedelta(hours=9))).isoformat(),
        "engineSha256": digest(ROOT / "scripts/benchmark_retrieval_engine.py"),
        "model": embedder.model_id,
        "modelRevision": embedder.encoder._first_module().auto_model.config._commit_hash,
        "modelLoadMs": model_load_ms,
        "headingEmbeddingMs": title_ms,
        "meanQueryEmbeddingMs": statistics.mean(embedding_ms.values()),
        "memory": memory(),
        "cacheDirectory": str(cache_dir),
        "originalCollectionCount": original.count(),
        "benchmarkCollectionCount": clone.count(),
        "metrics": metrics,
    }
    save(destination / "SUMMARY.json", environment)
    if any(m["errors"] for m in metrics.values()):
        raise RuntimeError("Recorded execution errors; review before proceeding")
    if phase == "development":
        best = max(
            methods,
            key=lambda m: (
                metrics[m]["allSourceClauses"],
                metrics[m]["allPolicies"],
                -metrics[m]["meanContextTokens"],
            ),
        )
        save(
            BENCH / "SELECTION.json",
            {
                "method": best,
                "datasetSha256": lock["sha256"],
                "engineSha256": environment["engineSha256"],
                "selectedAt": environment["completedAt"],
                "rule": "allSourceClauses, then allPolicies, then smaller meanContextTokens",
                "developmentMetrics": metrics,
                "runHashes": {m: digest(destination / f"{m}.jsonl") for m in methods},
                "finalSetUsedForSelection": False,
            },
        )
        print(f"Selected {best}; final split has not been evaluated.", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("phase", choices=["development", "final"])
    main(parser.parse_args().phase)
