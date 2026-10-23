# Coverage Map

This page answers three questions:

1. **Where is topic X taught?**
2. **What is the complete course catalogue and its time cost?**
3. **What is deliberately not covered, and how would I go deeper?**

It is a map, not a substitute for the course files. A course code tells you where to start; the course file contains the exact readings, labs, and exit check.

## 1. Professional knowledge map

| Knowledge area | What you must be able to do | Primary courses | Evidence |
| --- | --- | --- | --- |
| Programming and software construction | Write tested, readable programs; use Git, debugging, packaging, and code review | F1, F3, F5, S10, S17 | P1, P2, P4 |
| Algorithms and complexity | Choose and implement data structures; analyse time/space; recognize trade-offs | F2 | F2 implementations, P1 query/index work |
| Mathematics | Discrete math, linear algebra, calculus, probability; read an ML derivation | F4, AI2 | F4 notebook, P7 math checks |
| Digital logic and computer architecture | Explain gates to ISA to pipeline; read assembly; reason about caches and memory | S2, S3, S4, S7, S8 | P2 disassembly, P3 simulator |
| Operating systems and Linux | Explain processes, virtual memory, files, signals, syscalls, scheduling, I/O | S1, S5, S6, S10, S14 | P2, P4, S5 labs |
| Concurrency and memory models | Write correct concurrent code; diagnose races, deadlocks, and false sharing | S6, S7, S8, S10, S17 | P4 bounded queue/service, P3 false sharing |
| Performance engineering | Form a hypothesis, measure, profile, explain variance, and state limits | S3–S9, S13 | P3 report, S9 investigations |
| Networking | Explain TCP/IP, sockets, HTTP, TLS, DNS, congestion, and failure modes | S10, S16, D3 | P4, S16 labs, P10 |
| Storage and databases | Model data, write correct SQL, explain indexes, WAL, isolation, and LSM/B-tree trade-offs | F6, S12, AI13 | P1, P5 |
| Distributed systems | Reason about replication, consensus, partitions, retries, and client guarantees | S11, S12, S14, S15 | P6, C1/C2 |
| Cloud, containers, and operations | Package, deploy, observe, secure, and roll back a service | S14, S15, D8 | P4 deployment, SLO/incident drill |
| Software engineering practice | Turn ambiguity into requirements, design, tests, docs, and an operable change | F3, appendices, projects | Every project readme/design/evaluation |
| AI/ML foundations | Build honest baselines; evaluate; diagnose leakage, overfitting, and drift | AI1–AI6, AI13 | P7, P8 |
| Training, fine-tuning, and serving | Train/fine-tune a small model; serve it; measure quality, latency, and cost | AI7–AI9, AI16 | P8, P9 |
| Applied generative AI | Build bounded RAG/agent systems with citations, evals, and safety controls | AI10–AI12 | P9, C3 |
| AI depth electives | Generative/multimodal, RL/RLHF, kernels, causality, ranking, forecasting | AI14–AI19 | elective labs |
| Security foundations | Threat-model, reason about trust boundaries, and turn threats into tests | D1, D5 | P10, P11 |
| Memory safety and exploitation | Explain memory corruption and mitigations; build a safe vulnerable/fixed pair | D2, S2, S5 | P10 |
| Web and network security | Find, explain, fix, and retest common web and protocol weaknesses | D3, D9 | P10 |
| Systems and infrastructure assessment | Scope and conduct a non-destructive authorized assessment | D4, D5 | P11 |
| Detection, response, and forensics | Build detections, triage an incident, preserve evidence, and write a timeline | D7 | P11 detection/IR drill |
| Cloud and Kubernetes security | Threat-model and harden containers, clusters, identity, and supply chain | D8, D9 | P11 cloud assessment |
| AI security | Test models and LLM applications against misuse and prompt injection | D6 (elective), AI12 | P11 AI red-team |
| Privacy and governance | Map data flows, minimize data, assess privacy risk, and state residual risk | D10 | P11 risk register |
| Reverse engineering, hardware, mobile, red team | Go deeper into specialist offensive/defensive domains | D11–D14 (electives) | elective labs |
| Professional behavior | Communicate, review, operate, disclose, and keep learning | F0, F3, appendices | retrospectives, reports, reviews |

## 2. Complete course catalogue

### Foundations — 720 hours

| Code | Course | Hours | Type |
| --- | --- | ---: | --- |
| [F0](../foundations/F0-setup-tools-and-study-system.md) | Setup, Tools & Study System | 15 | Core |
| [F1](../foundations/F1-programming-i-python.md) | Programming I: Python | 120 | Core |
| [F2](../foundations/F2-data-structures-and-algorithms.md) | Data Structures & Algorithms | 150 | Core |
| [F3](../foundations/F3-engineering-practice.md) | Engineering Practice: Git, Testing, Debugging, C & Linux | 120 | Core |
| [F4](../foundations/F4-mathematics-i.md) | Mathematics I | 150 | Core |
| [F5](../foundations/F5-rust-foundations.md) | Rust Foundations | 90 | Core for Systems/Security |
| [F6](../foundations/F6-data-sql-and-web-foundations.md) | Data, SQL & Web Foundations | 75 | Core |

### Systems Engineering — 1,110 core hours, 150 elective hours

| Code | Course | Hours | Type |
| --- | --- | ---: | --- |
| [S1](../systems/S1-computer-systems-foundations.md) | Computer Systems Foundations | 90 | Core |
| [S2](../systems/S2-machine-code-cpu-and-architecture.md) | Machine Code, CPU & Architecture | 90 | Core |
| [S3](../systems/S3-memory-hierarchy-and-locality.md) | Memory Hierarchy & Locality | 60 | Core |
| [S4](../systems/S4-cpu-caches.md) | CPU Caches | 60 | Core |
| [S5](../systems/S5-virtual-memory.md) | Virtual Memory | 75 | Core |
| [S6](../systems/S6-concurrency-atomics-and-memory-models.md) | Concurrency, Atomics & Memory Models | 90 | Core |
| [S7](../systems/S7-cache-coherence-and-false-sharing.md) | Cache Coherence & False Sharing | 30 | Core |
| [S8](../systems/S8-numa-and-memory-topology.md) | NUMA & Memory Topology | 30 | Core |
| [S9](../systems/S9-performance-engineering-and-observability.md) | Performance Engineering & Observability | 75 | Core |
| [S10](../systems/S10-linux-systems-programming-and-networking.md) | Linux Systems Programming & Networking | 105 | Core |
| [S11](../systems/S11-distributed-systems.md) | Distributed Systems | 105 | Core |
| [S12](../systems/S12-data-systems-and-storage-engines.md) | Data Systems & Storage Engines | 90 | Core |
| [S13](../systems/S13-ai-infrastructure-systems-lens.md) | AI Infrastructure (Systems Lens) | 75 | Core |
| [S14](../systems/S14-containers-virtualization-and-cloud-operations.md) | Containers, Virtualization & Cloud Operations | 75 | Core |
| [S15](../systems/S15-reliability-incident-response-and-sre.md) | Reliability, Incident Response & SRE | 60 | Core |
| [S16](../systems/S16-networking-and-protocols-deep-dive.md) | Networking & Protocols Deep Dive | 60 | Elective |
| [S17](../systems/S17-compilers-and-language-runtimes.md) | Compilers & Language Runtimes | 90 | Elective |

### AI & Machine Learning — 990 core hours, 420 elective hours

| Code | Course | Hours | Type |
| --- | --- | ---: | --- |
| [AI1](../ai/AI1-python-for-data-and-ai.md) | Python for Data & AI | 60 | Core |
| [AI2](../ai/AI2-optimization-and-probabilistic-ml.md) | Optimization & Probabilistic ML | 60 | Core |
| [AI3](../ai/AI3-classical-machine-learning.md) | Classical Machine Learning | 90 | Core |
| [AI4](../ai/AI4-deep-learning-foundations.md) | Deep Learning Foundations | 90 | Core |
| [AI5](../ai/AI5-vision-and-sequence-architectures.md) | Vision & Sequence Architectures | 75 | Core |
| [AI6](../ai/AI6-transformers-nlp-and-llms.md) | Transformers, NLP & LLMs | 105 | Core |
| [AI7](../ai/AI7-training-fine-tuning-and-alignment.md) | Training, Fine-Tuning & Alignment | 75 | Core |
| [AI8](../ai/AI8-distributed-and-large-scale-training.md) | Distributed & Large-Scale Training | 75 | Core |
| [AI9](../ai/AI9-inference-serving-and-optimization.md) | Inference, Serving & Optimization | 75 | Core |
| [AI10](../ai/AI10-retrieval-agents-and-applied-genai.md) | Retrieval, Agents & Applied GenAI | 75 | Core |
| [AI11](../ai/AI11-mlops-and-production-deployment.md) | MLOps & Production Deployment | 75 | Core |
| [AI12](../ai/AI12-responsible-ai-safety-and-governance.md) | Responsible AI, Safety & Governance | 60 | Core |
| [AI13](../ai/AI13-data-engineering-for-ml.md) | Data Engineering for ML | 75 | Core |
| [AI14](../ai/AI14-generative-and-multimodal-models.md) | Generative & Multimodal Models | 75 | Elective |
| [AI15](../ai/AI15-reinforcement-learning-and-rlhf.md) | Reinforcement Learning & RLHF | 90 | Elective |
| [AI16](../ai/AI16-gpu-programming-and-kernels.md) | GPU Programming & Kernels | 75 | Elective |
| [AI17](../ai/AI17-causal-inference-and-experimentation.md) | Causal Inference & Experimentation | 60 | Elective |
| [AI18](../ai/AI18-recommender-systems-and-ranking.md) | Recommender Systems & Ranking | 60 | Elective |
| [AI19](../ai/AI19-time-series-and-forecasting.md) | Time Series & Forecasting | 60 | Elective |

### Security Engineering — 675 core hours, 345 elective hours

| Code | Course | Hours | Type |
| --- | --- | ---: | --- |
| [D1](../security/D1-security-foundations-and-threat-modeling.md) | Security Foundations & Threat Modeling | 60 | Core |
| [D2](../security/D2-memory-corruption-and-binary-exploitation.md) | Memory Corruption & Binary Exploitation | 90 | Core |
| [D3](../security/D3-network-and-web-application-security.md) | Network & Web Application Security | 90 | Core |
| [D4](../security/D4-systems-and-infrastructure-penetration-testing.md) | Systems & Infrastructure Penetration Testing | 90 | Core |
| [D5](../security/D5-applied-cryptography-and-secure-systems-design.md) | Applied Cryptography & Secure Systems Design | 75 | Core |
| [D6](../security/D6-ai-security-and-red-teaming.md) | AI Security & Red Teaming | 60 | Elective (AI security) |
| [D7](../security/D7-detection-incident-response-and-forensics.md) | Detection, Incident Response & Forensics | 75 | Core |
| [D8](../security/D8-cloud-container-and-kubernetes-security.md) | Cloud, Container & Kubernetes Security | 75 | Core |
| [D9](../security/D9-secure-sdlc-appsec-and-supply-chain.md) | Secure SDLC, AppSec & Supply Chain | 60 | Core |
| [D10](../security/D10-privacy-compliance-and-governance.md) | Privacy, Compliance & Governance | 60 | Core |
| [D11](../security/D11-reverse-engineering-and-malware-analysis.md) | Reverse Engineering & Malware Analysis | 75 | Elective |
| [D12](../security/D12-hardware-embedded-and-iot-security.md) | Hardware, Embedded & IoT Security | 75 | Elective |
| [D13](../security/D13-mobile-application-security.md) | Mobile Application Security | 60 | Elective |
| [D14](../security/D14-red-team-operations-and-adversary-emulation.md) | Red Team Operations & Adversary Emulation | 75 | Elective |

### Totals

| Measure | Hours |
| --- | ---: |
| Foundations | 720 |
| Systems core | 1,110 |
| AI core | 990 |
| Security core | 675 |
| All electives | 915 |
| One capstone | 180 |

The Security path adds the required systems prerequisites (630 hours). With Foundations and one capstone, its total is 2,205 hours. D6 is an AI-security elective requiring AI1–AI6 and AI12, so it is not included in the core path. See [roadmap.md](../roadmap.md) for calendar assumptions.

## 3. Where each local book is used

| Book | Strongest coverage | Limits |
| --- | --- | --- |
| [B1](../books/B1-but-how-do-it-know.md) — *But How Do It Know?* | Gates, memory, CPU, a toy computer, OS intuition | No modern architecture, pipelining, or quantitative performance |
| [B2](../books/B2-the-c-programming-language.md) — *The C Programming Language* | C syntax, pointers, arrays, structs, UNIX I/O | Dated C style; no modern tooling, sanitizers, or concurrency |
| [B3](../books/B3-digital-design-and-computer-architecture.md) — *Digital Design and Computer Architecture* | Logic, MIPS, pipelining, caches, virtual memory | MIPS-centric; no out-of-order, multicore coherence depth, or GPU |
| [B4](../books/B4-operating-systems-three-easy-pieces.md) — *Operating Systems: Three Easy Pieces* | Processes, scheduling, virtual memory, concurrency, persistence | Conceptual; Linux-specific APIs come from B5 and S10 |
| [B5](../books/B5-the-linux-programming-interface.md) — *The Linux Programming Interface* | Linux syscalls, processes, signals, threads, sockets, IPC | Large reference; not a project guide and not a performance text |
| [B6](../books/B6-what-every-programmer-should-know-about-memory.md) — *What Every Programmer Should Know About Memory* | Caches, coherence, NUMA, memory performance | 2007 hardware examples; verify current topology and counters |

The local library is deliberately narrow. Modern distributed systems, ML, web security, cloud-native security, and AI safety come from [resources.md](../resources.md) and the individual course files.

## 4. Topic-to-course quick index

Use this when a term appears in a project and you need the teaching sequence.

| Topic | Start here | Then |
| --- | --- | --- |
| Python, packaging, tests | F1 | F3, F6 |
| C, pointers, memory, debugging | F3 | S1, B2, B5 |
| Rust ownership and traits | F5 | S6, P2 |
| Data structures and complexity | F2 | S12, AI3 |
| Discrete math and proofs | F4 | S11, D5 |
| Linear algebra, calculus, probability | F4 | AI2 |
| Digital logic and ISA | S2 | B1, B3 |
| Processes, scheduling, syscalls | S1 | S10 |
| Virtual memory and page faults | S5 | S12, D2 |
| Caches and locality | S3, S4 | B6, S7, P3 |
| Coherence, false sharing, NUMA | S7, S8 | S9, S13 |
| Threads, atomics, memory ordering | S6 | S10, S17 |
| Profiling, tracing, observability | S9 | S13, S15 |
| Sockets and network programming | S10 | S16, P4 |
| TCP/IP, HTTP, TLS, DNS | S10 | S16, D3 |
| SQL, indexes, transactions | F6 | S12 |
| Storage engines, WAL, LSM/B-tree | S12 | P5, P6 |
| Replication, consensus, partitions | S11 | P6, C2 |
| Containers, Kubernetes, cloud | S14 | S15, D8 |
| SLOs, incidents, postmortems | S15 | P4, C1 |
| Data pipelines and warehouses | AI13 | AI11 |
| Classical ML and evaluation | AI3 | AI17, AI18, AI19 |
| Deep learning | AI4 | AI5, AI6 |
| Transformers and LLMs | AI6 | AI7–AI10 |
| Fine-tuning and alignment | AI7 | AI15 |
| Distributed training | AI8 | S11, S13 |
| Inference and serving | AI9 | S13, AI16 |
| RAG, agents, tool use | AI10 | AI12, D6, P9 |
| MLOps and production ML | AI11 | S14, S15 |
| AI safety and governance | AI12 | D6, D10 |
| Threat modeling | D1 | D5, D9 |
| Memory corruption and mitigations | D2 | S2, S5 |
| Web vulnerabilities | D3 | D9, P10 |
| Cryptography and protocol design | D5 | D9, P11 |
| Detection and incident response | D7 | D10, D14 |
| Cloud/Kubernetes security | D8 | S14, D9 |
| Supply chain and secure SDLC | D9 | D3, P10 |
| Privacy and data governance | D10 | D7, D8 |
| Reverse engineering and malware | D11 | D2, S2 |
| Hardware and IoT | D12 | D2, S5 |
| Mobile security | D13 | D3 |
| Red team operations | D14 | D4, D7 |

## 5. Deliberate boundaries

No curriculum can cover every specialization. This one aims at a **broad professional core plus selected depth**, not a research degree or a complete trade school. The following areas are out of scope or only introduced:

- analog electronics, RF, PCB design, and advanced digital verification (SystemVerilog/UVM, timing closure);
- operating-system kernel and driver development, real-time systems, and hypervisor implementation;
- formal methods, model checking, proof assistants, and program verification at scale;
- advanced compiler optimization, LLVM backend development, and JIT/GC implementation depth (S17 is an introduction);
- database query-optimizer implementation and storage hardware/device firmware;
- planet-scale distributed systems, multi-region consensus, and Byzantine fault tolerance;
- HPC cluster operations, interconnect fabrics, and custom accelerator hardware;
- frontend/mobile product engineering, graphics, game engines, and robotics;
- advanced data visualization, product analytics, and experimentation platform operations;
- legal compliance certification, audit attestation, and jurisdiction-specific legal advice;
- offensive exploit development, malware authoring, and weaponized payloads;
- security program management, budgeting, and executive governance beyond the D10 introduction.

### How to go deeper

1. **Choose one specialty** after the core and one capstone.
2. **Read primary sources:** specifications, papers, maintainer design docs, and postmortems.
3. **Reproduce a result** from the field, then extend it in one direction.
4. **Find a practitioner** and ask for a design review or a code review.
5. **Contribute to an open-source project** in that specialty; review is the fastest feedback loop.
6. **Write a public case study** with enough detail for someone else to reproduce it.
7. **Take a specialist course** only when you can state the gap it fills.

## 6. Coverage audit

At the end of Foundations and each specialization, answer these without notes:

- [ ] Can I trace one user request from input to syscall, storage, and output?
- [ ] Can I explain one performance result with a model, a measurement, and a limitation?
- [ ] Can I build a small service that handles partial I/O, overload, and shutdown?
- [ ] Can I state the consistency and durability guarantee of a storage system I built?
- [ ] Can I build a baseline, evaluate it honestly, and name what the metric misses?
- [ ] Can I explain how a transformer computes an output and where the memory goes?
- [ ] Can I threat-model a service and turn the top threat into a test?
- [ ] Can I verify a fix and write a regression test?
- [ ] Can I operate what I built, detect a failure, and roll back?
- [ ] Can another engineer reproduce my evidence from a clean checkout?

Any "no" is a concrete next course or project, not a reason to start a new curriculum.
