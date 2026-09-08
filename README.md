# chapchap-customer-ai

Customer-Service의 내부 Python/FastAPI AI Runtime이다. 정책 질문은 RAG, 개인 현재 상태는 승인된 Read-only MCP Capability로만 처리한다.

## 구현 범위

- 인증된 상담 요청의 `knowledgeVersionIds`로 검색 범위를 제한한다. 누락/빈 목록은 전체 검색으로 대체하지 않는다.
- MinIO presigned URL 다운로드 → 추출·청킹 → E5/Chroma 저장 → 처리 결과 콜백을 연결한다.
- DeepSeek JSON 응답의 인용 ID·형식·길이를 검증한다. 상담 요약은 최대 500자다.
- Auth Service의 client_credentials 계약으로 콜백 토큰을 발급·캐시·갱신한다. 내부 요청은 Service JWT/Subject Assertion 검증을 거친다.
- Subscription 현재 결제·환불·구독 상태 HTTP 경계를 연결한다.
- Delivery의 customer-ai 전용 인증 계약에 맞춘 Consumer와 설정 기반 연결을 구현했다. URL/전용 키가 없으면 비활성이다.
- 운영 진단은 구조화 로그를 사용한다. Prometheus는 사용하지 않는다.

기본 앱은 health-only다. 운영 활성화는 Customer-Service gate 및 실제 의존성 검증과 별개다.

## 개발 준비

Python 3.11 이상이 필요하다.

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
python -m pytest
python -m ruff check src tests
python -m pip check
uvicorn chapchap_customer_ai.main:create_app --factory --host 127.0.0.1 --workers 1
```

실제 환경변수와 Credential은 저장소에 넣지 않는다. 설정 이름은 `config/provider-runtime.env.example`을 참고한다.

## 격리 Runtime

`CUSTOMER_AI_PROVIDER_RUNTIME_MODE=isolated`, `CUSTOMER_AI_ENVIRONMENT=local`, 내부 인증 활성화 및 필수 의존성 설정이 있어야 위 앱에 상담·지식처리·요약 API가 연결된다. 실제 RAG 실행에는 `.[rag]` 의존성, E5 모델과 Chroma 저장 경로가 필요하다. MinIO는 Customer가 발급한 presigned HTTPS URL과 허용 호스트만 사용한다. 설정된 앱의 실제 요청은 LLM 요금과 callback/Chroma 쓰기를 발생시킬 수 있다.

이 모드는 **단일 프로세스 검증용**이다. 메모리 멱등 레지스트리와 작업 큐는 재시작·다중 worker·콜백 장애 후 복구를 보장하지 않는다. production 환경은 거절한다. 운영에는 공유 멱등 저장소, 내구성 작업 큐/결과 재전송 및 실제 의존성 검증이 필요하다.

### Delivery 현재 상태

Delivery dev `1bfe49063e40b9067ff817165d27f13480bcd089`의 구현 계약을 기준으로 한다. Consumer 격리 검증은 완료했으나 실제 양쪽 서버 통합은 미검증이며 운영 활성화 승인이 아니다. Delivery 서버는 변경하지 않았다.

- 조회 전용 `GET /internal/deliveries/current`; query/body 없음.
- 고정 헤더: `X-Internal-Service: customer-ai`, `X-Internal-Scope: delivery.status.read`, `X-User-Role: CUSTOMER`.
- `X-User-Id`는 검증된 Customer Subject의 양의 int64만 사용한다. `X-Internal-Api-Key`는 Delivery 전용 키다.
- 성공: `{"code":"00","message":"SUCCESS","data":{"status":"DELIVERING","delayStatus":"UNKNOWN","statusChangedAt":null}}`.
- `404` + `DELIVERY_036` + null data만 업무상 부재로 처리한다. `409/DELIVERY_037`은 계약 오류, `401/403`은 권한 실패, `5xx`는 일시 불가로 구분한다.
- 자동 재시도와 리다이렉트는 없다. HTTP timeout은 남은 예산과 2초 중 작은 값이며, 늦게 수신된 응답은 TIMEOUT 처리한다. 동기 HTTP I/O의 단계별 timeout이므로 프로세스 수준의 강제 취소 보장은 아니다.

연결하려면 `CUSTOMER_AI_DELIVERY_CURRENT_STATE_BASE_URL`과 `CUSTOMER_AI_DELIVERY_CURRENT_STATE_API_KEY`를 함께 설정한다. 키는 Delivery의 `DELIVERY_CUSTOMER_AI_API_KEY`와 같아야 하며 Auth client secret과 별개다. 둘 다 미설정이면 UNAVAILABLE, 일부만 설정하면 격리 runtime 시작을 거부한다. 기본은 직접 HTTPS origin이며, 로컬 HTTP만 `CUSTOMER_AI_DELIVERY_CURRENT_STATE_ALLOW_LOOPBACK_HTTP=true`로 명시 허용할 수 있다. 실제 값은 Git에 저장하지 않는다.

자동 테스트는 외부 통신을 대체하여 JWT 검증부터 지식 처리·상담·요약 콜백까지 검증한다. 실제 Auth/JWKS/MinIO/Chroma/DeepSeek/Delivery 접속 성공을 의미하지 않는다.
