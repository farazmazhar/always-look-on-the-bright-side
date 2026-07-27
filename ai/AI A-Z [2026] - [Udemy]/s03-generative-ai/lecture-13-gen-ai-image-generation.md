# Lecture 13 — Generative AI for Image Generation

## Three Modalities

| Direction | What it does | Example |
|---|---|---|
| **Text → Image** | Generate image from text description | "A wolf sitting on a cloud playing guitar" → image |
| **Image → Text** | Describe an image in words (captioning) | Upload photo → "A dog running on a beach at sunset" |
| **Image → Image** | Transform one image into another | Sketch → photorealistic render; day scene → night scene; inpainting, style transfer |

## Diffusion Models

One of the leading approaches to generative image models (used in Stable Diffusion, DALL-E, Midjourney).

### Forward Diffusion (Training)

Take a real image and gradually add noise over many steps until it becomes pure random noise. The model learns to reverse this process.

```
Original image → +noise → +noise → +noise → ... → Pure noise
```

### Reverse Diffusion / Denoising (Image Generation)

Start with pure noise and gradually remove it, step by step, guided by the text prompt.

```
Pure noise → -noise → -noise → -noise → ... → Generated image
```

> The model learns: "given a noisy image at step t, predict what the noise looks like, so I can subtract it."

### Examples

| Prompt | Process |
|---|---|
| `"A cyberpunk cat in a neon city"` | Noise → denoise guided by "cyberpunk" + "cat" + "neon city" → final image |
| Image-to-image: sketch of a chair + `"leather armchair, photorealistic"` | Noisy sketch → denoise guided by prompt → rendered chair |
