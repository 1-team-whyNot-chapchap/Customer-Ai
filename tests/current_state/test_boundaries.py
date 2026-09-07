from pathlib import Path


def test_current_state_runtime_has_no_direct_data_or_unconfirmed_http_adapter() -> None:
    source_root = Path("src/chapchap_customer_ai/current_state")
    source = "\n".join(
        path.read_text(encoding="utf-8") for path in sorted(source_root.glob("*.py"))
    ).lower()

    forbidden_dependencies = (
        "sqlalchemy",
        "pymysql",
        "sqlite3",
        "kafka",
        "requests",
        "boto3",
    )
    assert all(dependency not in source for dependency in forbidden_dependencies)
    assert "select *" not in source
    assert "insert into" not in source
    assert "update set" not in source
    # SUB-FN-018 confirms HTTP only at the Subscription boundary and its factory.
    for path in source_root.glob("*.py"):
        if path.name not in {"http.py", "runtime.py", "delivery_http.py"}:
            assert "httpx" not in path.read_text(encoding="utf-8")
