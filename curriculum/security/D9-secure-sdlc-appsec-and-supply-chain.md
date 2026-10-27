# D9 — Secure SDLC, AppSec & Supply Chain

**Track:** Security · **Prerequisite:** D1, D3 · **Core** · **Time:** 4 weeks, 60 hours · **Project:** P10 secure SDLC review
**Status:** `draft` · [status labels](../../spec/status-labels.md)

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../templates/progress.md)

## Purpose

Move security into design, code review, CI, and the software supply chain. You will build a lightweight secure-development workflow with threat modeling, automated checks, dependency controls, artifact signing, and a review process that developers can actually use.

## Outcomes

You can:

- map security activities across the software lifecycle;
- write security requirements and abuse cases;
- perform a design and code security review;
- integrate SAST, dependency scanning, secret scanning, and DAST sensibly;
- manage false positives and developer friction;
- produce and consume an SBOM;
- pin, verify, and sign dependencies/artifacts;
- define branch protection and release gates;
- assess a third-party dependency or vendor;
- measure whether the process improves security.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| [NIST SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) | Full | Secure software development practices |
| [OWASP SAMM](https://owaspsamm.org/) | Governance, design, implementation, verification | Program maturity |
| [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | Level 1–2 selected | Requirements/verification |
| [SLSA](https://slsa.dev/) | Levels, provenance, build | Supply-chain integrity |
| [Sigstore docs](https://docs.sigstore.dev/) | Cosign, signing, verification | Artifact trust |
| [CycloneDX](https://cyclonedx.org/) or [SPDX](https://spdx.dev/) | SBOM formats | Inventory |
| *Secure by Design* (Johnsson et al.) | Selected chapters | Design heuristics |
| [OWASP Dependency-Check / Dependabot docs] | Configuration | Dependency risk |

## Modules

### 1. Secure development lifecycle

- roles and responsibilities;
- security requirements;
- design review and threat modeling;
- secure coding standards;
- code review;
- testing and verification;
- release and response;
- metrics and maturity.

### 2. Design and code review

- trust boundaries and authorization;
- input validation and output encoding;
- secrets and configuration;
- error handling and logging;
- dependency and license review;
- cryptography review (use D5);
- concurrency and resource limits;
- review checklist and evidence.

### 3. Automated security testing

- SAST strengths and false positives;
- dependency/SCA scanning;
- secret scanning;
- DAST and IAST;
- fuzzing (connect D2);
- container/image scanning;
- policy-as-code;
- developer workflow and triage.

### 4. Supply chain

- dependency pinning and lockfiles;
- provenance and reproducible builds;
- SBOM generation and use;
- artifact signing and verification;
- registry controls;
- build isolation;
- maintainer/typosquatting risk;
- incident response for a compromised dependency.

### 5. Release and operations

- branch protection;
- required checks;
- code owners;
- environment promotion;
- secrets in CI;
- least-privilege tokens;
- rollback;
- vulnerability disclosure;
- patch SLAs.

## Labs

### Lab 1 — Security requirements

Take P1/P4/P9 and write five security requirements with acceptance tests. Map each to a threat and an ASVS/SSDF practice. Reject one vague requirement and rewrite it.

### Lab 2 — Code review

Review a local codebase for authorization, injection, secrets, error handling, and dependency risk. Produce three validated findings and two verified controls. Include a suggested patch and test.

### Lab 3 — CI security pipeline

Add to a local repository:

- dependency audit;
- secret scanning;
- SAST;
- tests;
- SBOM generation;
- artifact signing (or a documented local alternative).

Demonstrate a failing check and a passing fix. Measure runtime and triage burden.

### Lab 4 — Supply-chain verification

Generate an SBOM, pin a dependency, and verify an artifact digest/signature. Simulate a compromised dependency or typosquat and show the detection path. Do not publish malicious packages.

### Lab 5 — Secure SDLC review

Assess the repository against a subset of SAMM/SSDF. Produce a gap register with owner, risk, and next action. Include one metric that would show improvement and one gaming risk.

## Exercises

1. Write an abuse case for a file upload.
2. Map three SSDF practices to CI checks.
3. Explain SAST false positives and triage.
4. Compare SBOM formats.
5. Explain build provenance.
6. Design a patch SLA by severity.
7. Review a dependency for maintenance risk.
8. Explain least privilege for CI tokens.
9. Define a release gate that does not block emergencies.
10. State what signing does not guarantee.

## Project increment — P10 secure SDLC review

Produce:

- security requirements and acceptance tests;
- code review with validated findings;
- CI security pipeline and evidence;
- SBOM and artifact verification;
- dependency/vendor risk assessment;
- gap register and patch policy.

**Brief:** [P10 — secure-review](../projects/project-ladder.md#p10--secure-review)

## Exit check

- [ ] map security activities to the lifecycle;
- [ ] show a design/code review with a verified fix;
- [ ] demonstrate a CI check failing and passing;
- [ ] produce and inspect an SBOM;
- [ ] verify an artifact/dependency boundary;
- [ ] define release gates and emergency handling;
- [ ] state what automation cannot catch.

## Common failure modes

- Adding scanners without triage ownership.
- Blocking every build on low-value findings.
- Treating an SBOM as a security guarantee.
- Signing an artifact built from unreviewed code.
- Storing long-lived cloud credentials in CI.
- Ignoring transitive dependencies.
- Measuring finding count instead of risk reduction.
- No process for a compromised dependency.

## Evidence to commit

- `labs/security/D9/` with requirements, review, CI config, SBOM, verification, gap register
- P10 secure SDLC review
- `notes/security/D9/summary.md`

## Optional depth

- *Building Secure and Reliable Systems* (Google), selected chapters.
- *Agile Application Security* (Bell et al.).
- OpenSSF Scorecard and Best Practices.
- in-toto and reproducible builds.
- NIST SP 800-161 (cyber supply-chain risk).
