# chapchap-customer-ai

Customer-Service의 내부 Python/FastAPI AI Runtime이다. 정책 질문은 RAG, 개인 현재 상태는 승인된 Read-only MCP Capability로만 처리한다.

## 현재 초기 범위

- FastAPI App Factory와 health endpoint
- Customer-Service 인계 계약 DTO·Port 경계
- RAG/Vector Store/LLM/내부 인증의 구현 전 인터페이스

실제 Customer-Service 호출, 인증 검증, MinIO·Chroma·DeepSeek 연결은 Candidate 계약의 양쪽 Contract Test 이후에 활성화한다.

## 개발 준비

Python 3.11 이상이 필요하다. 이 PC에는 아직 실행 가능한 Python이 없으므로 설치 후 아래를 실행한다.

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
python -m pytest
uvicorn chapchap_customer_ai.main:create_app --factory --reload
```

실제 환경변수와 Credential은 저장소에 넣지 않는다. 필요한 설정 이름은 `.env.example`에만 둔다.
