#!/usr/bin/env python3
"""Build the GitHub Pages site from README.md.

README.md stays the single source of truth; this turns it into a styled
static page (site/template.html) with a sidebar table of contents.

    pip install markdown==3.7
    python site/build.py            # writes _site/index.html
"""
from __future__ import annotations

import html
import re
import subprocess
import sys
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
REPO = "https://github.com/wendsell/P1S-BMCU-Lifeline"
OUT = ROOT / "_site"


def github_slug(text: str, sep: str = "-") -> str:
    """Anchor ids the way GitHub makes them, so #links from the README work."""
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text).strip().lower()
    text = re.sub(r"[^\w\- ]", "", text)  # drop punctuation, keep word chars, '-', ' '
    return text.replace(" ", "-")


def split_hero(md: str) -> tuple[str, str]:
    """Everything above the first horizontal rule is the hero."""
    parts = re.split(r"^---\s*$", md, maxsplit=1, flags=re.M)
    return (parts[0], parts[1]) if len(parts) == 2 else ("", md)


def extract_toc(body: str) -> tuple[list[tuple[str, str]], str]:
    """Pull the README's own 'Table of Contents' section out for the sidebar."""
    m = re.search(r"^##\s+Table of Contents\s*$(.*?)^---\s*$", body, flags=re.M | re.S)
    if not m:
        return [], body
    items = re.findall(r"^\s*[-*]\s+\[([^\]]+)\]\(#([^)]+)\)", m.group(1), flags=re.M)
    return items, body[: m.start()] + body[m.end():]


def restructure(body: str, section_ids: set[str]) -> str:
    """README uses '#' both for sections and for shouted one-liners.

    - '# X' in the TOC, or right after a '---' rule -> section heading (h2)
    - any other '# X'                               -> SHOUT paragraph (styled, not in nav)
    - '##' / '###'                                  -> shifted down one level
    - '---' rules are dropped; headings carry the structure on the page
    """
    out, in_code, after_rule = [], False, True
    for line in body.splitlines():
        if line.lstrip().startswith("```"):
            in_code = not in_code
            out.append(line)
            after_rule = False
            continue
        if in_code:
            out.append(line)
            continue
        if re.match(r"^---\s*$", line):
            after_rule = True
            continue
        if not line.strip():
            out.append(line)
            continue
        m = re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", line)
        was_after_rule, after_rule = after_rule, False
        if m:
            level, text = len(m.group(1)), m.group(2)
            if level == 1:
                if github_slug(text) in section_ids or was_after_rule:
                    out.append(f"## {text}")
                else:
                    out.append(f"\nSHOUT:: {text}\n")
                continue
            out.append("#" * min(level + 1, 6) + " " + text)
            continue
        out.append(line)
    return "\n".join(out)


ALERTS = {
    "NOTE": "Note", "TIP": "Tip", "IMPORTANT": "Important",
    "WARNING": "Warning", "CAUTION": "Caution",
}


def post_process(h: str) -> str:
    # Shouted one-liners
    h = re.sub(r"<p>SHOUT:: (.*?)</p>", r'<p class="shout">\1</p>', h, flags=re.S)

    # GitHub alert blockquotes -> callouts
    def alert(m: re.Match) -> str:
        kind, rest = m.group(1).upper(), m.group(2)
        rest = re.sub(r"^\s*<br\s*/?>\s*", "", rest.lstrip())
        return (f'<div class="callout {kind.lower()}"><p class="callout-title">{ALERTS[kind]}</p>'
                f"<p>{rest}</div>")
    h = re.sub(r"<blockquote>\s*<p>\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*(.*?)</blockquote>",
               alert, h, flags=re.S)
    # Plain blockquotes are the guide's one-line mottos
    h = h.replace("<blockquote>", '<blockquote class="motto">')

    # Tables scroll on small screens
    h = re.sub(r"(<table>.*?</table>)", r'<div class="table-wrap">\1</div>', h, flags=re.S)
    # Status emoji cells centered
    h = re.sub(r"<td([^>]*)>\s*(✅|❌)\s*</td>", r'<td\1 class="status">\2</td>', h)

    # Images: lazy, framed, captioned by alt text
    def img(m: re.Match) -> str:
        alt, src = m.group(1), m.group(2)  # already HTML-escaped by markdown
        return (f'<figure><img src="{src}" alt="{alt}" loading="lazy" decoding="async">'
                f"<figcaption>{alt}</figcaption></figure>")
    h = re.sub(r'<p>\s*<img alt="([^"]*)" src="([^"]+)"\s*/?>\s*</p>', img, h)

    # External links open in a new tab
    h = re.sub(r'<a href="(https?://[^"]+)">', r'<a href="\1" target="_blank" rel="noopener">', h)

    # Single-line ```text blocks are specs/values: render compact
    h = re.sub(r'<pre><code class="language-text">([^\n<]*\n?(?:[^\n<]*\n?)?)</code></pre>',
               lambda m: '<div class="spec">' + "".join(
                   f"<code>{line}</code>" for line in m.group(1).strip().split("\n")) + "</div>", h)
    return h


def render_hero(hero_md: str) -> dict[str, str]:
    title = re.search(r"^#\s+(.+)$", hero_md, flags=re.M)
    tagline = re.search(r"^###\s+(.+)$", hero_md, flags=re.M)
    image = re.search(r"!\[([^\]]*)\]\(([^)\s]+)\)", hero_md)
    rest = hero_md
    for m in (title, tagline, image):
        if m:
            rest = rest.replace(m.group(0), "")
    md = markdown.Markdown(extensions=["extra"])
    intro = md.convert(rest.strip())
    intro = intro.replace("<blockquote>", '<blockquote class="hero-quote">')
    return {
        "title": title.group(1).strip() if title else "P1S BMCU Lifeline",
        "tagline": tagline.group(1).strip() if tagline else "",
        "intro": intro,
        "image": image.group(2) if image else "",
        "image_alt": image.group(1) if image else "",
    }


def last_updated() -> str:
    """Date of the last commit touching README.md, e.g. 'July 5, 2026'."""
    from datetime import date
    try:
        iso = subprocess.run(["git", "log", "-1", "--format=%cs", "--", "README.md"],
                             cwd=ROOT, capture_output=True, text=True, timeout=10).stdout.strip()
        d = date.fromisoformat(iso)
        return f"{d:%B} {d.day}, {d.year}"
    except Exception:
        return ""


def build() -> Path:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    hero_md, body = split_hero(readme)
    toc, body = extract_toc(body)
    section_ids = {anchor for _, anchor in toc}
    body = restructure(body, section_ids)

    md = markdown.Markdown(
        extensions=["extra", "sane_lists", "toc"],
        extension_configs={"toc": {"slugify": lambda value, separator: github_slug(value, separator)}},
    )
    body_html = post_process(md.convert(body))

    # Wrap each h2 section so the page can style and scroll-spy them.
    chunks = re.split(r'(?=<h2 id=")', body_html)
    body_html = chunks[0] + "".join(f'<section class="sec">{c}</section>' for c in chunks[1:])

    missing = [a for _, a in toc if f'id="{a}"' not in body_html]
    if missing:
        print(f"warning: TOC anchors with no matching section: {missing}", file=sys.stderr)

    hero = render_hero(hero_md)
    nav = "\n".join(f'<li><a href="#{a}">{html.escape(t)}</a></li>' for t, a in toc)
    plain_tagline = re.sub(r"[*_`]", "", hero["tagline"])

    tpl = (ROOT / "site" / "template.html").read_text(encoding="utf-8")
    page = (tpl
            .replace("{{title}}", html.escape(hero["title"]))
            .replace("{{tagline}}", html.escape(hero["tagline"]))
            .replace("{{description}}", html.escape(plain_tagline))
            .replace("{{intro}}", hero["intro"])
            .replace("{{hero_image}}", html.escape(hero["image"]))
            .replace("{{hero_alt}}", html.escape(hero["image_alt"]))
            .replace("{{nav}}", nav)
            .replace("{{body}}", body_html)
            .replace("{{repo}}", REPO)
            .replace("{{updated}}", html.escape(last_updated())))
    OUT.mkdir(exist_ok=True)
    (OUT / "index.html").write_text(page, encoding="utf-8")
    (OUT / ".nojekyll").write_text("")
    return OUT / "index.html"


if __name__ == "__main__":
    print(build())
