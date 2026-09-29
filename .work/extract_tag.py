#!/usr/bin/env python3
"""Convert an OnixS FIX 4.4 tag page (raw HTML) to a clean Markdown fragment.

Usage: extract_tag.py <tag> <html_file>
Prints a JSON header line, then '===MD===', then the markdown.
"""
import json
import re
import sys
from html.parser import HTMLParser


CONTENT_START = re.compile(r'<section class="rich-text-module fix-dictionary">')
CONTENT_END = re.compile(r'</section>')


def slice_content(raw: str) -> str:
    m = CONTENT_START.search(raw)
    if not m:
        raise ValueError("content section not found")
    rest = raw[m.start():]
    e = CONTENT_END.search(rest)
    if not e:
        raise ValueError("content section end not found")
    return rest[: e.end()]


class Node:
    __slots__ = ("tag", "attrs", "children", "text")

    def __init__(self, tag, attrs):
        self.tag = tag
        self.attrs = attrs
        self.children = []
        self.text = ""


class TreeBuilder(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("root", {})
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        n = Node(tag, dict(attrs))
        self.stack[-1].children.append(n)
        if tag not in ("br", "img", "hr", "meta", "link"):
            self.stack.append(n)
        else:
            if tag == "br":
                n.text = "\n"
                self.stack[-1].children.append(Node("#text", {}))
                self.stack[-1].children[-1].text = "\n"

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        # pop until matching
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                return

    def handle_data(self, data):
        n = Node("#text", {})
        n.text = data
        self.stack[-1].children.append(n)


def node_text(n) -> str:
    out = []
    def walk(x):
        if x.tag == "#text":
            out.append(x.text)
        elif x.tag == "br":
            out.append("\n")
        else:
            for c in x.children:
                walk(c)
    walk(n)
    return re.sub(r"[ \t]*\n[ \t]*", "\n", "".join(out)).strip()


def node_md(n, base_href="") -> str:
    """Render a node to markdown (inline links preserved)."""
    out = []

    def walk(x, buf):
        if x.tag == "#text":
            buf.append(x.text)
        elif x.tag == "br":
            buf.append("\n")
        elif x.tag == "a":
            inner = []
            for c in x.children:
                walk(c, inner)
            t = re.sub(r"\s+", " ", "".join(inner)).strip()
            href = x.attrs.get("href", "")
            if t and href and not href.startswith("#"):
                buf.append(f"[{t}]({href})")
            elif t:
                buf.append(t)
        elif x.tag in ("b", "strong"):
            inner = []
            for c in x.children:
                walk(c, inner)
            t = "".join(inner).strip()
            if t:
                buf.append(f"**{t}**")
        elif x.tag == "del":
            inner = []
            for c in x.children:
                walk(c, inner)
            t = "".join(inner).strip()
            if t:
                buf.append(f"~~{t}~~")
        else:
            for c in x.children:
                walk(c, buf)

    walk(n, out)
    return "".join(out)


def find_first(n, tag):
    if n.tag == tag:
        return n
    for c in n.children:
        r = find_first(c, tag)
        if r is not None:
            return r
    return None


def find_all(n, tag, acc):
    if n.tag == tag:
        acc.append(n)
    for c in n.children:
        find_all(c, tag, acc)


def is_breadcrumb_link(n) -> bool:
    """True for <a> inside td.listLinks (the nav row)."""
    return False  # handled by ancestor check below


def in_nav_table(n, ancestors) -> bool:
    for a in ancestors:
        if a.tag == "td" and "listLinks" in a.attrs.get("class", ""):
            return True
    return False


def extract(html_raw: str):
    content = slice_content(html_raw)
    tb = TreeBuilder()
    tb.feed(content)
    root = tb.root

    # locate the top <td valign="top"> container: everything interesting is inside
    # h2 title
    h2s = []
    find_all(root, "h2", h2s)
    title = re.sub(r"\s+", " ", node_text(h2s[0])) if h2s else None

    # field type: paragraph starting with 'Type:'
    ps = []
    find_all(root, "p", ps)
    field_type = None
    for p in ps:
        t = node_text(p)
        if t.lower().startswith("type:"):
            # keep markdown links (e.g. char -> index.html#char)
            md = node_md(p)
            field_type = re.sub(r"^type:\s*", "", md, flags=re.I).strip()
            break

    # h3 sections
    h3s = []
    find_all(root, "h3", h3s)

    description_nodes = []
    used_in_links = []

    for h3 in h3s:
        label = node_text(h3).lower()
        # walk following siblings of h3's parent chain: h3 sits inside td; we take
        # subsequent siblings of the h3 element itself (they are at the same level)
        # In this markup h3 is a child of the same td as the following <p>/<ul>.
        # So: find h3's parent, iterate children after h3.
        parent = None
        # find parent
        def find_parent(n, target, par=None):
            nonlocal parent
            if n is target:
                parent = par
                return True
            for c in n.children:
                if find_parent(c, target, n):
                    return True
            return False
        find_parent(root, h3)
        if parent is None:
            continue
        idx = parent.children.index(h3)
        siblings = parent.children[idx + 1:]

        if "description" in label:
            # stop at next h3
            for s in siblings:
                if s.tag == "h3":
                    break
                if s.tag == "a" and not s.children and not s.text:
                    continue  # named anchor
                description_nodes.append(s)
        elif "used in" in label:
            for s in siblings:
                if s.tag == "h3":
                    break
                if s.tag == "ul":
                    for li in s.children:
                        if li.tag != "li":
                            continue
                        a = find_first(li, "a")
                        if a is not None:
                            t = re.sub(r"\s+", " ", node_text(a))
                            used_in_links.append((t, a.attrs.get("href")))
                        else:
                            t = re.sub(r"\s+", " ", node_text(li))
                            if t:
                                used_in_links.append((t, None))

    return title, field_type, description_nodes, used_in_links


def to_markdown(title, field_type, desc_nodes, used_in) -> str:
    out = []
    if title:
        out.append("# " + title)
    if field_type:
        out.append(f"\n**Type:** {field_type}")

    desc_md = []
    for n in desc_nodes:
        if n.tag == "p":
            t = node_md(n).strip()
            if t:
                # normalize wrapped lines: collapse newline+indent into a space
                t = re.sub(r"\n[ \t]+", " ", t)
                desc_md.append(re.sub(r"\n{3,}", "\n\n", t).strip())
        elif n.tag == "ul":
            for li in n.children:
                if li.tag == "li":
                    t = node_md(li).strip()
                    if t:
                        desc_md.append("- " + t)
        elif n.tag == "#text":
            t = n.text.strip()
            if t:
                desc_md.append(t)
    if desc_md:
        out.append("\n## Description\n")
        out.append("\n\n".join(desc_md))

    if used_in:
        out.append("\n## Used In\n")
        seen = set()
        for t, h in used_in:
            key = (t, h)
            if key in seen or not t:
                continue
            seen.add(key)
            out.append(f"- [{t}]({h})" if h else f"- {t}")
    return "\n".join(out).strip() + "\n"


def main():
    tag, html_file = sys.argv[1], sys.argv[2]
    with open(html_file, encoding="utf-8", errors="replace") as f:
        raw = f.read()
    title, field_type, desc_nodes, used_in = extract(raw)
    md = to_markdown(title, field_type, desc_nodes, used_in)
    print(json.dumps({
        "tag": tag,
        "title": title,
        "type": field_type,
        "desc_blocks": len(desc_nodes),
        "used_in": len(used_in),
    }))
    print("===MD===")
    print(md)


if __name__ == "__main__":
    main()
