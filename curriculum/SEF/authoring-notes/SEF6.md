# SEF6 — Lesson authoring notes

> Optional instructional context preserved from the original source. These are not required course metadata, assessments or module briefs.

## Course orientation

- **Introduction:** C is the language closest to the machine that is still widely used. Learning it shows what higher-level languages hide: memory addresses, manual lifetimes, and how source code becomes an executable.
- **History:** Dennis Ritchie created C at Bell Labs in 1972 and 1973, and Unix was rewritten in it in 1973. The book by Kernighan and Ritchie in 1978 defined the language informally, and ANSI standardized it in 1989.
- **Usage:** The learner writes multi-file C programs, builds them with a compiler and Make, and debugs them with GDB and sanitizers.
- **Applications:** Operating system kernels, embedded firmware, databases, language runtimes, and libraries that must be fast.
- **Strengths:** Performance is predictable, the runtime is small, the programmer controls memory directly, and an enormous body of existing code is written in C.
- **Limitations:** C has no bounds checking and leaves many mistakes undefined, and manual memory management makes memory errors and security vulnerabilities common.
- **Key concepts:** type; pointer; address; array; structure; stack; heap; malloc and free; header file; compiler; linker; Make; debugger; sanitizer

## Module 1 — C Data & Control Flow

- **Introduction:** C exposes how data really sits in memory. This module introduces C's types and control flow and the binary representation underneath.
- **Overview:** It covers C types and values, operators, control flow, binary and hexadecimal, integer representation, and text as bytes.
- **History:** Dennis Ritchie created C at Bell Labs in 1972 and 1973, and Unix was rewritten in it in 1973. Kernighan and Ritchie published The C Programming Language in 1978, and ANSI standardized C in 1989.
- **Limitations:** There is no bounds checking, many mistakes cause undefined behavior, and integer overflow gives no warning.
- **Key concepts:** type; size; signed and unsigned; hexadecimal; overflow; operators; control flow; characters

## Module 2 — Functions & Program Structure

- **Introduction:** Larger C programs are split across files. This module teaches how functions, scope, and headers fit together.
- **Overview:** It covers functions and arguments, scope and storage, header files, multiple source files, and the preprocessor.
- **Limitations:** Headers are text copied in by the preprocessor, so careless macros and duplicate declarations cause confusing errors.
- **Key concepts:** function; scope; static; header file; declaration and definition; preprocessor; macro

## Module 3 — Addresses & Pointers

- **Introduction:** A pointer is an address stored in a variable. It is the central idea that makes C powerful and dangerous.
- **Overview:** It covers addresses, pointers, passing addresses to functions, pointers and arrays, address arithmetic, and strings.
- **History:** Dennis Ritchie refined C's pointer and array design in the early 1970s from the earlier B language.
- **Strengths:** They give direct and efficient access to memory and allow flexible data structures.
- **Limitations:** An invalid pointer causes crashes and security vulnerabilities, and pointer arithmetic has no safety net.
- **Key concepts:** address; pointer; dereference; pass by address; arrays and pointers; pointer arithmetic; string

## Module 4 — Stack, Heap & Dynamic Memory

- **Introduction:** Where a value lives decides how long it lives. This module shows the layout of a process's memory and how to manage it by hand.
- **Overview:** It covers the address space, stack frames, heap allocation with malloc and free, lifetime errors, buffer overruns, and a comparison with Python's model.
- **Strengths:** The programmer has full control over memory use and lifetime, with no hidden pauses.
- **Limitations:** Leaks, double frees, use after free, and overruns are the programmer's responsibility.
- **Key concepts:** address space; stack frame; heap; malloc and free; leak; double free; dangling pointer; overrun

## Module 5 — Structures & Input/Output

- **Introduction:** Real data has several fields. Structures group them, and the standard library moves them in and out of programs.
- **Overview:** It covers structures, pointers to structures, self-referential structures, unions and bit-fields, formatted input and output, and file access.
- **Limitations:** Layout includes padding that differs between machines, so writing structures directly to files is not portable, and formatted input is easy to misuse.
- **Key concepts:** structure; member access; padding; union; bit-field; formatted I/O; file stream

## Module 6 — Building & Debugging C Programs

- **Introduction:** A C program becomes an executable through several tools, and failures often hide in that pipeline. This module explains the pipeline and the tools for diagnosing memory errors.
- **Overview:** It covers compiling, linking, executables and loading, Make, debugging with GDB, and sanitizers.
- **History:** Stuart Feldman wrote Make at Bell Labs in 1976, and Richard Stallman began GDB in 1986 for the GNU project.
- **Limitations:** Build configurations are brittle, linker errors are cryptic, and some errors appear only in optimized builds.
- **Key concepts:** compiler; object file; linker; symbol; executable; loader; Make; breakpoint; backtrace; sanitizer

## Module 7 — C Data-Structure Library

- **Introduction:** This lab integrates the course. The learner builds a tested C library of familiar data structures and defends its memory behavior.
- **Overview:** It combines multi-file structure, pointers, dynamic allocation, a Makefile, tests, and a clean sanitizer run.
- **Applications:** Language runtimes, databases, and operating systems are built from libraries of this kind.
- **Key concepts integrated:** pointers; allocation; lifetime; modular structure; build automation; debugging

1. **Build, test, and defend the C Data-Structure Library**
   - kind: `lab`

## Original topic inventory

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
