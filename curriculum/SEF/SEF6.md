# SEF6 — C Programming & Machine Memory

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** [SEF3](SEF3.md), [SEF4](SEF4.md), [SEF5](SEF5.md)
**Duration:** 8 weeks
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
- Recognize defined versus undefined C behavior and enforce ownership, buffer-length and failure-handling contracts.

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
9. **Inspect integer representations** — `lab`

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
6. **Split a program into modules** — `lab`

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
8. **Trace pointers** — `lab`

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
8. **Fix memory errors** — `lab`

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
7. **Model a record file** — `lab`

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
8. **Diagnose a segmentation fault** — `lab`

### Module 7 — C Semantics & Undefined Behavior

#### Outcomes

- Distinguish portable, defined behavior from compiler-dependent assumptions.
- Diagnose or prevent one material error.

#### Lessons

1. **Integer promotions, signedness and overflow** — `lesson`
2. **Arrays, pointer arithmetic and bounds** — `lesson`
3. **Object lifetime and aliasing basics** — `lesson`
4. **Undefined versus implementation-defined behavior** — `lesson`
5. **Const correctness and interfaces** — `lesson`
6. **C Semantics & Undefined Behavior reasoning** — `test`
7. **Repair a C undefined-behavior defect** — `lab`

### Module 8 — Ownership, Interfaces & Defensive Parsing

#### Outcomes

- Build a robust C interface with explicit resource ownership.
- Diagnose or prevent one material error.

#### Lessons

1. **Resource ownership and cleanup paths** — `lesson`
2. **Header contracts and separate compilation** — `lesson`
3. **Buffer lengths and binary/text representation** — `lesson`
4. **Recoverable error returns and diagnostics** — `lesson`
5. **Parser validation and testing malformed inputs** — `lesson`
6. **Ownership, Interfaces & Defensive Parsing reasoning** — `test`
7. **Harden a length-bounded parser** — `lab`

### Module 9 — C Data-Structure Library

#### Outcomes

- Complete and explain the **C Data-Structure Library** integration lab, demonstrating the relevant course outcomes and retained evidence.

#### Lessons

1. **C library memory and API defense** — `test`
2. **Build, test, and defend the C Data-Structure Library** — `lab`

   **Final integration lab — required work**

   **C Data-Structure Library**

   Implement a small, tested library in C containing a dynamic array, a linked list, and a hash map, each with a documented interface. The library must include:

   - Separate header and source files with a Makefile
   - A test program that exercises normal use and failure cases
   - A clean run under a memory sanitizer, with no leaks or errors
   - A short written comparison of how the same structures manage memory in Python and in C
   - Documented caller/library ownership and failure-safe cleanup for all APIs
   - Boundary, collision, growth and allocation-failure tests with clean-checkout instructions

## Completion requirements

- Complete the required course exercises, checkpoints and evaluated labs below.
- Complete the final integrated `lab` in the last module and meet its observable exit criteria.
- Retain reproducible artifacts, verification results, design explanations, and a technical retrospective as required by the [OEE Evidence Rules](../../spec/evidence-rules.md).

Complete these required exercises:

**Practical practice:**

- Inspect the bytes of values of different types.
- Trace a pointer program by hand and compare it with real output.
- Repair a program with a leak, a double free, and an overrun.
- Compile and inspect object files.
- Diagnose a segmentation fault with a debugger.

**Required checkpoints and reproducible labs:**

Each of the nine modules has two reasoning questions with expected-answer guidance and a required lab. A reviewer may substitute equivalent previously unseen examples if they assess the same outcome. Correctness depends on the C11 language contract, declared implementation assumptions, object lifetimes and independently reproducible evidence, not on a single observed output or a sanitizer badge.

**Shared environment and safety:**

Use a nonprivileged local Linux C11-capable compiler (GCC or Clang), Make and a terminal, with a disposable fixture/project directory. Record compiler version, C standard mode, OS architecture, flags and exact commands. Prefer `cc -std=c11 -Wall -Wextra -Wpedantic -g -O0` for beginner debugging; run AddressSanitizer/UndefinedBehaviorSanitizer and leak detection where supported, and document unsupported tools rather than claiming a clean result. Never deliberately run dangerous undefined-behavior examples outside an isolated teaching fixture; a supplied diagnostic report is acceptable when a local sanitizer is unavailable. No paid, networked or privileged service is required.

**Shared assessment rules:**

- Demonstrate the specified normal, boundary, invalid-input and allocation/failure cases. Never infer portable language semantics from an undefined-behavior demonstration.
- Record compile and link commands, actual runtime environment, input fixtures, tool warnings, observed outcomes and comparison with expected values.
- Explain all ownership transfers, resource cleanup and pointer validity, including which claims are implementation-defined rather than guaranteed by C11.
- Remediate incorrect foundational reasoning and reattempt with equivalent unfamiliar inputs. Retain a technical retrospective and an independent clean-checkout reproduction for the final project.

**Module 1 — C Data & Control Flow: checkpoint** — Required assessment details

- **Q1 (free):** Why is it unsafe to assume `char` is signed or that every C implementation has an eight-bit byte?
  - Expected answer and scoring: C defines a byte as `CHAR_BIT` bits and requires CHAR_BIT ≥ 8, not exactly eight. Whether plain char is signed is implementation-defined. Check `CHAR_BIT`, `CHAR_MIN`, `CHAR_MAX` and integer-type bounds, and distinguish representation observations from portable requirements.
- **Q2 (free):** For an unsigned n-bit integer, what is the result of adding 1 to its maximum representable value? Does the same rule apply to signed int?
  - Expected answer and scoring: Unsigned arithmetic wraps modulo 2^n, so the result is zero. Signed overflow is undefined behavior in C11; do not intentionally execute it to discover a 'wraparound' result.

**Module 1 — Inspect integer representations: required lab** — Required assessment details

- **Objective:** Demonstrate the module's stated outcomes through a concrete, inspectable C artifact and defensible memory/error behavior.
- **Prerequisites:** Complete the module lessons and the conceptual checkpoint; use only previously validated interfaces from earlier modules.
- **Environment:** Use a nonprivileged local Linux C11-capable compiler (GCC or Clang), Make and a terminal, with a disposable fixture/project directory. Record compiler version, C standard mode, OS architecture, flags and exact commands. Prefer `cc -std=c11 -Wall -Wextra -Wpedantic -g -O0` for beginner debugging; run AddressSanitizer/UndefinedBehaviorSanitizer and leak detection where supported, and document unsupported tools rather than claiming a clean result. Never deliberately run dangerous undefined-behavior examples outside an isolated teaching fixture; a supplied diagnostic report is acceptable when a local sanitizer is unavailable. No paid, networked or privileged service is required.
- **Procedure:**
  1. Compile a C11 program reporting CHAR_BIT, sizeof and the numeric limits of char, int and unsigned int; record compiler and platform.
  2. Inspect the object representation of initialized unsigned integer values through a pointer to unsigned char and print each byte as a numeric value.
  3. Predict and test the defined unsigned wrap of UINT_MAX + 1u; explain why byte order and integer width cannot be assumed without inspection.
  4. Use a checked conditional before a potentially overflowing signed addition instead of evaluating an overflow expression.
  5. Test zero, one, type maximum and invalid numeric input using a documented parser such as strtol with error and range checks.
- **Expected result:** Compiler reports actual widths; byte dump matches that implementation; UINT_MAX+1u is zero; unsafe signed overflow is avoided by an explicit check.
- **Verification:** Compare output to limits.h bounds and independent calculations; run normal and invalid-input fixtures and explain any implementation-specific byte ordering.
- **Evidence:** Source revision, build/run/test commands, expected-versus-observed fixtures, warnings/diagnostics, ownership notes, negative-case results and technical retrospective.
- **Failure analysis:** Explain a faulty assumption about CHAR_BIT, sign of plain char, byte order, or signed-integer overflow.
- **Acceptance:** The stated behavior and safety contracts are demonstrable under documented tool/environment assumptions, and all required invalid and failure paths are handled. Incomplete ownership, unsupported assertions of safety or unreproduced results block completion.

**Module 2 — Functions & Program Structure: checkpoint** — Required assessment details

- **Q1 (free):** What does placing a non-static function definition in a header included by two C source files risk, and what is a safer organization?
  - Expected answer and scoring: Multiple external definitions may produce a duplicate-symbol error at link time. Put declarations in guarded headers, define ordinary external functions in one .c file, and use static/internal linkage where appropriate. Inline semantics require special care and are not a generic workaround.
- **Q2 (free):** Does passing an int to a C function allow the callee to modify the caller's variable directly? How can the function deliberately change it?
  - Expected answer and scoring: The callee receives a value copy; changing its local parameter does not modify the caller's object. Pass a valid pointer with an explicit contract and assign through it when mutation is intended.

**Module 2 — Split a program into modules: required lab** — Required assessment details

- **Objective:** Demonstrate the module's stated outcomes through a concrete, inspectable C artifact and defensible memory/error behavior.
- **Prerequisites:** Complete the module lessons and the conceptual checkpoint; use only previously validated interfaces from earlier modules.
- **Environment:** Use a nonprivileged local Linux C11-capable compiler (GCC or Clang), Make and a terminal, with a disposable fixture/project directory. Record compiler version, C standard mode, OS architecture, flags and exact commands. Prefer `cc -std=c11 -Wall -Wextra -Wpedantic -g -O0` for beginner debugging; run AddressSanitizer/UndefinedBehaviorSanitizer and leak detection where supported, and document unsupported tools rather than claiming a clean result. Never deliberately run dangerous undefined-behavior examples outside an isolated teaching fixture; a supplied diagnostic report is acceptable when a local sanitizer is unavailable. No paid, networked or privileged service is required.
- **Procedure:**
  1. Start from a small one-file integer-record utility with at least two functions and expected input/output examples.
  2. Split public declarations into a header protected by include guards, implementations into source files, and client use into main.c.
  3. Compile each translation unit separately using C11 flags, link the executable and inspect which build step surfaces a declaration or duplicate-definition error.
  4. Compare normal outputs before and after extraction, test an invalid input and add a contract for pointer-output parameters.
  5. Make and repair a deliberate undefined-reference or duplicate-symbol build failure; document which compiler/linker stage detected it.
- **Expected result:** Multiple translation units compile and link cleanly, output matches original fixtures, and module contracts describe who may modify pointed-to data.
- **Verification:** Run a clean build and distinct compilation/link commands; compare before/after results and test an intentionally incorrect build.
- **Evidence:** Source revision, build/run/test commands, expected-versus-observed fixtures, warnings/diagnostics, ownership notes, negative-case results and technical retrospective.
- **Failure analysis:** Explain a missing include guard, incompatible declaration, duplicate definition, or assuming local parameter rebinding mutates caller state.
- **Acceptance:** The stated behavior and safety contracts are demonstrable under documented tool/environment assumptions, and all required invalid and failure paths are handled. Incomplete ownership, unsupported assertions of safety or unreproduced results block completion.

**Module 3 — Addresses & Pointers: checkpoint** — Required assessment details

- **Q1 (free):** What is printed conceptually by `int x=7; int *p=&x; *p=9;` when x is read afterward? Can a concrete pointer address be predicted between runs?
  - Expected answer and scoring: x becomes 9 because dereferencing p changes the addressed object. Numeric pointer addresses depend on implementation and runtime layout and must not be predicted as portable constants. Use %p with an appropriately converted void* to display an address.
- **Q2 (free):** Why may one-past-the-end pointers be formed but not dereferenced, and when is pointer subtraction valid?
  - Expected answer and scoring: A pointer one past a valid array may be computed for comparison/iteration but cannot be dereferenced. Pointer subtraction is defined only for pointers into the same array object or one past it, with a result representable in ptrdiff_t.

**Module 3 — Trace pointers: required lab** — Required assessment details

- **Objective:** Demonstrate the module's stated outcomes through a concrete, inspectable C artifact and defensible memory/error behavior.
- **Prerequisites:** Complete the module lessons and the conceptual checkpoint; use only previously validated interfaces from earlier modules.
- **Environment:** Use a nonprivileged local Linux C11-capable compiler (GCC or Clang), Make and a terminal, with a disposable fixture/project directory. Record compiler version, C standard mode, OS architecture, flags and exact commands. Prefer `cc -std=c11 -Wall -Wextra -Wpedantic -g -O0` for beginner debugging; run AddressSanitizer/UndefinedBehaviorSanitizer and leak detection where supported, and document unsupported tools rather than claiming a clean result. Never deliberately run dangerous undefined-behavior examples outside an isolated teaching fixture; a supplied diagnostic report is acceptable when a local sanitizer is unavailable. No paid, networked or privileged service is required.
- **Procedure:**
  1. Implement a small program with a local integer, an array of four integers and pointers to their elements; record which objects and addresses each pointer designates.
  2. Draw pointer/object diagrams before and after pointer assignment, dereference and a function modifying an integer by pointer.
  3. Print values and addresses using valid format specifiers (cast object pointers to void* for %p) and use ptrdiff_t for array-index differences.
  4. Exercise indexes 0, last and one-past solely as a pointer position, without accessing invalid storage.
  5. Demonstrate an incorrect predicted value in a written trace and correct it; never dereference an invalid or uninitialized pointer to create evidence.
- **Expected result:** Value mutations and pointer differences agree with object diagrams, within-array pointer operations are defined, and illegal dereferences are avoided.
- **Verification:** Compare manually reasoned values and distances with program output and check compiler warnings; do not require stable absolute addresses.
- **Evidence:** Source revision, build/run/test commands, expected-versus-observed fixtures, warnings/diagnostics, ownership notes, negative-case results and technical retrospective.
- **Failure analysis:** Explain confusing a pointer value with its referent, invalid pointer arithmetic, a missing address-of operator, or an erroneous format argument.
- **Acceptance:** The stated behavior and safety contracts are demonstrable under documented tool/environment assumptions, and all required invalid and failure paths are handled. Incomplete ownership, unsupported assertions of safety or unreproduced results block completion.

**Module 4 — Stack, Heap & Dynamic Memory: checkpoint** — Required assessment details

- **Q1 (free):** What is wrong with returning `&local` when local is an ordinary block-scope automatic variable?
  - Expected answer and scoring: The object's lifetime ends at block exit. Any later use of its former address to access that object is invalid/undefined; return a value or explicitly allocated object with ownership instead.
- **Q2 (free):** How should code handle `realloc(p, n)` failing, and what special case should be guarded rather than assuming realloc zero-size behavior?
  - Expected answer and scoring: Assign realloc's nonnull return to a temporary; when it returns NULL for a positive size, the original allocation remains valid and must still be freed or retained. Treat requested zero size explicitly with a documented free/empty policy because portability and return semantics have special cases.

**Module 4 — Fix memory errors: required lab** — Required assessment details

- **Objective:** Demonstrate the module's stated outcomes through a concrete, inspectable C artifact and defensible memory/error behavior.
- **Prerequisites:** Complete the module lessons and the conceptual checkpoint; use only previously validated interfaces from earlier modules.
- **Environment:** Use a nonprivileged local Linux C11-capable compiler (GCC or Clang), Make and a terminal, with a disposable fixture/project directory. Record compiler version, C standard mode, OS architecture, flags and exact commands. Prefer `cc -std=c11 -Wall -Wextra -Wpedantic -g -O0` for beginner debugging; run AddressSanitizer/UndefinedBehaviorSanitizer and leak detection where supported, and document unsupported tools rather than claiming a clean result. Never deliberately run dangerous undefined-behavior examples outside an isolated teaching fixture; a supplied diagnostic report is acceptable when a local sanitizer is unavailable. No paid, networked or privileged service is required.
- **Procedure:**
  1. Prepare a bounded heap-backed integer buffer with a clear owner and a size/capacity contract; allocate, write, grow and free it.
  2. Use an injectable allocation wrapper or test double to simulate a failed positive-size allocation/reallocation without depending on real out-of-memory conditions.
  3. Test successful allocation, zero-length policy, growth, overflow-safe element-count multiplication and cleanup on every error path.
  4. For teaching diagnostics, inspect a supplied sanitizer report or run a dedicated disposable failing example under AddressSanitizer when available; do not rely on undefined behavior's visible outcome.
  5. Repair a seeded leak, unsafe growth pattern or double-free path and record before/after tests and sanitizer or equivalent diagnostic evidence.
- **Expected result:** Buffer contents survive successful growth, simulated allocation failure does not lose ownership, and cleanup occurs once per acquired allocation.
- **Verification:** Run memory/error-path tests and compiler warnings; use ASan/LeakSanitizer where supported, or clearly document an alternate inspection method and its limitations.
- **Evidence:** Source revision, build/run/test commands, expected-versus-observed fixtures, warnings/diagnostics, ownership notes, negative-case results and technical retrospective.
- **Failure analysis:** Explain lost ownership after assigning realloc directly, returning a pointer to an expired local, double free or unchecked size multiplication.
- **Acceptance:** The stated behavior and safety contracts are demonstrable under documented tool/environment assumptions, and all required invalid and failure paths are handled. Incomplete ownership, unsupported assertions of safety or unreproduced results block completion.

**Module 5 — Structures & Input/Output: checkpoint** — Required assessment details

- **Q1 (free):** Can a structure be written to disk using `fwrite(&record,sizeof record,1,f)` and safely treated as a portable interoperable record format?
  - Expected answer and scoring: No. Structure padding, integer representation, endianness, alignment and implementation differences make raw object layouts unsuitable as a portable interchange format. Define a text or explicitly serialized binary schema.
- **Q2 (free):** How does `fgets` behave when a line is longer than the input buffer, and what must a parser check?
  - Expected answer and scoring: It reads at most n−1 characters then terminates with NUL; an overlong line can be split across reads. Detect missing newline and drain/reject or accumulate within an explicit limit; handle EOF/errors distinctly. Do not assume one fgets call always yields a full record.

**Module 5 — Model a record file: required lab** — Required assessment details

- **Objective:** Demonstrate the module's stated outcomes through a concrete, inspectable C artifact and defensible memory/error behavior.
- **Prerequisites:** Complete the module lessons and the conceptual checkpoint; use only previously validated interfaces from earlier modules.
- **Environment:** Use a nonprivileged local Linux C11-capable compiler (GCC or Clang), Make and a terminal, with a disposable fixture/project directory. Record compiler version, C standard mode, OS architecture, flags and exact commands. Prefer `cc -std=c11 -Wall -Wextra -Wpedantic -g -O0` for beginner debugging; run AddressSanitizer/UndefinedBehaviorSanitizer and leak detection where supported, and document unsupported tools rather than claiming a clean result. Never deliberately run dangerous undefined-behavior examples outside an isolated teaching fixture; a supplied diagnostic report is acceptable when a local sanitizer is unavailable. No paid, networked or privileged service is required.
- **Procedure:**
  1. Define a small text-based record schema with an integer id and bounded name, selecting a delimiter rule and maximum line length.
  2. Implement a struct for parsed data and separate functions for line reading, validation and displaying records.
  3. Use fgets and checked numeric conversion, then reject malformed, missing, duplicate or overlong fields with documented error status.
  4. Test empty file, final line without newline, overlong line, invalid numeric ID and a valid multi-record fixture.
  5. Show that replacing the explicit encoding with raw structure-byte fwrite would not establish a portable schema; document the intended serialization policy.
- **Expected result:** Valid records round-trip through the declared text schema, malformed/oversize lines fail safely, and memory/file resources are released.
- **Verification:** Compare parsed data with independently specified fixtures, run under warnings/sanitizers where supported and inspect error statuses.
- **Evidence:** Source revision, build/run/test commands, expected-versus-observed fixtures, warnings/diagnostics, ownership notes, negative-case results and technical retrospective.
- **Failure analysis:** Explain unchecked sscanf assumptions, truncated line accepted as complete, buffer overflow, or an implicit structure-padding dependency.
- **Acceptance:** The stated behavior and safety contracts are demonstrable under documented tool/environment assumptions, and all required invalid and failure paths are handled. Incomplete ownership, unsupported assertions of safety or unreproduced results block completion.

**Module 6 — Building & Debugging C Programs: checkpoint** — Required assessment details

- **Q1 (free):** What is the difference between preprocessing, compilation, linking and loading? Which stage reports a missing external function definition?
  - Expected answer and scoring: Preprocessing handles directives, compilation translates source to object code and identifies source issues, linking resolves symbol references and builds an executable, and the OS loader maps and starts it. A missing external definition normally produces a linker error when referenced.
- **Q2 (free):** Can an AddressSanitizer clean run prove that a C program contains no undefined behavior or memory defects?
  - Expected answer and scoring: No. A sanitizer run covers executed paths and the classes it instruments. It cannot prove correctness or absence of all UB, and tools, platforms and optimization affect findings. Complement it with bounds reasoning, tests, warnings and review.

**Module 6 — Diagnose a segmentation fault: required lab** — Required assessment details

- **Objective:** Demonstrate the module's stated outcomes through a concrete, inspectable C artifact and defensible memory/error behavior.
- **Prerequisites:** Complete the module lessons and the conceptual checkpoint; use only previously validated interfaces from earlier modules.
- **Environment:** Use a nonprivileged local Linux C11-capable compiler (GCC or Clang), Make and a terminal, with a disposable fixture/project directory. Record compiler version, C standard mode, OS architecture, flags and exact commands. Prefer `cc -std=c11 -Wall -Wextra -Wpedantic -g -O0` for beginner debugging; run AddressSanitizer/UndefinedBehaviorSanitizer and leak detection where supported, and document unsupported tools rather than claiming a clean result. Never deliberately run dangerous undefined-behavior examples outside an isolated teaching fixture; a supplied diagnostic report is acceptable when a local sanitizer is unavailable. No paid, networked or privileged service is required.
- **Procedure:**
  1. Build a small multi-file C program using Make, with a debug configuration (-g -O0) and warnings enabled.
  2. Use a provided, disposable program with an out-of-bounds access that is diagnosed by a supported sanitizer or supplied diagnostic report; never interpret arbitrary crash behavior as a reliable result.
  3. Use GDB where available to inspect a backtrace and local state for a controlled failure; document alternatives when debugger support is unavailable.
  4. Repair the bound check, run the original failing fixture and all normal/boundary tests and check no remaining reported sanitizer issues on executed paths.
  5. Explain one compile-time error, one linker error and one runtime failure using separate known fixtures.
- **Expected result:** Clean build succeeds, the seeded defect is isolated and repaired, and the relevant tested path no longer triggers the diagnostic.
- **Verification:** Compare compiler/linker/runtime logs, debugger backtrace and repeated regression tests, retaining platform/tool versions.
- **Evidence:** Source revision, build/run/test commands, expected-versus-observed fixtures, warnings/diagnostics, ownership notes, negative-case results and technical retrospective.
- **Failure analysis:** Explain confusing a link error with a segfault, using uninitialized data for diagnosis, or overstating sanitizer coverage.
- **Acceptance:** The stated behavior and safety contracts are demonstrable under documented tool/environment assumptions, and all required invalid and failure paths are handled. Incomplete ownership, unsupported assertions of safety or unreproduced results block completion.

**Module 7 — C Semantics & Undefined Behavior: checkpoint** — Required assessment details

- **Q1 (free):** What happens in strictly conforming C11 when signed int addition exceeds INT_MAX? Does observing a wrapped number on one machine define it?
  - Expected answer and scoring: Signed overflow is undefined behavior; one observed outcome does not establish its semantics. Validate operands before addition or use a documented wider/unsigned type with appropriate checks.
- **Q2 (free):** What is the difference between unspecified, implementation-defined and undefined behavior? Give one relevant example.
  - Expected answer and scoring: Implementation-defined requires an implementation-documented choice (such as signedness of plain char); unspecified permits a set of valid possibilities without mandating documentation; undefined imposes no requirements (e.g. out-of-bounds array access). Distinguish each from guaranteed portable behavior.

**Module 7 — Repair a C undefined-behavior defect: required lab** — Required assessment details

- **Objective:** Demonstrate the module's stated outcomes through a concrete, inspectable C artifact and defensible memory/error behavior.
- **Prerequisites:** Complete the module lessons and the conceptual checkpoint; use only previously validated interfaces from earlier modules.
- **Environment:** Use a nonprivileged local Linux C11-capable compiler (GCC or Clang), Make and a terminal, with a disposable fixture/project directory. Record compiler version, C standard mode, OS architecture, flags and exact commands. Prefer `cc -std=c11 -Wall -Wextra -Wpedantic -g -O0` for beginner debugging; run AddressSanitizer/UndefinedBehaviorSanitizer and leak detection where supported, and document unsupported tools rather than claiming a clean result. Never deliberately run dangerous undefined-behavior examples outside an isolated teaching fixture; a supplied diagnostic report is acceptable when a local sanitizer is unavailable. No paid, networked or privileged service is required.
- **Procedure:**
  1. Examine a provided arithmetic operation accepting user-supplied integers and establish its valid input bounds.
  2. Write a safe checked-addition routine for signed int, rejecting overflow before evaluating an invalid sum; test INT_MAX, INT_MIN, positive/negative values and zero.
  3. Add a bounded array-index example and test the one-past boundary without accessing out-of-range elements.
  4. Use compiler diagnostics and UBSan when supported to study a separate contained defective fixture or a provided report; repair before using the program for further tasks.
  5. Document which type widths and char signedness are implementation choices and which operations are undefined regardless of observed output.
- **Expected result:** Valid arithmetic matches hand calculations; overflow and out-of-bounds requests are rejected before the invalid operation; repaired tests pass.
- **Verification:** Assert acceptance/rejection against limits.h and reference arithmetic; retain diagnostic/warning logs and tool constraints.
- **Evidence:** Source revision, build/run/test commands, expected-versus-observed fixtures, warnings/diagnostics, ownership notes, negative-case results and technical retrospective.
- **Failure analysis:** Explain treating signed wrap as portable, evaluating overflow in a check, or believing every UB case must crash.
- **Acceptance:** The stated behavior and safety contracts are demonstrable under documented tool/environment assumptions, and all required invalid and failure paths are handled. Incomplete ownership, unsupported assertions of safety or unreproduced results block completion.

**Module 8 — Ownership, Interfaces & Defensive Parsing: checkpoint** — Required assessment details

- **Q1 (free):** A parser receives pointer p and claimed length n. Why is it insufficient to check for a terminating NUL by calling strlen(p) blindly?
  - Expected answer and scoring: The buffer might not contain a NUL within its valid extent, so strlen may read past the object. Define a (pointer,length) contract, validate using bounded operations and never read beyond n or assume the pointer remains valid.
- **Q2 (free):** Who frees a buffer returned by a parsing function? How should its header state ownership and failure behavior?
  - Expected answer and scoring: There is no universal default; the function's public API must state who owns returned allocations, who frees them, whether inputs are borrowed and whether output parameters remain unchanged/initialized on failure. Error codes and cleanup must be deterministic.

**Module 8 — Harden a length-bounded parser: required lab** — Required assessment details

- **Objective:** Demonstrate the module's stated outcomes through a concrete, inspectable C artifact and defensible memory/error behavior.
- **Prerequisites:** Complete the module lessons and the conceptual checkpoint; use only previously validated interfaces from earlier modules.
- **Environment:** Use a nonprivileged local Linux C11-capable compiler (GCC or Clang), Make and a terminal, with a disposable fixture/project directory. Record compiler version, C standard mode, OS architecture, flags and exact commands. Prefer `cc -std=c11 -Wall -Wextra -Wpedantic -g -O0` for beginner debugging; run AddressSanitizer/UndefinedBehaviorSanitizer and leak detection where supported, and document unsupported tools rather than claiming a clean result. Never deliberately run dangerous undefined-behavior examples outside an isolated teaching fixture; a supplied diagnostic report is acceptable when a local sanitizer is unavailable. No paid, networked or privileged service is required.
- **Procedure:**
  1. Write a parser for a simple length-prefixed or delimiter-framed record using (const unsigned char *data,size_t length) and a documented maximum record length.
  2. Specify ownership of every input and output, validate minimum header, length arithmetic, complete payload and trailing-byte policy before allocating.
  3. Test empty, truncated header, truncated body, oversized advertised length, embedded NUL, exact-size boundary and simulated allocation failure.
  4. Write unit tests using fixed byte arrays with explicit lengths; ensure no parser path reads one byte beyond length or leaks allocated output.
  5. Verify the parser contract and demonstrate that malformed inputs return an error without leaving unowned resources behind.
- **Expected result:** Valid input parses into the declared result; malformed, oversized and truncated records are rejected predictably and all resource paths are accounted for.
- **Verification:** Compare status, values, output-ownership state and memory diagnostics with independent fixture expectations.
- **Evidence:** Source revision, build/run/test commands, expected-versus-observed fixtures, warnings/diagnostics, ownership notes, negative-case results and technical retrospective.
- **Failure analysis:** Explain unbounded strlen, unchecked addition leading to size overflow, ambiguous ownership, or a partially initialized output after error.
- **Acceptance:** The stated behavior and safety contracts are demonstrable under documented tool/environment assumptions, and all required invalid and failure paths are handled. Incomplete ownership, unsupported assertions of safety or unreproduced results block completion.

**Module 9 — C Data-Structure Library: checkpoint** — Required assessment details

- **Q1 (free):** Why is resizing a dynamic array by multiplying capacity by two risky without checking sizes? What conditions ensure safe growth?
  - Expected answer and scoring: Capacity and byte-size multiplication can overflow size_t, causing undersized allocation. Check needed_count, available bound SIZE_MAX / sizeof element, and chosen growth policy before allocation; preserve original pointer and capacity on failed realloc.
- **Q2 (free):** What should an ownership contract say when a hash map stores a pointer supplied by the caller? What happens on replacement or removal?
  - Expected answer and scoring: Define borrowed versus copied/owned keys and values, their lifetimes, whether replacing frees old content, how removal transfers or destroys ownership and how failures leave the map. A hash collision must be resolved by a documented policy, not mistaken for key equality.

**Module 9 — Build, test, and defend the C Data-Structure Library: required lab** — Required assessment details

- **Objective:** Demonstrate the module's stated outcomes through a concrete, inspectable C artifact and defensible memory/error behavior.
- **Prerequisites:** Complete the module lessons and the conceptual checkpoint; use only previously validated interfaces from earlier modules.
- **Environment:** Use a nonprivileged local Linux C11-capable compiler (GCC or Clang), Make and a terminal, with a disposable fixture/project directory. Record compiler version, C standard mode, OS architecture, flags and exact commands. Prefer `cc -std=c11 -Wall -Wextra -Wpedantic -g -O0` for beginner debugging; run AddressSanitizer/UndefinedBehaviorSanitizer and leak detection where supported, and document unsupported tools rather than claiming a clean result. Never deliberately run dangerous undefined-behavior examples outside an isolated teaching fixture; a supplied diagnostic report is acceptable when a local sanitizer is unavailable. No paid, networked or privileged service is required.
- **Procedure:**
  1. Implement separate header/source files for an integer dynamic array, singly linked list and a hash map with a documented key/value ownership policy.
  2. Define initialization, insert/add, lookup/read, delete/remove and destruction contracts, including invalid arguments, out-of-memory and duplicate-key behavior.
  3. Implement bounds/capacity checks for dynamic arrays, failure-safe allocation and cleanup for all three structures; implement and test actual hash collisions and resizing or a documented fixed-capacity policy.
  4. Provide a Makefile with clean/rebuild/test targets and independent deterministic tests for empty, singleton, growth, collision, repeated insertion, removal and fault-injected allocation failure.
  5. Run warnings-enabled builds and ASan/UBSan/LeakSanitizer or an available comparable memory diagnostic on representative tests; disclose absent tooling instead of claiming untested clean runs.
  6. Document an outcomes-to-evidence map and Python-versus-C lifetime comparison, then have a reviewer reproduce one normal path and one failure path from clean checkout.
- **Expected result:** Each structure satisfies its documented API with correct data preservation, expected collision/duplicate semantics and no observed leaks or invalid accesses on tested paths.
- **Verification:** Build/test from scratch, compare with independent small reference sequences, retain sanitizer results for executed fixtures and check resource cleanup after injected failure.
- **Evidence:** Source revision, build/run/test commands, expected-versus-observed fixtures, warnings/diagnostics, ownership notes, negative-case results and technical retrospective.
- **Failure analysis:** Explain an incorrect ownership transfer, failed realloc losing original allocation, hash collision mishandling, dangling link or uninitialized slot.
- **Acceptance:** The stated behavior and safety contracts are demonstrable under documented tool/environment assumptions, and all required invalid and failure paths are handled. Incomplete ownership, unsupported assertions of safety or unreproduced results block completion.

**Exit demonstration:**

The learner can write a multi-file C program, explain every allocation and its lifetime, and explain the path from source code to a running process.
