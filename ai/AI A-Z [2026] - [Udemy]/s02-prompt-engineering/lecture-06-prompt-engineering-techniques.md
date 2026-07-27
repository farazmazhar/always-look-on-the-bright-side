# Lecture 6 — Prompt Engineering Techniques

## Techniques

| Technique | Description | Example |
|---|---|---|
| **Zero-shot** | No examples given. Model relies purely on pre-trained knowledge. | `"Translate to French: Hello, how are you?"` |
| **One-shot** | One example provided. | `"Q: What is the capital of France? A: Paris. Q: What is the capital of Germany?"` |
| **Few-shot** | Multiple examples (2–5+) provided. Teaches pattern, format, and style. | 3 example Q&A pairs → then ask a new question. Or 3 labeled reviews → classify the 4th. |
| **Chain of Thought (CoT)** | Prompt model to reason step-by-step before answering. | `"A farmer has 17 sheep. All but 9 die. How many are left? Let's think step by step."` |
| **Negative Prompting** | Tell the model what *not* to do. | `"Explain quantum computing. Do not use technical jargon. Do not mention Schrödinger's cat."` |

## When to use what

| Technique | Best for |
|---|---|
| **Zero-shot** | Simple tasks, model already strong on the domain |
| **Few-shot** | Specialized tasks, teaching format + style, niche domains |
| **Chain of Thought** | Math, logic, multi-step reasoning, puzzles |
| **Negative** | Tighten output quality, suppress unwanted behavior, guard against toxic/biased output |

## Risks & Limitations

| Risk | Description |
|---|---|
| **Exposure of Sensitive Data** | Prompts containing PII, API keys, or confidential info get sent to third-party LLM providers. Assume everything in your prompt is logged. |
| **Injection of Harmful Input** | Users can craft prompts that override system instructions (prompt injection), generate harmful content, or bypass safety filters. |
| **Output Manipulation** | Adversarial prompts can steer the model to produce misleading, biased, or flat-out wrong answers (e.g. "convince me that..."). |
| **Hallucination** | Model confidently produces factually incorrect output — especially risky when output is consumed without verification. |
| **Cost & Latency** | Long prompts (few-shot with many examples) increase token count → higher cost and slower response. |
