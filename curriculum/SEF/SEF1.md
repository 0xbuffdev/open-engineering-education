# SEF1 — Demystifying the Computer System

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** none
**Duration:** 4 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

This course starts from a single bit and builds the machine piece by piece: bytes and codes, logic gates, memory, the processor, arithmetic, instructions, input/output, storage, software, operating systems, files, firmware, and booting. By the end, the learner can explain what the machine is doing when a program runs.

This is the first course in the Foundations program because programming should begin with a concrete model of the machine being programmed. The course uses an educational computer model rather than reproducing every detail of a modern CPU.

**None.**

No prior programming experience is required. Basic computer skills (typing, managing files, and browsing the web) are helpful.

## Learning outcomes

By the end of the course, the learner will be able to:

- Explain what bits and bytes are and how codes turn bit patterns into meaning.
- Explain how logic gates combine to create useful digital components.
- Describe how registers, buses, memory, and addresses allow information to be stored and moved.
- Explain how an ALU performs basic arithmetic and logic operations.
- Build elementary logic gates, memory, and an ALU in a hardware simulator.
- Identify the main parts of the processor and trace the fetch/decode/execute cycle.
- Explain how machine instructions become programs and how control flow changes execution.
- Explain how keyboards, displays, disks, and other peripherals communicate with the CPU.
- Distinguish hardware, software, programs, operating systems, file systems, firmware, and the boot process.
- Trace a simple end-to-end path from stored program to CPU execution and external output.

## Modules

### Module 1 — Inside the Machine

#### Outcomes

- Integrate and demonstrate the course capabilities through the module's final practical work.

#### Lessons

1. **Course introduction: Demystifying the Computer System** — `lesson` — what the subject is, where it came from, where it is used, and its strengths and limits
2. **Why computers seem complicated** — `lesson`
3. **Bits and two-state systems** — `lesson`
4. **Bits in hardware** — `lesson`
5. **From bits to bytes** — `lesson`
6. **Bits and bytes** — `test`
7. **Bits in a byte** — `lab`

### Module 2 — Codes, Numbers & Addresses

#### Outcomes

- Integrate and demonstrate the course capabilities through the module's final practical work.

#### Lessons

1. **Bit patterns and meaning** — `lesson`
2. **Numbers in bytes** — `lesson`
3. **Addresses and locations** — `lesson`
4. **Same bits, different meanings** — `lesson`
5. **Codes and addresses** — `test`
6. **Encode and decode** — `lab`

### Module 3 — Gates & Circuits

#### Outcomes

- Integrate and demonstrate the course capabilities through the module's final practical work.

#### Lessons

1. **NAND and logic gates** — `lesson`
2. **Combining gates** — `lesson`
3. **Describing circuits** — `lesson`
4. **Logic gates** — `test`
5. **Build logic gates** — `lab`

### Module 4 — Registers & Memory

#### Outcomes

- Integrate and demonstrate the course capabilities through the module's final practical work.

#### Lessons

1. **Registers and enablers** — `lesson`
2. **Buses and RAM** — `lesson`
3. **Registers and memory** — `test`
4. **Build memory** — `lab` — predict register contents after a sequence of bus transfers on paper, then build the corresponding chip in a simulator

### Module 5 — How Hardware Computes

#### Outcomes

- Integrate and demonstrate the course capabilities through the module's final practical work.

#### Lessons

1. **Shifts and bitwise logic** — `lesson`
2. **NOT, AND, OR, XOR** — `lesson`
3. **The adder** — `lesson`
4. **Comparison and the ALU** — `lesson`
5. **ALU reasoning** — `test`
6. **Build the ALU** — `lab` — trace ALU operations on paper, including the zero result, then implement the ALU in a simulator

### Module 6 — Building the Processor

#### Outcomes

- Integrate and demonstrate the course capabilities through the module's final practical work.

#### Lessons

1. **Inside the processor** — `lesson`
2. **The clock and execution cycle** — `lesson`
3. **Control signals** — `lesson`
4. **Fetch, decode, execute** — `lesson`
5. **Processor execution** — `test`
6. **Processor steps** — `lab`

### Module 7 — Instructions & Programs

#### Outcomes

- Integrate and demonstrate the course capabilities through the module's final practical work.

#### Lessons

1. **Instruction registers** — `lesson`
2. **Instruction types** — `lesson`
3. **Jumps and control flow** — `lesson`
4. **Machine language** — `lesson`
5. **Instructions** — `test`
6. **A tiny program** — `lab`

### Module 8 — Hardware, Software & Booting

#### Outcomes

- Integrate and demonstrate the course capabilities through the module's final practical work.

#### Lessons

1. **I/O and device adapters** — `lesson`
2. **Peripherals** — `lesson`
3. **Hardware and software** — `lesson`
4. **Operating systems and files** — `lesson`
5. **Firmware and booting** — `lesson`
6. **Tiny computer model** — `lab`

## Completion requirements

- Complete the required exercises and checkpoints described in the [public course requirements](requirements/SEF1.md).
- Complete the final integrated `lab` in the last module and meet its stated observable exit criteria.
- Retain reproducible artifacts, verification results, design explanations, and a meaningful technical retrospective in accordance with [OEE Evidence Rules](../../spec/evidence-rules.md).
