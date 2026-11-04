# SEF1 — Required practical work and evaluation

> This public brief preserves the imported draft exercises, final lab and exit criteria. It is part of the free OEE learning requirements, not a commercial resource mapping. Detailed lab environment, verification and evidence instructions still require course-conformance review.

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

- Build a small set of gates from NAND behavior.
- Model an 8-bit register and shared bus.
- Trace an ALU operation and its zero result.
- Hand-assemble a few instructions and execute them on paper.
- Model a simple I/O exchange between CPU and a keyboard/display adapter.
- Trace the boot path from persistent program storage into memory and execution.

## Course lab

### Tiny Computer Model

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
