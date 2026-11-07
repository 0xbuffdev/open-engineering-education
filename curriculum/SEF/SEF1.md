# SEF1 — Demystifying the Computer System

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** none
**Duration:** 5 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–15 focused hours/week (provisional; calibrate with learner evidence)

> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Build an evidence-based model of how a computer works, from physical
two-state signals through logic, storage, arithmetic, instruction execution,
and external output. The goal is to explain and investigate what changes
when a stored program runs, not merely to memorize hardware terminology.

The course begins without a programming prerequisite. Learners use a free
digital-logic simulator for essential gates, storage, and ALU demonstrations.
For the processor and instruction-set model, a transparent no-code emulator
or reproducible manual state table is sufficient. A paid service, physical
electronics kit, or privately hosted evaluator is not required.

The reference machine below is intentionally small and deterministic. It
helps teach fundamental boundaries; it is **not** a faithful simulation of
a modern CPU, firmware, operating system, electrical circuit, or device
driver. Differences must be explained rather than hidden.

The duration is an initial planning estimate, not a readiness claim.
Course completion depends on the outcome evidence below.

## Learning outcomes

- **SEF1-O1:** Explain two-state signals, bit patterns, byte values, encoding conventions, and the distinction between a memory address and its contents.
- **SEF1-O2:** Construct basic Boolean gates from NAND logic and predict their behavior from complete truth tables.
- **SEF1-O3:** Build and investigate clocked eight-bit storage, controlled bus transfers, and addressable memory.
- **SEF1-O4:** Construct an eight-bit arithmetic/logic model and explain wraparound arithmetic, Boolean operations, and zero detection.
- **SEF1-O5:** Encode and trace reference-machine instructions, including fetch/decode/execute, branching, memory effects, and explicit fault states.
- **SEF1-O6:** Explain how memory-mapped devices, persistent storage, firmware, software, operating systems, and file systems relate without treating the teaching machine as a real OS.
- **SEF1-O7:** Connect tested logic and storage components to a defensible end-to-end program-to-output trace, including assumptions, failures, and model limitations.

## Modules

### Module 1 — Bits and Representation

#### Outcomes

- SEF1-O1

#### Lessons

1. **From Bits to Computers** — Describe the course's machine-building approach and the distinction between a model and a physical computer.
2. **Two-State Signals** — Explain logical states and why physical voltage or switch conventions must be defined.
3. **Bits and Bytes** — Reason about eight-bit patterns and their 256 possible states.
4. **Number Representations** — Convert selected unsigned values between binary, decimal, and hexadecimal.
5. **Codes and Meaning** — Explain how one byte can represent different things under different encodings.
6. **Addresses and Values** — Distinguish a memory location from the byte stored at that location.

### Module 2 — Logic Gates

#### Outcomes

- SEF1-O2
- SEF1-O1

#### Lessons

1. **Boolean Logic** — Predict a gate's output from inputs using a truth table.
2. **NAND Construction** — Derive NOT and AND from NAND operations.
3. **Combining Gates** — Construct OR and XOR and explain intermediate signals.
4. **Circuit Description** — Represent a small circuit with a diagram or simulator.
5. **Circuit Verification** — Compare all Boolean input combinations with independently derived expectations.

### Module 3 — Registers and Memory

#### Outcomes

- SEF1-O3
- SEF1-O1

#### Lessons

1. **Clocked Storage** — Explain the difference between changing an input and committing stored state.
2. **Registers and Enables** — Predict an eight-bit register's value across active clock edges.
3. **Bus Selection** — Select one data source and explain contention when drivers conflict.
4. **Addressable Memory** — Trace controlled reads and writes to separate RAM locations.

### Module 4 — Arithmetic and ALU

#### Outcomes

- SEF1-O4
- SEF1-O2

#### Lessons

1. **Bitwise Operations** — Apply NOT, AND, OR, XOR, and shifting to fixed-width patterns.
2. **Binary Addition** — Explain carries and eight-bit modular arithmetic.
3. **ALU Selection** — Trace how an operation selector chooses arithmetic or logic results.
4. **Zero Detection** — Predict when an eight-bit result sets the zero flag.
5. **ALU Debugging** — Use expected-versus-observed values to locate a computation fault.

### Module 5 — Processor Execution

#### Outcomes

- SEF1-O5
- SEF1-O3
- SEF1-O4

#### Lessons

1. **Processor Datapath** — Identify the roles of the PC, instruction decoder, accumulator, ALU, flag, and memory.
2. **Clock and Control** — Explain how decoded control signals cause state transitions.
3. **Fetch and Decode** — Trace a two-byte instruction from program memory to its operand.
4. **Execute and Commit** — Explain changes to the PC, accumulator, flag, and memory after an instruction.

### Module 6 — Instructions and Programs

#### Outcomes

- SEF1-O5

#### Lessons

1. **Instruction Encoding** — Distinguish opcodes, operands, and even-aligned instruction addresses.
2. **Data Movement** — Trace immediate loads, RAM reads, and permitted memory writes.
3. **Arithmetic Instructions** — Predict accumulator and zero-flag changes after ADDI and ANDI.
4. **Branches and Flags** — Compare JMP, taken JZ, and untaken JZ execution.
5. **Program Tracing** — Hand-assemble and trace short programs instruction by instruction.
6. **Invalid Instructions** — Explain unsupported opcodes, illegal addresses, and misaligned targets.

### Module 7 — Devices and Boot

#### Outcomes

- SEF1-O6
- SEF1-O5

#### Lessons

1. **Memory-Mapped I/O** — Explain why some addresses interact with devices rather than RAM.
2. **Input and Output** — Trace keyboard-input and display-output latch behavior.
3. **Polling and Interrupts** — Distinguish two device-notification approaches without assuming they exist in the reference machine.
4. **Storage and Files** — Relate persistent bytes, storage devices, and file-system abstractions.
5. **Firmware and Boot** — Distinguish program-image initialization from firmware, bootloader, and OS startup.
6. **Hardware and Software** — Separate CPU/device responsibilities from programs, drivers, and operating systems.

### Module 8 — Computer System Integration

#### Outcomes

- SEF1-O5
- SEF1-O6
- SEF1-O7

#### Lessons

1. **System Connections** — Link gates, registers, ALU, memory, control, and device latches in an inspectable diagram.
2. **Program-to-Output Trace** — Follow initialized instruction bytes through state transitions to a device result.
3. **Fault Diagnosis** — Distinguish wrong bit order, arithmetic errors, invalid branches, and unavailable devices.
4. **Model Boundaries** — Defend what the simplified machine explains and what real systems additionally require.

## Completion requirements

Course completion requires demonstration of every listed learning outcome
against the public criteria of three **required summative assessments**:

| Required assessment | Outcome coverage | Primary evidence |
| --- | --- | --- |
| `SEF1-AS1` — Representation and Logic | SEF1-O1, SEF1-O2 | Encoding analysis, circuit exports, exhaustive truth tables |
| `SEF1-AS2` — Storage and ALU | SEF1-O3, SEF1-O4 | Clock/storage traces, RAM checks, ALU circuits and verification |
| `SEF1-AS3` — Program-to-Output Investigation | SEF1-O5, SEF1-O6, SEF1-O7 | Machine-state traces, device and boot explanation, reproducible fault investigation |

These are three evidence checkpoints across a coherent progression, **not**
a requirement to submit an independent quiz and lab in every module.
Module investigations, self-checks, worked examples, and exercises not
designated in the assessment briefs are formative and do not independently
gate completion.

A reviewer may use unfamiliar but equivalent cases; they must evaluate the
same outcomes against the public criteria. An answer key, hidden scoring
service, or paid course is not a prerequisite. A copied result without
explainable intermediate states is insufficient evidence.

### Shared investigation environment

Use a free offline or browser-based digital-logic simulator offering gates,
clocked storage, and observable signals, or a free equivalent environment.
For SEF1-AS1 and SEF1-AS2, include **inspectable simulator circuits** for
the required gates, register, addressable memory, and ALU; paper-only
assertions do not demonstrate these construction outcomes.

For SEF1-AS3, the processor may be represented by a transparent educational
emulator or an independently checkable manual instruction-state table; a
fully gate-implemented CPU is **not required**. Connect that state model
explicitly to the previously inspected circuits. No programming language,
paid tool/account, privileged system operation, or physical electronics
is required.

Record the actual tool and version when software is used, along with
circuit/fixture inputs and the minimum steps another learner needs to
reproduce the result. Use synthetic bytes and local simulated devices;
do not interact with uncontrolled hardware or real firmware.

### Shared eight-bit reference machine

All SEF1-AS3 evaluations use the following deterministic educational machine,
or an explicitly documented simulator mapping whose observable semantics are
equivalent.

- **State:** One unsigned eight-bit accumulator `A`, eight-bit program counter
  `PC`, and zero flag `Z`; all initially zero. The display-output latch
  starts **unset** until written. Any instruction that writes `A` sets
  `Z=1` exactly when the new eight-bit result is zero. Arithmetic wraps
  modulo 256. Each completed instruction commits one state transition.
- **Memory map:** `0x00`–`0x7F` contains read-only preloaded program bytes;
  `0x80`–`0xEF` contains RAM; `0xF0` is a write-only display latch;
  `0xF1` is a read-only keyboard-input latch. Other addresses are reserved.
  Program bytes come from a supplied persistent image through a simplified
  initialization action **before** execution begins.
- **Encoding:** Instructions are exactly two bytes: an opcode followed by
  an immediate value or address. Instruction fetches begin at an even
  program address; the normal `PC` increment is 2. Branch targets must be
  even-aligned **initialized instruction addresses** in program memory.
  Fetching outside the initialized program or using a forbidden address,
  invalid target, or unsupported opcode produces an explicit simulated fault.
- **Instructions:**
  - `10 imm` — `LDI`: load immediate into `A`, update `Z`.
  - `11 imm` — `ADDI`: add immediate modulo 256, update `Z`.
  - `12 imm` — `ANDI`: AND with immediate, update `Z`.
  - `20 addr` — `LOAD`: read RAM or the input latch into `A`, update `Z`.
  - `21 addr` — `STORE`: write `A` to RAM or display latch; do not update `Z`.
  - `30 addr` — `JMP`: set `PC` to a valid branch target.
  - `31 addr` — `JZ`: branch to a valid target when `Z=1`; otherwise advance.
  - `FF 00` — `HALT`: terminate execution without changing `A` or `Z`.
- **Mapped-device behavior:** `STORE F0` sets the display latch; `LOAD F1`
  reads an initialized keyboard latch. An absent required device produces
  a simulated device fault. Reading the write-only display address or
  writing the read-only input address is an invalid access.
- **Excluded hardware behavior:** No interrupts, pipelines, caches,
  instruction privilege, MMU, real firmware execution, multitasking,
  device timing, or real OS boot is implemented by this model.

A reviewer must be able to independently derive each executed instruction's
effects from these rules. If a substitute simulator is used, its mapping
must explain any internal architectural differences while preserving the
published evaluation behaviors.

### Required assessments

- **SEF1-AS1** (required representation and gate investigation)
  - Outcomes: SEF1-O1, SEF1-O2
  - Work: represent and interpret selected eight-bit patterns, then build
    and verify elementary gates derived from NAND.
    Convert `00000000`, `00101101`, `10000000`, and `11111111`
    to unsigned decimal and hexadecimal. Explain that `00101101` can
    mean decimal 45 or the ASCII character `-`, depending on
    interpretation. Distinguish address `0x80` from the byte stored
    there, and explain the chosen logical input convention. In a
    simulator, build NAND and NAND-derived NOT, AND, OR, and XOR gates.
    Compare each two-input gate with all four possible input pairs
    and NOT with both possible inputs; identify and correct a wiring
    or logic mistake.
  - Criteria: correct 0–255 unsigned mapping and stated encoding;
    independently justified NAND construction; correct exhaustive
    truth tables and intermediate signal behavior; credible explanation
    of a wrong observation and its correction. Inputs must be explicitly
    driven rather than assuming an unconnected pin is logical zero.
  - Evidence: conversion table, address/value explanation, circuit
    exports or inspectable simulator files, input/output truth tables,
    and a concise fault-and-correction note with tool instructions.

- **SEF1-AS2** (required storage and computation investigation)
  - Outcomes: SEF1-O3, SEF1-O4
  - Work: construct an eight-bit clocked register with load-enable and
    controlled source selection; demonstrate hold and load behavior.
    Model at least four independently addressable eight-bit RAM cells;
    show that a write changes only the selected cell and that an
    unselected read does not alter storage. Build an eight-bit ALU
    supporting modular addition plus AND, OR, and XOR with an observable
    zero-result signal. Check `250+10=4`, `255+1=0`, `0+0=0`,
    and mixed-bit Boolean cases, including a deliberate wrong
    enable, carry, or zero-detection case.
  - Criteria: correct clock-edge and enable semantics; no conflicting
    active bus drivers; memory address and value separation; independent
    expected values for arithmetic/logic and overflow; `Z=1` only for
    an all-zero selected result; wrong behavior located and corrected.
    The circuit and verification must be independently inspectable.
  - Evidence: register/RAM/ALU simulator artifacts, wiring or block
    diagram, clock-by-clock register and memory state tables, operation
    results versus independently calculated values, and a concise
    fault-and-correction trace with reproduction steps.

- **SEF1-AS3** (required program-to-output investigation)
  - Outcomes: SEF1-O5, SEF1-O6, SEF1-O7
  - Work: draw an inspectable block diagram relating program image,
    program ROM, `PC`, decoder, accumulator, ALU, zero flag, RAM,
    and mapped input/output to the previously built circuits. Hand-encode
    the program `10 00 31 08 10 2A 21 F0 FF 00` at addresses
    `0x00`–`0x09`, then trace it after reset. Repeat with the
    first immediate byte changed from `00` to `01`. Record every
    fetched opcode/operand, executed `PC`, next `PC`, `A`, `Z`,
    memory effects, and output-latch state. Explain why the first run
    skips output and the second writes `0x2A` (42). Independently
    demonstrate `20 F1 21 F0 FF 00` with a known initialized
    keyboard byte. Investigate an odd JZ target (`05`), unsupported
    opcode, and absent display mapping; identify the fault rather than
    inventing successful execution. Distinguish image initialization,
    firmware/bootloader, device controllers/drivers, operating-system
    and file-system responsibilities. Identify at least two material
    ways the teaching machine differs from a modern computer.
  - Criteria: correctly aligned two-byte decoding; taken and untaken
    branch traces follow `Z` semantics; `PC`, accumulator, flag,
    memory, and output changes match the reference ISA; illegal
    instructions, addresses, and unavailable devices are detected;
    gate/storage/ALU test evidence is explicitly linked to the
    instruction-state model; software/firmware/OS boundaries are
    explained without claiming that the tiny machine implements a
    real operating system. A reviewer must reproduce the normal
    output and at least one selected fault from a clean start.
  - Evidence: architecture and boot-boundary diagrams, program bytes,
    stepwise state tables for both branch cases and device input,
    fault observations, links to SEF1-AS1/AS2 circuit evidence,
    clean-start instructions, and a concise explanation of the
    model's limits and one meaningful technical decision.

### Optional formative practice

The following are study aids, **not additional summative submissions**:

- Convert unfamiliar bit patterns and compare signed/unsigned
  interpretations using an explicitly chosen convention.
- Predict a NAND/AND/XOR output before inspecting a simulator.
- Trace register behavior for changing bus inputs with enable disabled.
- Explain a bus-contention diagram and replace it with controlled selection.
- Calculate an ALU result and flag before running the circuit.
- Hand-trace `10 FF 11 01 21 F0 FF 00`; it should write byte zero.
- Diagnose a deliberately swapped opcode/operand or stale zero flag.
- Map a realistic operating-system boot narrative onto the much smaller
  initialization and execution steps implemented here.

### Completion decision and historical transition

An assessment is complete only when its stated **Work**, **Criteria**, and
**Evidence** requirements are demonstrated. The three assessments jointly
cover every `SEF1-O*` outcome; a single assessment may establish several
outcomes, and optional practice cannot substitute for required evidence.
Passing circuit tests alone does not establish understanding of
instruction execution or OS boundaries, and a copied emulator output
alone does not establish the claimed circuit-building outcomes.

**Migration from the previous SEF1 revision:** The former ten module
checkpoint/lab pairs and mandatory final lab were replaced by three
cohesive required evaluations. Foundational circuit construction,
memory/ALU behavior, ISA/branch tracing, mapped device interaction,
boot distinctions, and reproducible failure cases remain required where
they establish course outcomes. Old completion records remain associated
with their original course revision; this rewrite neither invalidates
them nor automatically claims equivalence. Any historical
re-evaluation needs explicit review of the substantive evidence.

This course remains `draft`: the structural checks and assessment
design do not establish learner testing, reproducibility by an
independent reviewer, or `verified` readiness. See
[Evidence Rules](../../spec/evidence-rules.md) and
[Status Labels](../../spec/status-labels.md).
