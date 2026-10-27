# AI15 — Reinforcement Learning & RLHF

**Track:** AI & ML · **Prerequisite:** AI7, F4 · **Elective** · **Time:** 6 weeks, 90 hours · **Project:** elective
**Status:** `draft` · [status labels](../../spec/status-labels.md)

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../templates/progress.md)

## Purpose

Learn how agents learn from reward and how human preferences are turned into training signals. You will implement core RL algorithms in small environments and study RLHF/DPO as optimization with failure modes, not as a safety guarantee.

## Outcomes

You can:

- formalize a Markov decision process;
- explain value functions, Bellman equations, and dynamic programming;
- implement tabular Q-learning and a policy-gradient method;
- explain exploration, credit assignment, and reward shaping;
- explain PPO's clipped objective and KL control;
- explain reward modelling, preference data, and DPO;
- identify reward hacking, overoptimization, and distribution shift;
- evaluate an RL/RLHF run with fixed seeds and baselines;
- state safety and compute limitations.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| [Reinforcement Learning: An Introduction](http://incompleteideas.net/book/the-book.html) (Sutton & Barto, 2nd ed.) | Ch. **1–6, 9, 13** | MDPs, tabular methods, function approximation, policy gradients |
| [Spinning Up in Deep RL](https://spinningup.openai.com/) | Intro, VPG, PPO | Practical deep RL |
| [PPO paper](https://arxiv.org/abs/1707.06347) | Full | Clipped policy optimization |
| [InstructGPT paper](https://arxiv.org/abs/2203.02155) | Full | RLHF pipeline |
| [DPO paper](https://arxiv.org/abs/2305.18290) | Full | Preference optimization without RL |
| [TRL docs](https://huggingface.co/docs/trl) | PPO/DPO trainers | Implementation |
| [Deep RL doesn't work yet](https://www.alexirpan.com/2018/02/14/rl-hard.html) | Full | Honest limitations |

## Modules

1. **MDPs** — states, actions, rewards, transitions, policies, returns, discounting.
2. **Value-based methods** — Bellman equations, policy evaluation, policy iteration, value iteration, TD learning, Q-learning, exploration.
3. **Policy gradients** — REINFORCE, baselines, variance reduction, actor-critic, GAE.
4. **PPO and trust regions** — importance sampling, clipping, KL penalties, advantage estimation, hyperparameter sensitivity.
5. **RLHF** — demonstration data, reward model, preference pairs, Bradley–Terry, PPO with KL, DPO, rejection sampling.
6. **Failure analysis** — reward hacking, specification gaming, overoptimization, distribution shift, sparse reward, reproducibility, safety.

## Labs

### Lab 1 — Tabular MDP

Implement value iteration and Q-learning on a small gridworld. Compare exploration strategies. Show a case where the learned policy exploits a reward-design flaw.

### Lab 2 — Policy gradient

Implement REINFORCE with and without a baseline on a small environment (e.g., CartPole). Plot return variance and explain the baseline's effect.

### Lab 3 — PPO

Train PPO on a small environment. Ablate clipping or advantage normalization. Report seeds, compute, and failure cases. Do not claim general RL competence from one task.

### Lab 4 — Preference model

Train a small reward model or preference classifier on benign synthetic preferences. Evaluate held-out preference accuracy and show one spurious-correlation failure.

### Lab 5 — RLHF/DPO comparison

Compare SFT-only with DPO (or a simulated preference objective) on a tiny model/dataset. Use a fixed evaluation rubric and a KL/quality trade-off. Record compute and safety limitations.

## Exercises

1. Write the Bellman optimality equation.
2. Compute a Q-learning update by hand.
3. Explain exploration versus exploitation.
4. Derive the policy-gradient estimator.
5. Explain PPO clipping with a numerical example.
6. Explain the role of KL in RLHF.
7. Compare RLHF and DPO.
8. Identify three reward-hacking routes.
9. Design a held-out preference evaluation.
10. State why a small RL run cannot prove alignment.

## Project increment (optional)

Add a preference-optimization experiment to P8: compare SFT with DPO or a small PPO/RLHF run under the same evaluation budget. Report reward hacking, regressions, and the cost of the extra pipeline. This is an elective extension, not a new ladder project.

## Exit check

- [ ] formulate a task as an MDP;
- [ ] implement a tabular and a policy-gradient method;
- [ ] explain PPO's objective and one instability;
- [ ] build a preference dataset and evaluate a preference model;
- [ ] compare RLHF/DPO-style training with a fixed rubric;
- [ ] state reward-hacking and safety limits.

## Common failure modes

- Comparing returns across different environments/seeds.
- Tuning on the evaluation episodes.
- Reward shaping that creates loopholes.
- Ignoring variance across seeds.
- Treating human preference as ground truth.
- Claiming alignment from a toy run.
- Omitting compute and data provenance.

## Evidence to commit

- `labs/ai/AI15/` with MDP, policy gradient, PPO, preference model, comparison
- `notes/ai/AI15/summary.md`
- seeds, environment versions, compute record

## Optional depth

- *Algorithms for Decision Making* (Kochenderfer et al.).
- *Deep Reinforcement Learning Hands-On* (Lapan).
- GAE, TRPO, SAC, and AlphaZero papers.
- Constitutional AI and RLAIF papers.
- Reward-model overoptimization scaling laws.
