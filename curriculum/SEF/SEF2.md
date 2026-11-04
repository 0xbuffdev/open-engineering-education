# SEF2 — Programming & Computational Thinking

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** [SEF1](SEF1.md)
**Duration:** 7 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

This course introduces software, code, and software engineering, and sets up the learner's workspace: a terminal, a code editor, and Python. It then develops computational thinking: breaking problems into steps, writing conditionals, loops, and functions, working with collections and files, handling errors, and debugging. The emphasis is on how programs work rather than on memorizing syntax.

- [**SEF1 — Demystifying the Computer System**](SEF1.md)

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

## Modules

### Module 1 — Software, Code & Languages

#### Outcomes

- Integrate and demonstrate the course capabilities through the module's final practical work.

#### Lessons

1. **Course introduction: Programming & Computational Thinking** — `lesson` — what the subject is, where it came from, where it is used, and its strengths and limits
2. **What software is** — `lesson`
3. **What coding is** — `lesson`
4. **What software engineering is** — `lesson`
5. **Programming languages** — `lesson`
6. **Source code** — `lesson`
7. **Interpreters and compilers** — `lesson` — two ways to run a language; real languages mix them
8. **Bytecode and the virtual machine** — `lesson` — CPython compiles source to bytecode, then a virtual machine runs it; this is how CPython works, not a rule for every language; inspect bytecode with `dis`
9. **Software and code** — `test`

### Module 2 — Your Workspace

#### Outcomes

- Integrate and demonstrate the course capabilities through the module's final practical work.

#### Lessons

1. **The terminal** — `lesson`
2. **Installing Python** — `lesson`
3. **Code editors** — `lesson`
4. **The Python prompt** — `lesson`
5. **Running a file** — `lesson`
6. **Your first error** — `lesson`
7. **Run, break, fix** — `lab`

### Module 3 — Thinking in Programs

#### Outcomes

- Integrate and demonstrate the course capabilities through the module's final practical work.

#### Lessons

1. **Programs as steps** — `lesson`
2. **Values and types** — `lesson`
3. **Expressions and arithmetic** — `lesson`
4. **Variables and state** — `lesson` — a name is bound to an object; assignment rebinds the name and does not copy the object; objects live on the heap
5. **Printing output** — `lesson`
6. **Tracing execution** — `lesson`
7. **Programs, values, and state** — `test`
8. **First program** — `lab`

### Module 4 — Conditions & Loops

#### Outcomes

- Integrate and demonstrate the course capabilities through the module's final practical work.

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

- Integrate and demonstrate the course capabilities through the module's final practical work.

#### Lessons

1. **Defining functions** — `lesson`
2. **Parameters and arguments** — `lesson`
3. **Local variables and scope** — `lesson` — each call gets a frame on the call stack that holds its names; parameters bind to the argument objects; the frame goes away when the call returns
4. **Return values** — `lesson`
5. **Interfaces and decomposition** — `lesson`
6. **Modules and imports** — `lesson`
7. **Functions and scope** — `test`
8. **Refactor into functions** — `lab`

### Module 6 — Strings & Collections

#### Outcomes

- Integrate and demonstrate the course capabilities through the module's final practical work.

#### Lessons

1. **Strings** — `lesson`
2. **Lists** — `lesson` — lists are mutable; two names can refer to the same list (aliasing); a change through one name shows through the other; a copy is shallow
3. **Dictionaries** — `lesson`
4. **Tuples** — `lesson` — tuples and strings are immutable; why immutability makes sharing an object safe
5. **Sets** — `lesson`
6. **Choosing a collection** — `lesson`
7. **Strings and collections** — `test`
8. **Count words** — `lab`

### Module 7 — Files & Data

#### Outcomes

- Integrate and demonstrate the course capabilities through the module's final practical work.

#### Lessons

1. **Reading files** — `lesson`
2. **Writing files** — `lesson`
3. **Structured data** — `lesson`
4. **Directories and paths** — `lesson`
5. **Clean a data file** — `lab`

### Module 8 — Errors & Debugging

#### Outcomes

- Integrate and demonstrate the course capabilities through the module's final practical work.

#### Lessons

1. **Reading tracebacks** — `lesson`
2. **Handling exceptions** — `lesson`
3. **Raising exceptions** — `lesson`
4. **Validating input** — `lesson`
5. **Debugging by evidence** — `lesson`
6. **Errors and debugging** — `test`
7. **Repair a program** — `lab`

### Module 9 — Command-Line Task Manager

#### Outcomes

- Integrate and demonstrate the course capabilities through the module's final practical work.

#### Lessons

1. **Command-line arguments** — `lesson`
2. **Tests as checks** — `lesson`
3. **Logging and messages** — `lesson`
4. **Task manager** — `lab`

## Completion requirements

- Complete the required exercises and checkpoints described in the [public course requirements](requirements/SEF2.md).
- Complete the final integrated `lab` in the last module and meet its stated observable exit criteria.
- Retain reproducible artifacts, verification results, design explanations, and a meaningful technical retrospective in accordance with [OEE Evidence Rules](../../spec/evidence-rules.md).
