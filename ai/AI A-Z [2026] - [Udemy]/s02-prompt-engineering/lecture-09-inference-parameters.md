# Lecture 9 — Inference Parameters for Generative AI

Parameters that control how an LLM generates output at inference time.

## Randomness & Diversity

| Parameter | What it does | Range | Low value | High value |
|---|---|---|---|---|
| **Temperature** | Scales the probability distribution. Higher = more random. | 0–∞ | Deterministic, repetitive (good for facts/code) | Creative, diverse, unpredictable (good for brainstorming) |
| **Top-P** (nucleus sampling) | Only consider tokens whose cumulative probability ≥ P. | 0–1 | Narrow selection, conservative | Wide selection, diverse |
| **Top-K** | Only consider the K most likely next tokens. | 1–vocab_size | Small K = safe, focused | Large K = more variety |

### Examples

```
Prompt: "The cat sat on the..."

Temperature=0.1 → "...mat." (always picks most likely)
Temperature=0.9 → "...windowsill watching birds fly by." (more creative)
Temperature=1.5 → "...floating cloud of existential dread." (wild)

Top-P=0.1  → only tokens making up 10% of probability mass
Top-P=0.9  → tokens making up 90% of probability mass (more options)

Top-K=5    → pick from only the 5 most likely tokens
Top-K=50   → pick from the 50 most likely tokens
```

## Length Control

| Parameter | What it does |
|---|---|
| **Max Length** | Hard cap on total output tokens. Generation stops when reached. |
| **Stop Sequences** | String(s) that halt generation when encountered. Can define multiple. |

### Examples

```
Max Length=50  → "The cat sat on the mat. It was a sunny day." (truncated at 50 tokens)
Max Length=500 → full essay

Stop Sequence="\n\n" → stops at first double newline (end of paragraph)
Stop Sequence="###"  → stops before a new section heading
Stop Sequence=["</output>", "END"] → stops at any of these markers
```

## Typical Combinations

| Use Case | Temperature | Top-P | Max Length |
|---|---|---|---|
| Code generation | 0.1–0.3 | 0.95 | Long |
| Creative writing | 0.7–1.0 | 0.9 | Long |
| Factual Q&A | 0.0–0.2 | 0.95 | Short–Medium |
| Chatbot | 0.5–0.8 | 0.9 | Medium |
