# Scriptorium

A personal writing repository for blog posts and newsletters.

## Purpose
This is where I write, develop, and publish texts. The repository is my writing workspace — from first draft to published piece.

## Structure
- `writings/blog/` — blog post source files (.tex)
- `writings/newsletters/` — newsletter source files (.tex)
- `writings/drafts/` — unpublished work in progress
- `published/` — symlinks to pieces ready for web publication
- `templates/` — LaTeX templates for each document type
- `docs/` — generated site (do not edit manually, overwritten by CI)

## Publishing workflow
1. Write in `writings/blog/` or `writings/newsletters/`
2. Compile locally with pdflatex to check output
3. When ready to publish, create a symlink from the repo root:
   `ln -s ../writings/blog/my-post.tex published/my-post.tex`
4. Commit and push — GitHub Actions converts to HTML and deploys to GitHub Pages

## LaTeX conventions
- Keep LaTeX simple: standard sections, paragraphs, emphasis, lists, blockquotes, footnotes
- Avoid custom packages and complex environments — Pandoc cannot convert these to HTML
- Use `\footnote{}` for source attribution inline
- Set `\title{}`, `\author{}`, `\date{}` at the top of every document — these become the post header on the web

## Claude's role
Claude is the author's writing editor and assistant. When brought a document:
- Read and understand the full text before commenting
- Help with structure, clarity, argumentation, and style
- Ask about intent before suggesting rewrites
- Be direct about weak passages — do not flatter
