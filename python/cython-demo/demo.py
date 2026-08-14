"""
Cython demo — compile Python to a native C extension, then use it with stubs.

Run with:  .venv/bin/python demo.py

The story: you want to ship a library WITHOUT exposing readable Python source.
Cython compiles the .pyx implementation to C, then gcc builds that C into a
native .so extension. The user gets a binary module plus a .pyi stub — same
API, no readable source, and (bonus) real C speed.

Pipeline shown here:
  1. fastmath.pyx  ->  cython  ->  fastmath.c        (C source)
  2. fastmath.c    ->  gcc     ->  fastmath.*.so     (native binary)
  3. fastmath.pyi  ->  mypy reads it to type-check consumer.py

Just like the real world: the .so is importable, and mypy needs the .pyi to
know the signatures (a compiled module has no Python type info to inspect).
"""

import shutil
import subprocess
import sys
import sysconfig
from pathlib import Path

HERE = Path(__file__).resolve().parent
PYX = HERE / "fastmath.pyx"
C_FILE = HERE / "fastmath.c"
STUB = HERE / "fastmath.pyi"
CONSUMER = HERE / "consumer.py"

# The suffix gcc must produce so Python recognizes it as an importable module,
# e.g. ".cpython-314-x86_64-linux-gnu.so" — the magic is in the build tag.
import importlib.machinery as machinery

SO_FILE = HERE / f"fastmath{machinery.EXTENSION_SUFFIXES[0]}"
PY_INCLUDE = sysconfig.get_paths()["include"]  # where Python.h lives

print("== 0. The ingredients ==")
print("\nfastmath.pyx  (Cython source — the implementation):\n")
print(PYX.read_text())


# ---------------------------------------------------------------------------
# 1. cython: .pyx -> C
# ---------------------------------------------------------------------------
print("== 1. cython compiles .pyx -> C ==")
subprocess.run(
    [sys.executable, "-m", "cython", str(PYX), "-o", str(C_FILE)], check=True
)
print(f"generated: fastmath.c ({C_FILE.stat().st_size} bytes) — real C, no Python left")
print("first line of the C:", open(C_FILE).readline().strip())


# ---------------------------------------------------------------------------
# 2. gcc: C -> native .so extension
# ---------------------------------------------------------------------------
print("\n== 2. gcc compiles C -> native .so ==")
cmd = [
    "gcc",
    "-shared",
    "-fPIC",
    "-O2",
    f"-I{PY_INCLUDE}",
    "-o",
    str(SO_FILE),
    str(C_FILE),
]
subprocess.run(cmd, check=True)
print(f"built: {SO_FILE.relative_to(HERE)} ({SO_FILE.stat().st_size} bytes)")
print("  (a binary — 'strings' on it shows compiler symbols, not your code)")


# ---------------------------------------------------------------------------
# 3. USE the .so — import and call the compiled module
# ---------------------------------------------------------------------------
print("\n== 3. USING the .so ==")
import sys as _sys

_sys.path.insert(0, str(HERE))  # make sure Python finds the in-place .so
import fastmath  # imports fastmath.*.so

print("fastmath.__file__   :", Path(fastmath.__file__).relative_to(HERE))
print("  fib(10)           =", fastmath.fib(10))
print("  sum_of_squares(4) =", fastmath.sum_of_squares(4))
print("  PI                =", fastmath.PI)
print(
    "  is an extension   :",
    Path(fastmath.__file__).suffix in machinery.EXTENSION_SUFFIXES,
)


# ---------------------------------------------------------------------------
# 4. CREATE the .pyi stub for the compiled module
# ---------------------------------------------------------------------------
print("\n== 4. CREATING the .pyi stub ==")
STUB.write_text(
    '"""Type stubs for the compiled fastmath extension."""\n'
    "\n"
    "PI: float\n"
    "\n"
    "\n"
    "def fib(n: int) -> int: ...\n"
    "\n"
    "\n"
    "def sum_of_squares(n: int) -> int: ...\n",
    encoding="utf-8",
)
print("created: fastmath.pyi")
print(STUB.read_text())


# ---------------------------------------------------------------------------
# 5. USE the .pyi — mypy checks consumer.py against the stub
# ---------------------------------------------------------------------------
print("\n== 5. USING the .pyi ==")


def run_mypy(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, "-m", "mypy", *args],
        cwd=str(HERE),
        capture_output=True,
        text=True,
    )


# --- Step A: WITHOUT the stub. The .so has no Python annotations, so mypy
# cannot analyze it — same "missing library stubs" error as untyped packages.
stub_hidden = HERE / "fastmath.pyi.hidden"
shutil.move(str(STUB), str(stub_hidden))
r = run_mypy("consumer.py")
print("\n  A) mypy WITHOUT fastmath.pyi ->", f"exit {r.returncode}")
for line in r.stdout.splitlines():
    print("     ", line)
shutil.move(str(stub_hidden), str(STUB))

# --- Step B: WITH the stub. Now mypy reads the signatures and catches the
# bad call ("ten" passed to a function that wants an int).
r = run_mypy("consumer.py")
print(f"\n  B) mypy WITH fastmath.pyi   -> exit code {r.returncode}")
for line in r.stdout.splitlines():
    print("     ", line)
print("  The stub is the ONLY source of types: the .so has none to inspect.")


# ---------------------------------------------------------------------------
# Cleanup build artifacts (keep sources + stub for re-runs)
# ---------------------------------------------------------------------------
for f in (C_FILE, SO_FILE, stub_hidden):
    f.unlink(missing_ok=True)
print("\ncleaned up: fastmath.c, fastmath.*.so")
print("left behind:", ", ".join(p.name for p in sorted(HERE.iterdir()) if p.is_file()))
