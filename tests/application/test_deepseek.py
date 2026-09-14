import json

import httpx
import pytest
from pydantic import SecretStr

from chapchap_customer_ai.application.deepseek import DeepSeekComposer
from chapchap_customer_ai.consultation.models import (
    Capability,
    ConsultationDependencyError,
    StateAvailability,
    StateFact,
)
from chapchap_customer_ai.contracts.models import ConsultationSummaryMessage
from chapchap_customer_ai.rag.models import RagEvidence, RetrievedKnowledge
from chapchap_customer_ai.summary.models import SummaryComposerError

EVIDENCE = RetrievedKnowledge(
    "환불 기간은 7일입니다.",
    ("환불",),
    "refund",
    "REFUND",
    "1",
    "2026-09-07T00:00:00+09:00",
    RagEvidence(101, "chunk-1", 1, 0.9),
)


def completion(content, finish="stop"):
    return {
        "choices": [
            {
                "finish_reason": finish,
                "message": {
                    "role": "assistant",
                    "content": json.dumps(content, ensure_ascii=False),
                },
            }
        ]
    }


@pytest.mark.parametrize("availability", [StateAvailability.NOT_FOUND, StateAvailability.TIMEOUT])
def test_absence_grounding_never_conflates_failed_lookup(availability):
    data = []

    def handler(req):
        data.append(json.loads(json.loads(req.content)["messages"][1]["content"]))
        return httpx.Response(
            200, json=completion({"answer": "확인 결과예요.", "usedChunkIds": []})
        )

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        DeepSeekComposer(client, SecretStr("test-key")).compose(
            "구독 중인가요?",
            [],
            [],
            [StateFact(Capability.SUBSCRIPTION_CURRENT, availability)],
            timeout_seconds=1,
        )
    assert data[0]["service"] == "챱챱"
    fact = data[0]["stateFacts"][0]
    assert fact["availability"] == availability.value
    if availability == StateAvailability.NOT_FOUND:
        assert "조회 성공" in fact["safeAnswer"] and "정보 없음" in fact["safeAnswer"]
    else:
        assert fact["safeAnswer"] is None


def test_composer_uses_json_and_only_supplied_evidence():
    calls = []

    def handler(req):
        calls.append(req)
        return httpx.Response(
            200, json=completion({"answer": "7일입니다.", "usedChunkIds": ["chunk-1"]})
        )

    with httpx.Client(
        transport=httpx.MockTransport(handler),
        cookies={"private": "cookie"},
        auth=("wrong", "wrong"),
    ) as client:
        draft = DeepSeekComposer(client, SecretStr("test-key")).compose(
            "환불 정책", [], [EVIDENCE], [], timeout_seconds=1
        )
    assert draft.used_chunk_ids == ("chunk-1",)
    req = calls[0]
    assert str(req.url) == "https://api.deepseek.com/chat/completions"
    assert req.headers["authorization"] == "Bearer test-key" and "cookie" not in req.headers
    body = json.loads(req.content)
    assert body["response_format"] == {"type": "json_object"}
    assert body["thinking"] == {"type": "disabled"}
    assert "tools" not in body and body["stream"] is False
    assert "test-key" not in body["messages"][1]["content"]


def test_generated_brand_typo_is_corrected_before_customer_output():
    with httpx.Client(
        transport=httpx.MockTransport(
            lambda req: httpx.Response(
                200, json=completion({"answer": "챕챱의 내 정보 페이지예요."})
            )
        )
    ) as client:
        answer = DeepSeekComposer(client, SecretStr("test-key")).converse(
            "회원탈퇴는 어디서해요?",
            "NAVIGATION",
            "내 정보 보기",
            timeout_seconds=1,
        )
    assert answer == "챱챱의 내 정보 페이지예요."


@pytest.mark.parametrize(
    "data",
    [
        {"answer": "invented", "usedChunkIds": ["other"]},
        {"answer": "invented", "usedChunkIds": []},
        {"answer": "answer", "usedChunkIds": ["chunk-1", "chunk-1"]},
        {"answer": " ", "usedChunkIds": ["chunk-1"]},
        {"answer": "a" * 10001, "usedChunkIds": ["chunk-1"]},
        {"answer": "answer", "usedChunkIds": ["chunk-1"], "secret": "private"},
    ],
)
def test_invalid_or_forged_answer_is_rejected(data):
    with httpx.Client(
        transport=httpx.MockTransport(lambda req: httpx.Response(200, json=completion(data)))
    ) as client:
        with pytest.raises(ConsultationDependencyError) as error:
            DeepSeekComposer(client, SecretStr("private")).compose(
                "환불 정책", [], [EVIDENCE], [], timeout_seconds=1
            )
    assert "private" not in str(error.value)


@pytest.mark.parametrize("finish,status", [("length", 200), ("stop", 429), ("stop", 302)])
def test_truncated_or_failed_generation_is_not_a_summary(finish, status):
    with httpx.Client(
        transport=httpx.MockTransport(
            lambda req: httpx.Response(status, json=completion({"summary": "요약"}, finish))
        )
    ) as client:
        with pytest.raises(SummaryComposerError):
            DeepSeekComposer(client, SecretStr("test")).summarize([], timeout_seconds=1)


@pytest.mark.parametrize("length", [500, 501])
def test_summary_matches_customer_storage_limit(length):
    with httpx.Client(
        transport=httpx.MockTransport(
            lambda req: httpx.Response(200, json=completion({"summary": "가" * length}))
        )
    ) as client:
        composer = DeepSeekComposer(client, SecretStr("test"))
        messages = [ConsultationSummaryMessage(senderType="USER", content="환불 요청")]
        if length == 500:
            assert len(composer.summarize(messages, timeout_seconds=1).text) == 500
        else:
            with pytest.raises(SummaryComposerError):
                composer.summarize(messages, timeout_seconds=1)


def test_transport_timeout_preserves_safe_timeout_classification():
    def handler(req):
        raise httpx.ReadTimeout("private")

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        with pytest.raises(TimeoutError, match="deadline"):
            DeepSeekComposer(client, SecretStr("test")).summarize([], timeout_seconds=1)


def test_summary_limit_matches_java_utf16_length_for_emoji():
    with httpx.Client(
        transport=httpx.MockTransport(
            lambda req: httpx.Response(200, json=completion({"summary": "😀" * 251}))
        )
    ) as client:
        with pytest.raises(SummaryComposerError):
            DeepSeekComposer(client, SecretStr("test")).summarize([], timeout_seconds=1)


@pytest.mark.parametrize(
    "data",
    [
        {"answer": " "},
        {"answer": "가" * 301},
        {"answer": "안녕", "tool": "lookup"},
        {"answer": 123},
    ],
)
def test_dialogue_rejects_invalid_model_contract(data):
    with httpx.Client(
        transport=httpx.MockTransport(lambda req: httpx.Response(200, json=completion(data)))
    ) as client:
        with pytest.raises(ConsultationDependencyError):
            DeepSeekComposer(client, SecretStr("test")).converse(
                "안녕", "SMALL_TALK", "안녕하세요!", timeout_seconds=1
            )
