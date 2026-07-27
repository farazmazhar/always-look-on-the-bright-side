# Lecture 8 — Prompt Templates [Hands-On]

Continuing with the **Movie Script Generator** via **Amazon Bedrock**.

Course material: `course_material/Part 1 - Prompt Engineering/Movie_Script_Generator/`

## The Template

Uses `{{ }}` placeholders for reuse across different movie ideas:

```
You are an expert screenwriter. You are writing a script of a {{Genre}}
for a movie with the following outline: {{Outline}}.
The content should include at least 50 pages.
Include an appropriate movie title.
```

## Why Templates

- **Reusable** — swap `{{Genre}}` and `{{Outline}}` for any movie concept
- **Consistent** — same structure, format, and quality across runs
- **Scalable** — programmatically fill placeholders for batch generation
- **Maintainable** — tweak the template once, applies to all future generations

## Contrast with Lecture 7

| Aspect | Lecture 7 (inline) | Lecture 8 (template) |
|---|---|---|
| Structure | All 4 elements written out manually | Placeholders for dynamic parts |
| Reuse | Copy-paste and edit every time | Fill placeholders, run |
| Flexibility | Fixed to one movie idea | Works for any genre + outline |
