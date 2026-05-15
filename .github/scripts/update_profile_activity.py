#!/usr/bin/env python3
"""Update the auto-generated activity block in README.md.

This script updates the markdown block between:
<!-- AUTO:ACTIVITY_START -->
...
<!-- AUTO:ACTIVITY_END -->
"""

from __future__ import annotations

import datetime as dt
import json
import os
import re
import urllib.request
from pathlib import Path

README_PATH = Path("README.md")
START_MARKER = "<!-- AUTO:ACTIVITY_START -->"
END_MARKER = "<!-- AUTO:ACTIVITY_END -->"
USERNAME = os.getenv("PROFILE_USERNAME", "MatthewPaver")
MAX_REPOS = int(os.getenv("PROFILE_ACTIVITY_REPOS", "6"))


def fetch_json(url: str, token: str | None) -> list[dict] | dict:
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "profile-readme-updater",
        },
    )
    if token:
        req.add_header("Authorization", f"Bearer {token}")

    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def truncate(text: str, length: int = 88) -> str:
    text = (text or "").strip().replace("|", "\\|")
    if len(text) <= length:
        return text
    return text[: length - 1].rstrip() + "…"


def build_block(repos: list[dict]) -> str:
    now = dt.datetime.now(dt.UTC).strftime("%Y-%m-%d %H:%M")

    lines: list[str] = [
        START_MARKER,
        "## Latest Public Activity (Auto-Updated)",
        "",
        "_This section is automatically refreshed by GitHub Actions._",
        "",
        f"- Last refresh (UTC): {now}",
        "",
        "| Repo | Last push | What it is |",
        "|:---|:---:|:---|",
    ]

    if not repos:
        lines.append("| No public repositories found | - | - |")
    else:
        for repo in repos:
            name = repo.get("name", "unknown")
            url = repo.get("html_url", "")
            pushed = (repo.get("pushed_at") or "")[:10] or "-"
            desc = truncate(repo.get("description") or "No description")
            lines.append(f"| [{name}]({url}) | {pushed} | {desc} |")

    lines.extend(["", END_MARKER, ""])
    return "\n".join(lines)


def main() -> int:
    if not README_PATH.exists():
        raise FileNotFoundError("README.md not found")

    token = os.getenv("GITHUB_TOKEN")
    repo_api = (
        f"https://api.github.com/users/{USERNAME}/repos"
        "?per_page=100&type=owner&sort=pushed"
    )
    data = fetch_json(repo_api, token)
    if not isinstance(data, list):
        raise RuntimeError("Unexpected GitHub API response for repos list")

    public_non_fork = [
        r for r in data if not r.get("private", True) and not r.get("fork", False)
    ]
    public_non_fork.sort(key=lambda r: r.get("pushed_at") or "", reverse=True)
    top_repos = public_non_fork[:MAX_REPOS]

    block = build_block(top_repos)
    text = README_PATH.read_text(encoding="utf-8")

    pattern = re.compile(
        rf"{re.escape(START_MARKER)}[\s\S]*?{re.escape(END_MARKER)}",
        re.MULTILINE,
    )

    if START_MARKER in text and END_MARKER in text:
        updated = pattern.sub(block.strip(), text)
    else:
        anchor = "## Certifications"
        if anchor in text:
            updated = text.replace(anchor, block + "\n" + anchor)
        else:
            updated = text.rstrip() + "\n\n" + block

    README_PATH.write_text(updated + ("" if updated.endswith("\n") else "\n"), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
