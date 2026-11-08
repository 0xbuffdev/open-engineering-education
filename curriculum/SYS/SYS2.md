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


### Modules

#### Module 1 — Unix Processes & Resources



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

