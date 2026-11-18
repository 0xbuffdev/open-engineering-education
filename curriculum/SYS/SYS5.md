# SYS5 — Storage Engines & Data Systems

**Program:** SYS — Systems Engineering
**Type:** `course`
**Prerequisites:** [SYS2](SYS2.md), [SYS3](SYS3.md)
**Duration:** 16–20 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–15 focused hours/week (provisional)

> [Systems Engineering](README.md) · [Course format](../../spec/course-format.md) · [Design guide](../DESIGN-GUIDE.md)

## Overview

SYS5 teaches **single-node persistent storage correctness**: how an executable Rust key-value engine specifies observable operations, encodes checked durable records, recovers from interrupted writes, publishes immutable segments, prevents deleted data from reappearing, manages readers and proves its claims using independently calculated failure histories. [SYS2](SYS2.md) already teaches Rust ownership, checked byte I/O and file/descriptor behavior; [SYS3](SYS3.md) already teaches concurrency invariants, safe shared state and cancellation; [SYS10](SYS10.md) supplies the kernel filesystem, buffering and device-pathway model. SYS5 **advances beyond**, rather than reassesses, those prerequisites by implementing WAL/recovery, durable metadata, read indexes, compaction and crash-state reasoning. It does not require APP relational/SQL preparation or build a second B+tree database.

**Core integration:** A bounded Rust **single-node log-structured key-value store** with `get`, `put`, `delete` and ordered `scan` over synthetic byte keys/values; an explicitly defined durable or weaker acknowledgment mode; a validated versioned WAL, replay and checked record format; an ordered memtable; immutable indexed sorted segments; authoritative manifest generations; safe tombstones and compaction; a declared single-writer/reader visibility policy; deterministic fault injection and a reviewable technical defense. One cumulative source tree is **reused across** the WAL, segment, measurement and unknown-case assessments rather than producing four nearly identical engines.

**Correctness model:** A write *acknowledged durable* must survive within the published OS/filesystem/storage assumptions and fault model. A write that was **not acknowledged may still survive**, particularly after it was synced but before its reply was observed; recovery may not simply erase or falsely claim the absence of all unacknowledged writes. Process termination, injected short write, simulated torn sector, kernel crash and power loss are distinct events; no finite local process-fault suite proves universal physical-device persistence. A torn **final WAL tail** may be handled under an explicit conservative policy, but a corrupted **earlier committed record** or manifest cannot be silently skipped as if it were a harmless tail. File rename visibility, fsync of file contents and parent-directory metadata persistence are separate decisions, all conditional on documented platform guarantees.

**Execution and access:** Reference environment is stable Rust and Cargo, a nonprivileged local Linux filesystem and learner-owned disposable fixture directories with numeric disk/memory/open-file bounds. Optional free tools can help inspect layouts but no root, raw block device, production database, paid infrastructure, hardware power-cycle, mandatory unsafe Rust or proprietary checker is needed. The baseline can use safe Rust `std::fs` and standard collections, with declared platform-specific sync behavior; a simulated fault-injection adapter and optional isolated subprocess provide reviewable evidence without damaging unrelated data. A public `draft` course does not assert production durability or security certification.

**Effort:** **16–20 weeks** at **10–15 focused hours/week** (160–300 hours) is a provisional estimate covering source study, models, implementation, debug/fault sweeps, measurements, review and revision—not a fixed completion gate. The **fourteen stable learning outcomes and five assessment IDs** are retained. Changes to their evaluation detail are prospective to this source revision; historical learner decisions must remain tied to the applicable course/spec version.

## Learning outcomes

- **SYS5-O1:** Specify read/write/delete semantics, durability assumptions and crash invariants for a bounded single-node storage engine.
- **SYS5-O2:** Design a versioned on-disk record format with bounded encoding, lengths, checksums and corruption behavior.
- **SYS5-O3:** Explain OS buffering, write ordering, file and directory synchronization and the limits of crash-durability claims.
- **SYS5-O4:** Implement and validate append-only logging, WAL replay, truncation and idempotent crash recovery.
- **SYS5-O5:** Analyze page, B+tree and log-structured index trade-offs with explicit workload and access assumptions.
- **SYS5-O6:** Implement sorted-table, in-memory index, immutable-segment and compaction mechanisms with safe replacement rules.
- **SYS5-O7:** Explain tombstones, snapshot/read visibility, stale versions and resource reclamation in a single-node engine.
- **SYS5-O8:** Apply concurrency control to shared engine state and state precisely which transactions/isolation guarantees are and are not provided.
- **SYS5-O9:** Design checksum, length, offset and version checks that prevent silently accepting malformed or torn data.
- **SYS5-O10:** Construct a deterministic crash/fault-injection harness and compare recovered state with an independent oracle.
- **SYS5-O11:** Benchmark read/write/scan/compaction workloads with warm/cold cache caveats and write-amplification metrics.
- **SYS5-O12:** Build an inspectable Rust key-value engine with bounded memory, recovery, maintenance and correct shutdown.
- **SYS5-O13:** Distinguish storage correctness, operational resilience, encryption, permissions and secure erase boundaries.
- **SYS5-O14:** Defend a previously unseen corruption or durability defect with an explicit recovered-state proof and repair.

## Modules

### Module 1 — Storage Contracts, Crash Models and Observable Guarantees

#### Outcomes

- SYS5-O1
- SYS5-O3
- SYS5-O8
- SYS5-O13

#### Lessons

1. **From prerequisite APIs to a public persistent-state model** — Build from SYS2's owned files/checked byte I/O and SYS3's concurrent invariants without retesting either. Define byte-key `get`, `put`, `delete` and ordered `scan` semantics, bounded inputs and a sequential reference map; exhibit a case where individually correct writes and race-free code nevertheless violate post-restart state.
2. **Visibility, acknowledgment and persistence** — Separate receipt, append, memory publication, successful sync, client acknowledgment and recovery after restart. Show a legal failure trace where an unacknowledged write survives and why the protocol must not promise it disappears.
3. **Crash classes, recovery prefixes and acknowledgment uncertainty** — Distinguish process termination, injected short write, kernel crash, power loss and corruption under named fault assumptions. Derive legal recovered operation prefixes when a sync succeeds but the response is lost, requiring all acknowledged durable writes while allowing some unacknowledged writes to survive; do not treat a process-kill fixture as a physical power-loss experiment.
4. **Durable and weaker explicit modes** — Compare a selected durable-acknowledgment mode with an optional batch/no-sync mode. Explain which acknowledged writes are expected after restart *under the declared filesystem/device assumptions* and why the modes must not share a durability claim.
5. **Atomicity and consistency scope** — Define single-operation atomic update, ordered single-writer semantics and optional atomic batch as separate contracts; do not imply SQL transactions, multi-key isolation or distributed consensus merely because a WAL exists.
6. **Threat, privacy and test isolation** — Bound learner-owned fixture directories, file sizes, keys and logs; distinguish accidental checksum-detected corruption from malicious tampering, encryption, authorization and secure erasure. Never fault-inject against a real user database.

*Optional formative feedback:* Hand-solve an acknowledgment/restart timeline under durable and unsynced modes and identify which observed post-crash states are permitted.

### Module 2 — Binary Record Formats, Checked Parsing and Integrity

#### Outcomes

- SYS5-O2
- SYS5-O9
- SYS5-O13

#### Lessons

1. **Versioned disk grammar and incompatible-format policy** — Specify magic, type, sequence, key/value lengths, checksum coverage, endianness and maximum file/record sizes before encoding. Define an explicit reject or migration rule for an unsupported version, and provide a counterexample where accepting an unknown layout based only on its magic corrupts interpretation.
2. **Checked record arithmetic** — Use try_from and checked_add to verify offsets, length headers and file sizes before allocation or slicing; derive a corrupted maximum-length fixture that a naïve unchecked parser would mishandle.
3. **Record types, monotonic identities and tombstone semantics** — Distinguish put, delete tombstone, empty value, optional control record and duplicate sequence/operation IDs in a canonical byte contract. State which replay duplicates are idempotent, which conflicting same-sequence record must be refused, and why a tombstone must not be decoded as an absent record.
4. **Checksums and covered regions** — Define which header/payload bytes contribute to an accidental-error checksum, where the checksum is stored and what a mismatch means. Explain CRC collision limits and why it neither authenticates records nor protects against a malicious editor.
5. **Header and body truncation states** — Classify EOF at a record boundary, truncated header, truncated body and a checksum-failed *complete* record separately; prescribe a conservative parser/recovery action rather than skipping arbitrary bytes to find magic.
6. **Pages and block-layout comparison** — Model fixed-size pages, slotted-page offsets and sequential-log records to compare update locality, fragmentation and storage overhead without requiring a production page manager or raw direct I/O.
7. **Independent golden byte oracles** — Hand-derive exact bytes and checksum inputs for normal put/delete, empty value, maximum allowed length, invalid checksum, overflow, early EOF and unknown-version cases. Compare implementation output to independent fixtures.

*Optional formative feedback:* Review a deliberately corrupted binary header and calculate precisely why it must be rejected before a buffer allocation.

### Module 3 — File Synchronization, Directory Metadata and Publication Ordering

#### Outcomes

- SYS5-O1
- SYS5-O3
- SYS5-O4
- SYS5-O6

#### Lessons

1. **User buffers, handles and fallible persistence completion** — Trace BufWriter::flush, file writes, File::sync_all/sync_data, ordinary Drop and opened handles to the actual userspace/kernel boundary without reteaching SYS2 APIs. Distinguish errors that must be observed explicitly, kernel writeback and durability guarantees a destructor or a successful partial write cannot establish.
2. **Short I/O and persistent error handling** — Handle partial writes, Interrupted, disk-full and a failed sync before returning an acknowledgment; show why an I/O error may leave a partial physical/logical file and why retry may require recovery inspection.
3. **Rename visibility, directory identity and filesystem assumptions** — Analyze same-filesystem atomic namespace visibility, changing directory entries and stable open-file identity; separate it from persistence of directory metadata and platform-specific rename guarantees. Use collision-safe private temporary paths and reject cross-filesystem or unverified hostile-path publication assumptions.
4. **File-before-manifest publication and dependency ordering** — Derive the write-temp, complete-file-sync, rename, directory-sync and manifest-generation publication graph under an explicitly supported Linux filesystem model. Ensure a durable manifest never names an unsynced segment, old generations remain until the new one is authoritative, and show one crash state where a reversed dependency would lose acknowledged data.
5. **Crash-points in two-phase publication** — Trace failures before temporary file sync, after sync, after rename, before directory sync and after directory sync. Classify whether startup chooses the previous or next generation under explicit persistence assumptions.
6. **Fail-safe conservative fallback** — When host filesystem/OS assumptions are not verifiable, refuse an unsupported durability level or document a narrower one; no mandatory raw block-device or privileged power-failure experiment.

*Optional formative feedback:* Draw the ordering DAG for a new segment and manifest; identify the first incorrect publication step when a crash leaves a manifest pointing at an unsynced file.

### Module 4 — Write-Ahead Logging, Commit Decisions and Restart Replay

#### Outcomes

- SYS5-O1
- SYS5-O3
- SYS5-O4
- SYS5-O9
- SYS5-O10

#### Lessons

1. **WAL role, sequence identity and commit frontier** — Distinguish WAL-as-authoritative-append from WAL-protecting-memtable-and-segments, and publish record sequence/high-water/optional grouped-ack rules. Identify the durable-ack frontier and replay range, and explain why a complete but unacknowledged record beyond that frontier may still be recovered without falsely implying absence.
2. **Single-writer commit pipeline and ambiguous response** — Trace validate → append full framed record → successful required sync → publish visible state → reply under a stated single-writer policy. Derive independent recovery oracles for failure before sync, after sync before response and after acknowledgment; distinguish the client's unknown result from an engine claim that a synced update disappeared.
3. **Partial append and write failure** — Simulate short writes, no-space, interrupted transfers and a process stop between header and body bytes; ensure an incomplete tail is not treated as a complete committed operation.
4. **Idempotent replay through repeated interruption** — Reconstruct latest key versions and tombstones from ordered WAL records plus a durable checkpoint high-water mark, refusing conflicted sequence IDs. Inject a second shutdown during replay or checkpoint cleanup and prove repeated clean reopens do not apply one accepted effect twice or retire evidence needed for acknowledged state.
5. **Tail damage versus internal corruption** — Allow a carefully specified incomplete **final tail** to be truncated/rejected based on policy, while treating checksum/structure corruption *inside an earlier required record* as an error requiring refusal or explicit repair—not silent resynchronization.
6. **Checkpoint state and WAL retirement** — Describe a checkpoint generation that durably captures records through a known sequence, ensuring referenced segments and manifest are published and synced before older WAL extents may be retired.
7. **Fault hooks and publication trace ledger** — Install deterministic user-space hooks after append, sync, memtable publish, segment sync, manifest publish, directory sync and WAL retirement; log enough stage and sequence identity to reconstruct recovery decisions.
8. **Evidence versus physical crash guarantees** — Separate a simulated write tear, injected sync error and process termination from actual kernel crash or sudden power loss. Document why tests exercise algorithmic ordering and cannot establish every device/cache persistence behavior.

*Optional formative feedback:* Predict recovered key versions for failures after the append, sync, visible update, manifest sync and WAL retirement, then compare to independently derived legal prefixes.

### Module 5 — Memtables, B+Tree Comparison and Indexed Read Paths

#### Outcomes

- SYS5-O5
- SYS5-O6
- SYS5-O7
- SYS5-O9
- SYS5-O11

#### Lessons

1. **In-memory memtable state** — Choose a bounded ordered map for the initial single-writer memtable, keeping latest version/tombstone per key and calculating size accounting for key/value plus container overhead.
2. **From append offsets to lookup** — Contrast scanning the full WAL, a hash index of current offsets and a sorted run with sparse index. Explain the effect of workload and key order on point lookup, ordered iteration and rebuild cost.
3. **B+tree lookup, update paths and LSM trade-offs** — Under an explicit page size/fanout, hand-trace B+tree root-to-leaf lookup plus split/merge/rebalance for a small index, deriving page reads and rewritten nodes. Contrast with the log-structured read/write pattern without requiring a second executable B+tree engine or treating a toy calculation as a universal performance winner.
4. **Log-structured merge organization** — Explain write buffer, immutable sorted-table files, generation/level metadata and the read path merging newer and older runs, without promising RocksDB's exact production compaction semantics.
5. **Checked sparse indexes and optional Bloom filters** — Specify bounded SSTable block offsets, footer lengths and sparse key entries checked before dereferencing or allocating; reject an out-of-range corrupt index. Where a Bloom filter is used, calculate its memory/false-positive trade-off and explain why a reliable negative depends on correct version/segment coverage and a positive never proves membership.
6. **Range scans and merge order** — Perform an ordered k-way merge across memtable and multiple immutable runs with duplicate keys, latest sequence wins and tombstones suppressing older values; specify range endpoints and output count limits.
7. **Read and write amplification accounting** — Calculate an illustrative point-read file count, scan work, bytes written and storage overhead for two workload mixes; identify cache and compression/size limitations rather than treating one LSM configuration as universal.

*Optional formative feedback:* Compute a two-level B+tree lookup and a three-run LSM read for the same keys; derive where the latest tombstone must win.

### Module 6 — Immutable SSTables, Manifest Generations and Crash-Safe Compaction

#### Outcomes

- SYS5-O3
- SYS5-O6
- SYS5-O7
- SYS5-O9
- SYS5-O10
- SYS5-O12

#### Lessons

1. **Sorted immutable segment and WAL-covered flush** — Create a sorted checked SSTable-like file with valid key order, block/footer layout and integrity checks, built from a frozen bounded memtable. Trace incomplete write, file sync and live publication, showing why the WAL still covers updates until a verified durable segment and manifest are authoritative.
2. **Authoritative manifest generations and atomic replacement** — Define versioned checksummed manifest contents, active segment IDs, order and covered sequence high-water mark. Derive next-generation temp-write/sync/rename/parent-directory-sync publication under named filesystem assumptions; identify why a renamed but unsynced directory entry is not a universally durable commit.
3. **Startup selection and orphan cleanup** — Choose the valid published generation deterministically after crash; ignore or quarantine unreferenced temporary/new files and distinguish safe garbage collection from deleting still-live segments.
4. **Version-aware compaction, tombstones and resurrection prevention** — Merge sorted runs with latest-sequence-wins for point lookups/scans and explicitly retain values needed by active snapshots or deeper overlapping runs. Hand-derive a delete whose tombstone removal resurrects an older value; permit drop only when the relevant older-version and reader retention horizons are proven safe.
5. **Peak disk and temporary-space constraints** — Budget input and output files, temporary manifest, source retention and concurrent writes so compaction may refuse or pause safely when free-space budget is exhausted without deleting the last recoverable copy.
6. **Interruption before and after publication** — Inject failure during output file construction, sync, manifest write, rename, directory sync and old-file reclaim; reopen and verify active keys and tombstones against independent expected generations.
7. **Reader generations and safe reclamation** — Keep immutable segment generations pinned until readers release them; schedule deferred unlink only after durable new manifest and absence of consumers needing older files.
8. **WAL checkpoint truncation order** — Link compacted sequence coverage, durable segment/manifest publication and WAL retirement, verifying that replay never assumes a missing checkpoint record and that old WAL is not removed prematurely.

*Optional formative feedback:* Trace a compaction across two overlapping runs with an old value and a delete marker; demonstrate how a premature tombstone drop resurrects deleted data after reopen.

### Module 7 — Snapshot Visibility, Concurrency Control and Resource Policies

#### Outcomes

- SYS5-O1
- SYS5-O7
- SYS5-O8
- SYS5-O12
- SYS5-O13

#### Lessons

1. **Explicit single-writer architecture** — Specify a single mutating writer and multiple readers using SYS3's Rust synchronization competencies; say how other process instances are excluded or unsupported rather than silently asserting inter-process lock correctness.
2. **Commit visibility and read ordering** — Define an operation's linearization/visibility point relative to the synced WAL and in-memory state; demonstrate how a concurrent get can see a complete old or new version, not a partial multi-step mutation.
3. **Snapshot sequence, pinned generations and tombstone retention** — Define a snapshot's sequence/visibility point and pin immutable segments plus in-memory versions for its full lifetime, including scans during concurrent compaction. Prove which tombstones and old values remain necessary until the oldest relevant reader releases its reference, then identify a premature-reclaim counterexample.
4. **Lock order and maintenance lifecycle** — Apply SYS3 lock-order and wakeup reasoning to writer, memtable, manifest and compaction work; keep blocking disk I/O outside inappropriate long-held critical sections under an explicit invariant.
5. **Batch atomicity versus unsupported transactions** — Describe a possible atomic batch with one commit marker or protected group, but make any implementation optional unless explicitly covered by selected API. Do not claim serializable arbitrary multi-key transactions from per-record append.
6. **Engine-wide resource quotas and fail-closed persistence** — Publish numeric bounds for key/value sizes, memtable, WAL, open readers/files, snapshots, disk footprint and peak compaction temporary space. Inject ENOSPC and sync failure, accounting for already-dirty state without acknowledging an unsynced write; use a safe refusal or read-only/fail-closed policy rather than continuing with unresolved corruption.
7. **Operational privacy and access boundaries** — Describe OS file permissions, possible filename/backup data exposure, checksums versus authentication and the absence of built-in encryption or secure erase; keep logs from leaking key/value contents by default.

*Optional formative feedback:* With two long-running scans, a delete and compaction, show which generations remain pinned and the earliest safe reclaim event.

### Module 8 — Independent State Models, Crash Sweeps and Corruption Diagnosis

#### Outcomes

- SYS5-O1
- SYS5-O4
- SYS5-O9
- SYS5-O10
- SYS5-O13

#### Lessons

1. **Independent state model and reproducible operation histories** — Construct a separate sequential put/get/delete/ordered-scan oracle with sequence IDs, accepted/failed replies and reference key-version state. Generate seeded normal, replacement, deletion, duplicate and range histories within published budgets, comparing every acknowledged result rather than deriving expectations from the storage engine's own output.
2. **Enumerate persistence cut points** — Define a finite crash sweep over the WAL append/sync/memory publish, segment write/sync, manifest write/rename/directory sync and obsolete-file reclaim stages, with repeatable small fixtures.
3. **Unacknowledged versus acknowledged uncertainty** — Compute allowed recovered states for a crash before/after acknowledgment, preserving all acknowledged durable operations and allowing a synced-but-unacknowledged operation under the declared mode rather than insisting it disappear.
4. **Tail tear and internal corruption adversaries** — Inject partial final header/body, a checksum-invalid complete interior record, malformed sparse offset and corrupted manifest. Require explicit distinguishable recover, refuse, quarantine or supported repair outcomes.
5. **Controlled I/O fault seams versus process termination** — Inject partial writes, failed sync, ENOSPC and permission/EOF faults using bounded adapters, with deterministic recovery-stage provenance. Optionally stop an owned subprocess at a declared hook then reopen it; explicitly distinguish modeled failure, real process death and untested kernel/power-failure behavior.
6. **Repeated reopen and idempotence oracle** — Reopen recovered stores multiple times without new writes, compare version/tombstone/manifest state and prove no additional effects, leakage or premature segment deletion across repeated recovery.
7. **Causal corruption diagnosis and independent regression** — For a rehearsed or independently specified failure, contrast record checksum, stale index, WAL commit frontier, manifest publication and tombstone reclamation explanations. Select a discriminating fixture, justify a minimal repair or conservative refusal and rerun an independent negative oracle plus previously correct cases; reserve a genuinely novel variant for AS5.

*Optional formative feedback:* Use a supplied failure-stage ledger to predict restart state, then identify whether wrong output comes from unsynced acknowledgment, index update or bad manifest publication.

### Module 9 — Performance, Write Amplification and Storage Capacity Evidence

#### Outcomes

- SYS5-O5
- SYS5-O6
- SYS5-O11
- SYS5-O12

#### Lessons

1. **Comparable workload, datasets and cache provenance** — Specify fixed key/value distribution, point-write/update/delete/get/scan mix, working-set size and independently checked data results. State warm/cold cache limitations and filesystem/device assumptions, and avoid comparing a synced engine with an unsynced alternative as if their guarantees were identical.
2. **Throughput, latency and repeated-trial uncertainty** — Measure useful operations/s, logical bytes/s, operation latencies and only sample-supported percentiles; retain at least five individual trials per configuration plus center/spread, units, refused operations and actual toolchain/OS/storage environment. Explain background work and cache/warmup confounders rather than presenting an unsupported precision claim.
3. **Write/read/space amplification** — Measure or derive logical payload bytes, WAL bytes, segment/compaction bytes, pages or runs examined per lookup and temporary/steady disk usage; distinguish ratios from end-to-end filesystem device writes.
4. **Compaction policy under concurrent reads and disk limits** — Compare no/size-triggered/level-like compaction with read latency under fixed correct workloads, explicitly accounting for lock hold, cache effects, temporary disk, tombstone horizons and write/read amplification. Reject an apparent optimization that discards acknowledged data or exhausts disk before safe publication.
5. **Flush and synchronization cost** — Measure log-sync grouping under durable and weaker modes separately, explaining how batching changes acknowledgment latency, failure windows and reproducibility rather than advertising unsafe speedup.
6. **Performance-informed engineering decision** — Defend one memory/disk/latency trade-off using measured evidence and explicit threat to durability or correctness, including a rationale for rejecting a faster configuration.

*Optional formative feedback:* Analyze a compaction workload where faster writes come from disabled sync and explain why it cannot be claimed as a same-guarantee performance improvement.

### Module 10 — Integrated Rust Storage Engine and Independent Defense

#### Outcomes

- SYS5-O1
- SYS5-O4
- SYS5-O6
- SYS5-O7
- SYS5-O8
- SYS5-O10
- SYS5-O11
- SYS5-O12
- SYS5-O14

#### Lessons

1. **One bounded engine API, modes and implementation scope** — Release a single nonprivileged Rust key-value engine with get/put/delete/ordered-scan, clear byte-format and key/value limits, single-writer/readers contract, durable versus weaker acknowledgment modes and error categories. State unsupported multi-key transactions and filesystem/power-loss guarantees before testing.
2. **Integrate one WAL, indexed segment and manifest pipeline** — Reuse AS2's validated WAL/replay and AS3's ordered memtable, SSTables, manifest, tombstones and compaction in the same source tree. Trace sequence coverage from acknowledged append through synced immutable segment and durable generation to safe WAL retirement, refusing a checkpoint that would leave data unrecoverable.
3. **Snapshot, compaction and end-to-end crash regression** — Verify bounded reader generations, no resurrection after delete, disk-failure refusal and safe maintenance while scans run. Apply AS2/AS3 independent byte/state oracles and AS4 whole-engine crash fixtures to successive reopens without demanding a second database or duplicating the earlier summative submissions.
4. **Reproducible runbook, capacity and meaningful measurement** — Publish exact Rust/Cargo/target/FS assumptions, commands and finite memory/disk/fd budgets, with privacy-safe logs and separate durability modes. Reuse same-guarantee read/write/scan/compaction trials with raw data, checked recovered state, amplification and carefully bounded performance claims, not a misleading no-sync speedup.
5. **Defend an unseen recovery defect** — Analyze a reviewer-supplied unknown WAL/manifest/compaction/snapshot failure with two hypotheses, a before-observation prediction, source-grounded minimal correction/refusal and independent positive/negative regression.

*Optional formative feedback:* Present a previously unseen crash just after directory sync but before WAL retirement, then prove the recovered acknowledged prefix and which files may be reclaimed.

## Completion requirements

**Exactly five summative evaluations cover SYS5-O1–SYS5-O14.** Module practice and supplementary reading are formative, not hidden gates. AS5 evaluates only the distinct unfamiliar-diagnosis outcome O14; all other outcomes remain mandatory under AS1–AS4. AS2 provides the WAL/recovery code, AS3 adds indexed segments/compaction, AS4 integrates and measures the **same engine**, and AS5 evaluates a novel failure on that base; no additional unrelated database implementation is required. Each distinct assessment still requires independently evaluated behavior, success criteria and evidence. A green build, a single successful restart or a benchmark chart alone does not establish crash safety.

- **SYS5-AS1** — Public Storage, Binary Format and Durability Contract
  - **Outcomes:** SYS5-O1, SYS5-O2, SYS5-O3, SYS5-O9, SYS5-O13.
  - **Work:** Specify `get/put/delete/scan`, sequential visible-state behavior, durable and optionally weaker acknowledgment semantics, a versioned binary record layout with bounded fields/checksum and a manifest-generation/file-publication ordering plan. Independently solve **at least five distinct histories or byte fixtures** covering successful write, sync-before-reply crash, final partial WAL record, interior corruption, and file/manifest rename plus directory-sync failure under stated Linux/filesystem assumptions.
  - **Criteria:** Valid and invalid bytes have exact independently computed outcomes with length arithmetic checked before allocation; magic/version/sequence/checksum/encoding fields and unknown-format policy are unambiguous. Committed/acknowledged writes must not be lost in the declared durability model, whereas synced-but-unacknowledged operations are not falsely asserted absent. File write, flush, sync_all/sync_data, rename and parent-directory sync are distinguished rather than treated as interchangeable durability proofs. Earlier committed-record corruption is not silently dismissed as trailing damage; checksum is not represented as authentication or secure erasure.
  - **Evidence:** API/state and failure-model specification, versioned grammar and byte-layout tables, five independent golden/invalid fixtures and hand-derived recovery histories, required ordering DAG, named environment assumptions, threat/retention limitations and rationale.

- **SYS5-AS2** — WAL, Acknowledgment and Replay Implementation
  - **Outcomes:** SYS5-O1, SYS5-O3, SYS5-O4, SYS5-O9, SYS5-O10.
  - **Work:** Implement the bounded Rust WAL append/checked parser/replay/recovery component used by AS4. Use deterministic fault hooks **before append, during partial append, after complete append, before sync, after sync but before reply, and during replay/checkpoint retirement**. Supply independent expected key/version sequences, distinct acknowledged and ambiguous operations, and repeated-reopen evidence; publish durable and any optional weaker sync mode separately.
  - **Criteria:** A durable acknowledgment is emitted only after the required successful sync under the declared model; partial/error paths fail visibly without silently acknowledging data. Replay accepts complete valid records in sequence, conservatively classifies an **incomplete final tail** and **does not silently truncate a checksum-invalid complete record** merely because it is the final record; earlier committed or structurally invalid records require explicit refusal/quarantine unless a separately justified recovery protocol applies. Replay is idempotent across repeated restarts and checkpoints. Injected short I/O, disk full and sync errors have bounded outcomes. The independent oracle permits a correctly persisted unacknowledged operation but cannot accept missing acknowledged durable operations or double-application effects. Evidence never calls injected process crashes a proof of physical power-loss durability.
  - **Evidence:** Reproducible Rust WAL source, manifest/toolchain lockfile where appropriate, state and sequence tables, fault hooks and seeds, hand-derived allowed-recovery oracle, actual observed restart logs, repeated-open and malformed-record tests, explanatory limitations.

- **SYS5-AS3** — Indexed SSTables, Tombstones and Safe Compaction
  - **Outcomes:** SYS5-O5, SYS5-O6, SYS5-O7, SYS5-O8, SYS5-O9.
  - **Work:** Extend the **same engine** with a bounded ordered memtable, immutable indexed sorted segment files and active-generation manifest; implement merge, delete tombstones and a compaction/publish/reclaim protocol. Provide a worked B+tree versus LSM index comparison, and a read/snapshot policy with explicit reader lifetime. Test interrupted flush/compaction, corrupt segment offsets, a live reader during replacement and older versions behind tombstones.
  - **Criteria:** Latest-wins get and ordered scan match a separately derived sequential oracle across updates, deletions and multiple runs; index/footer offset and record-length validation reject malformed data. Output segments are synchronized before a durable manifest may reference them, old files are not reclaimed before authoritative publication or reader release, and WAL retention covers any sequence not yet durably checkpointed. Compaction does not resurrect deleted keys by premature tombstone removal; snapshots see one declared coherent version and keep required segment generations alive. Numeric memory/disk/temporary-space constraints and low-space refusal are explicit. The B+tree comparison uses independently calculated page/layout costs and does not demand a second storage product.
  - **Evidence:** Source and layout fixtures, manifest generation/ownership diagrams, independent get/scan/tombstone reference cases, hand-derived B+tree and LSM costs, interruption/corruption/restart results, snapshot/reclamation traces and documented resource policy.

- **SYS5-AS4** — Reproducible Single-Node Rust Engine and Storage Measurements
  - **Outcomes:** SYS5-O1, SYS5-O4, SYS5-O6, SYS5-O8, SYS5-O11, SYS5-O12, SYS5-O13.
  - **Work:** Integrate the **same AS2/AS3 source** into a local, nonprivileged `get/put/delete/scan` Rust library or CLI with documented single-writer/concurrent-reader scope, recovery and maintenance operations. Test normal, malformed, disk-full, sync-error, compaction-interrupted and snapshot read cases with an independent state oracle. Compare at least **two workload regimes** (such as write-heavy and scan-heavy) in the **same declared durability mode**, and optionally compare explicitly labeled weaker-mode performance separately.
  - **Criteria:** Fresh checkout reproduces the implementation and independent invalid/restart tests, with numerical caps on keys/values, memtable, WAL, readers, active/temporary disk and file handles. No corrupt checksum or invalid manifest is silently accepted; forced maintenance or failure cannot discard committed acknowledged data under the model. Both workload regimes check identical intended data semantics and present **at least five individual timings per configuration**, valid units, center/spread, measured read/write/space amplification where relevant and cache/filesystem/device confounders. An unsynced variant is not presented as a same-guarantee speedup. File permissions, logs, encryption absence and secure-deletion boundaries are described accurately.
  - **Evidence:** Complete runnable Rust project with documented dependencies and lockfile, clean-build/readme runbook, numeric limits and guarantee table, fixture sources, independent end-to-end/failure suite, repeat-run timing datasets and calculations, operator/shutdown notes and explicit limitations.

- **SYS5-AS5** — Unfamiliar Persistent-State Failure Defense
  - **Outcomes:** SYS5-O14.
  - **Work:** Investigate **one previously unseen** bounded storage failure supplied by an independent reviewer or transparent public variant rule: an incomplete WAL tail, corrupted internal record, stale sparse index, prematurely dropped tombstone, manifest referencing an unsynced segment, early WAL retirement or reader/compaction generation hazard. **Before running code**, name two competing causes, hand-predict the allowed recovered key/sequence/manifest state under the declared durability model and design a test that discriminates them. Apply a minimal justified repair or conservative refusal, and run independent failing/previously correct regressions using the same engine. This evaluates **SYS5-O14 unfamiliar recovered-state diagnosis and defense**; a variable one-case task cannot automatically re-evaluate separate format, file-sync, index, integrity, test-harness and full-engine outcomes.
  - **Criteria:** The learner reconstructs a source- and model-consistent failure order, identifies the first violated storage invariant and distinguishes an actually lost acknowledged durable write from permitted unacknowledged persistence and deliberate corruption refusal. A discriminating observation supports one of at least two plausible explanations, and any repair or bounded refusal is justified against an independently derived recovery oracle. Regressions protect previously correct behavior and label simulated versus observed faults and filesystem assumptions honestly; the defense establishes individual understanding rather than familiarity with a rehearsed trace. **O2/O3/O5/O9/O10/O12 still require separate AS1–AS4 decisions**, not automatic credit from a selected AS5 scenario.
  - **Evidence:** New challenge/seed and prior predictions, independent operation and file-generation oracle, failing byte/state trace, cause discrimination, patch or justified quarantining decision, repeated reopen/regression logs, remaining assumptions and reviewable written, recorded or live defense.

### Academic boundaries, safe experimentation and scope

[SEF7](../SEF/SEF7.md) assesses foundational POSIX file work; [SYS2](SYS2.md) assesses Rust ownership, byte I/O and fallible resource cleanup; [SYS3](SYS3.md) assesses concurrency invariants and bounded workers; [SYS10](SYS10.md) explains kernel file/device pathways. SYS5 uniquely verifies an application's *persistent engine*, including log acknowledgment, crash replay, segment/index/manifest consistency, tombstones, reader generations, bounded space and honest measurement. [SYS6](SYS6.md) later combines local durability with networked replication/consensus and cross-node client-operation identity; [SYS7](SYS7.md) performs deeper production performance inference. APP relational SQL, sharding, multi-node failure recovery, general transactional databases, mandatory C/Rust unsafe FFI and specialty cryptographic storage are outside required SYS5 scope.

All destructive tests must be within clearly owned temporary directories, never on personal files, running databases, raw block devices or public systems. Any toolchain and fixture must be available without payment or privileged host access; no real power failure, offline block-device mount or special filesystem privilege is mandatory. Full application-specific encryption, authenticated integrity, resistance to malicious filesystem writers and secure erasure remain **explicitly out of scope**, not properties accidentally provided by CRC, Rust safety, deletion or compaction.

### Assessment revisions, provenance and readiness

Stable learning outcome IDs **SYS5-O1–SYS5-O14** and summative assessment IDs **SYS5-AS1–SYS5-AS5** remain unchanged. The consolidation removes duplicate recovery-oracle, file-order and capstone-integration instruction without removing WAL/manifest/snapshot or measurement competencies. AS2 explicitly distinguishes incomplete final tails from fully present checksum-invalid records, while AS5 now evaluates O14 without overclaiming six unrelated competencies from one optional-kind unseen case. These are **material assessment-clarity changes applying only to this revision**. Preserve historical learner assessments under their applicable course and OEE specification revision; do not retroactively award or withdraw completion through an editorial change. Each evaluation records actual test/failure setup, learner source revision, outcome/assessment IDs, expected vs observed states, reviewer decision and material environmental limitations. A passing CI pipeline or structurally conformant markdown source **does not** establish that this `draft` course has been learner-tested or independently verified.

## Optional disciplinary references

Public technical references aid investigation; they are not compulsory paid readings or hidden tests.

- [Rust std::fs::File and sync_all](https://doc.rust-lang.org/std/fs/struct.File.html) and [std::fs::rename](https://doc.rust-lang.org/std/fs/fn.rename.html) — explicit I/O, sync requests and platform-dependent publication boundaries.
- [SQLite — Atomic Commit](https://www.sqlite.org/atomiccommit.html), [How To Corrupt an SQLite Database](https://www.sqlite.org/howtocorrupt.html) — ordering assumptions, journal/recovery design, failure boundaries and why process-crash evidence differs from hardware behavior.
- [RocksDB — Write Ahead Log](https://github.com/facebook/rocksdb/wiki/Write-Ahead-Log) and [RocksDB Architecture](https://github.com/facebook/rocksdb/wiki/Rocksdb-Architecture-Guide) — conceptual LSM/WAL, manifests, sorted runs and compaction (not a mandate to duplicate a production database).
- [LSM deletion and tombstone retention research](https://doi.org/10.1145/3599724) — why deletion markers, read amplification and eventual reclamation can interact.
