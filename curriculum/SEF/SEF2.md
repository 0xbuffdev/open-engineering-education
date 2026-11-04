> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

# SEF2 — Programming & Computational Thinking

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** SEF1
**Duration:** 7 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

## Overview

This course introduces software, code, and software engineering, and sets up the learner's workspace: a terminal, a code editor, and Python. It then develops computational thinking: breaking problems into steps, writing conditionals, loops, and functions, working with collections and files, handling errors, and debugging. The emphasis is on how programs work rather than on memorizing syntax.

## Course brief

The course introduction is the first lesson of the first module. It combines the overview above with these fields.

- **Introduction:** Programming is the central skill of the curriculum. This course teaches it from the first terminal command to a finished command-line application, with an emphasis on understanding what the computer does at each step.
- **History:** Guido van Rossum began Python in the late 1980s and released it in 1991. Python 3, a deliberate redesign, followed in 2008. The name refers to the comedy group Monty Python.
- **Usage:** The learner writes programs in a terminal and an editor, runs them with the Python interpreter, and tests and debugs them.
- **Applications:** Python is used for web back ends, automation, data analysis, scientific computing, and machine learning.
- **Strengths:** Its syntax is readable, its standard library is large, and it lets beginners concentrate on programming concepts.
- **Limitations:** Python programs usually run more slowly than compiled programs, and many type errors appear only when the code runs.
- **Key concepts:** program; source code; interpreter; value; type; variable; binding; condition; loop; function; collection; mutability; file; exception; test; command-line application

## Prerequisites

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

#### Module brief

- **Introduction:** Before writing code it helps to know what code is. This module explains what software, a program, coding, and software engineering are, and how a program written for people becomes something a machine runs.
- **Overview:** It covers languages, source code, interpreters and compilers, and how CPython compiles source to bytecode and runs it on a virtual machine.
- **History:** FORTRAN, released in 1957, was the first widely used high-level language, C appeared in 1972, and Guido van Rossum released Python in 1991.
- **Key concepts:** software; program; source code; high-level and low-level languages; interpreter; compiler; bytecode; virtual machine

#### Module outcomes

By the end of this module, the learner can:

- Explain what software, a program, coding, and software engineering are, and how they differ.
- Explain how source code written in a programming language becomes a running program.
- Describe how CPython compiles source code to bytecode and runs it on a virtual machine, and inspect the bytecode of a small function.

1. **Course introduction: Programming & Computational Thinking** — what the subject is, where it came from, where it is used, and its strengths and limits
2. **What software is** — module introduction
3. **What coding is**
4. **What software engineering is**
5. **Programming languages**
6. **Source code**
7. **Interpreters and compilers** — two ways to run a language; real languages mix them
8. **Bytecode and the virtual machine** — CPython compiles source to bytecode, then a virtual machine runs it; this is how CPython works, not a rule for every language; inspect bytecode with `dis`
9. **Software and code**
   - kind: `test`

### Module 2 — Your Workspace

#### Module brief

- **Introduction:** Programming happens in an environment you control. This module sets up and explains the three tools used every day: the terminal, a code editor, and the Python interpreter.
- **Overview:** It covers the shell and basic commands, installing Python, editing and running a file, the interactive prompt, and reading a first error message.
- **Key concepts:** terminal; shell; prompt; directory and path; editor; interpreter; error message

#### Module outcomes

By the end of this module, the learner can:

- Use a terminal to move between directories, list files, and run commands.
- Install Python, write a program in an editor, run it, and read the error message when it fails.

1. **Introduction: Your Workspace** — what the topic is, where it is used, and its strengths and limits
2. **The terminal**
3. **Installing Python**
4. **Code editors**
5. **The Python prompt**
6. **Running a file**
7. **Your first error**
8. **Run, break, fix**
   - kind: `lab`

### Module 3 — Thinking in Programs

#### Module brief

- **Introduction:** A program is a sequence of steps acting on values. This module builds that idea from the smallest pieces.
- **Overview:** It covers values and types, expressions, variables, output, how a name is bound to an object, and tracing a program by hand.
- **Key concepts:** value; type; expression; variable; binding; object; reference; heap; state; trace

#### Module outcomes

By the end of this module, the learner can:

- Explain how a program is built from ordered steps that operate on values.
- Trace short code by hand and predict the state and output it produces.
- Explain that a name refers to an object, and that assignment rebinds the name instead of copying the object.

1. **Introduction: Thinking in Programs** — what the topic is, where it is used, and its strengths and limits
2. **Programs as steps**
3. **Values and types**
4. **Expressions and arithmetic**
5. **Variables and state** — a name is bound to an object; assignment rebinds the name and does not copy the object; objects live on the heap
6. **Printing output**
7. **Tracing execution**
8. **Programs, values, and state**
   - kind: `test`
9. **First program**
   - kind: `lab`

### Module 4 — Conditions & Loops

#### Module brief

- **Introduction:** Programs become useful when they choose and repeat. This module teaches conditions and loops.
- **Overview:** It covers Boolean expressions, if statements, while and for loops, and common loop patterns.
- **History:** The earliest machine languages already had conditional jumps, which compose into loops. Structured control flow became standard after Edsger Dijkstra's 1968 letter criticizing the goto statement.
- **Key concepts:** Boolean; condition; if and else; while; for; range; break and continue; loop patterns

#### Module outcomes

By the end of this module, the learner can:

- Explain how Boolean conditions select which code runs and how loops repeat work.
- Choose between conditionals, `while` loops, and `for` loops for a given task.

1. **Introduction: Conditions & Loops** — what the topic is, where it is used, and its strengths and limits
2. **Boolean expressions**
3. **If statements**
4. **While loops**
5. **For loops**
6. **Loop patterns**
7. **Conditions and loops**
   - kind: `test`
8. **Trace a loop**
   - kind: `lab`

### Module 5 — Functions & Decomposition

#### Module brief

- **Introduction:** Large problems become manageable when split into named pieces. Functions are the basic tool.
- **Overview:** It covers defining and calling functions, parameters and arguments, return values, local variables and scope, call frames on the call stack, decomposition, and modules.
- **Key concepts:** function; parameter; argument; return value; scope; call stack; frame; interface; decomposition; module

#### Module outcomes

By the end of this module, the learner can:

- Define and call functions with parameters, local state, and return values.
- Explain where a call keeps its names and what happens to them when it returns.
- Decompose a problem into small functions with clear responsibilities.

1. **Introduction: Functions & Decomposition** — what the topic is, where it is used, and its strengths and limits
2. **Defining functions**
3. **Parameters and arguments**
4. **Local variables and scope** — each call gets a frame on the call stack that holds its names; parameters bind to the argument objects; the frame goes away when the call returns
5. **Return values**
6. **Interfaces and decomposition**
7. **Modules and imports**
8. **Functions and scope**
   - kind: `test`
9. **Refactor into functions**
   - kind: `lab`

### Module 6 — Strings & Collections

#### Module brief

- **Introduction:** Real programs handle many values at once. This module introduces Python's built-in containers and the rules for choosing among them.
- **Overview:** It covers strings, lists, dictionaries, tuples, and sets, mutable and immutable objects, aliasing, and copying.
- **Strengths:** Built-in collections are fast, well tested, and expressive.
- **Limitations:** A mutable collection can be changed through any name that refers to it, and a poor choice, such as searching a list instead of a set, makes programs slow.
- **Key concepts:** string; list; dictionary; tuple; set; mutable and immutable; alias; shallow copy

#### Module outcomes

By the end of this module, the learner can:

- Explain the behavior of strings, lists, dictionaries, tuples, and sets.
- Choose an appropriate collection for a problem and use it correctly.
- Predict the effect of aliasing, mutation, and shallow copies on mutable objects.

1. **Introduction: Strings & Collections** — what the topic is, where it is used, and its strengths and limits
2. **Strings**
3. **Lists** — lists are mutable; two names can refer to the same list (aliasing); a change through one name shows through the other; a copy is shallow
4. **Dictionaries**
5. **Tuples** — tuples and strings are immutable; why immutability makes sharing an object safe
6. **Sets**
7. **Choosing a collection**
8. **Strings and collections**
   - kind: `test`
9. **Count words**
   - kind: `lab`

### Module 7 — Files & Data

#### Module brief

- **Introduction:** A program that forgets everything when it stops is limited. This module covers reading and writing files and storing structured data.
- **Overview:** It covers reading and writing text files, paths and directories, and the JSON format.
- **History:** Douglas Crockford specified JSON in the early 2000s from JavaScript's object notation, and it was later standardized as ECMA-404.
- **Key concepts:** file; path; reading and writing; text encoding; JSON; serialization

#### Module outcomes

By the end of this module, the learner can:

- Read from and write to files, including structured data such as JSON.
- Navigate paths and directories from a program.

1. **Introduction: Files & Data** — what the topic is, where it is used, and its strengths and limits
2. **Reading files**
3. **Writing files**
4. **Structured data**
5. **Directories and paths**
6. **Clean a data file**
   - kind: `lab`

### Module 8 — Errors & Debugging

#### Module brief

- **Introduction:** Every program fails. This module teaches how to read failures, handle expected ones, and find unexpected ones systematically.
- **Overview:** It covers tracebacks, exceptions, validating input, and debugging as forming and testing hypotheses.
- **History:** The word bug was used for faults in machines long before computers. A moth found in the Harvard Mark II in 1947 is a famous logbook entry.
- **Limitations:** Catching exceptions too broadly hides real faults, and validation cannot foresee every bad input.
- **Key concepts:** traceback; exception; try and except; raise; validation; hypothesis; reproduction

#### Module outcomes

By the end of this module, the learner can:

- Explain what a traceback reports and handle expected failures with exceptions.
- Validate input and diagnose a failing program by forming and testing hypotheses.

1. **Introduction: Errors & Debugging** — what the topic is, where it is used, and its strengths and limits
2. **Reading tracebacks**
3. **Handling exceptions**
4. **Raising exceptions**
5. **Validating input**
6. **Debugging by evidence**
7. **Errors and debugging**
   - kind: `test`
8. **Repair a program**
   - kind: `lab`

### Module 9 — Command-Line Task Manager

#### Module brief

- **Introduction:** This module turns separate skills into one tool that people can run from a terminal. It also introduces the habits that keep it working: tests and logs.
- **Overview:** It covers command-line arguments, automated checks with doctest and unittest, logging, and the course lab.
- **Key concepts:** command-line argument; exit status; test; assertion; logging; persistence

#### Module outcomes

By the end of this module, the learner can:

- Explain how a command-line program receives input and reports results.
- Build a tested, documented command-line application from a specification.

1. **Introduction: Command-Line Task Manager** — what the topic is, where it is used, and its strengths and limits
2. **Command-line arguments**
3. **Tests as checks**
4. **Logging and messages**
5. **Task manager**
   - kind: `lab`

## Topics

- Software, programming, and software engineering
- Programming languages, source code, interpreters, and compilers
- Bytecode and the Python virtual machine
- The terminal, installing Python, and code editors
- The Python prompt and running files
- Reading error messages
- Steps and programs
- Values and types
- Expressions and variables
- Names, objects, and references
- The call stack and the heap, at Python level
- Mutable and immutable objects, aliasing
- Conditionals, `while` loops, and `for` loops
- Functions, parameters, and scope
- Return values and decomposition
- Modules and imports
- Strings, lists, dictionaries, tuples, and sets
- Reading and writing files
- Structured data and JSON
- Paths and directories
- Tracebacks and exceptions
- Input validation
- Debugging as a reasoning process
- Command-line arguments
- Automated checks with doctest and unittest
- Logging

## Language

**Python** is the primary teaching language.

The objective is programming fundamentals, not Python specialization. Python is used because it allows beginners to focus on programming concepts before low-level complexity becomes dominant.

## Small exercises

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

## Practical exercises

3. Install Python, run a three-line file, break it, and fix it from the error message.
4. Trace a program by hand and predict its output.
5. Write and run a small program that solves a stated problem.
6. Parse a real text or CSV dataset into structured records.
7. Add validation and error handling to a broken program.
8. Turn a written specification into a small command-line tool.

## Course lab

**Command-Line Task Manager**

Build a tested CLI application with:

- Add, list, update, and delete operations
- Persistence to JSON
- Input validation
- Useful error messages
- Doctests or unit tests
- README and usage examples

## Exit check

The learner writes a small program from a specification without a template and explains the control flow.
