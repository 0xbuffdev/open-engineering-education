# SEC3 — Systems & Binary Security

**Program:** SEC — Security Engineering
**Type:** `course`
**Prerequisites:** [SEC1](SEC1.md), [SEF6](../SEF/SEF6.md)
**Duration:** 10–14 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** approximately 10–14 focused hours/week (provisional; 100–196 hours)

> [Security Engineering](README.md) · [Design guide](../DESIGN-GUIDE.md) · [Course format](../../spec/course-format.md) · [Evidence rules](../../spec/evidence-rules.md)

## Overview

**Systems security asks how an error in a compiled program's memory or resource contract can cross a security boundary—and how to detect, prevent, and contain that crossing.** SEC3 investigates native C source and compiled artifacts as connected evidence. Learners reconstruct the relevant inputs, memory objects, lifetimes, binary assumptions and attacker influence; diagnose spatial, temporal and initialization defects; interpret compiler/debugger/sanitizer output without treating it as a formal proof; distinguish exploit preconditions from a crash; assess build/runtime hardening; implement secure C repairs; and defend a corrected decision under an unfamiliar bounded change.

**Context and relevance.** Native software underlies parsers, codecs, operating-system components, storage engines, client libraries and other high-impact trust boundaries. A length miscalculation may expose adjacent bytes; a write outside an object may corrupt state; a stale pointer may reference an object no longer owned; and a compiler/loader defense may interrupt one consequence without correcting the source. Memory-corruption weaknesses remain relevant in contemporary vulnerability taxonomies, but a weakness identifier, sanitizer message or successful process crash does not by itself prove a remote exploit, data theft or reliable code execution. Security conclusions depend on the specific program, input influence, object layout, target, mitigation state and evidence.

**Prerequisites and course ownership.** [SEC1](SEC1.md) establishes authorization, threat hypotheses, risk decisions and independent security test oracles. [SEF6](../SEF/SEF6.md) already teaches C11 syntax, representations, pointer bounds, lifetime, allocation failures, safe parsers, compilation and introductory debugger/sanitizer diagnosis. SEC3 does **not** repeat that foundation or require a second C data-structures portfolio: it adds adversarial root-cause analysis across the **source-to-binary boundary**, evidence-limited exploitability reasoning, mitigation assessment, security-specific repair and independent technical defense. [SYS1](../SYS/SYS1.md) provides deeper machine architecture and ABI/performance study, and [SYS2](../SYS/SYS2.md) teaches Rust, its ownership model and C/Rust interoperability; neither is a direct prerequisite. The minimal ABI, process-layout and safe-Rust concepts necessary to compare security claims are taught from supplied examples here. Practical Rust rewrites and FFI construction belong to SYS2 and are not required for SEC3. SYS3 owns advanced concurrency/memory-order reasoning; SEC4 owns operational host/network hardening.

**Reference environment and accessibility.** Use a nonprivileged, isolated local C11 toolchain with Clang or GCC, a free debugger and a binary-inspection tool on a declared target and ABI; GNU/Linux ELF on x86-64 or AArch64 is a useful reference. Equivalent free tools and supported targets are acceptable if the same security observations can be demonstrated and the target-specific rules are made explicit. For platform features unavailable to the learner, provide authentic, labeled source, compiler output, debug/symbol information and binary metadata from a **named** reference target so an assessor can evaluate equivalent reasoning. Required source fixes and regression tests must still be built and executed on an accessible local toolchain; optional hardware counters, privileged tracing, containers, custom kernels, public networks, proprietary reverse-engineering tools or a Rust compiler are not prerequisites. Declare the compiler and sanitizer versions, optimization/debug flags, target triple, ABI, OS and any supplied observations material to conclusions.

**Safe investigation.** All active work must be scoped to self-authored or supplied intentionally vulnerable local programs, disposable input files and synthetic data. No live third-party binary, privileged process, production service, real secret, persistent payload, shellcode, exploit chain, unauthorized memory probing or target compromise is required. A controlled and instrumented crash, a source-level proof of an invalid operation, or a supplied credible diagnostic trace can establish a defect; do **not** require learners to execute undefined C behavior merely to produce a dramatic crash. In particular, executing invalid pointer dereferences or signed overflow outside a diagnostic fixture is not an acceptable teaching oracle. A process completing normally does not establish the absence of undefined behavior, and a process aborting does not prove exploitability. Assessments require repaired programs with defined behavior and independently checked invalid, boundary and failure cases.

**Workload and evidence.** The provisional 10–14 weeks at 10–14 focused hours/week covers investigation of distinct memory mechanisms, trace interpretation, binary/build comparison, hardening limitations, source remediation, controlled fault injection and independent defense. One or two small versioned C components and a curated trace set may be reused across assessments; do not build a succession of disconnected vulnerable applications just to fill assignments. Four summative assessments evaluate distinct evidence contracts. All other lesson investigations and formative checks are optional unless their substance is explicitly required below. Duration and lesson completion do not establish mastery; the course remains `draft` pending qualified review and empirical calibration.

## Learning outcomes

- **SEC3-O1:** Establish authorized scope and a reproducible native-program security baseline, including input/privilege boundaries, build configuration, declared architecture/ABI, program behavior and independently expected protected-state outcomes.
- **SEC3-O2:** Identify and causally analyze spatial memory errors in stack, heap and aggregate objects, including out-of-bounds read/write, pointer arithmetic, object size and invalid string/record assumptions, without inferring defined effects from undefined behavior.
- **SEC3-O3:** Diagnose security-relevant integer conversion, overflow/wraparound, truncation and allocation-length mistakes; derive checked size and length invariants that hold at relevant boundary, malformed and failure inputs.
- **SEC3-O4:** Analyze temporal memory and ownership failures, including use-after-free, double release, stale aliases, realloc ownership and mismatched allocation/free contracts, and specify a safe lifetime/cleanup repair.
- **SEC3-O5:** Investigate uninitialized, stale and unintentionally disclosed native data or state, distinguishing actual initialization and object-lifetime evidence from speculative information exposure or a single diagnostic result.
- **SEC3-O6:** Use C source inspection, reproducible compiler output, debugger traces and appropriately available AddressSanitizer/UndefinedBehaviorSanitizer or supplied diagnostic evidence to localize a defect, reconcile contradictory observations and state tool coverage/false-confidence limits.
- **SEC3-O7:** Relate a named target's C source constructs to relevant compiler output, symbols, calling convention, object layout and stack/heap/segment evidence, distinguishing language, compiler, loader, operating-system and ABI guarantees without assuming a single portable binary layout.
- **SEC3-O8:** Examine build/runtime defenses such as ASLR, nonexecutable mappings, stack-protection checks, position-independent executables, relocation protections and sanitizer instrumentation; verify what a selected defense is configured to do and which source-level defects remain.
- **SEC3-O9:** Evaluate realistic preconditions, reachability, attacker-controlled data, plausible security impacts and uncertainty for native weaknesses, distinguishing demonstrated memory errors, potential exploitability and unsupported claims of reliable compromise.
- **SEC3-O10:** Implement and verify minimal effective, defined-behavior C repairs with explicit bounds, validated sizes, ownership and initialization contracts, failure-safe output state and independent security regressions that preserve valid behavior.
- **SEC3-O11:** Compare C11 safety obligations with supplied safe Rust ownership/bounds examples, compiler-rejected alternatives and unsafe/FFI boundaries, explaining the guarantees gained and the remaining logic, resource, panic and foreign-code risks without requiring a Rust rewrite.
- **SEC3-O12:** Produce an actionable, reproducible and evidence-limited native-security finding and independently diagnose and defend a previously unseen bounded variant, correcting hypotheses when observed data contradicts them.

## Modules

### Module 1 — Native Security Boundaries and Reproducible Evidence

#### Outcomes

- SEC3-O1
- SEC3-O6
- SEC3-O9

#### Lessons

1. **From C correctness to security consequence** — Start with a supplied parser or record service whose legitimate inputs and protected state are specified. Identify the untrusted byte/size/operation boundary, the actor who controls it and the protected object or decision. Compare a correct functional test, a vulnerable source path and a security claim, rejecting the inference that ordinary execution means memory safety.
2. **Permission, isolation and consequence classification** — Document the training program, permitted runs, synthetic inputs, output files, resource caps, cleanup and stop rules. Contrast a crash affecting only a disposable process, a plausible local information exposure and an unsupported remote-control assertion. Map the evidence and assumptions each conclusion would require.
3. **A named target and reproducible build** — Record C language mode, compiler/runtime version, warnings, optimization/debug/sanitizer switches and target ABI. Rebuild a small corrected or known-defined fixture on a supported local toolchain and compare observable results with independent expectations. Explain why different flags or targets may make undefined operations appear different without changing their C-language invalidity.
4. **Source, trace and finding quality** — Inspect a short credible diagnostic report and source excerpt; distinguish faulting access, earlier root cause, suspected corrupted state and secondary abort. Propose a discriminating safe observation and label any source/trace mismatch rather than forcing a known CWE category.

*Optional formative feedback:* Reconcile a clean ordinary run with a sanitizer report from a differently instrumented build, listing which facts both observations establish.

### Module 2 — Spatial Memory and Length/Arithmetic Invariants

#### Outcomes

- SEC3-O2
- SEC3-O3
- SEC3-O6
- SEC3-O10

#### Lessons

1. **Bounds of C objects and views** — Derive the valid index and one-past boundary for a fixed array, allocated buffer, pointer/length slice and structure member from actual object extents. Distinguish a write beyond one subobject, a whole-allocation boundary and a logically invalid but in-bounds write; predict security effects only conditionally.
2. **Out-of-bounds reads and data disclosure** — Trace an input length into a read, copy, slice or string scan. Contrast missing terminators, off-by-one checks and a parser that reads beyond a supplied byte count; identify which nearby data could theoretically be exposed and what observation would be needed before claiming disclosure.
3. **Out-of-bounds writes and corrupted invariants** — Analyze a provided defective copy/append path using declared stack or heap objects. Identify where a length/offset/terminator operation exceeds the destination and why subsequent behavior is undefined; do not attempt a return-address overwrite or executable payload. Specify a denial or truncation policy that prevents the invalid write.
4. **Integer arithmetic before allocation or copying** — Compare signed/unsigned conversions, count × element-size multiplication, header + body addition, subtraction underflow, narrow casts and negative input handling. Compute maximum legal lengths using stated integer limits, design checked arithmetic and reject ambiguous overflow behavior even when a nearby guard appears to pass.
5. **A bounded parser with independent oracles** — Reconstruct an explicit-length text or binary record format with maximum size, EOF/truncation and output-state rules. Repair a defective parser without introducing an undefined operation; test exact-boundary, oversized, malformed, zero-length, arithmetic limit and allocation-failure inputs using expected values derived from the published format.

*Optional investigation:* Hand-derive the smallest malformed input that violates a declared length invariant, then verify the repaired program rejects it without reading or writing outside its permitted buffer.

### Module 3 — Temporal Safety, Initialization and Ownership

#### Outcomes

- SEC3-O4
- SEC3-O5
- SEC3-O6
- SEC3-O10

#### Lessons

1. **Ownership over a program lifetime** — Trace creation, borrowing, transfer, mutation and release for a heap buffer, linked object and callback-held reference. State the exact event after which a pointer is no longer a valid access path, including when a container frees child allocations or retains an alias.
2. **Use-after-free and stale alias reasoning** — Inspect source, lifetime timeline and a labeled diagnostic of a freed object subsequently referenced. Distinguish a dangling pointer value from an actually demonstrated invalid access, and reject the suggestion that nulling one alias removes other stale references. Repair ownership rather than relying on heap layout luck.
3. **Reallocation and failure-safe state transitions** — Compare successful and failed `realloc` behavior, original pointer ownership, temporary result handling and capacity invariants. Show how direct assignment or duplicated release can lose an allocation or create temporal invalidity; design an atomic update and test injected allocation failure without actually dereferencing freed storage.
4. **Double release and cleanup under partial failure** — Model multi-resource initialization with a state table showing which resources are live after each failing step. Design one authoritative cleanup path or explicitly owned independent releases, and demonstrate that repeated error handling neither leaks ownership nor frees the same allocation twice.
5. **Uninitialized/stale data and exposure claims** — Analyze a structure with padding, a partial read, an uninitialized output field or a reused buffer. Distinguish observable initialized bytes from unspecified/indeterminate data and from a reported leak of actual secrets; repair by explicit initialization and length-safe copying, and independently check output redaction and failure-state invariants.

*Optional formative feedback:* Given a cleanup flow with two partial allocation failures, identify stale aliases and required safe states without executing invalid frees.

### Module 4 — From Source to Binary and Diagnostic Limits

#### Outcomes

- SEC3-O1
- SEC3-O6
- SEC3-O7
- SEC3-O9

#### Lessons

1. **Toolchain stages and target-specific contracts** — Trace source, translation unit, object file, linker, loader and runtime on a named reference target. Distinguish portable C constraints from actual compiler optimizations, symbol visibility and calling conventions; give an explicit ABI before explaining stack-frame or return-address location.
2. **Binary layout and protective boundaries** — Interpret file headers, segment permissions, relocation/dynamic metadata and relevant symbols from real or supplied ELF/target-equivalent output. Separate file sections from loaded memory segments and dynamic allocations; do not present one diagram as a universal memory map.
3. **Source-level statements and machine observations** — Connect an ordinary C function, local object and call to bounded debugger/disassembly observations for an actual compiled **defined-behavior** fixture. Compare a debug build with an optimized build, explaining variable elision, inlining and frame differences without requiring detailed SYS1-level performance analysis.
4. **Sanitizer reports and their blind spots** — Correlate an AddressSanitizer report, an UndefinedBehaviorSanitizer diagnostic and a warning/static-inspection result to source conditions. Explain instrumentation scope, false negatives, runtime/version limitations and why absence of a finding is not proof. Use genuine reports where supported and supplied target-identified traces where tooling is unavailable.
5. **Causal vulnerability and risk argument** — For two competing explanations of an anomalous native trace, derive the earliest invalid operation, attacker preconditions, reachability and plausible integrity/confidentiality/availability harm. Distinguish CWE weakness naming, an observed defect, a security impact and a reliable exploitability claim; choose the safe next diagnostic that could disprove the preferred explanation.

*Optional investigation:* Compare an instrumented heap diagnostic with an optimized disassembly excerpt from a different build; state what cannot safely be inferred across them.

### Module 5 — Runtime/Build Defenses and Security Limits

#### Outcomes

- SEC3-O7
- SEC3-O8
- SEC3-O9

#### Lessons

1. **Preventing a defect versus impeding consequences** — Separate source-level bounds and lifetime invariants, instrumented test-time detection, compiler-added runtime checks, process mapping policy and privilege isolation. Classify which layer can prevent, detect, abort or only constrain a hypothetical corruption consequence, and identify failure behavior after a triggered check.
2. **Address-space randomization and position independence** — Explain ASLR's conditional address unpredictability and the role of PIE/shared-library placement under a named loader/OS. Inspect supplied or locally produced binary metadata and appropriately controlled safe process observations. Do not claim randomization corrects an out-of-bounds write or measure security from a handful of address samples.
3. **Nonexecutable memory and stack checks** — Interpret executable versus nonexecutable process mappings and stack-protection instrumentation on declared builds. Explain why NX/DEP constrains execution from data pages and a canary can detect selected stack corruption paths, but neither prevents all memory errors, data-only corruption or every redirection scenario.
4. **Relocations, hardened builds and compatibility** — Inspect relevant RELRO/binding and compiler hardening settings, separating link metadata from what a loader actually enforces. Compare tool-supported `-fstack-protector-strong`, PIE and relocation-protection choices **only on compatible platforms**. Explain build costs, architecture variability and which protections cannot be established from a file header alone.

*Optional formative feedback:* Rank three statements—"ASLR enabled", "ASan test passed", and "bounds are checked before writing"—by what each establishes about a specific defective copy operation and what remains unproven.

### Module 6 — Secure Repair, Memory-Safe Design and Independent Defense

#### Outcomes

- SEC3-O1
- SEC3-O3
- SEC3-O4
- SEC3-O5
- SEC3-O8
- SEC3-O9
- SEC3-O10
- SEC3-O11
- SEC3-O12

#### Lessons

1. **Minimal root-cause repair and fault handling** — Replace a defective size, ownership or initialization boundary with a precise API contract, checked arithmetic and defined failure results. Preserve legitimate input and cleanup behavior; verify that a sanitizer disappearance is backed by independent normal, boundary, malformed and failure-state expectations.
2. **Comparing C and safe Rust guarantees** — Examine supplied side-by-side C and safe Rust buffer/ownership examples, including representative compile-time borrow errors. Explain which use-after-free/alias operations safe Rust rejects and when checked indexing returns an error or panics; safe Rust does not guarantee correct authorization, no panic, bounded resource use or freedom from all logic defects. No Rust compiler or Rust implementation is required for assessment.
3. **Unsafe and FFI trust boundaries** — Reason from a provided small Rust `unsafe`/FFI wrapper and C signature about validity, aliasing, alignment, lifetime and allocation ownership. Explain why declaring an unsafe block does not discharge its invariants and why a sound safe interface must prevent safe clients from triggering undefined behavior. A live C-to-Rust port or new FFI layer remains an optional extension following SYS2 preparation.
4. **Repair sensitivity and boundary changes** — Demonstrate that a regression check fails for a safely reintroduced logical guard mistake or an equivalent supplied defective trace; do not reintroduce undefined operations into production-grade submissions. Challenge repairs under altered count limits, object lifetime, optimization level, caller assumptions or build settings, and distinguish observed from modeled results.
5. **Unfamiliar native-security investigation** — On a previously unseen but bounded C component or supplied binary/diagnostic, predict the failure path, eliminate a competing explanation, implement an independently testable repair and select proportionate defense-in-depth. Explain risk, security properties, affected evidence, compiler/ABI assumptions and residual unknowns in developer and risk-owner terms without relying on exploit payloads.

*Optional investigation:* Reconstruct a supplied Rust compile-fail ownership example and compare the closest C lifetime contract; implement a safe Rust rewrite only if SYS2-level language preparation is already available.

## Completion requirements

**Four required summative evaluations** jointly establish all SEC3 outcomes; they may share a local versioned C parser/library, its independent test harness and curated diagnostic fixtures. A supplied trustworthy vulnerable trace plus source-level analysis may establish the original defective path where directly executing undefined behavior is unnecessary or unsafe, but the learner's **repaired** implementation and its regression behavior must be reproducibly exercised. A reviewer must separately judge each stated criterion and source-level reasoning; copying sanitizer output or naming an exploit mitigation alone cannot pass. No other exercises are mandatory.

- **SEC3-AS1** — Spatial Memory and Checked-Length Security Repair
  - **Outcomes:** SEC3-O1, SEC3-O2, SEC3-O3, SEC3-O6, SEC3-O10.
  - **Work:** Inspect a learner-owned or supplied small C11 binary/text parser or record-copy component with one spatial error and one size/conversion error on an authorized synthetic input path. Use source analysis and an authentic, labeled sanitizer/compiler trace or equivalent bounded observation to explain the failure preconditions without asserting defined behavior for an invalid C operation. Derive permitted records and size maxima independently; implement a defined-behavior repair covering length checks, overflow-free allocation arithmetic, destination extents and output state. Exercise valid, exact-boundary, malformed/truncated, extreme-length and injected allocation-failure inputs and demonstrate that the original assertion would fail when the guard is deliberately weakened in a non-UB test seam.
  - **Criteria:** The initial model names the owned input, target object, declared ABI/build and specific failing invariant. Both distinct defect mechanisms are demonstrated by reproducible source/trace reasoning, not merely a suspicious C function name. The repaired code cannot perform the invalid operation on assessed inputs, rejects unsupported lengths before access/allocating, preserves all permitted data and has deterministic failures without stale output or leaks. Expected outputs precede execution; a test actually distinguishes a protective guard from a safely weakened alternative. Diagnostic limits and untested inputs are stated.
  - **Evidence:** Bounded permission/fixture declaration, C source and build instructions, annotated credible source/diagnostic correspondence, independently derived size/boundary table, repaired code diff, reproducible normal/negative/fault tests with observations, and limited security conclusion.

- **SEC3-AS2** — Lifetime, Cleanup and Data Disclosure Review
  - **Outcomes:** SEC3-O2, SEC3-O4, SEC3-O5, SEC3-O6, SEC3-O10.
  - **Work:** Analyze a local owner/borrower/cleanup component with a stale alias or double-release path and an additional partial-initialization or output-disclosure condition. Provide an explicit lifetime timeline and a credible source/static/instrumented diagnostic of the unsafe path, without requiring uninstrumented undefined behavior. Repair ownership transfer, cleanup and initialized output state. Exercise two different partial-failure points, repeated valid operations, invalid transitions and synthetic output redaction, and compare the protected state before and after repair.
  - **Criteria:** The learner identifies the earliest invalid lifetime or initialization decision and every retained alias or output path affected; merely setting one pointer to null is not credited as a complete ownership fix. Corrected resources are released exactly according to declared contracts, error paths neither reuse freed storage nor duplicate release, and all returned bytes are intentionally initialized. Regression cases distinguish correct cleanup from one deliberately weakened guard in a safe test fixture. No confidentiality exploit is claimed without an actual information-flow observation.
  - **Evidence:** Ownership/state table, annotated source and trustworthy diagnostic or provided trace, fixed implementation/diff, independent expected outputs for normal and injected-failure paths, reproducible tests, redacted data-flow evidence and explicit limits.

- **SEC3-AS3** — Compiled Artifact and Mitigation Assessment
  - **Outcomes:** SEC3-O1, SEC3-O6, SEC3-O7, SEC3-O8, SEC3-O9.
  - **Work:** With a declared target/ABI and a small local **defined-behavior** C program, inspect source, binary symbols/segments, and at least two genuine build configurations or supplied target-identical comparative artifacts that differ in relevant hardening/instrumentation. Trace a relevant function/data access to a compiled observation and compare the configured behavior/constraints of ASLR/PIE, nonexecutable memory, stack protection or relocation protection. Analyze a provided credible defective case, separate vulnerability preconditions from observed faults and plausible harm, and recommend hardening without disabling host safety to prove a bypass.
  - **Criteria:** The artifact's target, compiler/linker options, loader/OS assumptions and provenance are explicit; binary facts are consistent with source observations and actual tools, with sections/segments and compiler-versus-OS roles correctly distinguished. At least two independently evidenced defense configurations are evaluated, and the report accurately specifies which layer prevents, detects, aborts or constrains what consequence. Neither sanitizer success nor compiler hardening is offered as proof of memory safety; claims of exploitability are qualified by attacker influence, reachability and missing evidence. The inspected safe program executes normally under declared assumptions.
  - **Evidence:** Build/provenance notes, safe local source and executable reproduction or authentic labeled binary excerpts, target/ABI-appropriate disassembly/metadata, hardening comparison and source-to-observation annotations, independent expected behavior, tested or declared limitations, and measured/specified risk conclusions.

- **SEC3-AS4** — Unfamiliar Native-Security Repair and Technical Defense
  - **Outcomes:** SEC3-O1, SEC3-O3, SEC3-O4, SEC3-O5, SEC3-O7, SEC3-O9, SEC3-O10, SEC3-O11, SEC3-O12.
  - **Work:** Diagnose a previously unseen bounded C source component with an additional supplied source-to-binary or sanitizer trace and an altered size, cleanup or initialization assumption. Predict failure and choose a competing explanation **before** viewing a discriminating observation. Repair the actual root cause and reproduce clean normal, invalid and relevant fault-injection behavior. On a separate **supplied** C/safe-Rust pair and an unsafe/FFI boundary excerpt, explain which guarantees would change under a sound safe-Rust design and what security obligations remain; no Rust code submission or toolchain is needed. Provide a concise developer finding, credible risk decision and individual defense, including corrections to an initially wrong hypothesis if necessary.
  - **Criteria:** The prediction distinguishes C-language invalidity, observed diagnostic evidence, target-dependent binary behavior and actual attacker reachability. The patch enforces a verified and precise invariant rather than hiding the failing symptom; the learner explains why negative and failure-path tests would expose a reintroduced weakness. The C/Rust comparison correctly states ownership and bounds guarantees, the possibility of safe indexing panics, logic/resource errors and the unsafe/FFI contract; it neither claims all Rust code is immune nor presumes prior SYS2 completion. The independent defense demonstrates the reasoning behind the remedy, residual exposure and any unproven exploit claims, and handles a reviewer-provided variation.
  - **Evidence:** New bounded case and authorized scope, independently stated prediction/counter-hypothesis, trace and source/binary analysis with assumptions, repaired build and tests, annotated C/Rust safety comparison, concise developer/risk-owner report, and reviewable written/recorded/live defense with remaining uncertainty.

### Assessment evidence and readiness

Each summative record identifies the course revision, evaluation ID, required outcome IDs, inspected evidence and assessor decision. Include exact tool versions, target/ABI and build flags when needed to interpret diagnostics or binary differences, and reproducible steps from a clean local state for all coded repairs. Supplied trace evidence must identify the producing tool, target and relevant conditions; do not present an invented or synthetic trace as an actual observation. Reviewers must distinguish observed results, source-level deductions and assumptions. Do not publish third-party secrets or raw memory from other users.

No mandatory exploit construction, vulnerable binary deployment, real malware, shellcode, executable undefined-behavior experiment or Rust implementation is required. A successful sanitizer run, hardened ELF metadata or absence of a crash does not amount to a proof that a binary is secure. The course remains `draft` until the [course readiness rules](../../spec/status-labels.md) are met through qualified review and learner evidence.

### Optional disciplinary references

- [MITRE CWE Top 25 2025](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25) and [CWE-787](https://cwe.mitre.org/data/definitions/787.html), [CWE-416](https://cwe.mitre.org/data/definitions/416.html) — weakness and root-cause categories, not proof of exploitability.
- [SEI CERT C memory management](https://cmu-sei.github.io/secure-coding-standards/sei-cert-c-coding-standard/rules/memory-management-mem/) and [integer safety](https://cmu-sei.github.io/secure-coding-standards/sei-cert-c-coding-standard/rules/integers-int/) — memory/lifetime and integer contracts.
- [Clang AddressSanitizer](https://clang.llvm.org/docs/AddressSanitizer.html) and [UndefinedBehaviorSanitizer](https://clang.llvm.org/docs/UndefinedBehaviorSanitizer.html) — observed instrumented checks, coverage and limits.
- [OWASP C-Based Toolchain Hardening](https://cheatsheetseries.owasp.org/cheatsheets/C-Based_Toolchain_Hardening_Cheat_Sheet.html) and [GCC instrumentation options](https://gcc.gnu.org/onlinedocs/gcc/Instrumentation-Options.html) — build/runtime layers with target- and version-dependent support.
- [Rust Reference: unsafe](https://doc.rust-lang.org/reference/unsafe-keyword.html) and [undefined behavior](https://doc.rust-lang.org/reference/behavior-considered-undefined.html) — soundness limits of unsafe and FFI contracts.
- [CISA/NSA memory-safe-language guidance](https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4223298/nsa-and-cisa-release-csi-highlighting-importance-of-memory-safe-languages-in-so/) — memory-safe design as a preventive engineering strategy, not a claim of zero software-security risk.

All references are freely accessible aids and do not add hidden prerequisites or certification claims.
