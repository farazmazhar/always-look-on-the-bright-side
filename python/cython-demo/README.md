# Cython — compile Python to a native C extension

Cython turns Python-like source (`.pyx`) into C, which is then compiled into a
native extension (`.so` / `.pyd`). This demo follows the "ship a library
without exposing source" story from the pyc/pyi demo — but instead of
bytecode, Cython produces a real compiled binary that is far harder to read,
plus a `.pyi` stub so users still get full type checking and autocomplete.

## The pipeline

```
fastmath.pyx ──cython──▶ fastmath.c ──gcc──▶ fastmath.cpython-313-*.so
                  (C source)              (native binary, no readable Python)
fastmath.pyi  ──read by mypy──▶ consumer.py type-checked against the stub
```

## What the demo does

1. Shows the `.pyx` source, including `cdef` declarations that compile to
   fast C-level types.
2. Runs `cython` to generate C.
3. Runs `gcc` to build a native `.so` extension.
4. **Uses the `.so`** — imports it and calls `fib`, `sum_of_squares`, `PI`
   exactly like a normal Python module.
5. **Uses the `.pyi`** — runs mypy on `consumer.py`: without the stub it says
   `Cannot find implementation or library stub for module named "fastmath"`;
   with the stub it catches a real `[arg-type]` error.

> **Note:** the `.so` alone is enough to import the module at runtime — the
> `.pyi` is never loaded by the interpreter. The stub exists solely for
> **tools** (mypy, pyright, IDE autocomplete), because a compiled binary has
> no inspectable Python type info. Demo cleanup deletes `fastmath.c` and
> `fastmath.*.so` after each run so the folder stays source-only and re-runs
> are deterministic; `fastmath.pyi` is left behind on purpose.

## Run it

```bash
.venv/bin/python demo.py
```

## Install

The venv is built on uv-managed CPython 3.13 (the system 3.14 headers are
incomplete). `gcc` must be on your PATH.

```bash
uv venv --python 3.13 .venv
uv pip install --python .venv/bin/python cython mypy
```

### Missing Python.h

Compiling a C extension needs the Python **development headers**, which the
base runtime doesn't ship. If gcc fails with
`fatal error: Python.h: No such file or directory`, install the dev package
for your distro:

- Fedora / RHEL / CentOS: `sudo dnf install python3-devel`
- Debian / Ubuntu: `sudo apt install python3-dev`

Verify with `ls /usr/include/python3.14/Python.h` (path depends on version).
Using a Python that bundles headers (uv-managed, pyenv, conda) sidesteps this.

## Key concepts

- **`.pyx`** — Cython source: valid Python plus optional C declarations.
- **`cdef`** — declares C-level types/locals, so hot loops run as native code
  (the speed win over pure Python).
- **`cython` CLI** — translates `.pyx` to C.
- **`gcc -shared -fPIC`** — builds the C into an importable shared library.
- **Extension suffix** — `.cpython-313-x86_64-linux-gnu.so`; the version tag
  must match the interpreter, so each supported Python version needs its own
  build (the same version-locking `.pyc` has).
- **`.pyi`** — the compiled binary has no Python type info to inspect, so the
  stub is the *only* source of types for mypy/pyright/IDEs.

## Version compatibility

Does the Python version need to match for a `.so` to load? **Yes — the minor
version must match**, for the same reason `.pyc` files are version-locked.

- The filename embeds the tag: `fastmath.cpython-313-*.so` only loads under
  CPython 3.13. Importing under 3.12 fails with `ImportError: dynamic module
  does not define module export function (PyInit_fastmath)`.
- **Minor version (3.13 vs 3.14)** is the hard boundary; **patch level**
  (3.13.1 vs 3.13.11) almost always works but isn't guaranteed; **platform**
  (CPU, glibc vs musl, OS) must also match.
- **The exception:** extensions built with the limited API and tagged `abi3`
  (e.g. `cp37-abi3-manylinux_x86_64`) run on every CPython 3.7+ on that
  platform, because they promise to use only the stable public API. Cython
  supports this; you just can't use internal CPython APIs.

## Packaging for multiple Python versions

Since a `.so` is version+platform locked, you ship **one wheel per Python
version (× platform)** and let pip pick the right one. Each wheel's filename
encodes what it runs on:

```
fastmath-1.0.0-cp313-cp313-manylinux_2_17_x86_64.whl   # CPython 3.13, Linux x86_64
fastmath-1.0.0-cp312-cp312-manylinux_2_17_x86_64.whl   # CPython 3.12, Linux x86_64
fastmath-1.0.0-cp313-cp313-macosx_11_0_arm64.whl       # CPython 3.13, macOS arm64
```

- `cp313` requires CPython 3.13; the platform tag covers OS/CPU. pip reads the
  user's interpreter + platform and installs the matching wheel — no user-side
  juggling.
- You don't hand-build the matrix: **cibuildwheel** builds it in CI
  (GitHub Actions) for every Python version and platform, then uploads all
  wheels to PyPI. One command, ~20 wheels from one source.
- With `abi3`, build **once per platform instead of once per version**
  (`py-limited-api = "cp37"` → one wheel serves every 3.7+ on that platform).

### The wheel file in this repo

`pyproject.toml` builds a wheel with:

```toml
[[tool.setuptools.ext-modules]]
name = "fastmath"
sources = ["fastmath.pyx"]

[tool.setuptools.data-files]
"" = ["fastmath.pyi"]
```

Build it with:

```bash
.venv/bin/python -m build --wheel
```

A wheel is just a **zip file** with a fixed layout. Building this demo
produces `dist/fastmath-1.0.0-cp313-cp313-linux_x86_64.whl` containing:

| Entry | What it is |
|-------|-----------|
| `fastmath.cpython-313-*.so` | the compiled module — the actual code |
| `fastmath-1.0.0.data/data/fastmath.pyi` | type stub, installed beside the `.so` |
| `fastmath-1.0.0.dist-info/METADATA` | name, version, `Requires-Python`, deps |
| `fastmath-1.0.0.dist-info/WHEEL` | spec version + `Tag: cp313-cp313-linux_x86_64` (what pip uses to match) |
| `fastmath-1.0.0.dist-info/RECORD` | file list + hashes (uninstall/verification) |
| `fastmath-1.0.0.dist-info/top_level.txt` | importable names |

Notably **absent**: no `.pyx`, no `.py` source — the "ship binary + stub, hide
source" story in a single artifact. The `Root-Is-Purelib: false` flag in
`WHEEL` is the key marker: it tells pip this wheel contains compiled artifacts,
so it must not be treated as a version-agnostic `py3-none-any` package.

## Why use it?

- Hide readable source — users get a binary, not your Python.
- Real C speed for numeric/hot-path code.
- Ship the same wheel you'd publish: native extension + `.pyi` stubs.

## Caveats

- Not bulletproof — C code is still reverse-engineerable; it just raises the
  bar far above `.pyc`.
- One build per Python version *and* platform (wheels: `manylinux`, macOS,
  Windows). The stable ABI (`abi3`) can loosen the version lock.
- Requires a C compiler and the Python development headers (`Python.h`).

## References

- Cython docs: https://cython.readthedocs.io/
- Cython language basics: https://cython.readthedocs.io/en/latest/src/userguide/language_basics.html
- cibuildwheel: https://cibuildwheel.pypa.io/
