# zensical

**zensical** is a modern **static site generator** built by the team behind
Material for MkDocs. You write documentation in Markdown, configure it with a
single `zensical.toml`, and build a fast, searchable, beautiful static site.

It is implemented in Rust + Python and distributed as a Python package.

## Why use it?

- Write docs in Markdown you already know; get a professional site in seconds.
- Ships with the batteries included: search, dark mode, code copy buttons,
  admonitions, tabs, footnotes, diagrams (mermaid), math, and more.
- Fast builds (Rust core) and a built-in live-preview server (`zensical serve`).
- The direct successor to the mkdocs-material experience, simplified.

## Key features

- CLI: `zensical new`, `zensical build`, `zensical serve`.
- Single config file: `zensical.toml` (site name, nav, theme, extensions).
- Markdown extensions: admonitions, code blocks + annotations, tabs, footnotes,
  task lists, tooltips, emoji, inline code highlighting.
- Themes, palettes (light/dark/system), and feature toggles.
- Built-in search, navigation features, and Mermaid diagrams.
- Outputs a plain static `site/` folder deployable anywhere.

## Install

```bash
pip install zensical
```

## Use cases

- Project documentation and API reference sites.
- Internal wikis and knowledge bases.
- Technical blogs and course notes.
- Publishing Markdown-based docs to GitHub Pages/Netlify.

## Things you can achieve

- `zensical new` scaffolds a complete, themed docs project.
- One `zensical.toml` controls navigation, theme, and features.
- `zensical build` turns Markdown into a deployable static site.
- `zensical serve` gives instant live preview while you write.

## References

- Docs: https://zensical.org/docs/
- PyPI: https://pypi.org/project/zensical/
- GitHub: https://github.com/zensical/zensical
