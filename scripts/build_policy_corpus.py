"""Reproduce verbatim policy excerpts; keep editorial metadata outside upload files."""

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "knowledge" / "policy-corpus"


def digest(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def build(source_root: Path, check: bool) -> dict:
    selection = json.loads((CORPUS / "selection.json").read_text(encoding="utf-8"))
    sources = {}
    for name, expected_hash in selection["sources"].items():
        raw = (source_root / name).read_bytes()
        if digest(raw) != expected_hash:
            raise ValueError(f"Source changed; review selection again: {name}")
        sources[name] = raw.decode("utf-8-sig").splitlines(keepends=True)
    manifest = {"sourceCommit": selection["sourceCommit"], "documents": []}
    for doc in selection["documents"]:
        # Only original source spans plus blank separators. No generated policy wording.
        pieces = []
        spans = []
        for span in doc["spans"]:
            lines = sources[doc["source"]]
            start, end = span["start"], span["end"]
            if not 1 <= start <= end <= len(lines):
                raise ValueError(f"Invalid source range: {span}")
            original = "".join(lines[start - 1:end]).replace("\r\n", "\n").rstrip("\n")
            pieces.append(original)
            spans.append({**span, "sha256": digest(original.encode("utf-8"))})
        output = ("\n\n".join(pieces) + "\n").encode("utf-8")
        target = CORPUS / "upload" / doc["file"]
        if target.name != doc["file"] or target.suffix != ".md":
            raise ValueError("Output must be a Markdown basename")
        if check:
            if not target.is_file() or target.read_bytes() != output:
                raise ValueError(f"Excerpt differs from selected source: {target.name}")
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(output)
        manifest["documents"].append({
            "file": doc["file"], "source": doc["source"],
            "sha256": digest(output), "bytes": len(output), "spans": spans,
        })
    actual = {p.name for p in (CORPUS / "upload").iterdir() if p.is_file()}
    expected = {d["file"] for d in selection["documents"]}
    if actual != expected:
        raise ValueError("Unexpected/missing upload files")
    inventory = selection["policyInventory"]
    identifiers = [entry["id"] for entry in inventory]
    if len(identifiers) != len(set(identifiers)):
        raise ValueError("Duplicate policy inventory entries")
    for entry in inventory:
        if entry["decision"] not in {"included", "partial", "excluded", "hold"}:
            raise ValueError("Unreviewed policy")
        if not entry["reason"]:
            raise ValueError("Missing review reason")
    manifest["policyCounts"] = {
        status: sum(p["decision"] == status for p in inventory)
        for status in ("included", "partial", "excluded", "hold")
    }
    manifest_path = CORPUS / "manifest.json"
    serialized = json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"
    if check:
        if manifest_path.read_text(encoding="utf-8") != serialized:
            raise ValueError("Manifest differs from source and output")
    else:
        manifest_path.write_text(serialized, encoding="utf-8")
    return {"documents": len(expected), **manifest["policyCounts"], "result": "PASS"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, default=ROOT.parent / "chapchap-docs")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    print(json.dumps(build(args.source_root, args.check), ensure_ascii=False))
