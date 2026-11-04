> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

# SEF6 — C Programming & Machine Memory

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** SEF3, SEF4, SEF5
**Duration:** 6 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

## Overview

This course teaches C as a way to see and control the machine. Learners write multi-file C programs, reason about types and their binary representations, use pointers and addresses, trace how stack and heap memory are used, build programs with a compiler and Make, and diagnose memory errors with a debugger and sanitizers. It builds directly on the name, object, and call-stack model from SEF2 by showing what that model hides.

## Course brief

The course introduction is the first lesson of the first module. It combines the overview above with these fields.

- **Introduction:** C is the language closest to the machine that is still widely used. Learning it shows what higher-level languages hide: memory addresses, manual lifetimes, and how source code becomes an executable.
- **History:** Dennis Ritchie created C at Bell Labs in 1972 and 1973, and Unix was rewritten in it in 1973. The book by Kernighan and Ritchie in 1978 defined the language informally, and ANSI standardized it in 1989.
- **Usage:** The learner writes multi-file C programs, builds them with a compiler and Make, and debugs them with GDB and sanitizers.
- **Applications:** Operating system kernels, embedded firmware, databases, language runtimes, and libraries that must be fast.
- **Strengths:** Performance is predictable, the runtime is small, the programmer controls memory directly, and an enormous body of existing code is written in C.
- **Limitations:** C has no bounds checking and leaves many mistakes undefined, and manual memory management makes memory errors and security vulnerabilities common.
- **Key concepts:** type; pointer; address; array; structure; stack; heap; malloc and free; header file; compiler; linker; Make; debugger; sanitizer

## Prerequisites

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

#### Module brief

- **Introduction:** C exposes how data really sits in memory. This module introduces C's types and control flow and the binary representation underneath.
- **Overview:** It covers C types and values, operators, control flow, binary and hexadecimal, integer representation, and text as bytes.
- **History:** Dennis Ritchie created C at Bell Labs in 1972 and 1973, and Unix was rewritten in it in 1973. Kernighan and Ritchie published The C Programming Language in 1978, and ANSI standardized C in 1989.
- **Limitations:** There is no bounds checking, many mistakes cause undefined behavior, and integer overflow gives no warning.
- **Key concepts:** type; size; signed and unsigned; hexadecimal; overflow; operators; control flow; characters

#### Module outcomes

By the end of this module, the learner can:

- Read and write C values in binary and hexadecimal and explain how integers are stored.
- Write C programs using types, operators, expressions, and control flow.

1. **Course introduction: C Programming & Machine Memory** — what the subject is, where it came from, where it is used, and its strengths and limits
2. **Introduction: C Data & Control Flow** — what the topic is, where it is used, and its strengths and limits
3. **C types and values**
4. **Operators and expressions**
5. **C control flow**
6. **Binary and hexadecimal**
7. **Integer representation**
8. **Characters and text**
9. **C data and binary**
   - kind: `test`
10. **Inspect integer representations** — print the bytes of values of different types, predict the output first, and explain overflow and sign behavior

- kind: `lab`

### Module 2 — Functions & Program Structure

#### Module brief

- **Introduction:** Larger C programs are split across files. This module teaches how functions, scope, and headers fit together.
- **Overview:** It covers functions and arguments, scope and storage, header files, multiple source files, and the preprocessor.
- **Limitations:** Headers are text copied in by the preprocessor, so careless macros and duplicate declarations cause confusing errors.
- **Key concepts:** function; scope; static; header file; declaration and definition; preprocessor; macro

#### Module outcomes

By the end of this module, the learner can:

- Define functions, explain argument passing, and use scope and `static` correctly.
- Split a program into source and header files.

1. **Introduction: Functions & Program Structure** — what the topic is, where it is used, and its strengths and limits
2. **Functions and arguments**
3. **Scope and storage**
4. **Header files and multiple source files**
5. **The C preprocessor**
6. **Functions and structure**
   - kind: `test`
7. **Split a program into modules** — reorganize a single-file program into modules with headers and verify that behavior is unchanged
   - kind: `lab`

### Module 3 — Addresses & Pointers

#### Module brief

- **Introduction:** A pointer is an address stored in a variable. It is the central idea that makes C powerful and dangerous.
- **Overview:** It covers addresses, pointers, passing addresses to functions, pointers and arrays, address arithmetic, and strings.
- **History:** Dennis Ritchie refined C's pointer and array design in the early 1970s from the earlier B language.
- **Strengths:** They give direct and efficient access to memory and allow flexible data structures.
- **Limitations:** An invalid pointer causes crashes and security vulnerabilities, and pointer arithmetic has no safety net.
- **Key concepts:** address; pointer; dereference; pass by address; arrays and pointers; pointer arithmetic; string

#### Module outcomes

By the end of this module, the learner can:

- Explain addresses and use pointers, including the relationship between pointers and arrays, correctly.
- Pass data to functions by value and by address, and predict the effect.

1. **Introduction: Addresses & Pointers** — what the topic is, where it is used, and its strengths and limits
2. **Addresses**
3. **Pointers**
4. **Pointers and function arguments**
5. **Pointers and arrays**
6. **Address arithmetic**
7. **Strings as arrays of characters**
8. **Values and addresses**
   - kind: `test`
9. **Trace pointers** — trace a program that uses pointers by hand, record each address and value, and compare the trace with real output
   - kind: `lab`

### Module 4 — Stack, Heap & Dynamic Memory

#### Module brief

- **Introduction:** Where a value lives decides how long it lives. This module shows the layout of a process's memory and how to manage it by hand.
- **Overview:** It covers the address space, stack frames, heap allocation with malloc and free, lifetime errors, buffer overruns, and a comparison with Python's model.
- **Strengths:** The programmer has full control over memory use and lifetime, with no hidden pauses.
- **Limitations:** Leaks, double frees, use after free, and overruns are the programmer's responsibility.
- **Key concepts:** address space; stack frame; heap; malloc and free; leak; double free; dangling pointer; overrun

#### Module outcomes

By the end of this module, the learner can:

- Describe how a process lays out the stack, the heap, and static data.
- Allocate and release memory with `malloc` and `free`, and recognize leaks, double frees, use after free, and buffer overruns.

1. **Introduction: Stack, Heap & Dynamic Memory** — what the topic is, where it is used, and its strengths and limits
2. **Address space of a process**
3. **Stack frames and function calls**
4. **Heap allocation with `malloc` and `free`**
5. **Lifetime errors: leaks, double free, and dangling pointers**
6. **Buffer overruns**
7. **C and Python lifetimes compared**
8. **Memory behavior**
   - kind: `test`
9. **Fix memory errors** — repair a program containing a leak, a double free, and an overrun, and explain how each corrupts or wastes memory
   - kind: `lab`

### Module 5 — Structures & Input/Output

#### Module brief

- **Introduction:** Real data has several fields. Structures group them, and the standard library moves them in and out of programs.
- **Overview:** It covers structures, pointers to structures, self-referential structures, unions and bit-fields, formatted input and output, and file access.
- **Limitations:** Layout includes padding that differs between machines, so writing structures directly to files is not portable, and formatted input is easy to misuse.
- **Key concepts:** structure; member access; padding; union; bit-field; formatted I/O; file stream

#### Module outcomes

By the end of this module, the learner can:

- Define and use structures, arrays of structures, and pointers to structures.
- Read and write text and formatted data with the standard library.

1. **Introduction: Structures & Input/Output** — what the topic is, where it is used, and its strengths and limits
2. **Structures**
3. **Pointers to structures and self-referential structures**
4. **Unions and bit-fields**
5. **Formatted output and input**
6. **File access with the standard library**
7. **Structures and I/O**
   - kind: `test`
8. **Model a record file** — define a structure, read and write records to a file, and handle malformed input without crashing
   - kind: `lab`

### Module 6 — Building & Debugging C Programs

#### Module brief

- **Introduction:** A C program becomes an executable through several tools, and failures often hide in that pipeline. This module explains the pipeline and the tools for diagnosing memory errors.
- **Overview:** It covers compiling, linking, executables and loading, Make, debugging with GDB, and sanitizers.
- **History:** Stuart Feldman wrote Make at Bell Labs in 1976, and Richard Stallman began GDB in 1986 for the GNU project.
- **Limitations:** Build configurations are brittle, linker errors are cryptic, and some errors appear only in optimized builds.
- **Key concepts:** compiler; object file; linker; symbol; executable; loader; Make; breakpoint; backtrace; sanitizer

#### Module outcomes

By the end of this module, the learner can:

- Explain how C source becomes a linked, loadable executable, and build it with Make.
- Use a debugger and sanitizers to locate memory errors.

1. **Introduction: Building & Debugging C Programs** — what the topic is, where it is used, and its strengths and limits
2. **Compiling C**
3. **Linking**
4. **Executables and loading**
5. **Automating builds with Make**
6. **Debugging with GDB**
7. **Finding memory errors with sanitizers**
8. **Source to executable**
   - kind: `test`
9. **Diagnose a segmentation fault** — locate and fix a segmentation fault in an unfamiliar program using the debugger and a sanitizer, recording each hypothesis and its result
   - kind: `lab`

### Module 7 — C Data-Structure Library

#### Module brief

- **Introduction:** This lab integrates the course. The learner builds a tested C library of familiar data structures and defends its memory behavior.
- **Overview:** It combines multi-file structure, pointers, dynamic allocation, a Makefile, tests, and a clean sanitizer run.
- **Applications:** Language runtimes, databases, and operating systems are built from libraries of this kind.
- **Key concepts integrated:** pointers; allocation; lifetime; modular structure; build automation; debugging

1. **Build, test, and defend the C Data-Structure Library**
   - kind: `lab`

## Topics

- C types and values
- Binary and hexadecimal representation
- Integer representation
- Control flow
- Functions and scope
- Header files and the preprocessor
- Addresses and pointers
- Arrays, strings, and pointer arithmetic
- Structures
- The stack and the heap
- Dynamic allocation
- Memory errors
- Compilation and linking
- Make
- Debugging with GDB
- Sanitizers
- Standard library input and output

## Practical exercises

2. Inspect the bytes of values of different types.
3. Trace a pointer program by hand and compare it with real output.
4. Repair a program with a leak, a double free, and an overrun.
5. Compile and inspect object files.
6. Diagnose a segmentation fault with a debugger.

## Course lab

**C Data-Structure Library**

Implement a small, tested library in C containing a dynamic array, a linked list, and a hash map, each with a documented interface. The library must include:

- Separate header and source files with a Makefile
- A test program that exercises normal use and failure cases
- A clean run under a memory sanitizer, with no leaks or errors
- A short written comparison of how the same structures manage memory in Python and in C

## Exit check

The learner can write a multi-file C program, explain every allocation and its lifetime, and explain the path from source code to a running process.
