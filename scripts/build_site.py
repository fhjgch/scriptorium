#!/usr/bin/env python3
"""Converts published/ symlinks to HTML and generates the site index."""

import os
import shutil
import subprocess
from pathlib import Path

PUBLISHED = Path("published")
DOCS      = Path("docs")
TEMPLATES = Path("templates/html")

DOCS.mkdir(exist_ok=True)
shutil.copy(TEMPLATES / "style.css", DOCS / "style.css")

blogs       = []
newsletters = []

for tex in sorted(PUBLISHED.glob("*.tex")):
    target = os.readlink(tex)
    is_newsletter = "newsletter" in target
    kind     = "Newsletter" if is_newsletter else "Blog"
    backlink = "./newsletters.html" if is_newsletter else "./blog.html"
    backlabel = "All newsletters" if is_newsletter else "All posts"
    slug     = tex.stem
    out_file = DOCS / f"{slug}.html"

    meta_raw = subprocess.run(
        ["pandoc", str(tex), "--template", str(TEMPLATES / "meta.txt")],
        capture_output=True, text=True
    ).stdout.strip()

    parts  = (meta_raw + "||").split("|")
    title  = parts[0].strip() or slug
    author = parts[1].strip()
    date   = parts[2].strip()

    subprocess.run(
        [
            "pandoc", str(tex),
            "--template", str(TEMPLATES / "post.html"),
            "--metadata", f"type={kind}",
            "--metadata", f"backlink={backlink}",
            "--metadata", f"backlabel={backlabel}",
            "--standalone",
            "-o", str(out_file),
        ],
        check=True,
    )
    print(f"  [{kind}] {title} → {out_file.name}")

    entry = {"title": title, "author": author, "date": date, "href": f"{slug}.html"}
    (newsletters if is_newsletter else blogs).append(entry)

def build_list_page(entries, title, filename):
    entries.sort(key=lambda p: p["date"], reverse=True)
    items = ""
    for p in entries:
        items += (
            f'        <li class="post-item">\n'
            f'            <a href="{p["href"]}" class="post-link">{p["title"]}</a>\n'
            f'            <span class="post-date">{p["date"]}</span>\n'
            f'        </li>\n'
        )
    html = (TEMPLATES / "list.html").read_text()
    html = html.replace("<!-- TITLE -->", title).replace("<!-- POSTS -->", items)
    (DOCS / filename).write_text(html)
    print(f"  Built {filename} ({len(entries)} entries)")

build_list_page(blogs,       "Blog",       "blog.html")
build_list_page(newsletters, "Newsletter", "newsletters.html")

shutil.copy(TEMPLATES / "index.html", DOCS / "index.html")
print(f"  Built index.html")

print(f"\nDone — {len(blogs)} post(s), {len(newsletters)} newsletter(s)")
