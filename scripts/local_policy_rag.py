"""Offline policy ingestion/search in an isolated, non-production Chroma database."""

import argparse
import hashlib
import json
import math
import os
from dataclasses import asdict
from pathlib import Path

from build_policy_corpus import CORPUS, ROOT, build

CASES = [
    ("구독 시작 전날 오후 2시에 취소할 수 있나요?", "POL-SUBSCRIPTION-003", "14:00"),
    ("도시락 두 개를 주문하면 둘 다 첫 구독 30% 할인이 되나요?", "POL-PAYMENT-009", "한 개"),
    ("배송비는 얼마인가요?", "POL-PAYMENT-002", "3,000"),
    ("구독은 며칠 동안 이용하나요?", "POL-SUBSCRIPTION-005", "28일"),
    ("서울 주소로 도시락 배송을 신청할 수 있나요?", "POL-ADDRESS-001", "대구"),
    ("공휴일 배송은 다른 날짜로 옮겨 주나요?", "POL-ORDER-006", "다른 날짜"),
    ("결제 카드를 삭제했는데 환불은 어디로 받나요?", "POL-PAYMENT-012", "원 결제"),
    ("환불 중 일부 결제만 취소되면 완료인가요?", "POL-PAYMENT-012", "확인 필요"),
    ("고객이 집에 없으면 배달은 어떻게 하나요?", "DLV-POL-ABSENCE-001", "연락"),
    ("배송 지연 알림을 받으면 환불도 완료된 건가요?", "DLV-POL-DELAY-002", "알림 Event만으로"),
    ("품질 문의를 접수하면 바로 환불되나요?", "CS-POL-QI-003", "의미하지 않는다"),
    ("품질 문의 첨부파일은 몇 MB까지 가능한가요?", "CS-POL-FILE-003", "10MB"),
    ("마케팅 이메일 동의를 거절해도 가입할 수 있나요?", "AUTH-POL-CNS-003", "선택"),
    ("만 13세도 가입할 수 있나요?", "AUTH-POL-SIGN-005", "14세"),
]


def save(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def run(query=None):
    os.environ["HF_HUB_OFFLINE"] = "1"
    os.environ["TRANSFORMERS_OFFLINE"] = "1"
    os.environ["HF_HUB_DISABLE_IMPLICIT_TOKEN"] = "1"
    os.environ["ANONYMIZED_TELEMETRY"] = "False"
    import chromadb
    from chromadb.config import Settings

    from chapchap_customer_ai.rag.chunking import HybridPolicyV1Chunker
    from chapchap_customer_ai.rag.embeddings import MultilingualE5SmallEmbedder
    from chapchap_customer_ai.rag.extraction import TextDocumentExtractor
    from chapchap_customer_ai.rag.models import KnowledgeContext
    from chapchap_customer_ai.rag.services import RagCoreService
    from chapchap_customer_ai.rag.tokenization import MultilingualE5TokenCounter
    from chapchap_customer_ai.rag.vector_store import ChromaVectorStore

    build(ROOT.parent / "chapchap-docs", check=True)
    manifest_bytes = (CORPUS / "manifest.json").read_bytes()
    manifest = json.loads(manifest_bytes)
    embedder = MultilingualE5SmallEmbedder.from_pretrained()
    counter = MultilingualE5TokenCounter(embedder.encoder.tokenizer)
    overhead = len(counter.tokenizer.encode("passage: ", add_special_tokens=True))
    limit = embedder.encoder.max_seq_length
    budget = limit - overhead
    fingerprint = hashlib.sha256(manifest_bytes + str(budget).encode()).hexdigest()[:16]
    directory = ROOT / "reports" / "local-rag" / fingerprint
    directory.mkdir(parents=True, exist_ok=True)
    client = chromadb.PersistentClient(
        path=str(directory / "chroma"), settings=Settings(anonymized_telemetry=False)
    )
    name = "local_policy_review_v1"
    if query:
        collection = client.get_collection(name)
    else:
        collection = client.get_or_create_collection(name, metadata={"hnsw:space": "cosine"})
    assert collection.metadata["hnsw:space"] == "cosine"
    store = ChromaVectorStore(collection)
    allowed_ids = list(range(1, len(manifest["documents"]) + 1))

    def search(text):
        return [asdict(hit) for hit in store.search(
            embedder.embed_query(text), allowed_ids, top_k=5, similarity_threshold=0.70
        )]

    if query:
        result = {"query": query, "storedChunks": collection.count(), "hits": search(query)}
        save(directory / "last-query.json", result)
        print(json.dumps(result, ensure_ascii=False), flush=True)
        return

    service = RagCoreService(
        TextDocumentExtractor(), HybridPolicyV1Chunker(counter, max_tokens=budget)
    )
    all_chunks, documents = [], []
    max_input = 0
    first_vector = None
    for local_id, doc in enumerate(manifest["documents"], 1):
        content = (CORPUS / "upload" / doc["file"]).read_bytes()
        context = KnowledgeContext(
            local_id, "HYBRID_POLICY_V1", Path(doc["file"]).stem, "LOCAL_POLICY_REVIEW",
            manifest["sourceCommit"][:7], "LOCAL_REVIEW_ONLY",
        )
        chunks = service.build_chunks(context, content, "text/markdown")
        for chunk in chunks:
            length = len(counter.tokenizer.encode(
                "passage: " + chunk.text, add_special_tokens=True
            ))
            assert length <= limit, f"Would truncate: {chunk.chunk_id} ({length})"
            max_input = max(max_input, length)
        vectors = embedder.embed_passages([chunk.text for chunk in chunks])
        for vector in vectors:
            assert len(vector) == 384 and all(math.isfinite(x) for x in vector)
            assert abs(math.sqrt(sum(x*x for x in vector)) - 1) < 1e-4
        store.upsert(chunks, vectors)
        if first_vector is None:
            first_vector = vectors[0]
        all_chunks.extend(chunks)
        documents.append({"file": doc["file"], "localVersionId": local_id, "chunks": len(chunks)})
        print(json.dumps(documents[-1]), flush=True)
    assert collection.count() == len(all_chunks)
    stored = collection.get(include=["documents", "embeddings"])
    expected = {c.chunk_id: c.text for c in all_chunks}
    assert dict(zip(stored["ids"], stored["documents"], strict=True)) == expected
    assert all(len(vector) == 384 for vector in stored["embeddings"])
    store.upsert([all_chunks[0]], [first_vector])
    assert collection.count() == len(all_chunks), "Idempotent upsert changed count"
    assert not store.search(embedder.embed_query("배송비"), [999999], top_k=5)
    save(directory / "chunks.json", [asdict(chunk) for chunk in all_chunks])
    evaluations = []
    for question, policy, condition in CASES:
        hits = search(question)
        relevant = [h for h in hits if any(policy in part for part in h["section_path"])]
        evaluations.append({"question": question, "expectedPolicy": policy,
                            "policyHit": bool(relevant),
                            "conditionHit": any(condition in h["text"] for h in relevant),
                            "hits": hits})
    negatives = [{"question": q, "hits": search(q)} for q in [
        "내 배송은 지금 어디에 있나요?", "파이썬 리스트 정렬 코드를 알려주세요",
        "도시락을 실온에 정확히 몇 시간까지 두어도 안전한가요?",
    ]]
    save(directory / "retrieval-review.json", {"positive": evaluations, "negative": negatives})
    result = {"scope": "LOCAL_REVIEW_ONLY", "directory": str(directory),
              "sourceCommit": manifest["sourceCommit"], "documents": documents,
              "chunks": len(all_chunks), "dimensions": 384, "bodyTokenBudget": budget,
              "maxActualInputTokens": max_input, "inputLimit": limit,
              "storedTextAndVectorCheck": "PASS", "idempotentUpsert": "PASS",
              "versionFilter": "PASS", "policyHits": sum(x["policyHit"] for x in evaluations),
              "conditionHits": sum(x["conditionHit"] for x in evaluations),
              "questions": len(evaluations),
              "negativeQueriesReturningHits": sum(bool(x["hits"]) for x in negatives),
              "customerApiUploadPerformed": False}
    save(directory / "result.json", result)
    save(ROOT / "reports" / "local-rag" / "latest.json", result)
    print(json.dumps(result, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query")
    args = parser.parse_args()
    run(args.query)
