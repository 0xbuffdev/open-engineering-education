## SYS2 — Systems Programming with C & Rust

**Duration:** 6 weeks
**Expected workload:** 10–15 focused hours/week
**Prerequisite:** SYS1

### Overview

Work with Unix processes, memory allocation, files, system calls, and resource lifetimes in C and Rust. The course uses side-by-side implementations to make memory safety and ownership meaningful rather than abstract.

### Prerequisites

**SYS1 — Computer Architecture, Memory & Performance**

**Kind:** `course`

### Learning outcomes

By the end of the course, you will be able to:

- Use Unix system interfaces to interact with processes, files, and operating-system resources.
- Reason about resource ownership and lifetime in systems programs.
- Inspect and diagnose low-level memory and process behavior.
- Compare manual memory-management risks with Rust ownership and borrowing.
- Build a multi-module systems utility and test its failure and cleanup paths.


### Resource map

**Required**

- **B5** Ch. 3–7, 13–14, 20–22, 24–27, 37 and 44 (with §§6.3–6.4) · **B4** Ch. 2, 4–6 and 13–15 · **B2** Ch. 4–5 and §8.7 — local library.
- **B15** Ch. 4, 9, 10 (§10.3), 12, 15 (§15.3) and 20 (§20.1) — ownership, errors, lifetimes, a CLI project, Drop, unsafe Rust.
- **R36** Meet Safe and Unsafe; Obligatory Resource Management; Unwinding; Foreign Function Interface.

**Optional**

- **R42** Command-line apps in Rust.

### Modules

#### Module 1 — Unix Processes & Resources

**Reading:** **B5** Ch. 6 (Processes), Ch. 24 (Process Creation), Ch. 25 (Process Termination), Ch. 26 (Monitoring Child Processes), Ch. 27 (Program Execution). **B4** Ch. 4 (The Abstraction: The Process), Ch. 5 (Interlude: Process API), Ch. 6 (Mechanism: Limited Direct Execution). **B15** Ch. 4 §4.1 (What Is Ownership?), Ch. 15 §15.3 (Running Code on Cleanup with the Drop Trait).


### Module outcomes

By the end of this module, the learner can:

- Explain **Unix process model and process creation** in the context of the course.
- Apply **Resource ownership and lifetime** in a problem, implementation, experiment, or design decision.

1. **Unix process model and process creation**
   - kind: `lesson`
2. **Resource ownership and lifetime**
   - kind: `lesson`
3. **Checkpoint: process and resource reasoning**
   - kind: `test`

4. **Micro-lab: Track which component owns each file descriptor or allocated resource.**
   - kind: `lab`
#### Module 2 — Memory & System Calls

**Reading:** **B5** Ch. 3 (System Programming Concepts), Ch. 4 (File I/O: The Universal I/O Model), Ch. 5 (File I/O: Further Details), Ch. 7 (Memory Allocation), §§6.3–6.4 (memory layout; virtual memory management). **B4** Ch. 13 (Address Spaces), Ch. 14 (Interlude: Memory API), Ch. 15 (Mechanism: Address Translation). **B2** §8.7 (A Storage Allocator).


### Module outcomes

By the end of this module, the learner can:

- Explain **Memory allocation and address spaces** in the context of the course.
- Apply **Files, descriptors, and system calls** in a problem, implementation, experiment, or design decision.

1. **Memory allocation and address spaces**
   - kind: `lesson`
2. **Files, descriptors, and system calls**
   - kind: `lesson`
3. **Checkpoint: system interfaces**
   - kind: `test`

4. **Micro-lab: Observe a system call boundary and explain its inputs and outputs.**
   - kind: `lab`
#### Module 3 — C/Rust Safety Boundaries

**Reading:** **B15** Ch. 4 (Understanding Ownership), Ch. 10 §10.3 (Validating References with Lifetimes), Ch. 20 §20.1 (Unsafe Rust). **R36** Meet Safe and Unsafe; Foreign Function Interface. **B2** Ch. 5 (Pointers and Arrays) as the C side of the comparison.


### Module outcomes

By the end of this module, the learner can:

- Explain **C memory hazards and Rust ownership** in the context of the course.
- Apply **Unsafe boundaries and FFI concepts** in a problem, implementation, experiment, or design decision.

1. **C memory hazards and Rust ownership**
   - kind: `lesson`
2. **Unsafe boundaries and FFI concepts**
   - kind: `lesson`
3. **Checkpoint: safety guarantees**
   - kind: `test`

4. **Micro-lab: Compare one resource-management implementation in C and Rust.**
   - kind: `lab`
#### Module 4 — Signals & Robust Services

**Reading:** **B5** Ch. 20 (Signals: Fundamental Concepts), Ch. 21 (Signals: Signal Handlers), Ch. 22 (Signals: Advanced Features), Ch. 25 (Process Termination), Ch. 37 (Daemons). **B15** Ch. 9 (Error Handling).


### Module outcomes

By the end of this module, the learner can:

- Explain **Signals and controlled shutdown** in the context of the course.
- Apply **Error handling in systems programs** in a problem, implementation, experiment, or design decision.

1. **Signals and controlled shutdown**
   - kind: `lesson`
2. **Error handling in systems programs**
   - kind: `lesson`
3. **Checkpoint: service correctness**
   - kind: `test`

4. **Micro-lab: Add graceful signal handling and verify cleanup.**
   - kind: `lab`
#### Module 5 — Rust Unix Service Utility

**Reading:** **B5** Ch. 37 (Daemons), Ch. 44 (Pipes and FIFOs), Ch. 13–14 (File I/O Buffering; File Systems). **B15** Ch. 9 (Error Handling), Ch. 11 (Writing Automated Tests), Ch. 12 (An I/O Project: Building a Command Line Program). *Optional:* **R42** Command-line apps in Rust.


1. **Build and validate the Rust Unix Service Utility**
   - kind: `lab`

### Topics

- Unix process model
- memory allocation
- files and descriptors
- system calls
- ownership and resource lifetime
- unsafe versus safe boundaries
- process creation
- signals
- error handling
- FFI concepts

### Labs

- file-descriptor monitor
- process launcher
- allocator experiment
- C-to-Rust comparison
- resource cleanup tests

### Substantial course lab

**Rust Unix Service Utility**

A multi-module command-line or daemon-style utility that interacts directly with Linux facilities.

---

