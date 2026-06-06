# Scriptorium

A personal writing repository. Blog posts and newsletters written in LaTeX, published as HTML to GitHub Pages.

## Writing

Copy a template, write, compile locally to check output:

```bash
cp templates/blog-post.tex writings/blog/my-post.tex
pdflatex writings/blog/my-post.tex
```

## Publishing

When a piece is ready, create a symlink in `published/`:

```bash
ln -s ../writings/blog/my-post.tex published/my-post.tex
git add published/my-post.tex
git commit -m "publish: my post"
git push
```

GitHub Actions converts it to HTML and deploys to GitHub Pages.

## Structure

```
writings/blog/          blog post source files (.tex)
writings/newsletters/   newsletter source files (.tex)
writings/drafts/        unpublished work in progress
published/              symlinks to pieces ready to publish
templates/              LaTeX and HTML templates
docs/                   generated site (do not edit)
```

## Live site

https://fhjgch.github.io/scriptorium/
