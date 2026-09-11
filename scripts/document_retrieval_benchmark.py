"""Audit and render every frozen benchmark result without rerunning retrieval."""

import json
from collections import Counter
from pathlib import Path

from benchmark_retrieval_engine import policy_id
from build_policy_corpus import ROOT, build
from build_retrieval_benchmark import BENCH
from run_retrieval_benchmark import digest, evaluate, save, summarize


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write(name, lines):
    (BENCH / name).write_text("\n".join(lines) + "\n", encoding="utf-8")


def block(value):
    return "```json\n" + json.dumps(value, ensure_ascii=False, indent=2) + "\n```"


def main():
    build(ROOT.parent / "chapchap-docs", check=True)
    data, lock = read(BENCH / "questions.json"), read(BENCH / "DATASET-LOCK.json")
    assert digest(BENCH / "questions.json") == lock["sha256"]
    selection = read(BENCH / "SELECTION.json")
    assert digest(ROOT / "scripts/benchmark_retrieval_engine.py") == selection["engineSha256"]
    questions = {q["id"]: q for q in data["questions"]}
    assert len(questions) == len(data["questions"]) == 300
    groups = {
        phase: {q["group"] for q in questions.values() if q["split"] == phase}
        for phase in ("development", "final")
    }
    assert not groups["development"] & groups["final"]
    for source, expected in data["sourceHashes"].items():
        assert digest(ROOT.parent / "chapchap-docs" / source) == expected
    for q in questions.values():
        for gold in q["gold"]:
            for source in gold["sources"]:
                lines = (
                    (ROOT.parent / "chapchap-docs" / source["source"])
                    .read_text(encoding="utf-8-sig")
                    .splitlines()
                )
                assert lines[source["line"] - 1] == source["quote"]
    local = read(ROOT / "reports/local-rag/latest.json")
    chunks = read(Path(local["directory"]) / "chunks.json")
    catalog = {c["chunk_id"]: c for c in chunks}
    assert len(catalog) == 146
    save(BENCH / "CHUNK-CATALOG.json", chunks)
    catalog_lines = [
        "# 검색 원문 청크 전체 146개",
        "",
        "원문·메타데이터 보존본. 문항 정답은 임베딩에 포함하지 않았다.",
        "",
    ]
    for cid, c in catalog.items():
        catalog_lines.extend([f"## {cid}", "", block(c), ""])
    write("CHUNK-CATALOG.md", catalog_lines)
    all_runs, summaries, failures = {}, {}, []
    table = [
        "| 단계 | 방식 | 문항 | 원문 구절 완전 회수 | 정책 완전 회수 | "
        "검색 중앙값 ms | 문맥 평균 토큰 |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]
    links = []
    for phase, methods in (
        ("development", ("R1", "R2", "R3", "R4")),
        ("final", ("R1", selection["method"])),
    ):
        for method in dict.fromkeys(methods):
            path = BENCH / "runs" / phase / f"{method}.jsonl"
            rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
            expected_ids = {q["id"] for q in questions.values() if q["split"] == phase}
            assert len(rows) == len(expected_ids) and {r["id"] for r in rows} == expected_ids
            if phase == "development":
                assert digest(path) == selection["runHashes"][method]
            for row in rows:
                assert "error" not in row
                assert row["split"] == phase and row["method"] == method
                assert evaluate(questions[row["id"]], row) == row["evaluation"]
                for c in row["context"]:
                    assert {k: c[k] for k in catalog[c["chunk_id"]]} == catalog[c["chunk_id"]]
                    assert c["knowledge_version_id"] in range(1, 8)
                for key in ("hits", "candidates"):
                    assert all(c["chunkId"] in catalog for c in row[key])
                assert all(cid in catalog for cid in row["omittedChunkIds"])
            metric = summarize(rows)
            assert metric == read(path.parent / "SUMMARY.json")["metrics"][method]
            key = f"{phase}-{method}"
            summaries[key], all_runs[key] = metric, rows
            table.append(
                f"| {phase} | {method} | {len(rows)} | "
                f"{metric['allSourceClauses']}/{metric['answerable']} | "
                f"{metric['allPolicies']}/{metric['answerable']} | "
                f"{metric['medianRetrievalMs']:.3f} | {metric['meanContextTokens']:.2f} |"
            )
            filename = f"{key}.md"
            links.append(
                f"- [{key} 전체 {len(rows)}건]({filename}) / "
                f"[원시 JSONL](runs/{phase}/{method}.jsonl)"
            )
            md = [
                f"# {key}: {len(rows)}건 전체 결과",
                "",
                "각 JSON은 순서가 있는 전체 후보·중간 순위·점수·평가·시간을 보존한다. "
                "context는 원문을 중복 인쇄하는 대신 "
                "[전체 청크](CHUNK-CATALOG.md)의 ID로 연결한다. "
                "원시 JSONL에는 반환 원문도 모두 들어 있다.",
                "",
            ]
            for row in rows:
                q = questions[row["id"]]
                compact = {k: v for k, v in row.items() if k != "context"}
                compact["contextReferences"] = [
                    {"chunkId": c["chunk_id"], "originHit": c["originHit"]} for c in row["context"]
                ]
                md.extend(
                    [
                        f"## {row['id']}",
                        "",
                        q["question"],
                        "",
                        "### 기대 근거·처리",
                        "",
                        block(
                            {
                                "expectedRoute": q["expectedRoute"],
                                "rationale": q["rationale"],
                                "gold": q["gold"],
                            }
                        ),
                        "",
                        "### 실제 검색 결과 전체",
                        "",
                        block(compact),
                        "",
                    ]
                )
                e = row["evaluation"]
                if not e["allSourceClauses"]:
                    failures.append(
                        {
                            "run": key,
                            "id": row["id"],
                            "question": q["question"],
                            "type": "MISSING_GOLD_CLAUSE"
                            if e["answerable"]
                            else "NON_POLICY_CANDIDATES_REQUIRE_ROUTING",
                            "missing": [c for c in e["checks"] if not c["sourceClauseHit"]],
                            "returnedPolicyIds": sorted(
                                {policy_id(c) or "NO_POLICY_ID" for c in row["context"]}
                            ),
                        }
                    )
            assert sum(line.startswith("## Q") for line in md) == len(rows)
            write(filename, md)
    assert sum(len(rows) for rows in all_runs.values()) == 1000
    selected = (
        all_runs[f"development-{selection['method']}"] + all_runs[f"final-{selection['method']}"]
    )
    selected.sort(key=lambda r: r["id"])
    assert len(selected) == len({r["id"] for r in selected}) == 300
    save(BENCH / "RESULTS-300.json", selected)
    combined = [
        "# 선정 방식 300문항 전체 기록",
        "",
        "개선용 200건과 최종용 100건은 평가 성격이 다르므로 합산 정확도로 주장하지 않는다.",
        "",
        "| ID | 구분 | 질문 | 기대 처리 | 원문 구절 전부 회수 | 상세 |",
        "|---|---|---|---|---|---|",
    ]
    for row in selected:
        q = questions[row["id"]]
        grade = str(row["evaluation"]["allSourceClauses"])
        combined.append(
            f"| {row['id']} | {row['split']} | {q['question'].replace('|', '/')} | "
            f"{q['expectedRoute']} | {grade} | "
            f"[결과]({row['split']}-{row['method']}.md#{row['id'].lower()}) |"
        )
    write("RESULTS-300.md", combined)
    save(BENCH / "FAILURES.json", failures)
    write(
        "FAILURES.md",
        [
            "# 누락 및 비정책 후보 반환 전체",
            "",
            "실험별 모든 건을 기록한다. 다른 정책 반환 자체가 오답이라는 판정은 아니다. "
            "비정책 질문은 라우터 미구현 진단이며 고객에게 틀린 답변을 보냈다는 의미가 아니다.",
            "",
            *[f"## {f['run']} / {f['id']}\n\n{block(f)}\n" for f in failures],
        ],
    )
    comparison = [
        "# 최종 100문항 기준선 대 선정 방식",
        "",
        "| ID | 질문 | R1 구절 | R4 구절 | R1 정책 | R4 정책 |",
        "|---|---|---|---|---|---|",
    ]
    baseline = {r["id"]: r for r in all_runs["final-R1"]}
    improved, regressed = [], []
    for row in all_runs["final-R4"]:
        previous = baseline[row["id"]]["evaluation"]
        current = row["evaluation"]
        if current["answerable"]:
            if current["allSourceClauses"] and not previous["allSourceClauses"]:
                improved.append(row["id"])
            if previous["allSourceClauses"] and not current["allSourceClauses"]:
                regressed.append(row["id"])
        comparison.append(
            f"| {row['id']} | {row['question'].replace('|', '/')} | "
            f"{previous['allSourceClauses']} | {current['allSourceClauses']} | "
            f"{previous['allPolicies']} | {current['allPolicies']} |"
        )
    write("FINAL-COMPARISON-100.md", comparison)
    covered = {g["policyId"] for q in questions.values() for g in q["gold"]}
    audit = {
        "questions": 300,
        "scenarioGroups": len(set.union(*groups.values())),
        "development": 200,
        "final": 100,
        "crossSplitGroups": 0,
        "policyIdsCovered": len(covered),
        "chunks": 146,
        "executionRows": 1000,
        "sourceHashesUnchanged": True,
        "goldQuotesMatchSourceLines": True,
        "contextsMatchOriginalChunks": True,
        "metricsRecomputedMatch": True,
        "developmentRunHashesUnchanged": True,
        "finalClauseImprovements": improved,
        "finalClauseRegressions": regressed,
        "failureRecords": len(failures),
        "categories": dict(Counter(q["category"] for q in questions.values())),
    }
    assert len(covered) == 70
    ambiguous = [
        {"id": q["id"], "question": q["question"], "split": q["split"], "gold": gold}
        for q in questions.values()
        for gold in q["gold"]
        if len(gold["sources"]) > 1
    ]
    save(BENCH / "GOLD-REVIEW.json", ambiguous)
    write(
        "GOLD-REVIEW.md",
        [
            "# 최종 정답 근거 재검수: 대체 원문 행이 여러 개인 항목 전체",
            "",
            "아래는 한 앵커에 여러 행이 매칭된 모든 항목이다. 동일 조건의 반복 설명일 수도 "
            "있어 자동 오류로 단정하지 않는다. 현재 점수는 이 중 하나를 포함하면 통과하므로 "
            "필수 입력·예외 조건을 놓칠 가능성이 있다. 조건별 필수 근거를 구분하는 업무 검수는 "
            "다음 데이터셋 버전에서 수행해야 한다. 이번 잠금 질문·점수는 소급 변경하지 않았다.",
            "",
            f"대상: {len(ambiguous)}개 문항-앵커, 고유 문항 {len({r['id'] for r in ambiguous})}개.",
            "",
            *[f"## {r['id']} / {r['gold']['policyId']}\n\n{block(r)}\n" for r in ambiguous],
        ],
    )
    audit["multiSourceGoldAnchors"] = len(ambiguous)
    save(BENCH / "AUDIT.json", audit)
    write(
        "METRICS.md",
        [
            "# 검색 비교 결과",
            "",
            *table,
            "",
            "구절 완전 회수는 지정한 원문 근거 행이 검색 문맥에 모두 존재하는지의 기계적 검사다. "
            "의미적 답변 정확도·조건 전체의 충분성·운영 성공률을 측정하지 않는다.",
            "",
            f"최종 구절 개선 {len(improved)}건, 악화 {len(regressed)}건. "
            "[모든 변화](FINAL-COMPARISON-100.md)에서 확인한다.",
        ],
    )
    write(
        "00-INDEX.md",
        [
            "# 챱챱 정책 검색 300문항 벤치마크",
            "",
            "원문 4개 → 발췌 7개 → 청크 146개 → 150시나리오/300문항 → 1000회 검색 기록.",
            "",
            "- [별도 최종 검수](FINAL-REVIEW.md)",
            "- [설계](01-DESIGN.md)",
            "- [공식 자료 리서치](02-RESEARCH.md)",
            "- [질문·정답 근거 300개](QUESTIONS-300.md)",
            "- [선정 방식 결과 300개](RESULTS-300.md)",
            "- [비교 지표](METRICS.md)",
            "- [최종 100개 전후 비교](FINAL-COMPARISON-100.md)",
            "- [실패·위험 진단 전체](FAILURES.md)",
            "- [청크 원문 전체](CHUNK-CATALOG.md)",
            "- [작업 이력·재현 명령](WORKLOG.md)",
            "- [자동 검수 결과](AUDIT.json)",
            "- [정답 근거 재검수의 주의 항목 전체](GOLD-REVIEW.md)",
            "- [파일 SHA-256](FILES-SHA256.json)",
            "",
            *links,
        ],
    )
    print(json.dumps(audit, ensure_ascii=False))


if __name__ == "__main__":
    main()
