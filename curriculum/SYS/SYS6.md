# SYS6 — Distributed Systems

**Program:** SYS — Systems Engineering
**Type:** `course`
**Prerequisites:** [SYS4](SYS4.md), [SYS5](SYS5.md)
**Duration:** 18–24 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–15 focused hours/week (provisional)

> [Systems Engineering](README.md) · [Course format](../../spec/course-format.md) · [Design guide](../DESIGN-GUIDE.md)

## Overview

**SYS6 develops failure-aware distributed reasoning and a verifiably bounded replicated-state service.** [SYS4](SYS4.md) already teaches Rust multi-client networking, framing, backpressure and ambiguous transport failure; [SYS5](SYS5.md) already teaches WAL durability, log replay and snapshot/manifest publication; [SYS3](SYS3.md) covers concurrent histories, invariants and progress. The new intellectual challenge is that *separate processes and replicas cannot share an instantaneous observation*: message delay can look like failure; retry can duplicate a committed effect; a durable local log is not a distributed commit; and a single responding leader cannot guarantee that it is still authorized.

**Core assessed design:** Implement one **three-node, fixed-membership, non-Byzantine, crash-recovery, leader-based Rust replicated key-value service**, using separate local process/file identities and a controllable message scheduler. Teach **Raft's actual safety obligations** to the extent claimed by the executable reference: persistent term/vote and log records, up-to-date-log voting, matching-prefix append, safe conflict handling, current-term majority commit, commit-before-apply and ordered deterministic execution. A client success response for a durable write requires that the entry is *durably replicated to a quorum*, committed by the specified rule and applied. The teaching implementation may intentionally omit production features such as membership reconfiguration, leases, optimized ReadIndex, rolling upgrades, snapshot-install implementation and multi-region deployment, but **must not claim consensus safety if it drops a rule necessary for that claim**. If a feature is incomplete, publish and enforce a narrower guarantee/refusal state rather than equating a toy log with production Raft.

**Client semantics:** Define stable client-session/operation identity and a replicated, restart-recoverable deduplication result within a stated finite retention window; a lost response after committing an increment is an **unknown client outcome**, not proof of rollback. Provide an explicitly safe *strong-read path* by committing/applying a read barrier or read-command entry through a current-term quorum; optional follower-local reads are labeled stale and never silently substitute for strong reads. ReadIndex, clock-based leader leases, external exactly-once side effects and arbitrary dynamic membership require further proofs and are outside the mandatory baseline. For snapshots, assess explicit last-included index/term, applied state and dedup retention; an educational service that does not implement installation must **cap and refuse new log growth** and clearly document that operational limitation.

**Reference environment and failure evidence:** Three nonprivileged Rust processes on **one learner-owned Linux host** with independent disposable storage directories, loopback ports, finite clients/queues/disk budgets and a deterministic fault scheduler. Separate process files establish crash/restart logic but **not independent hardware, clock, power or network-fault domains**. A reproducible small state-machine model and independent client-history checker complement executable tests. Simulated drop/duplicate/reorder/partition, injected persistence errors and process termination do not prove behavior under every asynchronous schedule, arbitrary storage corruption or real data-center power failure. No paid cloud, production deployment, root, public hosts, destructive partitions or proprietary prover is required.

**Completion and workload:** All **15 existing learning outcomes** and **6 existing assessment IDs** remain stable. AS1/AS2 establish failure, consistency and consensus reasoning; AS3 implements the durable fixed-member service; AS4 attacks it with independent deterministic histories; AS5 measures same-guarantee replication costs; AS6 evaluates unfamiliar fault transfer and defense. The **same implementation and fixtures are reused** across AS3–AS6, not reimplemented six times. A lesson may cover multiple teaching sessions and experiments; consolidating duplicate exercises does not reduce the required consensus safety, recovery, actual implementation or independent evidence. The **18–24 weeks** at **10–15 focused hours/week** (approximately 180–360 hours) are provisional workload estimates, not a completion rule; difficulty, tool setup, review and learner results must determine future calibration. Course status remains `draft` pending authentic learner/reviewer evidence.

## Learning outcomes

- **SYS6-O1:** Model asynchronous message delays, omission, duplication, process crash and network partitions and explain indistinguishable observations.
- **SYS6-O2:** Specify RPC identity, deadline, retry, deduplication and uncertain outcomes without promising exactly-once execution.
- **SYS6-O3:** Distinguish consistency, availability, durability and safety/liveness claims under explicit failure assumptions.
- **SYS6-O4:** Analyze linearizability, sequential consistency and eventual consistency through client histories and counterexamples.
- **SYS6-O5:** Explain quorum intersection, replication factor and acknowledgment policies with concrete failure budgets.
- **SYS6-O6:** Design leader epochs/terms, fencing and durable replicated-log constraints that prevent stale-leader acceptance.
- **SYS6-O7:** Derive the essential election, log-matching, commitment and state-machine safety properties of a leader-based consensus protocol.
- **SYS6-O8:** Implement a bounded replicated log or state-machine service with crash-recoverable term/log state and controlled deterministic scheduling.
- **SYS6-O9:** Specify read semantics, membership and configuration limitations, and distinguish stale, leader and quorum-based reads.
- **SYS6-O10:** Reason about snapshot, compaction and state transfer while preserving applied/committed boundaries.
- **SYS6-O11:** Design fault-injection tests for partition, delay, duplication, crash/restart, leader change and quorum loss.
- **SYS6-O12:** Use independent history checking or a reference state machine to evaluate claimed safety under generated schedules.
- **SYS6-O13:** Measure the latency/availability cost of replication under controlled local workloads and disclose extrapolation limits.
- **SYS6-O14:** Build and operate a small replicated key-value service or equivalent coordination component with honest guarantee documentation.
- **SYS6-O15:** Defend an unfamiliar distributed failure by identifying an invalid history, deriving root cause and testing a correction.

## Modules

### Module 1 — Distributed Execution, Failure Models and Impossibility Boundaries

#### Outcomes

- SYS6-O1
- SYS6-O3
- SYS6-O5

#### Lessons

1. **Distributed operation and honest shared-host evidence** — Move beyond SYS4 transport and SYS5 local WAL: trace client response, remote delivery, state-machine execution and durable replica state separately. Use three independently identified local processes only as a *logical* fault experiment—same Linux host, CPU, power, clock and storage do not establish independent physical failure domains.
2. **Asynchrony, delay ambiguity and local timers** — Construct a schedule with unbounded message delay, duplication, reordering or omission and show why timeout cannot distinguish a slow leader from a crashed leader. Use monotonic elapsed timers for retry/election *liveness*, never wall-clock timestamps or timeout alone as a safety/fencing authority.
3. **Crash-stop, crash-recovery and storage faults** — State which nodes may halt and recover, what stable storage survives and which volatile fields are reconstructed. Distinguish corruption, process termination and Byzantine behavior, which the reference protocol explicitly excludes.
4. **Reachability graphs and network partitions** — Draw a three-node connectivity graph for healthy, isolated leader and minority/majority partitions, tracking directional message links rather than treating partition as permanent node death.
5. **Safety, availability and conditional progress under partition** — Specify never-commit-conflicting-results as safety and eventual service only under restored majority connectivity and fairness as liveness. Compare a minority refusal with an unsafe available response using an explicit failure model; qualify CAP vocabulary rather than treating packet availability, linearizability and durability as one slogan.

### Module 2 — RPC Identity, Retries, Fencing and Durable Duplicate Handling

#### Outcomes

- SYS6-O2
- SYS6-O3
- SYS6-O14

#### Lessons

1. **Versioned and bounded RPC envelopes** — Define operation kind, protocol version, client/session ID, monotonic request sequence, payload length, term/leader hint and response status; reject malformed/oversized frames before scheduling or allocation.
2. **Retry attempts and unknown client outcomes** — Contrast lost request, lost reply after an applied effect, and delayed execution beyond deadline. Separate transport attempt count, definite success/refusal and **unknown** result: no-retry or repeated-RPC delivery alone implies neither exactly-once execution nor automatic rollback.
3. **Durable replicated operation identity and dedup effects** — Define session ID plus monotonic request sequence and command fingerprint, with a replayable *result*. Make dedup part of deterministic replicated applied state, persisting or snapshotting it across leader replacement; refuse reuse of the same identity with conflicting payload instead of silently executing another effect.
4. **Deterministic retention horizons and side-effect limits** — Bound session/dedup memory through replicated, deterministic expiration or an explicit generation/horizon protocol, preserving snapshot state and refusing stale retries outside supported retention. Distinguish scoped deduplicated key-value effects from nontransactional email, payments and other external side effects; ordinary wall-clock cache eviction is not a consensus-safe dedup rule.
5. **Client redirection and stale leader hints** — Represent not-leader, unknown-leader, overloaded and quorum-unavailable outcomes distinctly; treat a redirect as advice to retry with the same operation identity, not authority to execute twice.
6. **Retry backoff and admission limits** — Bound attempts, outstanding requests, message bytes and elapsed time; show how unbounded retries worsen a partition and how backoff/cancellation affects availability without altering the correctness rule.

*Formative diagnosis:* Predict the result of retrying an increment after its reply was lost, a leader change and replicated dedup recovery.

### Module 3 — Consistency Models, Client Histories and Quorum Mathematics

#### Outcomes

- SYS6-O3
- SYS6-O4
- SYS6-O5
- SYS6-O9
- SYS6-O12

#### Lessons

1. **Client intervals, linearizability and pending operations** — Record invocation, response, per-client order and pending/unknown outcomes, then hand-search legal sequential key-value histories respecting nonoverlapping real-time precedence. Exhibit a stale-read counterexample rather than trusting sorted node log timestamps or only comparing final maps.
2. **Sequential consistency versus eventual convergence** — Construct a per-client-order-preserving sequentially consistent history that violates real-time linearizability, and an eventually convergent replica execution that temporarily violates monotonic reads. State actual delivery and no-new-write assumptions instead of promising strong consistency from eventual convergence.
3. **Safety versus stale-read policy** — Distinguish follower-local stale read, leader-local read without a quorum check and a separately justified linearizable read. Require the public API to name which one is exposed.
4. **Majority intersection is necessary, not sufficient to commit** — Calculate majority thresholds/intersections for N=3,4,5 and distinguish independent voting replicas from duplicate RPC acknowledgments. Explain why a majority *holding* an old-term entry is not itself Raft commitment: matching log, durable acknowledgments and current-term commit restrictions must also hold before client success.
5. **Read from a committed log position** — Analyze the conservative reference strategy of appending a read barrier/no-op or read command in the **current leader term**, waiting for durable majority commitment and local apply before serving a claimed linearizable read; distinguish optimized ReadIndex/lease approaches requiring their own proofs.
6. **Independent history checking** — Write a tiny sequential key-value oracle and explore legal orders for bounded concurrent histories including pending operations; do not infer consistency solely by sorting response timestamps.

### Module 4 — Replica State, Fixed Membership and Leader Authority

#### Outcomes

- SYS6-O1
- SYS6-O5
- SYS6-O6
- SYS6-O7

#### Lessons

1. **Fixed configuration and fault budget** — Choose exactly three configured voting members for baseline, stable IDs and independent on-disk directories. Explain the one-node crash tolerance and why changing peers dynamically is outside this course.
2. **Follower, candidate and leader transitions** — Define the transition table for current term, known leader, vote, election timeout, heartbeat and step-down on a higher term; identify which observations are stale or unauthoritative.
3. **Persisted votes, election intersection and crash safety** — Trace term/votedFor persistence before an affirmative election response, then crash/restart during voting. Combine one-vote-per-term with overlapping majorities to rule out two leaders in one term, and independently expose a bug where an unsynced vote is forgotten.
4. **Up-to-date log voting rule** — Compare candidate versus voter lastLogTerm and then lastLogIndex; construct a trace where voting for a log with the wrong suffix would threaten an already committed entry.
5. **Stale leadership, fencing and asymmetric partitions** — Model an isolated old leader that can still serve local reads or receive obsolete replies, but cannot validate a current quorum. Require step-down on higher term, safe refusal of strong reads/writes without current authority and an explicit external fencing contract if a non-replicated service is contacted; a term label alone does not fence external effects.
6. **Heartbeat behavior and timer fairness** — Use randomized/deterministically seeded election timeouts and bounded heartbeats as liveness techniques, not as safety proofs or guaranteed fixed completion latency.

### Module 5 — Log Matching, Durable Replication and Safe Commitment

#### Outcomes

- SYS6-O5
- SYS6-O6
- SYS6-O7
- SYS6-O8

#### Lessons

1. **Log identity, matching-prefix append and checks** — Define index, term, command, integrity and snapshot-boundary metadata, then trace prevLogIndex/prevLogTerm matching and follower append/rejection. Reject responses that falsely claim success before the corresponding record is valid and durably stored.
2. **Conflict resolution and committed-prefix preservation** — Trace competing uncommitted suffixes and how a legitimate new leader repairs them; establish why a follower must not overwrite entries already known committed under a safe leader-election/log-matching protocol.
3. **Durable follower acknowledgment and real replication progress** — Count follower matchIndex only for safely persisted matching entries and update nextIndex on actual conflict/rejection. Derive retransmission after loss, duplicate response or disk failure, showing why multiple replies from one node never increase the voting-quorum count and why unsynced followers cannot establish durable write success.
4. **Current-term commit restriction** — Apply the Raft rule: a leader directly advances commitIndex by counting a majority only for an entry from its **current term**. An older-term entry becomes committed indirectly when a current-term entry at or beyond it commits; demonstrate the classic prior-term counterexample.
5. **Commit, ordered deterministic apply and reply authority** — Distinguish a majority-committed log index from lastApplied and a client-visible reply. Replay commands in the identical deterministic order on every node, including dedup effects and explicit errors; do not acknowledge a strong operation until the declared commit, application and durable-result requirements are satisfied.
6. **Replica replay and catch-up** — Use committed index, last applied index and leader-announced bounds to replay safely without applying an entry twice after restart; model slow follower catch-up without clearing already committed prefix.
7. **Safety invariants and negative histories** — Check election safety, log matching, leader completeness, monotonic commit/apply and state-machine safety with hand-derived adversarial traces rather than treating a green leader election as proof.

*Formative diagnosis:* Construct a five-server thought experiment where an old-term entry appears on a majority yet cannot be committed directly by a new leader until a current-term entry is committed.

### Module 6 — Persistent Term, Log, Vote and Crash-Recovery State

#### Outcomes

- SYS6-O6
- SYS6-O7
- SYS6-O8
- SYS6-O10

#### Lessons

1. **Replica hard state and crash-safe persistence boundaries** — Separate stable term/vote/log records from volatile role, election timer, nextIndex and matchIndex, while stating any durable commit/applied marker policy. Reuse SYS5's checksummed WAL/sync protocol to prevent sending votes, append acks or client success dependent on unpersisted state.
2. **Recover after term or vote write** — Inject a stop before sync, after successful sync and before reply; verify that restarted voters do not cast an incompatible second vote in the same persisted term.
3. **Recover a partial or corrupt log record** — Reject invalid interior records and apply an explicit conservative final-tail policy without silently truncating acknowledged entries; distinguish a node's local corruption from quorum-wide committed data loss.
4. **Restart, commit knowledge and exactly-once-within-scope apply** — Show that a restarted follower's log can include **uncommitted** entries and may only apply a safely known committed prefix. Reconstruct deterministic key-value and replicated dedup state to a declared lastApplied/commit boundary so a retried non-idempotent increment is not silently applied twice after recovery.
5. **Disk-full, sync failure and read-only safety** — Treat failed persistence as refusal or safe step-down; never count an unsynced append as quorum durability and avoid silently serving strong results after local irrecoverable storage errors.
6. **Independent hard-state fault oracles and record versions** — Hand-derive expected durable term, votedFor, log, commit/apply, version and response states for bounded crash/sync points, and reject incompatible persistence formats. Separate process-kill/injected errors from actual power-loss durability and identify a restart scenario where a corrupted schema must fail closed.

### Module 7 — Read Safety, Deduplication, Snapshots and State Transfer

#### Outcomes

- SYS6-O2
- SYS6-O9
- SYS6-O10
- SYS6-O14

#### Lessons

1. **Strong read barriers versus explicitly stale reads** — For **each strong read**, establish current-term leader authority with a fresh ordered read-command/barrier whose required entry is durably quorum-committed and locally applied before returning the result; otherwise refuse or report unknown under lost majority. A previously committed entry or merely identifying as leader is not a current quorum check. Label optional follower-local reads explicitly stale, with the observed applied index/term.
2. **Durable request identity across leadership** — Place client-session dedup results in deterministic applied replicated state and any supported snapshot; on a new leader, identical retries return the prior recorded result rather than apply an increment twice.
3. **Snapshot boundary and metadata** — Define lastIncludedIndex/lastIncludedTerm, application state and dedup/session state for an optional snapshot; distinguish a snapshot of *applied committed prefix* from copying a random incomplete memtable.
4. **Durable snapshot publication and log retention** — Under SYS5's file/manifest ordering, persist snapshot before compacting covered log entries; keep the boundary term and any remaining suffix required for follower replication and safe restart.
5. **Snapshot installation, stale-transfer rejection and atomic boundaries** — Model a lagging follower receiving a versioned bounded InstallSnapshot-like transfer with checksums, lastIncludedIndex/Term, applied key-value state and dedup horizon. Reject truncated/stale chunks and publish all-or-nothing durable installation under named SYS5 file/manifest assumptions; do not expose half-installed state or reapply earlier committed effects.
6. **Log growth without mandatory snapshot implementation** — Require an *executable bounded log limit and safe refusal* if snapshot installation is only modeled/analysed, and explicitly publish that limitation. Implementing production-grade compaction/state transfer is optional only if all SYS6-O10 reasoning and AS3/AS5 inspection criteria are still met.

### Module 8 — Three-Replica Integration and Deterministic Adversarial Schedules

#### Outcomes

- SYS6-O1
- SYS6-O7
- SYS6-O8
- SYS6-O11
- SYS6-O12
- SYS6-O14

#### Lessons

1. **One real bounded three-replica Rust service and resource ledger** — Run exactly three fixed-member local Rust processes with stable IDs, independent disposable paths and loopback ports. Reuse one source tree for all summatives, bounding queues, RPC bytes, client sessions, log/snapshot growth, disk, event count and test time; a deterministic model cannot replace the actually running three-process service.
2. **Fault-controlled transport adapter** — Expose message deliver, drop, delay, duplicate, reorder and asymmetric partition decisions through a deterministic seeded scheduler or proxy while preserving a separate mode that runs real local processes.
3. **Minority refusal, stale leader and conflicting suffix schedules** — Inject a 2+1 partition, leader isolation, old-term AppendEntries, delayed acknowledgments and conflicting uncommitted suffixes. Independently predict durable vote/log/commit states and refuse minority strong success; verify no two different commands can become committed at one index under declared fault assumptions.
4. **Lost reply, retry and dedup replay** — Commit an increment, suppress its reply, change leaders and retry with the same client-session sequence; verify one logical effect and explicitly unknown client outcome before a successful later response.
5. **Crash recovery at durable cut points** — Stop and restart voters/leaders after term/vote sync, log append, follower sync, commit/apply and reply boundaries, comparing recovered state with independent expected or allowed histories.
6. **Partition recovery, counterexample shrinking and proof limits** — Restore an asymmetric link or lost leader and inspect leader-correct catch-up and committed-prefix convergence under conditional fairness. Shrink a failing deterministic seed to a minimal state/event trace and label shared-host/proxy scheduling assumptions; finite successful seeds do not prove all asynchronous executions.
7. **Independent history and state checker** — Compare observed client-operation intervals with a separately implemented sequential map plus dedup semantics and a bounded linearizability search; inspect log/term invariants in addition to final key-value equality.

### Module 9 — Replication Cost, Availability Limits and Operational Evidence

#### Outcomes

- SYS6-O3
- SYS6-O9
- SYS6-O10
- SYS6-O13
- SYS6-O14

#### Lessons

1. **Cost of a durable majority commit** — Break response time into client transport, leader queue, local/follower sync, quorum receipt, apply and response. Show which components may overlap and which gate durable success.
2. **Comparable healthy, degraded and unavailable workloads** — Run identical acknowledged-durability command streams in a healthy three-member cluster, one slowed follower with majority intact and a no-majority partition. Count offered/admitted/committed/applied, duplicate, unknown and refused operations separately so lost-quorum unavailability is not concealed by successful-only denominators.
3. **Read and write asymmetry** — Compare safe log-barrier strong reads against clearly labeled stale reads using consistent client conditions, explaining the safety cost and which lease/ReadIndex optimizations are not implemented.
4. **Replication factor and quorum arithmetic** — Reason with a three-node baseline and bounded thought models for N=5, tracking majority, failure budget, replication overhead and why independent physical failures cannot be demonstrated by loopback nodes.
5. **Repeated measurement, shared-host confounders and honest claims** — Retain at least five raw trial values per comparable configuration with center/spread, units, sample counts, CPU/disk/toolchain/OS and shared-host interference. Distinguish model-proven safety, observed process-level service and untested independent-power or cross-region availability; never derive an SLA from one laptop.
6. **Failure operations and safe recovery runbook** — Document leader/no-quorum responses, node restart, log inspection, disk-full quarantine, partition healing and fixture cleanup with commands that cannot touch a live external service.

*Formative diagnosis:* Interpret one graph with a surviving two-node majority and a slower follower: distinguish quorum-gated latency from a mislabeled '99.99% availability' claim.

### Module 10 — Integrated Replicated Service and Unfamiliar Failure Defense

#### Outcomes

- SYS6-O6
- SYS6-O7
- SYS6-O8
- SYS6-O9
- SYS6-O10
- SYS6-O11
- SYS6-O12
- SYS6-O13
- SYS6-O14
- SYS6-O15

#### Lessons

1. **One guarantee matrix and reproducible three-node handoff** — Publish fixed-member non-Byzantine crash-recovery scope, durable term/log state, majority-write rule, per-read quorum barrier, dedup/session retention and optional snapshot/install omissions. Provide exact Rust/Cargo/lockfile commands, three independent storage paths, bounded fixture inputs and safe cleanup for the **same AS3 implementation**, not another cluster.
2. **Reuse election, log, replay and client-ambiguity proofs** — Demonstrate from existing AS2/AS3/AS4 evidence persisted votes, up-to-date-log voting, current-term majority commit, matching-prefix repair and deterministic apply. Recheck one lost-response-after-commit/restart/retry sequence using replicated dedup and an independently expected client result rather than reconstructing a second consensus implementation.
3. **Safe reads, snapshot bounds, quorum loss and resource failure** — Check the per-read current-authority barrier or explicit refusal, then source/model-reason snapshot lastIncludedIndex/Term, dedup retention, follower catch-up or the safe refusal/log-cap alternative. Reuse actual partition, crash, malformed-RPC and persistence-error fixtures with finite resource ceilings.
4. **Publish benchmark and limitation record** — Supply raw steady/degraded trials, accepted/committed/unknown counts, safe redacted traces, model-search bounds and the limitations of sharing one kernel, physical disk and local network.
5. **Unknown-case diagnosis, minimal correction and independent defense** — For a genuinely unseen stale-term, overcommit, unsafe read, duplicate operation or snapshot mismatch, predict two rival causes and a discriminating term/log/client timeline. Make a minimal evidence-backed correction or conservative refusal, verify independent negative and previously valid regression, and defend omitted production guarantees without claiming formal Raft verification.

## Completion requirements

**Six summative assessments cover SYS6-O1–SYS6-O15.** Each assessment has its own public Work/Criteria/Evidence, and all outcomes must be demonstrated against actual mechanisms, not only linked by an ID. AS6 evaluates the distinct unseen-failure transfer outcome **SYS6-O15**; AS1–AS5 retain all other mandatory competencies. Module feedback, supplementary reading and optional protocol extensions do not create hidden completion gates. AS3–AS6 evaluate separate aspects of **one cumulative fixed-membership codebase**: durable replication, adversarial safety verification, constrained measurement and an independent unfamiliar failure. No unrelated new three-node cluster is required for each evaluation.

- **SYS6-AS1** — Distributed Failure, Consistency and Client-Outcome Histories
  - **Outcomes:** SYS6-O1, SYS6-O2, SYS6-O3, SYS6-O4, SYS6-O5.
  - **Work:** Specify a three-replica failure model and a bounded RPC grammar. Analyze **at least five distinct independently supplied or hand-derived histories**: (a) lost response after operation effect, (b) minority partition, (c) a linearizable versus sequentially consistent read/write ordering, (d) duplicate retry with operation identity, and (e) majority/quorum failure with delayed or unacknowledged persistence. Calculate majority intersection for a declared three-node configuration plus one four- or five-node thought case.
  - **Criteria:** Each history identifies named clients/replicas, invocation and response intervals, logical message/term events, state/failure assumptions and accepted/unknown/refused result. Linearizability and sequential consistency are assessed by a real-time/allowed-order argument, not log timestamp sort; a timeout is not mistaken for node death or rollback, and a local-only majority is not assumed to commit unsafe prior-term log entries. The learner distinguishes transport attempt semantics, durable application effect, client visibility, conditional liveness and partition availability without invoking exactly-once RPC magic.
  - **Evidence:** Public fault model, versioned bounded request/response protocol, five independent event histories and expected outcomes, quorum calculations, consistency counterexamples and a defensible assumptions/limitations table.

- **SYS6-AS2** — Fixed-Membership Election, Log and Read Safety Proof Obligations
  - **Outcomes:** SYS6-O5, SYS6-O6, SYS6-O7, SYS6-O9.
  - **Work:** Derive and defend **at least six** small adversarial state traces that cover persistent term/vote before response, last-log-term/index election eligibility, conflicting AppendEntries suffixes, current-term-only direct majority commit, stale isolated leaders, and **per-read** strong authority (a freshly committed current-term log barrier/read command or an independently justified equivalent). Include one prior-term entry present on a majority but not yet safely committed, and a leader that previously committed an entry but **subsequently lost quorum before a new strong read**.
  - **Criteria:** Election safety, leader completeness, log matching, committed-prefix preservation, durable follower acknowledgment, monotonically valid commit/apply and fixed-member majority intersection follow from explicit transitions and relevant Raft safety restrictions. An old-term entry on a majority is not automatically directly committed. A stale leader without **current quorum authority** cannot serve a linearizable read or acknowledge strong writes, and a **previously committed** no-op is not by itself proof of authority for a **later** read. Lease/ReadIndex optimizations require their additional proof obligations; voting and conflict rules exclude the actual counterexample instead of hiding it behind a happy path.
  - **Evidence:** Six independent term/index/log/vote and read event traces, persistent-state transition table, hand-derived majority/commit calculations, safety invariant/counterexample explanations, declared omissions and versioned reference model.

- **SYS6-AS3** — Durable Three-Replica Rust State Machine
  - **Outcomes:** SYS6-O2, SYS6-O6, SYS6-O7, SYS6-O8, SYS6-O10, SYS6-O14.
  - **Work:** Implement one locally reproducible **three-process, fixed-member Rust key-value service** with separate persistent replica directories, bounded RPC queues and message sizes, leader election, log append/matching/retry, quorum-based **current-term** commit, ordered apply, client-session request deduplication and safe strong read or explicit refusal. Persist term/vote/log before protocol responses that depend on them and reuse SYS5's crash-safe record approach. Publish and analyze a bounded snapshot/lagging-follower state-transfer example (lastIncludedIndex/Term, applied index, durable dedup state), implementing snapshot install optionally; if omitted, enforce a finite log cap and explicit unavailable/refusal behavior.
  - **Criteria:** Known fixed members have unique stable identities and bounded resources; majority durable replication precedes durable-acknowledged write success, and the current-term commit restriction prevents unsafe prior-term commitment. Follower conflict handling, persistent votes and recovery cannot knowingly discard a committed acknowledged prefix under the declared crash model; state-machine apply is ordered and deterministic. Duplicate same-session request IDs return the prior replicated applied result without rerunning a non-idempotent effect within the documented retention horizon, while mismatched payload IDs and expired sessions are rejected. Retention expiry is an explicit deterministic replicated-state transition or versioned session-generation protocol, **not a leader-local wall-clock cache eviction**, and any snapshot must carry the needed dedup/result state. **Each strong read** must be ordered by a fresh current-term read-command/barrier, durably committed through a valid majority and applied locally before reply (or independently justify an equivalent current-authority proof). Merely having been leader or having committed an earlier entry cannot authorize later reads after quorum loss; loss of quorum causes refusal or unknown rather than fabricated success. Snapshots/state transfer are source/model analyzed even if optional in the executable. If installation is absent, the service must enforce a finite log cap and **safely refuse writes or a catch-up it cannot perform**, never compact away a prefix that a supported follower still needs and then claim it will inevitably recover. **No claim of formally verified production consensus follows merely from passing tests.**
  - **Evidence:** Compilable source, Cargo manifest/lockfile and declared toolchain, three-replica startup fixture, protocol/term/log/dedup models and numeric limits, persistent file/rollback tests, independent normal/retry/read/restart traces, snapshot-boundary reasoning and clean-run guarantees/omissions.

- **SYS6-AS4** — Controlled Partitions, Crash-Recovery and Independent History Checking
  - **Outcomes:** SYS6-O1, SYS6-O3, SYS6-O8, SYS6-O11, SYS6-O12.
  - **Work:** Use a documented **seeded deterministic delivery/fault scheduler** (or precise reproducible equivalent) with delayed, duplicated, dropped, reordered and asymmetric-partition messages and bounded crash/restart points. Run at least **six distinct fault families** including 2+1 split, leader isolation/change, lost reply and duplicate increment, stale-term append, voter/log persistence failure, and follower catch-up or a snapshot-boundary model. Compare client intervals and log/commit metadata to an independently implemented sequential map/history checker with published assumptions.
  - **Criteria:** In tested histories, no conflicting entries are deemed committed at the same index, no minority acknowledges a strong write, no stale leader returns an unvalidated strong read, and no acknowledged durable committed state disappears after supported restarts. Independent client-history matching permits pending/unknown outcomes without accepting a proven invalid read-after-write order or duplicated dedup effect; show at least one intentionally faulty fixture that the checker correctly rejects. Logs include actual stable IDs/terms/indexes and observed versus simulated provenance. Bound queue sizes, state exploration depth, disk writes and test duration, and disclose why finite seeds are not an exhaustive safety proof.
  - **Evidence:** Scheduler/proxy and checker source, seeds/configuration, per-replica state logs and independent expected histories, positive/negative counterexamples, bounded fault table, crash/reopen results and explicit modeling/test-coverage limits.

- **SYS6-AS5** — Replication Cost, Degraded Operation and Honest Availability Study
  - **Outcomes:** SYS6-O3, SYS6-O9, SYS6-O10, SYS6-O13.
  - **Work:** Measure the **same AS3 service** under (a) steady healthy three-node load, (b) one intentionally slowed follower with a majority intact and (c) loss of majority with refusal/unknown outcomes; compare strong-read versus deliberately labeled stale-read policy only if both are implemented and traceably distinct. Analyze log/disk-sync/quorum/apply overhead, snapshot-related growth or explicit log-cap behavior, and a safe local recovery runbook.
  - **Criteria:** Every compared healthy/degraded configuration uses the same documented protocol/durability semantics and independently checked useful-work results; do not label disabled sync, stale reads or dropped errors as a same-guarantee speedup. Report offered/admitted/committed/applied/unknown/rejected work, payload and queue limits, and **at least five raw repeated timing observations per meaningfully compared configuration** with units, center/spread, sample count and observed confounders. Explain lack of quorum progress without incorrectly asserting liveness under partition; report shared-host CPU/storage/network caveats and avoid extrapolating availability SLAs or cross-region latency.
  - **Evidence:** Reproducible workload/chaos scripts, exact node configurations and hardware/OS/runtime details, independent correctness results, raw trial data and summary calculations, per-stage timing/lag observations, safe restart/quorum-loss runbook and claims/assumptions/limitations.

- **SYS6-AS6** — Unfamiliar Distributed Failure and Recovery Defense
  - **Outcomes:** SYS6-O15.
  - **Work:** Diagnose **one previously unseen**, bounded reviewer-provided or transparently generated distributed failure, such as a second persisted-term vote after crash, direct old-term overcommit, outdated strong-read authority, stale-term suffix overwrite, lost replicated dedup result, invalid snapshot installation or conflicting duplicate ID. **Before running the case**, propose two rival causes, predict independently expected client/term/log/commit/apply states and identify a discriminating observation. Make a minimal justified code/model correction or safe refusal and rerun a negative plus previously correct history. This evaluates **SYS6-O15 unfamiliar distributed failure diagnosis/defense**, not an automatic reassessment of all different consensus, history, fault-harness and engineering competencies previously evaluated by AS1–AS5.
  - **Criteria:** The learner identifies the earliest violated election/log/commit/read/application invariant in a legal asynchronous history and distinguishes ambiguous client completion from acknowledged data loss or demonstrably invalid consistency. At least one observation genuinely differentiates plausible causes, and the minimal correction or technically bounded refusal respects current-term quorum, durable response, read barrier, deterministic dedup and relevant snapshot boundaries. Independently predicted new-case and previously correct regressions show what changed; model-versus-actual-process provenance and untested schedules/hardware assumptions remain explicit. One optional-kind unfamiliar case **does not award SYS6-O4/O6/O7/O11/O12/O14 anew**: these remain independently required under AS1–AS5.
  - **Evidence:** Original unseen challenge/seed, predictions and competing hypotheses, annotated event and state timelines, independent sequential/history oracle, source patch or bounded refusal rationale, before/after and neighboring-case regressions, a written/recorded/live technical defense and residual limitations.

### Academic scope, safe practice and independence

[SYS4](SYS4.md) owns connection-level framing, nonblocking multi-client service, transport failure and network backpressure; [SYS5](SYS5.md) owns local WAL durability, manifest/snapshot publication and file fault injection; [SYS3](SYS3.md) owns user-space concurrency invariants and concurrent history analysis. SYS6 uniquely owns distributed failure ambiguity, operation identity across nodes, quorum intersection, term/vote/log safety, strong read semantics, deterministic fault schedules and replicated state-machine recovery. [SYS7](SYS7.md) will develop deeper production-performance causality; [SYS8](SYS8.md) owns operational reliability/capacity/deployment trade-offs, not a second consensus implementation. Full production Raft membership change, Byzantine-tolerant protocols, multi-region deployment, cryptographically authenticated cluster traffic, unbounded log compaction and universally linearizable lease reads remain outside this reference course unless independently implemented, specified and verified.

Every assessed experiment uses bounded local synthetic clients, controlled process termination, independent fixture directories and nonprivileged loopback sockets, never destructive host network rules, public deployments, real production data or paid infrastructure. Code-only or offline model alternatives can aid understanding, but SYS6-O8/O14 and AS3 require **an actually running three-process educational replica service**. Learners may submit equivalent accessible state tables, event timelines, source excerpts and written rather than live defenses while meeting the identical correctness/evidence rules.

### Assessment records and readiness

Records identify the source revision, replica and filesystem assumptions, evaluated outcomes, independently expected term/log and client histories, actual results and reviewer. Local three-process tests do not establish independent-host failure tolerance. The course remains `draft` until learner testing and qualified review support a status change.

## Optional disciplinary references

All are public independent-study sources rather than compulsory paid materials, hidden tests or assertions of accreditation.

- [Ongaro and Ousterhout — Raft extended paper](https://pdos.csail.mit.edu/6.824/papers/raft-extended.pdf) — core terms, persistent votes/log, leader completeness, majority/current-term commitment, membership and snapshots.
- [MIT 6.5840 Distributed Systems](https://pdos.csail.mit.edu/6.5840/) — public distributed-failure reasoning, historical clients and fault-controlled testing.
- [Raft project](https://raft.github.io/) — consensus visualizations and linked primary material.
- [Jepsen — consistency models](https://jepsen.io/consistency) — client histories, read/write outcomes and model distinctions.
- [TLA+](https://lamport.azurewebsites.net/tla/tla.html) — an optional formal exploration tool, not a mandatory hidden prerequisite or substitute for required implemented evidence.
