# SYS7 — Performance Engineering & Observability

**Program:** SYS — Systems Engineering
**Type:** `course`
**Prerequisites:** [SYS3](SYS3.md), [SYS4](SYS4.md)
**Duration:** 12–16 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–15 focused hours/week (provisional)

> [Systems Engineering](README.md) · [Course format](../../spec/course-format.md) · [Design guide](../DESIGN-GUIDE.md)

## Overview

**SYS7 teaches evidence-grounded systems performance diagnosis, not performance theater or a mandatory speedup.** [SYS1](SYS1.md) has already established machine-level cache/processor models, [SYS3](SYS3.md) has assessed lock-contention, concurrent progress and correctness, and [SYS4](SYS4.md) has assessed a bounded, multi-client Rust service with observable latency and backpressure. SYS7 connects those competencies to **scientific workload design; CPU/off-CPU profiling and causal attribution; carefully budgeted metrics/logs/traces; queue stability, tails and coordinated omission; controlled cross-layer fault experiments; and a defensible optimization decision**. [SYS6](SYS6.md)'s replication measurements can provide an optional advanced workload, but **SYS6 is not a SYS7 prerequisite**. [SYS8](SYS8.md) later uses these measurements to make production capacity and operational decisions; SYS7 does not pre-award operating SLAs.

**Core investigation:** Reuse one previously assessed SYS4-style local Rust service or a clearly specified public synthetic equivalent. Build an independent response oracle, a bounded client-load generator with an explicit *offered* workload, an instrumentation layer and a reproducible measurement harness; collect a CPU sample stack or a sufficiently disclosed source-level approximation, a separate wait/off-CPU observation, privacy-safe metric/log/trace evidence and at least one **causally discriminating** intervention. A legitimate final result may recommend **no change**, reject an appealing optimization or report that the available observations cannot distinguish two causes. Independent correctness and a transparent failure or falsification case are more important than an arbitrary percentage improvement.

**Measurement precision:** A response-dependent closed-loop generator may *coordinate with a stalled server* by sending fewer requests, hiding the latency impact of waiting users. For an open-loop capacity or tail claim, preserve **scheduled arrival time**, actual send/admit time, completion/error or timeout and missed/unsent-arrival counts; otherwise disclose the different closed-loop workload claim. Distinguish offered, admitted, successful, rejected, failed and pending work, and separate CPU execution, runnable wait, lock/I/O blocking and client wall-clock response. Quantiles require population, sample count and method—**do not infer a trustworthy p99 from a handful of values**, add per-stage percentiles, or average independent p95s. Apply `L = λW` only to a consistently defined, stable system with an effective admitted rate; sustained overload backlog is not a steady-state queue.

**Reproducible access:** A normal nonprivileged Linux machine and stable Rust/Cargo are sufficient. If `perf`, eBPF, system-wide tracing or CPU counters are blocked by kernel access policy, use per-process/thread timing, bounded user-space spans and independently supplied sampling/trace fixtures; honestly document what cannot be attributed. No root, `perf_event_paranoid` relaxation, paid telemetry service, proprietary profiler, privileged production access or public load test is required. Any synthetic local experiments must publish finite CPU, disk, thread, network, memory and time limits. Treat raw identifiers, arbitrary paths, request payloads and trace metadata as potential sensitive data. High-cardinality metric attributes are not free: bound combinations and emission cost as part of the performance contract.

**Workload estimate:** The existing **12–16 weeks** at **10–15 focused hours/week** (approximately 120–240 hours) remains provisional, covering study, instrument design, controlled experiments, diagnosis, raw-data interpretation, revision and defense. This is not a learner-completion clock or claim of independently verified readiness. Preserve all **12 stable outcome IDs and five summative assessment IDs**; only this source revision strengthens their public assessment requirements, without retroactive regrading of prior evidence.

## Learning outcomes

- **SYS7-O1:** Define a falsifiable performance question and distinguish symptoms, candidate causes and independent measurements.
- **SYS7-O2:** Design correct, reproducible throughput and latency benchmarks with warmup, controls, repetitions, variability and workload realism.
- **SYS7-O3:** Interpret CPU profiles, call stacks and flame graphs with sampling and inlining limitations.
- **SYS7-O4:** Investigate blocked/off-CPU time, I/O, lock contention, memory pressure and event-loop scheduling using suitable evidence.
- **SYS7-O5:** Design service metrics, structured logs and distributed or local traces with cardinality, correlation and privacy constraints.
- **SYS7-O6:** Explain queues, utilization, Little's Law and capacity bottlenecks while identifying assumptions of the chosen model.
- **SYS7-O7:** Analyze percentile/tail latency, coordinated omission and queue-induced collapse without confusing percentiles with averages.
- **SYS7-O8:** Correlate load, resource saturation, errors and traces to discriminate CPU, memory, storage, network and synchronization constraints.
- **SYS7-O9:** Perform safe workload and fault experiments on bounded local services, including a controlled negative or invalid hypothesis.
- **SYS7-O10:** Evaluate a proposed optimization against correctness, repeatability, implementation cost and regression risk.
- **SYS7-O11:** Write an independent performance report with inspectable data, uncertainty, alternative explanations and no unsupported generalization.
- **SYS7-O12:** Defend an unfamiliar bottleneck investigation and revise the experiment or implementation when new evidence contradicts the first diagnosis.

## Modules

### Module 1 — Performance Science, Service Contracts and Causal Questions

#### Outcomes

- SYS7-O1
- SYS7-O2
- SYS7-O10
- SYS7-O11

#### Lessons

1. **From component timing to service behavior** — Build on SYS1's CPU/cache experiments, SYS3's lock-contention measurements and SYS4's framed multi-client workload instead of reteaching their APIs. Define new end-to-end attribution: how a local service's queueing, execution, I/O and instrumentation combine into a client-observed outcome.
2. **Symptoms, mechanisms and causal hypotheses** — Separate an observed p95 latency increase from candidate causes such as run-queue delay, expensive handler, socket backpressure or allocation churn. Formulate at least two falsifiable hypotheses with different predicted traces.
3. **Service-level measurement contract** — Specify request type, accepted/completed/rejected/error semantics, identical useful work, timing boundaries, timeouts and resource constraints. Explain why success-only throughput or a fast but incorrect response cannot demonstrate improvement.
4. **Independent correctness and baseline oracles** — Reuse SYS4's separately derived request/response fixtures or an equivalent public synthetic component. Count original request IDs and client-verified results, not only server log success, before comparing performance variants.
5. **Measurement boundaries and clocks** — Use a monotonic clock for local durations and distinguish wall time, task CPU time, cumulative CPU time across threads and process uptime; reject comparing unsynchronized multi-process timestamps as proof of one causal order.
6. **Controlled comparisons and confounding** — Name the independent variable, controls and response metric before testing; account for build profile, core count, data set, background processes, temperature and cache state rather than attributing every fluctuation to code.
7. **Hypothesis discrimination** — Design a perturbation that differs between the two proposed causes, such as changing handler CPU work versus queue admission. Explain what outcome would reject each hypothesis rather than always accepting an improvement narrative.
8. **Validity, transfer and negative results** — Distinguish internal validity for one lab from generalization to other machines and production traffic. Require a preserved negative or inconclusive result where a plausible first hypothesis is contradicted by measurement.
9. **Ethics and resource budget** — Limit loops, threads, processes, fixture files, load duration, CPU and buffer allocations; collect no production customer payload or unconsented trace data and ensure tests cannot accidentally overwhelm a public listener.

*Optional formative feedback:* Review a synthetic p95 regression under fixed correctness: state two incompatible causes and one independent observation that separates them.

### Module 2 — Benchmark Design, Offered Load and Statistical Evidence

#### Outcomes

- SYS7-O2
- SYS7-O7
- SYS7-O9
- SYS7-O11

#### Lessons

1. **Target workload and operation mix** — Specify synthetic request sizes, key distributions, CPU/I/O mix, concurrency, arrival patterns, success/error policy and workload seed; reject results from a workload that changed data or did less intended work.
2. **Warmup and experimental phases** — Separate tool setup, startup, warmup, steady-state observation, overload and cooldown. Define windows and explain why a single averaged whole-run number hides transients or drift.
3. **Open-loop versus closed-loop load** — Compare fixed scheduled arrivals independent of completion with response-driven client populations. Choose the model matching the intended question, and report the actual arrivals and outstanding requests in either model.
4. **Coordinated omission and missed arrivals** — Trace a server pause that prevents a closed-loop generator from sending its next request; show the resulting undercounted client waiting. Use scheduled-arrival-to-completion timing and count late/unsent requests when evaluating an open-loop claim.
5. **Offered versus admitted versus completed** — Publish attempt, admission, successful completion, rejection, timeout and still-pending counts plus elapsed time. Avoid quoting client-side success-only latency as overall quality under overload.
6. **Generator saturation and backpressure** — Measure load-generator CPU, request scheduling drift and outstanding-operation caps separately from service capacity; detect a client that silently reduces offered load when the server slows.
7. **Raw trials and randomization** — Record at least five independent timed trials for each comparable configuration, randomized or alternated variant order where possible, actual units, run-level summaries and complete raw artifacts rather than the best single run.
8. **Effect, spread and sample size** — Compare effect magnitude against run-to-run spread using a stated descriptive or inferential method; do not treat observations from the same busy second as independent replications or infer stable p99 from a tiny sample.
9. **Correctness and overhead budget** — Check each run's outputs against an independent oracle and record benchmark harness/instrumentation overhead; a profiler that changes the workload or scheduling invalidates naïve apples-to-apples timing.

*Optional formative feedback:* Show how a one-second pause appears in scheduled-arrival and response-driven load logs, then classify rejected and unfinished requests without hiding them.

### Module 3 — On-CPU Profiling, Call Stacks and Attribution Limits

#### Outcomes

- SYS7-O3
- SYS7-O8
- SYS7-O10

#### Lessons

1. **Statistical sampling versus event tracing** — Contrast sampled call stacks, exact-instrumented function spans and event counters, explaining overhead and why a sample percentage is not a count of every instruction or a complete execution trace.
2. **Build symbols, inlining and optimization** — Compile a bounded Rust service with recorded build flags, debug symbol settings and optimization profile. Explain missing frames, inlined functions and tail calls without concluding that an omitted frame consumed no time.
3. **Inclusive and exclusive cost** — Interpret inclusive stack width, exclusive leaf cost, recursive stacks and call-path aggregation; distinguish percentages of sampled CPU time from wall-clock request latency and do not sum overlapping inclusive costs as disjoint.
4. **CPU flame graph reading** — Use a supplied or generated flame graph/call-stack histogram to find hot branches. Explain why rectangle color and horizontal placement do not directly encode event time, thread scheduling or exact cost.
5. **Sampling frequency and observer effect** — Compare low versus high sampling or manual timers with measurement overhead; track sample counts and check for systematic bias, lost samples, periodic aliasing or missed short functions.
6. **CPU execution versus run-queue waiting** — Distinguish a runnable-but-unscheduled thread from a thread executing instructions. Use process/task CPU and wall-clock measurements to reject a simplistic '100% CPU' interpretation on multicore hardware.
7. **Cache, branch and allocator hypotheses** — Link suspected cache misses, frequent allocations, instruction work and branch behavior to a concrete alternate observation; hardware performance-counter values are optional and architecture-dependent.
8. **Nonprivileged profiling fallback** — Use optional perf only where access policies permit; otherwise record self-instrumented spans, per-thread CPU or supplied sample traces with precise limits. Root, perf_event permission changes and proprietary profilers are not assessment prerequisites.
9. **Independent attribution challenge** — Evaluate two competing flame/call-stack interpretations against the same workload and choose a discriminating measurement, e.g. total CPU consumed versus high off-CPU time, instead of optimizing the largest-looking block blindly.

*Optional formative feedback:* Label exclusive versus inclusive samples in a short stack tree and find a counterexample where the apparent hot function is not the end-to-end latency bottleneck.

### Module 4 — Off-CPU Time, Locks, Scheduling and I/O Wait

#### Outcomes

- SYS7-O4
- SYS7-O8
- SYS7-O9

#### Lessons

1. **State model for request time** — Break one service request into queue wait, runnable-but-not-running, active CPU, sleeping on a lock, disk or network, response queue and client network time; label which periods can overlap across threads.
2. **Runnable pressure and context switches** — Compare a CPU-bound worker, oversubscribed thread pool and deliberately starved reactor using run queue/runnable counters or deterministic trace fixtures; do not mistake high wall time for high CPU usage.
3. **Mutex hold versus wait costs** — Apply SYS3's lock invariants to separately measure guard hold time, acquisition wait and work completed; show why reducing lock time could be irrelevant if another resource remains saturated.
4. **Event-loop fairness and blocked handlers** — Instrument SYS4-style ready, admitted, read, parsed, queued and write-complete transitions; identify accidental blocking handler work or unconditional writable-interest spin without reteaching epoll coding.
5. **Storage flush and filesystem delays** — Distinguish the duration of a local file sync call, buffered write and background writeback. A slow sync fixture is evidence of measured waiting, not a proof that every storage device has the same persistence behavior.
6. **Socket queue and slow-client behavior** — Trace an output buffer cap and TCP send backpressure under slow readers; distinguish application queueing from kernel socket buffers and from remote host delay.
7. **Memory pressure, allocation and page faults** — Use bounded allocations, process RSS or application counters and known synthetic pressure to distinguish allocator contention, page fault latency and process memory growth; avoid destructive host OOM tests.
8. **Wait-state source provenance** — Correlate timers and trace events to code or supplied OS traces and classify exact observable versus inferred wait cause. State when a tool lacks privilege or fidelity to distinguish scheduler delay from an I/O event.

*Optional formative feedback:* Given one 400-ms request with 5-ms CPU and long blocked spans, formulate a useful follow-up instead of replacing a CPU loop.

### Module 5 — Service Metrics, Logs, Traces and Telemetry Budgeting

#### Outcomes

- SYS7-O5
- SYS7-O8
- SYS7-O11

#### Lessons

1. **Signals and decisions** — Define a minimal metric/trace/log schema supporting concrete questions: throughput, errors, queue backlog, stage latency and resource saturation. Explain why instrumentation with no decision or bound imposes unjustified overhead.
2. **Counters, gauges and histograms** — Select correct units and temporality for total requests, in-flight jobs, queue depth and latency distributions; avoid interpreting a per-process counter reset as a physical decline in demand.
3. **Label cardinality as a capacity constraint** — Calculate combinations of method/status/route attributes and the blow-up from raw request IDs, user IDs or arbitrary paths; enforce a published cardinality budget and use stable bounded labels for metrics.
4. **Safe structured log events** — Record bounded event type, stage, request correlation ID and error category, redacting keys, payload bytes, credentials and personal addresses; reject newline/log injection and unlimited debug dumps.
5. **Spans and causality in one service** — Construct a request timeline from local client schedule, accept, queue, execute, I/O and response spans, relating parent/child and correlated identifiers without confusing span duration with sampled CPU cost.
6. **Across processes and clock skew** — Explain message-causal context propagation, clock offset and missing spans; when joining client/server or multiple processes, use monotonic local durations and logical links rather than subtracting unsynchronized wall clocks as an exact latency breakdown.
7. **Sampling and missing data** — Compare head-based, tail-based or deterministic sampling at a conceptual level, state event/drop percentages and explain why an unsampled long-running error could alter reported tail behavior.
8. **Metrics/histogram aggregation caution** — Distinguish aggregating raw latency observations or compatible histograms from averaging per-instance percentiles; explicitly preserve units, bucket schemes and population weighting when merging summaries.
9. **Privacy, retention and instrumentation overhead** — Limit high-cardinality logs, metric streams, buffer sizes, trace retention and collection frequency. Quantify or bound extra per-request work and ensure the observed behavior is not primarily caused by an invasive diagnostic.

*Optional formative feedback:* Design a 5-metric schema and three trace events for a loopback service, then identify one label that would create unbounded series and one secret that must not be logged.

### Module 6 — Queueing Models, Tail Latency and Sustainable Capacity

#### Outcomes

- SYS7-O6
- SYS7-O7
- SYS7-O8
- SYS7-O9

#### Lessons

1. **Arrival, service and departure rates** — Define offered arrival rate, admitted effective arrival rate and completed departure rate, separating requests blocked or rejected at admission from actual service capacity.
2. **Little's Law with valid boundaries** — Compute L = λW for a steady-state stable system with consistent population and effective admitted throughput; distinguish queue-only Lq/Wq from total in-flight L/W and reject applying equilibrium arithmetic to a growing outage queue.
3. **Utilization and bottleneck saturation** — Analyze a one-server or worker-pool queue with service demands and bounded concurrency. Explain why high utilization can correspond to rapidly growing wait time even when useful CPU work per request is unchanged.
4. **Finite buffers and overload policy** — Model fixed queue depth, blocking clients, timeout, fast rejection and slow-reader backpressure under fixed offered load. State which strategy bounds memory and which moves waiting into the client.
5. **Latency mean, median and quantiles** — Compute a hand-ranked small dataset's median and a declared nearest-rank p95 with units; explain why p99 from a very small sample is poorly resolved, and why percentiles cannot be added across stages or averaged without care.
6. **Tail amplification from queues** — Trace a short service pause through a finite FIFO queue and calculate later requests' waits, distinguishing service-time variance, head-of-line blocking, scheduling interference and admission queue backlog.
7. **Coordinated omission under tail events** — Construct an arrival schedule that continues through a stall; compare recorded completed-only latency with scheduled-arrival-to-completion delays and the count of dropped/unserved requests, and explain residual bias in any histogram correction.
8. **Open-loop stability and collapse** — Use finite synthetic arrivals to show throughput plateau, queue growth, refusal and timeouts at overload. Mark the offered-load region where the system no longer achieves steady state; refuse to extrapolate that region using Little's Law as if stationary.
9. **Capacity estimation and headroom** — Derive a cautious service capacity range from repeated tests and confidence limitations, including error and tail-latency budgets rather than highest one-minute successes; no global SLA or production instance count follows automatically.
10. **Queue policy and fairness limits** — Compare FIFO, limited priority and bounded fair service under small synthetic job classes, including how an optimization for average response can harm a minority tail or reject rate.

*Optional formative feedback:* Calculate L, W, λ for a stable offered workload and then show why the same algebra misleads when the queue increases by 10 requests every second.

### Module 7 — Cross-Layer Fault Experiments and Causal Attribution

#### Outcomes

- SYS7-O4
- SYS7-O8
- SYS7-O9
- SYS7-O12

#### Lessons

1. **Build a causal hypothesis table** — List competing CPU saturation, scheduler wait, lock contention, allocator/memory pressure, disk sync, network slow-reader and test-harness defects; associate each with expected metric, wait trace and controlled intervention.
2. **CPU-busy versus worker-starved contrast** — Inject bounded extra CPU work and, separately, run-queue pressure with a capped thread count, then compare CPU time, wall time, queue depth and completed work under the same correctness oracle.
3. **Lock contention versus lock hold** — Introduce a bounded critical-section delay or false-sharing fixture and measure acquisition wait, per-worker progress and application throughput; avoid inferring deadlock merely from a finite stalled sample.
4. **Memory and allocator interference** — Use limited synthetic object allocation or working-set change and observe RSS, fault count where available and latency; preserve safety bounds and state which measurements cannot identify cache miss or allocator internals exactly.
5. **Disk latency and recovery effects** — Inject local synthetic file-sync delay through a controlled adapter or temporary fixture, distinguishing it from real device persistence, and check whether server queue latency or client retry policies amplify the delay.
6. **Network and slow-peer backpressure** — Run two or more loopback clients with a deliberately slow reader or fragmented writes and contrast application write-queue backlog with CPU samples, read-ready signals and end-to-end response completion.
7. **Observer and load-generator faults** — Insert logging overhead, lost trace samples or saturated client scheduler as adversarial measurement conditions; identify how apparently favorable throughput/latency can result from missing work or changed offered traffic.
8. **Discriminating experiments with independent outcomes** — Before each injection predict which two metrics should diverge if the hypothesis holds and identify a falsifier. Record raw positive/negative observations rather than choosing explanations after seeing the chart.
9. **Failure and safe cleanup** — Cap all local CPU/memory/network/file experiments, restore fixture state and confirm process/port/temporary-file cleanup; no public endpoint, root, synthetic kernel fault or real customer data is used.

*Optional formative feedback:* Given rising p99 but flat request CPU, choose one wait-state probe and a deliberate perturbation that would distinguish a slow reader from scheduler starvation.

### Module 8 — Optimization, Regression and Decision Quality

#### Outcomes

- SYS7-O2
- SYS7-O9
- SYS7-O10
- SYS7-O11

#### Lessons

1. **Protect correctness and user-visible contracts** — State byte/protocol outputs, admission/refusal policies, deadline meaning and resource budgets that must not change before optimization. A faster result that omits requests or weaker durability is not a like-for-like speedup.
2. **Choose one evidence-grounded intervention** — Rank at least two possible changes by mechanism, expected effect, complexity and risks; select only a targeted change whose predicted observations distinguish it from simpler alternatives.
3. **Matched baseline and changed variant** — Run equivalent inputs, Rust build flags, request IDs, warmup and resource limits, alternating version order if possible to reduce drift; retain both exact commits and repeatable clean-checkout instructions.
4. **Measure improvement and variance** — Publish five or more raw timed trials for each comparable variant, unit-labeled center/spread, sample counts and the unmodified correctness oracle; avoid asserting significance without an appropriate statistical model.
5. **Observe regressions and displacement** — Check the intended primary metric plus client errors, p95/tail, memory, I/O, CPU and queue pressure to detect a change that merely moves work to another resource or worsens important edge cases.
6. **Discuss economics and maintainability** — Account for code complexity, portability, testing burden, CPU time, memory and instrumentation cost. Decide whether a small uncertain gain justifies ongoing maintenance or operational risk.
7. **Negative and inconclusive experiment decisions** — Present a previously plausible change that failed, could not be distinguished from noise or hurt correctness; recommend retain, revert or gather more evidence without fabricating a gain.
8. **Regression guard with limitations** — Add a small reproducible benchmark regression fixture and behavior test with declared tolerance, machine variation and false-alarm risk; preserve failed raw runs rather than enforcing a flaky universal latency gate.

*Optional formative feedback:* Review before/after reports where throughput rises but p99 latency and errors worsen; decide against declaring a general speedup.

### Module 9 — Integrated Performance Investigation and Independent Technical Defense

#### Outcomes

- SYS7-O1
- SYS7-O2
- SYS7-O3
- SYS7-O4
- SYS7-O5
- SYS7-O6
- SYS7-O7
- SYS7-O8
- SYS7-O9
- SYS7-O10
- SYS7-O11
- SYS7-O12

#### Lessons

1. **Select one inspectable prior service** — Use the SYS4 bounded Rust multi-client service or a freely supplied equivalent with validated request bytes; SYS6 replication is optional context, not a new hidden prerequisite or mandatory platform.
2. **Publish performance and evidence question** — Define the user-visible symptom, at least two distinct causal hypotheses, workload/arrival schedule, correctness oracle, numerical resource limits, negative prediction and comparison plan before running experiments.
3. **Instrument minimum useful observability** — Add bounded metric labels and histogram, privacy-safe trace spans and structured events for admission, queue, handler, I/O and completion, with calibrated overhead and no hidden paid backend.
4. **Record baseline and wait/CPU profiles** — Collect timed workload trials, raw client results and a CPU sample stack or source-trace equivalent plus at least one off-CPU/wait observation, clearly separating inferred causes from measured events.
5. **Test a causal intervention** — Perturb one bottleneck condition without violating a public contract, compare against unchanged controls, retain complete negative and anomalous results and confirm the client-side result set remains correct.
6. **Evaluate the optimization decision** — If a change is warranted, implement a bounded minimal revision with matched trials, new risk analysis and a regression fixture; otherwise defend why leaving code unchanged better follows the evidence.
7. **Unseen workload or trace contradiction** — Accept a new reviewer-supplied finite workload, misleading flamegraph or missing-span scenario, state two competing explanations and run a discriminating test before defending a revised causal model.
8. **Evidence, applicability and handoff** — Deliver raw measurements, scripts, environment/tool permissions, independent oracles, privacy/resource policies, uncertainty, rejected explanations, limitations and a written, recorded or live reviewable technical defense suitable for SYS8 design decisions.

*Optional formative feedback:* Have a reviewer change the request mix after you name the bottleneck; predict which metric should move and revise the diagnosis if the change falsifies it.

## Completion requirements

**Five public summative assessments establish all SYS7-O1–SYS7-O12.** Lessons, informal profiling practice and optional hardware observations are formative; the same bounded SYS4-style service and its test fixture may support AS1–AS5 while the independent outcome/evidence criteria remain distinct. **No arbitrary speedup, particular paid tool, privileged counter or mandatory production dashboard** is required. If the evidence rejects the initial hypothesis or supports no safe optimization, that is an acceptable engineering decision when all associated diagnostic and evidential criteria are genuinely satisfied.

- **SYS7-AS1** — Reproducible Load Design, Queue Mathematics and Baseline
  - **Outcomes:** SYS7-O1, SYS7-O2, SYS7-O6, SYS7-O7.
  - **Work:** Specify a falsifiable service performance question and **two competing causes**, a correct public synthetic workload and a separate accepted/completed/error oracle. Design either a scheduled-arrival (open-loop) trial or a correctly caveated response-driven (closed-loop) trial, plus a deliberate server-stall/capacity boundary case. Independently solve **at least three numerical cases**: steady-state `L = λW` with the appropriate population/effective rate, overload growth violating steady-state assumptions, and client-latency percentiles/omitted requests with a declared quantile rule. Run baseline configurations with at least **five raw independent timed trials each**, fixed useful work and a recorded environment.
  - **Criteria:** Request/event timing boundaries, offered/admitted/successful/refused/pending counts and units are explicit; correct outputs and error/timeout policy are checked independent of service instrumentation. Workload arrival scheduling is not silently controlled by response time when claiming open-loop behavior, and slow/hung requests do not vanish from the tail or denominator. Queue and Little's Law calculations distinguish admitted versus attempted requests, total-in-system versus queue-only averages and stable versus growing queues; percentile calculations state rank rule and credible sample granularity. Raw trial spread, warmup, caching, harness scheduling drift and host noise are disclosed; a one-off best run is not a result.
  - **Evidence:** Public experiment protocol, independent request/response fixture and load-generator logic, initial two hypotheses, arrival/completion event schedule, three hand-checked calculations, raw repetitions and result/error counts, environment/build data and honest threats to validity.

- **SYS7-AS2** — CPU Profiles, Off-CPU Wait and Competing Cause Attribution
  - **Outcomes:** SYS7-O3, SYS7-O4, SYS7-O8.
  - **Work:** For **at least two different constrained bottleneck scenarios**, collect and interpret a sampled CPU stack/flame representation or labeled public fixture together with independent source-level CPU/wall timing and a wait/off-CPU/event history. Include a CPU-bound versus blocked/scheduled scenario and identify a discriminating observation for two plausible explanations; use nonprivileged tracing or supplied samples when `perf` is unavailable.
  - **Criteria:** Interpret inclusive versus exclusive sample attribution, inlining/missing frames, samples-versus-complete-events, runnable versus blocked time and process/thread CPU versus client elapsed time correctly. Tie an observed queue, lock, I/O or scheduling delay to trace events without asserting that an unsampled function did zero work or that a CPU flame block proves client tail latency. Give one hypothesis that data **rules out or leaves unresolved** and quantify or at least characterize measurement overhead and privilege limitations. All required evidence is reproducible without CAP_PERFMON, root or a proprietary profiling backend.
  - **Evidence:** Annotated sample/call-stack or flame data, independently timed CPU/wait spans, declared tool settings and sample counts, two explicit causal predictions, differing expected/observed traces, bottleneck-specific alternative explanations and limitations.

- **SYS7-AS3** — Privacy-Safe Instrumentation, Tail and Capacity Evidence
  - **Outcomes:** SYS7-O5, SYS7-O6, SYS7-O7, SYS7-O8, SYS7-O9.
  - **Work:** Instrument the **same bounded local service** with minimal counters, a latency distribution/histogram, queue-depth/saturation gauges, structured logs and correlated request spans covering arrival or admission through response. Use a **declared metric-attribute cardinality budget**, bounded trace/log buffering and synthetic IDs. Exercise normal traffic plus a controlled burst, slow-client/handler pause or rejection/timeout overload, and compare scheduled arrivals with observed completions.
  - **Criteria:** The observability schema and numeric limits separate offered, admitted, completed, failed, rejected and pending work; queue and resource saturation expose overload rather than hiding it behind successful responses. At least one trace accurately distinguishes CPU, queue wait and blocked I/O with a published uncertainty/clock-domain disclaimer. Cardinality limits reject arbitrary request IDs/usernames/raw URLs as metric labels; bounded storage and negative payload/log-injection cases protect secrets and prevent telemetry-driven resource runaway. Mean/median/tail claims specify sample size and missing data; histogram or multi-process aggregation does not incorrectly average percentiles or treat unsynchronized clock offsets as precise causal durations. Instrumentation overhead is checked against an uninstrumented or low-overhead baseline.
  - **Evidence:** Service instrumentation source/schema, explicit label-combination and memory budget, safe log/trace fixtures, reproducible normal/overload workload and independent client oracle, arrival/queue/response timeline, histogram or raw latency observations, cardinality/privacy negative tests and observed overhead.

- **SYS7-AS4** — Controlled Performance Intervention and Regression Decision
  - **Outcomes:** SYS7-O2, SYS7-O9, SYS7-O10, SYS7-O11.
  - **Work:** Investigate one significant suspected bottleneck on the AS3 service with a causal prediction, run one controlled perturbation and test a small proposed code/queue/configuration change **or a justified do-not-change decision**. Collect comparable before/after or intervention/control evidence in **at least five independent timed trials per meaningful condition**, with correct matched inputs, useful-work/error accounting and one unchanged/negative test that could invalidate the explanation.
  - **Criteria:** All variants honor identical published correctness, request-admission, timing and resource contracts; no hidden speedup from disabled work, dropped responses, weaker durability or omitted slow requests. Raw per-run units, robust center/spread, environmental variation and quantile sample limitations are visible, with no unjustified statistical certainty. Distinguish effect on targeted CPU/wait/queue mechanism from a moved bottleneck or a worse tail/error rate, evaluate complexity/portability/operational costs and explicitly accept negative/inconclusive evidence. A minimally scoped regression guard preserves correctness and discloses machine-noise thresholds; only a warranted improvement is claimed.
  - **Evidence:** Hypothesis and predicted discriminator written before measurement, exact baseline/intervention code/flags, full raw trial dataset, client correctness and errors, before/after trace or profile comparison, alternative-cause discussion, documented retain/revert/no-change decision and a bounded regression fixture.

- **SYS7-AS5** — Unfamiliar Service Performance Incident Defense
  - **Outcomes:** SYS7-O1, SYS7-O3, SYS7-O4, SYS7-O5, SYS7-O8, SYS7-O10, SYS7-O11, SYS7-O12.
  - **Work:** Diagnose an **unseen** bounded workload, profile/log/trace contradiction or performance regression supplied by a reviewer or transparent public variant generator, such as high p99 with low CPU, unexpectedly flat throughput, hidden coordinated omission, a cardinality explosion or a slow-reader cascade. Before collecting more data, record **two competing causal explanations and a predicted distinguishing observation**. Reuse the same service or supplied synthetic fixtures, run a discriminating measurement, revise or reject the first diagnosis, and defend a minimal safe change, no-change decision or justified evidence limitation.
  - **Criteria:** Link an observed symptom to the actual affected work/population, correctly identify sample, clock, arrival/load-generator, instrumentation and resource confounders, and avoid retrofitting a hypothesis solely from a successful optimization run. The corrected or declined intervention preserves independent behavioral oracles and makes one independently checkable prediction on the unseen case, with before/after results and credible uncertainty. State what remains untested and why one local workstation's measurement cannot establish a universal production SLO. An unexamined flame graph or speculative bottleneck label is insufficient evidence of SYS7-O12.
  - **Evidence:** Unseen challenge source/seed, pre-measurement hypotheses, exact discriminator and expected outcomes, raw client, queue, profile and instrument traces, negative/positive regression evidence or justified constrained refusal, decision report and written/recorded/live technical defense.

### Discipline ownership, access and operational safety

SYS1 already assesses architectural cache/CPU modeling; SYS3 assesses locks, atomic memory order and local contention under concurrency correctness; SYS4 assesses correct multi-client framing, nonblocking readiness and service resource limits; SYS6 may provide optional replicated workloads. SYS7 owns **end-to-end experimental design, measurement instrumentation, on-/off-CPU causal diagnosis, queue/tail analysis, controlled interventions and scientific performance decisions**. [SYS8](SYS8.md) owns service architecture/capacity/SLO policy and production operations, while [SYS9](SYS9.md) integrates independent performance evidence into its capstone. A capacity **estimate** from SYS7 is not a guarantee of system availability, and good profiling cannot substitute for correctness evidence.

All mandatory experiments use learner-controlled loopback services, synthetic data and resource budgets. A reference sample/flame trace and manually instrumented Rust code are valid when host perf/eBPF access is restricted, provided the evaluation explicitly distinguishes real measurement from supplied/simulated traces. Do not relax kernel security configuration, require root or load-test public services. Keep sensitive payloads, personally identifying labels and secrets out of submitted logs and traces. Text tables and equivalent state traces may substitute for visual flame charts when their attribution/interpretation remains decidable.

### Revision, independent review and readiness

All **SYS7-O1–SYS7-O12** and **SYS7-AS1–SYS7-AS5** identities are retained. Expanded assessment criteria for offered load, missing tail observations, privacy-safe cardinality, multiple raw trials, cross-layer cause discrimination and explicit no-change decisions apply to **this source revision**, not retroactively to earlier completed evidence. Every summative decision records course/spec revision, outcome/assessment IDs, actual environmental and workload constraints, independently expected versus observed results, qualified review, meaningful limitations and a reproducible source/configuration reference. Passing repository CI or obtaining a performance percentage does not promote this course from `draft`; real learner trials and independent academic review remain required.

## Optional disciplinary references

These public references aid study and are not mandatory paid readings, hidden evaluations or claims of institutional accreditation:

- [Linux perf events security and permissions](https://docs.kernel.org/admin-guide/perf-security.html) — Linux `perf_event_paranoid`, CAP_PERFMON, per-process and system-wide profiling constraints.
- [Linux perf_event_open(2)](https://man7.org/linux/man-pages/man2/perf_event_open.2.html) — sampled performance monitoring and architecture/platform limitations.
- [OpenTelemetry metrics](https://opentelemetry.io/docs/concepts/signals/metrics/) and [semantic conventions](https://opentelemetry.io/docs/specs/semconv/general/metrics/) — instrument semantics, label cardinality and data collection contracts.
- [HdrHistogram documentation](https://hdrhistogram.github.io/HdrHistogram/JavaDoc/) — histogram population/precision, expected-interval correction and coordinated-omission limitations.
- [Coordinated-omission explanation in wrk2](https://github.com/giltene/wrk2) — why response-driven request generation can hide pauses and how scheduled arrivals change the latency claim.
- [Little's Law and its assumptions](https://www.columbia.edu/~ww2040/4615S15/LittlesLawNotes012715.pdf) — steady-state population, throughput and residence-time relationships.
