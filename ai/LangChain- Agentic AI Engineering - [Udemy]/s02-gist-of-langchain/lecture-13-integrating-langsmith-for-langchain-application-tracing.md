# Integrating LangSmith for LangChain Application Tracing

## What is LangSmith?

Platform for tracing, observing, debugging, and monitoring LangChain applications. Paid, but offers a free **Developer** tier.

## Setup

### 1. Create Account & Generate API Key
Sign up at LangSmith, generate an API key from the dashboard.

### 2. Configure Environment Variables (`.env`)
```env
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=<your-generated-key>
LANGSMITH_PROJECT=<project-name>   # e.g., "hello-world"
```

> **Note:** `LANGSMITH_ENDPOINT` differs between US and non-US regions. A wrong endpoint causes **auth errors**.

### 3. Automatic Tracing
Once configured, running the LangChain app automatically sends detailed execution traces to the specified LangSmith project — no code changes needed.

## Analyzing Traces

LangSmith dashboard shows for each run:
- **Waterfall view** — breaks execution flow into individual steps (PromptTemplate → LLM call)
- Per-step metrics: **latency**, **time-to-first-token**, **token count**, **status** (success/failure)
- **Input / output** at each step

## Comparing LLMs
Ran the chain with both OpenAI (`gpt-5`) and Ollama (local) to compare traces:
- Local Ollama: ~1.4s latency
- OpenAI: ~16s latency
Significant performance difference visible directly in the dashboard.

## Housekeeping
Committed and pushed all code changes made so far.
