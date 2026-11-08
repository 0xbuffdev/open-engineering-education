## SEC5 — Applied Cryptography & Secure Protocols

**Duration:** 5 weeks
**Expected workload:** 10–15 focused hours/week
**Prerequisite:** SEC1

### Overview

Learn practical cryptography from security goals through symmetric encryption, AEAD, hashes, MACs, key exchange, signatures, and TLS. The course emphasizes correct library use and protocol design rather than implementing primitives yourself.

### Prerequisites

**SEC1 — Security Foundations & Threat Modeling**

**Kind:** `course`

### Learning outcomes

By the end of the course, you will be able to:

- Map security requirements to appropriate cryptographic primitives and protocols.
- Explain randomness, key management, nonces, authentication, confidentiality, and integrity.
- Use established cryptographic libraries without inventing primitives.
- Analyze common protocol failures such as nonce reuse and unauthenticated encryption.
- Document and test a small secure protocol component.


### Modules

#### Module 1 — Security Goals & Randomness



### Module outcomes

By the end of this module, the learner can:

- Explain **Confidentiality, integrity, authenticity, and availability** in the context of the course.
- Apply **Entropy and secure randomness** in a problem, implementation, experiment, or design decision.

1. **Confidentiality, integrity, authenticity, and availability**
   - kind: `lesson`
2. **Entropy and secure randomness**
   - kind: `lesson`
3. **Checkpoint: cryptographic goals**
   - kind: `test`

4. **Micro-lab: Identify where predictable randomness would break a protocol.**
   - kind: `lab`
#### Module 2 — Symmetric Protection



### Module outcomes

By the end of this module, the learner can:

- Explain **Symmetric encryption and AEAD** in the context of the course.
- Apply **Hashes and MACs** in a problem, implementation, experiment, or design decision.

1. **Symmetric encryption and AEAD**
   - kind: `lesson`
2. **Hashes and MACs**
   - kind: `lesson`
3. **Checkpoint: symmetric primitives**
   - kind: `test`

4. **Micro-lab: Choose the primitive that matches a stated security goal.**
   - kind: `lab`
#### Module 3 — Public-Key Cryptography



### Module outcomes

By the end of this module, the learner can:

- Explain **Key exchange and public-key encryption** in the context of the course.
- Apply **Digital signatures and trust** in a problem, implementation, experiment, or design decision.

1. **Key exchange and public-key encryption**
   - kind: `lesson`
2. **Digital signatures and trust**
   - kind: `lesson`
3. **Checkpoint: asymmetric cryptography**
   - kind: `test`

4. **Micro-lab: Trace a simplified key-exchange and signature verification flow.**
   - kind: `lab`
#### Module 4 — Protocol Design & Key Management



### Module outcomes

By the end of this module, the learner can:

- Explain **TLS concepts and secure protocol composition** in the context of the course.
- Apply **Nonce handling, key management, and failure behavior** in a problem, implementation, experiment, or design decision.

1. **TLS concepts and secure protocol composition**
   - kind: `lesson`
2. **Nonce handling, key management, and failure behavior**
   - kind: `lesson`
3. **Checkpoint: protocol correctness**
   - kind: `test`

4. **Micro-lab: Inspect a protocol transcript and identify where nonce reuse or key misuse would matter.**
   - kind: `lab`
#### Module 5 — Secure Protocol Component



1. **Build and evaluate a protocol component using established cryptographic libraries only**
   - kind: `lab`

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

---

