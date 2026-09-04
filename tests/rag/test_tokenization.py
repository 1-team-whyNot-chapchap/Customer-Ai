from chapchap_customer_ai.rag.tokenization import Qwen3EmbeddingTokenCounter


class FakeQwenTokenizer:
    def encode(self, text: str, *, add_special_tokens: bool) -> list[int]:
        token_count = len(text.split())
        return [0] * (token_count + int(add_special_tokens))


def test_qwen_token_counter_excludes_special_tokens() -> None:
    counter = Qwen3EmbeddingTokenCounter(FakeQwenTokenizer())

    assert counter.count("refund policy") == 2
