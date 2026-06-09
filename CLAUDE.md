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

## Writing identity (from first coaching session, June 2026)

**What he wants to achieve**
Bridge the rational and spiritual — show intellectually serious secular readers that there is coherence in taking spirituality seriously. Simultaneously challenge his own community to fulfill Shri Mataji's vision with greater urgency.

**Two readers, two projects**
- **Basti** — his scientifically trained friend who represents genuine honest doubt. The primary reader for all outward-facing writing. Every essay for the secular world is written to him specifically.
- **Senior yogis** — inward-facing challenge to his community. Different register, different piece entirely.
- Rule: one reader per piece, decided before starting.

**Why he writes**
He carries something rare: genuine intellectual rigor and genuine spiritual experience held together honestly. He writes from testimony, not frustration — he has made himself accountable first.

**Two core arguments (for Basti)**
1. Science hasn't solved consciousness — the depths of human inner life remain unmapped by the current paradigm.
2. Humanity engaged with the sacred for virtually all of its history. Two hundred years of dismissal hasn't explained why — and the cost is measurable.

**Posture:** not to convince, but to show there is a rational case.

**Practical approach**
- Write one arguable thesis sentence before every piece
- Capture ideas immediately via voice memo addressed to Basti, then transcribe and edit
- Zero draft first: fast, speaking voice, no judgment — editing comes after
- Never generate and judge simultaneously

**First piece:** finish the meditation draft — what Western mindfulness gets wrong about what meditation actually is.
