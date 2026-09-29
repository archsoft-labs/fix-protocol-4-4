#!/usr/bin/env python3
"""Orchestrate per-tag extraction: fetch tag page, parse, write markdown file.

Resumable: skips tags whose output file already exists.
Logs failures to .work/failures.txt for retry.
"""
import json
import os
import re
import subprocess
import sys
import time
import urllib.request

BASE = "https://www.onixs.biz/fix-dictionary/4.4"
WORK = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(WORK)
TAGS_FILE = os.path.join(WORK, "tags.txt")
HTML_DIR = os.path.join(WORK, "html")
OUT_DIR = os.path.join(ROOT, "tags")
FAIL_LOG = os.path.join(WORK, "failures.txt")
SUMMARY = os.path.join(WORK, "summary.jsonl")

os.makedirs(HTML_DIR, exist_ok=True)
os.makedirs(OUT_DIR, exist_ok=True)


def read_main_table():
    """tag -> (field_name, description) from the main md file."""
    rows = {}
    with open(os.path.join(ROOT, "fix-4.4-fields-by-tag.md"), encoding="utf-8") as f:
        for line in f:
            m = re.match(r"\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*(.*?)\s*\|\s*$", line)
            if m:
                rows[int(m.group(1))] = (m.group(2), m.group(3))
    return rows


def fetch(tag: int) -> str:
    path = os.path.join(HTML_DIR, f"tagNum_{tag}.html")
    if os.path.exists(path) and os.path.getsize(path) > 1000:
        return path
    url = f"{BASE}/tagNum_{tag}.html"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                data = r.read()
            if len(data) < 1000:
                raise ValueError(f"suspiciously small response: {len(data)} bytes")
            with open(path, "wb") as f:
                f.write(data)
            return path
        except Exception as e:
            if attempt == 2:
                raise
            time.sleep(2 * (attempt + 1))
    return path


def parse(tag: int, html_path: str):
    r = subprocess.run(
        [sys.executable, os.path.join(WORK, "extract_tag.py"), str(tag), html_path],
        capture_output=True, text=True, timeout=60,
    )
    if r.returncode != 0:
        raise RuntimeError(r.stderr.strip()[:500])
    head, sep, md = r.stdout.partition("\n===MD===\n")
    meta = json.loads(head.strip().splitlines()[-1])
    return meta, md


def slugify(name: str) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "-", name).strip("-")
    return s or "field"


def absolutize(md: str) -> str:
    """Rewrite relative OnixS links to absolute URLs so they work in the repo."""
    return re.sub(r"\]\((?!https?://|#)([^)]+)\)", rf"]({BASE}/\1)", md)


def main():
    tags = [int(t) for t in open(TAGS_FILE, encoding="utf-8").read().split()]
    table = read_main_table()
    only = [int(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else None

    done = failed = skipped = 0
    for i, tag in enumerate(tags):
        if only and tag not in only:
            continue
        field_name = table.get(tag, (None, None))[0]
        if field_name is None:
            with open(FAIL_LOG, "a", encoding="utf-8") as f:
                f.write(f"{tag}\tNOT-IN-MAIN-TABLE\n")
            failed += 1
            continue
        out_file = os.path.join(OUT_DIR, f"{tag}-{slugify(field_name)}.md")
        if os.path.exists(out_file) and os.path.getsize(out_file) > 200:
            skipped += 1
            continue
        try:
            html_path = fetch(tag)
            meta, md = parse(tag, html_path)
            md = absolutize(md)
            header = (
                f"> Source: [OnixS FIX 4.4 — tag {tag}]"
                f"({BASE}/tagNum_{tag}.html)\n\n"
            )
            with open(out_file, "w", encoding="utf-8") as f:
                f.write(header + md)
            with open(SUMMARY, "a", encoding="utf-8") as f:
                f.write(json.dumps({"tag": tag, "field": field_name, **meta}) + "\n")
            done += 1
            print(f"[{i+1}/{len(tags)}] tag {tag} {field_name} OK", flush=True)
        except Exception as e:
            with open(FAIL_LOG, "a", encoding="utf-8") as f:
                f.write(f"{tag}\t{type(e).__name__}: {e}\n")
            failed += 1
            print(f"[{i+1}/{len(tags)}] tag {tag} FAILED: {e}", flush=True)
        time.sleep(0.15)  # be polite

    print(f"\nDONE: {done} written, {skipped} already existed, {failed} failed")


if __name__ == "__main__":
    main()
