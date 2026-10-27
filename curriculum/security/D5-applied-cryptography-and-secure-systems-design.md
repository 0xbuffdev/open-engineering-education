# D5 — Applied Cryptography & Secure Systems Design

**Track:** Security · **Prerequisite:** D1, S6, F4 · **Core** · **Time:** 5 weeks, 75 hours · **Project:** P11 protocol review
**Status:** `draft` · [status labels](../../spec/status-labels.md)

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../templates/progress.md)

## Purpose

Learn to use cryptography correctly without inventing primitives. You will choose protocols for a threat model, manage keys and nonces, implement with vetted libraries, verify against test vectors, and review a protocol for missing authentication or context binding.

## Outcomes

You can:

- distinguish encryption, MAC, hash, signature, KDF, and AEAD;
- choose primitives and parameters for a stated threat model;
- explain nonce/key lifecycle, rotation, and compromise recovery;
- implement a small protocol with a vetted library;
- bind context with associated data;
- validate formats and reject invalid inputs;
- explain replay, downgrade, and key-substitution attacks;
- review a transcript for authentication and freshness;
- avoid home-grown crypto and unsafe defaults;
- state the security claims the design does not provide.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| *Serious Cryptography* (Aumasson, 2nd ed., 2024) | Ch. **1–12** | Symmetric, public-key, TLS, crypto misuse |
| *Cryptography Engineering* (Ferguson, Schneier, Kohno) | Ch. **1–8, 11–12** (selected) | Protocol and key management |
| [NIST SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final) | GCM specification/usage | AEAD details |
| [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446) (TLS 1.3) | Overview, handshake, key schedule | Real protocol |
| [libsodium docs](https://doc.libsodium.org/) | AEAD, key exchange, signatures | Safe APIs |
| [OpenSSL EVP docs](https://docs.openssl.org/master/man7/evp.7/) | AEAD/key derivation | Alternative API |
| [OWASP Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) | Full | Storage guidance |
| [Project Wycheproof](https://github.com/C2SP/wycheproof) | Selected test vectors | Edge-case validation |

## Modules

### 1. Cryptographic primitives

- cryptographic randomness;
- hashes and collision resistance;
- MACs and constant-time comparison;
- symmetric encryption and modes;
- AEAD (AES-GCM, ChaCha20-Poly1305);
- key derivation (HKDF, Argon2id);
- public-key encryption and signatures;
- key exchange and forward secrecy;
- post-quantum awareness.

### 2. Key and nonce management

- key generation, storage, rotation, retirement;
- separation by purpose;
- nonce uniqueness and failure;
- key compromise recovery;
- envelope encryption;
- hardware/OS keystores;
- secrets in config/logs;
- backup and deletion.

### 3. Protocol design

- threat model and security goals;
- message framing and canonical encoding;
- authentication and associated data;
- freshness, replay, and ordering;
- session establishment;
- downgrade and version negotiation;
- error handling and side channels;
- transcript binding;
- test vectors and interoperability.

### 4. Correct implementation

- use vetted libraries;
- avoid ECB, static IVs, nonce reuse, and unauthenticated encryption;
- constant-time operations;
- input validation and length limits;
- secure random sources;
- zeroization limitations;
- memory and secret handling;
- dependency and version pinning.

### 5. Review and verification

- protocol transcript review;
- key lifecycle review;
- test vectors;
- negative tests;
- cryptographic storage review;
- common pitfalls (JWT, TLS, password hashing);
- audit and formal verification awareness;
- what a review cannot prove.

## Labs

### Lab 1 — Primitive map

Choose a scenario (secure messaging, file storage, API tokens). Select primitives and parameters, and justify each. Explain what a hash does not provide and why encryption alone is insufficient.

### Lab 2 — AEAD protocol

Using libsodium or OpenSSL, implement a small local protocol with:

- a unique nonce per message;
- associated data binding the sender/recipient/context;
- length-prefixed framing;
- authentication failure handling;
- test vectors and negative tests.

### Lab 3 — Key lifecycle

Design key generation, storage, rotation, compromise recovery, and deletion for the protocol. Implement a local key store abstraction. Test replay and a wrong-key failure.

### Lab 4 — Misuse lab

In a safe local test, demonstrate why nonce reuse, ECB, unauthenticated encryption, or a missing context binding is dangerous. Do not implement a production attack tool. Show the failure with test vectors and explain the fix.

### Lab 5 — Protocol review

Review a supplied protocol transcript or your own. Identify missing authentication, freshness, context binding, or error handling. Write findings with severity and concrete fixes. Include one thing the protocol does well.

## Exercises

1. Compare a hash, MAC, and signature.
2. Explain AEAD's authentication guarantee.
3. Explain nonce reuse in GCM or ChaCha20-Poly1305.
4. Choose a password-hashing scheme and parameters.
5. Derive keys with HKDF for two purposes.
6. Explain forward secrecy.
7. Identify a replay in a transcript.
8. Explain why `random` is not a CSPRNG.
9. Compare JWT validation pitfalls.
10. State what a test vector does not prove.

## Project increment — P11 protocol review

Produce:

- a threat model and security goals;
- primitive/parameter rationale;
- key and nonce lifecycle;
- implementation with a vetted library;
- test vectors and negative tests;
- protocol review findings and fixes;
- residual-risk statement.

**Brief:** [P11 — authorized-assessment](../projects/project-ladder.md#p11--authorized-assessment)

## Exit check

- [ ] select primitives from requirements, not fashion;
- [ ] implement AEAD with unique nonces and associated data;
- [ ] explain key rotation and compromise recovery;
- [ ] demonstrate a misuse failure and its fix;
- [ ] review a transcript for authentication/freshness;
- [ ] state what the design does not protect against;
- [ ] use only vetted implementations.

## Common failure modes

- Inventing a primitive or mode.
- Reusing a nonce.
- Using encryption without authentication.
- Using ECB or a static IV.
- Deriving keys with a plain hash.
- Comparing secrets with `==` in a timing-sensitive context.
- Logging keys or plaintext.
- Treating TLS as a complete application-security solution.
- Claiming "military-grade" or "unbreakable".

## Evidence to commit

- `labs/security/D5/` with primitive map, AEAD implementation, key lifecycle, misuse lab, protocol review
- P11 protocol review
- `notes/security/D5/summary.md`

## Optional depth

- *Real-World Cryptography* (Wong).
- *Introduction to Modern Cryptography* (Katz & Lindell), selected chapters.
- Noise Protocol Framework.
- OWASP Secrets Management Cheat Sheet.
- Signal Protocol and MLS specifications (selected).
