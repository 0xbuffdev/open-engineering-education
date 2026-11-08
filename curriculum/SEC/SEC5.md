# SEC5 — Applied Cryptography & Secure Protocols

**Program:** SEC — Security Engineering
**Type:** `course`
**Prerequisites:** SEC1 *(legacy mapping; reconcile before activation)*
**Duration:** 5 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> **Unmigrated historical course — not OEE v0.2.0-conforming.** This educational outline was transferred from [the content repository](https://github.com/0xbuffdev/content/blob/0e14d4ff5808a4ea972206ed015a3e4737b33ad7/docs/curriculum/SEC.md) before curriculum duplication is retired. The former `test` and `lab` labels are descriptions of historical activities, not automatic OEE completion requirements. Its outcome IDs, assessment IDs, criteria, and evidence still require v0.2.0 review. Reading and purchasing mappings remain in the content repository.

## Overview

Learn practical cryptography from security goals through symmetric encryption, AEAD, hashes, MACs, key exchange, signatures, and TLS. The course emphasizes correct library use and protocol design rather than implementing primitives yourself.

## Learning outcomes

- Map security requirements to appropriate cryptographic primitives and protocols.
- Explain randomness, key management, nonces, authentication, confidentiality, and integrity.
- Use established cryptographic libraries without inventing primitives.
- Analyze common protocol failures such as nonce reuse and unauthenticated encryption.
- Document and test a small secure protocol component.

## Modules

### Module 1 — Security Goals & Randomness

#### Outcomes

By the end of this module, the learner can:

- Explain **Confidentiality, integrity, authenticity, and availability** in the context of the course.
- Apply **Entropy and secure randomness** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Confidentiality, integrity, authenticity, and availability** — `lesson`
2. **Entropy and secure randomness** — `lesson`
3. **Checkpoint: cryptographic goals** — `test`
4. **Micro-lab: Identify where predictable randomness would break a protocol.** — `lab`

### Module 2 — Symmetric Protection

#### Outcomes

By the end of this module, the learner can:

- Explain **Symmetric encryption and AEAD** in the context of the course.
- Apply **Hashes and MACs** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Symmetric encryption and AEAD** — `lesson`
2. **Hashes and MACs** — `lesson`
3. **Checkpoint: symmetric primitives** — `test`
4. **Micro-lab: Choose the primitive that matches a stated security goal.** — `lab`

### Module 3 — Public-Key Cryptography

#### Outcomes

By the end of this module, the learner can:

- Explain **Key exchange and public-key encryption** in the context of the course.
- Apply **Digital signatures and trust** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Key exchange and public-key encryption** — `lesson`
2. **Digital signatures and trust** — `lesson`
3. **Checkpoint: asymmetric cryptography** — `test`
4. **Micro-lab: Trace a simplified key-exchange and signature verification flow.** — `lab`

### Module 4 — Protocol Design & Key Management

#### Outcomes

By the end of this module, the learner can:

- Explain **TLS concepts and secure protocol composition** in the context of the course.
- Apply **Nonce handling, key management, and failure behavior** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **TLS concepts and secure protocol composition** — `lesson`
2. **Nonce handling, key management, and failure behavior** — `lesson`
3. **Checkpoint: protocol correctness** — `test`
4. **Micro-lab: Inspect a protocol transcript and identify where nonce reuse or key misuse would matter.** — `lab`

### Module 5 — Secure Protocol Component

#### Outcomes

*Outcome review pending against this course's required capabilities.*

#### Lessons

1. **Build and evaluate a protocol component using established cryptographic libraries only** — `lab`

## Completion requirements

**Pending outcome-based migration:** Preserve and review the historical tasks and project requirements below. Before adopting this course against v0.2.0, assign stable outcome and summative assessment IDs, define published work/criteria/evidence, verify full outcome coverage and safety constraints, and distinguish formative practice from required work.

### Topics

- security goals
- entropy
- randomness
- symmetric encryption
- AEAD
- hashes
- MACs
- key exchange
- public-key cryptography
- signatures
- TLS
- key management
- nonce handling

### Labs

- authenticated-encryption experiment
- nonce-reuse demonstration
- signature verification
- protocol transcript analysis

### Substantial course lab

**Secure Protocol Component**

Build a small protocol using established cryptographic libraries and document:

- threat model
- primitives
- key handling
- nonce rules
- failure behavior
- compatibility tests

Never invent cryptographic primitives.
