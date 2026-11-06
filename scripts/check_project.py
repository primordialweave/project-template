#!/usr/bin/env python3
"""Minimal dependency-free health check for the starter template.

This validates repository structure and relative Markdown links only.
It is not a substitute for real application tests, security scanning, or a build.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = (
    "README.md",
    "README.zh-CN.md",
    "PROJECT-SETUP.md",
    "LICENSE-CHOICE.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "docs/GETTING_STARTED.md",
    "docs/ARCHITECTURE.md",
    "docs/RELEASING.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/ISSUE_TEMPLATE/bug_report.yml",
    ".github/ISSUE_TEMPLATE/feature_request.yml",
    ".github/ISSUE_TEMPLATE/documentation.yml",
    ".github/workflows/quality.yml",
)
LINK = re.compile(r"\[[^]]*\]\(([^)]+)\)")


def issues() -> list[str]:
    errors: list[str] = []
    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            errors.append(f"Missing required file: {rel}")
    for md in ROOT.rglob("*.md"):
        if any(part in {".git", ".venv", "node_modules"} for part in md.parts):
            continue
        content = md.read_text(encoding="utf-8")
        for value in LINK.findall(content):
            dest = value.split("#", 1)[0].strip()
            if not dest or dest.startswith(("http://", "https://", "mailto:", "data:")):
                continue
            dest = unquote(dest)
            if not (md.parent / dest).exists():
                errors.append(f"{md.relative_to(ROOT)}: missing link target {dest}")
    return errors


def main() -> int:
    errors = issues()
    if errors:
        for error in errors:
            print("ERROR:", error, file=sys.stderr)
        return 1
    print(f"Starter structure and local Markdown links are valid ({len(REQUIRED)} required files).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
