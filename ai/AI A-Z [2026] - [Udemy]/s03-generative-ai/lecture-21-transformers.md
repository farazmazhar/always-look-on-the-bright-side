# Lecture 21 — Transformers

## What is a Transformer?

A **neural network architecture** introduced by Google in the 2017 paper ["Attention Is All You Need"](https://arxiv.org/abs/1706.03762). It replaced RNNs/LSTMs as the dominant architecture for sequence tasks and is the foundation of all modern LLMs.

## Original Architecture: Encoder + Decoder

Designed for **translation** tasks. Two halves working together:

```
Input (English)                    Output (French)
      │                                   ▲
      ▼                                   │
┌──────────┐                        ┌──────────┐
│ Encoder  │  ──→ context ──→       │ Decoder  │
│          │     (cross-attention)   │          │
│ "I love  │                        │ "J'aime  │
│  coding" │                        │  coder"  │
└──────────┘                        └──────────┘

Encoder: reads and understands the input (English)
Decoder: generates the output (French), attending to encoder's understanding
```

| Component | Role | Example |
|---|---|---|
| **Encoder** | Processes input, builds a rich representation of meaning | Reads "I love coding" → captures subject, verb, object |
| **Decoder** | Generates output token by token, attending to encoder output | Generates "J'" → "aime" → "coder" |

---

## Modern Evolution: Decoder-Only

Most LLMs today (GPT, Llama, Claude) use **decoder-only** Transformers — the encoder is dropped entirely.

### Why Decoder-Only?

| Advantage | Explanation |
|---|---|
| **Simpler** | One stack of layers, not two |
| **Unified objective** | Always "predict next token" — no separate encoding step |
| **Better at generation** | Optimized for autoregressive text generation |
| **Surprisingly good at translation** | Despite being decoder-only, modern decoder models match or exceed encoder-decoder on translation benchmarks |
| **Scales well** | Stack more layers, more parameters — performance keeps improving |

### Example

```
Prompt: "Translate to French: I love coding"

Decoder-only LLM (GPT-4):
  Step 1: "Translate to French: I love coding" → "J'"
  Step 2: "Translate to French: I love coding → J'" → "aime"
  Step 3: "... → J'aime" → "coder"
  Step 4: "... → J'aime coder" → <EOS>

No separate encoder needed. The model learns to "understand" and "generate" in one pass.
```

---

## The Core Innovation: Self-Attention

Instead of processing words sequentially (like RNNs), Transformers look at **all words simultaneously** and compute how much each word should "pay attention" to every other word.

```
Sentence: "The cat sat on the mat because it was tired."

"it" pays attention to:
  "cat"   → 0.65  (most likely what "it" refers to)
  "mat"   → 0.18
  "sat"   → 0.08
  ...

Without attention, the model wouldn't know what "it" refers to.
```

---

## Parameters vs. Hyperparameters

### Parameters (learned during training)

These are the model's **knowledge**. They get updated by backpropagation.

| What | Description | Example |
|---|---|---|
| **Weights** | Connection strengths between neurons | Weight matrix `W` in a linear layer: `[[0.23, -0.54], [0.18, 0.91]]` |
| **Biases** | Offset added to neuron output | Bias vector `b`: `[0.05, -0.12]` |
| **Attention weights** | How much each token attends to others | Attention scores matrix |
| **Embedding tables** | Vector representation of each token in vocabulary | The vector for token "cat": `[0.12, 0.87, -0.44, ...]` |

```
Parameter counts:
  GPT-3:   175 billion parameters
  Llama 3: 8B / 70B / 400B parameters
  GPT-4:   ~1.7 trillion parameters (estimated)
```

### Hyperparameters (set before training, NOT learned)

These control **how** the model learns. Set by the engineer, not updated during training.

| Hyperparameter | What it controls | Example |
|---|---|---|
| **Learning rate** | How big each weight update step is | 0.001 |
| **Batch size** | How many samples per training step | 64 |
| **Number of layers** | Depth of the network | 96 layers |
| **Hidden dimension** | Width of each layer | 12,288 |
| **Number of attention heads** | Parallel attention computations | 96 heads |
| **Dropout rate** | Fraction of neurons randomly disabled during training (prevents overfitting) | 0.1 |
| **Epochs** | How many passes over the full dataset | 3 |
| **Optimizer** | Which algorithm updates weights | Adam, AdamW, SGD |

### The Difference

| | Parameters | Hyperparameters |
|---|---|---|
| **Who sets them?** | Learned by the model during training | Set by the engineer before training |
| **When do they change?** | Every training step (backprop) | Never during training |
| **What do they represent?** | The model's knowledge | The training recipe |
| **Analogy** | The student's brain after studying | How the student studies (hours per day, method) |

### Example

```
Hyperparameters (engineer's recipe):
  Learning rate: 0.0001
  Batch size: 512
  Layers: 80
  Hidden dim: 8192

  ↓ Training (millions of steps) ↓

Parameters (model's knowledge):
  Weights, biases, embeddings, attention weights
  → The model now knows English, code, reasoning...

Tweak hyperparameters → different training outcome → different parameter values
```
