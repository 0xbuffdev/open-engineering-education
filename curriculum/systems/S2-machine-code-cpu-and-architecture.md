# S2 — Machine Code, CPU & Computer Architecture

**Track:** Systems · **Prerequisite:** S1 · **Core** · **Time:** 6 weeks, 90 hours · **Project:** P2 disassembly/report
**Status:** `draft` · [status labels](../../spec/status-labels.md)

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../templates/progress.md)

## Purpose

Understand the machine that executes your code: gates, datapaths, instruction encoding, pipelining, hazards, branch prediction, superscalar execution, and the limits of instruction-count reasoning. This is where "the compiler did something weird" becomes explainable.

## Outcomes

You can:

- follow a load, call, branch, and return at the machine level;
- read x86-64 and one RISC ISA (MIPS/RISC-V) assembly well enough to map it to C;
- explain instruction encoding, registers, flags, and calling conventions;
- trace a single-cycle, multicycle, and pipelined datapath;
- explain data/control/structural hazards and forwarding;
- explain branch prediction, speculation, superscalar, out-of-order, register renaming, SIMD, and multithreading;
- use `objdump`, `readelf`, `nm`, and a debugger to inspect generated code;
- explain why instruction count is not the same as performance.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| B1 *But How Do It Know?* | “More Gate Combinations” through “Ta Daa!”; “A Few More Words on Arithmetic” | Build the CPU from gates, registers, ALU, control, instructions |
| B3 *Digital Design and Computer Architecture* | Ch. **1, 5, 6, 7** | Number systems, building blocks, architecture, microarchitecture |
| B3 | §§**7.2–7.5, 7.8** | Performance, single/multicycle/pipelined, advanced microarchitecture |
| B3 | §§**6.2–6.6** | Assembly, machine language, programming, addressing, compiling/loading |
| CS:APP | Ch. **3** | x86-64 assembly and processor view |
| [Agner Fog's optimization manuals](https://www.agner.org/optimize/) | Selected chapters | Real x86 microarchitecture detail |

**Edition note:** B3 section numbers below refer to the 2nd edition (MIPS). If you own the ARM or RISC-V edition, use the section titles; the concepts are the same.

## Modules

### 1. Digital building blocks

- number systems, signed/unsigned, two's complement;
- gates, combinational logic, sequential logic;
- registers, counters, shifters, memory arrays;
- ALU design, adders, comparators, zero logic;
- clocks, setup/hold, metastability (concept);
- HDL/testbench (optional, recommended if you have time).

### 2. Instruction set architecture

- registers, flags, program counter, stack pointer;
- instruction formats: R/I/J, opcode, funct, immediate;
- load/store, arithmetic/logical, branch/jump, call/return;
- addressing modes;
- x86-64 vs MIPS/RISC-V;
- encoding and decoding;
- assembly ↔ machine code ↔ C.

### 3. Calling conventions and ABI

- argument registers, return values, stack alignment;
- caller-saved vs callee-saved;
- frame pointer, red zone, varargs;
- stack unwinding and exceptions;
- position-independent code and relocations;
- how a C function call appears in assembly.

### 4. Microarchitecture

- single-cycle datapath and control;
- multicycle datapath;
- pipelining: IF/ID/EX/MEM/WB;
- hazards: structural, data, control;
- forwarding, stalls, branch delay slots;
- branch prediction (static/dynamic, BTB, history);
- exceptions and interrupts;
- superscalar, out-of-order, register renaming, reorder buffer;
- SIMD/vector units, multithreading, multicore;
- GPU architecture preview (S13).

### 5. Performance reasoning

- CPU time = instructions × CPI × cycle time;
- IPC, stalls, pipeline depth;
- instruction count vs cycles vs frequency;
- branch misprediction and cache misses;
- Amdahl's law and parallelism;
- benchmark pitfalls (warm-up, frequency scaling, noise).

## Labs

### Lab 1 — Trace a datapath

Take a small instruction sequence (load, add, branch, call, return). Draw the single-cycle and pipelined datapath states cycle by cycle. Identify one hazard and the forwarding/stall solution.

### Lab 2 — C to assembly

Compile five C functions at `-O0` and `-O2`. Map arguments, locals, loops, and calls to assembly. Explain one optimization the compiler made and one it could not.

### Lab 3 — Binary inspection

Use `objdump -d`, `readelf -h/-S/-s`, and `nm` on a small binary. Identify the entry point, `.text`, `.data`, `.bss`, one relocation, and one imported function. Disassemble one function and annotate it.

### Lab 4 — Branch and arithmetic benchmark

Write a branch-heavy and an arithmetic-heavy benchmark. Measure with `perf stat` where available. Compare predicted vs measured cycles and explain the gap. Include a branch-prediction-friendly and unpredictable variant.

### Lab 5 — Calling convention

Write a C function with six arguments and a local array. Inspect the assembly. Then write a small assembly function called from C and explain the ABI contract.

## Exercises

1. Convert ten numbers between binary, hex, and decimal; explain two's complement.
2. Encode five instructions by hand.
3. Decode five machine instructions into assembly.
4. Trace a function call's stack frame.
5. Explain five pipeline hazards with a fix for each.
6. Calculate CPU time for three instruction/CPI/frequency scenarios.
7. Explain why a shorter instruction sequence can be slower.
8. Compare x86-64 and RISC-V calling conventions.
9. Identify one place where the compiler vectorized and one where it did not.
10. Explain the difference between latency and throughput for one instruction.

## Project increment — P2 disassembly report

Add a `sysprobe disasm <binary>` mode or a standalone report that:

- identifies the architecture and entry point;
- lists sections and imported symbols;
- disassembles one function and maps it to source;
- reports one optimization or ABI detail;
- includes a benchmark with a prediction and explanation.

**Brief:** [P2 — sysprobe](../projects/project-ladder.md#p2--sysprobe)

## Exit check

- [ ] follow a load, call, branch, and return at machine level;
- [ ] explain a data hazard, control hazard, and forwarding;
- [ ] explain branch prediction and one reason it fails;
- [ ] read a disassembly and map it to C;
- [ ] explain why instruction count is not performance;
- [ ] calculate CPU time from instructions, CPI, and frequency.

## Common failure modes

- Reading assembly without knowing the calling convention.
- Assuming `-O2` output is "the truth" for all compilers.
- Benchmarking with too few iterations or without warm-up.
- Confusing latency with throughput.
- Ignoring branch prediction and cache effects when comparing instruction counts.
- Treating x86 as the only architecture.

## Evidence to commit

- `labs/systems/S2/` with datapath trace, C/assembly mapping, binary inspection, benchmark report
- P2 disassembly report
- `notes/systems/S2/summary.md`

## Optional depth

- B3 Ch. 2–4 (combinational/sequential logic, HDL).
- *Computer Architecture: A Quantitative Approach* (Hennessy & Patterson) Ch. 1–3.
- *Computer Organization and Design* (Patterson & Hennessy).
- Build a small CPU in a hardware description language or a simulator.
