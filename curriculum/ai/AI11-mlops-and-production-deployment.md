# AI11 — MLOps & Production Deployment

**Track:** AI & ML · **Prerequisite:** AI7, AI9 · **Core** · **Time:** 5 weeks, 75 hours · **Project:** P9 deployment/rollback
**Status:** `draft` · [status labels](../../spec/status-labels.md)

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../templates/progress.md)

## Purpose

Operate a model system in production: version data and models, package an environment, deploy changes safely, monitor quality and drift, and roll back without losing evidence. This course turns an experiment into a service someone can own.

## Outcomes

You can:

- define lineage across data, code, configuration, model, and evaluation;
- package a model/service with locked dependencies and reproducible builds;
- design offline, online, and operational metrics;
- implement model/data/config versioning and promotion gates;
- deploy a canary and roll back;
- monitor drift, skew, latency, errors, and cost;
- define an SLO and alert that reflects user impact;
- write a runbook for the top failure modes;
- audit secrets, permissions, and supply-chain boundaries;
- distinguish a model regression from a system or data regression.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| [Designing Machine Learning Systems](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/) (Huyen, 2022) | Ch. **7–10** | Deployment, drift, continual learning, infrastructure |
| [Google ML Test Score](https://research.google/pubs/pub46555/) | Full | Production readiness rubric |
| [Hidden Technical Debt in ML Systems](https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems.pdf) | Full | System-level risks |
| [Kubernetes docs](https://kubernetes.io/docs/) | Deployments, probes, autoscaling, config | Deployment substrate |
| [OpenTelemetry docs](https://opentelemetry.io/docs/) | Metrics, traces, logs | Observability |
| [SLSA](https://slsa.dev/) and [Sigstore](https://www.sigstore.dev/) | Overview | Supply-chain integrity |
| S15 | SLOs, incidents, postmortems | Operations discipline |

## Modules

### 1. Lineage and reproducibility

- data version and schema;
- code commit and container digest;
- configuration and feature flags;
- model artifact and tokenizer;
- evaluation dataset/version;
- environment lockfile;
- promotion record;
- retention and deletion.

### 2. Packaging and deployment

- model artifacts and formats;
- dependency locking;
- multi-stage containers;
- non-root runtime;
- resource requests/limits;
- model loading and warm-up;
- health/readiness;
- canary and blue/green;
- rollback and roll-forward.

### 3. Monitoring

- operational: latency, errors, saturation, cost;
- data: schema, missingness, ranges, drift;
- model: calibration, score distribution, delayed labels;
- business/user outcomes;
- skew between training and serving;
- alert design and runbooks;
- dashboards that answer questions.

### 4. Drift and continual learning

- covariate shift, label shift, concept drift;
- detection methods and false positives;
- delayed ground truth;
- retraining triggers;
- shadow deployment;
- feedback loops and bias amplification;
- approval and rollback.

### 5. Production readiness

- ML test score categories;
- ownership and on-call;
- SLO/error budget;
- incident response;
- backup/restore for model state;
- security and least privilege;
- privacy and retention;
- cost controls;
- documentation.

## Labs

### Lab 1 — Lineage manifest

Create a manifest that maps every P9 artifact: data hash, split, code commit, config, model hash, tokenizer, evaluation set, metrics, and container digest. Prove two runs with the same manifest produce the same evaluation result.

### Lab 2 — Package and deploy

Package P9 with a locked environment, non-root container, probes, limits, secrets via environment/secret store, and a local Kubernetes/Compose deployment. Record the exact commands in a runbook.

### Lab 3 — Canary and rollback

Deploy a new model/config to a canary. Compare quality and operational metrics. Inject a regression, detect it via the predeclared gate, and roll back. Preserve the bad artifact and incident timeline for analysis.

### Lab 4 — Drift simulation

Simulate schema drift, feature shift, and label delay. Show which monitors fire, which do not, and what an operator should do. Avoid claiming that a drift detector proves quality degradation.

### Lab 5 — Production-readiness review

Score P9 against a documented subset of the ML Test Score. For each missing item, write an owner and a concrete next step. Include a threat model for model/data supply chain and a cost estimate.

## Exercises

1. Define lineage for a model trained yesterday.
2. Explain offline versus online evaluation.
3. Design a canary gate with a rollback threshold.
4. Distinguish data drift from concept drift.
5. Explain why delayed labels complicate monitoring.
6. Write an alert for a model-quality regression.
7. Identify three secrets/supply-chain risks in a pipeline.
8. Define a retraining trigger and approval path.
9. Explain model skew with an example.
10. State what a green dashboard does not prove.

## Project increment — P9 deployment/rollback

Add:

- lineage manifest and promotion record;
- locked image and local deployment;
- quality/operational dashboard and alerts;
- canary plus tested rollback;
- drift/label-delay monitoring;
- runbook, readiness review, and cost note.

**Brief:** [P9 — doc-compass](../projects/project-ladder.md#p9--doc-compass)

## Exit check

- [ ] reproduce the deployed model from a lineage manifest;
- [ ] show a canary gate and a rollback with timestamps;
- [ ] demonstrate a monitor firing for a real injected change;
- [ ] distinguish model, data, and system regressions;
- [ ] state the SLO and alert-to-runbook path;
- [ ] name the top residual production risk and its owner.

## Common failure modes

- Versioning code but not data, tokenizer, or config.
- Deploying `latest` with no digest.
- Monitoring only uptime while quality collapses.
- Treating drift as proof of degradation.
- Retraining automatically without approval or rollback.
- Logging sensitive inputs for "observability".
- A rollback that was never tested.
- No owner for the model after launch.

## Evidence to commit

- `labs/ai/AI11/` with lineage manifest, deployment, canary/rollback log, drift simulation, readiness review
- P9 deployment manifests, dashboard, alerts, runbook
- `notes/ai/AI11/summary.md`

## Optional depth

- *Reliable Machine Learning* (Chen et al.).
- *Machine Learning Design Patterns* (Lakshmanan et al.).
- Kubeflow, MLflow, or Weights & Biases docs (choose one).
- Feature-store design (Feast docs).
- *Accelerate* (Forsgren et al.) for delivery metrics.
