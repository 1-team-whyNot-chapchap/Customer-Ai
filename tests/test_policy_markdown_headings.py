from chapchap_customer_ai.rag.extraction import TextDocumentExtractor


def test_policy_headings_without_parent_do_not_accumulate_sibling_policies():
    document = TextDocumentExtractor().extract(
        "### POLICY-A\nA\n#### 예외\nA exception\n### POLICY-B\nB".encode(),
        "text/markdown",
    )
    assert [(section.path, section.text) for section in document.sections] == [
        (("POLICY-A",), "A"),
        (("POLICY-A", "예외"), "A exception"),
        (("POLICY-B",), "B"),
    ]


def test_heading_level_gaps_preserve_actual_ancestors_on_return():
    document = TextDocumentExtractor().extract(
        b"# Root\nintro\n### A\na\n##### Deep\nd\n## B\nb\n### C\nc",
        "text/markdown",
    )
    assert [section.path for section in document.sections] == [
        ("Root",), ("Root", "A"), ("Root", "A", "Deep"),
        ("Root", "B"), ("Root", "B", "C"),
    ]
