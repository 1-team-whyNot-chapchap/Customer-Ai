"""Approved customer entry points, verified against the client's router and prerequisites."""

from dataclasses import dataclass
from enum import StrEnum


class Destination(StrEnum):
    ADDRESSES = "ADDRESSES"
    PAYMENT_METHODS = "PAYMENT_METHODS"
    PROFILE = "PROFILE"
    SUBSCRIBE = "SUBSCRIBE"
    SUBSCRIPTION = "SUBSCRIPTION"
    PAYMENTS = "PAYMENTS"
    DELIVERIES = "DELIVERIES"


@dataclass(frozen=True)
class Page:
    label: str
    path: str
    guidance: str

    @property
    def link(self):
        return f"[{self.label}]({self.path})"


PAGES = {
    Destination.ADDRESSES: Page(
        "배송지 관리 보기",
        "/mypage/addresses",
        "배송지 관리 페이지에서 주소를 확인하고 새 배송지를 등록할 수 있어요.",
    ),
    Destination.PAYMENT_METHODS: Page(
        "결제수단 관리 보기",
        "/mypage/payment-methods",
        "결제수단 관리 페이지에서 등록한 카드를 확인하고 결제수단을 추가할 수 있어요.",
    ),
    Destination.PROFILE: Page(
        "내 정보 보기",
        "/mypage/profile",
        "내 정보 페이지에서 회원정보와 계정 이용 안내를 확인하실 수 있어요.",
    ),
    Destination.SUBSCRIBE: Page(
        "구독 상품 보기",
        "/plans",
        "구독하려면 먼저 상품을 선택해 주세요. 상품을 고른 뒤 구독 신청을 진행할 수 있어요.",
    ),
    Destination.SUBSCRIPTION: Page(
        "내 구독 보기",
        "/subscription",
        "내 구독 페이지에서 이용 정보를 확인하실 수 있어요.",
    ),
    Destination.PAYMENTS: Page(
        "결제 내역 보기",
        "/mypage/payments",
        "결제 내역 페이지에서 결제·환불 기록을 확인하실 수 있어요.",
    ),
    Destination.DELIVERIES: Page(
        "배송 내역 보기",
        "/mypage/deliveries",
        "배송 내역 페이지에서 기록을 확인하실 수 있어요.",
    ),
}
