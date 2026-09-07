# 작업 기록 및 재현

## 순서와 변경 사유

1. 기존 `feature/policy-knowledge-corpus`에서 진행했다. 기준 dev는 `00ff6a66440098d7b420e43d532978cda705e89e`다. 원문 저장소 `chapchap-docs`의 기준은 `309746605697d5119aac7d5621a097632e9ee182`다. 이번 작업에서 commit/push/PR/merge는 수행하지 않았다.
2. 구현 전에 `01-DESIGN.md`와 로컬 `docs/work-plans/retrieval-benchmark-300-20260908.md`에 범위·방법·평가·기록 기준을 작성했다. 기존 발췌 7개와 146청크, 기존 Chroma를 보존하도록 정했다.
3. 공식 자료의 parent retrieval, BM25, RRF, retrieve/rerank를 조사했다. 출처와 채택 범위는 `02-RESEARCH.md`에 기록했다. 새 CrossEncoder 모델은 사용하지 않았다.
4. 취소·환불·할인·배송·계정·문의 등 150시나리오를 각각 두 표현으로 작성했다. 70개 발췌 정책을 모두 질문 근거로 포함하고, 답 없음·개인 상태·무관 질문 60개를 별도로 넣었다. 같은 시나리오는 동일 split에 두었다.
5. 원문 대조 중 앵커의 띄어쓰기/표현을 수정했다. `할인금액`→`할인 금액`, `연장`→`종료일을 뒤로 미루지 않는다`, 인원 범위→`1명부터 6명까지`, 변경 시각 질문→`보다 전이면 다음 날`/`부터면 다다음 날` 근거를 지정했다. **질문 근거 표시만 수정했으며 정책 원문은 수정하지 않았다.** 이 수정은 데이터셋 잠금 전에 수행했다.
6. `questions.json`의 SHA-256을 `DATASET-LOCK.json`에 고정했다. 이후 정답·질문·split은 변경하지 않았다. 질문 작성자는 최종용 질문도 작성/검수했으므로 독립된 사람의 블라인드 평가가 아니다.
7. 기존 임베딩을 별도 Chroma에 복사해 R1~R4를 개선용 200문항에 각각 실행했다. 800건 모두 검색 성공·디스크 기록 후 환경 집계에서 `ZoneInfoNotFoundError`가 발생했다. Windows 가상환경에 `tzdata`가 없었다. 검색은 재실행하지 않고 `recover_benchmark_summary.py`로 800행의 ID·해시·원문을 확인한 뒤 집계만 복구했다. 시각 처리는 현재 한국 시간 UTC+09:00의 고정 오프셋으로 수정했다. 최초 개발 실행의 모델 로드 시간·메모리 스냅샷은 복구할 수 없어 null로 남겼다.
8. 사전에 정한 원문 구절 회수→정책 회수→문맥 비용 순서로 R4를 선정하고 `SELECTION.json`에 고정했다. 최종 결과는 선정에 사용하지 않았다.
9. R5에서 최종 100문항에 R1/R4를 각각 한 번 실행했다. 200건 성공. 총 1000건의 검색 결과를 보존했다. 최종 점수 확인 후 검색 가중치·후보 수·질문을 재튜닝하지 않았다.
10. 검증된 엔진은 `src/chapchap_customer_ai/rag/local_policy_search.py`로 로컬 조회 명령에 연결했다. 실험 엔진은 해시 보존을 위해 그대로 남겼다. 실행 코드에는 후보가 없을 때 빈 `Chroma.get(ids=[])`를 호출하지 않는 방어 처리를 추가했다. 이 경우는 실험 1000건에서 발생하지 않았으며 별도 회귀 테스트로 확인했다. 운영 검색기 기본 설정은 교체하지 않았다.
11. 신규 회귀 12개 및 전체 348개 테스트를 통과했다. 기존 AnyIO 별칭 사용 중단 예정 경고 1개는 남아 있다. Ruff에서 발견한 줄 길이는 수정했다. 선택 방식으로 실제 로컬 조회를 실행한 원문 결과를 `LOCAL-QUERY-SMOKE.json`에 남겼다.
12. 전 실행의 판정을 재계산하고 원문 청크·정답 출처 줄·개발 실행 해시·그룹 분리·문항 수를 검사했다. 결과를 6개 실행별 Markdown/JSONL, 선정 방식 300개 결과, 최종 100개 전후 비교, 실패/진단 전체 384개, 별도 최종 검수 문서로 기록했다. 기록 봉인 시 파일 SHA-256을 생성한다.

## 재현 환경

- Python 3.12.14, sentence-transformers 3.4.1, transformers 4.57.6, torch 2.14.0, chromadb 1.5.9.
- 모델: `intfloat/multilingual-e5-small`, revision `614241f622f53c4eeff9890bdc4f31cfecc418b3`, 384차원 정규화 벡터. CPU 로컬 실행, 익명 공개 모델 캐시 이용, 오프라인 환경 변수 적용.
- 기존 Chroma: `reports/local-rag/84b0f725b562218a/chroma`, collection `local_policy_review_v1`.
- 별도 실험 Chroma: `reports/retrieval-benchmark-20260908/334a68cac24aee22/chroma`, collection `benchmark_policy_v1`.
- BM25의 제목+본문 토큰 카운팅 과정에서 526>512 경고가 출력된다. 해당 긴 문자열은 BM25 토큰화 대상이며 신경망에 입력하지 않는다. 본문 임베딩은 기존 146청크를 재사용했고 기존 최대 실제 입력은 509/512토큰이었다. 새 신경망 입력은 질문과 제목이다.
- 로컬 경로·캐시·가상환경은 별도 준비가 필요하다. JSONL/Markdown 결과를 읽는 데 모델이나 서버는 필요하지 않다. Customer 관리자 업로드, MinIO, 운영 DB, LLM 답변 생성은 실행하지 않았다.

## 명령 (Customer-Ai 폴더에서)

```powershell
.venv/Scripts/python.exe scripts/build_policy_corpus.py --check
.venv/Scripts/python.exe scripts/audit_policy_corpus.py
.venv/Scripts/python.exe scripts/build_retrieval_benchmark.py
.venv/Scripts/python.exe scripts/document_retrieval_benchmark.py
.venv/Scripts/python.exe scripts/query_policy_knowledge.py '첫 주문 할인은 얼마인가요?'
.venv/Scripts/python.exe scripts/query_policy_knowledge.py '첫 주문 할인은 얼마인가요?' --baseline
.venv/Scripts/python.exe -m pytest -q
.venv/Scripts/ruff.exe check src tests scripts
.venv/Scripts/python.exe scripts/seal_benchmark_report.py --check
```

새로운 별도 복사본에서 실험 결과 파일이 없는 경우에만 `run_retrieval_benchmark.py development` 후 `run_retrieval_benchmark.py final`을 실행한다. 기존 실행 결과가 있으면 덮어쓰지 않고 오류로 중단하도록 구현했다. 이번 실험 기록을 삭제해서 재실행하지 않는다. 집계 복구 스크립트도 SELECTION이 존재하면 중단한다.
