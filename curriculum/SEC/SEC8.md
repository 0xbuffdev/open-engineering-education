## SEC8 — AI Security & Authorized Red Teaming

**Duration:** 4 weeks
**Expected workload:** 10–15 focused hours/week
**Prerequisite:** SEC1, SEC2, SEC7, and AI5

**Recommended:** AI4, or equivalent knowledge.

### Overview

Apply security engineering to retrieval systems, tool-using agents, and model-powered applications. Learners examine permissions, prompt injection, data isolation, dangerous outputs, rate limits, escalation, and layered defenses within explicitly authorized environments.

### Prerequisites

**SEC1 — Security Foundations & Threat Modeling**
**SEC2 — Web & Application Security**
**SEC7 — Detection, Incident Response & Threat Hunting**
**AI5 — Retrieval, Agents & Applied Generative AI**
**Recommended:** AI4, or equivalent knowledge.

**Kind:** `course`

### Learning outcomes

By the end of the course, you will be able to:

- Identify AI-specific attack surfaces involving retrieval, tools, permissions, and generated outputs.
- Conduct bounded and authorized security tests against a controlled AI system.
- Evaluate isolation, rate limiting, dangerous-action controls, logging, and escalation paths.
- Translate findings into layered mitigations and regression tests.
- Produce a clear AI security assessment and demonstrate the retest results.


### Resource map

**Required**

- **R60** LLM01, LLM02 and LLM05–LLM08, LLM10 — carried from ZtP D6 (record the edition/date at study time) · **R61** OWASP Top 10 for Agentic Applications.
- **R62** NIST AI 100-2 E2025 · **R63** MITRE ATLAS · **R59** Greshake et al. · **B38** Ch. 5 and 10 · **R75** NIST SP 800-115.

### Modules

#### Module 1 — AI Attack Surfaces

**Reading:** **R60** LLM01 (Prompt Injection), LLM02 (Sensitive Information Disclosure), LLM07 (System Prompt Leakage), LLM08 (Vector and Embedding Weaknesses). **R59** indirect prompt injection. **B38** Ch. 5 (defensive prompt engineering), Ch. 6 §6.1 (RAG).


### Module outcomes

By the end of this module, the learner can:

- Explain **Prompt injection and instruction boundaries** in the context of the course.
- Apply **Retrieval isolation and data access** in a problem, implementation, experiment, or design decision.

1. **Prompt injection and instruction boundaries**
   - kind: `lesson`
2. **Retrieval isolation and data access**
   - kind: `lesson`
3. **Checkpoint: AI attack surfaces**
   - kind: `test`

4. **Micro-lab: Create a benign retrieval-isolation test and observe the boundary.**
   - kind: `lab`
#### Module 2 — Tool & Agent Controls

**Reading:** **R60** LLM05 (Improper Output Handling), LLM06 (Excessive Agency). **R61** agentic-application risks. **B38** Ch. 6 (agents: tools; failure modes).


### Module outcomes

By the end of this module, the learner can:

- Explain **Tool permissions and agent boundaries** in the context of the course.
- Apply **Dangerous tool execution and output handling** in a problem, implementation, experiment, or design decision.

1. **Tool permissions and agent boundaries**
   - kind: `lesson`
2. **Dangerous tool execution and output handling**
   - kind: `lesson`
3. **Checkpoint: tool security**
   - kind: `test`

4. **Micro-lab: Attempt an unauthorized tool path and verify the permission control blocks it.**
   - kind: `lab`
#### Module 3 — Abuse Cases & Defensive Controls

**Reading:** **R60** LLM03 (Supply Chain), LLM04 (Data and Model Poisoning), LLM10 (Unbounded Consumption). **R62** NIST AI 100-2 E2025 (attacks and mitigations). **B38** Ch. 10 (guardrails; monitoring).


### Module outcomes

By the end of this module, the learner can:

- Explain **AI-specific abuse cases and rate limits** in the context of the course.
- Apply **Layered controls and logging** in a problem, implementation, experiment, or design decision.

1. **AI-specific abuse cases and rate limits**
   - kind: `lesson`
2. **Layered controls and logging**
   - kind: `lesson`
3. **Checkpoint: layered defense**
   - kind: `test`

4. **Micro-lab: Turn an abuse case into prevention, detection, and recovery controls.**
   - kind: `lab`
#### Module 4 — Authorized Red Teaming & Retest

**Reading:** **R63** MITRE ATLAS (tactics, techniques, case studies). **R62** NIST AI 100-2 E2025. **R75** NIST SP 800-115 for assessment methodology and reporting. **B38** Ch. 4 (regression evaluation).


### Module outcomes

By the end of this module, the learner can:

- Explain **Red-team methodology and evidence** in the context of the course.
- Apply **Remediation and regression testing** in a problem, implementation, experiment, or design decision.

1. **Red-team methodology and evidence**
   - kind: `lesson`
2. **Remediation and regression testing**
   - kind: `lesson`
3. **Checkpoint: assessment reasoning**
   - kind: `test`

4. **Micro-lab: Retest a repaired control using the same bounded attack case.**
   - kind: `lab`
#### Module 5 — AI Security Assessment

**Reading:** Apply Modules 1–4. **R60** as the findings checklist; **R75** for scope and reporting.


1. **Assess only a controlled AI system or local training application; produce findings, remediation, and retest evidence**
   - kind: `lab`

### Topics

- prompt injection
- retrieval isolation
- tool permissions
- model output risks
- agent boundaries
- dangerous tool execution
- rate limiting
- AI-specific abuse cases
- red-team methodology
- remediation

### Substantial course lab

**AI Security Assessment**

Assess a controlled AI system or local training application, produce findings, implement defenses, and retest.

---

