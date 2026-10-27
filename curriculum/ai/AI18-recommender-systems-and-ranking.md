# AI18 — Recommender Systems & Ranking

**Track:** AI & ML · **Prerequisite:** AI3 · **Elective** · **Time:** 4 weeks, 60 hours · **Project:** elective
**Status:** `draft` · [status labels](../../spec/status-labels.md)

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../templates/progress.md)

## Purpose

Learn how recommender and ranking systems turn user-item interactions into ordered predictions, and why offline metrics often fail to predict online value. You will build a reproducible ranking baseline and evaluate it with the right splits and metrics.

## Outcomes

You can:

- frame recommendation as retrieval, ranking, or scoring;
- build popularity and content baselines;
- implement collaborative filtering and matrix factorization;
- explain implicit versus explicit feedback;
- use leave-one-out, temporal, and user-based splits correctly;
- evaluate with recall@k, precision@k, MAP, MRR, and nDCG;
- analyze cold start, popularity bias, and filter bubbles;
- design an offline-to-online evaluation plan;
- state privacy and fairness risks.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| [Recommender Systems: The Textbook](https://www.springer.com/gp/book/9783319296579) (Aggarwal) | Ch. **1–6** | Foundations, neighborhood, matrix factorization |
| [Recommender Systems Handbook](https://link.springer.com/book/10.1007/978-1-0716-2197-4) (3rd ed.) | Selected chapters | Advanced methods and evaluation |
| [Deep Learning for Recommender Systems](https://arxiv.org/abs/1707.07435) | Full | Neural architectures |
| [BPR paper](https://arxiv.org/abs/1205.2618) | Full | Pairwise ranking |
| [nDCG / ranking metrics](https://dl.acm.org/doi/10.1145/582415.582418) | Full | Metric semantics |
| [Microsoft Recommenders](https://github.com/recommenders-team/recommenders) | Selected notebooks | Reference implementation |

## Modules

1. **Problem framing** — retrieval vs ranking, implicit/explicit feedback, pointwise/pairwise/listwise, business constraints.
2. **Baselines** — popularity, recent, content-based, association rules; why baselines are mandatory.
3. **Collaborative filtering** — user/item neighborhoods, cosine/Jaccard, matrix factorization, ALS, BPR.
4. **Neural and sequence models** — embeddings, two-tower retrieval, wide-and-deep, session-based models, transformers for sequential recommendation.
5. **Evaluation** — offline splits, leakage, recall@k, nDCG, MAP, coverage, diversity, novelty, cold start, popularity bias.
6. **Production** — candidate generation, ranking, re-ranking, exploration, feedback loops, logging, privacy, fairness.

## Labs

### Lab 1 — Baselines and splits

Choose a licensed, non-sensitive interaction dataset. Build popularity and content baselines. Compare random, temporal, and leave-one-out splits and show how the split changes the result.

### Lab 2 — Matrix factorization

Implement/implicit ALS or BPR. Tune one regularizer with validation. Report recall@k and nDCG@k against baselines, plus coverage and popularity bias.

### Lab 3 — Two-tower retrieval

Build a small two-tower model or a content embedding baseline. Evaluate retrieval separately from ranking. Show one cold-start failure.

### Lab 4 — Ranking and diversity

Add a re-ranker or diversity constraint. Measure the trade-off between relevance and diversity/coverage. Explain who benefits and who loses.

### Lab 5 — Evaluation audit

Audit your offline evaluation: leakage, negative sampling, metric mismatch, popularity bias, and reproducibility. Propose an online experiment and guardrail metrics. Do not claim online impact from offline results.

## Exercises

1. Compare explicit and implicit feedback.
2. Compute recall@k and nDCG@k for a toy list.
3. Explain negative sampling bias.
4. Design a temporal split.
5. Explain cold start for users and items.
6. Compare pointwise and pairwise losses.
7. Identify popularity feedback loops.
8. Design a diversity metric.
9. Explain one privacy risk.
10. State what offline evaluation cannot prove.

## Project increment (optional)

Add a ranking or retrieval-reranking experiment to P7 or P9. Compare against a popularity or lexical baseline with nDCG/recall, report cold-start and popularity bias, and keep the evaluation split honest. This is an elective extension, not a new ladder project.

## Exit check

- [ ] build and compare at least two baselines;
- [ ] use a leakage-resistant split;
- [ ] report ranking and coverage metrics;
- [ ] explain cold start and popularity bias with evidence;
- [ ] state the offline-to-online gap;
- [ ] document privacy/fairness limits.

## Common failure modes

- Random splits for temporal interactions.
- Evaluating with the same negatives used for training.
- Reporting only nDCG and ignoring coverage.
- Ignoring popularity bias.
- Tuning on the test set.
- Claiming business impact from offline metrics.
- Using sensitive attributes without justification.

## Evidence to commit

- `labs/ai/AI18/` with baselines, matrix factorization, two-tower, ranking study, audit
- `notes/ai/AI18/summary.md`
- dataset license and preprocessing record

## Optional depth

- *Practical Recommender Systems* (Falk).
- *Recommender Systems Handbook* evaluation and fairness chapters.
- LightFM, Implicit, and TorchRec docs.
- Sequential recommendation papers (SASRec, BERT4Rec).
- Counterfactual evaluation and off-policy estimation.
