"""
complexipy demo — measure cognitive complexity of Python code.

Run with:  .venv/bin/python 14-complexipy/demo.py

Cognitive complexity penalizes nesting and control-flow that is hard for a
human to read. This demo analyzes a code string, then a real file.
"""

from complexipy import code_complexity, file_complexity


def show(title: str) -> None:
    print(f"\n{title}")


# ---------------------------------------------------------------------------
# 1. Analyze a code string
# ---------------------------------------------------------------------------
show("1. code_complexity() on a code string")

snippet = '''
def trivial(x):
    return x + 1

def nested(data):
    if data:
        for item in data:
            if item.is_valid():
                process(item)

def early_returns(n):
    if n < 0:
        return "negative"
    if n == 0:
        return "zero"
    return "positive"
'''

result = code_complexity(snippet, check_script=True)
print(f"   total complexity: {result.complexity}")

for func in result.functions:
    print(f"   - {func.name:<14} complexity={func.complexity:<3} "
          f"(lines {func.line_start}-{func.line_end})")


# ---------------------------------------------------------------------------
# 2. Per-line complexity: see *where* the nesting hurts
# ---------------------------------------------------------------------------
show("2. Line-level complexity of the `nested` function")

# Grab the nested function from the previous result to inspect its lines.
nested = next(f for f in result.functions if f.name == "nested")
for line in nested.line_complexities:
    print(f"   line {line.line:>2}: complexity {line.complexity}")

# Note how each extra level of nesting bumps the per-line score (1 -> 2 -> 3),
# which is the key difference from cyclomatic complexity.


# ---------------------------------------------------------------------------
# 3. Analyze a real file
# ---------------------------------------------------------------------------
show("3. file_complexity() on a real file")

# This folder ships a small sample file with functions of varying complexity.
from pathlib import Path

sample = Path(__file__).with_name("sample_code.py")
file_result = file_complexity(str(sample), check_script=True)

print(f"   file: {file_result.file_name}")
print(f"   total complexity: {file_result.complexity}")
for func in file_result.functions:
    flag = "  <-- over threshold" if func.complexity > 5 else ""
    print(f"   - {func.name:<16} complexity={func.complexity:<3}{flag}")


print("\nDone — lower is better; refactor the highest-scoring functions first.")
