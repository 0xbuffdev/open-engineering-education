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

- Read and write C values in binary and hexadecimal and explain how integers are stored.
- Write C programs using types, operators, expressions, and control flow.

#### Lessons

1. **Course introduction: C Programming & Machine Memory** — `lesson`

   C is the language closest to the machine that is still widely used. Learning it shows what higher-level languages hide: memory addresses, manual lifetimes, and how source code becomes an executable.
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

- Define functions, explain argument passing, and use scope and `static` correctly.
- Split a program into source and header files.

#### Lessons

1. **Functions and arguments** — `lesson`
2. **Scope and storage** — `lesson`
3. **Header files and multiple source files** — `lesson`
4. **The C preprocessor** — `lesson`
5. **Functions and structure** — `test`
6. **Split a program into modules** — `lab` — reorganize a single-file program into modules with headers and verify that behavior is unchanged

### Module 3 — Addresses & Pointers

#### Outcomes

- Explain addresses and use pointers, including the relationship between pointers and arrays, correctly.
- Pass data to functions by value and by address, and predict the effect.

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

- Describe how a process lays out the stack, the heap, and static data.
- Allocate and release memory with `malloc` and `free`, and recognize leaks, double frees, use after free, and buffer overruns.

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

- Define and use structures, arrays of structures, and pointers to structures.
- Read and write text and formatted data with the standard library.

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

- Explain how C source becomes a linked, loadable executable, and build it with Make.
- Use a debugger and sanitizers to locate memory errors.

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

- Complete and explain the **C Data-Structure Library** integration lab, demonstrating the relevant course outcomes and retained evidence.

#### Lessons

1. **Build, test, and defend the C Data-Structure Library** — `lab`

   **Final integration lab — required work**

   **C Data-Structure Library**

   Implement a small, tested library in C containing a dynamic array, a linked list, and a hash map, each with a documented interface. The library must include:

   - Separate header and source files with a Makefile
   - A test program that exercises normal use and failure cases
   - A clean run under a memory sanitizer, with no leaks or errors
   - A short written comparison of how the same structures manage memory in Python and in C

## Completion requirements

- Complete the required course exercises, checkpoints and evaluated labs below.
- Complete the final integrated `lab` in the last module and meet its observable exit criteria.
- Retain reproducible artifacts, verification results, design explanations, and a technical retrospective as required by the [OEE Evidence Rules](../../spec/evidence-rules.md).

**Required exercises**

**Practical practice:**

- Inspect the bytes of values of different types.
- Trace a pointer program by hand and compare it with real output.
- Repair a program with a leak, a double free, and an overrun.
- Compile and inspect object files.
- Diagnose a segmentation fault with a debugger.

**Exit demonstration:**

The learner can write a multi-file C program, explain every allocation and its lifetime, and explain the path from source code to a running process.
