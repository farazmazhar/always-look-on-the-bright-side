# Lecture 14 — Foundation Models Overview

## What is a Foundation Model?

A large model trained on **massive, broad datasets** that serves as a base for downstream tasks. Instead of training from scratch for each task, you take a foundation model and adapt it.

The term "foundation" comes from the idea that these models are the **base layer** upon which countless applications are built — like a foundation of a house.

## How They're Built

```
Model Architecture → Pretraining on huge data → Foundation Model
                        ↑
           Lots of compute, time, money
```

1. **Choose/adjust architecture** — e.g. Transformer-based (GPT, Llama, etc.)
2. **Pretrain** on enormous corpora — text, images, code, audio, etc.

### Why Pretraining is So Expensive

| Resource | Scale |
|---|---|
| **Data** | Trillions of tokens (e.g. GPT-4 trained on ~13T tokens) |
| **Compute** | Thousands of GPUs/TPUs running for weeks or months |
| **Time** | Weeks to months of continuous training |
| **Cost** | Millions of dollars in compute alone (GPT-4 estimated ~$100M+) |
| **Energy** | Massive electricity consumption — equivalent to hundreds of homes for a year |

### What Happens During Pretraining

The model learns **general knowledge** and **patterns** from the data:
- Grammar, syntax, reasoning patterns (for text)
- Object shapes, textures, lighting (for images)
- Relationships between concepts across modalities

This is **unsupervised** or **self-supervised** learning — the model predicts the next token or fills in masked tokens, no human labeling needed.

## Why Foundation Models Matter

| Without FM | With FM |
|---|---|
| Train model from scratch for each task | Start from pretrained FM, fine-tune |
| Need huge labeled dataset per task | Need small task-specific dataset |
| Weeks of training per task | Minutes to hours of fine-tuning |
| Prohibitively expensive | Accessible to individuals/small teams |

### How You Adapt a Foundation Model

| Method | What it is | Example |
|---|---|---|
| **Prompting** | Zero-shot or few-shot via natural language | `"Summarize this article: ..."` |
| **Fine-tuning** | Further train on task-specific data | Fine-tune GPT on medical records for diagnosis |
| **RAG** | Augment with external knowledge retrieval | FM + vector DB of company docs for Q&A |
| **LoRA/QLoRA** | Efficient fine-tuning with small adapter weights | Fine-tune Llama on a single GPU |

## Examples

| Foundation Model | Provider | Modality | Known For |
|---|---|---|---|
| GPT-4 / GPT-4o | OpenAI | Text + Vision | General purpose, strong reasoning |
| Llama 3 | Meta | Text | Open-source, competitive with GPT-4 |
| Claude 3.5 | Anthropic | Text + Vision | Safety-focused, long context |
| Gemini | Google | Multimodal | Natively multimodal (text, image, audio, video) |
| Stable Diffusion | Stability AI | Image | Open-source image generation |
| DALL-E 3 | OpenAI | Image | Text-to-image, integrated with ChatGPT |
| Midjourney | Midjourney | Image | High-quality artistic image generation |
