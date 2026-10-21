#!/usr/bin/env python3
"""Append or refresh the AWS attack-page census inside WORK_PLAN.md.

This is a source triage queue, not a claim that a page is undetected.
Run with a local clone containing the pinned HackTricks Cloud commit.
"""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
import re
import subprocess


SOURCE_COMMIT = "47c375ae496ae89f81936f47ab1cb84885c88373"
START = "<!-- AWS_ATTACK_PAGE_CENSUS_START -->"
END = "<!-- AWS_ATTACK_PAGE_CENSUS_END -->"
CATEGORIES = (
    "aws-cross-account-attacks",
    "aws-persistence",
    "aws-post-exploitation",
    "aws-privilege-escalation",
    "aws-unauthenticated-enum-access",
)
BASE = "src/pentesting-cloud/aws-security/"
REFERENCE = re.compile(
    r"https://github\.com/HackTricks-wiki/hacktricks-cloud/blob/[0-9a-f]{40}/"
    r"(src/pentesting-cloud/aws-security/[^#\s]+\.md)"
)


def git(repo: Path, *args: str) -> str:
    return subprocess.check_output(["git", "-C", str(repo), *args], text=True)


def render(source_repo: Path, rules_root: Path) -> str:
    paths = git(source_repo, "ls-tree", "-r", "--name-only", SOURCE_COMMIT).splitlines()
    attack_pages = sorted(
        path for path in paths
        if path.endswith(".md") and any(path.startswith(BASE + cat + "/") for cat in CATEGORIES)
    )
    references = {
        path for rule in sorted(rules_root.rglob("*.yml"))
        for path in REFERENCE.findall(rule.read_text(encoding="utf-8"))
    }
    counts: dict[str, Counter[str]] = {cat: Counter() for cat in CATEGORIES}
    unreferenced: list[tuple[str, int, int]] = []
    for path in attack_pages:
        category = path[len(BASE):].split("/", 1)[0]
        counts[category]["all"] += 1
        if path in references:
            counts[category]["referenced"] += 1
            continue
        content = git(source_repo, "show", f"{SOURCE_COMMIT}:{path}")
        h2 = len(re.findall(r"^##\s+", content, re.MULTILINE))
        h3 = len(re.findall(r"^###\s+", content, re.MULTILINE))
        counts[category]["unreferenced"] += 1
        counts[category]["h3_3plus" if h3 >= 3 else "h3_1or2" if h3 else "no_h3"] += 1
        unreferenced.append((path, h2, h3))
    output = [
        "# AWS attack-page source census",
        "",
        f"Pinned HackTricks Cloud source: `{SOURCE_COMMIT}`. This covers all Markdown pages under",
        "`aws-cross-account-attacks`, `aws-persistence`, `aws-post-exploitation`,",
        "`aws-privilege-escalation` and `aws-unauthenticated-enum-access`.",
        "A missing direct YAML URL is a **triage signal**, not proof that a technique lacks",
        "a detection. A direct URL also does not establish that every technique on that page",
        "is covered. H2/H3 counts include navigation and explanatory headings.",
        "Service enumeration and basic-information pages are outside this census and need",
        "separate review for embedded attack routes.",
        "",
        "| Category | Source pages | With direct YAML reference | No reference: ≥3 H3 | No reference: 1–2 H3 | No reference: 0 H3 |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for cat in CATEGORIES:
        x = counts[cat]
        output.append(f"| `{cat}` | {x['all']} | {x['referenced']} | {x['h3_3plus']} | {x['h3_1or2']} | {x['no_h3']} |")
    output.append(f"| **Total** | **{len(attack_pages)}** | **{sum(x['referenced'] for x in counts.values())}** | **{sum(x['h3_3plus'] for x in counts.values())}** | **{sum(x['h3_1or2'] for x in counts.values())}** | **{sum(x['no_h3'] for x in counts.values())}** |")
    output += ["", "## Pages requiring semantic review", "",
               "The page path links to the pinned source. Review each technique and test evidence before",
               "marking it covered, blocked or not observable in CloudTrail.", "",
               "| Source page | H2 | H3 |", "| --- | ---: | ---: |"]
    for path, h2, h3 in unreferenced:
        url = f"https://github.com/HackTricks-wiki/hacktricks-cloud/blob/{SOURCE_COMMIT}/{path}"
        output.append(f"| [{path}]({url}) | {h2} | {h3} |")
    return "\n".join(output) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-repo", type=Path, required=True)
    parser.add_argument("--rules-root", type=Path, default=Path(__file__).resolve().parents[1] / "rules" / "aws")
    parser.add_argument("--plan", type=Path, default=Path(__file__).resolve().parents[1] / "WORK_PLAN.md")
    args = parser.parse_args()
    result = render(args.source_repo.resolve(), args.rules_root.resolve())
    plan = args.plan.read_text(encoding="utf-8")
    if START in plan or END in plan:
        if plan.count(START) != 1 or plan.count(END) != 1:
            raise ValueError("Malformed AWS census markers")
        before, rest = plan.split(START, 1)
        _, after = rest.split(END, 1)
        plan = before.rstrip() + "\n\n" + START + "\n" + result + END + after
    else:
        plan = plan.rstrip() + "\n\n" + START + "\n" + result + END + "\n"
    args.plan.write_text(plan, encoding="utf-8")
    print(f"source_census_rows={result.count(chr(10) + '| [')}")


if __name__ == "__main__":
    main()
