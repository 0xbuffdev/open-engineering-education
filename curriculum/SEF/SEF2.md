# SEF2 — Programming & Computational Thinking

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** [SEF1](SEF1.md)
**Duration:** 10–12 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–15 focused hours/week (provisional; calibrate with learner evidence)

> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Learn to build and reason about small programs from their behavior rather than memorize Python syntax. Start with the difference between source code, the Python interpreter and execution state. Prepare a terminal-based local workspace, then learn values, conditions, loops, functions, collections, files, errors, and debugging. Introduce user-defined classes, instance state, encapsulation and composition before explaining type annotations, their optional static interpretation, and the difference between a declared type and runtime input validation. Investigate mutation and file-integrity failures before combining these capabilities in a persistent command-line task manager.

Python 3.11 or later and its standard library are the reference teaching environment. Use Windows, macOS or Linux, a text editor, and an ordinary terminal; `python`, `python3` or `py` may be the working interpreter command. An alternative equivalent free local Python environment is acceptable if the submitted work remains reproducible. All required work is possible offline with no paid account, service, third-party package, administrator privileges, or real personal data.

This is a `course` in programming foundations, not the larger professional software-engineering capstone. Its six summative evaluations progressively combine skills and may reuse a learner's earlier artifacts, including the same persistent task-manager project for the final abstraction-and-typing investigation. The lesson sequence and optional practice provide preparation; **the required outcomes, assessments and evidence below determine completion**. A fixed number of quizzes, per-module labs or mandatory final lab is not imposed.

The 10–12-week duration is a revised provisional estimate reflecting two new foundational modules and reviewable abstraction/typing work, not measured learner time or a readiness claim. All work should use disposable project directories and fabricated input records.

## Learning outcomes

- **SEF2-O1:** Observe CPython source-to-execution behavior with an unfamiliar function and distinguish interpreter bytecode from CPU instructions.
- **SEF2-O2:** Prepare a portable local Python workspace, execute a program from the terminal, interpret its diagnostics, and reproduce its run.
- **SEF2-O3:** Predict and explain state, names, values, expressions, branches, and loop execution in an unfamiliar short Python program.
- **SEF2-O4:** Decompose a written behavior specification into testable functions using explicit parameters, returns, modules, conditions, and loops.
- **SEF2-O5:** Select and use appropriate Python strings and collections to process and summarize structured or unstructured records.
- **SEF2-O6:** Trace aliasing and mutation across function boundaries and enforce an explicit ownership and side-effect contract for nested data.
- **SEF2-O7:** Read, validate, transform, and serialize local text, CSV, and JSON data with explicit encodings and documented formats.
- **SEF2-O8:** Diagnose erroneous program behavior using a minimal reproduction, state observations, a causal hypothesis, a correction, and a regression test.
- **SEF2-O9:** Design file updates so invalid input or failed processing does not silently destroy a previously valid output, and explain the limits of replacement-based writes.
- **SEF2-O10:** Implement, test, and explain a persistent command-line application from a public behavioral contract, including predictable errors and cross-process behavior.
- **SEF2-O11:** Design and verify a small Python class with a constructor, instance attributes, methods and explicit state invariants, and use object composition where it improves domain responsibility without obscuring aliasing or mutation.
- **SEF2-O12:** Annotate Python function, parameter, return and collection types, including an optional value; distinguish annotations and optional static analysis from actual runtime enforcement, validation and exception behavior.

## Modules

### Module 1 — Software, Code & Languages

#### Outcomes

- SEF2-O1

#### Lessons

1. Course introduction: Programming & Computational Thinking
2. What software is
3. What coding is
4. What software engineering is
5. Programming languages
6. Source code
7. Interpreters and compilers
8. Bytecode and the virtual machine

*Optional practice:* Use a free local CPython interpreter and the `dis` module to compare an execution prediction with a real trace; explain an intentionally introduced syntax error.

### Module 2 — Your Workspace

#### Outcomes

- SEF2-O2

#### Lessons

1. The terminal
2. Installing Python
3. Code editors
4. The Python prompt
5. Running a file
6. Your first error

*Optional practice:* Install and select an interpreter, reproduce an invocation from a clean folder, and distinguish a missing interpreter from a script failure.

### Module 3 — Thinking in Programs

#### Outcomes

- SEF2-O3

#### Lessons

1. Programs as steps
2. Values and types
3. Expressions and arithmetic
4. Variables and state
5. Printing output
6. Tracing execution

*Optional practice:* Trace a sequence of assignments and prints by hand; explain why names bind to objects rather than containing copied values.

### Module 4 — Conditions & Loops

#### Outcomes

- SEF2-O3
- SEF2-O4

#### Lessons

1. Boolean expressions
2. If statements
3. While loops
4. For loops and ranges
5. Loop patterns, termination and edge cases
6. Iterables and iterators — Explain `iter()`, `next()`, exhaustion, and why a for-loop advances an iterator without assuming every iterable is a list.
7. Iteration helpers — Use `enumerate()` and `zip()`, including unequal lengths and their stopping behavior.
8. Comprehensions — Express a small transformation clearly and explain when an explicit loop is easier to read or debug.

*Optional practice:* Predict loop termination and boundary behavior, including empty input and a zero-iteration case.

### Module 5 — Functions & Decomposition

#### Outcomes

- SEF2-O4

#### Lessons

1. Defining functions
2. Parameters and arguments
3. Local variables and scope
4. Return values
5. Interfaces and decomposition
6. Modules and imports
7. Calls and defaults — Distinguish positional/keyword arguments, valid function defaults and the hazard of a shared mutable default.
8. Modules versus scripts — Explain importing without accidental execution and use a `__main__` entry point appropriately.

*Optional practice:* Refactor a short script into independently testable functions; compare its outputs before and after the refactor. Test an example where a mutable default unexpectedly retains data between calls.

### Module 6 — Strings & Collections

#### Outcomes

- SEF2-O5
- SEF2-O6

#### Lessons

1. Strings
2. Lists
3. Dictionaries
4. Tuples
5. Sets
6. Choosing a collection
7. Slices, membership and iteration — Explain sequence slicing, dictionary membership, insertion-order guarantees and why modifying a collection during iteration needs care.
8. Equality and hashing — Explain why mutable lists cannot be dictionary keys while immutable hashable tuples may be valid keys, without assuming every tuple is hashable.

*Optional practice:* Try word counting with lists, dictionaries, tuples, and sets; compare what each structure makes easy or difficult. Predict whether a sequence copy preserves nested aliases.

### Module 7 — Files & Data

#### Outcomes

- SEF2-O7

#### Lessons

1. Reading files
2. Writing files
3. Structured data
4. Directories and paths

*Optional practice:* Inspect UTF-8 local text, CSV, and JSON files in a disposable directory; compare expected and observed serialized types.

### Module 8 — Errors & Debugging

#### Outcomes

- SEF2-O8

#### Lessons

1. Reading tracebacks
2. Handling exceptions
3. Raising exceptions
4. Validating input
5. Debugging by evidence

*Optional practice:* Reproduce a traceable failure, fix the cause rather than hiding the exception, and add a regression case.

### Module 9 — Mutation & Function Contracts

#### Outcomes

- SEF2-O6
- SEF2-O8

#### Lessons

1. Names, objects, identity and equality
2. Mutable aliases and shallow copies
3. Nested collection behavior
4. Parameters, side effects and returns
5. Preconditions and assertions

*Optional practice:* Draw the object-reference graph for a nested-list alias and a shallow copy; test a function's non-mutation promise.

### Module 10 — Reliable Files & Input

#### Outcomes

- SEF2-O7
- SEF2-O8
- SEF2-O9

#### Lessons

1. Text encodings and newlines
2. CSV and JSON error handling
3. Exceptions versus result values
4. Safe file writes and temporary files
5. Boundary tests and CLI contracts

*Optional practice:* Practice rejecting duplicate IDs, malformed records, and failed writes without damaging an existing output file.

### Module 11 — Classes, Instances and Domain Abstractions

#### Outcomes

- SEF2-O4
- SEF2-O6
- SEF2-O11

#### Lessons

1. **Why create a class** — Compare plain functions and dictionaries with a small domain object whose data and operations belong together; avoid classes when they add no useful invariant.
2. **Defining a class and instances** — Explain a class definition, calling a class, the role of `__init__`, the meaning of `self`, and where individual instance state lives.
3. **Attributes, methods and object identity** — Predict attribute reads/writes, method calls, mutation through an alias and equality versus identity.
4. **Class versus instance attributes** — Diagnose shared mutable class attributes and build safely independent instance records.
5. **Initialization and invariants** — Establish nonempty identifiers, a Boolean completion field and valid transitions, rejecting invalid construction and updates.
6. **Encapsulation in Python** — Explain a public interface, underscore conventions, properties when justified and the fact that Python naming conventions are not enforceable security boundaries.
7. **Composition before inheritance** — Create one collection object containing task objects; compare delegation and responsibility with an unnecessary inheritance hierarchy.
8. **Representing and serializing state** — Translate domain objects into plain JSON-compatible values at an explicit boundary; distinguish object identity from persisted identifiers.
9. **Standard-library alternatives** — Compare a hand-written constructor with `dataclasses.dataclass` and recognize mutable-default hazards; do not mistake generated code for an absence of state contracts.
10. **Tests of an abstraction** — Verify constructor rejection, independent instances, invalid transitions, alias effects and compositional behavior on previously unseen cases.

*Optional practice:* Build a small `Task` and `TaskCollection` pair, predict behavior when two names reference the same task, and demonstrate why a global mutable task list weakens isolation. It is acceptable to retain a function-based CLI and use objects only where they reduce complexity.

### Module 12 — Type Annotations, Contracts and Runtime Behavior

#### Outcomes

- SEF2-O4
- SEF2-O8
- SEF2-O11
- SEF2-O12

#### Lessons

1. **Why type annotations exist** — Distinguish documentation and optional static checking from executable validation or automatic conversion.
2. **Basic parameter and result types** — Annotate `int`, `str`, `bool`, and `None` in function interfaces; distinguish a return value from an exception.
3. **Typed collections and classes** — Express `list[Task]`, `dict[str, Task]`, `tuple[str, int]` and nested data shapes appropriate to Python 3.11+.
4. **Optional values and unions** — Use `Task | None` only when absence is meaningful, handle both branches and explain why `None` does not mean an empty task.
5. **Annotations at runtime** — Inspect annotations with standard-library facilities and demonstrate a wrong-typed argument still reaches an annotated function unless code explicitly validates it.
6. **Static versus dynamic verification** — Explain the limits of optional external type checkers and why an untyped dependency, `Any`, casts and false assumptions can bypass static guarantees.
7. **Contracts and exception boundaries** — Validate untrusted CLI/JSON input and object invariants at runtime even if parameters are annotated.
8. **Typing and tests together** — Use independently checked normal, invalid and optional-value cases; demonstrate how annotations, tests and human review reveal different defects.
9. **Keeping annotations proportionate** — Preserve simple, readable interfaces without requiring advanced generics, protocols, metaclasses or any particular third-party analysis tool.

*Optional practice:* Annotate a function that finds a task and returns `Task | None`, then pass a wrong runtime type to prove the annotation does not validate input automatically. Compare the corrected explicit validation against a call that fails unexpectedly.

### Module 13 — Command-Line Task Manager

#### Outcomes

- SEF2-O4
- SEF2-O5
- SEF2-O7
- SEF2-O8
- SEF2-O9
- SEF2-O10
- SEF2-O11
- SEF2-O12

#### Lessons

1. **Command-line interface and arguments** — Define add/list/update/delete behavior and distinguish command parsing from domain operations.
2. **Tests as independent checks** — Use `unittest`, subprocess execution and expected persistent-state values, not just a green report.
3. **Logging and messages** — Produce controlled failures and user-facing output with useful exit status.
4. **Object boundaries** — Represent task records with coherent domain methods when appropriate, preserving a simple, usable CLI.
5. **Typed interfaces and runtime validation** — Annotate a public domain API while rejecting malformed persisted values and invalid commands explicitly.
6. **End-to-end reasoning** — Trace an unfamiliar lifecycle over two processes and defend storage, ownership, error and abstraction decisions.

*Optional practice:* Run a CLI through two independent processes, inspect persisted state, and explain one deliberate error path. Compare the same task manager with and without a coherent object boundary; avoid a class hierarchy that adds no value.

## Completion requirements

### Assessment environment and review

Required assessments may be performed locally using Python 3.11 or later and standard-library modules such as `dis`, `argparse`, `csv`, `json`, `pathlib`, `tempfile` and `unittest`. Record the interpreter implementation/version, platform, precise execution and test commands, and relevant assumptions. Use only synthetic records and disposable working directories. Source code and expected behavior must remain public and reviewable without a proprietary grader, paid account or private answer key.

For reproducible code, supply a source repository revision or portable directory snapshot, a README explaining the clean-start commands, representative positive and negative test results, and any material known limitations. For a conceptual explanation or state trace, provide a reviewable written, recorded, or other equivalent accessible explanation; reproducing a canned answer is insufficient where an assessment asks for reasoning about unfamiliar input. Reviewers may use different but equivalent unseen inputs under the same published criteria.

**Shared assessment decision:** Each assessment is passed only if its stated criteria are met and the evidence can be inspected. A failing test or an unresolved defect that violates a stated criterion cannot be compensated for by extra unrelated work. A small clarification or corrected submission can be reassessed against the same criteria. Effort, attendance, passive reading, an activity checkmark, or a screenshot of a green test alone does not prove the required outcome.

### Required summative assessments

- **SEF2-AS1** (required interpreter and execution investigation)
  - Outcomes: SEF2-O1, SEF2-O2, SEF2-O3
  - Work: In a fresh local directory, create and run a small Python script that computes a result using expressions, rebinding and a conditional. Before execution, provide a trace predicting the values, branch selected and displayed output. Then inspect an unfamiliar two-argument function with CPython's standard-library disassembly and explain source, compilation, bytecode execution and native machine instructions. Deliberately introduce a syntax error in a copy, capture and correct its diagnostic, and repeat the run.
  - Criteria: The clean-start invocation works using the documented interpreter; predicted state, branch and output agree with the code or a correction explains the discrepancy; the interpreter implementation and actual version are recorded; disassembly is interpreted by instruction role rather than assuming stable opcode names; CPython bytecode is not mistaken for CPU machine code; the intentionally invalid copy fails visibly and the repaired copy succeeds.
  - Evidence: Script and its edited failure case, interpreter/version and run commands, predicted-versus-observed trace, representative disassembly, a short source-to-output explanation, and error/fix transcript.
  - Review cases: The reviewer may replace a constant or branch input and ask the learner to predict the new trace; comparison is against the actual submitted program, not a memorized disassembly.

- **SEF2-AS2** (required function and collection program)
  - Outcomes: SEF2-O3, SEF2-O4, SEF2-O5, SEF2-O8
  - Work: Implement a small text-record summary from a written input contract: each nonempty line contains `name:count` with a nonempty name and a base-10 nonnegative integer count. Normalize names using `strip()` and `casefold()`, aggregate duplicate normalized names, and report total count, distinct-name count and names in alphabetical order. Separate parsing, aggregation and display into functions with explicit parameters and return values. Define what happens on a blank line, missing separator, missing name, negative count and non-integer count. Trace one supplied multi-line input by hand before running code, then deliberately introduce and repair a logic defect.
  - Criteria: Valid input is processed deterministically, equivalent names are aggregated, display ordering is stable, zero and empty datasets are handled according to the documented contract, and invalid records produce a predictable error without an unexplained crash. Function boundaries, loop/conditional behavior and data-structure choice are defensible. Tests expose the seeded defect, pass after the repair, and cover a normal case, repeated name, empty input and each stated invalid input class.
  - Evidence: Source and public input/output contract, state trace, runnable table of fixtures/expected results, standard-library tests with observed results, a before/after defect reproduction, and concise reasoning about function interfaces and collection choice.
  - Review cases: A reviewer may supply an unfamiliar mixture of repeated names and invalid counts and ask for the expected result or error before executing it.

- **SEF2-AS3** (required state-ownership and debugging investigation)
  - Outcomes: SEF2-O3, SEF2-O6, SEF2-O8
  - Work: Given two groups of tasks represented by nested lists, demonstrate how a shallow copy can share an inner list. Draw the name/object references and predict state before and after an append through one alias. Reproduce a surprising mutation in a minimal test, then implement a function that updates one group while leaving the caller's nested input unchanged. State and defend whether the function copies mutable members or creates fresh structures, and show how the revised contract affects repeated calls.
  - Criteria: The state predictions match observed nested values and object sharing; the learner distinguishes rebinding from mutation and shallow from nested copying. The failing case is independently reproducible. Corrected behavior changes only the intended returned data; input objects and unrelated groups remain unchanged across repeated calls, empty groups and multi-group cases. The explanation discusses why gratuitous deep copies may be undesirable.
  - Evidence: Minimal faulty and corrected code, object-reference diagram, before/after state observations, tests for repeated and boundary cases, and a short hypothesis/fix explanation.
  - Review cases: A reviewer may add a second shared nested list and ask the learner to identify which aliases would change under each implementation.

- **SEF2-AS4** (required reliable local data conversion)
  - Outcomes: SEF2-O7, SEF2-O8, SEF2-O9
  - Work: Implement a local CSV-to-JSON conversion function or command that accepts explicit input and output paths. The CSV header must contain `id` and `title`; records must have unique, nonempty identifiers and nonempty titles. Choose and document how extra columns and blank lines are handled. Use explicit UTF-8 for text, validate the complete input before changing an existing destination, serialize normalized records deterministically, and write to a temporary file in the destination directory before completing a successful replacement with `os.replace`. Simulate missing input, malformed CSV, invalid record, duplicate ID and a failed write or replacement.
  - Criteria: Valid CSV becomes parseable deterministic JSON with the documented schema and UTF-8 text intact. Every invalid source or simulated pre-replacement failure reports a controlled non-success outcome while preserving the exact bytes of an existing valid destination; temporary files are cleaned up when feasible. Exceptions are handled at a meaningful boundary without hiding unrelated bugs. The learner explains that an atomic replacement on the same filesystem is not, by itself, a guarantee of power-loss durability, and identifies any platform or permission limitations.
  - Evidence: Source, CSV and expected JSON samples, schema/validation policy, clean-run commands, normal and negative test results, exact before/after destination-byte comparisons, simulated failure record, and a concise data-integrity analysis.
  - Review cases: Include empty input, duplicate IDs, non-ASCII titles, missing fields and malformed encodings. Test file operations only on disposable paths, not pre-existing personal files.

- **SEF2-AS5** (required persistent command-line application)
  - Outcomes: SEF2-O2, SEF2-O4, SEF2-O5, SEF2-O6, SEF2-O7, SEF2-O8, SEF2-O9, SEF2-O10
  - Work: Build a Python standard-library task manager with `add`, `list`, `update` and `delete` commands, unique nonempty task IDs and titles, and an explicit Boolean completed state. Define command usage, arguments, JSON storage shape, data location, success output and nonzero error behavior. Separate domain operations from argument parsing and file I/O; persist records across separate processes. Use safe validation and file replacement principles from SEF2-AS4, and avoid accidental shared-state mutations in domain functions. Demonstrate a full task lifecycle, missing/duplicate IDs, malformed stored JSON, invalid arguments and a simulated failed write without silently changing prior valid data. Provide a reviewable technical defense of the design and one failure investigated.
  - Criteria: All four commands and help/usage behave according to the documented contract; data persists correctly across independent invocations; no duplicate IDs or invalid state are silently accepted; an operation on a missing ID fails distinguishably and does not mutate storage; unexpected parse/write failures preserve previously valid data wherever the documented safe-update guarantee applies. Normal, boundary and failure tests use the standard library and run from a clean checkout. The learner can explain control flow, mutable-state ownership, serialization, error boundaries and one concrete engineering trade-off without relying solely on a green test report.
  - Evidence: Versioned or portable source, README with interpreter and cross-process usage, JSON schema and sample data, clean-start/test commands, unit and subprocess-based integration results, positive and negative CLI transcripts, before/after storage checks, a documented corrected defect, and a concise written or recorded technical defense.
  - Review cases: A reviewer may choose an unfamiliar combination of add/update/delete operations, then ask the learner to predict output and persisted state before running them.

- **SEF2-AS6** (required object abstractions and typing investigation)
  - Outcomes: SEF2-O4, SEF2-O6, SEF2-O8, SEF2-O10, SEF2-O11, SEF2-O12
  - Work: Extend or refactor the existing SEF2-AS5 task manager's domain layer, rather than build a second application. Define a small `Task` class with a constructor, independently owned instance attributes and methods that preserve a nonempty ID/title and Boolean completion state; define a composed task collection or repository object that works with multiple `Task` instances without an unnecessary inheritance hierarchy. Keep CLI and serialization responsibilities at explicit boundaries. Annotate a few actual public interfaces, including a typed collection and a lookup that returns `Task | None`. Write a runnable demonstration that passing a string to an `int`-annotated function does not inherently enforce or coerce the type. Add explicit runtime validation at relevant untrusted-input and state-transition boundaries. Independently test two separate instances, one shared alias, an invalid constructor, an invalid update, a missing lookup, a persisted round trip and an unfamiliar reviewer-supplied valid/invalid record. Explain which existing function-only design would remain preferable and why.
  - Criteria: A real instance is created with `__init__` and `self`; instance state is distinct unless explicitly shared, and class attributes do not silently leak mutable task state. Each public method has an explicit coherent responsibility and the composition boundary is meaningful rather than decorative. Invariants are maintained or invalid inputs rejected with visible behavior; no unexplained mutation of unrelated tasks occurs. Annotations accurately describe ordinary valid use, including missing results; the learner correctly distinguishes optional static-analysis feedback from runtime checking, demonstrates that annotations alone do not validate values and enforces needed runtime checks. Existing `add`, `list`, `update` and `delete` behavior and persistence from AS5 remain correct; an unfamiliar review case is reasoned about before execution. No proprietary or third-party type checker is required, and introducing abstraction must not make the program less understandable.
  - Evidence: Revised portable task-manager source, concise explanation or diagram of object identities and composition, annotated domain interfaces, tests of normal and failing cases with observed outputs, a demonstration of annotation-versus-runtime behavior, before/after CLI and persisted-data regression results, a documented corrected class/typing defect or reviewer challenge, and a technical defense of when a class is useful.

### Completion decision

All **six required assessments** must pass their published criteria, together demonstrating SEF2-O1 through SEF2-O12. The task manager may reuse the validated file-writing design from SEF2-AS4; the object/typing investigation SEF2-AS6 may refactor or extend **that same task manager**. The learner is not required to build unrelated extra applications, repeat a lab in every module, install a third-party type checker, or take a separate final examination. Optional lesson exercises, guided examples, additional quizzes and practice tasks are formative and **do not** add hidden completion conditions.

The reviewer records the assessment decisions and supporting evidence. Substantial discrepancies must be corrected or explicitly bounded when they do not violate a stated acceptance criterion. A technical defense can be written, recorded, live or another reviewable accessible format that evaluates the same published outcomes. No learner is automatically `tested` or `verified` because this course file has passed a structural check; the published course itself remains `draft` pending the learner and reviewer evidence required by [Status Labels](../../spec/status-labels.md).

### Revision history and evidence compatibility

**Historical contract:** [SEF2 at OEE commit `fd772ce7d120300fc2b6ef89121b52345525cd56`](https://github.com/0xbuffdev/open-engineering-education/blob/fd772ce7d120300fc2b6ef89121b52345525cd56/curriculum/SEF/SEF2.md), before this focused academic revision. The historical reference is immutable and must not be inferred from the latest `main` branch.

| Historical requirement | Current requirement | Evidence interpretation |
| --- | --- | --- |
| `SEF2-O1`–`O10` | Same IDs and same outcome statements | Previous assessed competence is not relabeled or silently extended |
| `SEF2-AS1`–`AS5` | Same IDs, work, criteria, evidence and review cases | Existing records remain tied to the earlier revision and can support corresponding unchanged capabilities |
| No independently stated class/composition outcome | New `SEF2-O11` evaluated with `SEF2-AS6` | Requires inspectable object-design and state-invariant evidence |
| No independently stated typing/runtime-boundary outcome | New `SEF2-O12` evaluated with `SEF2-AS6` | Requires accurate annotation, explicit runtime checks and evidence-based reasoning |

This revision retains **SEF2-O1–O10** with exactly their original meaning and keeps the **Work, Criteria, and Evidence of SEF2-AS1–AS5** unchanged. Newly required `SEF2-O11` (classes, object invariants, composition) and `SEF2-O12` (type annotations versus runtime behavior) are evaluated by new `SEF2-AS6`, whose implementation reuses the assessed task manager. The two new modules and their additional formative lessons are not separate mandatory assignments. The nominal duration changes from 8 to 10–12 weeks provisionally.

Historical completions and submitted evidence remain associated with their original course revision. A learner who completed the previous ten-outcome SEF2 contract is not automatically marked as having demonstrated the two new outcomes; an evidence-based reviewer may recognize an already established capability or require the new unfamiliar cases. No prior course completion is deleted or automatically revoked by this revision, and no source modification changes the course's `draft` readiness label. See the [accepted SEF architecture decision](../../rfcs/0003-sef-academic-progression.md) and [Status Labels](../../spec/status-labels.md).
