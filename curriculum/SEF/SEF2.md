# SEF2 — Programming & Computational Thinking

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** [SEF1](SEF1.md)
**Duration:** 8 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

This course introduces software, code, and software engineering, and sets up the learner's workspace: a terminal, a code editor, and Python. It then develops computational thinking: breaking problems into steps, writing conditionals, loops, and functions, working with collections and files, handling errors, and debugging. The emphasis is on how programs work rather than on memorizing syntax.

- [**SEF1 — Demystifying the Computer System**](SEF1.md)

**Python** is the primary teaching language.

The objective is programming fundamentals, not Python specialization. Python is used because it allows beginners to focus on programming concepts before low-level complexity becomes dominant.

## Learning outcomes

By the end of the course, the learner will be able to:

- Explain what software, programming, and software engineering are, and how source code becomes a running program.
- Use a terminal, a code editor, and the Python interpreter to write, run, and fix a program.
- Break a problem into smaller computational steps.
- Write Python programs using functions, conditionals, loops, collections, and file I/O.
- Explain how names refer to objects, and predict how assignment, aliasing, mutation, and function calls change program state.
- Handle invalid input and runtime errors with validation and exceptions.
- Read and debug small programs written by others.
- Explain the control flow and major design decisions of programs they have written.
- Build a small command-line application from a specification.
- Test program state, mutable aliases, input parsing and file failure behavior independently of tutorials.

## Modules

### Module 1 — Software, Code & Languages

#### Outcomes

- Explain what software, a program, coding, and software engineering are, and how they differ.
- Explain how source code written in a programming language becomes a running program.
- Describe how CPython compiles source code to bytecode and runs it on a virtual machine, and inspect the bytecode of a small function.

#### Lessons

1. **Course introduction: Programming & Computational Thinking** — `lesson`

   Programming is the central skill of the curriculum. This course teaches it from the first terminal command to a finished command-line application, with an emphasis on understanding what the computer does at each step.
2. **What software is** — `lesson`
3. **What coding is** — `lesson`
4. **What software engineering is** — `lesson`
5. **Programming languages** — `lesson`
6. **Source code** — `lesson`
7. **Interpreters and compilers** — `lesson`
8. **Bytecode and the virtual machine** — `lesson`
9. **Software and code** — `test`
10. **Inspect Python bytecode** — `lab`

### Module 2 — Your Workspace

#### Outcomes

- Use a terminal to move between directories, list files, and run commands.
- Install Python, write a program in an editor, run it, and read the error message when it fails.

#### Lessons

1. **The terminal** — `lesson`
2. **Installing Python** — `lesson`
3. **Code editors** — `lesson`
4. **The Python prompt** — `lesson`
5. **Running a file** — `lesson`
6. **Your first error** — `lesson`
7. **Workspace readiness and error diagnosis** — `test`
8. **Run, break, fix** — `lab`

### Module 3 — Thinking in Programs

#### Outcomes

- Explain how a program is built from ordered steps that operate on values.
- Trace short code by hand and predict the state and output it produces.
- Explain that a name refers to an object, and that assignment rebinds the name instead of copying the object.

#### Lessons

1. **Programs as steps** — `lesson`
2. **Values and types** — `lesson`
3. **Expressions and arithmetic** — `lesson`
4. **Variables and state** — `lesson`
5. **Printing output** — `lesson`
6. **Tracing execution** — `lesson`
7. **Programs, values, and state** — `test`
8. **First program** — `lab`

### Module 4 — Conditions & Loops

#### Outcomes

- Explain how Boolean conditions select which code runs and how loops repeat work.
- Choose between conditionals, `while` loops, and `for` loops for a given task.

#### Lessons

1. **Boolean expressions** — `lesson`
2. **If statements** — `lesson`
3. **While loops** — `lesson`
4. **For loops** — `lesson`
5. **Loop patterns** — `lesson`
6. **Conditions and loops** — `test`
7. **Trace a loop** — `lab`

### Module 5 — Functions & Decomposition

#### Outcomes

- Define and call functions with parameters, local state, and return values.
- Explain where a call keeps its names and what happens to them when it returns.
- Decompose a problem into small functions with clear responsibilities.

#### Lessons

1. **Defining functions** — `lesson`
2. **Parameters and arguments** — `lesson`
3. **Local variables and scope** — `lesson`
4. **Return values** — `lesson`
5. **Interfaces and decomposition** — `lesson`
6. **Modules and imports** — `lesson`
7. **Functions and scope** — `test`
8. **Refactor into functions** — `lab`

### Module 6 — Strings & Collections

#### Outcomes

- Explain the behavior of strings, lists, dictionaries, tuples, and sets.
- Choose an appropriate collection for a problem and use it correctly.
- Predict the effect of aliasing, mutation, and shallow copies on mutable objects.

#### Lessons

1. **Strings** — `lesson`
2. **Lists** — `lesson`
3. **Dictionaries** — `lesson`
4. **Tuples** — `lesson`
5. **Sets** — `lesson`
6. **Choosing a collection** — `lesson`
7. **Strings and collections** — `test`
8. **Count words** — `lab`

### Module 7 — Files & Data

#### Outcomes

- Read from and write to files, including structured data such as JSON.
- Navigate paths and directories from a program.

#### Lessons

1. **Reading files** — `lesson`
2. **Writing files** — `lesson`
3. **Structured data** — `lesson`
4. **Directories and paths** — `lesson`
5. **File I/O and data formats** — `test`
6. **Clean a data file** — `lab`

### Module 8 — Errors & Debugging

#### Outcomes

- Explain what a traceback reports and handle expected failures with exceptions.
- Validate input and diagnose a failing program by forming and testing hypotheses.

#### Lessons

1. **Reading tracebacks** — `lesson`
2. **Handling exceptions** — `lesson`
3. **Raising exceptions** — `lesson`
4. **Validating input** — `lesson`
5. **Debugging by evidence** — `lesson`
6. **Errors and debugging** — `test`
7. **Repair a program** — `lab`

### Module 9 — Mutation & Function Contracts

#### Outcomes

- Predict and test state mutation across function calls.
- Diagnose an unexpected result using observable evidence.

#### Lessons

1. **Names, objects and identity** — `lesson`
2. **Mutable aliases and copies** — `lesson`
3. **Nested collection behavior** — `lesson`
4. **Parameters, side effects and returns** — `lesson`
5. **Preconditions and assertions** — `lesson`
6. **Mutation & Function Contracts reasoning** — `test`
7. **Repair an aliasing defect** — `lab`

### Module 10 — Reliable Files & Input

#### Outcomes

- Build a robust file-processing command with predictable failure behavior.
- Diagnose an unexpected result using observable evidence.

#### Lessons

1. **Text encodings and newlines** — `lesson`
2. **CSV and JSON error handling** — `lesson`
3. **Exceptions versus result values** — `lesson`
4. **Safe file writes and temporary files** — `lesson`
5. **Boundary tests and CLI contracts** — `lesson`
6. **Reliable Files & Input reasoning** — `test`
7. **Harden a dataset converter** — `lab`

### Module 11 — Command-Line Task Manager

#### Outcomes

- Explain how a command-line program receives input and reports results.
- Build a tested, documented command-line application from a specification.

#### Lessons

1. **Command-line arguments** — `lesson`
2. **Tests as checks** — `lesson`
3. **Logging and messages** — `lesson`
4. **CLI behavior and persistence contracts** — `test`
5. **Task manager** — `lab`

   **Final integration lab — required work**

   **Command-Line Task Manager**

   Build a tested CLI application with:

   - Add, list, update, and delete operations
   - Persistence to JSON
   - Input validation
   - Useful error messages
   - Doctests or unit tests
   - README and usage examples
   - Tests for persistence across separate CLI invocations and invalid operations
   - Explicit error and exit-status behavior, with no corruption of existing data

## Completion requirements

- Complete the required course exercises, checkpoints and evaluated labs below.
- Complete the final integrated `lab` in the last module and meet its stated observable exit criteria.
- Retain reproducible artifacts, verification results, design explanations, and a meaningful technical retrospective in accordance with [OEE Evidence Rules](../../spec/evidence-rules.md).

Complete these required exercises:

**Conceptual practice:**

- Terminal navigation drills
- Number and string problems
- Expression and variable tracing
- Condition and loop problems
- Function and decomposition exercises
- List, dictionary, and set problems
- File parsing and structured data
- Input validation
- Search and counting programs
- Command-line utilities
- Deliberately broken programs to diagnose and repair

**Practical practice:**

- Install Python, run a three-line file, break it, and fix it from the error message.
- Trace a program by hand and predict its output.
- Write and run a small program that solves a stated problem.
- Parse a real text or CSV dataset into structured records.
- Add validation and error handling to a broken program.
- Turn a written specification into a small command-line tool.

**Required conceptual checkpoints and practical lab contracts:**

The 11 checkpoints below provide two example written questions each, with expected reasoning. They may be replaced by equivalent unfamiliar questions assessing the same outcomes. All questions and required labs must be completed with demonstrable understanding; merely reproducing the example answer or showing a passing screenshot does not establish mastery. A learner who cannot yet explain an outcome receives further practice and reassessment.

**Shared environment and accessibility:**

Use Python 3.11 or later and its standard library on Windows, macOS or Linux, a local editor and a terminal. Document the actual interpreter/version, operating system and exact build/run/test commands. Python may be invoked as `python`, `python3` or `py`, depending on the host; do not assume one alias exists everywhere. Tests use `python -m unittest discover -s tests -v` (or a documented equivalent command for the selected interpreter). No paid service, third-party Python package, administrator privileges or external network access is required.

**Shared acceptance and evidence requirements:**

- Treat source code and its observed behavior as separate claims: predict before execution, compare actual results with expected values, and explain discrepancies.
- Document normal, boundary, invalid-input and failure behavior wherever the lab includes data or executable code. Do not require work against real user files or existing private credentials.
- Retain source revision, test commands/output, fixtures, errors, corrections, and a technical retrospective. Keep all writing and file-mutation exercises inside a disposable working directory.
- The course begins with guided examples, then progressively requires independent code creation. SEF5 addresses deeper CI, Git collaboration and professional review; this course establishes their programming prerequisites.

**Module 1 — Software, Code & Languages: checkpoint** — Required assessment details

- **Q1 (free):** How do source code, CPython bytecode and the interpreter's virtual machine relate? Is CPython bytecode a CPU machine instruction?
  - Expected answer and scoring: CPython parses/compiles Python source to a CPython-specific intermediate bytecode representation, which the interpreter executes. This bytecode is not the target CPU's native machine code. Actual details and disassembly vary by CPython version; avoid equating all Python implementations with CPython.
- **Q2 (free):** Explain the difference between a program, a programming language and software engineering using one concrete example.
  - Expected answer and scoring: A program is executable instructions/data implementing behavior; a programming language specifies a syntax/semantics for expressing it; software engineering includes specifying, testing, maintaining and validating it. For instance, a small task script may be Python code, while its tests, documentation and failure handling are engineering practices.

**Module 1 — Inspect Python bytecode: required lab** — Required assessment details

- **Objective:** Run and inspect a tiny Python program and explain execution layers without requiring pre-existing programming expertise.
- **Prerequisites:** Complete the module's teaching material and explain the conceptual checkpoint. Modules may reuse earlier lab artifacts when their behavior is explicitly verified.
- **Environment:** Use Python 3.11 or later and its standard library on Windows, macOS or Linux, a local editor and a terminal. Document the actual interpreter/version, operating system and exact build/run/test commands. Python may be invoked as `python`, `python3` or `py`, depending on the host; do not assume one alias exists everywhere. Tests use `python -m unittest discover -s tests -v` (or a documented equivalent command for the selected interpreter). No paid service, third-party Python package, administrator privileges or external network access is required.
- **Procedure:**
  1. Identify the installed Python interpreter and its implementation/version using documented commands and confirm that it can run a small provided `hello.py` file.
  2. Use a supplied two-statement Python script that prints a message and computes `2+3`; predict and record stdout before running it.
  3. Use Python's standard-library `dis` module to inspect the bytecode of a supplied function `def add(a,b): return a+b`. Record representative instructions and explain their roles rather than assuming stable opcode names across versions.
  4. Intentionally introduce a syntax error in a copy of the file, capture its diagnostic, restore the valid version and verify execution.
  5. Draw the path from source file through CPython compilation and bytecode execution to displayed output and distinguish these stages from the CPU model studied in SEF1.
- **Expected result:** The program prints its documented message and arithmetic result; the disassembly represents executable CPython bytecode, and a syntax error is detected before normal execution.
- **Verification:** Compare predicted stdout to observed output, record implementation/version, and check that the invalid copy fails and the fixed copy succeeds.
- **Evidence:** Source, terminal transcript, interpreter details, disassembly excerpt, execution diagram and brief error correction.
- **Failure analysis:** Explain confusing Python bytecode with native instructions or assuming bytecode is identical across interpreters.
- **Acceptance:** The learner demonstrates the listed normal and negative behavior, provides an inspectable source revision and independently checkable results, and explains a relevant failure. Missing required functionality, inaccurate reasoning or unreproducible evidence prevents completion.

**Module 2 — Your Workspace: checkpoint** — Required assessment details

- **Q1 (free):** A file exists in `project/hello.py`, but `python hello.py` fails with a file-not-found error from the parent directory. What should be checked before changing source code?
  - Expected answer and scoring: Check the current working directory and the relative path. Run with the correct path or change into the project directory; the failure may be an invocation/path issue rather than a syntax or runtime bug. Explain how to inspect the current directory and list files on the chosen platform.
- **Q2 (free):** What is the practical distinction between executing `python -c 'print(2+3)'` and `python hello.py`, and how can you check which interpreter ran?
  - Expected answer and scoring: The first evaluates a provided command string, while the second executes a source file. Interpreter aliases and virtual environments vary; record `sys.executable` and `sys.version` from the running interpreter rather than assuming a shell command name uniquely identifies it.

**Module 2 — Run, break, fix: required lab** — Required assessment details

- **Objective:** Create a working local editor-to-interpreter workflow and diagnose path, syntax and runtime problems without changing unrelated system settings.
- **Prerequisites:** Complete the module's teaching material and explain the conceptual checkpoint. Modules may reuse earlier lab artifacts when their behavior is explicitly verified.
- **Environment:** Use Python 3.11 or later and its standard library on Windows, macOS or Linux, a local editor and a terminal. Document the actual interpreter/version, operating system and exact build/run/test commands. Python may be invoked as `python`, `python3` or `py`, depending on the host; do not assume one alias exists everywhere. Tests use `python -m unittest discover -s tests -v` (or a documented equivalent command for the selected interpreter). No paid service, third-party Python package, administrator privileges or external network access is required.
- **Procedure:**
  1. Create a new disposable project directory with a README and a Python file edited in a text editor; use documented terminal commands appropriate to the host OS.
  2. Write a small script that prints the current Python version and a user-visible greeting, run it from the project directory and then from its parent using a correct file path.
  3. Introduce a missing quote to trigger a SyntaxError; copy the message and line reference, predict the fix, repair it and rerun the file.
  4. Introduce a separate controlled division-by-zero error and distinguish its runtime traceback from the previous syntax error.
  5. Record the command that reports the interpreter path and version and explain how to reproduce the working program from an empty terminal.
- **Expected result:** The clean script runs from both documented locations; the syntax and runtime errors are correctly categorized, reproduced and repaired.
- **Verification:** A reviewer follows the written path/run commands and obtains the expected greeting and version; the seeded error copies fail in the stated ways.
- **Evidence:** Project source, README, interpreter/version output, terminal commands, two error traces and corrective changes.
- **Failure analysis:** Explain running the wrong interpreter, invoking a wrong working directory, or confusing a SyntaxError with a runtime exception.
- **Acceptance:** The learner demonstrates the listed normal and negative behavior, provides an inspectable source revision and independently checkable results, and explains a relevant failure. Missing required functionality, inaccurate reasoning or unreproducible evidence prevents completion.

**Module 3 — Thinking in Programs: checkpoint** — Required assessment details

- **Q1 (free):** Trace `x = 3; y = x; x = x + 2; print(x, y)` in Python. What prints, and why does the earlier assignment to y not change?
  - Expected answer and scoring: It prints `5 3`. Names initially refer to the same immutable integer object; rebinding x to the result of x+2 does not mutate that integer or rebind y.
- **Q2 (free):** Predict `print(7 // 2, 7 % 2, 7 / 2)` and explain the meaning of each operator.
  - Expected answer and scoring: The result is `3 1 3.5`: // performs floor division, % produces the remainder consistent with Python's identity, and / performs true division. Explain this for positive operands rather than generalizing truncation to negative values.

**Module 3 — First program: required lab** — Required assessment details

- **Objective:** Convert a simple written specification into traceable Python statements and verify their state changes.
- **Prerequisites:** Complete the module's teaching material and explain the conceptual checkpoint. Modules may reuse earlier lab artifacts when their behavior is explicitly verified.
- **Environment:** Use Python 3.11 or later and its standard library on Windows, macOS or Linux, a local editor and a terminal. Document the actual interpreter/version, operating system and exact build/run/test commands. Python may be invoked as `python`, `python3` or `py`, depending on the host; do not assume one alias exists everywhere. Tests use `python -m unittest discover -s tests -v` (or a documented equivalent command for the selected interpreter). No paid service, third-party Python package, administrator privileges or external network access is required.
- **Procedure:**
  1. Given three item prices 12, 7 and 5, create a script that computes total cost, item count and average cost using named intermediate values.
  2. Write a manual execution table identifying each expression, variable value and printed output before running the program.
  3. Add an optional discount of 10% and explain how the final price changes without altering the source item list.
  4. Test an empty-item case by explicitly defining whether the average is undefined, omitted or reported with a clear message; do not silently divide by zero.
  5. Change one assignment order to introduce an intentional error, demonstrate the resulting mismatch, then repair it with a new manual trace.
- **Expected result:** Base total=24, count=3 and average=8; 10% discount yields 21.6. Empty-item behavior is documented and never triggers an unhandled division by zero.
- **Verification:** Use independently worked arithmetic, verify printed output and state transitions, and repeat tests for normal, discounted and empty cases.
- **Evidence:** Source, hand trace, observed outputs, edge-case contract and failure/repair narrative.
- **Failure analysis:** Explain a rebinding misconception, arithmetic/precedence error or unsupported empty collection.
- **Acceptance:** The learner demonstrates the listed normal and negative behavior, provides an inspectable source revision and independently checkable results, and explains a relevant failure. Missing required functionality, inaccurate reasoning or unreproducible evidence prevents completion.

**Module 4 — Conditions & Loops: checkpoint** — Required assessment details

- **Q1 (free):** What are the final values of total and n after `total=0; for n in range(1,5): total += n`? How many iterations execute?
  - Expected answer and scoring: The loop visits 1,2,3,4 (four iterations); total=10 and n=4 afterward. The stop of range is exclusive.
- **Q2 (free):** Describe a termination invariant for `while remaining > 0: remaining -= 1` when remaining initially equals 3. Why might this loop fail to stop if decrement is omitted?
  - Expected answer and scoring: remaining is nonnegative at loop entry and decreases by exactly one while positive, so it reaches zero after three iterations and terminates. Without decreasing progress, the condition stays true indefinitely. Explain a guard/iteration bound for debugging loops.

**Module 4 — Trace a loop: required lab** — Required assessment details

- **Objective:** Select conditional and loop structures, trace each iteration and prevent nonterminating or incorrect boundary behavior.
- **Prerequisites:** Complete the module's teaching material and explain the conceptual checkpoint. Modules may reuse earlier lab artifacts when their behavior is explicitly verified.
- **Environment:** Use Python 3.11 or later and its standard library on Windows, macOS or Linux, a local editor and a terminal. Document the actual interpreter/version, operating system and exact build/run/test commands. Python may be invoked as `python`, `python3` or `py`, depending on the host; do not assume one alias exists everywhere. Tests use `python -m unittest discover -s tests -v` (or a documented equivalent command for the selected interpreter). No paid service, third-party Python package, administrator privileges or external network access is required.
- **Procedure:**
  1. Implement a bounded sum-of-integers function for n from 0 to a user-given nonnegative limit and a second function classifying values into positive, zero or negative.
  2. Create a loop trace table for n=4 showing the value before and after each iteration, including the loop's stop condition.
  3. Test n=0, n=1, n=4 and invalid negative or noninteger inputs, with documented behavior.
  4. Introduce an off-by-one range error in a separate version and demonstrate the first failing input; repair it and retain a regression check.
  5. Show how to abort or cap a nonterminating demonstration safely rather than asking a beginner to run an uncontrolled infinite loop.
- **Expected result:** The sum of 0..4 equals 10; the classification routine distinguishes negative, zero and positive values; invalid inputs are handled explicitly.
- **Verification:** Compare outputs with hand-calculated sums, inspect trace rows and run edge/invalid tests with a bounded execution policy.
- **Evidence:** Code, trace table, test transcript, failing boundary fixture and explanation of termination.
- **Failure analysis:** Explain an exclusive range stop, an unintended loop-state reset or a missing progress update.
- **Acceptance:** The learner demonstrates the listed normal and negative behavior, provides an inspectable source revision and independently checkable results, and explains a relevant failure. Missing required functionality, inaccurate reasoning or unreproducible evidence prevents completion.

**Module 5 — Functions & Decomposition: checkpoint** — Required assessment details

- **Q1 (free):** Trace `x=10; def f(x): x=x+1; return x; y=f(x)`. What are x and y afterward? Explain the name bindings.
  - Expected answer and scoring: x remains 10 and y is 11. Function parameter x is a separate local name bound to the argument object; its later rebinding does not change the outer x. Python function calls pass references to objects through argument binding, not writable name slots.
- **Q2 (free):** What changes when a function prints a result instead of returning it? For `def f(): print(3)`, what does `f()` return?
  - Expected answer and scoring: It writes `3` to stdout as a side effect but returns `None` implicitly. A caller cannot reliably use the printed output as a numeric return value without separate capture; choose returns for computation and printing for presentation.

**Module 5 — Refactor into functions: required lab** — Required assessment details

- **Objective:** Turn a monolithic beginner program into small functions with testable inputs and clear return contracts.
- **Prerequisites:** Complete the module's teaching material and explain the conceptual checkpoint. Modules may reuse earlier lab artifacts when their behavior is explicitly verified.
- **Environment:** Use Python 3.11 or later and its standard library on Windows, macOS or Linux, a local editor and a terminal. Document the actual interpreter/version, operating system and exact build/run/test commands. Python may be invoked as `python`, `python3` or `py`, depending on the host; do not assume one alias exists everywhere. Tests use `python -m unittest discover -s tests -v` (or a documented equivalent command for the selected interpreter). No paid service, third-party Python package, administrator privileges or external network access is required.
- **Procedure:**
  1. Start from the Module 3 shopping-cost script or a provided single-block equivalent and identify at least three independent responsibilities: input validation, calculation and output formatting.
  2. Refactor into functions `validate_prices`, `calculate_total` and `format_summary` (or equivalent names), using explicit parameters and return values.
  3. Document valid input, empty input and negative-price policy. Demonstrate that calculation functions return data without requiring print statements.
  4. Write standard-library `unittest` cases for each function and a small end-to-end call, including invalid input behavior.
  5. Create a deliberate local-versus-global variable confusion and trace its correction without using global state as an unexplained workaround.
- **Expected result:** For [12,7,5], the computed total remains 24 and outputs match the original contract; the functions can be tested without invoking the entire CLI.
- **Verification:** Run independent function tests and compare original and refactored observable results for normal and invalid fixtures.
- **Evidence:** Before/after source, function signatures, test results, scope trace and a short design decision note.
- **Failure analysis:** Explain missing return values, unintended globals or a function that mixes validation and display so its behavior cannot be isolated.
- **Acceptance:** The learner demonstrates the listed normal and negative behavior, provides an inspectable source revision and independently checkable results, and explains a relevant failure. Missing required functionality, inaccurate reasoning or unreproducible evidence prevents completion.

**Module 6 — Strings & Collections: checkpoint** — Required assessment details

- **Q1 (free):** For `items=['a','b']; alias=items; alias.append('c')`, what does items contain? Contrast this with rebinding alias to a new list.
  - Expected answer and scoring: items becomes ['a','b','c'] because both names refer to the same mutable list. Rebinding alias to a new list would not modify the original items. Explain mutation versus name reassignment.
- **Q2 (free):** Which collection is suitable for counting words, testing membership and storing unique words, respectively?
  - Expected answer and scoring: A dictionary maps word→count for frequencies; a set provides membership/uniqueness; a list retains ordered occurrences if needed. Choose based on required semantics, not an unsupported blanket performance claim.

**Module 6 — Count words: required lab** — Required assessment details

- **Objective:** Normalize text and count token frequencies while demonstrating appropriate use of strings, dictionaries and sets.
- **Prerequisites:** Complete the module's teaching material and explain the conceptual checkpoint. Modules may reuse earlier lab artifacts when their behavior is explicitly verified.
- **Environment:** Use Python 3.11 or later and its standard library on Windows, macOS or Linux, a local editor and a terminal. Document the actual interpreter/version, operating system and exact build/run/test commands. Python may be invoked as `python`, `python3` or `py`, depending on the host; do not assume one alias exists everywhere. Tests use `python -m unittest discover -s tests -v` (or a documented equivalent command for the selected interpreter). No paid service, third-party Python package, administrator privileges or external network access is required.
- **Procedure:**
  1. Define a simple, explicitly limited tokenizer: convert to lowercase and split on whitespace after removing chosen leading/trailing punctuation characters; document that this does not solve all natural-language tokenization.
  2. Count occurrences in a dictionary and collect unique words in a set, with an independently worked example such as `Cat cat DOG` yielding cat:2 and dog:1.
  3. Sort report rows by frequency descending and then word ascending to create deterministic output; never rely on dictionary iteration to imply a frequency ranking.
  4. Test empty input, repeated words, punctuation, Unicode case behavior within the stated normalization policy and a one-token string.
  5. Introduce an error that overwrites rather than increments a word's count, reproduce the mismatch and repair it.
- **Expected result:** Case-normalized frequencies match the chosen tokenizer contract; `Cat cat DOG` yields cat 2 and dog 1, and outputs have deterministic sorting.
- **Verification:** Use independently counted small examples, total-count invariant sum(counts)=number of tokens, and edge cases under the declared tokenization rule.
- **Evidence:** Tokenizer specification, source, input/output fixtures, frequency tables, invariant checks and defect trace.
- **Failure analysis:** Explain losing repeated counts, assuming punctuation disappears automatically or relying on unspecified sort order.
- **Acceptance:** The learner demonstrates the listed normal and negative behavior, provides an inspectable source revision and independently checkable results, and explains a relevant failure. Missing required functionality, inaccurate reasoning or unreproducible evidence prevents completion.

**Module 7 — Files & Data: checkpoint** — Required assessment details

- **Q1 (free):** Why should a text file opened for reading declare a character encoding? How can a UTF-8 decoding failure differ from a missing-file failure?
  - Expected answer and scoring: Encoding defines how bytes map to text; decoding errors (for invalid encoded bytes) differ from filesystem errors like FileNotFoundError. Handle expected failures separately and avoid silently replacing malformed bytes unless the contract explicitly permits it.
- **Q2 (free):** A JSON file contains `[{'name':'A'}]` using single quotes. Is it valid JSON, and what must a program do?
  - Expected answer and scoring: It is not valid JSON because JSON strings/property names require double quotation marks. A parser should report a controlled JSONDecodeError or documented validation error rather than evaluating it as Python source.

**Module 7 — Clean a data file: required lab** — Required assessment details

- **Objective:** Read and normalize a small local file into a validated structured form without hiding malformed records.
- **Prerequisites:** Complete the module's teaching material and explain the conceptual checkpoint. Modules may reuse earlier lab artifacts when their behavior is explicitly verified.
- **Environment:** Use Python 3.11 or later and its standard library on Windows, macOS or Linux, a local editor and a terminal. Document the actual interpreter/version, operating system and exact build/run/test commands. Python may be invoked as `python`, `python3` or `py`, depending on the host; do not assume one alias exists everywhere. Tests use `python -m unittest discover -s tests -v` (or a documented equivalent command for the selected interpreter). No paid service, third-party Python package, administrator privileges or external network access is required.
- **Procedure:**
  1. Create a CSV or JSON fixture with at least four records including whitespace, duplicate IDs and one malformed record. State the intended acceptance/rejection policy before writing code.
  2. Implement a reader using explicit UTF-8 and the standard-library csv or json module; separate parsing from record validation.
  3. Normalize selected text fields without silently changing identifiers and output a list of valid records plus a documented error summary for bad records.
  4. Write results only into a dedicated temporary output file, leaving the original fixture unchanged; document the output schema.
  5. Test empty input, missing file, malformed JSON/CSV and unexpected record types, recording expected error behavior.
- **Expected result:** Valid records become the stated normalized schema, invalid records are counted/rejected according to policy and the original file remains unchanged.
- **Verification:** Compare exact record counts, IDs and fields with hand-checked fixtures; test the parser independently of filesystem writes.
- **Evidence:** Input fixture, output example, validation rules, source, parse error tests and data-integrity checks.
- **Failure analysis:** Explain silent data loss, accidental read/write confusion, reliance on implicit encodings or treating a Python literal as JSON.
- **Acceptance:** The learner demonstrates the listed normal and negative behavior, provides an inspectable source revision and independently checkable results, and explains a relevant failure. Missing required functionality, inaccurate reasoning or unreproducible evidence prevents completion.

**Module 8 — Errors & Debugging: checkpoint** — Required assessment details

- **Q1 (free):** A traceback ends in `ValueError: invalid literal for int()` after user input `abc`. What caused the failure, and should a program broadly catch every exception?
  - Expected answer and scoring: int('abc') cannot parse the string as an integer. Validate or catch the expected ValueError at the input boundary and report an actionable message; an unqualified catch-all can hide unrelated programming defects.
- **Q2 (free):** A script displays the wrong total but raises no exception. Describe an evidence-driven debugging sequence.
  - Expected answer and scoring: State expected-versus-actual output, construct a minimal reproducer, trace intermediate values, form and test a specific hypothesis, correct the cause, and add a regression test. Do not equate absence of exceptions with correctness.

**Module 8 — Repair a program: required lab** — Required assessment details

- **Objective:** Diagnose failures and incorrect results by isolating evidence, not by speculative edits.
- **Prerequisites:** Complete the module's teaching material and explain the conceptual checkpoint. Modules may reuse earlier lab artifacts when their behavior is explicitly verified.
- **Environment:** Use Python 3.11 or later and its standard library on Windows, macOS or Linux, a local editor and a terminal. Document the actual interpreter/version, operating system and exact build/run/test commands. Python may be invoked as `python`, `python3` or `py`, depending on the host; do not assume one alias exists everywhere. Tests use `python -m unittest discover -s tests -v` (or a documented equivalent command for the selected interpreter). No paid service, third-party Python package, administrator privileges or external network access is required.
- **Procedure:**
  1. Start with a small supplied script that parses an integer count and computes a total; seed one invalid-input crash and one silent arithmetic defect.
  2. Record both symptoms using exact commands and minimal input fixtures; explain why one raises an exception while the other does not.
  3. Form two testable hypotheses, add trace prints or debugger inspection for state and isolate the responsible code.
  4. Repair the input validation with a narrowly handled ValueError and correct the arithmetic defect without hiding unexpected exceptions.
  5. Add regression tests for valid input, the invalid string, zero and a boundary value; demonstrate the before/after results.
- **Expected result:** The valid calculation matches its stated formula; invalid input yields a clear non-success result without an uncontrolled traceback; regression tests detect both seeded faults.
- **Verification:** Run the original and repaired versions against identical fixtures, capture before/after outputs and test exit status or error contract.
- **Evidence:** Bug reproduction, trace, competing hypotheses, fix diff, tests and a short retrospective.
- **Failure analysis:** Explain a broad exception handler masking an unrelated error, debugging only by changing values or a fix that fails to add regression coverage.
- **Acceptance:** The learner demonstrates the listed normal and negative behavior, provides an inspectable source revision and independently checkable results, and explains a relevant failure. Missing required functionality, inaccurate reasoning or unreproducible evidence prevents completion.

**Module 9 — Mutation & Function Contracts: checkpoint** — Required assessment details

- **Q1 (free):** For `rows=[[1],[2]]; clone=rows.copy(); clone[0].append(9)`, what happens to rows, and why?
  - Expected answer and scoring: rows becomes [[1,9],[2]]. list.copy creates a new outer list but the nested lists are still shared references; mutation to the nested element is observable through both.
- **Q2 (free):** When is a copy required versus an explicit immutable interface or pure function for avoiding shared-state bugs?
  - Expected answer and scoring: A shallow copy is sufficient only when nested mutable objects will not be shared in an unsafe way; a deep copy or re-creating nested structures can isolate mutable values, while designing a pure function or immutable data contract may eliminate the ownership ambiguity. Explain cost and intended sharing.

**Module 9 — Repair an aliasing defect: required lab** — Required assessment details

- **Objective:** Show how aliases and shallow copies affect nested mutable state, then enforce an explicit ownership contract.
- **Prerequisites:** Complete the module's teaching material and explain the conceptual checkpoint. Modules may reuse earlier lab artifacts when their behavior is explicitly verified.
- **Environment:** Use Python 3.11 or later and its standard library on Windows, macOS or Linux, a local editor and a terminal. Document the actual interpreter/version, operating system and exact build/run/test commands. Python may be invoked as `python`, `python3` or `py`, depending on the host; do not assume one alias exists everywhere. Tests use `python -m unittest discover -s tests -v` (or a documented equivalent command for the selected interpreter). No paid service, third-party Python package, administrator privileges or external network access is required.
- **Procedure:**
  1. Start with a function that accepts nested task groups and appends an item to one group's list; create two logically independent callers that share an inner list through a shallow copy.
  2. Capture the unintended mutation in a minimal deterministic test and draw which objects each name references before and after the call.
  3. Refactor the function to return a fresh set of nested lists or use another explicit ownership rule, avoiding accidental mutation of caller data.
  4. Test repeated function calls, empty nested lists, multiple groups and unchanged original inputs; demonstrate that changes do not leak between groups.
  5. Discuss why indiscriminate deep copying can add expense or change intended sharing and document the chosen contract.
- **Expected result:** The initial bug visibly changes the original nested state; after repair, original input remains unchanged and updates appear only in the returned/new collection.
- **Verification:** Assert both returned values and original-state invariants on nested fixtures; retain an object-reference diagram and regression test.
- **Evidence:** Original and corrected implementations, minimal reproduction, object diagram, tests, ownership specification and retrospective.
- **Failure analysis:** Explain why copying only the outer list fails or why rebinding a local parameter does not necessarily mutate its caller.
- **Acceptance:** The learner demonstrates the listed normal and negative behavior, provides an inspectable source revision and independently checkable results, and explains a relevant failure. Missing required functionality, inaccurate reasoning or unreproducible evidence prevents completion.

**Module 10 — Reliable Files & Input: checkpoint** — Required assessment details

- **Q1 (free):** A converter writes directly to an existing output file and fails halfway through JSON parsing. What data-integrity problem is possible, and which standard-library operations improve safety?
  - Expected answer and scoring: The previous valid output may be truncated/corrupted before validation finishes. Validate/build output first, write a temporary file in the destination directory, flush and close it, then use os.replace for a same-filesystem replace. Explain that this avoids partial visible application output for the described case but alone does not guarantee durability after a power failure.
- **Q2 (free):** How should a CSV/JSON command distinguish a missing file, malformed content and an invalid schema?
  - Expected answer and scoring: Use explicitly defined error categories and nonzero exit status/messages without exposing traceback internals to normal users; classify FileNotFoundError/OS errors, parser errors and semantic record validation separately. Include exit behavior in the CLI contract.

**Module 10 — Harden a dataset converter: required lab** — Required assessment details

- **Objective:** Implement repeatable file conversion with safe failure behavior and documented input/output contracts.
- **Prerequisites:** Complete the module's teaching material and explain the conceptual checkpoint. Modules may reuse earlier lab artifacts when their behavior is explicitly verified.
- **Environment:** Use Python 3.11 or later and its standard library on Windows, macOS or Linux, a local editor and a terminal. Document the actual interpreter/version, operating system and exact build/run/test commands. Python may be invoked as `python`, `python3` or `py`, depending on the host; do not assume one alias exists everywhere. Tests use `python -m unittest discover -s tests -v` (or a documented equivalent command for the selected interpreter). No paid service, third-party Python package, administrator privileges or external network access is required.
- **Procedure:**
  1. Define a CSV-to-JSON conversion contract with required `id` and `title` fields, unique nonempty identifiers, explicit UTF-8 encoding and deterministic output ordering.
  2. Build a validator that reads and checks all source records before modifying the destination; distinguish missing input, malformed CSV structure, duplicate identifiers and invalid fields.
  3. Write the successful normalized JSON to a temporary file created in the output directory, close it and replace the destination with os.replace only after successful conversion and output serialization.
  4. Seed a valid existing JSON output and then run conversions with malformed or missing input; compare the existing output's exact bytes before and after failure.
  5. Test empty files, duplicate IDs, non-ASCII text, unexpected encodings and a simulated write/rename failure using an injectable filesystem operation or controlled test fixture, without changing unrelated files.
- **Expected result:** Valid input produces correct JSON with deterministic records; invalid input preserves prior destination bytes and reports a documented error status.
- **Verification:** Compare exact before/after output bytes, parse generated JSON independently, assert record invariants and failure codes, and disclose the crash-durability limitations of os.replace.
- **Evidence:** Schema, source code, fixtures, output snapshots, file-preservation tests, injected fault results and failure analysis.
- **Failure analysis:** Explain opening the destination too early, treating partial input as success, assuming os.replace guarantees fsync-style durability or mishandling UTF-8.
- **Acceptance:** The learner demonstrates the listed normal and negative behavior, provides an inspectable source revision and independently checkable results, and explains a relevant failure. Missing required functionality, inaccurate reasoning or unreproducible evidence prevents completion.

**Module 11 — Command-Line Task Manager: checkpoint** — Required assessment details

- **Q1 (free):** What should happen when the task manager receives `update` for an identifier that does not exist? Why must an error be distinguishable from a successful no-op?
  - Expected answer and scoring: The CLI must report a predictable error and nonzero exit status, without changing persisted data, because a silent success misleads callers and obscures failures. The exact message and status are part of the documented public contract.
- **Q2 (free):** A task manager stores JSON records with IDs and done/undone state. What must an integration test verify after adding a task and starting a new process?
  - Expected answer and scoring: It must verify persistence across independent CLI invocations, correct id uniqueness and round-trip serialization, and that list/update/delete reflect stored state. Testing only in-memory functions misses CLI argument parsing and filesystem boundaries.

**Module 11 — Task manager: required lab** — Required assessment details

- **Objective:** Build a complete beginner-level, persistent CLI application from a public behavioral specification and defend its implementation.
- **Prerequisites:** Complete the module's teaching material and explain the conceptual checkpoint. Modules may reuse earlier lab artifacts when their behavior is explicitly verified.
- **Environment:** Use Python 3.11 or later and its standard library on Windows, macOS or Linux, a local editor and a terminal. Document the actual interpreter/version, operating system and exact build/run/test commands. Python may be invoked as `python`, `python3` or `py`, depending on the host; do not assume one alias exists everywhere. Tests use `python -m unittest discover -s tests -v` (or a documented equivalent command for the selected interpreter). No paid service, third-party Python package, administrator privileges or external network access is required.
- **Procedure:**
  1. Define `add`, `list`, `update` and `delete` commands. Assign each task a unique nonempty identifier and title, a boolean completed flag, and a documented JSON schema and storage path under a temporary/project directory.
  2. Implement argument parsing with Python's standard-library argparse, separate state operations from file I/O and support a clear command usage/help path.
  3. Use UTF-8 JSON persistence and the same safe temporary-file-and-replace discipline introduced in Module 10 for successful writes. Do not erase an existing valid store on malformed input.
  4. Create standard-library unittest tests for domain functions and cross-process CLI invocations; include create, update, delete, persistence, duplicate IDs, missing IDs, invalid arguments and malformed JSON.
  5. Define clear success versus failure exit statuses and error output. Ensure operations on missing tasks do not silently succeed or mutate persisted content.
  6. Rebuild from a clean checkout with a written README and one test command, then have an independent reviewer reproduce a successful task lifecycle and a deliberate failure.
  7. Present a short technical defense showing control flow, state mutations, module interfaces, error handling, and one wrong assumption corrected during development.
- **Expected result:** All four commands work according to the published behavior; persisted records survive separate executions; invalid operations fail predictably without corrupting existing data.
- **Verification:** Run a fresh-process end-to-end task lifecycle and negative scenarios in a disposable directory; compare stdout/stderr, exit status, JSON file and test output to the documented contract.
- **Evidence:** Versioned source, README, CLI transcripts, input/output fixtures, unit and end-to-end tests, reviewer reproduction and technical retrospective.
- **Failure analysis:** Explain accidental overwrites, unchecked duplicate identifiers, aliasing across functions or missing error handling at the file boundary.
- **Acceptance:** The learner demonstrates the listed normal and negative behavior, provides an inspectable source revision and independently checkable results, and explains a relevant failure. Missing required functionality, inaccurate reasoning or unreproducible evidence prevents completion.

**Exit demonstration:**

The learner writes a small program from a specification without a template and explains the control flow.
