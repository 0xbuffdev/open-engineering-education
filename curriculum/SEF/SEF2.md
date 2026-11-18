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

Learn to build and reason about small programs from their behavior rather than memorize Python syntax. Start with the difference between source code, the Python interpreter and execution state. Prepare a terminal-based local workspace, then learn values, conditions, loops, functions, collections, files, errors, and debugging. Investigate aliases and mutable state, debugging, structured-file integrity and safe updates before building a persistent command-line task manager. Then use that same application to evaluate when classes, composition and type annotations improve domain contracts, while distinguishing declared types from required runtime validation.

Python 3.11 or later and its standard library are the reference teaching environment. Use Windows, macOS or Linux, a text editor, and an ordinary terminal; `python`, `python3` or `py` may be the working interpreter command. An alternative equivalent free local Python environment is acceptable if the submitted work remains reproducible. All required work is possible offline with no paid account, service, third-party package, administrator privileges, or real personal data.

This is a `course` in programming foundations, not the larger professional software-engineering capstone. Its six summative evaluations progressively combine skills and may reuse a learner's earlier artifacts, including the same persistent task-manager project for the final abstraction-and-typing investigation. The lesson sequence and optional practice provide preparation; **the required outcomes, assessments and evidence below determine completion**. A fixed number of quizzes, per-module labs or mandatory final lab is not imposed.

The 10–12-week duration is a provisional planning range for programming, investigation, persistent data and object/typing work; it is not calibrated against learner completion time and does not imply educational readiness. All work should use disposable project directories and fabricated input records.

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

### Module 1 — Python Execution and a Reproducible Workspace

#### Outcomes

- SEF2-O1
- SEF2-O2

#### Lessons

1. **From a computer to a program** — Reconnect SEF1's stored instructions to a higher-level program, distinguishing a behavior specification, source text, executable instructions, and the software that carries out the translation or execution. Explain what programming changes without conflating coding with the whole engineering process.
2. **Python language and interpreter implementations** — Distinguish the Python language from CPython and other conforming implementations; trace how CPython compiles source to a code object and interpreter bytecode, then executes it, without calling that bytecode the processor's instruction set.
3. **A known local interpreter** — Install or select a freely available supported Python 3.11+ interpreter, record implementation and version, and check which executable the shell actually invokes on Windows, macOS, or Linux; distinguish a launcher alias from the interpreter it starts.
4. **Files, working directories, and commands** — Create an owned project directory and a source file; predict how the current working directory, an explicit script path, and the selected interpreter affect a command's result. Reproduce a clean-start run without assuming a particular editor or shell.
5. **Interactive exploration versus a script** — Compare an expression evaluated in the Python prompt with the same statement in an edited source file; explain visible output, state that persists only within one process, and why a second invocation starts fresh.
6. **The first failure is evidence** — Reproduce a missing executable, wrong working directory, invalid Python syntax, or runtime exception in a disposable example; use the actual diagnostic to identify the failed stage and correct it without suppressing the error.

*Optional practice:* Give a second learner the exact interpreter, directory and script commands and ask them to reproduce a run and classify one deliberately changed environment or syntax failure.

### Module 2 — Values, Names, Expressions and Execution Traces

#### Outcomes

- SEF2-O3

#### Lessons

1. **Values, types, and representations** — Evaluate simple integer, floating-point, Boolean, string, and `None` values; distinguish a value, its type, and the textual representation used to display it. Note that a value's representation is not its memory address.
2. **Names and rebinding** — Predict the effect of assignments and reassignments in a running program; distinguish a name referring to an object from a fixed storage box, anticipating later mutable-object behavior without requiring copying rules yet.
3. **Expressions, conversions, and failure** — Evaluate operators, precedence, integer division and remainder, comparisons, and explicit type conversions; predict a wrong-type or invalid-operation failure instead of inventing a useful result.
4. **Output and observation** — Use `print()` and simple formatted output to expose a computation's intermediate values; distinguish an observation from the program's underlying state and from a function's eventual return value.
5. **Trace before execution** — Construct a stepwise state table for an unfamiliar short script with expressions, assignments and output; check the prediction against a real run and identify the exact statement responsible for any discrepancy.

*Optional practice:* Change one input or assignment in a short program, predict the new state and output, then verify and explain why the result changed.

### Module 3 — Decisions, Repetition and Termination

#### Outcomes

- SEF2-O3
- SEF2-O4

#### Lessons

1. **Truth values and conditional decisions** — Evaluate comparisons, Boolean operators and Python truthiness in a bounded example; distinguish a Boolean expression from an arbitrary object used in a condition and test both branches.
2. **Branching with explicit cases** — Choose between `if`, `elif` and `else` cases using a written input contract; trace mutually exclusive paths and demonstrate an unmatched or boundary case.
3. **While loops and evolving state** — Model a loop as initialization, condition, state update and termination; use an explicit progress argument to diagnose an off-by-one or nonterminating loop without relying on an arbitrary iteration count.
4. **For loops, ranges and finite iteration** — Predict the values and stopping conditions of `for` loops over `range()` and short iterable examples; distinguish an empty traversal from a failed execution.
5. **Choosing and testing a repetition strategy** — Compare a condition-driven loop with a finite traversal for a real small task; verify the zero-iteration, first-item, last-item and invalid-input cases and explain which implementation makes termination clearer.

*Optional practice:* Hand-trace a counting loop with a changed bound and correct a deliberately misplaced update that makes the loop behave incorrectly.

### Module 4 — Functions, Scope, Modules and Source Inspection

#### Outcomes

- SEF2-O1
- SEF2-O3
- SEF2-O4

#### Lessons

1. **Decompose behavior into functions** — Turn a short external input/output specification into independently understandable operations; distinguish a function's responsibility from its caller and avoid functions whose only purpose is to shorten a file.
2. **Arguments, parameters and return values** — Define and call functions with positional and keyword arguments; trace parameter binding, returned results and the difference between a returned value and printed output.
3. **Local scope and state changes** — Predict local name lookup, rebinding and execution across a call; explain when a function needs an explicit argument or return instead of relying on module-level mutable state.
4. **Interfaces and optional parameters** — Publish clear preconditions and return/error behavior for small functions; use a justified default argument while deferring the shared-mutable-default hazard to the later aliasing lesson.
5. **Modules, imports and executable entry points** — Separate reusable functions from a command-line entry point; distinguish importing a module from running a file, use a `__main__` guard where appropriate, and verify that importing does not execute the application.
6. **Inspecting an unfamiliar compiled function** — Use CPython's standard-library `dis` on a small previously unseen function and map instruction roles to source-level state and control flow; record the actual runtime version and explain why opcode names, caches and layouts are implementation-dependent.
7. **Behavior-preserving decomposition** — Refactor a short script into functions and modules; use independent expected outputs, normal cases and one deliberate error to show behavior was preserved rather than merely changing organization.

*Optional practice:* Explain how a two-argument function would behave when one argument changes, then use `dis` to distinguish observed interpreter bytecode from the CPU instructions introduced in SEF1.

### Module 5 — Text, Collections and Iterable Data

#### Outcomes

- SEF2-O5
- SEF2-O3
- SEF2-O4

#### Lessons

1. **Text as Unicode and domain data** — Select string operations for parsing, slicing, normalizing and formatting text; compare `strip()` and `casefold()` against naïve case comparisons, and avoid equating one Unicode character with one byte.
2. **Ordered sequences and fixed records** — Use lists and tuples for appropriate ordered data; predict indexing, slicing, membership and empty-input behavior and justify when a fixed record should not be an editable list.
3. **Mappings and keyed aggregation** — Build dictionaries from unfamiliar records, distinguish a key's presence from its stored value, and verify updates, duplicate-key behavior and the documented iteration-order guarantee.
4. **Sets, hashability and identity of keys** — Use sets for distinct membership; explain why mutable lists cannot serve as dictionary keys and why a tuple is hashable only if its elements are, rather than declaring all tuples safe keys.
5. **The iteration protocol** — Trace how `iter()` produces an iterator, how `next()` advances it to exhaustion, and why `for` works with iterables beyond lists; demonstrate how mutation during traversal can invalidate an iteration assumption.
6. **Iteration helpers and comprehensions** — Use `enumerate()` and `zip()` with explicit stopping behavior for unequal inputs; choose a readable comprehension for a simple transformation and an explicit loop when error handling or state transitions make it clearer.
7. **Choose a data representation from a contract** — Compare list, dictionary, set and tuple designs for a record-summary task; trace ordered output, case-normalized duplicate names, zero/empty records and predictable rejection of malformed inputs.

*Optional practice:* Predict the result of aggregating differently capitalized names, then independently verify the dictionary state and sorted output rather than comparing only a final printout.

### Module 6 — Aliasing, Mutation and Function Side Effects

#### Outcomes

- SEF2-O6
- SEF2-O3
- SEF2-O8

#### Lessons

1. **Names, object identity and equality** — Draw a reference graph for two names and one mutable object; distinguish rebinding, equal values and shared identity before predicting any mutation.
2. **Mutation and shallow copies** — Trace a list or dictionary update through aliases, then compare slice/shallow copies with the original; identify which nested members remain shared.
3. **Nested state and ownership choices** — Inspect a nested record in which a change to one group unexpectedly affects another; decide whether fresh structure construction or selective copying establishes the required non-mutation contract, without copying everything automatically.
4. **Function effects and shared defaults** — Explain mutation across a function call, return and argument boundary; reproduce a shared mutable default that retains state between invocations and replace it with a clear per-call policy.
5. **Make a non-mutation promise testable** — Compare independently derived before/after reference graphs with observed state; build tests that detect changes to caller-owned data, unrelated nested records and repeated-call behavior.

*Optional practice:* Correct a function that unintentionally mutates a caller's nested list, then challenge it with a second shared nested object.

### Module 7 — Validation, Exceptions, Debugging and Tests

#### Outcomes

- SEF2-O8
- SEF2-O4

#### Lessons

1. **Syntax, runtime and logic failures** — Distinguish errors caught while parsing, exceptions raised during execution and incorrect results that appear to run successfully; use the failure's actual circumstances, not a guessed cause.
2. **Read a traceback as causal evidence** — Identify the failing call path, exception type, relevant input and source location; reduce a noisy program to a minimal independently reproducible case.
3. **Raise, propagate and handle exceptions** — Choose where an error should be reported, transformed or allowed to propagate; avoid `except: pass`, generic catches that hide bugs, and treating every exception as invalid user input.
4. **Contracts and input validation** — Specify the valid shape and domain of input before processing it; distinguish caller errors, corrupted persisted state and programmer defects, and explain when to raise versus return a result.
5. **A falsifiable debugging investigation** — Record an observation, propose a causal hypothesis, choose a discriminating experiment, repair the actual cause and show a test that failed before the correction.
6. **Independent expected results with `unittest`** — Create normal, empty, boundary and malformed cases with oracles not copied from the implementation; isolate fixture state and explain why a green test alone cannot prove a missing behavior.

*Optional practice:* Repair a record parser that silently accepts invalid input and document a minimal negative fixture that would expose a regression.

### Module 8 — Local Files, Structured Records and Safe Updates

#### Outcomes

- SEF2-O7
- SEF2-O8
- SEF2-O9

#### Lessons

1. **File paths and controlled lifetimes** — Read and write local files using `pathlib`, explicit paths and context managers; separate a caller-selected data location from the current directory and keep experiments inside disposable fixtures.
2. **Encodings, newlines and decoding errors** — Open text explicitly with UTF-8, explain byte-to-text decoding and platform newline differences, and show why malformed bytes must not be silently converted into plausible valid data.
3. **CSV as a constrained record format** — Use the standard-library `csv` module with `newline=''`, a declared header and row policy; identify quoted separators, missing or extra fields, duplicate records and precise per-record validation.
4. **JSON shapes and round trips** — Distinguish JSON objects/arrays/numbers/strings/Booleans/null from Python values, define a public schema, and verify deterministic serialization, decoding, type checking and non-ASCII text.
5. **Validate before modifying a destination** — Parse and validate the entire source before changing any existing valid output; define meaningful error categories and verify that invalid records never trigger an incidental partial overwrite.
6. **Temporary output and replacement semantics** — Create a safely named temporary file in the destination directory, write and close it, then use `os.replace` under documented platform assumptions; explain that replacement atomicity does not guarantee power-loss durability.
7. **Fault injection and independent byte evidence** — Simulate malformed CSV/JSON, invalid encoding, missing input and failed write/replace; compare the destination's exact prior and resulting bytes, clean temporary artifacts when feasible and report limitations honestly.

*Optional practice:* Make a CSV-to-JSON conversion that survives a simulated pre-replacement failure without losing the old valid JSON; inspect the bytes and the failure report instead of only testing success.

### Module 9 — Persistent Command-Line Application

#### Outcomes

- SEF2-O2
- SEF2-O4
- SEF2-O5
- SEF2-O6
- SEF2-O7
- SEF2-O8
- SEF2-O9
- SEF2-O10

#### Lessons

1. **Define the user's command contract** — Specify `add`, `list`, `update` and `delete`, required identifiers and titles, argument and output conventions, Boolean completion state, help text and distinguishable failure outcomes.
2. **Separate CLI, domain and persistence responsibilities** — Parse arguments with a documented standard-library approach; keep core state operations independently callable and testable without requiring a command-line subprocess for each small rule.
3. **Protect stored and in-memory state** — Validate task records and commands, prevent accidental shared-state mutation and duplicate identifiers, and reuse the same controlled temporary-file replacement principles developed for structured records.
4. **Trace a lifecycle across processes** — Run multiple independent invocations against one disposable task file; predict the persisted JSON after add/update/list/delete and distinguish fresh interpreter memory from cross-process persistence.
5. **Test errors as seriously as success** — Use `unittest` and subprocess execution with independent expected outputs and storage bytes for unknown commands, missing IDs, malformed stored JSON and a simulated failed write.
6. **Defend the smallest sufficient implementation** — Reproduce the program from clean state, explain one concrete debugging correction and a trade-off in data representation, and respond to an unfamiliar bounded CLI scenario without adding an unrelated second application.

*Optional practice:* Complete one task's lifecycle in separate processes, then compare the observed JSON with a hand-derived state table and diagnose a failed update.

### Module 10 — Classes, Instances and Coherent Domain Invariants

#### Outcomes

- SEF2-O4
- SEF2-O6
- SEF2-O10
- SEF2-O11

#### Lessons

1. **Choose a class only for a real responsibility** — Compare functions plus dictionaries with a domain object whose operations must preserve state invariants; explain why adding a class to every value would not improve the task manager.
2. **Construct an instance** — Define a `Task` class with `__init__`, `self`, explicit fields and valid initial state; trace how two constructor calls produce independently owned instance attributes.
3. **Attribute lookup, methods and object identity** — Predict method calls and attribute updates through aliases, distinguishing the identity of an instance from its persisted task identifier and from an equal record.
4. **Class versus instance state** — Diagnose a shared mutable class attribute and repair it with an appropriate per-instance allocation or explicit shared-state policy.
5. **Transitions and rejected invalid states** — Encode the domain rule that task IDs/titles are nonempty and completion is Boolean; exercise valid updates, rejected construction and a state transition that must leave other instances untouched.
6. **Encapsulation and composition as boundaries** — Publish a small usable interface, distinguish underscore conventions from security enforcement, and compose a `TaskCollection` instead of inventing a subclass hierarchy for unrelated tasks.
7. **Serialize objects deliberately** — Convert domain objects to validated JSON-compatible records and back, keeping object aliasing and file representation separate; test a round trip against a real earlier CLI fixture.
8. **Proportionate alternatives and independent tests** — Compare a hand-written constructor to a standard-library dataclass and its mutable-default restrictions; verify independent instances, aliased references, invalid transitions and the original CLI behavior before deciding whether the refactor helped.

*Optional practice:* Refactor the same task manager from Module 9 rather than creating a second project. Reject a deliberately incorrect shared class-level list while retaining the original persistent-data contract.

### Module 11 — Type Annotations, Runtime Trust and an Integrated Defense

#### Outcomes

- SEF2-O4
- SEF2-O8
- SEF2-O10
- SEF2-O11
- SEF2-O12

#### Lessons

1. **What an annotation does not do** — Annotate a simple function and observe what happens when it receives a wrong runtime type; distinguish documentation, optional static inspection and actual validation or conversion.
2. **Types for actual function and collection interfaces** — Use `int`, `str`, `bool`, `None`, `list[Task]` and `dict[str, Task]` where they accurately describe valid input and return contracts; keep annotations proportional to the beginner application.
3. **Optional results and explicit absent states** — Model a task lookup returning `Task | None` and explain how callers handle both branches, why an empty task is not the same as absence and why an exception is a different result path.
4. **Annotation inspection and static limitations** — Inspect runtime annotation information and describe what an optional checker can and cannot infer; do not rely on third-party checking, `Any`, a cast or an assertion to validate untrusted data.
5. **Typed boundaries still need runtime checks** — Validate CLI arguments, decoded JSON, domain invariants and object transitions at their actual trust boundaries; demonstrate a test where annotations alone would accept a bad value.
6. **Refine and defend the existing task manager** — Add a few meaningful annotations to the Module 9/10 codebase, reproduce earlier CLI and storage tests, correct an unfamiliar class or typing defect, and explain the trade-offs of functions versus class composition and static hints versus observed runtime behavior.

*Optional practice:* A reviewer supplies a malformed persisted task and a missing lookup; predict the annotated API's result and demonstrate the actual runtime checks without installing a static type checker.

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

An earlier course revision introduced **SEF2-O11** (classes, invariants and composition), **SEF2-O12** (annotations versus runtime behavior) and **SEF2-AS6**, reusing the assessed task manager rather than requiring an unrelated application. **This competency-derived instructional realignment retains all twelve currently published outcomes and all six required assessment contracts.** It reorganizes how learners prepare for and integrate those capabilities, without changing previous assessment decisions or silently granting evidence for a newer requirement.

Historical completions and submitted evidence remain associated with their original course revision. A learner who completed the previous ten-outcome SEF2 contract is not automatically marked as having demonstrated the two new outcomes; an evidence-based reviewer may recognize an already established capability or require the new unfamiliar cases. No prior course completion is deleted or automatically revoked by this revision, and no source modification changes the course's `draft` readiness label. See the [accepted SEF architecture decision](../../rfcs/0003-sef-academic-progression.md) and [Status Labels](../../spec/status-labels.md).
