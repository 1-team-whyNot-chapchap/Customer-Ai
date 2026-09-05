from chapchap_customer_ai.rag.tokenization import MultilingualE5TokenCounter


class FakeE5Tokenizer:
    def encode(self, text: str, *, add_special_tokens: bool) -> list[int]:
        token_count = len(text.split())
        return [0] * (token_count + int(add_special_tokens))


def test_e5_token_counter_excludes_special_tokens() -> None:
    counter = MultilingualE5TokenCounter(FakeE5Tokenizer())

    assert counter.count("refund policy") == 2
