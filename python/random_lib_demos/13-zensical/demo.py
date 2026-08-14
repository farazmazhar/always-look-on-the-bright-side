"""
zensical demo — build a static site from Markdown.

Run with:  .venv/bin/python 13-zensical/demo.py

zensical is a CLI tool (not an importable API), so this demo drives it via
subprocess: it scaffolds a project, adds a Markdown page, builds the site,
and prints what was produced. No network access is required.
"""

import shutil
import subprocess
import sys
from pathlib import Path

# The `zensical` binary lives next to the venv's python interpreter.
ZENSICAL = Path(sys.executable).with_name("zensical")

# Build everything inside this folder so it is easy to find and clean up.
DEMO_DIR = Path(__file__).parent
SITE_DIR = DEMO_DIR / "example-site"


def run(*args: str) -> None:
    """Run a zensical subcommand, printing its output."""
    print(f"\n$ zensical {' '.join(args)}")
    result = subprocess.run([str(ZENSICAL), *args], cwd=SITE_DIR, text=True)
    if result.returncode != 0:
        raise SystemExit(f"zensical exited with {result.returncode}")


# ---------------------------------------------------------------------------
# 1. Scaffold a new project from the official template
# ---------------------------------------------------------------------------
print("1. Scaffolding a new project")
if SITE_DIR.exists():
    shutil.rmtree(SITE_DIR)  # start fresh so the demo is repeatable

# `zensical new <dir>` creates docs/, zensical.toml, and a GitHub workflow.
subprocess.run([str(ZENSICAL), "new", str(SITE_DIR)], text=True, check=True)

# Show what the template contains.
print("   created files:")
for path in sorted(p for p in SITE_DIR.rglob("*") if p.is_file()):
    print("     -", path.relative_to(SITE_DIR))


# ---------------------------------------------------------------------------
# 2. Add a page of our own and wire it into the navigation
# ---------------------------------------------------------------------------
print("\n2. Adding a custom Markdown page")

page = SITE_DIR / "docs" / "hello.md"
page.write_text(
    "---\n"
    "icon: lucide/sparkles\n"
    "---\n"
    "\n"
    "# Hello, zensical!\n"
    "\n"
    "This page was written by the demo script.\n"
    "\n"
    "!!! note\n"
    "    Admonitions, like this note, come for free.\n"
    "\n"
    "```python\n"
    "print('code blocks too')\n"
    "```\n"
)

# Add the new page to the nav list in zensical.toml.
config_path = SITE_DIR / "zensical.toml"
config = config_path.read_text()
config = config.replace(
    'nav = [\n  { "Get started" = "index.md" },\n',
    'nav = [\n  { "Get started" = "index.md" },\n  { "Hello" = "hello.md" },\n',
)
config_path.write_text(config)
print("   wrote:", page.relative_to(SITE_DIR))
print("   updated nav in:", config_path.relative_to(SITE_DIR))


# ---------------------------------------------------------------------------
# 3. Build the static site
# ---------------------------------------------------------------------------
print("\n3. Building the site")
run("build")

# The build produces plain HTML in site/.
built = sorted(SITE_DIR.glob("site/**/*.html"))
print("   generated HTML files:")
for path in built:
    print("     -", path.relative_to(SITE_DIR))

# Show a fragment of the generated index to prove it worked.
index_html = SITE_DIR / "site" / "index.html"
if index_html.exists():
    title_line = next(
        (ln.strip() for ln in index_html.read_text().splitlines() if "<title>" in ln),
        "",
    )
    print("   index title tag:", title_line)


print("\n4. Preview it (run manually, then open the URL):")
print(f"   {ZENSICAL} serve -f {SITE_DIR / 'zensical.toml'}")

print("\nDone — Markdown became a static site in:", SITE_DIR.relative_to(DEMO_DIR.parent))
