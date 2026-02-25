#!/usr/bin/env python3
"""
Weekly auto-updater for mcp-library.

Fetches the latest MCP server entries from community sources:
  - punkpeye/awesome-mcp-servers
  - wong2/awesome-mcp-servers
  - modelcontextprotocol/servers (official)

Updates:
  - README.md LAST_UPDATED timestamp
  - CHANGELOG.md with newly discovered servers
  - scripts/known_servers.json (persistent dedup store)

Usage:
  python scripts/update_library.py
"""

import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SOURCES = {
    "punkpeye/awesome-mcp-servers": (
        "https://raw.githubusercontent.com/punkpeye/awesome-mcp-servers/main/README.md"
    ),
    "wong2/awesome-mcp-servers": (
        "https://raw.githubusercontent.com/wong2/awesome-mcp-servers/main/README.md"
    ),
    "modelcontextprotocol/servers": (
        "https://raw.githubusercontent.com/modelcontextprotocol/servers/main/README.md"
    ),
}

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
KNOWN_SERVERS_FILE = os.path.join(SCRIPT_DIR, "known_servers.json")
CHANGELOG_FILE = os.path.join(REPO_ROOT, "CHANGELOG.md")
README_FILE = os.path.join(REPO_ROOT, "README.md")

# Patterns that look like noise rather than real MCP server links
NOISE_PATTERNS = [
    "shield",
    "badge",
    "actions/",
    "issues/",
    "pulls/",
    "releases/",
    "commits/",
    "blob/",
    "tree/",
    "wiki/",
    "/LICENSE",
    "/CONTRIBUTING",
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def fetch_url(url: str) -> str | None:
    """Fetch a URL and return the text body, or None on failure.

    Tries urllib first, then falls back to curl for environments with
    SSL certificate issues (e.g. macOS without certifi installed).
    """
    import ssl
    import subprocess

    # Try urllib with default SSL context
    for ctx in [None, ssl.create_default_context()]:
        try:
            req = urllib.request.Request(
                url, headers={"User-Agent": "mcp-library-updater/2.0"}
            )
            kwargs: dict = {"timeout": 30}
            if ctx is not None:
                ctx.check_hostname = False
                ctx.verify_mode = ssl.CERT_NONE
                kwargs["context"] = ctx
            with urllib.request.urlopen(req, **kwargs) as resp:
                return resp.read().decode("utf-8")
        except Exception:  # noqa: BLE001
            continue

    # Fallback: curl (available on macOS and most Linux)
    try:
        result = subprocess.run(
            ["curl", "-s", "-L", "--max-time", "30", url],
            capture_output=True,
            text=True,
            timeout=35,
        )
        if result.returncode == 0 and result.stdout:
            return result.stdout
    except Exception as exc:  # noqa: BLE001
        print(f"  WARNING: curl fallback failed for {url}: {exc}", file=sys.stderr)

    print(f"  WARNING: all fetch methods failed for {url}", file=sys.stderr)
    return None


def extract_github_links(markdown: str) -> list[dict]:
    """
    Extract [name](github-url) pairs from markdown.
    Returns list of {"name": str, "url": str}.
    """
    pattern = r"\[([^\]]{4,80})\]\((https://github\.com/[^\)]{5,120})\)"
    results = []
    seen: set[str] = set()
    for match in re.finditer(pattern, markdown):
        name, url = match.group(1).strip(), match.group(2).strip()
        # Skip noisy links
        if any(noise in url for noise in NOISE_PATTERNS):
            continue
        # Skip duplicate URLs
        if url in seen:
            continue
        seen.add(url)
        results.append({"name": name, "url": url})
    return results


def load_known_servers() -> dict:
    try:
        with open(KNOWN_SERVERS_FILE) as fh:
            return json.load(fh)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"servers": [], "last_updated": ""}


def save_known_servers(data: dict) -> None:
    os.makedirs(os.path.dirname(KNOWN_SERVERS_FILE), exist_ok=True)
    with open(KNOWN_SERVERS_FILE, "w") as fh:
        json.dump(data, fh, indent=2)


def update_readme_timestamp(readme_path: str, timestamp: str) -> None:
    with open(readme_path) as fh:
        content = fh.read()
    updated = re.sub(
        r"<!-- LAST_UPDATED -->.*?<!-- /LAST_UPDATED -->",
        f"<!-- LAST_UPDATED -->{timestamp}<!-- /LAST_UPDATED -->",
        content,
    )
    with open(readme_path, "w") as fh:
        fh.write(updated)


def append_changelog(changelog_path: str, new_entries: list[dict], timestamp: str) -> None:
    cap = 30
    shown = new_entries[:cap]
    lines = "\n".join(f"- [{e['name']}]({e['url']})" for e in shown)
    extra = ""
    if len(new_entries) > cap:
        extra = f"\n\n_(and {len(new_entries) - cap} more — see known_servers.json)_"

    section = (
        f"\n## {timestamp}\n\n"
        f"### {len(new_entries)} New MCP Servers Discovered\n\n"
        f"{lines}{extra}\n"
    )

    try:
        with open(changelog_path) as fh:
            existing = fh.read()
    except FileNotFoundError:
        existing = "# MCP Library Changelog\n"

    # Insert new section right after the top-level heading
    if "## " in existing:
        insert_pos = existing.find("## ")
        updated = existing[:insert_pos] + section.lstrip("\n") + "\n" + existing[insert_pos:]
    else:
        updated = existing + section

    with open(changelog_path, "w") as fh:
        fh.write(updated)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    now = datetime.now(timezone.utc)
    timestamp = now.strftime("%Y-%m-%d")

    print(f"[{timestamp}] Starting MCP library update ...")

    known = load_known_servers()
    known_urls: set[str] = {s["url"] for s in known.get("servers", [])}

    all_entries: list[dict] = []
    for source_name, url in SOURCES.items():
        print(f"  Fetching {source_name} ...")
        content = fetch_url(url)
        if content:
            entries = extract_github_links(content)
            print(f"    → {len(entries)} GitHub links extracted")
            all_entries.extend(entries)
        else:
            print(f"    → skipped (fetch failed)")

    # Deduplicate across sources
    seen_urls: set[str] = set()
    unique_entries: list[dict] = []
    for entry in all_entries:
        if entry["url"] not in seen_urls:
            seen_urls.add(entry["url"])
            unique_entries.append(entry)

    # Identify truly new entries
    new_entries = [e for e in unique_entries if e["url"] not in known_urls]
    print(f"  Total unique entries: {len(unique_entries)}")
    print(f"  New entries:          {len(new_entries)}")

    # Merge and persist
    merged = {e["url"]: e for e in known.get("servers", [])}
    for entry in unique_entries:
        merged[entry["url"]] = entry

    known["servers"] = list(merged.values())
    known["last_updated"] = timestamp
    save_known_servers(known)
    print(f"  Saved {len(known['servers'])} total servers to known_servers.json")

    # Update README timestamp
    update_readme_timestamp(README_FILE, timestamp)
    print(f"  README.md LAST_UPDATED → {timestamp}")

    # Append changelog only if there's something new
    if new_entries:
        append_changelog(CHANGELOG_FILE, new_entries, timestamp)
        print(f"  CHANGELOG.md updated with {len(new_entries)} new entries")
    else:
        print("  No new entries — library is up to date, timestamp only updated")

    print("Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
