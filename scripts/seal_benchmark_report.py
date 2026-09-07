"""Seal or verify benchmark artifacts and their executable source hashes."""

import argparse
import json

from build_policy_corpus import ROOT
from build_retrieval_benchmark import BENCH
from run_retrieval_benchmark import digest, save


def main(check=False):
    target = BENCH / "FILES-SHA256.json"
    paths = [p for p in BENCH.rglob("*") if p.is_file() and p != target]
    paths += list((ROOT / "scripts").glob("*.py"))
    paths += [
        ROOT / name
        for name in (
            "src/chapchap_customer_ai/rag/local_policy_search.py",
            "src/chapchap_customer_ai/rag/extraction.py",
            "tests/test_local_policy_search.py",
            "tests/test_policy_markdown_headings.py",
            "pyproject.toml",
        )
    ]
    actual = {p.relative_to(ROOT).as_posix(): digest(p) for p in sorted(set(paths))}
    if check:
        expected = json.loads(target.read_text(encoding="utf-8"))
        assert actual == expected["files"], "Files changed or were added/removed after sealing"
    else:
        assert not target.exists(), "Existing seal cannot be silently replaced"
        save(
            target,
            {"algorithm": "SHA-256", "pathBase": "Customer-Ai repository root", "files": actual},
        )
    print(
        json.dumps({"mode": "verify" if check else "seal", "files": len(actual), "status": "PASS"})
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    main(parser.parse_args().check)
