"""Audit source coverage, exception retention and actual Markdown extraction."""

import json
import re
from pathlib import Path

from build_policy_corpus import CORPUS, ROOT, build

from chapchap_customer_ai.rag.extraction import TextDocumentExtractor

POLICY = re.compile(r"(?<![\w-])(?:AUTH-|CS-|DLV-)?POL-[A-Z]+-\d{3}")


def audit(source_root: Path) -> dict:
    summary = build(source_root, check=True)
    selection = json.loads((CORPUS / "selection.json").read_text(encoding="utf-8"))
    expected = set()
    for source in selection["sources"]:
        for number, line in enumerate(
            (source_root / source).read_text(encoding="utf-8-sig").splitlines(), 1
        ):
            if re.match(r"^#{1,3} ", line) and (match := POLICY.search(line)):
                expected.add((source, number, match.group()))
    classified = {(p["source"], p["line"], p["id"]) for p in selection["policyInventory"]}
    assert classified == expected, "Policy inventory missed a source heading"
    selected_ids = {
        span["policyId"] for doc in selection["documents"] for span in doc["spans"]
    }
    for entry in selection["policyInventory"]:
        assert (entry["id"] in selected_ids) == (entry["decision"] in {"included", "partial"})
    all_text = "\n".join(
        (CORPUS / "upload" / doc["file"]).read_text(encoding="utf-8")
        for doc in selection["documents"]
    )
    # Independently selected boundary facts, including omissions found during review.
    critical_fragments = [
        "기본 주소 문자열에 `대구`가 포함된 경우에만 배송 가능",
        "현재 정책에서 별도로 확정하지 않은 배송 후 분실·도난·변질",
        "같은 변경 적용일의 설정 변경이 연속으로 확정되면 가장 마지막에 확정된 설정만",
        "`14:00:00 KST`보다 이전에 서버가 취소 요청을 접수",
        "해당 구독에 `처리 중` 결제 거래가 하나라도 있으면 요청을 확정하지 않는다",
        "이미 결제되어 이용 중인 현재 이용 기간은 즉시 종료하거나 환불하지 않고",
        "과거 결제·환불 이력과의 관계는 유지한다",
        "다른 등록 수단을 현재 결제수단으로 선택한 뒤 이전 수단을 삭제",
        "부분 성공 이후의 추가 처리와 완료 기능은 현재 프로젝트 범위에 포함하지 않는다",
        "해당 주문에 포함된 모든 도시락을 함께 환불하며 일부 도시락만 나누어 환불하지 않는다",
        "현재 도시락 가격·현재 인원수·현재 구독 설정으로 환불금액을 다시 계산하지 않는다",
        "일요일과 대한민국의 공식 공휴일·대체공휴일에는 주문을 생성하지 않는다",
        "고객은 생성된 주문 한 건만 따로 취소하거나 환불받을 수 없으며",
        "배송 실패 회차는 재배송하지 않고 부분 환불한다",
        "해당 고객과 업무상 필요한 관리자만 조회한다",
        "고객 서명과 인증번호는 MVP에서 수집하지 않는다",
        "구체적인 보관 온도·허용시간·계절별 보냉 기준은 생산·포장·품질 검증 후",
        "Customer용 `DELIVERY_DELAYED` 알림 Event만으로는 환불하지 않는다",
        "내부 `failure_code`와 기사·관리자 메모는 고객에게 공개하지 않는다",
        "`OTHER`는 특정 주문·상품·배송과 직접 연결되지 않는 문의도 허용한다",
        "품질 문의 등록 자체가 환불·재배송·배송 변경·구독 상태 변경을 의미하지 않는다",
        "`PAYMENT_RETRY_STOPPED`, `SUBSCRIPTION_STATUS_CHANGED`는 고객 알림을 생성하지 않는다",
        "만 14세 미만이면 가입을 완료하지 않는다",
        "이메일 마케팅은 선택이며 거절해도 가입·로그인·핵심 서비스 이용을 제한하지 않는다",
        "새 마케팅 Version은 과거 동의를 자동 승계하지 않는다",
        "이메일·전화번호·이름이 같다는 이유로 계정을 자동 통합하지 않는다",
        "탈퇴 전 역할, 마케팅 동의, 대표 주소와 세션을 자동 복구하지 않는다",
        "유휴 만료가 남아 있어도 절대 만료를 넘을 수 없다",
        "기존 Access Token은 자체 만료까지 남을 수 있다",
    ]
    for text in critical_fragments:
        assert text in all_text, f"Missing critical source condition: {text}"
    assert "AUTH-POL-WD-003" not in selected_ids, "Conflicting withdrawal policy included"
    assert "AUTH-POL-SUB-002" not in selected_ids, "Conflicting subscription policy included"
    assert "DLV-POL-FAILURE-002" not in selected_ids, "Internal failure codes included"
    assert "7일 이내 환불" not in all_text, "Synthetic test policy leaked into corpus"
    documents = []
    for doc in selection["documents"]:
        raw = (CORPUS / "upload" / doc["file"]).read_bytes()
        parsed = TextDocumentExtractor().extract(raw, "text/markdown")
        assert parsed.sections
        for section in parsed.sections:
            identifiers = POLICY.findall(" / ".join(section.path))
            assert len(set(identifiers)) <= 1, "Sibling policy contamination in section path"
            if identifiers:
                assert "2. 핵심 용어" not in section.path, "Missing policy parent heading"
        assert raw.count(b"```") % 2 == 0, "Unclosed Markdown fence"
        assert len(raw) < 10 * 1024 * 1024
        if doc["file"] == "04-refunds.md":
            text = raw.decode("utf-8")
            assert text.index("가정식 플랜에서 월요일 1명") < text.index("앞의 월요일 1명")
        documents.append({"file": doc["file"], "sections": len(parsed.sections),
                          "bytes": len(raw)})
    return {**summary, "classifiedPolicies": len(expected),
            "criticalConditions": len(critical_fragments), "files": documents,
            "embeddingPerformed": False, "uploadPerformed": False}


if __name__ == "__main__":
    result = audit(ROOT.parent / "chapchap-docs")
    (CORPUS / "audit.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False))
