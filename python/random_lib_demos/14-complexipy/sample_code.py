"""
Sample file used by the complexipy demo (14-complexipy/demo.py).

It intentionally contains functions of varying cognitive complexity so the
demo has something real to measure.
"""


def add(a, b):
    return a + b


def classify(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    return "F"


def deep(data):
    if data:
        for item in data:
            if item:
                for sub in item:
                    if sub:
                        print(sub)


def guarded(value):
    if value is None:
        return 0
    if value < 0:
        return -1
    return value
