### CS-POL-RBAC-001 일반 사용자

`CUSTOMER`, `RIDER`는 다음 본인 데이터만 접근할 수 있다.

- 본인 상담
- 본인 품질 문의
- 본인 직접 수신 알림
- 공개 FAQ

다른 사용자의 상담·문의·직접 수신 알림 접근은 거부해야 한다. `MUST`

### CS-POL-CON-001 상담 상태

종료된 상담에서 추가 문의가 필요하면 기존 상담을 재개하지 않고 새로운 상담을 생성한다. `MUST`

### CS-POL-CON-002 관리자 자동 전환

다음 중 하나라도 해당하면 AI 단독 상담을 중단하고 `WAITING_ADMIN`으로 전환한다.

- 사용자가 관리자 연결을 명시적으로 요청
- RAG 검색 근거 부족
- 적용 가능한 활성 정책 Version 없음
- 정책 간 충돌
- 결제·환불·법적 분쟁·개인정보 등 고위험 판단 필요
- 동일 의도에서 반복적인 AI 실패
- 사용자 부정 반응 반복
- 해당 질문 처리에 필요한 DeepSeek API 장애·Timeout으로 안전한 답변이 불가능한 상태
- 해당 질문에 RAG 근거가 필수인데 Vector Store 장애로 안전한 근거를 구성할 수 없는 상태
- 질문에 필수적인 Current-State Tool이 `TIMEOUT`, `UNAVAILABLE`, `FORBIDDEN`, `CONTRACT_ERROR` 등으로 안전한 Fact를 제공하지 못하는 상태

단, 장애가 해당 질문의 필수 경로가 아니거나 검증된 Deterministic Fact만으로 안전한 답변이 가능한 경우에는 장애 자체만으로 관리자 전환하지 않을 수 있다.

AI는 위 상황에서 정책이나 실제 상태를 추측하여 답변해서는 안 된다. `MUST NOT`

### CS-POL-QI-001 문의 유형

```text
DAMAGED
MISSING
QUALITY
DELIVERY
OTHER
```

### CS-POL-QI-002 문의 상태

```text
RECEIVED
IN_PROGRESS
RESOLVED
CLOSED
```

허용 전이는 다음 정방향만 사용한다.

```text
RECEIVED → IN_PROGRESS
IN_PROGRESS → RESOLVED
RESOLVED → CLOSED
```

다음 전이는 허용하지 않는다.

```text
RECEIVED → RESOLVED
RECEIVED → CLOSED
IN_PROGRESS → CLOSED
RESOLVED → IN_PROGRESS
CLOSED → 모든 상태
```

- 단계 생략과 역방향 전이를 허용하지 않는다. `MUST NOT`
- `CLOSED` 이후 추가 처리가 필요하면 새로운 품질 문의를 생성한다. `MUST`
- 중복·오접수도 동일한 정방향 처리 흐름 안에서 사유를 기록한 뒤 종료한다.

### CS-POL-QI-003 실제 도메인 업무와 분리

- 품질 문의 등록 자체가 환불·재배송·배송 변경·구독 상태 변경을 의미하지 않는다. `MUST`
- Customer-Service가 다른 서비스 업무를 대신 실행하지 않는다. `MUST NOT`
- 필요한 실제 업무는 관리자 상담 또는 해당 도메인 서비스의 사용자 절차로 안내한다.

### CS-POL-QI-004 AI 사용

- AI는 문의 유형·Priority·요약 초안을 생성할 수 있다.
- 최종 문의 유형·Priority·관리자 답변은 관리자가 확인한다.
- AI 초안을 원본 도메인 업무 결과로 간주하지 않는다. `MUST NOT`

### CS-POL-QI-005 외부 ID

`orderId`, `productId`, `deliveryId`는 타 서비스가 소유한 논리 ID이며 품질 문의 유형에 따라 다음 조건을 적용한다.

| inquiry_type | orderId | productId | deliveryId |
|---|---|---|---|
| `DAMAGED` | 필수 | 필수 | 선택 |
| `MISSING` | 필수 | 필수 | 선택 |
| `QUALITY` | 필수 | 필수 | 선택 |
| `DELIVERY` | 필수 | 선택 | 필수 |
| `OTHER` | 선택 | 선택 | 선택 |

- `DAMAGED`, `MISSING`, `QUALITY`는 어느 주문의 어떤 상품에 대한 문제인지 식별할 수 있어야 한다. `MUST`
- `DELIVERY`는 어느 주문의 어느 배송 건에 대한 문제인지 식별할 수 있어야 한다. `MUST`
- `OTHER`는 특정 주문·상품·배송과 직접 연결되지 않는 문의도 허용한다. `MAY`

### CS-POL-NOTI-003 고객 알림 18종

기존 고객용 허용 알림 유형은 다음 **18종**이며 기존 Event 매핑을 유지한다.

| notification_type | 생성 조건·사용자 의미 |
|---|---|
| `FIRST_SUBSCRIPTION_PAYMENT_COMPLETED` | 첫 구독 결제 성공 |
| `REGULAR_PAYMENT_COMPLETED` | 정기결제 성공 |
| `SETTING_CHANGE_PAYMENT_COMPLETED` | 설정 변경 추가 결제 성공 |
| `REGULAR_PAYMENT_RETRY_WAITING` | 09시 정기결제 실패 후 13시 재시도 대기 |
| `REGULAR_PAYMENT_FINAL_FAILED` | 13시 정기결제 최종 실패 |
| `SETTING_CHANGE_PAYMENT_FAILED` | 설정 변경 추가 결제 실패 |
| `REFUND_COMPLETED` | 환불 완료 |
| `REFUND_FAILED` | 환불 실패 |
| `SUBSCRIPTION_SETTING_CHANGED` | 구독 설정 변경 실제 적용 |
| `SUBSCRIPTION_CANCELLATION_CONFIRMED` | 시작 전 취소 또는 다음 기간 해지 확정 |
| `SUBSCRIPTION_ENDED` | 실제 이용 구독 종료 |
| `DELIVERY_ADDRESS_CHANGED` | 배송지 변경 완료 |
| `DELIVERY_ADDRESS_CHANGE_REJECTED` | 배송지 수정·삭제 요청 거절 |
| `DELIVERY_CREATED` | 배송 생성·준비 |
| `DELIVERY_STARTED` | 배송 시작 |
| `DELIVERY_DELAYED` | 배송 지연 사실 |
| `DELIVERY_COMPLETED` | 배송 완료 |
| `DELIVERY_FAILED` | 배송 실패 |

`PAYMENT_RETRY_STOPPED`, `SUBSCRIPTION_STATUS_CHANGED`는 고객 알림을 생성하지 않는다.

### CS-POL-NOTI-007 읽음 상태

- CUSTOMER/RIDER 직접 알림은 해당 `recipient_user_id` 본인만 읽음 처리할 수 있다.

### CS-POL-FILE-003 파일 검증

업로드 용도별 허용 파일은 다음과 같이 제한한다.

#### 품질 문의 첨부파일

| 항목 | 정책 |
|---|---|
| 허용 확장자 | `.jpg`, `.jpeg`, `.png`, `.webp`, `.pdf` |
| 파일당 최대 크기 | `10MB` |
| 용도 | 파손·누락·품질·배송 문제 증빙 |

공통 검증 규칙:

- 확장자만으로 파일 유형을 판단하지 않는다. `MUST NOT`
- 확장자, `Content-Type`, 실제 File Signature를 함께 검증한다. `MUST`
- 허용된 문서·이미지는 정상적으로 Parsing 또는 Decoding 가능한지 확인한다. `MUST`
- 실행 파일, 압축 파일, 암호화 파일, HTML, SVG와 같은 Active Content는 허용하지 않는다. `MUST NOT`
