# Resources

A deliberately small external library. Each course has **one primary spine**; everything else is reference or practice. Do not collect ten courses for the same topic. Record the exact edition, URL, and date in `notes/<track>/<course>/resources.md`.

**Access key:** 🌐 free/legal online · 🛒 purchase or library · 🔐 account or hardware required · ⚠️ verify current edition before use.

## Foundations

| Course | Primary spine | Practice / reference | Access |
| --- | --- | --- | --- |
| [F0](foundations/F0-setup-tools-and-study-system.md) | [The Missing Semester](https://missing.csail.mit.edu/) | Git book, shellcheck, `man` pages | 🌐 |
| [F1](foundations/F1-programming-i-python.md) | [Python Tutorial](https://docs.python.org/3/tutorial/) | [CS50P](https://cs50.harvard.edu/python/) or [CS50x](https://cs50.harvard.edu/x/); pytest, Ruff, mypy docs | 🌐 |
| [F2](foundations/F2-data-structures-and-algorithms.md) | [MIT 6.006](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) **or** *Algorithms* (Sedgewick & Wayne, 4th ed.) | CLRS 4th ed. for proofs; [VisuAlgo](https://visualgo.net/); [NeetCode](https://neetcode.io/) | 🌐 / 🛒 |
| [F3](foundations/F3-engineering-practice.md) | [Pro Git](https://git-scm.com/book/en/v2) + B2 + [Learn C the Hard Way](https://learncodethehardway.org/c/) (selected) | `gdb`, ASan/UBSan, `valgrind`, `make`, pytest docs | 🌐 / 🛒 |
| [F4](foundations/F4-mathematics-i.md) | [Mathematics for Machine Learning](https://mml-book.github.io/) (MML) | [MIT 6.042](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/); [3Blue1Brown](https://www.3blue1brown.com/topics/linear-algebra) | 🌐 |
| [F5](foundations/F5-rust-foundations.md) | [The Rust Programming Language](https://doc.rust-lang.org/book/) | [Rustlings](https://github.com/rust-lang/rustlings); [Rust by Example](https://doc.rust-lang.org/rust-by-example/); `clippy` docs | 🌐 |
| [F6](foundations/F6-data-sql-and-web-foundations.md) | [PostgreSQL Tutorial](https://www.postgresql.org/docs/current/tutorial.html) or [SQLite docs](https://www.sqlite.org/docs.html) | [Use The Index, Luke](https://use-the-index-luke.com/); [MDN HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP); DDIA Ch. 1–2 | 🌐 / 🛒 |

## Systems

| Course | Primary spine | Practice / reference | Access |
| --- | --- | --- | --- |
| [S1](systems/S1-computer-systems-foundations.md) | B2 + B4 + B5 (see course) | CS:APP Ch. 1–3, 7, 9; `man 2`; ELF/`strace` docs | 🛒 / 🌐 |
| [S2](systems/S2-machine-code-cpu-and-architecture.md) | B3 Ch. 1, 5–7 + B1 | CS:APP Ch. 3; [Compiler Explorer](https://godbolt.org/); MIPS/ARM docs | 🛒 / 🌐 |
| [S3](systems/S3-memory-hierarchy-and-locality.md) | B6 Ch. 2, 3.1–3.5 + B3 §5.5, 8.1–8.3 | CS:APP Ch. 6; `perf` docs; cachegrind | 🛒 / 🌐 |
| [S4](systems/S4-cpu-caches.md) | B6 §3.2–3.5 + B3 §8.2–8.3 | CS:APP Ch. 6; [cachegrind](https://valgrind.org/docs/manual/cg-manual.html); `perf c2c` | 🛒 / 🌐 |
| [S5](systems/S5-virtual-memory.md) | B4 Ch. 12–24 + B5 §6.3–6.4, Ch. 49–50 | CS:APP Ch. 9; B3 §8.4; kernel `Documentation/mm` | 🛒 / 🌐 |
| [S6](systems/S6-concurrency-atomics-and-memory-models.md) | B5 Ch. 29–33, 53 + B4 Ch. 25–34 | [Rust Atomics and Locks](https://marabos.nl/atomics/) (free); [C++ memory model](https://en.cppreference.com/w/cpp/atomic/memory_order) | 🛒 / 🌐 |
| [S7](systems/S7-cache-coherence-and-false-sharing.md) | B6 §6.4 + B3 §7.8.8 | [A Primer on Memory Consistency and Cache Coherence](https://link.springer.com/book/10.1007/978-3-031-01764-3); `perf c2c` | 🛒 / 🌐 |
| [S8](systems/S8-numa-and-memory-topology.md) | B6 Ch. 5 + Linux NUMA docs | `numactl`, `numastat`, `lstopo`, `hwloc` docs | 🌐 |
| [S9](systems/S9-performance-engineering-and-observability.md) | *Systems Performance* (Gregg, 2nd ed.) | `perf`, `bpftrace`, FlameGraphs, Prometheus/OpenTelemetry docs | 🛒 / 🌐 |
| [S10](systems/S10-linux-systems-programming-and-networking.md) | B5 + [Beej's Guide](https://beej.us/guide/bgnet/) | CS:APP Ch. 10–11; `epoll(7)`; `io_uring` docs | 🛒 / 🌐 |
| [S11](systems/S11-distributed-systems.md) | *Designing Data-Intensive Applications* 2nd ed. + [MIT 6.5840](https://pdos.csail.mit.edu/6.824/) | [Raft paper](https://raft.github.io/raft.pdf); [Jepsen consistency models](https://jepsen.io/consistency) | 🛒 / 🌐 |
| [S12](systems/S12-data-systems-and-storage-engines.md) | *Database Internals* (Petrov) + B4 Ch. 36–45 | DDIA Ch. 3–4; SQLite WAL docs; RocksDB design docs | 🛒 / 🌐 |
| [S13](systems/S13-ai-infrastructure-systems-lens.md) | [CUDA C Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/) + [vLLM docs](https://docs.vllm.ai/) | [FlashAttention](https://arxiv.org/abs/2205.14135); Nsight Compute docs; B6 | 🌐 / 🔐 |
| [S14](systems/S14-containers-virtualization-and-cloud-operations.md) | [Kubernetes docs](https://kubernetes.io/docs/concepts/) + [OCI specs](https://github.com/opencontainers) | Linux namespaces/cgroups docs; Docker/Podman docs; cloud provider docs | 🌐 / 🔐 |
| [S15](systems/S15-reliability-incident-response-and-sre.md) | [Google SRE Book](https://sre.google/sre-book/table-of-contents/) + [Workbook](https://sre.google/workbook/table-of-contents/) | Prometheus/OpenTelemetry docs; public postmortems | 🌐 |
| [S16](systems/S16-networking-and-protocols-deep-dive.md) | *Computer Networking: A Top-Down Approach* (Kurose & Ross) | [Beej](https://beej.us/guide/bgnet/); TCP/IP Illustrated; RFC 9293/9110/9000; Wireshark | 🛒 / 🌐 |
| [S17](systems/S17-compilers-and-language-runtimes.md) | [Crafting Interpreters](https://craftinginterpreters.com/) + *Engineering a Compiler* | [LLVM Kaleidoscope](https://llvm.org/docs/tutorial/); B2 Ch. 5, 7–8; B3 Ch. 6–7 | 🌐 / 🛒 |

## AI & Machine Learning

| Course | Primary spine | Practice / reference | Access |
| --- | --- | --- | --- |
| [AI1](ai/AI1-python-for-data-and-ai.md) | [Python for Data Analysis](https://wesmckinney.com/book/) 3rd ed. | NumPy/pandas/matplotlib docs; Datasheets for Datasets | 🌐 |
| [AI2](ai/AI2-optimization-and-probabilistic-ml.md) | MML Ch. 5–7 | *Deep Learning* Ch. 4–5, 7; scipy.stats | 🌐 |
| [AI3](ai/AI3-classical-machine-learning.md) | [ISL](https://www.statlearning.com/) 2nd ed. | scikit-learn user guide; Model Cards; Fairness and ML | 🌐 |
| [AI4](ai/AI4-deep-learning-foundations.md) | [Dive into Deep Learning](https://d2l.ai/) Ch. 1–5, 11 | PyTorch tutorials; CS231n notes; *Deep Learning* Ch. 6–8 | 🌐 |
| [AI5](ai/AI5-vision-and-sequence-architectures.md) | D2L Ch. 6–10 | CS231n; *Deep Learning* Ch. 9–10; Illustrated Transformer | 🌐 |
| [AI6](ai/AI6-transformers-nlp-and-llms.md) | [Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/) + [nanoGPT](https://github.com/karpathy/nanoGPT) | Transformer/GPT-2 papers; HF LLM course; D2L Ch. 10–11, 14–15 | 🌐 |
| [AI7](ai/AI7-training-fine-tuning-and-alignment.md) | [HF LLM Course](https://huggingface.co/learn/llm-course) + PEFT/TRL docs | LoRA, QLoRA, InstructGPT, DPO papers; HELM | 🌐 / 🔐 |
| [AI8](ai/AI8-distributed-and-large-scale-training.md) | [PyTorch FSDP](https://pytorch.org/docs/stable/fsdp.html) + [DeepSpeed](https://www.deepspeed.ai/) docs | ZeRO, Megatron-LM, GPipe, Efficient Large-Scale Training | 🌐 / 🔐 |
| [AI9](ai/AI9-inference-serving-and-optimization.md) | [vLLM docs](https://docs.vllm.ai/) | PagedAttention, FlashAttention, Triton Inference Server; S13 | 🌐 / 🔐 |
| [AI10](ai/AI10-retrieval-agents-and-applied-genai.md) | [Hugging Face Agents Course](https://huggingface.co/learn/agents-course) | RAG, ReAct, OWASP GenAI, NIST AI RMF; one pinned framework | 🌐 |
| [AI11](ai/AI11-mlops-and-production-deployment.md) | *Designing Machine Learning Systems* (Huyen) Ch. 7–10 | Google ML Test Score; Kubernetes/OpenTelemetry docs; S15 | 🛒 / 🌐 |
| [AI12](ai/AI12-responsible-ai-safety-and-governance.md) | [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) + GenAI Profile | OWASP LLM Top 10; Model Cards; EU AI Act overview; Fairness and ML | 🌐 |
| [AI13](ai/AI13-data-engineering-for-ml.md) | *Fundamentals of Data Engineering* (Reis & Housley) | DDIA Ch. 3–4, 10–11; dbt/Airflow/Dagster docs; Great Expectations | 🛒 / 🌐 |
| [AI14](ai/AI14-generative-and-multimodal-models.md) | DDPM + Latent Diffusion + CLIP papers | *Generative Deep Learning* (Foster); D2L generative chapters; FID paper | 🌐 / 🛒 |
| [AI15](ai/AI15-reinforcement-learning-and-rlhf.md) | [Sutton & Barto](http://incompleteideas.net/book/the-book.html) + [Spinning Up](https://spinningup.openai.com/) | PPO, InstructGPT, DPO; TRL docs | 🌐 |
| [AI16](ai/AI16-gpu-programming-and-kernels.md) | [CUDA C Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/) + [Triton tutorials](https://triton-lang.org/main/getting-started/tutorials/) | PMPP 4th ed.; Nsight Compute; Roofline paper | 🌐 / 🛒 / 🔐 |
| [AI17](ai/AI17-causal-inference-and-experimentation.md) | [Causal Inference: What If](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/) | Trustworthy Online Controlled Experiments; DoWhy docs | 🌐 / 🛒 |
| [AI18](ai/AI18-recommender-systems-and-ranking.md) | *Recommender Systems: The Textbook* (Aggarwal) | BPR paper; Microsoft Recommenders; nDCG paper | 🛒 / 🌐 |
| [AI19](ai/AI19-time-series-and-forecasting.md) | [Forecasting: Principles and Practice](https://otexts.com/fpp3/) 3rd ed. | statsmodels/Prophet docs; M5 competition; N-BEATS/TFT | 🌐 |

## Security

| Course | Primary spine | Practice / reference | Access |
| --- | --- | --- | --- |
| [D1](security/D1-security-foundations-and-threat-modeling.md) | *Threat Modeling: Designing for Security* (Shostack) Ch. 1–11 | OWASP Threat Modeling; OWASP Top 10; NIST SP 800-30; ATT&CK | 🛒 / 🌐 |
| [D2](security/D2-memory-corruption-and-binary-exploitation.md) | *Practical Binary Analysis* (Andriesse) + [pwn.college](https://pwn.college/) | B2 Ch. 5, 8; B4 Ch. 13–24; ASan docs; Rustonomicon | 🌐 / 🛒 / 🔐 |
| [D3](security/D3-network-and-web-application-security.md) | [PortSwigger Web Security Academy](https://portswigger.net/web-security) | OWASP Top 10/ASVS/WSTG; *Web Application Hacker's Handbook*; MDN | 🌐 / 🛒 |
| [D4](security/D4-systems-and-infrastructure-penetration-testing.md) | [PTES](http://www.pentest-standard.org/) + [NIST SP 800-115](https://csrc.nist.gov/pubs/sp/800/115/final) | *Penetration Testing* (Weidman); ATT&CK; CIS Benchmarks | 🌐 / 🛒 / 🔐 |
| [D5](security/D5-applied-cryptography-and-secure-systems-design.md) | *Serious Cryptography* (Aumasson) 2nd ed. | *Cryptography Engineering*; libsodium docs; RFC 8446; Wycheproof | 🛒 / 🌐 |
| [D6](security/D6-ai-security-and-red-teaming.md) | [OWASP GenAI](https://genai.owasp.org/) + [MITRE ATLAS](https://atlas.mitre.org/) | NIST AI 100-2; AI RMF GenAI Profile; indirect prompt injection paper | 🌐 |
| [D7](security/D7-detection-incident-response-and-forensics.md) | [NIST SP 800-61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) + [SigmaHQ](https://github.com/SigmaHQ/sigma) | Zeek/Suricata docs; *Art of Memory Forensics*; ATT&CK; DFIR Report | 🌐 / 🛒 |
| [D8](security/D8-cloud-container-and-kubernetes-security.md) | [NSA/CISA Kubernetes Hardening Guide](https://www.cisa.gov/resources-tools/resources/kubernetes-hardening-guidance) + K8s security docs | OWASP Kubernetes Top 10; NIST SP 800-190; CIS benchmark; *Container Security* | 🌐 / 🛒 |
| [D9](security/D9-secure-sdlc-appsec-and-supply-chain.md) | [NIST SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) + [OWASP SAMM](https://owaspsamm.org/) | SLSA, Sigstore, CycloneDX/SPDX, ASVS; *Secure by Design* | 🌐 / 🛒 |
| [D10](security/D10-privacy-compliance-and-governance.md) | [NIST Privacy Framework](https://www.nist.gov/privacy-framework) + GDPR text | LINDDUN; ISO 27701 overview; ICO guidance; CCPA/CPRA | 🌐 / 🛒 |
| [D11](security/D11-reverse-engineering-and-malware-analysis.md) | *Practical Malware Analysis* (Sikorski & Honig) | Ghidra, x64dbg, REMnux, FLARE VM, ATT&CK | 🛒 / 🌐 / 🔐 |
| [D12](security/D12-hardware-embedded-and-iot-security.md) | *Practical IoT Hacking* (Chantzis et al.) | *Hardware Hacking Handbook*; OWASP IoT Top 10; FSTM | 🛒 / 🌐 / 🔐 |
| [D13](security/D13-mobile-application-security.md) | [OWASP MASTG](https://mas.owasp.org/MASTG/) + [MASVS](https://mas.owasp.org/MASVS/) | Android/iOS security docs; Frida; MobSF | 🌐 / 🔐 |
| [D14](security/D14-red-team-operations-and-adversary-emulation.md) | *Red Team Development and Operations* (Vest & Tubberville) | ATT&CK; TIBER-EU; CISA red-team reports; Atomic Red Team | 🛒 / 🌐 / 🔐 |

## Cross-cutting references

| Need | Use |
| --- | --- |
| Linux man pages | <https://man7.org/linux/man-pages/> |
| Performance | *Systems Performance* (Gregg); `perf`; `bpftrace` |
| Distributed systems | DDIA; MIT 6.5840; Jepsen; Raft paper |
| Security standards | OWASP ASVS/Top 10/WSTG; NIST 800-series; CIS Benchmarks |
| AI governance | NIST AI RMF; OWASP GenAI; EU AI Act overview |
| Research papers | [arXiv](https://arxiv.org/), [Papers with Code](https://paperswithcode.com/), [Semantic Scholar](https://www.semanticscholar.org/) |
| Legal/regulatory | Official government/regulator text; qualified counsel |

## How to acquire resources legally

- Use the official free edition (B4, B6, MML, ISL, D2L, FPP3, Crafting Interpreters, Rust Book, SRE books).
- Buy or borrow paid books (B2, B3, B5, DDIA, Database Internals, security texts).
- Use a library or institutional access where available.
- Do not commit PDFs, course videos, paywalled chapters, datasets with restrictive licenses, or model weights.
- If a resource is unavailable, write the blocker in the course `resources.md` and choose a documented alternative. Do not silently substitute a TikTok summary for a textbook.

## Resource budget

A realistic budget for the first year:

- one paid systems book at a time (B2, B3 or B5);
- one paid ML/security book per specialization;
- free official docs for tools;
- a small cloud/lab budget for S14/AI9 (or use local alternatives);
- no expensive bootcamp is required.

If a course requires a paid book you cannot obtain, use the alternative named in the course file and record the gap. The exit check, labs, and evidence matter more than owning every book.
