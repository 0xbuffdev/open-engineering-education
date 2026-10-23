# Glossary

A working vocabulary for the curriculum. Definitions are deliberately short: enough to use the term correctly in a design review, not a replacement for the course. The **See** column names the course where the term is developed. Use the [coverage map](coverage-map.md) or the track indexes to open that course.

## Study and engineering practice

| Term | Working definition | See |
| --- | --- | --- |
| Prerequisite | The evidence you need before a course will make sense. | F0 |
| Core | The minimum defensible material for a track; not optional. | F0 |
| Elective | Depth for a role or interest, taken after the core or when a job requires it. | F0 |
| Exit check | A closed-book demonstration that you can use the course's ideas, not just recognize them. | F0 |
| Evidence | A reproducible artifact: test, benchmark, trace, report, threat model, or commit. | F0 |
| Baseline | The simplest credible reference result that a new approach must beat. | AI3, P7 |
| Benchmark | A controlled measurement of performance against a stated workload and environment. | S9 |
| Reproducibility | The ability to obtain the same result from a clean checkout with recorded inputs and versions. | F0, S9 |
| Design doc | A short document covering requirements, architecture, interfaces, state, failure handling, and trade-offs. | F3 |
| ADR | Architecture decision record: the context, decision, alternatives, and consequences of one choice. | F3 |
| Runbook | Step-by-step operational instructions for deploy, rollback, restore, and alert response. | S15 |
| Postmortem | A blame-free timeline and causal analysis of an incident, with owned follow-up actions. | S15 |
| Retrospective | A personal or team review of what was believed, what the evidence changed, and what to do next. | F0 |
| SLI | Service level indicator: the measured quantity, such as successful-request ratio or p99 latency. | S15 |
| SLO | Service level objective: the target range for an SLI over a window. | S15 |
| SLA | Service level agreement: a contractual commitment, usually with consequences. | S15 |
| Error budget | The allowed amount of unreliability implied by an SLO; it funds change and experimentation. | S15 |
| Threat model | A structured description of assets, trust boundaries, adversaries, abuse cases, controls, and residual risk. | D1 |
| Authorization | Explicit permission to test a named system within a scope and time window. | D1 |
| Least privilege | Granting only the access needed for a task, for only as long as needed. | D1, D8 |
| Responsible disclosure | Reporting a vulnerability privately, allowing a fix window, and avoiding publication of weaponized detail. | D1 |

## Computer systems

| Term | Working definition | See |
| --- | --- | --- |
| ISA | Instruction set architecture: the programmer-visible instructions, registers, and memory model of a processor. | S2 |
| Microarchitecture | The implementation of an ISA: pipelines, caches, execution units, and scheduling. | S2 |
| Register | A small, fast storage location inside a CPU. | S2 |
| ABI | Application binary interface: calling convention, data layout, and binary interface between compiled components. | S1, S2 |
| Calling convention | The rules for passing arguments, returning values, and preserving registers across a function call. | S2 |
| Stack frame | The per-call region holding return address, saved registers, arguments, and local variables. | S2 |
| Heap | Dynamically allocated memory whose lifetime is managed by the program or runtime. | S1 |
| Pointer | A value holding the address of another object. | F3 |
| Undefined behavior | A C/C++ program state for which the language standard imposes no requirements; the optimizer may assume it never occurs. | F3 |
| Memory safety | The property that a program cannot access memory outside the intended object or after its lifetime. | F5, D2 |
| Process | An isolated execution context with its own virtual address space and resources. | S1 |
| Thread | A schedulable execution stream sharing an address space with other threads in a process. | S6 |
| Context switch | Saving one execution context and restoring another so the CPU can run something else. | S1 |
| System call | The controlled entry from user space into the kernel to request a service. | S1, S10 |
| Signal | An asynchronous notification to a process, such as `SIGTERM` or `SIGSEGV`. | S10 |
| File descriptor | A small integer naming an open file, socket, pipe, or other kernel object. | S10 |
| Inode | A filesystem metadata object describing a file's type, permissions, size, and data blocks. | S10 |
| Virtual address | An address in a process's private address space, translated by the MMU. | S5 |
| Page | A fixed-size unit of virtual memory and physical memory management, commonly 4 KiB. | S5 |
| Page table | The per-process structure mapping virtual pages to physical frames and permissions. | S5 |
| TLB | Translation lookaside buffer: a cache of recent virtual-to-physical translations. | S5 |
| Page fault | A trap caused by a virtual page that is not present or not permitted; the kernel resolves it or terminates the process. | S5 |
| `mmap` | A system call that maps a file or anonymous memory into a process's address space. | S5 |
| Copy-on-write | Sharing pages until one writer needs a private copy, used by `fork` and some filesystems. | S5 |
| Demand paging | Loading pages only when they are first accessed. | S5 |
| Thrashing | Excessive paging that leaves little time for useful work. | S5 |
| Cache line | The fixed-size block (commonly 64 bytes) transferred between cache levels and memory. | S3 |
| Cache hit / miss | A hit finds the requested block in a cache level; a miss must fetch it from a lower level. | S3 |
| Associativity | The number of locations in a cache set where a given block may be placed. | S4 |
| Locality | The tendency of programs to reuse recent data (temporal) or nearby data (spatial). | S3 |
| Write-back / write-through | A cache writes on eviction (write-back) or writes through to the next level immediately (write-through). | S4 |
| Cache coherence | The protocol that keeps per-core cached copies of a location consistent. | S7 |
| False sharing | Performance loss when independent variables share a cache line and cores contend on it. | S7 |
| NUMA | Non-uniform memory access: memory latency and bandwidth depend on which node owns the memory. | S8 |
| DMA | Direct memory access: a device transfers data to or from memory without the CPU copying each word. | S1 |
| Interrupt | A hardware or software event that transfers control to a handler. | S1 |
| Race condition | A correctness bug whose result depends on the timing or interleaving of operations. | S6 |
| Data race | Two threads access the same memory location concurrently, at least one writes, and there is no synchronization. | S6 |
| Atomic operation | An operation that appears indivisible to other threads. | S6 |
| Memory ordering | The rules governing when one thread's memory operations become visible to another. | S6 |
| Mutex | Mutual exclusion lock protecting a critical section. | S6 |
| Semaphore | A counter plus wait/signal operations used to limit concurrency or signal events. | S6 |
| Condition variable | A wait/notify primitive used with a mutex to wait for a predicate. | S6 |
| Deadlock | A cycle of threads each waiting for a resource held by another. | S6 |
| Livelock | Threads continue executing but make no progress because they keep reacting to each other. | S6 |
| Starvation | A thread is perpetually denied the resource it needs. | S6 |
| Lock-free | At least one thread makes progress without blocking on a lock, though individual threads may starve. | S6 |
| Wait-free | Every thread completes its operation in a bounded number of steps. | S6 |
| Backpressure | A mechanism that slows producers when consumers cannot keep up, instead of buffering without bound. | S10 |
| Latency | Time from a request or event to its result. | S9 |
| Throughput | Work completed per unit time. | S9 |
| Bandwidth | Data transferred per unit time; often the upper bound on throughput. | S3 |
| p50 / p95 / p99 | Percentiles of a latency distribution; p99 is the value below which 99% of requests fall. | S9 |
| Tail latency | The slowest requests in a distribution, often caused by queueing, GC, or interference. | S9 |
| Profiling | Sampling or instrumenting a running program to attribute time or resources to code. | S9 |
| Tracing | Recording timed events across components to reconstruct a request's path. | S9 |
| Observability | The ability to infer internal state from logs, metrics, traces, and events. | S9, S15 |
| Roofline | A model relating achievable performance to memory bandwidth and compute peak. | S9, AI16 |
| IPC | Instructions per cycle, a basic measure of CPU throughput. | S2 |
| Write amplification | Bytes written to storage per logical byte written by the application. | S12 |
| Socket | An endpoint for network communication identified by address and port. | S10 |
| TCP | A reliable, ordered, connection-oriented byte stream with flow and congestion control. | S10 |
| UDP | A connectionless datagram protocol with no delivery or ordering guarantee. | S10 |
| Three-way handshake | TCP connection setup exchanging SYN, SYN-ACK, and ACK. | S10 |
| Congestion control | Adapting send rate to network capacity and loss/delay signals. | S10, S16 |
| DNS | The distributed naming system that resolves names to addresses and other records. | S10 |
| TLS | Transport Layer Security: authenticated, encrypted transport over a byte stream. | D5, S16 |
| HTTP | The request/response application protocol of the web. | F6 |
| RPC | Remote procedure call: invoking a function-like interface across a process or network boundary. | S11 |
| Idempotency | The property that repeating an operation has the same effect as performing it once. | S10, S11 |
| Timeout | A bound on how long a caller waits before treating an operation as failed. | S10 |
| Retry storm | A failure mode where many clients retry at once and amplify overload. | S15 |
| Load balancer | A component that distributes requests across backends and removes unhealthy ones. | S14 |
| Reverse proxy | A server that forwards client requests to backends, often terminating TLS and enforcing policy. | S10 |
| NAT | Network address translation, rewriting addresses/ports between network domains. | S16 |
| Durability | The guarantee that acknowledged data survives the stated failure model. | S12 |
| WAL | Write-ahead log: append a record and flush it before applying the change, so recovery can replay or undo. | S12 |
| `fsync` | A system call requesting that data and metadata be flushed to durable storage. | S12 |
| B-tree | A balanced, page-oriented search tree used by many databases and filesystems. | S12 |
| LSM tree | Log-structured merge tree: buffer writes, flush sorted runs, and compact them in the background. | S12 |
| SSTable | Sorted string table: an immutable, sorted on-disk file with an index and often a bloom filter. | S12 |
| Memtable | An in-memory sorted write buffer in an LSM engine. | S12 |
| Compaction | Merging on-disk runs to remove obsolete versions and bound read amplification. | S12 |
| Tombstone | A deletion marker that must survive until older versions are compacted away. | S12 |
| Bloom filter | A probabilistic set membership structure with no false negatives and tunable false positives. | S12 |
| ACID | Atomicity, consistency, isolation, durability: a set of transaction guarantees, not a single property. | S12 |
| Isolation level | The allowed visibility of concurrent transactions, such as read committed or serializable. | S12 |
| MVCC | Multi-version concurrency control: readers see a consistent snapshot while writers create new versions. | S12 |
| Index | A data structure that speeds access at the cost of storage and write maintenance. | F6 |
| Query plan | The execution strategy chosen by a database for a query. | F6, S12 |
| Replication | Maintaining copies of data on multiple nodes for availability, durability, or read scale. | S11 |
| Partition | A network failure that splits nodes into groups that cannot communicate. | S11 |
| Quorum | The minimum set of replicas whose agreement is required for an operation. | S11 |
| Consensus | Agreement among replicas on a sequence of values despite failures. | S11 |
| Raft | A consensus protocol with leader election, log replication, and committed entries. | S11 |
| Leader election | Choosing one node to coordinate writes for a term. | S11 |
| Commit index | In Raft, the highest log index known to be committed by a majority. | S11 |
| Snapshot | A compacted point-in-time state used to catch up a replica or shorten recovery. | S11, S12 |
| Linearizability | A strong consistency model in which operations appear atomic and ordered consistently with real time. | S11 |
| Serializability | A transaction isolation guarantee equivalent to some serial execution of committed transactions. | S12 |
| CAP | During a network partition, a distributed system must sacrifice either availability or strong consistency for the affected operation. | S11 |
| Exactly-once | A delivery/processing guarantee that each effect occurs once, usually implemented with idempotency and deduplication. | S11 |
| At-least-once | A guarantee that a message is delivered one or more times, so consumers must deduplicate. | S11 |
| At-most-once | A guarantee that a message is delivered zero or one time, with possible loss. | S11 |
| Idempotency key | A client-supplied identifier used to suppress duplicate effects across retries. | S11 |
| Clock skew | Difference between clocks on different machines, which breaks naive time-based ordering. | S11 |

## AI and machine learning

| Term | Working definition | See |
| --- | --- | --- |
| Feature | An input variable used by a model. | AI1 |
| Label | The target value a supervised model learns to predict. | AI3 |
| Supervised learning | Learning a mapping from inputs to labelled targets. | AI3 |
| Unsupervised learning | Finding structure in unlabelled data, such as clusters or low-dimensional representations. | AI3 |
| Train / validation / test | Data used to fit parameters, tune choices, and estimate generalization, respectively. | AI3 |
| Leakage | Information from the target or test set contaminating training or feature construction. | AI3 |
| Overfitting | Fitting noise or training-specific detail so that generalization suffers. | AI3 |
| Underfitting | A model too simple or poorly trained to capture the real structure. | AI3 |
| Regularization | A penalty or constraint that discourages overly complex fits. | AI3 |
| Bias-variance trade-off | The balance between systematic error from restrictive assumptions and variance from sensitivity to data. | AI3 |
| Loss function | A scalar objective measuring prediction error during training. | AI2, AI4 |
| Gradient | The vector of partial derivatives of a function; the direction of steepest increase. | AI2 |
| Learning rate | The step size used by gradient-based optimization. | AI4 |
| Epoch | One pass over the training dataset. | AI4 |
| Batch | A subset of examples processed in one optimization step. | AI4 |
| SGD | Stochastic gradient descent: updating parameters from a sampled batch or example. | AI4 |
| Precision | Of the items predicted positive, the fraction that are truly positive. | AI3 |
| Recall | Of the items that are truly positive, the fraction the model finds. | AI3 |
| F1 | The harmonic mean of precision and recall. | AI3 |
| Confusion matrix | A table of predicted versus actual classes. | AI3 |
| ROC-AUC | The probability that a classifier ranks a random positive above a random negative. | AI3 |
| Calibration | Agreement between predicted probabilities and observed frequencies. | AI3 |
| Cross-validation | Repeatedly splitting data into train/validation folds to estimate generalization. | AI3 |
| Embedding | A learned dense vector representation of an item or token. | AI5 |
| Transformer | A neural architecture built from multi-head self-attention, feed-forward layers, residual connections, and normalization. | AI6 |
| Attention | A mechanism that weights information from other positions based on learned query-key similarity. | AI6 |
| Token | A unit of text produced by a tokenizer and processed by a language model. | AI6 |
| Tokenizer | The algorithm mapping text to tokens and back. | AI6 |
| Context window | The maximum number of tokens a model can condition on at once. | AI6 |
| Pretraining | Training a model on a broad corpus with a general objective before task-specific adaptation. | AI6 |
| Fine-tuning | Further training of a pretrained model on a narrower dataset or objective. | AI7 |
| LoRA | Low-rank adaptation: training small low-rank matrices while freezing the base model. | AI7 |
| RLHF | Reinforcement learning from human feedback, often used to align model behavior. | AI7, AI15 |
| DPO | Direct preference optimization: a preference-learning objective that avoids a separate reward model. | AI7, AI15 |
| Inference | Running a trained model to produce predictions or generations. | AI9 |
| KV cache | Cached key/value tensors that avoid recomputing past tokens during autoregressive generation. | AI9 |
| Quantization | Reducing numeric precision of weights or activations to save memory and compute. | AI9 |
| RAG | Retrieval-augmented generation: retrieve relevant passages and condition generation on them. | AI10 |
| Agent | A system that uses a model to choose actions or tool calls toward a goal under constraints. | AI10 |
| Tool call | A structured request from a model to an external function with typed arguments. | AI10 |
| Prompt injection | Manipulating a model through untrusted input so it follows attacker instructions or misuses tools. | AI10, D6 |
| Hallucination | A fluent but unsupported or false model output. | AI6, AI12 |
| Evaluation harness | The reproducible code, data, metrics, and thresholds used to test a model or system. | AI3, AI11 |
| Model card | A document stating a model's intended use, training data, evaluation, limitations, and ethical considerations. | AI12 |
| Data card | A document describing a dataset's source, license, collection, fields, preprocessing, and limitations. | AI13 |
| Data drift | Change in input distribution that can degrade a deployed model. | AI11 |
| MLOps | Engineering practice for reproducible training, deployment, monitoring, and governance of ML systems. | AI11 |
| GPU | A highly parallel processor used for training and serving neural networks. | AI16 |
| CUDA | NVIDIA's programming model and toolchain for GPU computation. | AI16 |
| Kernel (GPU) | A function executed in parallel across many GPU threads. | AI16 |
| Multimodal model | A model that processes or generates more than one modality, such as text and images. | AI14 |
| Recommender system | A system that ranks or selects items for a user from behavior and content signals. | AI18 |
| Time series | A sequence of observations ordered in time, often with trend, seasonality, and autocorrelation. | AI19 |
| Causal inference | Estimating the effect of an intervention rather than an association. | AI17 |
| Confounding | A variable that affects both treatment and outcome, distorting an observed association. | AI17 |

## Security

| Term | Working definition | See |
| --- | --- | --- |
| Asset | Something of value that an attacker could affect: data, availability, money, safety, reputation. | D1 |
| Threat | A potential cause of harm, such as an adversary, accident, or failure. | D1 |
| Vulnerability | A weakness that can be exploited to violate a security property. | D1 |
| Exploit | A technique or input that turns a vulnerability into an effect. | D2 |
| Risk | The combination of likelihood and impact of a threat exploiting a vulnerability in a context. | D1 |
| Trust boundary | A line where data, identity, or privilege changes hands and must be validated. | D1 |
| Attack surface | The set of interfaces, inputs, accounts, and dependencies an attacker can reach. | D1 |
| STRIDE | A threat-classification mnemonic: spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege. | D1 |
| Control | A safeguard that prevents, detects, or limits a threat. | D1 |
| Defense in depth | Layered controls so that one failure does not become a compromise. | D1 |
| Authentication | Proving an identity claim. | D3 |
| Authorization | Deciding what an authenticated identity may do. | D3 |
| Session | Server-side or token-based state that maintains authentication across requests. | D3 |
| CSRF | Cross-site request forgery: causing a victim's browser to send an authenticated state-changing request. | D3 |
| XSS | Cross-site scripting: injecting executable content into a page viewed by another user. | D3 |
| SQL injection | Injecting SQL through unsanitized input to alter a query. | D3 |
| SSRF | Server-side request forgery: making a server fetch an attacker-chosen destination. | D3 |
| IDOR | Insecure direct object reference: accessing an object by changing an identifier without an authorization check. | D3 |
| Path traversal | Using `..` or similar input to escape an intended directory. | D3 |
| Memory corruption | Invalid memory access that can alter control flow or data. | D2 |
| Buffer overflow | Writing beyond the bounds of a buffer. | D2 |
| Use-after-free | Accessing memory after it has been released, often enabling type confusion or code execution. | D2 |
| ASLR | Address space layout randomization, a mitigation that makes addresses unpredictable. | D2 |
| NX / DEP | Marking memory non-executable to block injected code execution. | D2 |
| Stack canary | A sentinel value checked on function return to detect stack corruption. | D2 |
| ROP | Return-oriented programming: chaining existing code gadgets to bypass non-executable memory. | D2 |
| Sandbox | An isolation boundary restricting what untrusted code can access. | D8 |
| seccomp | A Linux facility restricting which system calls a process may make. | D8 |
| Capability | A granular privilege or handle; in Linux, a split of root's powers. | D8 |
| Supply chain | The dependencies, build systems, artifacts, and distribution paths that produce software. | D9 |
| SBOM | Software bill of materials: an inventory of components and versions in an artifact. | D9 |
| SAST | Static application security testing: analysing source or bytecode for weakness patterns. | D9 |
| DAST | Dynamic application security testing: probing a running application. | D9 |
| SCA | Software composition analysis: identifying vulnerable or unlicensed dependencies. | D9 |
| Fuzzing | Feeding generated inputs to a program to find crashes and invariant violations. | D9 |
| CVSS | A standardized severity scoring system; a score is not a complete risk assessment. | D1 |
| CVE | A public identifier for a specific vulnerability. | D1 |
| CWE | A taxonomy of weakness types. | D1 |
| Red team | An adversarial team emulating realistic threats against an authorized target. | D14 |
| Penetration test | A scoped, authorized assessment that validates exploitable weaknesses. | D4 |
| Detection engineering | Designing, testing, and maintaining signals that identify malicious or abnormal behavior. | D7 |
| SIEM | Security information and event management: centralized log collection, correlation, and alerting. | D7 |
| EDR | Endpoint detection and response: endpoint telemetry, detection, and containment. | D7 |
| IOC | Indicator of compromise: an observable associated with an intrusion, such as a hash or domain. | D7 |
| TTP | Tactics, techniques, and procedures: how an adversary operates. | D7 |
| ATT&CK | MITRE's knowledge base of adversary tactics and techniques. | D7 |
| Incident response | The process of preparing for, detecting, containing, eradicating, recovering from, and learning from an incident. | D7 |
| Forensics | Collecting and analysing evidence while preserving its integrity and provenance. | D7 |
| Chain of custody | The documented history of who handled evidence, when, and how. | D7 |
| Privacy | The protection of personal data and the interests of the people it describes. | D10 |
| PII | Personally identifiable information: data that can identify an individual directly or indirectly. | D10 |
| GDPR | The EU General Data Protection Regulation, governing personal-data processing in its scope. | D10 |
| DPIA | Data protection impact assessment: a structured analysis of high-risk processing. | D10 |
| Zero trust | A design stance that does not grant implicit trust based on network location; every request is authenticated and authorized. | D8 |
| Threat hunting | Proactive search for undetected adversary activity using hypotheses and telemetry. | D7 |

## Mathematics

| Term | Working definition | See |
| --- | --- | --- |
| Vector | An ordered tuple of numbers; a point or direction in a vector space. | F4 |
| Matrix | A rectangular array representing a linear map or a table of data. | F4 |
| Rank | The dimension of the image of a linear map. | F4 |
| Eigenvalue / eigenvector | A scalar and nonzero vector satisfying `Av = λv` for a square matrix `A`. | F4 |
| Derivative | The instantaneous rate of change of a function. | F4 |
| Partial derivative | The derivative with respect to one variable while holding others fixed. | F4 |
| Gradient | The vector of partial derivatives; points toward steepest increase. | F4 |
| Chain rule | The rule for differentiating a composition of functions. | F4 |
| Probability | A measure of uncertainty over outcomes, between 0 and 1. | F4 |
| Conditional probability | The probability of an event given that another event occurred. | F4 |
| Bayes' theorem | A rule relating conditional probabilities: `P(A|B) = P(B|A)P(A)/P(B)`. | F4 |
| Expectation | The probability-weighted average of a random variable. | F4 |
| Variance | The expected squared deviation from the mean. | F4 |
| Distribution | A function or rule assigning probabilities to the values of a random variable. | F4 |
| Maximum likelihood | Choosing parameters that maximize the probability of the observed data. | AI2 |
| Hypothesis test | A procedure for deciding whether observed data are consistent with a null hypothesis. | AI2 |
| p-value | The probability, under the null hypothesis, of a statistic at least as extreme as observed. | AI2 |
| Confidence interval | An interval constructed to contain the true parameter at a stated long-run coverage rate. | AI2 |
| Causal effect | The change in an outcome caused by an intervention, not merely associated with it. | AI17 |
| Confounder | A variable affecting both treatment and outcome that can create a spurious association. | AI17 |

## How to use the glossary well

- Prefer the precise term in design reviews and reports; vague language hides missing understanding.
- If you cannot define a term without an example, revisit the course section.
- Do not memorize definitions in isolation. For each term, be able to give an example, a counterexample, and a failure mode.
- When two terms are often confused, write the distinction explicitly: latency vs throughput, concurrency vs parallelism, authentication vs authorization, vulnerability vs risk, linearizability vs serializability.
