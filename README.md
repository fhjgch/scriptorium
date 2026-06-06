# Scriptorium

The word *scriptorium* referred to the room in a medieval monastery where monks copied manuscripts. Here it is something more modest: a folder on a hard drive, a few text files, and the habit of returning to them.

Writing things down forces you to find out what you actually think. The act of composing a sentence is not a record of a thought already formed — it is the formation of the thought itself.

---

Blog posts and newsletters written in LaTeX, published as HTML to GitHub Pages.

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
