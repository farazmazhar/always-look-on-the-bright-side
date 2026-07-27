# Lecture 15 — Foundation Model Lifecycle

## The 8 Stages

```
1. Data Selection & Prep
        ↓
2. Model Selection & Architecture
        ↓
3. Pretraining
        ↓
4. Fine-tuning
        ↓
5. Evaluation
        ↓
6. Deployment
        ↓
7. Monitoring & Feedback
        ↓
8. Iteration & Maintenance  ←──────┘ (loop back)
```

---

## 1. Data Selection & Preparation

- **Collect** data from diverse sources — web crawl, books, code repos, images, audio
- **Clean** — remove duplicates, PII, toxic content, low-quality samples
- **Format** — tokenize text, resize/normalize images, convert audio to spectrograms
- **Split** — training / validation / test sets

| Data Type | Source Examples |
|---|---|
| Text | Wikipedia, books, Common Crawl, Reddit, code repos |
| Image | LAION, ImageNet, stock photo libraries |
| Audio | LibriSpeech, podcasts, music databases |
| Video | YouTube, stock footage |

---

## 2. Model Selection & Architecture

Choose architecture based on task and modality.

| Modality | Architecture |
|---|---|
| Text generation | Transformer (decoder-only: GPT, Llama) |
| Text understanding | Transformer (encoder-only: BERT) |
| Text-to-text (translation, summarization) | Transformer (encoder-decoder: T5, BART) |
| Image generation | Diffusion models, GANs, VAEs |
| Multimodal | Combined encoders + decoders (Gemini, GPT-4V) |

**Selection factors:** model size, latency needs, cost, open-source vs. proprietary, community support.

### Example

```
Task: Medical chatbot → choose Llama 3 (open-source, can fine-tune on medical data)
Task: Image generation for e-commerce → choose Stable Diffusion (open-source, customizable)
```

---

## 3. Pretraining

Train the chosen architecture on the prepared data from step 1.

- **Objective:** Learn general patterns, knowledge, and representations
- **Method:** Self-supervised (predict next token, fill in masked tokens, denoise images)
- **Output:** A model that understands language/images/etc. but isn't specialized yet

### Example

```
Train a Transformer on 10 trillion tokens of internet text
→ Model can complete sentences, answer general questions, write code
→ But doesn't know medical terminology in depth
```

---

## 4. Fine-tuning

Adapt the pretrained model to a specific domain or task with a smaller, focused dataset.

| Fine-tuning Type | What it is | Example |
|---|---|---|
| **Domain-specific** | Train on domain data (labeled or unlabeled) | Medical journals → medical LLM |
| **Instruction tuning** | Train on (instruction, response) pairs | "Summarize this:" → summary |
| **RLHF** | Reinforcement Learning from Human Feedback | Human ranks outputs, model optimizes for preference |
| **Transfer learning** | Adapt knowledge from one domain to another | English model → fine-tune for Hindi |

### Example

```
Pretrained Llama 3 → fine-tune on 100K medical Q&A pairs
→ Now the model can diagnose symptoms, explain treatments, read lab reports
```

---

## 5. Evaluation

Measure how well the fine-tuned model performs before deploying.

| Metric | Use for | Example |
|---|---|---|
| **BLEU** | Translation quality | Compare generated vs. reference translation |
| **ROUGE** | Summarization quality | Overlap of n-grams with reference summary |
| **F1 Score** | Classification accuracy | Precision + recall balance |
| **Perplexity** | Language model quality | Lower = better predictions |
| **Human evaluation** | Subjective quality | Humans rate fluency, relevance, safety |
| **BERTScore** | Semantic similarity | Uses embeddings, not just word overlap |

### Example

```
BLEU score: 0.45 (decent translation)
ROUGE-L: 0.38 (acceptable summarization)
Human eval: 4.2/5 relevance, 4.5/5 fluency → ready for deployment
```

---

## 6. Deployment

Put the model into production where users can access it.

- **API endpoint** — model hosted on cloud, accessed via REST/gRPC
- **Edge deployment** — run on device (phone, IoT) for low latency
- **Batch inference** — run on large datasets offline

### Example

```
Deploy fine-tuned medical LLM on AWS Bedrock → doctors query via API
Deploy lightweight image model on mobile app → on-device photo editing
```

---

## 7. Monitoring & Feedback

Track model behavior in production and collect user feedback.

| What to monitor | Why |
|---|---|
| **Latency** | Users leave if slow |
| **Error rates** | Model might degrade over time |
| **Output quality** | Toxicity, hallucinations, bias creep |
| **Data drift** | Real-world data changes, model becomes stale |
| **User feedback** | Thumbs up/down, ratings, reported issues |

### Example

```
Medical chatbot: track that diagnoses match doctor confirmation rates
Users report hallucinations → flag for retraining
New drug names appear in queries → model doesn't know them → data drift detected
```

---

## 8. Iteration & Maintenance

Use monitoring insights to improve the model — then loop back.

| Trigger | Action |
|---|---|
| Data drift | Retrain on fresh data |
| Poor evaluations | Better fine-tuning data, different architecture |
| User complaints | Adjust safety filters, improve accuracy |
| New capabilities needed | Add new data modalities, expand training |

### Example

```
Step 7 detects data drift (new medical terms)
→ Go back to Step 1, collect recent medical literature
→ Step 4, fine-tune again on updated data
→ Step 5, re-evaluate
→ Step 6, redeploy improved model
```
