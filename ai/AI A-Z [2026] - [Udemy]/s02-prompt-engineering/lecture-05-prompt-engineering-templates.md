# Lecture 5 — Prompt Engineering & Prompt Templates

## Four Elements of a Good Prompt

| Element | Purpose | Example |
|---|---|---|
| **Instruction** | What you want the model to do | "Summarize the following text..." |
| **Context** | Background or constraints | "You are a helpful medical assistant..." |
| **Input Data** | The actual data to process | The article/text to summarize |
| **Output Indicator** | How the output should look | "Respond in 3 bullet points" or "Return JSON" |

## Prompt Templates

Reusable prompt structures where placeholders (`{input}`, `{topic}`) get filled dynamically. Enables consistent, repeatable AI interactions at scale.

## Risks

- **Prompt Injection** — malicious user input overrides the template instructions (e.g. "Ignore all previous instructions and...")
- **Prompt Leaking** — model reveals the system prompt or template internals
- **Jailbreaking** — crafted prompts bypass safety guardrails

## Mitigation Strategies

- Sanitize and validate user inputs
- Use delimiters to separate trusted instructions from untrusted input
- Keep instructions at the end (harder to override)
- Run output through moderation filters
