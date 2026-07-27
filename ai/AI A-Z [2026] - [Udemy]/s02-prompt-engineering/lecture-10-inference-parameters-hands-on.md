# Lecture 10 — Inference Parameters [Hands-On]

Used **Amazon Bedrock** to experiment with inference parameters on the Movie Script Generator.

Course material: `course_material/Part 1 - Prompt Engineering/Movie_Script_Generator/`

## Setup

Used the template prompt from Lecture 8:

```
You are an expert screenwriter. You are writing a script of a {{Genre}}
for a movie with the following outline: {{Outline}}.
The content should include at least 50 pages.
Include an appropriate movie title.
```

## Parameters Tested

| Parameter | Values tried | Observed effect |
|---|---|---|
| **Temperature** | 0.0 → 1.0 | Low: safe, predictable plots. High: unexpected twists, more humor, occasional nonsense. |
| **Top-P** | 0.1 → 1.0 | Low: repetitive sentence structures. High: varied vocabulary and phrasing. |
| ~~**Max Length**~~ | ~~100 → 2000 tokens~~ | ~~Controls how much of the script gets written before cutoff.~~ |

## Key Takeaways

- Same template, same `{{Genre}}`/`{{Outline}}` — radically different outputs based on params
- **Temperature 0.7–0.9** hit the sweet spot for creative comedy scripts
- **Top-P 0.9** gave enough variety without going off-script
- Low temperature + low top-P → stiff, formulaic writing
- High temperature + high top-P → creative but can lose coherence
