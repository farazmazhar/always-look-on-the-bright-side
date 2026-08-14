# pyc & pyi — bytecode caches and type stubs

A hands-on demo that creates real `.pyc` and `.pyi` files and then actually
uses both:

- **`.pyc`** — compiled bytecode. The demo compiles `geometry.py` into
  `__pycache__/geometry.cpython-314.pyc`, then imports and runs the module
  from that bytecode with the `.py` source hidden.
- **`.pyi`** — a type stub. The demo writes `geometry.pyi`, then runs `mypy`
  on `consumer.py` and shows that the stub — not the implementation — is what
  drives type checking.

## The twist that makes the stub essential

`geometry.py` is deliberately written with **no type annotations**, the way a
real-world C extension or legacy module would be. The only place the types
exist is `geometry.pyi`:

| With `geometry.pyi`            | Without `geometry.pyi`       |
| ------------------------------ | ---------------------------- |
| mypy catches the bad call      | mypy stays silent            |
| types come from the stub       | untyped module → no checking |

Run the demo and you'll see `mypy` flag
`consumer.py:9: error: Argument 1 to "area_of_square" has incompatible type "str"; expected "float"` —
a mistake it only notices because the stub declared the signature.

## Files

- `geometry.py` — untyped implementation (the "library" being compiled/typed).
- `consumer.py` — imports `geometry`; type-checked against the stub.
- `demo.py` — creates the `.pyc` and `.pyi`, then uses both.
- `demo_stub_package.py` — how `types-requests`-style stub packages work.

## Run it

```bash
.venv/bin/python demo.py
.venv/bin/python demo_stub_package.py
```

## Install

`py_compile`/`importlib` are standard library. Only `mypy` needs installing:

```bash
python3 -m venv .venv
.venv/bin/pip install mypy
```

## Key APIs

- `py_compile.compile(src, doraise=True)` — compile one source file to `.pyc`.
- `compileall.compile_dir(...)` / `.compile_file(...)` — compile whole trees.
- `importlib.util.spec_from_file_location(...)` + a `SourcelessFileLoader` —
  import a `.pyc` with no `.py` present.
- `sys.dont_write_bytecode` / `-B` / `PYTHONDONTWRITEBYTECODE=1` — disable
  automatic `.pyc` writes.
- `mypy` (or `pyright`, IDE autocomplete) — reads the `.pyi` stub instead of
  executing the module.

## How .pyc naming works

`__pycache__/geometry.cpython-314.pyc`:

- `cpython` — the interpreter implementation.
- `314` — the Python version. Bytecode format changes between versions, so the
  cache is keyed per-version; a stale cache is ignored and rebuilt.
- A hash/tag suffix (3.8+) further disambiguates platforms.

Modern `.pyc` files start with a 16-byte header — magic number, flags, and a
timestamp or source hash — followed by a `marshal`-serialized code object
containing the actual opcodes the VM executes.

## Why use them?

- **`.pyc`** — faster imports (parsing is skipped) and `.pyc`-only deployments
  that ship code without readable source.
- **`.pyi`** — type-check C extensions, `.pyc`-only libraries, or any module
  whose implementation you don't want to run; also exposes a clean public API
  contract for tools.

## Stub packages (`types-<lib>`)

Libraries that ship no type info (e.g. `requests`) rely on a **stub-only
companion package** installed from PyPI. Per PEP 561, a stub package is a
distribution that contains only `.pyi` files, installed into a
`<name>-stubs/` directory in site-packages. Type checkers automatically look
for `<name>-stubs/` when resolving `import <name>` — no marker file needed,
the `-stubs` suffix *is* the signal.

`demo_stub_package.py` reproduces this end to end with a fake `widgets`
library: installing `widgets-stubs` flips mypy from
`error: Skipping analyzing "widgets": ... missing library stubs or py.typed marker`
to catching a real type error against the stub's signatures.

## References

- `py_compile` docs: https://docs.python.org/3/library/py_compile.html
- `compileall` docs: https://docs.python.org/3/library/compileall.html
- `.pyi` / type stubs (PEP 484): https://peps.python.org/pep-0484/#stub-files
- Stub-only packages (PEP 561): https://peps.python.org/pep-0561/
