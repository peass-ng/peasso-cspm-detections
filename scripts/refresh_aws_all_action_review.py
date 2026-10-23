#!/usr/bin/env python3
"""Index every pinned AWS attack-page heading against exact YAML event names.

This is a triage index, never a claim that a technique is detected or missing.
CloudTrail action names often differ from IAM names, and many headings are
background text rather than attack routes.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import subprocess

import yaml


ROOT = Path(__file__).resolve().parents[1]
SOURCE_COMMIT = "47c375ae496ae89f81936f47ab1cb84885c88373"
BASE = "src/pentesting-cloud/aws-security/"
CATEGORIES = (
    "aws-cross-account-attacks", "aws-persistence", "aws-post-exploitation",
    "aws-privilege-escalation", "aws-unauthenticated-enum-access",
)
REFERENCE = re.compile(
    r"https://github\.com/HackTricks-wiki/hacktricks-cloud/blob/[0-9a-f]{40}/"
    r"(src/pentesting-cloud/aws-security/[^#\s]+\.md)"
)
ACTION = re.compile(r"`([a-z0-9-]+):([A-Z][A-Za-z0-9]+)`")
HEADING = re.compile(r"^###\s+(.+)$", re.MULTILINE)


def git(repo: Path, *args: str) -> str:
    return subprocess.check_output(["git", "-C", str(repo), *args], text=True)


def render(source_repo: Path, rules_root: Path, source_commit: str = SOURCE_COMMIT) -> str:
    if not re.fullmatch(r"[0-9a-f]{40}", source_commit):
        raise ValueError("--source-commit must be a full lowercase Git SHA")
    paths = git(source_repo, "ls-tree", "-r", "--name-only", source_commit).splitlines()
    pages = sorted(
        path for path in paths
        if path.endswith(".md") and any(path.startswith(BASE + cat + "/") for cat in CATEGORIES)
    )
    refs: set[str] = set()
    names: set[str] = set()
    for rule in sorted(rules_root.rglob("*.yml")):
        text = rule.read_text(encoding="utf-8")
        refs.update(REFERENCE.findall(text))
        parsed = yaml.safe_load(text)
        selected = parsed["detection"]["selection"].get("event.name")
        if isinstance(selected, str):
            names.add(selected)
        elif isinstance(selected, list):
            names.update(item for item in selected if isinstance(item, str))
    rows: list[tuple[str, bool, int, int, int, int, list[tuple[int, str, str]]]] = []
    headings = exact = absent = manual = 0
    for path in pages:
        content = git(source_repo, "show", f"{source_commit}:{path}")
        local_headings = 0
        local_exact = 0
        local_absent = 0
        local_manual = 0
        candidates: list[tuple[int, str, str]] = []
        for match in HEADING.finditer(content):
            local_headings += 1
            text = match.group(1).strip()
            actions = ACTION.findall(text)
            if not actions:
                local_manual += 1
            for service, action in actions:
                if action in names:
                    local_exact += 1
                else:
                    local_absent += 1
                    candidates.append((content.count("\n", 0, match.start()) + 1,
                                       f"{service}:{action}", text))
        headings += local_headings
        exact += local_exact
        absent += local_absent
        manual += local_manual
        rows.append((path, path in refs, local_headings, local_exact,
                     local_absent, local_manual, candidates))
    direct = sum(row[1] for row in rows)
    output = [
        "# AWS attack-page action review queue",
        "",
        f"Pinned HackTricks Cloud source: `{source_commit}`. This lists **all** attack-page",
        "Markdown files in the five AWS attack categories, including pages that already",
        "have a rule reference. It is an index for further semantic review, not a count",
        "of attacks, tested techniques, or missing detectors. IAM actions can have a",
        "different CloudTrail event name, no standalone event, or an existing broader rule.",
        "An exact event-name match also does not prove detection of the described route.",
        "H3 headings can be setup or background, and attack routes may appear outside H3.",
        "",
        f"- Pages: **{len(rows)}**; direct YAML reference: **{direct}**; no direct reference: **{len(rows)-direct}**.",
        f"- H3 headings: **{headings}**; exact action-name mentions: **{exact}**;",
        f"  mentions without an exact YAML event name: **{absent}**; headings without",
        f"  a backticked `service:Action`: **{manual}**.",
        "",
        "The [work plan](WORK_PLAN.md) contains the full no-reference census and",
        "live-test receipts. The [high-heading review](AWS_COVERAGE_REVIEW.md) lists",
        "pages with at least three H3 headings and no direct YAML reference.",
        "",
        "## Page index",
        "",
        "| Source page | Direct YAML ref | H3 | Exact action name | No exact name | Manual H3 |",
        "| --- | :---: | ---: | ---: | ---: | ---: |",
    ]
    for path, referenced, local_headings, local_exact, local_absent, local_manual, _ in sorted(
        rows, key=lambda row: (row[1], -row[4], -row[5], row[0])
    ):
        url = f"https://github.com/HackTricks-wiki/hacktricks-cloud/blob/{source_commit}/{path}"
        output.append(
            f"| [{path}]({url}) | {'yes' if referenced else 'no'} | {local_headings} | "
            f"{local_exact} | {local_absent} | {local_manual} |"
        )
    output += ["", "## Action names without an exact YAML event name", "",
               "Each item needs manual review of the source paragraph, existing rule",
               "semantics, CloudTrail shape, service availability and live test evidence.", ""]
    for path, _, _, _, _, _, candidates in rows:
        if not candidates:
            continue
        output.append(f"### {path}")
        output.append("")
        for line, action, _ in candidates:
            url = f"https://github.com/HackTricks-wiki/hacktricks-cloud/blob/{source_commit}/{path}#L{line}"
            output.append(f"- [`{action}`]({url})")
        output.append("")
    return "\n".join(output).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-repo", type=Path, required=True)
    parser.add_argument("--source-commit", default=SOURCE_COMMIT)
    parser.add_argument("--rules-root", type=Path, default=ROOT / "rules" / "aws")
    parser.add_argument("--output", type=Path, default=ROOT / "AWS_ACTION_REVIEW_ALL.md")
    args = parser.parse_args()
    result = render(args.source_repo.resolve(), args.rules_root.resolve(), args.source_commit)
    args.output.write_text(result, encoding="utf-8")
    print(f"wrote={args.output} pages={result.count(chr(10) + '| [')}")


if __name__ == "__main__":
    main()
