# SEF6 — C Programming & Machine Memory

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** [SEF3](SEF3.md), [SEF4](SEF4.md), [SEF5](SEF5.md)
**Duration:** 6 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

This course teaches C as a way to see and control the machine. Learners write multi-file C programs, reason about types and their binary representations, use pointers and addresses, trace how stack and heap memory are used, build programs with a compiler and Make, and diagnose memory errors with a debugger and sanitizers. It builds directly on the name, object, and call-stack model from SEF2 by showing what that model hides.

- [**SEF3 — Linux & the Command Line**](SEF3.md)
- [**SEF4 — Data Structures & Algorithms**](SEF4.md)
- [**SEF5 — Software Engineering Practice**](SEF5.md)

## Learning outcomes

By the end of the course, the learner will be able to:

- Write, compile, and run multi-file C programs from the command line.
- Read and write C values in binary and hexadecimal, and explain how integers and characters are stored.
- Use pointers, arrays, strings, and structures correctly, and trace addresses and values by hand.
- Explain the stack, the heap, and the lifetime of a C object, and allocate and release memory correctly.
- Explain how C source becomes a linked, loadable executable.
- Diagnose segmentation faults, leaks, and other memory errors with a debugger and sanitizers.
- Implement familiar data structures in C and compare C's manual lifetimes with Python's reference model.

## Modules

### Module 1 — C Data & Control Flow

#### Outcomes

- Integrate and demonstrate the course capabilities through the module's final practical work.

#### Lessons

1. **Course introduction: C Programming & Machine Memory** — `lesson` — what the subject is, where it came from, where it is used, and its strengths and limits
2. **C types and values** — `lesson`
3. **Operators and expressions** — `lesson`
4. **C control flow** — `lesson`
5. **Binary and hexadecimal** — `lesson`
6. **Integer representation** — `lesson`
7. **Characters and text** — `lesson`
8. **C data and binary** — `test`
9. **Inspect integer representations** — `lab` — print the bytes of values of different types, predict the output first, and explain overflow and sign behavior

### Module 2 — Functions & Program Structure

#### Outcomes

- Integrate and demonstrate the course capabilities through the module's final practical work.

#### Lessons

1. **Functions and arguments** — `lesson`
2. **Scope and storage** — `lesson`
3. **Header files and multiple source files** — `lesson`
4. **The C preprocessor** — `lesson`
5. **Functions and structure** — `test`
6. **Split a program into modules** — `lab` — reorganize a single-file program into modules with headers and verify that behavior is unchanged

### Module 3 — Addresses & Pointers

#### Outcomes

- Integrate and demonstrate the course capabilities through the module's final practical work.

#### Lessons

1. **Addresses** — `lesson`
2. **Pointers** — `lesson`
3. **Pointers and function arguments** — `lesson`
4. **Pointers and arrays** — `lesson`
5. **Address arithmetic** — `lesson`
6. **Strings as arrays of characters** — `lesson`
7. **Values and addresses** — `test`
8. **Trace pointers** — `lab` — trace a program that uses pointers by hand, record each address and value, and compare the trace with real output

### Module 4 — Stack, Heap & Dynamic Memory

#### Outcomes

- Integrate and demonstrate the course capabilities through the module's final practical work.

#### Lessons

1. **Address space of a process** — `lesson`
2. **Stack frames and function calls** — `lesson`
3. **Heap allocation with `malloc` and `free`** — `lesson`
4. **Lifetime errors: leaks, double free, and dangling pointers** — `lesson`
5. **Buffer overruns** — `lesson`
6. **C and Python lifetimes compared** — `lesson`
7. **Memory behavior** — `test`
8. **Fix memory errors** — `lab` — repair a program containing a leak, a double free, and an overrun, and explain how each corrupts or wastes memory

### Module 5 — Structures & Input/Output

#### Outcomes

- Integrate and demonstrate the course capabilities through the module's final practical work.

#### Lessons

1. **Structures** — `lesson`
2. **Pointers to structures and self-referential structures** — `lesson`
3. **Unions and bit-fields** — `lesson`
4. **Formatted output and input** — `lesson`
5. **File access with the standard library** — `lesson`
6. **Structures and I/O** — `test`
7. **Model a record file** — `lab` — define a structure, read and write records to a file, and handle malformed input without crashing

### Module 6 — Building & Debugging C Programs

#### Outcomes

- Integrate and demonstrate the course capabilities through the module's final practical work.

#### Lessons

1. **Compiling C** — `lesson`
2. **Linking** — `lesson`
3. **Executables and loading** — `lesson`
4. **Automating builds with Make** — `lesson`
5. **Debugging with GDB** — `lesson`
6. **Finding memory errors with sanitizers** — `lesson`
7. **Source to executable** — `test`
8. **Diagnose a segmentation fault** — `lab` — locate and fix a segmentation fault in an unfamiliar program using the debugger and a sanitizer, recording each hypothesis and its result

### Module 7 — C Data-Structure Library

#### Outcomes

- Integrate and demonstrate the course capabilities through the module's final practical work.

#### Lessons

1. **Build, test, and defend the C Data-Structure Library** — `lab`

## Completion requirements

- Complete the required exercises and checkpoints described in the [public course requirements](requirements/SEF6.md).
- Complete the final integrated `lab` in the last module and meet its observable exit criteria.
- Retain reproducible artifacts, verification results, design explanations, and a technical retrospective as required by the [OEE Evidence Rules](../../spec/evidence-rules.md).
