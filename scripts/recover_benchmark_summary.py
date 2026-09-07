"""Recover aggregation only after the recorded tzdata failure; never rerun searches."""

import json
from datetime import datetime, timedelta, timezone

from build_retrieval_benchmark import BENCH
from run_retrieval_benchmark import ROOT, digest, save, summarize


def main():
    data = json.loads((BENCH / "questions.json").read_text(encoding="utf-8"))
    lock = json.loads((BENCH / "DATASET-LOCK.json").read_text())
    assert digest(BENCH / "questions.json") == lock["sha256"]
    for name, expected in data["sourceHashes"].items():
        assert digest(ROOT.parent / "chapchap-docs" / name) == expected
    expected_ids = {q["id"] for q in data["questions"] if q["split"] == "development"}
    destination = BENCH / "runs/development"
    assert not (BENCH / "SELECTION.json").exists()
    metrics = {}
    for method in ("R1", "R2", "R3", "R4"):
        rows = [
            json.loads(line)
            for line in (destination / f"{method}.jsonl").read_text(encoding="utf-8").splitlines()
        ]
        assert len(rows) == 200 and {r["id"] for r in rows} == expected_ids
        assert all(r["method"] == method and r["split"] == "development" for r in rows)
        metrics[method] = summarize(rows)
        assert metrics[method]["errors"] == 0
    stamp = datetime.now(timezone(timedelta(hours=9))).isoformat()
    engine_hash = digest(ROOT / "scripts/benchmark_retrieval_engine.py")
    save(
        destination / "SUMMARY.json",
        {
            "phase": "development",
            "datasetSha256": lock["sha256"],
            "engineSha256": engine_hash,
            "recoveredAt": stamp,
            "metrics": metrics,
            "incident": "800 rows flushed before ZoneInfoNotFoundError (tzdata absent). "
            "Only aggregation recovered. Search records unchanged.",
            "modelLoadMs": None,
            "headingEmbeddingMs": None,
            "memory": None,
            "unavailableReason": "Process exited before environment snapshot; not reconstructed.",
        },
    )
    best = max(
        metrics,
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
            "engineSha256": engine_hash,
            "selectedAt": stamp,
            "finalSetUsedForSelection": False,
            "rule": "allSourceClauses, then allPolicies, then smaller meanContextTokens",
            "developmentMetrics": metrics,
            "runHashes": {m: digest(destination / f"{m}.jsonl") for m in metrics},
        },
    )
    print(json.dumps({"selected": best, "metrics": metrics}))


if __name__ == "__main__":
    main()
