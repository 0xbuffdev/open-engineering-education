> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

# SEF1 — Demystifying the Computer System

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** none
**Duration:** 4 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

## Overview

This course starts from a single bit and builds the machine piece by piece: bytes and codes, logic gates, memory, the processor, arithmetic, instructions, input/output, storage, software, operating systems, files, firmware, and booting. By the end, the learner can explain what the machine is doing when a program runs.

This is the first course in the Foundations program because programming should begin with a concrete model of the machine being programmed. The course uses an educational computer model rather than reproducing every detail of a modern CPU.

## Course brief

The course introduction is the first lesson of the first module. It combines the overview above with these fields.

- **Introduction:** Every later topic in the curriculum runs on a computer, and most difficulties in programming come from treating that computer as magic. This course builds a small computer from a single bit and leaves the learner able to explain what happens when a program runs.
- **History:** The first electronic stored-program computers ran in 1948 and 1949. The transistor, invented at Bell Labs in 1947, and the integrated circuit, developed in 1958 and 1959, made computers smaller and cheaper, and Intel's 4004 of 1971, the first commercial microprocessor, led to personal computers.
- **Usage:** The learner builds gates, memory, and an ALU in a hardware simulator, traces instructions by hand, and follows a program from storage through the processor to the screen.
- **Applications:** The model applies to every computer, from phones and laptops to servers and embedded devices, and it underlies later study of performance, operating systems, and security.
- **Strengths:** A small, complete model makes each part understandable, and building the parts shows why they have the shape they have.
- **Limitations:** The model is much simpler than a modern processor, which has caches, pipelines, and several cores. SYS1 adds those.
- **Key concepts:** bit; byte; code; logic gate; register; memory; bus; ALU; instruction; fetch, decode, execute; operating system; booting

## Prerequisites

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

#### Module brief

- **Introduction:** A computer looks complicated because it does an enormous number of very simple things very fast. This module shows that the whole machine rests on one idea: a physical object that can be in one of two states.
- **Overview:** It defines the bit, shows how bits are stored and moved, and groups eight of them into a byte, the unit used throughout the rest of the course.
- **History:** The word bit, short for binary digit, is credited to John Tukey in 1947 and was made famous by Claude Shannon's 1948 paper on information theory. Werner Buchholz coined byte in 1956, and the eight-bit byte became the standard unit with IBM's System/360 in the 1960s.
- **Key concepts:** two-state systems; bit; byte; the number of patterns n bits can form

#### Module outcomes

By the end of this module, the learner can:

- Explain why computers appear complex even though they perform a small set of simple operations very quickly.
- Explain bits and bytes as the physical foundation for computer state and information.

1. **Course introduction: Demystifying the Computer System** — what the subject is, where it came from, where it is used, and its strengths and limits
2. **Why computers seem complicated** — module introduction
3. **Bits and two-state systems**
4. **Bits in hardware**
5. **From bits to bytes**
6. **Bits and bytes**
   - kind: `test`
7. **Bits in a byte**
   - kind: `lab`

### Module 2 — Codes, Numbers & Addresses

#### Module brief

- **Introduction:** Bits become useful only when everyone agrees what a pattern means. This module explains the agreements that turn patterns into letters, numbers, and locations.
- **Overview:** It covers codes for text, binary numbers, and addresses that name a byte's place in memory, and it shows how one pattern can mean different things.
- **History:** ASCII was first published in 1963 as a seven-bit code for English text. Unicode began in the late 1980s to cover every writing system, and UTF-8, designed in 1992 by Ken Thompson and Rob Pike, became the dominant way to store it.
- **Key concepts:** code (encoding); binary and decimal; unsigned values; address; interpretation of the same bits

#### Module outcomes

By the end of this module, the learner can:

- Explain how bit patterns can represent different kinds of information.
- Reason about bytes, numbers, and addresses.

1. **Introduction: Codes, Numbers & Addresses** — what the topic is, where it is used, and its strengths and limits
2. **Bit patterns and meaning**
3. **Numbers in bytes**
4. **Addresses and locations**
5. **Same bits, different meanings**
6. **Codes and addresses**
   - kind: `test`
7. **Encode and decode**
   - kind: `lab`

### Module 3 — Gates & Circuits

#### Module brief

- **Introduction:** Hardware makes decisions by combining signals with logic gates. This module builds the gates and shows that one gate, NAND, is enough to build all the others.
- **Overview:** Learners study truth tables, combine gates into larger circuits, and describe circuits in a hardware description language that a simulator can test.
- **History:** George Boole published his algebra of logic in the 1840s and 1850s. In 1937 Claude Shannon showed that it describes switching circuits, and in 1913 Henry Sheffer had shown that a single operation can express all the others.
- **Key concepts:** truth table; AND, OR, NOT, NAND; composition; hardware description language; simulation

#### Module outcomes

By the end of this module, the learner can:

- Explain basic logic gates and truth-table behavior.
- Describe a circuit in a hardware description language and test it in a simulator.

1. **Introduction: Gates & Circuits** — what the topic is, where it is used, and its strengths and limits
2. **NAND and logic gates**
3. **Combining gates**
4. **Describing circuits**
5. **Logic gates**
   - kind: `test`
6. **Build logic gates**
   - kind: `lab`

### Module 4 — Registers & Memory

#### Module brief

- **Introduction:** A computer must remember. This module shows how gates can hold a bit, how eight held bits become a register, and how many registers become memory.
- **Overview:** It covers storing a bit, enabling a register to load or hold a value, moving bytes over a shared bus, and selecting one of many bytes by address.
- **History:** Early computers stored data in relay circuits, vacuum tubes, delay lines, and magnetic cores. Dynamic RAM, invented by Robert Dennard at IBM in 1966, made large and cheap memory practical.
- **Key concepts:** stored bit; register; enable signal; bus; RAM; address selection

#### Module outcomes

By the end of this module, the learner can:

- Explain how registers, enablers, buses, and RAM create a usable memory system.
- Predict the contents of registers after a sequence of bus transfers.

1. **Introduction: Registers & Memory** — what the topic is, where it is used, and its strengths and limits
2. **Registers and enablers**
3. **Buses and RAM**
4. **Registers and memory**
   - kind: `test`
5. **Build memory** — predict register contents after a sequence of bus transfers on paper, then build the corresponding chip in a simulator
   - kind: `lab`

Registers can be built by combining memory bits with an enabler; a bus enables bytes to be copied between registers.

### Module 5 — How Hardware Computes

#### Module brief

- **Introduction:** Arithmetic is logic applied to bits. This module builds the circuits that add, compare, and combine bytes, and assembles them into the arithmetic and logic unit.
- **Overview:** It covers shifting, bitwise operations, the adder, comparison and zero detection, and how a control input selects the operation the ALU performs.
- **Key concepts:** bitwise logic; shifting; half adder and full adder; carry; zero flag; operation selection

#### Module outcomes

By the end of this module, the learner can:

- Explain bitwise logic, shifting, arithmetic, comparison, and zero detection.
- Explain how simple circuits combine into an **Arithmetic and Logic Unit (ALU)**.
- Trace an ALU operation and its zero result.

1. **Introduction: How Hardware Computes** — what the topic is, where it is used, and its strengths and limits
2. **Shifts and bitwise logic**
3. **NOT, AND, OR, XOR**
4. **The adder**
5. **Comparison and the ALU**
6. **ALU reasoning**
   - kind: `test`
7. **Build the ALU** — trace ALU operations on paper, including the zero result, then implement the ALU in a simulator
   - kind: `lab`

### Module 6 — Building the Processor

#### Module brief

- **Introduction:** A processor is registers, an ALU, and control logic that step through actions in time. This module shows how a clock and control signals make those parts cooperate.
- **Overview:** It covers the clock, control signals, the fetch, decode, and execute cycle, and how one instruction is carried out as a sequence of small steps.
- **History:** John von Neumann described the stored-program idea, in which instructions and data share one memory, in 1945, and the Manchester Baby first ran a stored program in 1948.
- **Key concepts:** clock; control signal; instruction register; instruction address; fetch, decode, execute

#### Module outcomes

By the end of this module, the learner can:

- Explain how registers, the ALU, control logic, and a clock cooperate inside a processor.
- Trace step-by-step processor execution.

1. **Introduction: Building the Processor** — what the topic is, where it is used, and its strengths and limits
2. **Inside the processor**
3. **The clock and execution cycle**
4. **Control signals**
5. **Fetch, decode, execute**
6. **Processor execution**
   - kind: `test`
7. **Processor steps**
   - kind: `lab`

### Module 7 — Instructions & Programs

#### Module brief

- **Introduction:** A program is a list of instructions stored as bytes. This module shows what those bytes mean and how jumps let a program repeat and decide.
- **Overview:** It covers instruction formats, arithmetic and logic instructions, load and store, data instructions, jumps and flags, and reading short machine-language programs.
- **History:** The first programmers wrote numeric codes directly. Assembly languages replaced them with readable names in the late 1940s, and high-level languages followed in the 1950s.
- **Strengths:** Machine language gives complete control and leaves no ambiguity about what the hardware does.
- **Limitations:** It is tedious, error-prone, and specific to one processor family, which is why most people write in higher-level languages.
- **Key concepts:** instruction; opcode and operands; load and store; jump and flags; machine language; assembly

#### Module outcomes

By the end of this module, the learner can:

- Explain instruction registers, instruction addresses, data movement, arithmetic/logic instructions, and control flow.
- Trace instructions and the execution of simple programs.

1. **Introduction: Instructions & Programs** — what the topic is, where it is used, and its strengths and limits
2. **Instruction registers**
3. **Instruction types**
4. **Jumps and control flow**
5. **Machine language**
6. **Instructions**
   - kind: `test`
7. **A tiny program**
   - kind: `lab`

Stored instruction bytes let a machine choose which hardware operations to execute next.

### Module 8 — Hardware, Software & Booting

#### Module brief

- **Introduction:** The earlier modules built a processor. This one explains how a complete computer gets input and output, stores data on disk, and starts itself and its software.
- **Overview:** It covers adapters and peripherals, hardware versus software, programs, operating systems, files, firmware, and the boot sequence.
- **History:** Early machines were operated directly by people. Operating systems appeared in the 1950s and 1960s to run programs automatically, and Unix, begun in 1969 at Bell Labs, shaped most modern systems.
- **Key concepts:** peripheral; adapter; hardware and software; operating system; file system; firmware; boot

#### Module outcomes

By the end of this module, the learner can:

- Explain I/O, peripherals, storage, software, programs, operating systems, file systems, firmware, and booting.
- Trace a complete path from stored instructions through CPU execution to external I/O.

1. **Introduction: Hardware, Software & Booting** — what the topic is, where it is used, and its strengths and limits
2. **I/O and device adapters**
3. **Peripherals**
4. **Hardware and software**
5. **Operating systems and files**
6. **Firmware and booting**
7. **Tiny computer model**
   - kind: `lab`

Peripherals exchange bytes with the computer through adapters, connecting hardware to software, operating systems, files, firmware, and booting.

## Why there is no separate lab module

This course does not need an additional lab-only module. Its hands-on work is distributed through Modules 2–7 as focused micro-labs, while Module 8 ends with the **Tiny Computer Model** course lab. That preserves the curriculum rule that the final module ends with the course lab without adding an otherwise redundant ninth module.

## Topics

- Computers as fast sequences of simple operations
- Bits and bytes
- Binary codes
- Numbers
- Addresses
- NAND and logic gates
- Hardware description and simulation
- Registers and enablers
- Buses
- RAM
- ALU
- Shifting and bitwise logic
- Addition and comparison
- Zero flags
- Processor organization
- Clock and control
- Instruction register
- Instruction address register
- Instruction execution
- Load/store and arithmetic/logic instructions
- Jumps and flags
- I/O bus and device adapters
- Keyboard and display
- Disk storage
- Hardware and software
- Programs
- Operating systems
- Languages and compilers
- File systems
- Errors and bugs
- Firmware
- Booting
- Digital versus analog

## Small exercises

- Convert small bit patterns to decimal values and back.
- Complete truth tables for logic gates.
- Predict a register value after a sequence of bus operations.
- Determine which memory address a register selects.
- Trace an ALU operation step by step.
- Decode a small instruction byte.
- Trace the fetch/decode/execute cycle for a short program.
- Explain what changes when a program reads keyboard data or writes display data.
- Distinguish hardware, software, firmware, and operating-system responsibilities in concrete scenarios.

## Practical exercises

3. Build a small set of gates from NAND behavior.
4. Model an 8-bit register and shared bus.
5. Trace an ALU operation and its zero result.
6. Hand-assemble a few instructions and execute them on paper.
7. Model a simple I/O exchange between CPU and a keyboard/display adapter.
8. Trace the boot path from persistent program storage into memory and execution.

## Course lab

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

The artifact may be implemented in a digital-logic simulator, an educational emulator, or another transparent environment that lets the learner inspect the state of the machine; a transparent digital-logic simulator can be used to implement and inspect the model. The learner must document the data path, execute a short program, trace at least one instruction cycle, and explain how software reaches the hardware operations that produce the result.

## Exit check

Given a simple program running on the course computer model, the learner can explain, step by step, what happens from instruction fetch through processor operations, memory access, and external I/O.
