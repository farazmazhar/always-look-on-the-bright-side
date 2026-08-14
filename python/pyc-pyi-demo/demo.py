"""
pyc & pyi demo — create real .pyc and .pyi files, then USE them.

Run with:  .venv/bin/python demo.py

Unlike a throwaway temp-dir demo, this one works with real files right here
in this folder. It:

  1. CREATES a .pyc  from geometry.py  (bytecode cache).
  2. CREATES a .pyi  for  geometry     (type stub).
  3. USES    the .pyc — imports and calls the module with the source hidden.
  4. USES    the .pyi — runs mypy on consumer.py and shows the stub driving
             type checking.

The twist that makes the stub essential: geometry.py has NO type annotations,
so the only place the types exist is geometry.pyi.
"""

import importlib.util
import os
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
GEOMETRY_SRC = HERE / "geometry.py"
STUB = HERE / "geometry.pyi"
CONSUMER = HERE / "consumer.py"

print("== 0. The ingredients ==")
print("\ngeometry.py  (the implementation — deliberately NO type hints):\n")
print(GEOMETRY_SRC.read_text())
print("consumer.py  (imports geometry; mypy will check it against the stub):\n")
print(CONSUMER.read_text())


# ---------------------------------------------------------------------------
# 1. CREATE the .pyc
# ---------------------------------------------------------------------------
print("== 1. CREATING the .pyc ==")
import py_compile

# py_compile compiles a single source file. With no cfile it writes to the
# standard __pycache__ location (exactly what a normal import does).
py_compile.compile(str(GEOMETRY_SRC), doraise=True)
pyc_path = importlib.util.cache_from_source(str(GEOMETRY_SRC))
print("created:", Path(pyc_path).relative_to(HERE), f"({Path(pyc_path).stat().st_size} bytes)")
print("the .pyc is compiled bytecode, not source text:",
      Path(pyc_path).read_bytes()[:16].hex())


# ---------------------------------------------------------------------------
# 2. CREATE the .pyi stub
# ---------------------------------------------------------------------------
print("\n== 2. CREATING the .pyi stub ==")

# A stub contains ONLY signatures — every body is "...". It is the contract
# tools read instead of running the implementation.
STUB.write_text(
    '"""Type stubs for the geometry module (no implementation)."""\n'
    "\n"
    "PI: float\n"
    "\n"
    "\n"
    "def area_of_square(side: float) -> float: ...\n"
    "\n"
    "\n"
    "def perimeter_of_rectangle(length: float, width: float) -> float: ...\n",
    encoding="utf-8",
)
print("created: geometry.pyi")
print(STUB.read_text())


# ---------------------------------------------------------------------------
# 3. USE the .pyc — run the module with the source hidden
# ---------------------------------------------------------------------------
print("== 3. USING the .pyc ==")

# Real deployments sometimes ship only the .pyc. To prove ours works without
# geometry.py, temporarily move the source out of the way.
hidden = HERE / "geometry.py.hidden"
shutil.move(str(GEOMETRY_SRC), str(hidden))
try:
    spec = importlib.util.spec_from_file_location("geometry", pyc_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # SourcelessFileLoader: bytecode only, no .py

    print("imported 'geometry' from:", Path(mod.__file__).relative_to(HERE))
    print("  area_of_square(4)      =", mod.area_of_square(4))
    print("  perimeter(2, 3)        =", mod.perimeter_of_rectangle(2, 3))
    print("  PI                     =", mod.PI)
    print("  geometry.py present?   ", GEOMETRY_SRC.exists(), "(hidden during this step)")
finally:
    shutil.move(str(hidden), str(GEOMETRY_SRC))  # put the source back


# ---------------------------------------------------------------------------
# 4. USE the .pyi — mypy checks consumer.py against the stub
# ---------------------------------------------------------------------------
print("\n== 4. USING the .pyi ==")

def run_mypy(*args: str) -> subprocess.CompletedProcess:
    # Run mypy from the demo folder so it finds geometry.pyi as a local module.
    return subprocess.run(
        [sys.executable, "-m", "mypy", *args],
        cwd=str(HERE),
        capture_output=True,
        text=True,
    )

# --- Step A: WITHOUT the stub. geometry.py is untyped, so mypy sees nothing
# to complain about — consumer.py checks clean.
stub_hidden = HERE / "geometry.pyi.hidden"
shutil.move(str(STUB), str(stub_hidden))
r = run_mypy("consumer.py")
print("\n  A) mypy WITHOUT geometry.pyi ->", "clean (no errors)" if r.returncode == 0 else "errors")
print("     (untyped geometry.py gives mypy nothing to check)")
shutil.move(str(stub_hidden), str(STUB))

# --- Step B: WITH the stub. Now mypy reads the signatures from geometry.pyi
# and the bad call in consumer.py ("four" passed to a float param) is caught.
r = run_mypy("consumer.py")
print(f"\n  B) mypy WITH geometry.pyi   -> exit code {r.returncode}")
print("     error caught:" if r.returncode != 0 else "     no errors?!")
for line in r.stdout.splitlines():
    print("     ", line)
print("  The stub is what makes this error visible: the types live only in .pyi.")


print("\nDone. Files left behind on purpose:")
for f in sorted(p for p in HERE.iterdir() if p.is_file()):
    print("  -", f.name)
