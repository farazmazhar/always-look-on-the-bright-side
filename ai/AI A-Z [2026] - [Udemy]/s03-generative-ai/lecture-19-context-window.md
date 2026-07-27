# Lecture 19 — Context Window

## What It Is

The **maximum number of tokens** an LLM can process in a single request — includes both the input prompt AND all generated output.

## The Limitation

```
Context window

├── Your prompt ──────────────┤
├── Model's response so far ──┤
├── Conversation history ─────┤  ← all must fit within the window
└── [OUT OF BOUNDS] ──────────┘  ← truncated, forgotten
```

Once the total tokens exceed the window, the **oldest tokens are dropped**. The model literally cannot see them anymore.

## Why It Matters

| Scenario | Problem |
|---|---|
| **Long conversations** | Chatbot forgets what was said at the start |
| **Large documents** | Can't summarize an entire book in one shot |
| **Codebase analysis** | Can't process a full repository at once |
| **Multi-turn tasks** | Earlier instructions get lost |

## Example

```
Context window: 4,096 tokens (~3,000 words)

User: "Summarize this 10-page report for me."
      [report = 3,500 tokens]
      [system prompt + instructions = 300 tokens]
      Total = 3,800 tokens → fits within 4,096 ✓

Next turn:
User: "Now explain point 3 in more detail."
      [entire previous conversation = 3,800 tokens]
      [new question = 20 tokens]
      [model starts generating...]
      [response = 500 tokens...]
      Total = 4,320 tokens → EXCEEDS WINDOW ✗
      → First part of report truncated → model loses context
```

## Mitigations

| Strategy | How it helps |
|---|---|
| **Summarize** | Periodically summarize conversation, discard old turns |
| **Chunking** | Split large docs into pieces, process one at a time |
| **RAG** | Store docs externally, retrieve only relevant chunks |
| **Use larger context model** | GPT-4 Turbo (128K) or Claude (200K) for big tasks |
| **Keep prompts concise** | Shorter system prompts = more room for conversation |

## Key Takeaway

> Context window is a **hard limit**. Plan your prompts and conversation flows around it. Anything pushed out is gone forever — the model has no "long-term memory" unless you build one externally.
