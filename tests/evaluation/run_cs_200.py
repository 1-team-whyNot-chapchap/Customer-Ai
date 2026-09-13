"""Manual live-model evaluation. Only authored synthetic fixtures leave the process.

Run from Customer-Ai with PYTHONPATH set to the repo root. No business API or DB access.
"""

import argparse
import json
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import httpx

from chapchap_customer_ai.application.deepseek import DeepSeekComposer
from chapchap_customer_ai.consultation.models import Capability, StateAvailability, StateFact
from chapchap_customer_ai.consultation.plans import ConsultationPlans
from chapchap_customer_ai.core.settings import Settings
from chapchap_customer_ai.current_state.normalization import ToolResultNormalizer
from tests.consultation.test_conversation_quality import execute, turn
from tests.consultation.test_response_service import Dependencies, retrieved

ROOT = Path(__file__).resolve().parents[2]
POLICY = (
    "합성 평가용 정책이며 실제 서비스 정책이 아닙니다. "
    "환불 신청은 결제일로부터 7일 이내에 고객센터로 문의합니다. "
    "배송 요일은 신청 과정에서 선택합니다. 등록된 카드로 정기 결제합니다. "
    "결제 실패의 재시도 일정, 변경 조건, 취소 수수료, 배송비, 알레르기 지원, "
    "일시정지, 탈퇴 개인정보 처리, 가족 이용 조건은 이 문서에 명시하지 않았습니다."
)


class SyntheticState:
    def __init__(self, state):
        self.state = state
        self.calls = []

    def fetch(self, capabilities, *args, **kwargs):
        self.calls.extend(c.value for c in capabilities)
        normalizer = ToolResultNormalizer()
        result = []
        for cap in capabilities:
            if cap == Capability.SUBSCRIPTION_CURRENT:
                if self.state in {"NOT_FOUND", "TIMEOUT", "UNAVAILABLE"}:
                    result.append(StateFact(cap, StateAvailability(self.state)))
                    continue
                payload = {"availability": "AVAILABLE", "status": self.state}
            elif cap == Capability.PAYMENT_CURRENT:
                payload = dict(
                    availability="AVAILABLE",
                    status="SUCCESS",
                    paymentType="FIRST_SUBSCRIPTION_PAYMENT",
                    amount=15900,
                    occurredAt="2026-09-13T10:00:00+09:00",
                )
            elif cap == Capability.REFUND_RECENT:
                payload = dict(
                    availability="AVAILABLE",
                    status="PENDING",
                    refundType="CANCELLATION_BEFORE_START",
                    requestedAmount=15900,
                    refundedAmount=0,
                    unprocessedAmount=15900,
                    requestedAt="2026-09-13T11:00:00+09:00",
                    completedAt=None,
                )
            else:
                payload = dict(availability="AVAILABLE", status="DELIVERING", delayStatus="UNKNOWN")
            fact = normalizer.normalize(cap, payload)
            assert fact.error_code is None, (cap, payload)
            result.append(fact)
        return tuple(result)


class RecordingComposer:
    def __init__(self, composer):
        self.composer = composer
        self.interpretation = None
        self.draft = None
        self.errors = []

    def interpret(self, *args, **kwargs):
        try:
            self.interpretation = self.composer.interpret(*args, **kwargs)
            return self.interpretation
        except Exception as exc:
            self.errors.append("interpret:" + type(exc).__name__)
            raise

    def compose(self, *args, **kwargs):
        try:
            result = self.composer.compose(*args, **kwargs)
            self.draft = result.answer
            return result
        except Exception as exc:
            self.errors.append("compose:" + type(exc).__name__)
            raise

    def converse(self, *args, **kwargs):
        try:
            self.draft = self.composer.converse(*args, **kwargs)
            return self.draft
        except Exception as exc:
            self.errors.append("converse:" + type(exc).__name__)
            raise


def run_case(case, settings):
    started = time.monotonic()
    with httpx.Client() as client:
        composer = RecordingComposer(
            DeepSeekComposer(
                client,
                settings.deepseek_api_key,
                settings.deepseek_model,
                settings.deepseek_temperature,
                settings.deepseek_max_output_tokens,
            )
        )
        deps = Dependencies()
        deps.composer = composer
        deps.state = SyntheticState(case.get("state", "NOT_FOUND"))
        deps.retriever.values = (retrieved(POLICY),)
        history = [
            turn(i + 1, t["content"], t["sender"]) for i, t in enumerate(case.get("history", []))
        ]
        try:
            plan, response = execute(ConsultationPlans(deps.service()), case["question"], history)
            answer = response.answer or ""
            intent = (composer.interpretation or {}).get("intent", "BLOCKED")
            flags = []
            if intent not in case["intents"]:
                flags.append("intent")
            expected_reads = sorted(
                "CAP-" + topic + "-" + ("RECENT" if topic == "REFUND" else "CURRENT")
                for topic in case["reads"]
            )
            if sorted(deps.state.calls) != expected_reads:
                flags.append("reads")
            if response.handoff_required != case.get("handoff", False):
                flags.append("handoff")
            if "destination" in case:
                destination = (composer.interpretation or {}).get("destination")
                if destination != case["destination"] or "](" not in answer:
                    flags.append("destination")
            if (
                case.get("subject")
                and (composer.interpretation or {}).get("subject") != case["subject"]
            ):
                flags.append("subject")
            if re.search(
                r"챕챱|챕찹|챱찹|찹챱|CAP-|NOT_FOUND|CANCELED_BEFORE_START|컨텍스트|제공된 증거",
                answer,
            ):
                flags.append("wording")
            if re.search(r"(이메일|계정 정보|비밀번호|전화번호).*(알려|제공|입력)", answer):
                flags.append("identity-request")
            if re.search(r"(이동|열어).*(드릴게|드렸|했습니다)", answer):
                flags.append("false-action")
            return dict(
                **case,
                interpretation=composer.interpretation,
                answer=answer,
                decision=response.decision.value,
                actualHandoff=response.handoff_required,
                readsActual=deps.state.calls,
                retrievalCalls=deps.retriever.calls,
                draft=composer.draft,
                dependencyErrors=composer.errors,
                flags=flags,
                seconds=round(time.monotonic() - started, 2),
            )
        except Exception as exc:
            return dict(**case, flags=["runner-error"], error=type(exc).__name__)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--label", required=True)
    parser.add_argument("--ids", default="")
    parser.add_argument("--workers", type=int, default=3)
    args = parser.parse_args()
    cases = json.loads((ROOT / "tests/fixtures/cs_200_questions.json").read_text(encoding="utf-8"))
    if args.ids:
        ids = set(args.ids.split(","))
        cases = [c for c in cases if c["id"] in ids]
    settings = Settings()
    report = ROOT.parent / "reports" / f"cs-200-{args.label}.json"
    assert not report.exists(), "Preserve previous evaluation evidence; choose a new label"
    results = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(run_case, case, settings) for case in cases]
        for future in as_completed(futures):
            results.append(future.result())
            results.sort(key=lambda r: r["id"])
            report.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
            if len(results) % 20 == 0 or len(results) == len(cases):
                flagged = sum(bool(r["flags"]) for r in results)
                print(
                    f"{len(results)}/{len(cases)} done; flagged={flagged}",
                    flush=True,
                )
    print("Report:", report, flush=True)
