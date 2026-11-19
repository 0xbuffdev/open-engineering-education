# SEC5 — Applied Cryptography & Secure Protocols

**Program:** SEC — Security Engineering
**Type:** `course`
**Prerequisites:** [SEC1](SEC1.md)
**Duration:** 12–16 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** approximately 10–14 focused hours/week (provisional; 120–224 hours)

> [Security Engineering](README.md) · [Design guide](../DESIGN-GUIDE.md) · [Course format](../../spec/course-format.md) · [Evidence rules](../../spec/evidence-rules.md)

## Overview

**Cryptographic security is a property of the entire use of a primitive: its keys, randomness, message boundaries, identities, versioning and failure behavior.** SEC5 teaches learners to turn concrete confidentiality, integrity, authenticity and trust requirements into evidence-backed uses of established cryptographic libraries and protocols. They will distinguish protection goals and adversary capabilities, implement bounded authenticated data protection, reason about key derivation and credential storage, inspect asymmetric identity and key-establishment flows, analyze composition mistakes, and defend a protocol component against an unfamiliar change. Correct-looking ciphertext, a valid signature and an encrypted connection are not comprehensive security guarantees.

**Context and applications.** Cryptography supports protected records, authenticated messages, software signatures, credentials, transport sessions, encrypted backups and inter-service communication. The same algorithm can fail when a nonce repeats, the wrong message context is authenticated, a key is reused across purposes, an identity is not bound to a peer, plaintext leaks on authentication failure, or old encrypted data becomes unreadable after rotation. The analysis must distinguish what a mathematically defined primitive offers from the guarantees established by its implementation and use. Security strength depends on selection, parameter and key-management assumptions; neither a home-built cipher nor an untested protocol composition is suitable as a production security claim.

**Prerequisite and course boundaries.** [SEC1](SEC1.md) establishes permission, protected assets, trust models, abuse reasoning, threat prioritization and independent security oracles. Its underlying SEF preparation supplies programming and basic mathematical reasoning. SEC5 introduces the additional cryptographic vocabulary and mathematical models needed for application; it does not assume prior number-theory or a specialist cryptography course. [APP1](../APP/APP1.md) explains HTTPS/TLS at the network-to-browser level, while [SEC4](SEC4.md) tests deployed TLS certificate, hostname and proxy trust configuration. SEC5 instead explains **why** authenticated key establishment, transcript binding, key schedules, replay/downgrade protections and failure rules make a protocol sound or unsound under stated assumptions. No SEC4, APP1, advanced math elective or particular implementation language becomes a hidden direct prerequisite. [SEC2](SEC2.md) addresses web-session and application authorization failures; SEC6 owns cloud secret services and deployment supply chains. Do not duplicate their complete projects.

**Free, independent reference environment.** A learner-controlled local Python environment is a suitable option because standard-library `secrets`, `hmac`, `hashlib` and `unittest` support relevant demonstrations; *the Python standard library does not supply the required general-purpose AEAD and signature APIs*. Use a maintained, freely available, pinned and documented cryptographic library such as Python `cryptography` for AES-GCM or ChaCha20-Poly1305, HKDF, Ed25519 and X25519 where supported, or an equivalent reviewed library with the same substantive properties. A free Argon2id library, or a supported `hashlib.scrypt` implementation, can demonstrate the password-hashing assessment. Tooling may be provisioned in advance; record pinned versions and observed library capabilities, and provide offline-replayable fixtures and known-answer test vectors after setup. No paid service, HSM, network account, public CA, dedicated accelerator, quantum computer or proprietary test oracle is required. Do not force implementations to expose a cryptographic algorithm their installed version does not support.

**Security and test constraints.** All assessed keys, credentials and messages are synthetic and confined to a locally owned fixture. Use OS-backed cryptographic random generation for live test-key creation; use deterministic **test-only** known-answer vectors separately, not a fixed production RNG seed. Never print, commit or submit private production keys or actual user passwords. Wrong-key, changed-ciphertext, invalid-tag and replay tests must establish explicit reject behavior; a decryption routine must not deliver unauthenticated plaintext to its caller. A controlled demonstration of nonce reuse is by **analysis or supplied vectors**, not by creating a reusable insecure application artifact. If an experiment explores a defective interface, isolate it as a disposable fixture and make the corrected implementation authoritative. Avoid timing/side-channel claims based on noisy microbenchmarks or invented cryptanalytic results.

**Scope, assessment and workload.** SEC5 assesses the disciplined engineering of a **small local protected-record and authenticated-message component**, plus independent protocol and lifecycle analysis—not the invention of new cryptographic primitives, a full TLS/HPKE stack, custom authenticated key exchange, an operational public PKI or post-quantum algorithm implementation. Four summative evaluations share fixtures and a versioned implementation where useful, each with its own success criteria. Optional lesson experiments are formative only. The 12–16-week planning range at 10–14 hours/week reflects reading formal guarantees, configuring a vetted library, constructing independent vectors, assessing failure boundaries, implementing the component, analyzing asymmetric transcripts, key rotation and unfamiliar variants. It is not learner-tested duration or evidence of competence; the course remains `draft`.

## Learning outcomes

- **SEC5-O1:** Translate a bounded security problem into precise cryptographic confidentiality, integrity, authenticity, identity, freshness and availability claims, identifying the adversary's control, non-cryptographic obligations, trust anchors and evidence that would falsify a proposed guarantee.
- **SEC5-O2:** Select and use supported cryptographic random generation, keys and unique per-key nonces with explicit key/nonce length and usage policies; distinguish unpredictability from uniqueness, reproducible test vectors from production randomness, and uncertain entropy from a demonstrable protocol property.
- **SEC5-O3:** Use a vetted authenticated-encryption API correctly for real local messages, binding associated data to the intended record or protocol context and rejecting wrong keys, corrupted ciphertext, changed context, truncation and invalid tags without exposing unauthenticated plaintext.
- **SEC5-O4:** Analyze nonce collisions/reuse, counters across restarts and writers, AEAD invocation/size limits, message ordering and replay; design and test a justified nonce-state and freshness policy appropriate to a declared bounded environment.
- **SEC5-O5:** Distinguish cryptographic hashes, keyed MACs, digital signatures, authenticated encryption and password verifiers by actual security properties, then implement and test appropriate integrity authentication and rejection with safe comparisons.
- **SEC5-O6:** Choose and verify a salted, tunable password-hashing or password-based derivation scheme, justify actual runtime/memory limits, and separate low-entropy passwords from high-entropy key material and from fast hash/HKDF use.
- **SEC5-O7:** Use a standard extract-and-expand key derivation API with correctly understood input key material, salt, context-specific information and output lengths; demonstrate separated purpose keys and identify where HKDF cannot create missing input entropy or replace a password KDF.
- **SEC5-O8:** Use a reviewed digital-signature API to verify an explicitly scoped message and trusted public-key identity, detecting tampering, wrong keys and canonicalization/format ambiguity while distinguishing signatures from confidentiality and from certificate authority.
- **SEC5-O9:** Trace a standard key agreement or KEM-based establishment scheme through peer identities, trusted public keys, shared-secret derivation and authenticated versus unauthenticated modes; identify active-interception/unknown-key-share risks and the limited guarantees of a successful shared-secret computation.
- **SEC5-O10:** Analyze protocol framing, domain separation, version and algorithm negotiation, transcript binding, authenticated context, replay/order rules, downgrade resistance and error behavior using specified message/state semantics and independent negative cases.
- **SEC5-O11:** Establish a defensible cryptographic key lifecycle and algorithm policy covering generation, storage access, purpose separation, key identifiers, rotation, revocation/compromise response, recoverability, deprecation and credible post-quantum migration constraints without mistaking a key-ID change for re-encryption.
- **SEC5-O12:** Build, reproduce and defend a small locally tested cryptographic component and associated trust/protocol argument with independently derived expected values, honest library/platform limitations, actionable defect remediation and transfer to a previously unseen bounded variant.

## Modules

### Module 1 — Security Claims, Adversaries and Cryptographic Randomness

#### Outcomes

- SEC5-O1
- SEC5-O2
- SEC5-O5

#### Lessons

1. **Which property must cryptography establish?** — Compare a private record, signed update, login credential, tamper-evident message and two-party exchange. For each, name exactly who must verify confidentiality, authenticity or integrity, whether freshness matters, and which trust or authorization problem cryptography does not solve. Disprove the claim that encrypting a message proves who sent it.
2. **Threat models and boundaries of a proof** — Identify attacker visibility, control over messages, access to keys, ability to replay/drop traffic and the assumptions under which a primitive's guarantee is stated. Distinguish a formal property for a primitive, a vetted implementation's claim, a tested use case and untested deployment behavior. Draw a precise boundary around claims about availability, endpoint compromise and authorized use.
3. **Random bytes, secrets and predictable values** — Compare a CSPRNG-backed symmetric key or token with a timestamp, PID, ordinary pseudorandom simulation and an exposed fixed seed. Use a supported OS-backed generator with requested lengths; explain why counting unique samples is not an entropy audit or proof that an RNG cannot fail.
4. **Unpredictable keys versus unique nonces** — Explain which values must remain secret or unpredictable and which must be unique per key, accounting for algorithm-specific constraints. Trace the danger of copying a deterministic seed into deployment, confusing salts with nonces, or creating two writers that reuse one counter space. Plan observations that test a system's state logic without purporting to prove global randomness quality.

*Optional formative feedback:* Given five candidate designs, reject a proposal using `random.random` for encryption keys and explain why a deterministic published test vector remains valid in a test suite.

### Module 2 — Authenticated Encryption and Nonce State

#### Outcomes

- SEC5-O2
- SEC5-O3
- SEC5-O4
- SEC5-O10

#### Lessons

1. **Why encryption alone is not enough** — Compare confidentiality-only encryption, encrypt-then-authenticate and standard authenticated encryption with associated data. Trace plaintext, key, nonce, AAD, ciphertext and tag through a published AEAD interface; identify which bytes are protected but not encrypted. Distinguish an AEAD algorithm's guarantee from endpoint identity or replay protection.
2. **Real AEAD library behavior** — Use a maintained AES-GCM or ChaCha20-Poly1305 high-level API for a synthetic record with an independently specified byte encoding. Verify correct decryption, empty and boundary records, invalid key/nonce sizes and selected known-answer vectors or an independent compatible implementation where available. State exact algorithm/key/message limits.
3. **Context binding and invalid ciphertext** — Bind a record's purpose, version, record identifier and relevant ownership context through correctly encoded AAD. Challenge the tag, ciphertext, AAD, key, length and algorithm identifier in negative cases. Assert that no plaintext is accepted or released before authentication succeeds, and distinguish an authentication error from a parse or unsupported-version error without leaking secrets.
4. **Nonce uniqueness, restart and multi-writer hazards** — Model random-nonce collision probability versus managed counter/sequence allocation for a named AEAD. Show why uniqueness is per *key*, why resets/restarts or simultaneous writers can make naive counters unsafe, and how a local single-writer durable sequence, separate subkeys or properly bounded random-nonce policy changes the risk. Evaluate supplied nonce-reuse cases analytically rather than demanding unsafe payloads.
5. **Replay, duplication and usage ceilings** — Inspect an authenticated record replayed with identical nonce and tag: authentication can succeed even when the application must reject a duplicate. Specify a recipient-side sequence/record-ID policy, relevant state persistence and mode-specific per-key invocation/size bounds. Test an out-of-order/duplicate record and a counter-exhaustion or failed-state update through a controlled fixture.

*Optional investigation:* Predict decryption and application acceptance separately for a tampered tag, changed AAD, a valid replay and a clean record under a new key ID.

### Module 3 — Hashes, MACs, Password Verification and Derived Keys

#### Outcomes

- SEC5-O5
- SEC5-O6
- SEC5-O7

#### Lessons

1. **Unkeyed hashes versus message authentication** — Distinguish collision/second-preimage considerations, checksum uses and HMAC verification with secret key possession. Construct and inspect a local signed-looking message whose unkeyed digest can be recomputed by an attacker, then repair the authenticator using a supported HMAC API and independent correct/incorrect-key tests. Use a library comparison suited to secret-derived authenticators; do not claim a timing guarantee from a single benchmark.
2. **Password verifiers need a different cost model** — Explain how a human-chosen password differs in entropy from a generated symmetric key and why fast hash, HMAC-only and HKDF-only storage are unsuitable. Use a salted password verifier with free Argon2id or scrypt/PBKDF2 support justified for the actual environment. Test correct/wrong password, independent salts, stored parameter metadata and invalid record handling without recording the synthetic password in report artifacts.
3. **Work-factor calibration and denial limits** — Measure a small, documented local cost configuration and compare its memory/latency constraints, particularly on lower-resource devices. Distinguish offline guessing economics from online rate controls and credential compromise. Choose a recorded parameter policy and a safe upper bound preventing attacker-controlled cost fields from exhausting the training process.
4. **Extract-and-expand with key-purpose isolation** — Inspect HKDF's input key material, salt, extract, expand and `info` context. Derive distinct output keys for encryption and authentication or two named record purposes from a true shared secret; test that domains differ and that repeating inputs yields the same result. State why changing `info` cannot manufacture entropy or safely stretch a human password without a password KDF.

*Optional feedback:* Classify six supplied values as password salt, AEAD nonce, KDF salt, KDF context, key ID and authentication tag and identify which must be unique, secret, verifiable or domain-separated.

### Module 4 — Public-Key Identity and Authenticated Key Establishment

#### Outcomes

- SEC5-O1
- SEC5-O7
- SEC5-O8
- SEC5-O9

#### Lessons

1. **Public-key identity and trust bootstrap** — Trace who owns a key pair, how a public key is bound to a claimed signer or peer, and what changes when a trusted key is substituted. Distinguish a raw fingerprint/pinned key, an application-owned trust registry and a certificate chain; a successful signature check authenticates a key, not an unspecified person.
2. **Signing exact bytes rather than mutable meaning** — Use a reviewed signature API such as Ed25519 on a clearly encoded synthetic message. Verify legitimate and tampered payloads, wrong public keys, mismatched key purpose and altered representation. Explain why an unambiguous protocol message format or canonical representation matters, and why a signature neither encrypts data nor proves that an authorized signer made a sound decision.
3. **Key agreement and KEM roles** — Analyze a standard Diffie–Hellman/ECDH or key-encapsulation example using real documented public/private key roles and shared-secret derivation. Distinguish exchanging public values from proving peer identity. Identify contributory key agreement versus KEM encapsulation/decapsulation and compare successful matching secrets with a possible active substitution.
4. **Authorship, peer authentication and transcripts** — Contrast an unauthenticated exchange, an exchange with authenticated public keys and a protocol binding identities and the negotiated transcript into derived traffic keys. Investigate an active-interception or unknown-key-share hypothesis using explicitly specified message traces, without implementing a new handshake or conducting attacks against real peers.
5. **Standard secure composition as a reference** — Inspect the intended roles of KEM, KDF, AEAD and optional sender authentication in RFC 9180 HPKE and the authenticated transcript/key schedule of TLS 1.3. Identify what base HPKE does **not** authenticate about the sender and why merely wrapping data in encryption is not equivalent to TLS. Use supplied trace and protocol documentation; an entire HPKE or TLS implementation is not required.

*Optional formative feedback:* Given two valid signatures with one substituted untrusted public key, determine which cryptographic checks passed and why the expected sender-identity claim still fails.

### Module 5 — Protocol Composition and Failure-Path Security

#### Outcomes

- SEC5-O1
- SEC5-O3
- SEC5-O4
- SEC5-O8
- SEC5-O9
- SEC5-O10

#### Lessons

1. **Message framing and unambiguous fields** — Define a bounded, versioned local record envelope containing algorithm/key-ID and a length-delimited header, nonce, ciphertext and tag as appropriate. Explain why concatenation without encoding can alias two different field tuples; parse and reject unsupported or truncated data *before* invoking cryptography while preserving an independent error policy.
2. **Domain/context binding and key separation** — Connect protocol purpose, role, message type, version and relevant record ID to AAD, signed input or KDF `info` as justified by the chosen scheme. Identify an authenticated but incorrectly interpreted record when binding is missing, including cross-purpose or cross-tenant confusion. Test the wrong-domain rejection using actual component behavior or a fully specified counterexample.
3. **Replay, ordering and state transitions** — Specify whether the protected record is a static file, a sequence of updates or a network message. Identify which replay/order semantics the application truly needs; a valid AEAD tag or signature does not reject replay by itself. Evaluate duplicate, missing, out-of-order and stale-key cases against a documented monotonic or unique-ID policy and clean state.
4. **Negotiation, downgrade and algorithm confusion** — Examine a transcript where the parties offer several versions or algorithms and a mediator can alter negotiation. Explain how a standard protocol authenticates negotiated choices, while an unprotected fallback or attacker-selected algorithm identifier can defeat the design. Require explicit allowed suites, rejected unknown identifiers and no silent downgrade; do not construct a new public transport protocol.
5. **Failure atomicity, error surfaces and side channels** — Trace parse, authentication, key lookup, file write and acknowledgment stages of a local component. Show that malformed/unverified data is not returned as plaintext, that failed writes do not mark a record accepted and that errors do not disclose keys or unsafe internal state. Discuss constant-time comparisons and potential timing leakage with honest library guarantees; no noisy microbenchmark is presented as proof of side-channel resistance.

*Optional investigation:* Evaluate two plausible but subtly different record decoders: one authenticates version and recipient context, the other trusts an unauthenticated header. Predict a counterexample and the smallest sufficient fix.

### Module 6 — Key Lifecycle, Cryptographic Agility and Independent Review

#### Outcomes

- SEC5-O1
- SEC5-O2
- SEC5-O4
- SEC5-O7
- SEC5-O10
- SEC5-O11
- SEC5-O12

#### Lessons

1. **Key lifecycle and compromise response** — Model creation, allowed purpose, identifiers, authorization, storage boundaries, rotation, retirement, recovery, revocation and incident handling for a local record key. Explain where process memory/copies and backups undermine a simplistic secure-deletion claim, and distinguish preventing new encryption under a key from decrypting old retained records.
2. **Key IDs, nonces and safe rotation** — Add an explicit key ID and permitted-suite policy to a versioned local envelope. Test successful decrypt of authorized earlier records after changing the active encryption key, failed unknown/retired-key uses, wrong-purpose key reuse and nonce counters/registries across restart. State which old keys remain accessible and when actual re-encryption is needed; changing only an ID is not rotation.
3. **Password, derived and asymmetric key inventories** — Produce a proportionate table of who generates/holds each secret, where it may be used, how access is restricted and what compromise reveals. Distinguish a password verifier, a symmetric data key, a derived purpose subkey, a signing private key and a trust anchor. Recommend a genuine key-storage service for production when applicable without requiring one in the free local assessment.
4. **Post-quantum exposure and algorithm inventory** — Apply NIST FIPS 203/204/205 and **final NIST IR 8547 (October 2026)** to a supplied realistic inventory of classical ECDH/KEM and signature use, key lifetimes, long-lived ciphertext and remote dependencies. Distinguish ML-KEM key encapsulation from ML-DSA/SLH-DSA signatures; prioritize based on data lifetime and ecosystem readiness, and recognize hybrid migration, compatibility and downgrade risks without requiring an unapproved PQ library or custom PQ implementation.
5. **Unseen cryptographic defect and individual defense** — Investigate a bounded variant such as reset nonce state, missing AAD context, swapped trusted signing key, broken rotation, untrusted suite selection or wrong key-purpose assignment. Before inspecting results, predict which guarantees fail and which still hold; propose a minimal reviewable fix, test positive/negative/invalid/failure behavior, defend the key/trust decision and retract any security claim unsupported by evidence.

*Optional formative feedback:* Review a synthetic cryptography migration plan that promises all historical ciphertexts are safe after changing a key ID and deploying one post-quantum signature library.

## Completion requirements

**Four required summative evaluations** collectively establish all SEC5 outcomes; they may share one versioned synthetic record-protection component and its test fixtures. No lesson-level check, optional reading or formative activity is an additional completion condition. Every evaluation must identify the exact algorithm and library version actually used, security property and threat assumptions, independent expected results, observed or explicitly modeled outcomes, reviewer decision and material untested behavior. A collection of green unit tests or a claimed "industry-standard" algorithm is not sufficient without a defended context and negative evidence.

- **SEC5-AS1** — Authenticated Record Protection and Nonce/Replay Contract
  - **Outcomes:** SEC5-O1, SEC5-O2, SEC5-O3, SEC5-O4, SEC5-O10, SEC5-O12.
  - **Work:** Implement a small **local, non-networked** authenticated record encoder/decoder using an established vetted AEAD API and synthetic data. Publish permitted plaintext sizes, authenticated context fields, chosen key/nonce scheme, record format and precise acceptance/rejection criteria. Use OS-backed randomness for test keys, a documented nonce policy for a declared single-writer or correctly coordinated environment, and an explicit recipient-side duplicate/replay rule where the fictional workflow requires freshness. Establish expectations before execution, then verify normal, empty/boundary, wrong-key, altered AAD, modified tag/ciphertext, truncation, repeated-record and nonce-exhaustion/failed-state cases using valid fixtures; do not deliberately execute an unsafe same-key repeated-nonce encryption outside supplied analytical vectors.
  - **Criteria:** The selected AEAD API is actually authenticated and supports the stated lengths and usage bounds. No unauthenticated plaintext escapes or is persisted when verification fails. AAD binds the declared version/purpose/record identity, with appropriately unambiguous encoding. Per-key nonce uniqueness is justified under actual writer and restart assumptions rather than a uniqueness assertion based only on a handful of samples. Replays are accepted or rejected according to the *explicit* application policy, not assumed automatically solved by AEAD. Legitimate operations continue to work, expected outputs precede observations, and a safely weakened guard or controlled invalid-case fixture makes the regression suite fail.
  - **Evidence:** Source and pinned library/tool versions; local fixture and permission/synthetic-key plan; cryptographic record/nonce/AAD specification; independent expected accept/reject table; clean encrypt/decrypt reproduction and failure tests; patched code/diff if starting from a defective fixture; declared collision, concurrency, restart and coverage limitations without raw private keys.

- **SEC5-AS2** — Message Authentication, Password and KDF Boundary Verification
  - **Outcomes:** SEC5-O1, SEC5-O5, SEC5-O6, SEC5-O7, SEC5-O12.
  - **Work:** For three **different** fictional security needs—authenticate a message, store a user-selected password verifier, and derive separate purpose keys from a suitably strong shared secret—choose and exercise a maintained library API for HMAC or equivalent keyed authentication, a supported salted adaptive password hash, and HKDF or a vetted extract-and-expand API. Establish independently expected valid/invalid-message and password results, key-purpose separation and bounded verifier cost. Demonstrate why replacing any of the three with a fast unkeyed hash or treating a password as high-entropy key material fails the declared goal. Record actual local password-hash runtime/memory settings and a defensible limit on attacker-controlled parameters.
  - **Criteria:** The message authenticator rejects modifications and wrong keys without relying on an unkeyed digest. Correct and incorrect test passwords are evaluated with distinct salted verifiers and an explicit work-factor policy; password values are not disclosed in assessment artifacts. HKDF derivations have purpose-separated context and do not purport to amplify weak password entropy. The explanation accurately separates salt, nonce, `info`, key ID and tag, and distinguishes what the selected library verifies from timing/side-channel properties it does not prove. Positive, invalid, wrong-purpose and failure cases are independently reviewable.
  - **Evidence:** Scoped synthetic use cases, vetted API declarations, confidential-local test fixtures, public expected outcome matrix, safe code/test results, password-hash parameter/latency rationale, separated derived-key comparisons using redacted representations, and a brief mistake/remediation and residual-risk analysis.

- **SEC5-AS3** — Signer Identity and Key-Establishment Protocol Review
  - **Outcomes:** SEC5-O1, SEC5-O7, SEC5-O8, SEC5-O9, SEC5-O10.
  - **Work:** Use a reviewed asymmetric signature API on an explicitly encoded synthetic message with a declared trusted public key and actor policy; verify original, tampered, substituted-key and ambiguous-format cases. Independently review supplied accurate key-agreement/KEM and authenticated-transcript traces, identifying sender/recipient/peer roles, shared-secret derivation, identity-binding and an active-interception or unknown-key-share precondition. Examine a documented HPKE or TLS 1.3 transcript example to distinguish base encryption, authenticated modes, signature identity, transcript protection and downgrade failure semantics. An entire handshake, TLS stack, custom crypto primitive or live public PKI is not required.
  - **Criteria:** Successful signature verification is correctly tied to **the specified trusted key and exact bytes**, not automatically to an arbitrary user, authority or confidentiality claim. Wrong keys and altered or ambiguously represented signed content are rejected or explicitly detected by the declared trust/format policy. The protocol analysis separates unauthenticated shared-secret computation from authenticated peer identity and analyzes at least one realistic message substitution/downgrade counterexample. The learner selects meaningful transcript/KDF/AAD bindings and acknowledges which supplied observations do not establish production transport security. Independent expected cases and justified residual gaps appear in the evidence.
  - **Evidence:** Public synthetic keys and test messages only, signed-message format, trust/identity policy, signature test outcomes, supplied protocol transcript with source/provenance, labeled peer/key schedule and authenticity reasoning, and a reviewer-checkable accepted/denied/conditional-case analysis.

- **SEC5-AS4** — Key Lifecycle, Post-Quantum Transition and Unfamiliar Defense
  - **Outcomes:** SEC5-O1, SEC5-O2, SEC5-O3, SEC5-O4, SEC5-O7, SEC5-O10, SEC5-O11, SEC5-O12.
  - **Work:** Extend the AS1 local record-protection fixture with an allowed-suite and key-ID policy, at least one test rotation event, safe decrypt rules for retained authorized records and a documented revocation/compromise decision. Test current, retained, unknown, wrong-purpose and retired-key use, a restart/duplicate condition and a safe failure/rollback scenario. For a supplied organization inventory, apply final NIST IR 8547 and FIPS 203/204/205 to distinguish classical key establishment, post-quantum KEMs and signatures and justify a prioritized migration/crypto-agility plan; do **not** implement PQ primitives. Diagnose an unseen changed security assumption, predict an allowed and forbidden result before checking it, repair or reject the design, and defend the outcome independently.
  - **Criteria:** Version/algorithm identifiers are bound to authenticated context or governed by explicit reject-before-accept rules with no silent insecure fallback. New encryption uses the correct active key and justified nonce policy; authorized old data remain decryptable only while a permitted retained key exists, and a key-ID switch is not misrepresented as re-encryption or key erasure. Unknown, revoked and wrong-purpose keys are rejected as specified, while legitimate use still works. The post-quantum plan distinguishes ML-KEM from ML-DSA/SLH-DSA and identifies data-lifetime risks, transition dependencies, hybrid/negotiation limitations and unverified deployment assumptions without claiming quantum safety from an unsupported local library. The unseen variant elicits a genuine independently reasoned correction, precise risk communication and evidence-limited defense.
  - **Evidence:** Declared local key inventory and recorded active/retained/revoked states, versioned synthetic envelope and policy, independent before/after and negative tests, rotation/restart/failure/rollback evidence, risk-prioritized cryptographic transition decision tied to named standards, and written/recorded/live defense with corrected hypothesis and unresolved limitations.

### Evaluation and readiness

Record the source revision and exact `SEC5-AS#` and `SEC5-O#` identifiers for each required decision. Executable work must reproduce from a clean installation using documented open-source dependencies and synthetic fixtures. Use public standard vectors where available and independently derived expected accept/reject behavior; never claim that decrypting data you just encrypted is independent interoperability proof. Where supplied transcript analysis replaces unavailable live key-exchange infrastructure, identify it as *analysis* rather than an executed cryptographic handshake. Key material generated for testing can be disposed of locally; do not collect real passwords, production secrets or unrecoverable private keys as assessment evidence.

The course remains `draft` pending the relevant [course readiness criteria](../../spec/status-labels.md). Its completion does not certify a production cryptosystem, guarantee side-channel resistance, grant formal cryptographic accreditation or establish compliance with a regulation.

### Optional disciplinary references

- [RFC 5116](https://www.rfc-editor.org/rfc/rfc5116.html) and [RFC 9771](https://www.rfc-editor.org/rfc/rfc9771.html) — AEAD interface, nonce obligations, associated data and security-property distinctions.
- [NIST SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final) — currently final GCM guidance. A 2026 pre-draft revision must not be treated as final.
- [RFC 8439](https://www.rfc-editor.org/rfc/rfc8439.html) — ChaCha20-Poly1305 construction and interoperability reference, not an invitation to reimplement it.
- [RFC 5869](https://www.rfc-editor.org/rfc/rfc5869.html) and [RFC 9106](https://www.rfc-editor.org/rfc/rfc9106.html) — standard HKDF roles and Argon2 password-hashing parameters.
- [RFC 9180](https://www.rfc-editor.org/rfc/rfc9180.html) and [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446.html) — standard KEM/KDF/AEAD composition and TLS 1.3 authenticated key schedule/transcripts.
- [NIST SP 800-57 Part 1 Rev. 5](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final) — currently final key management guidance; newer draft material does not replace it.
- [NIST FIPS 203](https://csrc.nist.gov/pubs/fips/203/final), [FIPS 204](https://csrc.nist.gov/pubs/fips/204/final), [FIPS 205](https://csrc.nist.gov/pubs/fips/205/final) and [NIST IR 8547, final October 2026](https://csrc.nist.gov/pubs/ir/8547/final) — established post-quantum algorithms and transition requirements.
- [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html), [Key Management](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) and [Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) — applied key, nonce, storage and password-security practice.

These public sources are aids for verification and deeper study, not paid prerequisites or substitute evaluations.
