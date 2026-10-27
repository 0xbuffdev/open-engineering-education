# AI14 — Generative & Multimodal Models

**Track:** AI & ML · **Prerequisite:** AI6 · **Elective** · **Time:** 5 weeks, 75 hours · **Project:** elective
**Status:** `draft` · [status labels](../../spec/status-labels.md)

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../templates/progress.md)

## Purpose

Understand how models generate images, audio, and joint vision-language representations. You will study autoencoders, GANs, diffusion, contrastive pretraining, and multimodal evaluation, then build small generative or retrieval models.

## Outcomes

You can:

- explain latent-variable generative models and the evidence lower bound;
- explain GAN training dynamics and failure modes;
- explain denoising diffusion, noise schedules, and sampling;
- explain CLIP-style contrastive training and zero-shot classification;
- explain text-to-image conditioning and cross-attention;
- train or fine-tune a small generative/multimodal model;
- evaluate sample quality, diversity, alignment, and bias;
- state the limitations of FID/CLIP scores;
- document data licensing and provenance.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| [Deep Learning](https://www.deeplearningbook.org/) | Ch. **14, 20** | Autoencoders and deep generative models |
| [DDPM paper](https://arxiv.org/abs/2006.11239) | Full | Denoising diffusion |
| [Latent Diffusion paper](https://arxiv.org/abs/2112.10752) | Full | Stable Diffusion architecture |
| [CLIP paper](https://arxiv.org/abs/2103.00020) | Full | Contrastive vision-language pretraining |
| [GAN paper](https://arxiv.org/abs/1406.2661) and [WGAN](https://arxiv.org/abs/1701.07875) | Full | Adversarial training and stability |
| D2L | Ch. **17–18** (generative/adversarial if available) | Implementation context |
| [FID paper](https://arxiv.org/abs/1706.08500) | Full | Evaluation pitfalls |

## Modules

1. **Latent variable models** — autoencoders, VAEs, ELBO, posterior collapse, reconstruction versus sample quality.
2. **GANs** — generator/discriminator, minimax objective, mode collapse, instability, evaluation.
3. **Diffusion** — forward noising, reverse denoising, score matching intuition, samplers, guidance, latent diffusion.
4. **Multimodal** — contrastive objectives, image-text pairs, zero-shot classification, retrieval, captioning, CLIP limitations.
5. **Conditioning and control** — text conditioning, cross-attention, classifier-free guidance, ControlNet/adapters (awareness), safety filters.
6. **Evaluation and governance** — FID/IS/CLIP score limits, human evaluation, diversity, bias, memorization, consent, copyright, watermarking/provenance.

## Labs

### Lab 1 — VAE or autoencoder

Train a small autoencoder/VAE on a licensed dataset. Show reconstructions, samples, and latent interpolation. Explain one failure (blurriness, posterior collapse, or overfitting).

### Lab 2 — Diffusion on small images

Train a tiny diffusion model on low-resolution licensed images. Compare two noise schedules or samplers. Report sample quality, diversity, compute, and limitations. Do not claim parity with production models.

### Lab 3 — CLIP-style retrieval

Use a pretrained open CLIP model on a small licensed image-text set. Measure retrieval recall and zero-shot accuracy. Show failure cases and one bias/provenance limitation.

### Lab 4 — Conditioning experiment

Compare two guidance strengths or conditioning methods for a small text-to-image setup. Evaluate alignment and diversity with a predeclared rubric. Identify cherry-picking risk.

### Lab 5 — Evaluation audit

Critique FID and CLIP score on your outputs. Add a small human rubric or a retrieval-based check. State what the metrics miss and what data/licensing constraints apply.

## Exercises

1. Derive the VAE ELBO at a high level.
2. Explain mode collapse.
3. Write the diffusion forward process.
4. Explain classifier-free guidance.
5. Compare CLIP zero-shot with a supervised classifier.
6. Explain why FID depends on the reference set.
7. Identify memorization risk in image generation.
8. Design a diversity metric.
9. Explain one consent/copyright issue.
10. State what a small-scale generative result cannot prove.

## Project increment (optional)

Add one generative or multimodal experiment to P8/P9: train a small VAE or diffusion model on a licensed dataset, or build a CLIP-style image-retrieval demo. Evaluate against a trivial baseline, report compute and license, and document failure cases. This is an elective extension, not a new ladder project.

## Exit check

- [ ] explain one generative model's objective and sampling path;
- [ ] train a small model and show samples plus failures;
- [ ] evaluate retrieval/zero-shot with a labelled set;
- [ ] explain one multimodal evaluation metric's limits;
- [ ] document data license and provenance;
- [ ] state a concrete misuse/non-use boundary.

## Common failure modes

- Judging samples by cherry-picked successes.
- Treating FID as a complete quality measure.
- Training on unlicensed or private images.
- Ignoring memorization.
- Comparing guidance settings without a rubric.
- Calling CLIP similarity "understanding".
- Omitting compute and data provenance.

## Evidence to commit

- `labs/ai/AI14/` with VAE/diffusion, retrieval eval, conditioning study, evaluation audit
- `notes/ai/AI14/summary.md`
- data/model license and compute record

## Optional depth

- *Generative Deep Learning* (Foster), 2nd ed.
- Score-based generative modeling survey.
- Imagen, DALL·E 2, and Stable Diffusion papers.
- *Multimodal Machine Learning* survey.
- C2PA content provenance specification.
