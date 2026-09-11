# 검색 보완 리서치 — 2026-09-08

원문 정책을 바꾸지 않고 검색·문맥 구성 방식만 비교한다. 아래 자료의 효과를 챱챱 성능으로 간주하지 않으며 실제 결과는 별도 측정한다.

| 방법 | 공식 근거 | 이번 비교에서 사용하는 방식 | 로컬 비용·한계 |
|---|---|---|---|
| 작은 청크 검색 후 큰 원문 문맥 반환 | [LangChain ParentDocumentRetriever](https://reference.langchain.com/python/langchain-classic/retrievers/parent_document_retriever/ParentDocumentRetriever) | 정책 ID·동일 지식 버전으로 본문/조건/예외 청크를 확장한다. | 추가 모델이 필요 없지만 문맥 길이가 증가한다. 최대 정책 3개·6000토큰 예산을 기록한다. |
| 의미 검색과 키워드 검색 결합 | [Microsoft RRF](https://learn.microsoft.com/en-us/azure/search/hybrid-search-ranking) | dense와 BM25 순위를 RRF 상수 60으로 합친다. 원점수 단위가 다르므로 그대로 더하지 않는다. | Azure 서비스를 설치하지 않는다. 순위 결합을 로컬에서 구현하고 각 원점수와 결합 점수를 별도로 보존한다. |
| BM25 | [Elastic similarity](https://www.elastic.co/docs/reference/elasticsearch/index-settings/similarity) | k1=1.2, b=0.75를 비교 시작값으로 고정한다. 한국어에는 기존 E5 tokenizer의 subword 토큰을 사용한다. | Elasticsearch와 같은 분석기·인덱스 구현이라는 뜻이 아니다. 한국어 조사·동의어 문제는 의미 검색과 함께 평가해야 한다. |
| 후보 재평가 | [Sentence Transformers Retrieve & Re-Rank](https://www.sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html) | 상위20 후보를 원문 제목 E5 유사도 0.3 + 본문 E5 유사도 0.7로 재정렬하는 경량 실험을 한다. | 공식 문서는 query/document를 함께 보는 CrossEncoder를 설명한다. 이번 제목 기반 bi-encoder 재평가는 CrossEncoder 실험이 아니다. 추가 모델 비용 없이 제목 효과를 먼저 분리한다. |
| 평가 데이터 구성 | [LangSmith 평가 안내](https://docs.langchain.com/langsmith/evaluate-chatbot-tutorial), [Ragas 평가 데이터 특성](https://docs.ragas.io/en/stable/concepts/test_data_generation/) | 질문·정답 근거·경계 사례를 정하고 변형을 그룹 단위로 나눈다. 최종100은 방식 선택 후에만 점수를 확인한다. | 300문항 자체가 품질 보증이 아니다. 이번 데이터는 작성한 합성 질문 150시나리오×2표현이며 실제 사용자 로그가 아니다. |

## 사전에 고정한 비교와 평가

- R1: 기존 본문 dense top5, cosine>=0.70.
- R2: 동일 R1 순위 + 원문 정책 확장.
- R3: dense/BM25 각20개 → RRF → 상위5 + 동일 확장.
- R4: R3 상위20 후보 → 제목/본문 유사도로 재정렬 → 상위5 + 동일 확장.
- R5: 개발200 결과로 선택을 고정한 후, 기준선과 선택 방식만 최종100에 실행한다.

R2와 R3/R4의 문맥 예산은 같게 둔다. R1은 원래 동작대로 상위5 원문만 사용한다. 따라서 R2의 개선은 순위 개선이 아니라 정책 문맥 확장 효과로 해석해야 한다. 실제 반환 청크 수·문맥 토큰 수·누락된 청크 ID를 함께 기록한다.

## 평가에서 과장하지 않을 부분

- 정책 ID 적중, 필수 구절 적중, 해당 원문 문장 전체 적중을 별도 기록한다. 모든 문장을 올바르게 이해한 AI 답변을 평가하는 것은 아니다.
- source 금액/정책 변경 없이 골드 근거를 추출한다. unsupported/current-state/out-of-scope 질문은 원문 근거만으로 답할 수 없다는 기대 처리를 기록한다.
- 검색 결과가 반환됐다는 사실만으로 답변을 생성했다고 표현하지 않는다. 이 실험에는 질문 라우터·LLM 생성기가 없으므로 실제 거절 정확도는 측정하지 못한다. 대신 비정책 질문에 반환된 점수와 근거를 기록한다.
- 임베딩은 CPU 로컬 계산이다. 문서 제목 임베딩 준비 시간, query 임베딩 시간과 검색·문맥 구성 시간을 구분한다. 메모리는 측정 가능한 프로세스 RSS/peak를 기록하고 서버 동시 부하 성능으로 해석하지 않는다.
- 전체 300개 중 개선용 200개를 반복 사용하므로 개선용 수치는 선택 편향이 있다. 최종100 결과를 별도로 보고하며 이후 같은100을 다시 튜닝하면 새 평가 세트가 필요하다.

## 질문 사전 검수 기록

원문 매칭 검사에서 `POL-SUBSCRIPTION-005`의 “연장”과 `POL-PAYMENT-009`의 “할인금액”이 실제 발췌 문자열과 다름을 발견했다. 원문은 그대로 두고 평가 앵커를 각각 “종료일을 뒤로 미루지 않는다”, “할인 금액”으로 수정했다. 단독 숫자 `6`·`14`는 날짜와 우연히 일치할 수 있어 인원 범위와 마감 전/후 두 조항으로 구체화했다. 이 수정은 최초 데이터 해시 고정 및 검색 실험 전에 수행했다.
