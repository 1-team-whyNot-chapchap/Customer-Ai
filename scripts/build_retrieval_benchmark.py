"""Freeze a source-grounded 300-question retrieval evaluation set."""

import csv
import hashlib
import json
import random
import re
from collections import Counter

from build_policy_corpus import CORPUS, ROOT, build

BENCH = ROOT / "knowledge" / "retrieval-benchmark-20260908"


def norm(text):
    return re.sub(r"\s+", " ", text).strip()


def main():
    build(ROOT.parent / "chapchap-docs", check=True)
    selection = json.loads((CORPUS / "selection.json").read_text(encoding="utf-8"))
    source_lines = {
        name: (ROOT.parent / "chapchap-docs" / name).read_text(encoding="utf-8-sig").splitlines()
        for name in selection["sources"]
    }
    policy_lines = {}
    for doc in selection["documents"]:
        for span in doc["spans"]:
            for number in range(span["start"], span["end"] + 1):
                text = source_lines[doc["source"]][number - 1]
                policy_lines.setdefault(span["policyId"], []).append(
                    {"source": doc["source"], "line": number, "quote": text}
                )
    with (BENCH / "scenarios.tsv").open(encoding="utf-8", newline="") as handle:
        scenarios = list(csv.DictReader(handle, delimiter="\t"))
    expected = {"basic": 50, "condition": 50, "multi": 20, "unsupported": 15, "external": 15}
    assert Counter(s["category"] for s in scenarios) == expected
    train_counts = {"basic": 34, "condition": 33, "multi": 13, "unsupported": 10, "external": 10}
    rng = random.Random(20260908)
    train = set()
    for category, count in train_counts.items():
        indices = [i for i, row in enumerate(scenarios) if row["category"] == category]
        rng.shuffle(indices)
        train.update(indices[:count])
    rows, errors = [], []
    for index, scenario in enumerate(scenarios):
        references = []
        route, rationale = "POLICY", "발췌 원문에서 필수 근거를 회수해야 함"
        for item in scenario["policy_anchors"].split(";"):
            policy, anchor = item.split(":", 1)
            if policy in {"NONE", "CURRENT", "OUT"}:
                route = {"NONE": "INSUFFICIENT", "CURRENT": "CURRENT_STATE", "OUT": "OUT_OF_SCOPE"}[
                    policy
                ]
                rationale = anchor
                continue
            matches = [
                p
                for p in policy_lines[policy]
                if norm(anchor) in norm(p["quote"]) and not p["quote"].startswith("#")
            ]
            if not matches:
                errors.append({"group": index + 1, "policy": policy, "anchor": anchor})
                continue
            # Keep every matching source line for inspection.
            # Alternative matches are not all required.
            references.append({"policyId": policy, "anchor": anchor, "sources": matches})
        for variant in ("a", "b"):
            rows.append(
                {
                    "id": f"Q{index * 2 + (1 if variant == 'a' else 2):03}",
                    "group": f"G{index + 1:03}",
                    "variant": variant,
                    "category": scenario["category"],
                    "split": "development" if index in train else "final",
                    "question": scenario[f"question_{variant}"],
                    "expectedRoute": route,
                    "rationale": rationale,
                    "gold": references,
                }
            )
    if errors:
        print(json.dumps(errors, ensure_ascii=False, indent=2))
        raise SystemExit("Source annotation review required before freeze")
    assert len(rows) == len({r["question"] for r in rows}) == 300
    assert Counter(r["split"] for r in rows) == {"development": 200, "final": 100}
    data = {
        "version": "1.0",
        "sourceCommit": selection["sourceCommit"],
        "sourceHashes": selection["sources"],
        "splitSeed": 20260908,
        "questions": rows,
    }
    raw = (json.dumps(data, ensure_ascii=False, indent=2) + "\n").encode()
    target = BENCH / "questions.json"
    if (BENCH / "DATASET-LOCK.json").exists() and target.read_bytes() != raw:
        raise ValueError("Frozen dataset differs; use an explicit new benchmark version")
    target.write_bytes(raw)
    lock = {
        "sha256": hashlib.sha256(raw).hexdigest(),
        "questions": 300,
        "groups": 150,
        "development": 200,
        "final": 100,
        "sourceCommit": selection["sourceCommit"],
    }
    (BENCH / "DATASET-LOCK.json").write_text(json.dumps(lock, indent=2) + "\n", encoding="utf-8")
    md = [
        "# 300문항 전체 목록",
        "",
        "150개 시나리오의 표현 2개씩이다. 정책 원문이 아닌 평가 데이터다.",
        "",
    ]
    for row in rows:
        md += [
            f"## {row['id']} — {row['question']}",
            "",
            f"그룹: {row['group']} / 분류: {row['category']} / split: {row['split']}",
            "",
            f"기대 처리: {row['expectedRoute']} — {row['rationale']}",
            "",
        ]
        for gold in row["gold"]:
            md += [f"필수 근거: {gold['policyId']} / 확인 구절: {gold['anchor']}", ""]
            for source in gold["sources"]:
                md += [
                    f"원본: `{source['source']}:{source['line']}`",
                    "",
                    "> " + source["quote"],
                    "",
                ]
    (BENCH / "QUESTIONS-300.md").write_text("\n".join(md), encoding="utf-8")
    print(json.dumps(lock))


if __name__ == "__main__":
    main()
