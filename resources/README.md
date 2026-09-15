# Resource Acquisition Checklist

`books/` is enough to begin Foundations and much of Systems. Obtain the following before the relevant course. Prefer the official source, keep the edition/date you used in that course's `resources.md`, and do not place copies here.

| Course(s) | Resource | Access/action |
| --- | --- | --- |
| F1 | [Python Tutorial](https://docs.python.org/3/tutorial/) and [CS50x](https://cs50.harvard.edu/x/) | 🌐 Free online. CS50x is suitable for learners with no prior CS experience. |
| F2 | One DS&A curriculum and practice source | 🌐 Select one structured source; record it in the course note rather than mixing several curricula. |
| F4, AI2 | [Mathematics for Machine Learning](https://mml-book.github.io/) | 🌐 Free legal online/PDF text. Required chapters are specified in `curriculum.md`. |
| S6 | [Rust Atomics and Locks](https://marabos.nl/atomics/) | 🌐 Free online. Read the chapter selection in `curriculum.md`. |
| S8 | [Linux NUMA memory policy docs](https://docs.kernel.org/admin-guide/mm/numa_memory_policy.html) | 🌐 Free online; multi-node hardware is optional but valuable. |
| S9 | `man perf`, Linux tracing documentation, and optionally *Systems Performance* | 🌐/🛒 Use a Linux host for the labs. |
| S11 | *Designing Data-Intensive Applications*, 2nd ed., and [MIT 6.5840](https://pdos.csail.mit.edu/6.824/) | 🛒/🌐 DDIA requires a legal copy; MIT course materials are online. See `curriculum.md` for the required chapters. |
| S12 | *Database Internals* | 🛒 Obtain a legal copy; its required chapters are in `curriculum.md`. |
| S13, AI9 | [vLLM documentation](https://docs.vllm.ai/) plus your GPU vendor's official docs | 🌐; 🔐 GPU is preferred, but a simulator may be used. |
| AI1 | [NumPy docs](https://numpy.org/doc/stable/) and [pandas docs](https://pandas.pydata.org/docs/) or *Python for Data Analysis* | 🌐/🛒 |
| AI3 | [scikit-learn user guide](https://scikit-learn.org/stable/user_guide.html) and introductory ML text/course | 🌐/🛒 |
| AI4–AI8 | [PyTorch tutorials](https://pytorch.org/tutorials/), [Hugging Face course](https://huggingface.co/learn), PEFT/FSDP/DeepSpeed docs | 🌐; 🔐 GPU increasingly useful from AI4 and ideal for AI8. |
| AI10 | Agent/retrieval framework documentation | 🌐 Select one framework, pin its version, and record it. |
| AI11 | *Designing Machine Learning Systems* (2022) or equivalent production-ML course | 🛒/🌐 The required chapter selection is in `curriculum.md`. |
| AI12, D6 | [OWASP GenAI Security Project](https://genai.owasp.org/) and current agentic-risk guidance | 🌐 Check the release date when you start; taxonomy changes rapidly. |
| D1 | *Threat Modeling: Designing for Security*, 1st ed. (2014), and [OWASP Top 10](https://owasp.org/projects/top-ten) | 🛒/🌐 Obtain a legal copy of the first edition; the 2nd edition is announced for February 2027 and is not required yet. Use the latest released OWASP edition, currently 2025. Required chapters are in `curriculum.md`. |
| D2 | [pwn.college](https://pwn.college/) | 🌐/🔐 Use only its sandbox or your own intentionally vulnerable environment. |
| D3 | [PortSwigger Web Security Academy](https://portswigger.net/web-security) | 🌐/🔐 Use Academy labs or applications you control. |
| D4 | TryHackMe or Hack The Box Academy | 🌐/🔐 Account and isolated authorized target required. |
| D5 | *Serious Cryptography*, 2nd ed. (2024), and vetted-library documentation | 🛒/🌐 Use established implementations; do not create new primitives. Required chapters are in `curriculum.md`. |

## Environment checkpoints

- **Before S1:** Linux shell, C compiler, Rust stable toolchain, Git, debugger, and a way to run tests.
- **Before S8/S9:** a Linux host that allows access to topology and performance tools; record unavailable counters rather than fabricating results.
- **Before AI4:** Python virtual environment and a reproducible dependency file. GPU is optional for small work.
- **Before AI8/AI9/S13:** budget for compute or choose the explicitly permitted simulator path.
- **Before D2–D6:** isolated, authorized targets only; written scope and rollback/snapshot plan. Never use course techniques against third-party systems.
