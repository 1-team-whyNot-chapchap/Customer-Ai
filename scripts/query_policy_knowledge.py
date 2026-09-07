"""Query local policy evidence using the frozen selected method (or --baseline)."""

import argparse
import json
import os
from pathlib import Path

from build_policy_corpus import ROOT, build
from build_retrieval_benchmark import BENCH
from run_retrieval_benchmark import digest


def main(query, baseline=False):
    build(ROOT.parent / "chapchap-docs", check=True)
    selection = json.loads((BENCH / "SELECTION.json").read_text(encoding="utf-8"))
    assert digest(ROOT / "scripts/benchmark_retrieval_engine.py") == selection["engineSha256"]
    for key in ("HF_HUB_OFFLINE", "TRANSFORMERS_OFFLINE", "HF_HUB_DISABLE_IMPLICIT_TOKEN"):
        os.environ[key] = "1"
    os.environ["ANONYMIZED_TELEMETRY"] = "False"
    import chromadb
    from chromadb.config import Settings

    from chapchap_customer_ai.rag.embeddings import MultilingualE5SmallEmbedder
    from chapchap_customer_ai.rag.local_policy_search import LocalSearchEngine

    local = json.loads((ROOT / "reports/local-rag/latest.json").read_text(encoding="utf-8"))
    directory = Path(local["directory"])
    chunks = json.loads((directory / "chunks.json").read_text(encoding="utf-8"))
    client = chromadb.PersistentClient(
        path=str(directory / "chroma"), settings=Settings(anonymized_telemetry=False)
    )
    collection = client.get_collection("local_policy_review_v1")
    model = MultilingualE5SmallEmbedder.from_pretrained()
    method = "R1" if baseline else selection["method"]
    heading = None
    if method == "R4":
        vectors = model.embed_passages([" / ".join(c["section_path"]) for c in chunks])
        heading = dict(zip([c["chunk_id"] for c in chunks], vectors, strict=True))
    engine = LocalSearchEngine(collection, chunks, model.encoder.tokenizer, heading)
    # Corpus-local IDs only; these are not production Knowledge version IDs.
    allowed = sorted({c["knowledge_version_id"] for c in chunks})
    result = engine.search(query, model.embed_query(query), method, allowed)
    print(
        json.dumps(
            {"scope": "LOCAL_EVIDENCE_CANDIDATES_ONLY", "method": method, "query": query, **result},
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query")
    parser.add_argument("--baseline", action="store_true")
    args = parser.parse_args()
    main(args.query, args.baseline)
