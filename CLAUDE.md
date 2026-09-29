# CLAUDE.md

Instructions for Claude Code in this repository.

## Project skills

This project's skills live in the [`.claude/skills/`](.claude/skills/) folder. Before performing browser tasks, read the corresponding skill:

- [`.claude/skills/browser-harness/SKILL.md`](.claude/skills/browser-harness/SKILL.md) — control a real browser via CDP (clicking, typing, navigation, logged-in sessions, JS-rendered or bot-protected pages). Do not use it for plain HTTP fetches of public content — use `curl` for those.

## About this repository

This repository is a **reference dictionary for the FIX (Financial Information Exchange) protocol, version 4.4**. Its main content is the [`README.md`](README.md) table — all 953 FIX 4.4 fields by tag number, with field names and descriptions — plus one detailed Markdown file per field under [`tags/`](tags/) (source: [OnixS FIX 4.4 field dictionary](https://www.onixs.biz/fix-dictionary/4.4/fields_by_tag.html)). When editing the documentation, keep it consistent with the official FIX 4.4 specification.
