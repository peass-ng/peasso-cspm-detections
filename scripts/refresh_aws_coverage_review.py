#!/usr/bin/env python3
"""Refresh the direct-reference triage queue after AWS rule batches.

This only removes pages with an exact HackTricks URL in an AWS rule. It does
not claim that every attack on a referenced page is covered.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import re


PAGE = re.compile(
    r"https://github\.com/HackTricks-wiki/hacktricks-cloud/blob/[0-9a-f]{40}/"
    r"(src/pentesting-cloud/aws-security/[^#\s]+\.md)(?:#L\d+)?"
)
SECTION = re.compile(r"(?=^## \[)", re.MULTILINE)
TITLE = re.compile(r"^## \[([^]]+)\].*?\((\d+) headings\)", re.MULTILINE)
SUMMARY = re.compile(
    r"Pages with at least three level-three headings and no direct YAML reference: "
    r"\*\*\d+\*\*\. Total headings: \*\*\d+\*\*\."
)


def refresh(review: str, rule_texts: list[str]) -> tuple[str, list[str], int]:
    pages = {page for text in rule_texts for page in PAGE.findall(text)}
    parts = SECTION.split(review)
    if not parts or not SUMMARY.search(parts[0]):
        raise ValueError("Unexpected AWS coverage review header")
    kept, removed, headings = [], [], 0
    for part in parts[1:]:
        match = TITLE.match(part)
        if match is None:
            raise ValueError("Unexpected AWS coverage review section")
        page, count = match.group(1), int(match.group(2))
        if page in pages:
            removed.append(page)
        else:
            kept.append(part)
            headings += count
    intro = SUMMARY.sub(
        f"Pages with at least three level-three headings and no direct YAML reference: "
        f"**{len(kept)}**. Total headings: **{headings}**.", parts[0], count=1
    )
    return intro + "".join(kept), removed, headings


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    path = root / "AWS_COVERAGE_REVIEW.md"
    text, removed, headings = refresh(
        path.read_text(encoding="utf-8"),
        [item.read_text(encoding="utf-8") for item in sorted((root / "rules/aws").rglob("*.yml"))],
    )
    path.write_text(text, encoding="utf-8")
    print(f"pages_removed={len(removed)} remaining_pages={text.count(chr(10) + '## [')} remaining_headings={headings}")
    for page in removed:
        print(page)


if __name__ == "__main__":
    main()
