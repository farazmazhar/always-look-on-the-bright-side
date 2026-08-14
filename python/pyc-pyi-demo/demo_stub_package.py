"""
stub-only package demo — how `pip install types-<lib>` gives an untyped
library its types.

Run with:  .venv/bin/python demo_stub_package.py

Real-world situation: `requests` ships NO type info. Type checkers need a
companion package. `types-requests` installs stubs into a directory named
`requests-stubs` in site-packages, and mypy automatically looks for
`<name>-stubs/` when it resolves `import <name>`.

This demo reproduces that exact mechanism with a fake library `widgets`:

  1. Installs an untyped `widgets` package into site-packages (like `requests`).
  2. Installs a `widgets-stubs` stub package alongside it (like `types-requests`).
  3. Runs mypy on a consumer WITHOUT the stubs  -> "missing library stubs"
  4. Runs mypy on a consumer WITH the stubs     -> stub types catch real errors

Everything is cleaned up afterwards — nothing is left in site-packages.
"""

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import site

HERE = Path(__file__).resolve().parent
SITE_PACKAGES = Path(site.getsitepackages()[0])

# The fake library + its stub companion, both living in site-packages.
WIDGETS = SITE_PACKAGES / "widgets"
WIDGETS_STUBS = SITE_PACKAGES / "widgets-stubs"

print("== 0. The cast ==")
print(f"  widgets/          ->  site-packages  (simulates 'requests', untyped, no py.typed)")
print(f"  widgets-stubs/    ->  site-packages  (simulates 'types-requests', .pyi only)")


def install_widgets() -> None:
    """Install the untyped runtime library (no .pyi, no py.typed)."""
    WIDGETS.mkdir(parents=True)
    (WIDGETS / "__init__.py").write_text(
        '"""Untyped runtime library — deliberately no annotations, no py.typed."""\n'
        "\n"
        "\n"
        "def make_widget(size):\n"
        '    return {"size": size}\n'
        "\n"
        "\n"
        "def widget_name(w):\n"
        '    return w["size"]\n',
        encoding="utf-8",
    )
    # NOTE: no py.typed marker file -> type checkers treat the library as untyped.


def install_stubs() -> None:
    """Install the stub-only companion package (the PEP 561 -stubs directory)."""
    WIDGETS_STUBS.mkdir(parents=True)
    (WIDGETS_STUBS / "__init__.pyi").write_text(
        '"""Type stubs for widgets (no implementation)."""\n'
        "\n"
        "\n"
        "def make_widget(size: int) -> dict[str, int]: ...\n"
        "\n"
        "\n"
        "def widget_name(w: dict[str, int]) -> str: ...\n",
        encoding="utf-8",
    )


# A consumer that imports widgets. mypy checks it against whatever it can find.
CONSUMER = """\
import widgets

ok: dict[str, int] = widgets.make_widget(5)
print(ok)

# BUG: passing a str where the stub demands int — only visible WITH the stubs.
bad: dict[str, int] = widgets.make_widget("nope")
"""


def run_mypy(consumer: Path) -> subprocess.CompletedProcess:
    cache = Path(tempfile.mkdtemp(prefix="mypy_cache_"))
    try:
        return subprocess.run(
            [sys.executable, "-m", "mypy", "--no-incremental",
             "--cache-dir", str(cache), str(consumer)],
            capture_output=True,
            text=True,
        )
    finally:
        shutil.rmtree(cache, ignore_errors=True)


def main() -> None:
    install_widgets()  # step 1: the untyped library is present
    consumer = Path(tempfile.mkdtemp(prefix="consumer_")) / "use_widgets.py"
    consumer.write_text(CONSUMER, encoding="utf-8")

    # --- Run 1: WITHOUT the stub package ----------------------------------
    print("\n== 1. mypy WITHOUT widgets-stubs installed ==")
    r1 = run_mypy(consumer)
    print(f"  exit code {r1.returncode}")
    for line in r1.stdout.splitlines():
        print("  ", line)
    print("  -> the library is untyped, so nothing is checked. (This is the")
    print("     'missing library stubs or py.typed marker' error you'd see with requests.)")

    # --- Run 2: WITH the stub package --------------------------------------
    print("\n== 2. installing widgets-stubs (simulates: pip install types-requests) ==")
    install_stubs()
    for f in sorted(WIDGETS_STUBS.rglob("*.pyi")):
        print("  installed:", f.relative_to(SITE_PACKAGES))

    r2 = run_mypy(consumer)
    print(f"\n  mypy WITH widgets-stubs installed -> exit code {r2.returncode}")
    for line in r2.stdout.splitlines():
        print("  ", line)
    print("  -> the stub told mypy the real signatures, so the bad call is caught.")

    # --- Cleanup -----------------------------------------------------------
    shutil.rmtree(WIDGETS, ignore_errors=True)
    shutil.rmtree(WIDGETS_STUBS, ignore_errors=True)
    shutil.rmtree(consumer.parent, ignore_errors=True)
    print("\ncleaned up: widgets, widgets-stubs and temp consumer are gone.")


if __name__ == "__main__":
    main()
