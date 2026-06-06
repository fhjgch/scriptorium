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

posts = []

for tex in sorted(PUBLISHED.glob("*.tex")):
    target   = os.readlink(tex)
    kind     = "Newsletter" if "newsletter" in target else "Blog"
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
            "--standalone",
            "-o", str(out_file),
        ],
        check=True,
    )
    print(f"  [{kind}] {title} → {out_file.name}")

    posts.append({"title": title, "author": author, "date": date,
                  "kind": kind, "href": f"{slug}.html"})

posts.sort(key=lambda p: p["date"], reverse=True)

items = ""
for p in posts:
    items += (
        f'        <li class="post-item">\n'
        f'            <span class="post-type">{p["kind"]}</span>\n'
        f'            <a href="{p["href"]}" class="post-link">{p["title"]}</a>\n'
        f'            <span class="post-date">{p["date"]}</span>\n'
        f'        </li>\n'
    )

index_html = (TEMPLATES / "index.html").read_text().replace("<!-- POSTS -->", items)
(DOCS / "index.html").write_text(index_html)

print(f"\nBuilt {len(posts)} post(s) → docs/")
