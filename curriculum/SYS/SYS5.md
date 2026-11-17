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

1. **From SYS2 resources to storage semantics** — Use completed SYS2 Rust I/O and SYS3 ownership/synchronization as prerequisites. Explain why correct read/write calls and race-free memory access do not by themselves establish an engine's update, restart or durability contract.
2. **Public key-value API and state model** — Specify bounded get, put, delete and ordered scan over byte keys/values, including absent key, replacement, duplicate delete, invalid key and ordering rules. Draw a sequential reference map before implementing persistence.
3. **Visibility, acknowledgment and persistence** — Separate receipt, append, memory publication, successful sync, client acknowledgment and recovery after restart. Show a legal failure trace where an unacknowledged write survives and why the protocol must not promise it disappears.
4. **Crash and corruption failure classes** — Distinguish an ordinary API error, process termination, kernel crash, sudden power loss, silent bit corruption and hostile modification. State the modeled guarantees for each instead of treating a forced process exit as a power-loss simulation.
5. **Durable and weaker explicit modes** — Compare a selected durable-acknowledgment mode with an optional batch/no-sync mode. Explain which acknowledged writes are expected after restart *under the declared filesystem/device assumptions* and why the modes must not share a durability claim.
6. **Atomicity and consistency scope** — Define single-operation atomic update, ordered single-writer semantics and optional atomic batch as separate contracts; do not imply SQL transactions, multi-key isolation or distributed consensus merely because a WAL exists.
7. **Recovery prefix and ambiguity** — Model a sequence of acknowledged and unacknowledged versioned operations, including a crash between sync and response. Define acceptable recovered prefixes or states while rejecting loss of acknowledged durable operations in the reference failure model.
8. **Threat, privacy and test isolation** — Bound learner-owned fixture directories, file sizes, keys and logs; distinguish accidental checksum-detected corruption from malicious tampering, encryption, authorization and secure erasure. Never fault-inject against a real user database.

*Optional formative feedback:* Hand-solve an acknowledgment/restart timeline under durable and unsynced modes and identify which observed post-crash states are permitted.

### Module 2 — Binary Record Formats, Checked Parsing and Integrity

#### Outcomes

- SYS5-O2
- SYS5-O9
- SYS5-O13

#### Lessons

1. **On-disk grammar and byte-order choices** — Publish a versioned record layout with magic, type, sequence number, key/value lengths, bounded payload and checksum; declare the endian convention and canonical meaning of every field before generating code.
2. **Checked record arithmetic** — Use try_from and checked_add to verify offsets, length headers and file sizes before allocation or slicing; derive a corrupted maximum-length fixture that a naïve unchecked parser would mishandle.
3. **Record types and tombstones** — Distinguish a value record, delete marker, control record and optional end marker; enforce type-specific value-length constraints and the semantics of an empty value versus an absent key.
4. **Sequence identity and duplicates** — Specify monotonic per-engine logical sequence numbers and how replay treats repeated operation IDs or rewrites; distinguish an identical duplicate record from a conflicting same-sequence payload.
5. **Checksums and covered regions** — Define which header/payload bytes contribute to an accidental-error checksum, where the checksum is stored and what a mismatch means. Explain CRC collision limits and why it neither authenticates records nor protects against a malicious editor.
6. **Header and body truncation states** — Classify EOF at a record boundary, truncated header, truncated body and a checksum-failed *complete* record separately; prescribe a conservative parser/recovery action rather than skipping arbitrary bytes to find magic.
7. **Pages and block-layout comparison** — Model fixed-size pages, slotted-page offsets and sequential-log records to compare update locality, fragmentation and storage overhead without requiring a production page manager or raw direct I/O.
8. **Versioning and incompatible upgrades** — Design one forward/older-format rejection or explicit migration rule, including what happens when a record version is unknown; do not silently accept incompatible formats based on a magic-byte resemblance.
9. **Independent golden byte oracles** — Hand-derive exact bytes and checksum inputs for normal put/delete, empty value, maximum allowed length, invalid checksum, overflow, early EOF and unknown-version cases. Compare implementation output to independent fixtures.

*Optional formative feedback:* Review a deliberately corrupted binary header and calculate precisely why it must be rejected before a buffer allocation.

### Module 3 — File Synchronization, Directory Metadata and Publication Ordering

#### Outcomes

- SYS5-O1
- SYS5-O3
- SYS5-O4
- SYS5-O6

#### Lessons

1. **Userspace flush versus kernel writeback** — Trace BufWriter::flush, ordinary write and File::sync_all/sync_data (where supported) across userspace buffering, kernel dirty pages, filesystem metadata and device acknowledgment; avoid equating Drop with durability.
2. **Short I/O and persistent error handling** — Handle partial writes, Interrupted, disk-full and a failed sync before returning an acknowledgment; show why an I/O error may leave a partial physical/logical file and why retry may require recovery inspection.
3. **Rename scope and atomic namespace changes** — Explain atomic rename *visibility* under named same-filesystem rules, cross-directory or cross-filesystem limitations and why successful rename alone does not prove durable directory metadata after a crash.
4. **File data before name publication** — Design a write-temporary, flush/sync, rename and parent-directory synchronization sequence for a new immutable segment or manifest; declare the target filesystem and fallback behavior if directory synchronization is unsupported.
5. **Ordering across files** — Write a dependency graph showing the segment file must be safely published before a durable manifest references it and old files must remain until a new durable manifest is authoritative; test a bad order that could orphan live data.
6. **Crash-points in two-phase publication** — Trace failures before temporary file sync, after sync, after rename, before directory sync and after directory sync. Classify whether startup chooses the previous or next generation under explicit persistence assumptions.
7. **Naming, paths and atomic replacement limits** — Use learner-owned private fixture directories, collision-safe temporary names and restricted file creation. Distinguish a stable opened file handle from its changing pathname and a same-filesystem atomic name operation from a distributed atomic update.
8. **File/descriptors and cleanup ownership** — Revisit only the SYS2 resource notions needed for a storage transaction: explicit close/sync failure reporting, open-file handles, owned temporary artifacts and cleanup on rollback; avoid retesting elementary Unix API syntax.
9. **Fail-safe conservative fallback** — When host filesystem/OS assumptions are not verifiable, refuse an unsupported durability level or document a narrower one; no mandatory raw block-device or privileged power-failure experiment.

*Optional formative feedback:* Draw the ordering DAG for a new segment and manifest; identify the first incorrect publication step when a crash leaves a manifest pointing at an unsynced file.

### Module 4 — Write-Ahead Logging, Commit Decisions and Restart Replay

#### Outcomes

- SYS5-O1
- SYS5-O3
- SYS5-O4
- SYS5-O9
- SYS5-O10

#### Lessons

1. **Why a write-ahead log exists** — Contrast a primary append-only record store with a WAL protecting an in-memory memtable and immutable segments. State the authoritative replay range and why a write must not be acknowledged durable before the required log sync.
2. **Single-writer commit pipeline** — Specify validated operation → append fully framed WAL record → sync for durable mode → update visible in-memory state → reply. Analyze an error after the durable sync but before the reply as an **ambiguous unacknowledged** outcome.
3. **WAL sequence and commit boundary** — Order per-record operation IDs, record checksums, fsync decision and optional grouped acknowledgments; state whether a valid record beyond the latest acknowledged sequence is permitted to appear during recovery.
4. **Partial append and write failure** — Simulate short writes, no-space, interrupted transfers and a process stop between header and body bytes; ensure an incomplete tail is not treated as a complete committed operation.
5. **Idempotent replay with versions** — Rebuild the in-memory latest-version map by replaying valid operation records in sequence; make replay against an existing checkpoint idempotent using a declared applied-up-to sequence bound.
6. **Tail damage versus internal corruption** — Allow a carefully specified incomplete **final tail** to be truncated/rejected based on policy, while treating checksum/structure corruption *inside an earlier required record* as an error requiring refusal or explicit repair—not silent resynchronization.
7. **Ambiguous acknowledgments in oracle design** — Test crash after durable sync but before responding; the returned client outcome was never observed, yet recovery may legitimately include the operation. Require state-oracle checks that permit that ambiguity without allowing already acknowledged data to disappear.
8. **Checkpoint state and WAL retirement** — Describe a checkpoint generation that durably captures records through a known sequence, ensuring referenced segments and manifest are published and synced before older WAL extents may be retired.
9. **Repeated crash and restart convergence** — Inject a second process stop during replay or checkpoint cleanup; demonstrate that reopening the same files repeatedly neither duplicates work nor discards acknowledged versions.
10. **Fault hooks and publication trace ledger** — Install deterministic user-space hooks after append, sync, memtable publish, segment sync, manifest publish, directory sync and WAL retirement; log enough stage and sequence identity to reconstruct recovery decisions.
11. **Evidence versus physical crash guarantees** — Separate a simulated write tear, injected sync error and process termination from actual kernel crash or sudden power loss. Document why tests exercise algorithmic ordering and cannot establish every device/cache persistence behavior.

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
3. **Page-oriented B+tree search** — Trace root-to-leaf search using sorted separators, fanout and page reads under a stated page size, highlighting why a B+tree optimizes a different write/read pattern from an LSM structure.
4. **B+tree split, merge and locality** — Hand-simulate insert/split and delete/rebalance for a small supplied tree; derive additional writes and page references. This is **comparative reasoning**, not a mandate to build a second B+tree storage engine.
5. **Log-structured merge organization** — Explain write buffer, immutable sorted-table files, generation/level metadata and the read path merging newer and older runs, without promising RocksDB's exact production compaction semantics.
6. **Block and sparse-index metadata** — Design checked block offsets and length tables plus a bounded sparse key index for a sorted segment; use exact known byte fixtures to avoid trusting corrupted offsets from a malformed file.
7. **Bloom filters and negative evidence** — Construct or analyze one filter's bit count/hash parameters, false positives and memory cost; explain that a reliable negative requires a valid filter built for the right segment/version and a positive never proves membership.
8. **Range scans and merge order** — Perform an ordered k-way merge across memtable and multiple immutable runs with duplicate keys, latest sequence wins and tombstones suppressing older values; specify range endpoints and output count limits.
9. **Read and write amplification accounting** — Calculate an illustrative point-read file count, scan work, bytes written and storage overhead for two workload mixes; identify cache and compression/size limitations rather than treating one LSM configuration as universal.

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

1. **Sorted immutable segment file** — Specify an SSTable-like file with sorted unique or versioned keys, block data, checked index/footer locations and checksums; reject unsorted entries, overlapping invalid bounds and truncated blocks.
2. **Flush without losing WAL coverage** — Build a new immutable segment from a frozen memtable, safely write/sync its file and publish its presence before retaining or retiring WAL data. Show why a partially written segment cannot be read as live state.
3. **Manifest as authoritative generation map** — Define a checksummed, versioned manifest listing active segment IDs/order, sequence high-water mark and next-generation intent; distinguish an open segment handle from the current manifest's logical membership.
4. **Atomic manifest replacement protocol** — Write the next manifest to a separate file, flush/sync it, atomically rename under declared filesystem assumptions and sync the parent directory; retain the old valid generation through recovery.
5. **Startup selection and orphan cleanup** — Choose the valid published generation deterministically after crash; ignore or quarantine unreferenced temporary/new files and distinguish safe garbage collection from deleting still-live segments.
6. **Compaction version-selection proof** — Merge sorted runs using highest relevant sequence, preserve scan/point lookup equivalence and retain older versions when a visible snapshot or lower-level overlapping segment can still require them.
7. **Tombstone survival and deletion horizon** — Show a concrete case where dropping a tombstone exposes an older value (resurrection); permit deletion only when no older version can reappear and no supported snapshot requires it.
8. **Peak disk and temporary-space constraints** — Budget input and output files, temporary manifest, source retention and concurrent writes so compaction may refuse or pause safely when free-space budget is exhausted without deleting the last recoverable copy.
9. **Interruption before and after publication** — Inject failure during output file construction, sync, manifest write, rename, directory sync and old-file reclaim; reopen and verify active keys and tombstones against independent expected generations.
10. **Reader generations and safe reclamation** — Keep immutable segment generations pinned until readers release them; schedule deferred unlink only after durable new manifest and absence of consumers needing older files.
11. **WAL checkpoint truncation order** — Link compacted sequence coverage, durable segment/manifest publication and WAL retirement, verifying that replay never assumes a missing checkpoint record and that old WAL is not removed prematurely.

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
3. **Snapshot semantics with generation pinning** — Choose a bounded per-read or explicit snapshot taken at a documented sequence number; pin immutable files and relevant in-memory versions so a range scan sees a coherent set while writes/compaction continue.
4. **Tombstone and version retention for readers** — Derive which deletes and older values must survive until the oldest active snapshot has released its reference; do not allow compaction to reclaim data still needed by a live reader.
5. **Lock order and maintenance lifecycle** — Apply SYS3 lock-order and wakeup reasoning to writer, memtable, manifest and compaction work; keep blocking disk I/O outside inappropriate long-held critical sections under an explicit invariant.
6. **Batch atomicity versus unsupported transactions** — Describe a possible atomic batch with one commit marker or protected group, but make any implementation optional unless explicitly covered by selected API. Do not claim serializable arbitrary multi-key transactions from per-record append.
7. **Quota decisions for memory and disk** — Publish numeric limits on memtable bytes, key/value lengths, active snapshots, open segments/files, WAL growth, temporary compaction space and total on-disk footprint; prove an admission/failure policy at each cap.
8. **Disk-full and sync-failure recovery** — Ensure an error on a dirty write/flush/sync cannot be reported as a durable success and that an engine can fail closed or enter read-only mode without allowing a later write to silently overwrite an unresolved corrupt state.
9. **Operational privacy and access boundaries** — Describe OS file permissions, possible filename/backup data exposure, checksums versus authentication and the absence of built-in encryption or secure erase; keep logs from leaking key/value contents by default.

*Optional formative feedback:* With two long-running scans, a delete and compaction, show which generations remain pinned and the earliest safe reclaim event.

### Module 8 — Independent State Models, Crash Sweeps and Corruption Diagnosis

#### Outcomes

- SYS5-O1
- SYS5-O4
- SYS5-O9
- SYS5-O10
- SYS5-O13
- SYS5-O14

#### Lessons

1. **Reference state-machine before implementation** — Construct a small separately implemented or hand-computed map over put/get/delete/scan using sequence IDs, expected per-operation replies and declared commit semantics; prevent the engine from generating its own golden results.
2. **Deterministic operation histories** — Seed mixed reads/writes/deletes, duplicate keys and range queries across size limits; compare accepted visible results with the reference after every acknowledged operation.
3. **Enumerate persistence cut points** — Define a finite crash sweep over the WAL append/sync/memory publish, segment write/sync, manifest write/rename/directory sync and obsolete-file reclaim stages, with repeatable small fixtures.
4. **Unacknowledged versus acknowledged uncertainty** — Compute allowed recovered states for a crash before/after acknowledgment, preserving all acknowledged durable operations and allowing a synced-but-unacknowledged operation under the declared mode rather than insisting it disappear.
5. **Tail tear and internal corruption adversaries** — Inject partial final header/body, a checksum-invalid complete interior record, malformed sparse offset and corrupted manifest. Require explicit distinguishable recover, refuse, quarantine or supported repair outcomes.
6. **Fault seam independence** — Use injected short writes, ENOSPC, failed sync, permission denial and unexpected EOF through controllable adapters; explain where injected errors differ from real filesystem semantics and avoid fragile host-global fault injection.
7. **Process crash as a second layer** — For suitable finite tests, run the engine in a learner-owned subprocess and terminate it at a controlled stage, then reopen a fresh process. Disclose that process termination is not a power-loss or kernel-crash proof.
8. **Repeated reopen and idempotence oracle** — Reopen recovered stores multiple times without new writes, compare version/tombstone/manifest state and prove no additional effects, leakage or premature segment deletion across repeated recovery.
9. **Classify competing causes** — Diagnose a previously unseen discrepancy by distinguishing parser checksum, WAL boundary, sync ordering, manifest publication, index stale read and compaction tombstone bugs; propose a discriminating fixture before patching.
10. **Minimal repair and regression retention** — Fix or conservatively refuse one failure state, retain an independent negative oracle and rerun prior correct cases, documenting unobserved interleavings, platform assumptions and remaining recovery limits.

*Optional formative feedback:* Use a supplied failure-stage ledger to predict restart state, then identify whether wrong output comes from unsynced acknowledgment, index update or bad manifest publication.

### Module 9 — Performance, Write Amplification and Storage Capacity Evidence

#### Outcomes

- SYS5-O5
- SYS5-O6
- SYS5-O11
- SYS5-O12

#### Lessons

1. **Define a comparable workload contract** — Choose fixed put/update/delete/get/scan distributions and independent expected results; separate an in-memory baseline and durable/less-durable mode instead of equating different consistency guarantees.
2. **Dataset and cache controls** — State input key/value distributions, working-set bytes, file sizes, OS/page cache assumptions and cold-versus-warm limitations. Avoid asserting that opening a file or one initial run provides a truly cold-cache benchmark.
3. **Throughput and latency metrics** — Compute logical operations/s, bytes/s, per-operation latency and percentile estimates only when sufficient samples exist, recording units and sample counts. Compare accepted work, failures and flush operations honestly.
4. **Write/read/space amplification** — Measure or derive logical payload bytes, WAL bytes, segment/compaction bytes, pages or runs examined per lookup and temporary/steady disk usage; distinguish ratios from end-to-end filesystem device writes.
5. **Compaction scheduling tradeoffs** — Contrast no/size-triggered/level-style compaction in a small model with write amplification, read amplification, tombstone delay and temporary disk budget; avoid claiming one policy dominates every workload.
6. **Flush and synchronization cost** — Measure log-sync grouping under durable and weaker modes separately, explaining how batching changes acknowledgment latency, failure windows and reproducibility rather than advertising unsafe speedup.
7. **Concurrent reads and background maintenance** — Compare read latency with and without controlled compaction under the same correctness oracle, describing lock hold, I/O contention and scheduler noise from SYS3/SYS10.
8. **Repeatable data and uncertainty** — Keep at least five individual timed trial values per meaningful configuration; compute center/spread and note CPU, storage medium, filesystem, toolchain and background-process confounders without requiring perf or special hardware.
9. **Performance-informed engineering decision** — Defend one memory/disk/latency trade-off using measured evidence and explicit threat to durability or correctness, including a rationale for rejecting a faster configuration.

*Optional formative feedback:* Analyze a compaction workload where faster writes come from disabled sync and explain why it cannot be claimed as a same-guarantee performance improvement.

### Module 10 — Integrated Rust Storage Engine and Independent Defense

#### Outcomes

- SYS5-O1
- SYS5-O2
- SYS5-O3
- SYS5-O4
- SYS5-O5
- SYS5-O6
- SYS5-O7
- SYS5-O8
- SYS5-O9
- SYS5-O10
- SYS5-O11
- SYS5-O12
- SYS5-O13
- SYS5-O14

#### Lessons

1. **Scope one executable local key-value engine** — Deliver a bounded single-node get/put/delete/ordered-scan Rust library or CLI using owned disposable files, safe byte handling and a published single-writer/multiple-reader or narrower concurrency contract.
2. **Specify API and failure policies first** — Publish maximum key/value/record sizes, accepted request/response/errors, format versions, durable acknowledgment mode, unacknowledged ambiguity and unsupported transactions before integration.
3. **Integrate WAL and memtable without duplication** — Reuse the AS2 WAL/replay work to build visible committed state and a bounded sorted in-memory index, preserving exactly the same sequence and checksum oracle across restart.
4. **Publish sorted segments and checkpoint metadata** — Reuse AS3 sorted-table, manifest, tombstone and compaction artifacts; require a crash-safe dependency order linking WAL coverage, file sync, manifest generation and old-file reclamation.
5. **Readers, snapshots and maintenance** — Use explicit limited snapshot/reader lifetimes, no resurrection after delete, bounded concurrent reads and a safe policy for background compaction and out-of-space failure.
6. **Reproduce deterministic crashes and malformed data** — Run the AS2/AS3 tests plus the AS4 integration harness against normal and injected failure scenarios with independent expected states, including repeated reopen and invalid segment/manifest bytes.
7. **Document operation and resource budgets** — Publish cargo manifest/lockfile, stable rustc/edition/target and Linux/filesystem details, exact clean-checkout commands, numeric memory/disk/fd limits and privacy-safe diagnostics in a short runbook.
8. **Compare workload regimes without false durability claims** — Report separate durable and weaker-mode measurements with raw trials and uncertainty; validate useful work and highlight write/space amplification, compaction peak space and unsupported power-loss guarantees.
9. **Defend an unseen recovery defect** — Analyze a reviewer-supplied unknown WAL/manifest/compaction/snapshot failure with two hypotheses, a before-observation prediction, source-grounded minimal correction/refusal and independent positive/negative regression.

*Optional formative feedback:* Present a previously unseen crash just after directory sync but before WAL retirement, then prove the recovered acknowledged prefix and which files may be reclaimed.

## Completion requirements

**Exactly five summative evaluations cover SYS5-O1–SYS5-O14.** Module practice and supplementary reading are formative, not hidden gates. AS2 provides the WAL/recovery code, AS3 adds indexed segments/compaction, AS4 integrates and measures the **same engine**, and AS5 evaluates a novel failure on that base; no additional unrelated database implementation is required. Each distinct assessment still requires independently evaluated behavior, success criteria and evidence. A green build, a single successful restart or a benchmark chart alone does not establish crash safety.

- **SYS5-AS1** — Public Storage, Binary Format and Durability Contract
  - **Outcomes:** SYS5-O1, SYS5-O2, SYS5-O3, SYS5-O9, SYS5-O13.
  - **Work:** Specify `get/put/delete/scan`, sequential visible-state behavior, durable and optionally weaker acknowledgment semantics, a versioned binary record layout with bounded fields/checksum and a manifest-generation/file-publication ordering plan. Independently solve **at least five distinct histories or byte fixtures** covering successful write, sync-before-reply crash, final partial WAL record, interior corruption, and file/manifest rename plus directory-sync failure under stated Linux/filesystem assumptions.
  - **Criteria:** Valid and invalid bytes have exact independently computed outcomes with length arithmetic checked before allocation; magic/version/sequence/checksum/encoding fields and unknown-format policy are unambiguous. Committed/acknowledged writes must not be lost in the declared durability model, whereas synced-but-unacknowledged operations are not falsely asserted absent. File write, flush, sync_all/sync_data, rename and parent-directory sync are distinguished rather than treated as interchangeable durability proofs. Earlier committed-record corruption is not silently dismissed as trailing damage; checksum is not represented as authentication or secure erasure.
  - **Evidence:** API/state and failure-model specification, versioned grammar and byte-layout tables, five independent golden/invalid fixtures and hand-derived recovery histories, required ordering DAG, named environment assumptions, threat/retention limitations and rationale.

- **SYS5-AS2** — WAL, Acknowledgment and Replay Implementation
  - **Outcomes:** SYS5-O1, SYS5-O3, SYS5-O4, SYS5-O9, SYS5-O10.
  - **Work:** Implement the bounded Rust WAL append/checked parser/replay/recovery component used by AS4. Use deterministic fault hooks **before append, during partial append, after complete append, before sync, after sync but before reply, and during replay/checkpoint retirement**. Supply independent expected key/version sequences, distinct acknowledged and ambiguous operations, and repeated-reopen evidence; publish durable and any optional weaker sync mode separately.
  - **Criteria:** A durable acknowledgment is emitted only after the required successful sync under the declared model; partial/error paths fail visibly without silently acknowledging data. Replay accepts valid complete records in sequence, conservatively classifies the incomplete final tail, refuses/quarantines unexpected interior corruption rather than skipping it, and is idempotent across repeated restarts and checkpoints. Injected short I/O, disk full and sync errors have bounded outcomes. The independent oracle permits a correctly persisted unacknowledged operation but cannot accept missing acknowledged durable operations or double-application effects. Evidence never calls injected process crashes a proof of physical power-loss durability.
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
  - **Outcomes:** SYS5-O2, SYS5-O3, SYS5-O5, SYS5-O9, SYS5-O10, SYS5-O12, SYS5-O14.
  - **Work:** Investigate an **unseen** bounded storage failure supplied by a reviewer or transparent public variant generator: a torn tail, malformed internal log record, stale sparse index, dropped tombstone, manifest pointing at an unsynced segment, premature WAL retirement or reader/compaction generation hazard. Before running code, name **two competing causes**, predict expected recovered key/sequence/manifest state and design a discriminating test. Apply a minimal justified fix or safe refusal and run independent before/after regressions using the same engine.
  - **Criteria:** Reconstruct a source- and model-consistent failure order, identify the first violated invariant, distinguish loss of acknowledged durability from an allowed ambiguous unacknowledged write and from detected corruption, and defend why the correction restores the declared guarantee. Golden expectations derive from a separate state/operation history, not the student's output; tests protect previously correct cases and record actual versus simulated evidence. The learner identifies limits of injected crashes, filesystem assumptions, cryptographic integrity and portability without claiming universal proof after one passing scenario.
  - **Evidence:** New challenge/seed and prior predictions, independent operation and file-generation oracle, failing byte/state trace, cause discrimination, patch or justified quarantining decision, repeated reopen/regression logs, remaining assumptions and reviewable written, recorded or live defense.

### Academic boundaries, safe experimentation and scope

[SEF7](../SEF/SEF7.md) assesses foundational POSIX file work; [SYS2](SYS2.md) assesses Rust ownership, byte I/O and fallible resource cleanup; [SYS3](SYS3.md) assesses concurrency invariants and bounded workers; [SYS10](SYS10.md) explains kernel file/device pathways. SYS5 uniquely verifies an application's *persistent engine*, including log acknowledgment, crash replay, segment/index/manifest consistency, tombstones, reader generations, bounded space and honest measurement. [SYS6](SYS6.md) later combines local durability with networked replication/consensus and cross-node client-operation identity; [SYS7](SYS7.md) performs deeper production performance inference. APP relational SQL, sharding, multi-node failure recovery, general transactional databases, mandatory C/Rust unsafe FFI and specialty cryptographic storage are outside required SYS5 scope.

All destructive tests must be within clearly owned temporary directories, never on personal files, running databases, raw block devices or public systems. Any toolchain and fixture must be available without payment or privileged host access; no real power failure, offline block-device mount or special filesystem privilege is mandatory. Full application-specific encryption, authenticated integrity, resistance to malicious filesystem writers and secure erasure remain **explicitly out of scope**, not properties accidentally provided by CRC, Rust safety, deletion or compaction.

### Assessment revisions, provenance and readiness

Stable learning outcome IDs **SYS5-O1–SYS5-O14** and summative assessment IDs **SYS5-AS1–SYS5-AS5** remain unchanged, with deeper independent evidence and crash-state acceptance criteria applying to **this revision**. Preserve historical learner assessments under their applicable course and OEE specification revision; do not retroactively award or withdraw completion through an editorial change. Each evaluation records actual test/failure setup, learner source revision, outcome/assessment IDs, expected vs observed states, reviewer decision and material environmental limitations. A passing CI pipeline or structurally conformant markdown source **does not** establish that this `draft` course has been learner-tested or independently verified.

## Optional disciplinary references

Public technical references aid investigation; they are not compulsory paid readings or hidden tests.

- [Rust std::fs::File and sync_all](https://doc.rust-lang.org/std/fs/struct.File.html) and [std::fs::rename](https://doc.rust-lang.org/std/fs/fn.rename.html) — explicit I/O, sync requests and platform-dependent publication boundaries.
- [SQLite — Atomic Commit](https://www.sqlite.org/atomiccommit.html), [How To Corrupt an SQLite Database](https://www.sqlite.org/howtocorrupt.html) — ordering assumptions, journal/recovery design, failure boundaries and why process-crash evidence differs from hardware behavior.
- [RocksDB — Write Ahead Log](https://github.com/facebook/rocksdb/wiki/Write-Ahead-Log) and [RocksDB Architecture](https://github.com/facebook/rocksdb/wiki/Rocksdb-Architecture-Guide) — conceptual LSM/WAL, manifests, sorted runs and compaction (not a mandate to duplicate a production database).
- [LSM deletion and tombstone retention research](https://doi.org/10.1145/3599724) — why deletion markers, read amplification and eventual reclamation can interact.
