# Lecture 17 — Foundation Model Selection

How to choose the right foundation model for your use case.

## Selection Criteria

### 1. Cost

| Cost Factor | Questions to ask |
|---|---|
| **Per-token pricing** | What's the cost per 1K input/output tokens? |
| **Fine-tuning cost** | How much to train on custom data? |
| **Hosting cost** | Self-host (GPU infra) vs. managed API? |
| **Free tier** | Is there a free tier for prototyping? |

**Example:** GPT-4 via API (~$30/M input tokens) vs. self-hosted Llama 3 on a $1.50/hr GPU instance — for high volume, self-hosting may be cheaper.

---

### 2. Modality

What type of data does the model handle?

| Modality | Models |
|---|---|
| **Text only** | GPT-4 (text mode), Llama 3, Claude (text mode), Mistral |
| **Image only** | Stable Diffusion, DALL-E, Midjourney |
| **Audio only** | Whisper (speech-to-text), ElevenLabs (text-to-speech) |
| **Multimodal** | GPT-4o/V, Claude 3.5 (text + vision), Gemini (text + image + audio + video) |

**Example:** Building a product description app → text-only LLM is enough. Building a receipt scanner → need vision-capable model.

---

### 3. Customization

Can you adapt the model to your needs?

| Level | What you can do | Example |
|---|---|---|
| **Prompt only** | Change behavior via instructions | "You are a legal assistant..." |
| **Fine-tuning** | Train on your own dataset | Fine-tune Llama on internal legal docs |
| **RAG** | Augment with external knowledge | Add vector DB of company policies |
| **Full training** | Train from scratch (rare) | Build a domain-specific model for a new language |

**Example:** Closed model (GPT-4) → only prompt + maybe fine-tune. Open model (Llama) → full control, fine-tune, quantize, deploy anywhere.

---

### 4. Inference Options

Where and how the model runs at prediction time.

| Option | Pros | Cons |
|---|---|---|
| **Managed API** (Bedrock, OpenAI) | No infra to manage, scales automatically | Higher per-token cost, data leaves your network |
| **Self-hosted** (own GPU/server) | Full control, data stays local, cheaper at scale | Must manage infra, scaling, uptime |
| **Edge/On-device** (phone, IoT) | Zero latency, offline, private | Limited model size, lower quality |
| **Serverless** (AWS Lambda + model) | Pay-per-use, auto-scale | Cold starts, size limitations |

**Example:** Chatbot for internal HR → self-host Llama 3 on company servers (data never leaves). Public demo app → Bedrock API (no infra to manage).

---

### 5. Latency

How fast does the model respond?

| Latency need | Approach |
|---|---|
| **Real-time** (<500ms) | Smaller model, edge deployment, streaming |
| **Interactive** (1-3s) | Mid-size model, API with streaming |
| **Batch** (minutes/hours) | Large model, can afford slow inference |

**Example:** Live customer chat → need <1s response, use smaller/faster model. Overnight report generation → can use the biggest, slowest model.

---

### 6. Architecture

| Architecture | Best for | Example |
|---|---|---|
| **Decoder-only (GPT-style)** | Text generation | GPT-4, Llama, Claude |
| **Encoder-only (BERT-style)** | Classification, NER, embeddings | BERT, RoBERTa |
| **Encoder-decoder (T5-style)** | Translation, summarization | T5, BART |
| **Diffusion** | Image generation | Stable Diffusion |
| **GAN** | Realistic image synthesis | StyleGAN |

---

### 7. Language Support

| Consideration | Example |
|---|---|
| **Monolingual** | English only → narrower choice |
| **Multilingual** | Need Hindi, Arabic, etc. → check language coverage |
| **Code** | Code generation → models trained on code repos |

**Example:** English-only app → any major LLM works. App for Japanese market → verify Japanese proficiency in benchmarks.

---

### 8. Size & Complexity

| Size | Trade-off |
|---|---|
| **Small** (1-7B params) | Fast, cheap, run on single GPU. Lower quality. |
| **Medium** (7-70B params) | Good balance. Multiple GPUs needed. |
| **Large** (70B-400B+) | Best quality. Expensive, slow, needs cluster. |

**Example:** Prototype on Llama 3 8B (runs on free Colab GPU) → production on Llama 3 70B (dedicated GPU server).

---

### 9. Ability to Scale

| Factor | What to check |
|---|---|
| **Concurrent users** | Can the API handle 10K simultaneous requests? |
| **Throughput** | Tokens per second at peak load? |
| **Rate limits** | API tier limits (requests/min, tokens/min)? |
| **Auto-scaling** | Does managed service auto-scale or do you configure it? |

---

### 10. Compliance & Licensing

| Concern | Example |
|---|---|
| **Data privacy** | Does data go to third-party servers? (GDPR, HIPAA) |
| **Commercial use** | Can you use model outputs in paid products? |
| **Open-source license** | MIT, Apache, Llama Community License — read the terms |
| **Copyright risk** | Who owns generated content? Any training data lawsuits? |

**Example:** Healthcare app handling patient data → self-host open model (HIPAA compliance), never send to external API.

---

### 11. Environmental Considerations

| Factor | Impact |
|---|---|
| **Training energy** | Large models = massive carbon footprint |
| **Inference energy** | Running 24/7 for millions of users → continuous energy draw |
| **Hardware lifecycle** | GPUs have limited lifespan, e-waste |

**Example:** Use existing pretrained model instead of training from scratch (avoids training energy). Choose smaller model if quality difference is marginal.

---

## Decision Framework

```
                    ┌─ Text only ──┐
Modality? ──────────┤              ├── Open-source? ──┬─ Yes → Llama, Mistral
                    ├─ Images ─────┤                   └─ No  → GPT-4, Claude
                    ├─ Multimodal ─┤
                    └─ Audio ──────┘

                    ┌─ < 500ms → Small model, edge deploy
Latency req? ───────┤
                    └─ > 2s    → Large model, API

                    ┌─ Yes → Self-hosted open model
Data sensitive? ────┤
                    └─ No  → Managed API is fine
```
