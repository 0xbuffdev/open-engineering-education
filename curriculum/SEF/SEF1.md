# SEF1 — Demystifying the Computer System

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** none
**Duration:** 5 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

This course starts from a single bit and builds the machine piece by piece: bytes and codes, logic gates, memory, the processor, arithmetic, instructions, input/output, storage, software, operating systems, files, firmware, and booting. By the end, the learner can explain what the machine is doing when a program runs.

This is the first course in the Foundations program because programming should begin with a concrete model of the machine being programmed. The course uses an educational computer model rather than reproducing every detail of a modern CPU.

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
- Trace instruction encoding, processor control, device output and boot boundaries in a complete simple-computer model.

## Modules

### Module 1 — Inside the Machine

#### Outcomes

- Explain why computers appear complex even though they perform a small set of simple operations very quickly.
- Explain bits and bytes as the physical foundation for computer state and information.

#### Lessons

1. **Course introduction: Demystifying the Computer System** — `lesson`

   Every later topic in the curriculum runs on a computer, and most difficulties in programming come from treating that computer as magic. This course builds a small computer from a single bit and leaves the learner able to explain what happens when a program runs.
2. **Why computers seem complicated** — `lesson`
3. **Bits and two-state systems** — `lesson`
4. **Bits in hardware** — `lesson`
5. **From bits to bytes** — `lesson`
6. **Bits and bytes** — `test`
7. **Bits in a byte** — `lab`

### Module 2 — Codes, Numbers & Addresses

#### Outcomes

- Explain how bit patterns can represent different kinds of information.
- Reason about bytes, numbers, and addresses.

#### Lessons

1. **Bit patterns and meaning** — `lesson`
2. **Numbers in bytes** — `lesson`
3. **Addresses and locations** — `lesson`
4. **Same bits, different meanings** — `lesson`
5. **Codes and addresses** — `test`
6. **Encode and decode** — `lab`

### Module 3 — Gates & Circuits

#### Outcomes

- Explain basic logic gates and truth-table behavior.
- Describe a circuit in a hardware description language and test it in a simulator.

#### Lessons

1. **NAND and logic gates** — `lesson`
2. **Combining gates** — `lesson`
3. **Describing circuits** — `lesson`
4. **Logic gates** — `test`
5. **Build logic gates** — `lab`

### Module 4 — Registers & Memory

#### Outcomes

- Explain how registers, enablers, buses, and RAM create a usable memory system.
- Predict the contents of registers after a sequence of bus transfers.

#### Lessons

1. **Registers and enablers** — `lesson`
2. **Buses and RAM** — `lesson`
3. **Registers and memory** — `test`
4. **Build memory** — `lab`

### Module 5 — How Hardware Computes

#### Outcomes

- Explain bitwise logic, shifting, arithmetic, comparison, and zero detection.
- Explain how simple circuits combine into an **Arithmetic and Logic Unit (ALU)**.
- Trace an ALU operation and its zero result.

#### Lessons

1. **Shifts and bitwise logic** — `lesson`
2. **NOT, AND, OR, XOR** — `lesson`
3. **The adder** — `lesson`
4. **Comparison and the ALU** — `lesson`
5. **ALU reasoning** — `test`
6. **Build the ALU** — `lab`

### Module 6 — Building the Processor

#### Outcomes

- Explain how registers, the ALU, control logic, and a clock cooperate inside a processor.
- Trace step-by-step processor execution.

#### Lessons

1. **Inside the processor** — `lesson`
2. **The clock and execution cycle** — `lesson`
3. **Control signals** — `lesson`
4. **Fetch, decode, execute** — `lesson`
5. **Processor execution** — `test`
6. **Processor steps** — `lab`

### Module 7 — Instructions & Programs

#### Outcomes

- Explain instruction registers, instruction addresses, data movement, arithmetic/logic instructions, and control flow.
- Trace instructions and the execution of simple programs.

#### Lessons

1. **Instruction registers** — `lesson`
2. **Instruction types** — `lesson`
3. **Jumps and control flow** — `lesson`
4. **Machine language** — `lesson`
5. **Instructions** — `test`
6. **A tiny program** — `lab`

### Module 8 — Instruction Encoding & Control

#### Outcomes

- Encode and trace a tiny instruction stream.
- Diagnose an unexpected result using observable evidence.

#### Lessons

1. **Instruction fields and binary encoding** — `lesson`
2. **Register and memory operand addressing** — `lesson`
3. **Branch targets and status flags** — `lesson`
4. **Instruction decoding and control signals** — `lesson`
5. **Instruction Encoding & Control reasoning** — `test`
6. **Hand-assemble a tiny program** — `lab`

### Module 9 — I/O, Firmware & Boot

#### Outcomes

- Explain the processor/software/device boundary through observable state.
- Diagnose an unexpected result using observable evidence.

#### Lessons

1. **Memory-mapped I/O concepts** — `lesson`
2. **Interrupts versus polling** — `lesson`
3. **Firmware, bootloader and OS responsibility** — `lesson`
4. **Device adapters and error states** — `lesson`
5. **I/O, Firmware & Boot reasoning** — `test`
6. **Trace boot and device output** — `lab`

### Module 10 — Hardware, Software & Booting

#### Outcomes

- Explain I/O, peripherals, storage, software, programs, operating systems, file systems, firmware, and booting.
- Trace a complete path from stored instructions through CPU execution to external I/O.

#### Lessons

1. **I/O and device adapters** — `lesson`
2. **Peripherals** — `lesson`
3. **Hardware and software** — `lesson`
4. **Operating systems and files** — `lesson`
5. **Firmware and booting** — `lesson`
6. **Tiny computer model** — `lab`

   **Final integration lab — required work**

   **Tiny Computer Model**

   Build a small, inspectable computer model that demonstrates the complete chain:

   ```text
   bits
     ↓
   logic gates
     ↓
   registers + bus + RAM
     ↓
   ALU
     ↓
   control + clock
     ↓
   instructions
     ↓
   program execution
     ↓
   I/O
   ```

   The artifact may be implemented in a digital-logic simulator, an educational emulator, or another transparent environment that lets the learner inspect the state of the machine. The learner must document the data path, execute a short program, trace at least one instruction cycle, and explain how software reaches the hardware operations that produce the result.

## Completion requirements

- Complete the required course exercises, checkpoints and evaluated labs below.
- Complete the final integrated `lab` in the last module and meet its stated observable exit criteria.
- Retain reproducible artifacts, verification results, design explanations, and a meaningful technical retrospective in accordance with [OEE Evidence Rules](../../spec/evidence-rules.md).

Complete these required exercises:

**Conceptual practice:**

- Convert small bit patterns to decimal values and back.
- Complete truth tables for logic gates.
- Predict a register value after a sequence of bus operations.
- Determine which memory address a register selects.
- Trace an ALU operation step by step.
- Decode a small instruction byte.
- Trace the fetch/decode/execute cycle for a short program.
- Explain what changes when a program reads keyboard data or writes display data.
- Distinguish hardware, software, firmware, and operating-system responsibilities in concrete scenarios.

**Practical practice:**

- Build a small set of gates from NAND behavior.
- Model an 8-bit register and shared bus.
- Trace an ALU operation and its zero result.
- Hand-assemble a few instructions and execute them on paper.
- Model a simple I/O exchange between CPU and a keyboard/display adapter.
- Trace the boot path from persistent program storage into memory and execution.

**Additional required micro-lab steps:**

- **Build memory:** Predict register contents after a sequence of bus transfers on paper, then build the corresponding chip in a simulator.
- **Build the ALU:** Trace ALU operations on paper, including the zero result, then implement the ALU in a simulator.

**Additional required practical assessments:**

- **Module 8 — Hand-assemble a tiny program:**
  - Objective: Encode and trace a tiny instruction stream.
  - Environment: Document local tools, versions and input fixtures.
  - Procedure: Encode four instructions, trace program counter and registers, and demonstrate a conditional branch.
  - Verification: Trace and simulator state match step by step.
  - Evidence: Retain implementation, failure test, trace and a short engineering explanation.
  - Failure analysis: Explain the injected or encountered error and the verified repair.
- **Module 9 — Trace boot and device output:**
  - Objective: Explain the processor/software/device boundary through observable state.
  - Environment: Document local tools, versions and input fixtures.
  - Procedure: Trace a stored program through load, fetch, execution and device output, including a missing device.
  - Verification: The trace identifies responsible layers and explains failure behavior.
  - Evidence: Retain implementation, failure test, trace and a short engineering explanation.
  - Failure analysis: Explain the injected or encountered error and the verified repair.

**Final integration extension:**

- Demonstrate the added course outcomes in the final lab with clean-checkout reproduction, invalid-input tests and a technical retrospective.

**Exit demonstration:**

Given a simple program running on the course computer model, the learner can explain, step by step, what happens from instruction fetch through processor operations, memory access, and external I/O.
