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

**Completion and workload:** All **15 existing learning outcomes** and **6 existing assessment IDs** remain stable. AS1/AS2 establish failure, consistency and consensus reasoning; AS3 implements the durable fixed-member service; AS4 attacks it with independent deterministic histories; AS5 measures same-guarantee replication costs; AS6 evaluates unfamiliar fault transfer and defense. The **same implementation and fixtures are reused** across AS3–AS6, not reimplemented six times. The **18–24 weeks** at **10–15 focused hours/week** (approximately 180–360 hours) are provisional workload estimates, not a completion rule; difficulty, tool setup, review and learner results must determine future calibration. Course status remains `draft` pending authentic learner/reviewer evidence.

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

1. **A distributed operation is not a local call** — Contrast SYS4's connection-level transport and SYS5's local durable commit with communication between independent state machines. Trace where client completion, network delivery, remote execution and local persistence can each diverge.
2. **Asynchronous execution and partial knowledge** — Specify finite but arbitrarily delayed messages, reordering, duplication and omission; illustrate why local observations cannot distinguish delay from process failure during an unbounded asynchronous interval.
3. **Crash-stop, crash-recovery and storage faults** — State which nodes may halt and recover, what stable storage survives and which volatile fields are reconstructed. Distinguish corruption, process termination and Byzantine behavior, which the reference protocol explicitly excludes.
4. **Reachability graphs and network partitions** — Draw a three-node connectivity graph for healthy, isolated leader and minority/majority partitions, tracking directional message links rather than treating partition as permanent node death.
5. **Timers, local monotonic time and clock skew** — Use elapsed-time scheduling to initiate retries/elections while distinguishing timeout-driven *liveness decisions* from evidence of true leader failure; forbid wall-clock timestamps as the sole safety or term authority.
6. **Safety and liveness in adverse schedules** — Define never-acknowledge-conflicting-state as safety and eventual completion under restored communication and scheduling fairness as conditional liveness. Give a partition trace in which the service must remain unavailable to preserve safety.
7. **CAP language with declared model** — Explain the trade-off in a partitioned setting without reducing all designs to a slogan; separate client operation availability, consistency model, failure assumptions and durability from per-link packet behavior.
8. **Three local processes are not three machines** — Publish limits of loopback experiments: shared CPU, power, kernel, clock, filesystem and fault domain. Specify which results come from deterministic logical links versus actual separate OS processes.

### Module 2 — RPC Identity, Retries, Fencing and Durable Duplicate Handling

#### Outcomes

- SYS6-O2
- SYS6-O3
- SYS6-O14

#### Lessons

1. **Versioned and bounded RPC envelopes** — Define operation kind, protocol version, client/session ID, monotonic request sequence, payload length, term/leader hint and response status; reject malformed/oversized frames before scheduling or allocation.
2. **Three distinct timeout outcomes** — Trace no response caused by request loss, response loss after a durable effect and delayed execution beyond client deadline. Express success, explicit rejection and unknown result separately rather than inventing a rollback.
3. **At-most-once versus at-least-once attempts** — Compare retry/no-retry behavior at the RPC transport layer and explain why neither alone yields exactly-once application effects across crash/restart.
4. **Stable operation identity and mismatched replays** — Design a dedup key of client session plus sequence, with operation fingerprint and stored response. Reject reuse of one ID with different payload rather than silently accepting a conflicting replay.
5. **Dedup is replicated state, not a cache trick** — Apply the dedup table as part of the deterministic replicated state machine and preserve it across restart and supported snapshot boundaries; an in-memory-only leader cache is insufficient after failover.
6. **Retention windows and expired sessions** — Define bounded dedup state, session expiry or explicit compaction horizon. State that a retry outside that horizon is refused or has weakened guarantees, not silently counted as known duplicate-free work.
7. **Client redirection and stale leader hints** — Represent not-leader, unknown-leader, overloaded and quorum-unavailable outcomes distinctly; treat a redirect as advice to retry with the same operation identity, not authority to execute twice.
8. **Retry backoff and admission limits** — Bound attempts, outstanding requests, message bytes and elapsed time; show how unbounded retries worsen a partition and how backoff/cancellation affects availability without altering the correctness rule.
9. **External side effects and exactly-once boundaries** — Restrict assessed operations to the replicated key-value state machine; distinguish its deduplicated effect within a retained session from an arbitrary email, payment or nontransactional external action.

*Formative diagnosis:* Predict the result of retrying an increment after its reply was lost, a leader change and replicated dedup recovery.

### Module 3 — Consistency Models, Client Histories and Quorum Mathematics

#### Outcomes

- SYS6-O3
- SYS6-O4
- SYS6-O5
- SYS6-O9
- SYS6-O12

#### Lessons

1. **Operation histories and real-time precedence** — Record invocation/response intervals, client order, pending outcomes, term and node metadata. Identify which operations are definitely complete and which may have executed despite missing responses.
2. **Linearizability under a sequential specification** — Try to place each completed operation at a single legal point between invocation and response, preserving nonoverlapping real-time order; provide a small counterexample with a stale read.
3. **Sequential consistency without real-time order** — Classify a history that permits one total operation sequence preserving each client's program order but violates linearizability's cross-client real-time precedence.
4. **Eventual convergence and what it excludes** — Define convergence under eventual message delivery and no new writes, then show why it does not ensure immediate read-after-write, read monotonicity or strong operation ordering.
5. **Safety versus stale-read policy** — Distinguish follower-local stale read, leader-local read without a quorum check and a separately justified linearizable read. Require the public API to name which one is exposed.
6. **Majority intersection arithmetic** — Compute q=floor(N/2)+1 and overlapping majorities for N=3,4,5, and why a minority cannot choose a new leader or safely acknowledge a strong write.
7. **A majority is not automatically a transaction commit** — Differentiate a majority response, *durably stored* matching log entries, current-term commit constraints, applied state and a successful client reply. Explain why raw quorum arithmetic alone does not establish linearizability.
8. **Read from a committed log position** — Analyze the conservative reference strategy of appending a read barrier/no-op or read command in the **current leader term**, waiting for durable majority commitment and local apply before serving a claimed linearizable read; distinguish optimized ReadIndex/lease approaches requiring their own proofs.
9. **Independent history checking** — Write a tiny sequential key-value oracle and explore legal orders for bounded concurrent histories including pending operations; do not infer consistency solely by sorting response timestamps.

### Module 4 — Replica State, Fixed Membership and Leader Authority

#### Outcomes

- SYS6-O1
- SYS6-O5
- SYS6-O6
- SYS6-O7

#### Lessons

1. **Fixed configuration and fault budget** — Choose exactly three configured voting members for baseline, stable IDs and independent on-disk directories. Explain the one-node crash tolerance and why changing peers dynamically is outside this course.
2. **Follower, candidate and leader transitions** — Define the transition table for current term, known leader, vote, election timeout, heartbeat and step-down on a higher term; identify which observations are stale or unauthoritative.
3. **Persist term and vote before responding** — On receiving a higher term or granting a vote, write the durable term/votedFor state before sending an affirmative election/replication response that relies on it; model a crash that otherwise enables two votes in one term.
4. **Election quorum and uniqueness** — Derive one-vote-per-term plus majority intersection for election safety. Show why concurrent candidates may produce no leader even though the invariant is preserved.
5. **Up-to-date log voting rule** — Compare candidate versus voter lastLogTerm and then lastLogIndex; construct a trace where voting for a log with the wrong suffix would threaten an already committed entry.
6. **Fencing and stale leadership** — Require old leaders to step down on higher observed terms and forbid stale writes/strong reads after they cannot establish current authority. Explain why a term field alone cannot fence an *external* service without that service enforcing it.
7. **Heartbeat behavior and timer fairness** — Use randomized/deterministically seeded election timeouts and bounded heartbeats as liveness techniques, not as safety proofs or guaranteed fixed completion latency.
8. **Leader changes under asymmetric links** — Model a split where one old leader continues answering local probes but cannot reach a majority; state what it can report (unavailable, redirect, or declared stale read) and must not acknowledge.

### Module 5 — Log Matching, Durable Replication and Safe Commitment

#### Outcomes

- SYS6-O5
- SYS6-O6
- SYS6-O7
- SYS6-O8

#### Lessons

1. **Replicated entry identities and log positions** — Define entry index, term, command and checksum with a zero/snapshot boundary sentinel. Distinguish an entry being present on one server from the index being committed.
2. **AppendEntries precondition and follower responses** — Check prevLogIndex/prevLogTerm against follower history, accept only a matching prefix, and report conflict without claiming a successful append when writes or sync fail.
3. **Conflict resolution and committed-prefix preservation** — Trace competing uncommitted suffixes and how a legitimate new leader repairs them; establish why a follower must not overwrite entries already known committed under a safe leader-election/log-matching protocol.
4. **Durable follower acknowledgments** — Apply SYS5's WAL/file-sync model to term/vote/log records; a follower may be counted in a durability-based quorum only after its matching required state is durably persisted under declared assumptions.
5. **Leader nextIndex and matchIndex bookkeeping** — Model per-follower progress and retransmission after rejection/loss, track matchIndex of actually stored entries, and prevent duplicate RPCs from pretending to be multiple independent voters.
6. **Current-term commit restriction** — Apply the Raft rule: a leader directly advances commitIndex by counting a majority only for an entry from its **current term**. An older-term entry becomes committed indirectly when a current-term entry at or beyond it commits; demonstrate the classic prior-term counterexample.
7. **Committed versus applied state** — Distinguish durable majority commitment from local state-machine application and client acknowledgment; never reply success for a command before the declared committed-and-applied point.
8. **Deterministic state-machine execution** — Require identical input commands/versions to produce the same results at each index, without local wall-clock decisions, random client effects or nondeterministic map traversal changing visible state.
9. **Replica replay and catch-up** — Use committed index, last applied index and leader-announced bounds to replay safely without applying an entry twice after restart; model slow follower catch-up without clearing already committed prefix.
10. **Safety invariants and negative histories** — Check election safety, log matching, leader completeness, monotonic commit/apply and state-machine safety with hand-derived adversarial traces rather than treating a green leader election as proof.

*Formative diagnosis:* Construct a five-server thought experiment where an old-term entry appears on a majority yet cannot be committed directly by a new leader until a current-term entry is committed.

### Module 6 — Persistent Term, Log, Vote and Crash-Recovery State

#### Outcomes

- SYS6-O6
- SYS6-O7
- SYS6-O8
- SYS6-O10

#### Lessons

1. **Persisted and reconstructed replica fields** — Separate hard state (term/vote/log) from reconstructible or bounded volatile state (role, nextIndex, matchIndex, timer and often commit/applied after recovery). Specify any implementation-specific durable commit markers explicitly.
2. **Crash-safe hard-state update** — Reuse SYS5's checked WAL and sync/atomic-replacement protocol for term/vote/log; define the write ordering and error handling that prevents election or append responses from promising unsaved state.
3. **Recover after term or vote write** — Inject a stop before sync, after successful sync and before reply; verify that restarted voters do not cast an incompatible second vote in the same persisted term.
4. **Recover a partial or corrupt log record** — Reject invalid interior records and apply an explicit conservative final-tail policy without silently truncating acknowledged entries; distinguish a node's local corruption from quorum-wide committed data loss.
5. **Restart before commit knowledge** — Show why a restarted follower's persisted log may include uncommitted entries and why only a valid leader commit announcement or equivalent safe persisted bound authorizes application.
6. **Durable application and idempotent replay** — Rebuild key-value and dedup state by applying only committed entries in log order with a recorded or safely reconstructed lastApplied boundary. Explain why applying a non-idempotent increment twice corrupts results.
7. **Disk-full, sync failure and read-only safety** — Treat failed persistence as refusal or safe step-down; never count an unsynced append as quorum durability and avoid silently serving strong results after local irrecoverable storage errors.
8. **Independent persistent-file fixtures** — Derive expected term/vote/log/commit/application state for a fixed sequence of failures using a separate oracle; keep real restart logs distinct from simulated device-power behavior.
9. **Versioned restart and migration boundaries** — Reject incompatible record/schema versions or perform explicitly defined upgrade only; do not let a software-version mismatch silently reinterpret a persisted term, sequence or command.

### Module 7 — Read Safety, Deduplication, Snapshots and State Transfer

#### Outcomes

- SYS6-O2
- SYS6-O9
- SYS6-O10
- SYS6-O14

#### Lessons

1. **Conservative linearizable read mechanism** — Use the reference service's *committed log barrier/read command* approach: after current-term authority is established, commit in quorum order, apply through its index and then return the read result; no unfenced leader-local 'strong' read.
2. **Stale reads as an explicit alternative** — Allow an explicitly named follower-local or possibly stale read endpoint with visible lastApplied/term metadata; never label it linearizable or silently substitute stale data when quorum disappears.
3. **Durable request identity across leadership** — Place client-session dedup results in deterministic applied replicated state and any supported snapshot; on a new leader, identical retries return the prior recorded result rather than apply an increment twice.
4. **Snapshot boundary and metadata** — Define lastIncludedIndex/lastIncludedTerm, application state and dedup/session state for an optional snapshot; distinguish a snapshot of *applied committed prefix* from copying a random incomplete memtable.
5. **Durable snapshot publication and log retention** — Under SYS5's file/manifest ordering, persist snapshot before compacting covered log entries; keep the boundary term and any remaining suffix required for follower replication and safe restart.
6. **Installing snapshots on lagging followers** — Model an InstallSnapshot-style state transfer to a follower missing a compacted prefix, including version, chunk bounds, checksum and final atomic installation of application/dedup state and index/term.
7. **Stale snapshot and partial-transfer rejection** — Reject a snapshot older than already installed/applied state, a truncated transfer or mismatched boundary; ensure interrupted copy cannot expose half-installed state or cause later duplicate application.
8. **Log growth without mandatory snapshot implementation** — Require an *executable bounded log limit and safe refusal* if snapshot installation is only modeled/analysed, and explicitly publish that limitation. Implementing production-grade compaction/state transfer is optional only if all SYS6-O10 reasoning and AS3/AS5 inspection criteria are still met.

### Module 8 — Three-Replica Integration and Deterministic Adversarial Schedules

#### Outcomes

- SYS6-O1
- SYS6-O7
- SYS6-O8
- SYS6-O11
- SYS6-O12
- SYS6-O14

#### Lessons

1. **One cumulative executable component** — Implement the baseline fixed-membership three-process Rust service with owned loopback ports and separate fixture directories; reuse this one source tree for election, log, recovery, performance and unknown-case defense.
2. **Fault-controlled transport adapter** — Expose message deliver, drop, delay, duplicate, reorder and asymmetric partition decisions through a deterministic seeded scheduler or proxy while preserving a separate mode that runs real local processes.
3. **Quorum loss and leader isolation** — Split the nodes into 2+1, then isolate or crash the leader. Verify only a component with a safe quorum may make a write/strong-read commitment, and reject any minority success claim.
4. **Old leader and conflicting suffix test** — Inject a stale term, obsolete leadership, delayed AppendEntries and conflict-resolution sequence; independently check no two distinct commands become committed at one index.
5. **Lost reply, retry and dedup replay** — Commit an increment, suppress its reply, change leaders and retry with the same client-session sequence; verify one logical effect and explicitly unknown client outcome before a successful later response.
6. **Crash recovery at durable cut points** — Stop and restart voters/leaders after term/vote sync, log append, follower sync, commit/apply and reply boundaries, comparing recovered state with independent expected or allowed histories.
7. **Partition healing and follower catch-up** — Restore links, remove duplicate/reordered messages and verify committed-prefix convergence and safe eventual progress *when* majority communication and fairness return.
8. **Independent history and state checker** — Compare observed client-operation intervals with a separately implemented sequential map plus dedup semantics and a bounded linearizability search; inspect log/term invariants in addition to final key-value equality.
9. **Counterexample shrinking and limits** — Reduce an observed failing seed to a minimal event trace, retain it as regression and disclose bounded search depth, assumptions, untested asynchronous schedules and shared-host artifact limitations.
10. **Capacity and resource guards** — Set numeric limits on clients, outstanding messages, payloads, pending RPCs, node count, term/log sizes, disk use and fault-test duration so adverse partitions cannot exhaust one learner's computer.

### Module 9 — Replication Cost, Availability Limits and Operational Evidence

#### Outcomes

- SYS6-O3
- SYS6-O9
- SYS6-O10
- SYS6-O13
- SYS6-O14

#### Lessons

1. **Cost of a durable majority commit** — Break response time into client transport, leader queue, local/follower sync, quorum receipt, apply and response. Show which components may overlap and which gate durable success.
2. **Three distinct workload regimes** — Measure steady one-leader operation, one slow follower while majority remains and quorum-unavailable/partition conditions. Keep the same command stream and explicit durability/consistency mode for comparable claims.
3. **Offered, admitted and completed requests** — Count attempted operations, accepted RPCs, committed commands, applied effects, duplicate retries, timeouts and unknown results separately; avoid hiding minority failures in a successful-service denominator.
4. **Read and write asymmetry** — Compare safe log-barrier strong reads against clearly labeled stale reads using consistent client conditions, explaining the safety cost and which lease/ReadIndex optimizations are not implemented.
5. **Replication factor and quorum arithmetic** — Reason with a three-node baseline and bounded thought models for N=5, tracking majority, failure budget, replication overhead and why independent physical failures cannot be demonstrated by loopback nodes.
6. **Controlled timing and uncertainty** — Collect at least five individual repeated trial results per chosen meaningful configuration, record p50 or comparable central estimates, dispersion, sample count and environmental confounders; disclose unsupported tail-latency precision.
7. **Failure operations and safe recovery runbook** — Document leader/no-quorum responses, node restart, log inspection, disk-full quarantine, partition healing and fixture cleanup with commands that cannot touch a live external service.
8. **No production SLA from one workstation** — Contrast model-based safety, tested local availability and real geographically distributed resilience; avoid claiming cross-region fault tolerance, linearizable stale reads or guaranteed time-to-recovery from shared-host experiments.

*Formative diagnosis:* Interpret one graph with a surviving two-node majority and a slower follower: distinguish quorum-gated latency from a mislabeled '99.99% availability' claim.

### Module 10 — Integrated Replicated Service and Unfamiliar Failure Defense

#### Outcomes

- SYS6-O1
- SYS6-O2
- SYS6-O3
- SYS6-O4
- SYS6-O5
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

1. **Public guarantee matrix and omissions** — Publish fixed membership, non-Byzantine crash-recovery assumptions, durability mode, majority-based write acknowledgment, leader authority, chosen strong/stale read policy, dedup horizon and unsupported dynamic membership.
2. **Build and configuration handoff** — Provide clean-checkout Rust toolchain/lockfile, executable three-replica setup, separate storage paths, bounded synthetic ports/clients, protocol grammar and repeatable local fault-control commands.
3. **Prove core log and election rules** — Use actual implementation traces and independent source/model arguments for persisted votes, last-log voting, matching prefixes, current-term majority commit, ordered apply and no stale-leader success.
4. **Recover with client uncertainty preserved** — Present a crash between sync, commitment, application and client response and distinguish all allowed recoveries; demonstrate one idempotent replay and replicated dedup on leader change.
5. **Test read and snapshot boundaries** — Demonstrate the chosen safe read barrier or explicit stale-read refusal plus a source/trace exercise for snapshot lastIncludedIndex/term, lagging-follower catch-up and dedup retention.
6. **Verify resource and partition failure modes** — Exercise 2+1 split, unreachable majority, slow follower, malformed RPC, queue cap and persistence error under numeric bounds and independently expected results.
7. **Publish benchmark and limitation record** — Supply raw steady/degraded trials, accepted/committed/unknown counts, safe redacted traces, model-search bounds and the limitations of sharing one kernel, physical disk and local network.
8. **Independent novel fault diagnosis** — Analyze an unseen stale leader, prior-term commit, duplicate increment, unsafe read, log/snapshot mismatch or recovery-acknowledgment schedule. Predict two causal hypotheses before replay and make a minimal proven correction or bounded refusal.
9. **Technical defense and forward boundary** — Defend tested invariants, causal repair, counterexamples and honest unknowns before SYS8 operational engineering; do not present a fixed-member teaching protocol as a production-certified Raft implementation.

## Completion requirements

**Six summative assessments cover SYS6-O1–SYS6-O15.** Each assessment has its own public Work/Criteria/Evidence, and all outcomes must be demonstrated against actual mechanisms, not only linked by an ID. Module feedback, supplementary reading and optional protocol extensions do not create hidden completion gates. AS3–AS6 evaluate separate aspects of **one cumulative fixed-membership codebase**: durable replication, adversarial safety verification, constrained measurement and an independent unfamiliar failure. No unrelated new three-node cluster is required for each evaluation.

- **SYS6-AS1** — Distributed Failure, Consistency and Client-Outcome Histories
  - **Outcomes:** SYS6-O1, SYS6-O2, SYS6-O3, SYS6-O4, SYS6-O5.
  - **Work:** Specify a three-replica failure model and a bounded RPC grammar. Analyze **at least five distinct independently supplied or hand-derived histories**: (a) lost response after operation effect, (b) minority partition, (c) a linearizable versus sequentially consistent read/write ordering, (d) duplicate retry with operation identity, and (e) majority/quorum failure with delayed or unacknowledged persistence. Calculate majority intersection for a declared three-node configuration plus one four- or five-node thought case.
  - **Criteria:** Each history identifies named clients/replicas, invocation and response intervals, logical message/term events, state/failure assumptions and accepted/unknown/refused result. Linearizability and sequential consistency are assessed by a real-time/allowed-order argument, not log timestamp sort; a timeout is not mistaken for node death or rollback, and a local-only majority is not assumed to commit unsafe prior-term log entries. The learner distinguishes transport attempt semantics, durable application effect, client visibility, conditional liveness and partition availability without invoking exactly-once RPC magic.
  - **Evidence:** Public fault model, versioned bounded request/response protocol, five independent event histories and expected outcomes, quorum calculations, consistency counterexamples and a defensible assumptions/limitations table.

- **SYS6-AS2** — Fixed-Membership Election, Log and Read Safety Proof Obligations
  - **Outcomes:** SYS6-O5, SYS6-O6, SYS6-O7, SYS6-O9.
  - **Work:** Derive and defend **at least six** small adversarial state traces that cover persistent term/vote before response, last-log-term/index election eligibility, conflicting AppendEntries suffixes, current-term-only direct majority commit, stale isolated leaders, and strong-read authority (conservative committed log barrier/read command or an independently justified equivalent). Include one trace with a previously elected leader and an old-term entry present on a majority but **not yet safely committed**.
  - **Criteria:** Election safety, leader completeness, log matching, committed-prefix preservation, durable follower acknowledgment, monotonically valid commit/apply and fixed-member majority intersection follow from explicit state transitions and original Raft safety restrictions relevant to the claimed design. No unqualified assertion that any majority copy of an older-term entry commits it. A stale leader without a current majority cannot serve a claimed linearizable read or acknowledge strong writes; lease/ReadIndex claims require their missing proof obligations to be recognized. A log-matching counterexample is actually excluded by the specified candidate-voting and conflict rules, not hidden by a happy-path replay.
  - **Evidence:** Six independent term/index/log/vote and read event traces, persistent-state transition table, hand-derived majority/commit calculations, safety invariant/counterexample explanations, declared omissions and versioned reference model.

- **SYS6-AS3** — Durable Three-Replica Rust State Machine
  - **Outcomes:** SYS6-O2, SYS6-O6, SYS6-O7, SYS6-O8, SYS6-O10, SYS6-O14.
  - **Work:** Implement one locally reproducible **three-process, fixed-member Rust key-value service** with separate persistent replica directories, bounded RPC queues and message sizes, leader election, log append/matching/retry, quorum-based **current-term** commit, ordered apply, client-session request deduplication and safe strong read or explicit refusal. Persist term/vote/log before protocol responses that depend on them and reuse SYS5's crash-safe record approach. Publish and analyze a bounded snapshot/lagging-follower state-transfer example (lastIncludedIndex/Term, applied index, durable dedup state), implementing snapshot install optionally; if omitted, enforce a finite log cap and explicit unavailable/refusal behavior.
  - **Criteria:** Known fixed members have unique stable identities and bounded resources; majority durable replication precedes durable-acknowledged write success, and the current-term commit restriction prevents unsafe prior-term commitment. Follower conflict handling, persistent votes and recovery cannot knowingly discard a committed acknowledged prefix under the declared crash model; state-machine apply is ordered and deterministic. Duplicate same-session request IDs return the prior applied result without rerunning a non-idempotent effect within the documented retention horizon, while mismatched payload IDs and expired sessions are rejected. Strong reads are processed by the declared committed/applied mechanism, never by leader identity alone; loss of quorum causes refusal or unknown, not a fabricated success. Snapshots/state transfer are source/model analyzed even if optional in the executable, with safe log-growth refusal when omitted. **No claim of formally verified production consensus follows merely from passing tests.**
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
  - **Outcomes:** SYS6-O4, SYS6-O6, SYS6-O7, SYS6-O11, SYS6-O12, SYS6-O14, SYS6-O15.
  - **Work:** Diagnose a **new** bounded reviewer-supplied fault or transparent public variant, such as a second vote after a crash, prior-term overcommit, unsafe read after lost quorum, stale-term log repair, lost dedup state after restart, incorrectly installed snapshot or duplicate RPC with conflicting payload. Before running the case, state **two competing causal hypotheses**, expected client/log/term transitions and one discriminating observation; provide a minimal code or model correction or justified safe refusal, then rerun independent negative and previously correct histories.
  - **Criteria:** The learner locates the earliest violated election/log/commit/read/application invariant in a plausible asynchronous event history and distinguishes unknown client completion, data loss and consistency violation. A correction preserves fixed-member quorum and durable-response rules, rejects old/conflicting authority and satisfies independently specified safety or honest refusal; the evidence differentiates deterministic model versus observed process behavior and states untested schedule and hardware assumptions. Merely replaying a memorized seed, showing a successful green suite or calling the component fully verified Raft cannot establish SYS6-O15.
  - **Evidence:** Original unseen challenge/seed, predictions and competing hypotheses, annotated event and state timelines, independent sequential/history oracle, source patch or bounded refusal rationale, before/after and neighboring-case regressions, a written/recorded/live technical defense and residual limitations.

### Academic scope, safe practice and independence

[SYS4](SYS4.md) owns connection-level framing, nonblocking multi-client service, transport failure and network backpressure; [SYS5](SYS5.md) owns local WAL durability, manifest/snapshot publication and file fault injection; [SYS3](SYS3.md) owns user-space concurrency invariants and concurrent history analysis. SYS6 uniquely owns distributed failure ambiguity, operation identity across nodes, quorum intersection, term/vote/log safety, strong read semantics, deterministic fault schedules and replicated state-machine recovery. [SYS7](SYS7.md) will develop deeper production-performance causality; [SYS8](SYS8.md) owns operational reliability/capacity/deployment trade-offs, not a second consensus implementation. Full production Raft membership change, Byzantine-tolerant protocols, multi-region deployment, cryptographically authenticated cluster traffic, unbounded log compaction and universally linearizable lease reads remain outside this reference course unless independently implemented, specified and verified.

Every assessed experiment uses bounded local synthetic clients, controlled process termination, independent fixture directories and nonprivileged loopback sockets, never destructive host network rules, public deployments, real production data or paid infrastructure. Code-only or offline model alternatives can aid understanding, but SYS6-O8/O14 and AS3 require **an actually running three-process educational replica service**. Learners may submit equivalent accessible state tables, event timelines, source excerpts and written rather than live defenses while meeting the identical correctness/evidence rules.

### Revision integrity, provenance and readiness

The published **SYS6-O1–SYS6-O15** and **SYS6-AS1–SYS6-AS6** identities remain stable; stronger explicit current-term-commit, durable-vote, dedup, read-authority, snapshot-boundary and independent-oracle expectations are **material clarifications applying to this course revision**, not grounds for automatic regrading or re-awarding preexisting learner work. Each evaluated decision identifies learner/source revision, environment, assessment/outcome IDs, independently expected and actually observed results, qualified reviewer, model assumptions and limitations. This course remains `draft` until authentic learner and independent reviewer evidence supports promotion; CI format checks are not proof of a formally correct consensus implementation.

## Optional disciplinary references

All are public independent-study sources rather than compulsory paid materials, hidden tests or assertions of accreditation.

- [Ongaro and Ousterhout — Raft extended paper](https://pdos.csail.mit.edu/6.824/papers/raft-extended.pdf) — core terms, persistent votes/log, leader completeness, majority/current-term commitment, membership and snapshots.
- [MIT 6.5840 Distributed Systems](https://pdos.csail.mit.edu/6.5840/) — public distributed-failure reasoning, historical clients and fault-controlled testing.
- [Raft project](https://raft.github.io/) — consensus visualizations and linked primary material.
- [Jepsen — consistency models](https://jepsen.io/consistency) — client histories, read/write outcomes and model distinctions.
- [TLA+](https://lamport.azurewebsites.net/tla/tla.html) — an optional formal exploration tool, not a mandatory hidden prerequisite or substitute for required implemented evidence.
