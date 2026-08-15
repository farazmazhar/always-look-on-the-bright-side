# Using Local Open-Weights Models with LangChain and Ollama

## Overview

Switch from a proprietary cloud LLM (OpenAI GPT) to a locally hosted open-weights model using **Ollama**.

## Alternatives Mentioned
- **Groq** — high-performance inference API, one alternative to local models (worth looking into further).

## Steps

### 1. Install Ollama
Download from [ollama.com](https://ollama.com) for your OS.

### 2. Pull a Local Model
```bash
ollama pull gemma3:270m   # lightweight model for local machines
ollama list               # confirm the model is downloaded
ollama run gemma3:270m    # interactive CLI chat session
```

### 3. Integrate with LangChain
```bash
uv add langchain-ollama
```

```python
from langchain_ollama import ChatOllama

llm = ChatOllama(model="gemma3:270m")
```
Only one line changes — the rest of the chain stays identical.

### 4. Debug and Compare
- Local model was much faster.
- Output quality was lower — failed to produce the two separate interesting facts as instructed.

## Key Takeaway
- **Model-agnostic design**: switch LLM providers (proprietary ↔ open-source, local ↔ cloud) by changing a single line of code.
- **Trade-off**: local models offer speed + cost savings; larger proprietary models offer better quality and instruction-following.

## Recommendation
Instructor recommends **gpt-oss** model.
