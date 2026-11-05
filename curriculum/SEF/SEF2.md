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
7. **Interpreters and compilers** — `lesson` — two ways to run a language; real languages mix them
8. **Bytecode and the virtual machine** — `lesson` — CPython compiles source to bytecode, then a virtual machine runs it; this is how CPython works, not a rule for every language; inspect bytecode with `dis`
9. **Software and code** — `test`

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
7. **Run, break, fix** — `lab`

### Module 3 — Thinking in Programs

#### Outcomes

- Explain how a program is built from ordered steps that operate on values.
- Trace short code by hand and predict the state and output it produces.
- Explain that a name refers to an object, and that assignment rebinds the name instead of copying the object.

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
3. **Local variables and scope** — `lesson` — each call gets a frame on the call stack that holds its names; parameters bind to the argument objects; the frame goes away when the call returns
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
2. **Lists** — `lesson` — lists are mutable; two names can refer to the same list (aliasing); a change through one name shows through the other; a copy is shallow
3. **Dictionaries** — `lesson`
4. **Tuples** — `lesson` — tuples and strings are immutable; why immutability makes sharing an object safe
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
5. **Clean a data file** — `lab`

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

### Module 9 — Command-Line Task Manager

#### Outcomes

- Explain how a command-line program receives input and reports results.
- Build a tested, documented command-line application from a specification.

#### Lessons

1. **Command-line arguments** — `lesson`
2. **Tests as checks** — `lesson`
3. **Logging and messages** — `lesson`
4. **Task manager** — `lab`

   **Final integration lab — required work**

   **Command-Line Task Manager**

   Build a tested CLI application with:

   - Add, list, update, and delete operations
   - Persistence to JSON
   - Input validation
   - Useful error messages
   - Doctests or unit tests
   - README and usage examples

## Completion requirements

- Complete the required course exercises, checkpoints and evaluated labs below.
- Complete the final integrated `lab` in the last module and meet its stated observable exit criteria.
- Retain reproducible artifacts, verification results, design explanations, and a meaningful technical retrospective in accordance with [OEE Evidence Rules](../../spec/evidence-rules.md).

**Required exercises**

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

**Exit demonstration:**

The learner writes a small program from a specification without a template and explains the control flow.
