#!/usr/bin/env python3
"""Reconcile the main fix-4.4-fields-by-tag.md table with the extracted tag files.

For each row, compare the table's short description with the first paragraph of
the tag file's Description section (from OnixS). If the site version differs
meaningfully (longer/corrected), update the table cell — keeping it single-line
(markdown table cells cannot contain newlines or pipes).

Also verifies: every tag in the table has a file in tags/ and vice versa.
"""
import json
import os
import re
import sys

WORK = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(WORK)
MAIN = os.path.join(ROOT, "fix-4.4-fields-by-tag.md")
TAGS_DIR = os.path.join(ROOT, "tags")
SUMMARY = os.path.join(WORK, "summary.jsonl")

ROW = re.compile(r"^(\|\s*)(\d+)(\s*\|\s*)([^|]+?)(\s*\|\s*)(.*?)(\s*\|)\s*$")


def first_paragraph(tag: int) -> str:
    """First paragraph of the Description section of the extracted tag file."""
    for f in os.listdir(TAGS_DIR):
        if f.startswith(f"{tag}-") and f.endswith(".md"):
            with open(os.path.join(TAGS_DIR, f), encoding="utf-8") as fh:
                text = fh.read()
            m = re.search(r"## Description\n+(.*?)(?:\n\n|\Z)", text, re.S)
            if m:
                para = m.group(1).strip()
                # strip markdown links, keep text
                para = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", para)
                para = re.sub(r"[*~`]", "", para)
                return re.sub(r"\s+", " ", para)
    return ""


def main():
    check_only = "--check" in sys.argv

    with open(MAIN, encoding="utf-8") as f:
        lines = f.readlines()

    # coverage check
    table_tags = set()
    for line in lines:
        m = ROW.match(line)
        if m:
            table_tags.add(int(m.group(2)))
    file_tags = {int(f.split("-")[0]) for f in os.listdir(TAGS_DIR) if f.endswith(".md")}

    missing_files = sorted(table_tags - file_tags)
    orphan_files = sorted(file_tags - table_tags)
    print(f"table tags: {len(table_tags)}, file tags: {len(file_tags)}")
    if missing_files:
        print(f"MISSING FILES for tags: {missing_files}")
    if orphan_files:
        print(f"ORPHAN FILES (not in table): {orphan_files}")

    # description reconciliation
    changed = 0
    diffs = []
    out_lines = []
    for line in lines:
        m = ROW.match(line)
        if not m:
            out_lines.append(line)
            continue
        tag = int(m.group(2))
        table_desc = m.group(6).strip()
        site_desc = first_paragraph(tag)
        if site_desc and site_desc != table_desc and "|" not in site_desc:
            # normalize both: <N> vs (N) tag refs, whitespace, trailing period
            def norm(s):
                s = re.sub(r"\s+", " ", s).strip().rstrip(".")
                s = re.sub(r"<(\d+)>", r"(\1)", s)  # unify tag-ref style
                return s.lower()
            t_norm = norm(table_desc)
            s_norm = norm(site_desc)
            if t_norm != s_norm:
                # skip if table cell is substantially longer (richer) than the
                # site's first paragraph — don't regress content
                if len(t_norm) > len(s_norm) + 40:
                    out_lines.append(line)
                    continue
                diffs.append((tag, table_desc, site_desc))
                new_desc = site_desc if site_desc.endswith(".") else site_desc + "."
                line = f"{m.group(1)}{m.group(2)}{m.group(3)}{m.group(4)}{m.group(5)}{new_desc}{m.group(7)}\n"
                changed += 1
        out_lines.append(line)

    print(f"\ndescription diffs: {len(diffs)}")
    for tag, old, new in diffs[:15]:
        print(f"  tag {tag}:")
        print(f"    OLD: {old[:110]}")
        print(f"    NEW: {new[:110]}")
    if len(diffs) > 15:
        print(f"  ... and {len(diffs)-15} more")

    if not check_only and changed:
        with open(MAIN, "w", encoding="utf-8") as f:
            f.writelines(out_lines)
        print(f"\nWROTE {changed} updated rows to {os.path.basename(MAIN)}")
    elif check_only:
        print("\n(check only — main file not modified)")


if __name__ == "__main__":
    main()
