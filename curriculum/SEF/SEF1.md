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

   The artifact uses inspectable digital-logic circuits for gates, memory and ALU, plus a transparent educational CPU emulator or reproducible manual instruction-state model. Use the reference eight-bit machine specified in Completion requirements (or document a complete equivalent mapping), execute a short program including a branch and a device output, and trace each instruction's PC, A, Z, memory and output effects. Explain the educational model's limits without asserting that it reproduces modern hardware or a real operating system.

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

**Required module checkpoints and hands-on lab contracts:**

Each of the ten modules below has two worked assessment prompts with expected reasoning and one required practical lab. Equivalent unfamiliar questions may be used only when they assess the same outcomes. Learners must explain how observed circuit and machine states follow from the defined rules. An answer copied without a demonstrable trace or independent explanation is not sufficient.

**Shared educational machine model (Modules 6–10):**

Use this deliberately simplified machine to make instruction and I/O questions determinable. It is a teaching contract, not a claim about real CPUs or operating systems. An equivalent simulator is acceptable only if the learner documents precisely how its behavior maps to this reference.

- **State:** One unsigned eight-bit accumulator `A`, eight-bit program counter `PC`, and zero flag `Z`; initially all are zero. Any operation that writes `A` recomputes `Z` as 1 exactly when the result is zero. Eight-bit arithmetic wraps modulo 256. Clocked state commits one instruction at a time.
- **Memory map:** `0x00`–`0x7F` holds read-only program bytes preloaded from a persistent image; `0x80`–`0xEF` holds RAM; `0xF0` is a write-only display-output latch and `0xF1` a read-only keyboard-input latch. All other addresses are reserved. Preloading program bytes represents a simplified boot initialization, not an actual modern firmware/OS process.
- **Encoding:** Every instruction occupies exactly two bytes (opcode followed by immediate/address operand), placed at even program addresses. Normally `PC` increases by 2. Branch targets must be even-aligned within the initialized program region. Invalid instruction fetches, unsupported opcodes and forbidden addresses yield an explicit simulated fault.
- **Instruction set:** `0x10 imm` = `LDI` (load immediate into A), `0x11 imm` = `ADDI` (A plus immediate modulo 256), `0x12 imm` = `ANDI` (A bitwise AND immediate), `0x20 addr` = `LOAD` (read RAM/input into A), `0x21 addr` = `STORE` (write A to RAM/output), `0x30 addr` = `JMP` (unconditional branch), `0x31 addr` = `JZ` (branch when Z=1), and `0xFF 00` = `HALT`. LOAD/LDI/ADDI/ANDI update Z; STORE, branches and HALT do not update A or Z.
- **Mapped I/O:** A STORE to `0xF0` changes the simulated display output latch; LOAD from `0xF1` reads the simulated keyboard input. When a required mapped device is absent, the model reports a simulated device fault. Interrupts, privilege, caches, pipelining, actual OS boot and drivers are outside this model.
- **Worked byte image:** `10 01 | 11 FF | 21 F0 | FF 00` preloaded at program addresses 0 through 7 loads 1, adds 255 modulo 256 to produce 0, writes 0 to output, then halts. Trace `PC`, `A`, `Z`, and the display after every instruction.

**Shared laboratory environment and safety:**

Use a free offline or browser-based digital-logic simulator with gates, clocks, registers and probes, or a transparent educational equivalent. Record the tool name/version and all circuit inputs. For NAND gates, registers, RAM and ALU construction, paper-only explanations are insufficient: include inspectable simulator circuits, truth tables and clock traces. Later instruction-state exercises may use a no-code emulator or detailed manual state table together with that circuit evidence. **No programming experience** or paid tool, account, privileged machine access or physical electronics kit is required.

**Shared review and acceptance rules:**

- Both checkpoint questions per module require correct reasoning; reviewers may use different unfamiliar examples if the same module outcomes are demonstrably assessed.
- Every required lab needs an inspectable circuit, state table or program trace appropriate to its objective; include normal, boundary and deliberate failure cases with independently checked expectations.
- Retain circuit files or screenshots, actual simulator version, construction steps, observed versus expected output, one investigated failure and a technical retrospective. A copied result without explaining its state transitions does not establish completion.
- The final integrated model must demonstrate instruction fetch/decode/execute through CPU and output changes; passing isolated component tests alone is insufficient.

**Module 1 — Inside the Machine: checkpoint** — Required assessment details

- **Q1 (free):** How many distinct states can one bit represent and how many eight independent bits represent? Why is a bit pattern not automatically a number or letter?
  - Expected answer and scoring: One bit has two states, and eight independent bits have 2⁸=256 patterns. Meaning depends on an agreed encoding/interpretation; a circuit only stores or transmits physical states.
- **Q2 (free):** A switch is open in a teaching circuit and is modeled as logical 0. Is that necessarily the same voltage convention in every real circuit? Explain.
  - Expected answer and scoring: No. Logical 0 and 1 are abstractions mapped to electrical ranges by a particular technology and circuit. An open switch needs pull-up/pull-down or other defined electrical behavior; floating inputs cannot be assumed to mean 0. The simulator exercise uses explicitly defined stable inputs.

**Module 1 — Bits in a byte: required lab** — Required assessment details

- **Objective:** Represent eight bits physically or in a simulated register and account for all patterns without relying on prior programming.
- **Prerequisites:** Complete the module's concepts and be able to explain its checkpoint. Use previously constructed circuit/state artifacts only after validating them against their earlier specifications.
- **Environment:** Use the shared free simulator and hand-tracing conventions specified above. State the actual tool name/version, input fixtures and required construction steps. No programming language or paid resource is required.
- **Procedure:**
  1. Use a logic simulator to create eight independent named input switches and eight visible output indicators, initializing all switches to zero.
  2. Set switches to represent `00000000`, `00000001`, `10000000` and `11111111`; record the full pattern and which indicator changes.
  3. Toggle one input at a time and trace that individual bit without changing unrelated positions; explain how positions are numbered consistently.
  4. Show on paper why eight positions admit 256 patterns, then design a second representation that groups them into two four-bit nibbles.
  5. Demonstrate and explain the difference between an explicitly driven zero input and an unconnected/floating simulator pin if the simulator exposes that state; do not require risky real electronics.
- **Expected result:** Each switch has two defined logical states; all shown eight-bit patterns match indicators and the learner explains the 256 possible combinations.
- **Verification:** Independently compare simulator output for the specified patterns against a hand-drawn eight-column truth table and verify the mapping for each switch.
- **Evidence:** Circuit or simulator project, labeled bit positions, input/output table, and an explanation of why physical states require conventions.
- **Failure analysis:** Describe a reversed bit-order label, undefined floating input or a mismatched switch/indicator and its correction.
- **Acceptance:** The stated normal, boundary and fault outcomes match independently calculated expectations; required circuit artifacts and machine traces are inspectable and reproducible. An unexplained failure, missing artifact or unverified essential behavior prevents completion.

**Module 2 — Codes, Numbers & Addresses: checkpoint** — Required assessment details

- **Q1 (free):** Convert unsigned binary `00101101` to decimal. Could the same pattern mean a character? What determines its meaning?
  - Expected answer and scoring: `00101101` = 32+8+4+1 = 45. Under ASCII this byte denotes the character `-`, while treated as unsigned binary it denotes 45. A specified encoding decides the interpretation; the bits themselves have no inherent type.
- **Q2 (free):** What does address `0x80` mean in an eight-bit address space, and how is an address different from the value stored there?
  - Expected answer and scoring: `0x80` is the numeric location 128; eight-bit addresses range 0–255. The address identifies where to access a cell or mapped device, not the data in that cell. Location and contents can both be eight-bit patterns but play different roles.

**Module 2 — Encode and decode: required lab** — Required assessment details

- **Objective:** Decode small representations and use address/value distinctions without confusing storage location and content.
- **Prerequisites:** Complete the module's concepts and be able to explain its checkpoint. Use previously constructed circuit/state artifacts only after validating them against their earlier specifications.
- **Environment:** Use the shared free simulator and hand-tracing conventions specified above. State the actual tool name/version, input fixtures and required construction steps. No programming language or paid resource is required.
- **Procedure:**
  1. Write tables for 8-bit unsigned binary, decimal and two-digit hexadecimal values for 0, 1, 45, 128 and 255.
  2. Use an explicitly stated character encoding (ASCII) to show how `00101101` may represent '-' rather than decimal 45; document that other encodings have other meanings.
  3. Create a diagram of sixteen numbered memory locations and place distinct byte patterns in two locations; demonstrate reading one address without changing its contents.
  4. Try interpreting the same pattern under the two declared conventions and explain why the expected output differs.
  5. Include edge checks for zero, maximum byte value and an invalid value outside the range 0–255.
- **Expected result:** All conversions and label mappings agree with the declared unsigned/ASCII interpretations; addresses are consistently separated from stored values.
- **Verification:** Check conversion tables independently with positional powers of two and known ASCII mapping; inspect the memory diagram against chosen locations.
- **Evidence:** Conversion table, address/value diagram, edge cases and explanation of the encoding choice.
- **Failure analysis:** Explain a left/right bit-order mistake, conflating address and data, or treating signed interpretation as automatic.
- **Acceptance:** The stated normal, boundary and fault outcomes match independently calculated expectations; required circuit artifacts and machine traces are inspectable and reproducible. An unexplained failure, missing artifact or unverified essential behavior prevents completion.

**Module 3 — Gates & Circuits: checkpoint** — Required assessment details

- **Q1 (free):** Give the NAND truth-table output for input pairs (0,0), (0,1), (1,0), (1,1). How can NOT x be built using a NAND gate?
  - Expected answer and scoring: NAND outputs 1,1,1,0 in that order. Wiring both NAND inputs to x yields NOT x because NAND(x,x)=NOT(x). Both results must be supported by the truth table.
- **Q2 (free):** Using only NAND gates, construct AND(x,y) and state its output for x=y=1.
  - Expected answer and scoring: Let t=NAND(x,y); AND(x,y)=NAND(t,t). When x=y=1, t=0 and NAND(0,0)=1. A learner must show the intermediate connection and all four input cases.

**Module 3 — Build logic gates: required lab** — Required assessment details

- **Objective:** Construct NOT, AND, OR and XOR from basic gates or NAND alone and explain circuit behavior through exhaustive truth tables.
- **Prerequisites:** Complete the module's concepts and be able to explain its checkpoint. Use previously constructed circuit/state artifacts only after validating them against their earlier specifications.
- **Environment:** Use the shared free simulator and hand-tracing conventions specified above. State the actual tool name/version, input fixtures and required construction steps. No programming language or paid resource is required.
- **Procedure:**
  1. Create a NAND gate and cycle through all four Boolean input pairs; save the observed table.
  2. Build NOT using NAND with tied inputs and AND using a NAND followed by a NAND inverter.
  3. Construct OR using De Morgan's law and XOR from a documented NAND-only arrangement or from basic gates; draw each internal signal.
  4. Test all four input pairs for each two-input gate and both states for NOT; compare outcomes to a separately worked truth table.
  5. Introduce one deliberate wiring mistake and show how an observed wrong truth-table row identifies the problem.
- **Expected result:** NOT, AND, OR and XOR match their Boolean truth tables for every possible input and every circuit has an inspectable signal path.
- **Verification:** Exhaustively compare output vectors, including XOR(1,1)=0 and OR(0,0)=0; retain intermediate node probes.
- **Evidence:** Circuit export, wiring diagrams, truth tables, probes and defective/repaired implementation.
- **Failure analysis:** Identify swapped wiring, a mistaken NAND-versus-AND assumption or an unresolved gate input.
- **Acceptance:** The stated normal, boundary and fault outcomes match independently calculated expectations; required circuit artifacts and machine traces are inspectable and reproducible. An unexplained failure, missing artifact or unverified essential behavior prevents completion.

**Module 4 — Registers & Memory: checkpoint** — Required assessment details

- **Q1 (free):** An eight-bit register contains `00001111`. At the next rising clock edge its load-enable is 0 and the bus carries `11110000`. What value remains? What if load-enable is 1?
  - Expected answer and scoring: With enable 0 it retains `00001111`; with enable 1 it captures `11110000` at the active edge under the course's synchronous register model. Separate clock-edge behavior from changes in input between edges.
- **Q2 (free):** Two enabled output drivers attempt to drive the same bus lines with opposite values. Is the result guaranteed to be the bitwise OR? Explain.
  - Expected answer and scoring: No. Conflicting active drivers cause contention or an undefined state unless a specific arbitration/wired-logic mechanism is provided. The design must select one driver or use properly controlled tri-state/multiplexer logic.

**Module 4 — Build memory: required lab** — Required assessment details

- **Objective:** Construct a clocked eight-bit register and model safe bus transfer and a small RAM address selection.
- **Prerequisites:** Complete the module's concepts and be able to explain its checkpoint. Use previously constructed circuit/state artifacts only after validating them against their earlier specifications.
- **Environment:** Use the shared free simulator and hand-tracing conventions specified above. State the actual tool name/version, input fixtures and required construction steps. No programming language or paid resource is required.
- **Procedure:**
  1. Build an eight-bit register from the simulator's storage primitives or explicit clocked elements; add a load-enable, eight input switches and eight output probes.
  2. Demonstrate that stable data is captured on the selected clock edge when enabled and held when disabled.
  3. Add a 2-to-1 source multiplexer on the register input; transfer two distinct patterns while selecting exactly one source.
  4. Model a memory with at least four independently addressable eight-bit cells, including explicit read and write controls; demonstrate that changing the address selects a different cell.
  5. Test no-write behavior, two distinct addresses, one-bit changes and a deliberately incorrect enable or source selection.
- **Expected result:** Register captures and holds the specified values, memory writes affect only the selected cell, and bus-source selection never leaves conflicting drivers.
- **Verification:** Compare clock-by-clock recorded outputs with independently prepared state tables; assert untouched cells preserve their values.
- **Evidence:** Simulator file, clock-edge and address tables, memory snapshot, mux/control diagram and corrected defect.
- **Failure analysis:** Explain level-sensitive versus edge-triggered confusion, lost state on disabled clocks, unintended writes or bus contention.
- **Acceptance:** The stated normal, boundary and fault outcomes match independently calculated expectations; required circuit artifacts and machine traces are inspectable and reproducible. An unexplained failure, missing artifact or unverified essential behavior prevents completion.

**Module 5 — How Hardware Computes: checkpoint** — Required assessment details

- **Q1 (free):** An unsigned eight-bit ALU adds 250 and 10 with results wrapped modulo 256. What is the eight-bit result and is its zero flag set?
  - Expected answer and scoring: The mathematical sum 260 wraps to 4, or `00000100`; Z=0. The result is eight-bit modular arithmetic, not an unrestricted integer or an automatic saturating sum.
- **Q2 (free):** For eight-bit inputs 11110000 and 10101010, compute bitwise AND and XOR. What happens to the zero flag for a zero result?
  - Expected answer and scoring: AND = `10100000`; XOR = `01011010`. Z=1 exactly when the resulting eight-bit ALU output is zero. Explain that AND and XOR operate bit by bit.

**Module 5 — Build the ALU: required lab** — Required assessment details

- **Objective:** Build and evaluate an eight-bit ALU that supports addition and selected Boolean operations with an observable zero result.
- **Prerequisites:** Complete the module's concepts and be able to explain its checkpoint. Use previously constructed circuit/state artifacts only after validating them against their earlier specifications.
- **Environment:** Use the shared free simulator and hand-tracing conventions specified above. State the actual tool name/version, input fixtures and required construction steps. No programming language or paid resource is required.
- **Procedure:**
  1. Create an eight-bit adder with a declared carry policy; for the course model, wrap addition modulo 256.
  2. Add an operation selector for ADD, AND, OR and XOR; expose selected output bits and a zero-detector result.
  3. Test 250+10=4, 255+1=0, 0+0=0 and at least one each of AND, OR and XOR using independent hand calculations.
  4. Demonstrate a zero-flag control output that is 1 only when the selected eight-bit result is all zeros.
  5. Introduce and repair an error in carry propagation or zero detection and retain both traces.
- **Expected result:** The ALU matches modular addition and truth-table-derived bitwise results; the zero flag reflects the selected eight-bit result.
- **Verification:** Compare every fixed test input to independent bitwise arithmetic; include overflow, all-zero, maximum-byte and mixed-bit cases.
- **Evidence:** ALU simulator project, operation table, carry/zero traces, hand calculations and failure analysis.
- **Failure analysis:** Explain a dropped carry incorrectly reported as saturation, confused XOR/OR or a zero detector wired to only one bit.
- **Acceptance:** The stated normal, boundary and fault outcomes match independently calculated expectations; required circuit artifacts and machine traces are inspectable and reproducible. An unexplained failure, missing artifact or unverified essential behavior prevents completion.

**Module 6 — Building the Processor: checkpoint** — Required assessment details

- **Q1 (free):** Using the SEF1 reference machine, program memory starts `10 05 21 F0 FF 00` at PC 0. What are A, PC, Z and display output after the first two instruction steps?
  - Expected answer and scoring: After LDI 05: A=5, PC=2, Z=0, display unchanged. After STORE F0: A=5, PC=4, Z remains 0, display latch becomes 5. Distinguish instruction bytes from data addresses and note the 2-byte instruction stride.
- **Q2 (free):** If A is 255 and the CPU executes ADDI 01, what are A and Z? Which parts of the CPU coordinate instruction progress?
  - Expected answer and scoring: A becomes 0 modulo 256 and Z becomes 1. The PC selects instruction bytes, decoder/control determines operation and bus/read/write signals, ALU computes, clocked state elements commit new values; sequencing is a teaching abstraction.

**Module 6 — Processor steps: required lab** — Required assessment details

- **Objective:** Trace fetch/decode/execute and clocked processor state changes using one fixed architectural contract.
- **Prerequisites:** Complete the module's concepts and be able to explain its checkpoint. Use previously constructed circuit/state artifacts only after validating them against their earlier specifications.
- **Environment:** Use the shared free simulator and hand-tracing conventions specified above. State the actual tool name/version, input fixtures and required construction steps. No programming language or paid resource is required.
- **Procedure:**
  1. Draw the reference machine datapath showing program ROM, PC, instruction decoder, A, ALU, Z, data RAM and mapped display latch.
  2. Load the byte sequence `10 05 21 F0 FF 00` at program addresses 0–5 and trace, by hand or in an inspectable simulator, two instruction steps and the final halt.
  3. Add a trace table with the fetched opcode/operand, effective address (if any), PC before/after, A, Z, and display output.
  4. Repeat with `10 FF 11 01 FF 00` and show the modular arithmetic result and zero-flag update.
  5. Make one deliberately incorrect control signal or PC increment in a diagram/state table, detect the error through expected trace and correct it.
- **Expected result:** Each instruction fetches an opcode and operand from its current PC; after the first two steps A=5, PC=4, Z=0 and display=5; the second example yields A=0 and Z=1 before halt.
- **Verification:** Independently execute the specified reference-state transitions on paper and compare every trace row; verify read/write permissions in the memory map.
- **Evidence:** CPU datapath, program bytes, executed step table, simulator/hand trace and an explained control error.
- **Failure analysis:** Explain fetching only one byte, incorrectly changing Z during STORE or treating a data write as a program fetch.
- **Acceptance:** The stated normal, boundary and fault outcomes match independently calculated expectations; required circuit artifacts and machine traces are inspectable and reproducible. An unexplained failure, missing artifact or unverified essential behavior prevents completion.

**Module 7 — Instructions & Programs: checkpoint** — Required assessment details

- **Q1 (free):** At PC 0 the program bytes are `10 FF 11 01 21 F0 FF 00`. Trace A and Z immediately after ADDI, and explain the display value after STORE.
  - Expected answer and scoring: LDI FF gives A=255, Z=0. ADDI 01 wraps A to 0, Z=1. STORE F0 writes 0 to the display latch without changing Z; HALT stops. The PC advances by two unless a branch overrides it.
- **Q2 (free):** Why is `0x21 0xF0` an instruction rather than a literal number? What does `0xF0` signify in the reference model?
  - Expected answer and scoring: At an even program address 0x21 is the STORE opcode and the following 0xF0 is its address operand. 0xF0 maps to the write-only display latch; interpretation depends on the fetch/decode context, not the raw bytes.

**Module 7 — A tiny program: required lab** — Required assessment details

- **Objective:** Run and explain a minimal stored-program sequence that uses an instruction set and memory-mapped output.
- **Prerequisites:** Complete the module's concepts and be able to explain its checkpoint. Use previously constructed circuit/state artifacts only after validating them against their earlier specifications.
- **Environment:** Use the shared free simulator and hand-tracing conventions specified above. State the actual tool name/version, input fixtures and required construction steps. No programming language or paid resource is required.
- **Procedure:**
  1. Copy the reference instruction table and mark each instruction's opcode, operand, legal effect and PC update.
  2. Hand-assemble the four-instruction program `10 FF 11 01 21 F0 FF 00` at addresses 0–7 and label its instruction boundaries.
  3. Trace PC, opcode/operand, A, Z and display after every executed step; show the output byte 0 explicitly.
  4. Alter ADDI immediate to 02, repeat the trace and predict output 1 and Z=0.
  5. Introduce an unsupported opcode in a copy and explain why execution should halt with an explicit fault rather than silently performing an unrelated operation.
- **Expected result:** The original program prints byte 0, the altered version prints byte 1; both trace tables follow the declared instruction semantics and handle unsupported opcodes as faults.
- **Verification:** Compare manual traces with a simulator or tabular interpreter using the same exact byte and flag rules; show expected and observed PC progression.
- **Evidence:** Program image, hand-assembly table, execution traces, output snapshots and invalid-opcode observation.
- **Failure analysis:** Explain instruction-byte misalignment, treating the operand as an opcode or missing the ADDI zero-flag update.
- **Acceptance:** The stated normal, boundary and fault outcomes match independently calculated expectations; required circuit artifacts and machine traces are inspectable and reproducible. An unexplained failure, missing artifact or unverified essential behavior prevents completion.

**Module 8 — Instruction Encoding & Control: checkpoint** — Required assessment details

- **Q1 (free):** A program at bytes 0–7 is `10 00 31 06 21 F0 FF 00`. Starting with Z=0, trace executed PCs and whether output occurs. Then replace the first operand with 01 and repeat.
  - Expected answer and scoring: LDI 00 sets A=0 and Z=1, so JZ at PC 2 branches to PC 6 and HALT executes: PCs 0,2,6; no display write. LDI 01 sets Z=0, so JZ falls through to STORE at PC 4, then HALT at 6: PCs 0,2,4,6; output latch receives 1.
- **Q2 (free):** The two-byte JZ instruction at PC 2 contains operand 05. Is that a valid branch destination in this course machine, and why?
  - Expected answer and scoring: No. A branch target must be an even-aligned address of a two-byte instruction within the program region 0x00–0x7F; address 0x05 points into an operand byte. The model reports an invalid branch target.

**Module 8 — Hand-assemble a tiny program: required lab** — Required assessment details

- **Objective:** Encode, execute and debug a four-instruction conditional program using deterministic branch semantics.
- **Prerequisites:** Complete the module's concepts and be able to explain its checkpoint. Use previously constructed circuit/state artifacts only after validating them against their earlier specifications.
- **Environment:** Use the shared free simulator and hand-tracing conventions specified above. State the actual tool name/version, input fixtures and required construction steps. No programming language or paid resource is required.
- **Procedure:**
  1. Represent the four-instruction program as hexadecimal bytes and mark valid program addresses and instruction boundaries.
  2. Construct two runs by setting the LDI operand first to 00 and then to 01, keeping JZ 06, STORE F0 and HALT 00 unchanged.
  3. Trace branch taken and branch not taken using PC, A and Z after each step; verify that no output is written in the first run and output 1 is written in the second.
  4. Replace JZ destination with odd address 05 and verify that the documented model detects an invalid branch rather than misdecoding an operand as an instruction.
  5. Demonstrate a status-flag misinterpretation and document the correction using the two traces.
- **Expected result:** With LDI 00, PC sequence 0→2→6 and no output; with LDI 01, sequence 0→2→4→6 and display output 1; invalid branch alignment is rejected.
- **Verification:** Compare manually encoded bytes against explicit table-driven decoding and examine taken/not-taken traces and the fault case.
- **Evidence:** Four-instruction byte table, PC/A/Z traces, output latch states, invalid-target test and corrected reasoning.
- **Failure analysis:** Explain misunderstanding of byte addressing, branch target alignment or stale zero-flag state.
- **Acceptance:** The stated normal, boundary and fault outcomes match independently calculated expectations; required circuit artifacts and machine traces are inspectable and reproducible. An unexplained failure, missing artifact or unverified essential behavior prevents completion.

**Module 9 — I/O, Firmware & Boot: checkpoint** — Required assessment details

- **Q1 (free):** In the reference machine, what happens when STORE F0 executes? How is that different from an ordinary RAM write, and what should happen if the display latch is absent?
  - Expected answer and scoring: STORE F0 transfers A to the mapped display-output register instead of a normal RAM location; an unavailable mapped device is a declared simulated fault. This illustrates device mapping only and is not a model of real OS drivers.
- **Q2 (free):** Distinguish persistent program image, simplified firmware initialization, CPU instruction execution and the role of a real operating system.
  - Expected answer and scoring: A persistent image keeps program bytes across simulated resets. Initialization loads or maps those bytes into program ROM before PC starts; the CPU fetches and executes them. A full OS would manage processes/devices/resources, which the reference model deliberately omits. Device interaction need not prove OS presence.

**Module 9 — Trace boot and device output: required lab** — Required assessment details

- **Objective:** Explain initialization from persistent program image and the boundary between CPU state and a mapped device.
- **Prerequisites:** Complete the module's concepts and be able to explain its checkpoint. Use previously constructed circuit/state artifacts only after validating them against their earlier specifications.
- **Environment:** Use the shared free simulator and hand-tracing conventions specified above. State the actual tool name/version, input fixtures and required construction steps. No programming language or paid resource is required.
- **Procedure:**
  1. Draw a sequence diagram with persistent bytes, initialization/firmware step, program ROM, PC, A, data RAM and the output latch.
  2. Reset the reference machine and load `10 2A 21 F0 FF 00`; execute its steps and demonstrate output latch 0x2A (decimal 42).
  3. Repeat while the simulated display mapping is unavailable, and demonstrate the explicit fault rather than claiming output occurred.
  4. Set the keyboard latch 0xF1 to a known byte and trace `20 F1 21 F0 FF 00` to show a LOAD from input followed by STORE to output.
  5. Explain, without claiming implementation, where a real bootloader, OS driver, interrupt handler and device controller might fit relative to this simplified teaching path.
- **Expected result:** Normal program outputs 42; missing display mapping produces a declared fault; keyboard latch input is copied to display through A when mappings are present.
- **Verification:** Compare before/after PC/A/Z/latch state for each fixture with expected state transition tables; identify initialization separately from instruction execution.
- **Evidence:** Initialization and device diagrams, stored image bytes, two traces, absent-device failure and model-limitations explanation.
- **Failure analysis:** Explain confusion between I/O and RAM, treating simulated firmware as a real OS or assuming a missing device must silently succeed.
- **Acceptance:** The stated normal, boundary and fault outcomes match independently calculated expectations; required circuit artifacts and machine traces are inspectable and reproducible. An unexplained failure, missing artifact or unverified essential behavior prevents completion.

**Module 10 — Hardware, Software & Booting: checkpoint** — Required assessment details

- **Q1 (free):** A learner draws gates, an ALU and a processor but cannot show an instruction changing output. Does that satisfy the final integration requirement?
  - Expected answer and scoring: No. The final demonstration must trace an actual stored instruction through fetch/decode/state changes and the output latch and link those steps to gate/register/ALU components. Separate diagrams alone do not show integrated behavior.
- **Q2 (free):** Which claims can the simple eight-bit machine support about a modern computer, and which would be unjustified?
  - Expected answer and scoring: It can illustrate encoding, state, memory addressing, instruction sequencing, simple I/O mapping and control. It cannot by itself establish modern OS boot sequencing, interrupts, MMUs, caches, privilege modes, actual device timings or real hardware electrical safety. The learner must name the abstraction boundary.

**Module 10 — Tiny computer model: required lab** — Required assessment details

- **Objective:** Build and defend an inspectable end-to-end computer demonstration tying bits, gates, memory, ALU, processor and device output together.
- **Prerequisites:** Complete the module's concepts and be able to explain its checkpoint. Use previously constructed circuit/state artifacts only after validating them against their earlier specifications.
- **Environment:** Use the shared free simulator and hand-tracing conventions specified above. State the actual tool name/version, input fixtures and required construction steps. No programming language or paid resource is required.
- **Procedure:**
  1. Present an integrated architecture diagram with gate primitives, 8-bit register/ALU and zero flag, program storage, PC, decoder, RAM and mapped input/output latches; identify which pieces are simulated versus manually reasoned.
  2. Export inspectable simulator circuits for NAND-derived gates, one eight-bit register or equivalent clocked storage block, and the ALU from earlier labs; retain exhaustive or representative tests.
  3. Use the SEF1 reference ISA to initialize and execute a documented short program producing an output, including a conditional branch. Show opcode/operand decoding, PC/A/Z transitions and display effects.
  4. Execute the normal program, an unsupported-opcode or invalid-branch case, and an absent-device or illegal-address case in the chosen transparent emulator/state model.
  5. Explain the difference between the simplified initialization image and a real firmware/bootloader/OS path, and between electrical signal truth tables and software instruction semantics.
  6. Provide a clean-start construction recipe, test/trace tables and a reviewer-facing outcomes-to-evidence matrix. Demonstrate that the reviewer can reproduce the main output and one fault case without hidden software or purchased services.
  7. Defend one design trade-off (e.g. shared vs separate program/data memory, PC width or output mapping) and document a mistaken prediction, the evidence against it and its correction.
- **Expected result:** The combined artifact connects logic primitives to persistent instruction bytes, CPU state transitions and output. A short program produces its predicted output; invalid cases fail visibly rather than silently producing arbitrary behavior.
- **Verification:** Compare every executed instruction step against the documented ISA and circuit tests; reproduce one output and one intentional fault from the exact construction steps.
- **Evidence:** Circuit exports, machine specification, memory/program image, trace table, error/fault evidence, README or equivalent instructions, reviewer demonstration, technical defense and retrospective.
- **Failure analysis:** Explain a real integration failure such as wrong PC increment, incorrect zero flag, reversed register bit order or absent I/O mapping, and provide a repair with a regression trace.
- **Acceptance:** The stated normal, boundary and fault outcomes match independently calculated expectations; required circuit artifacts and machine traces are inspectable and reproducible. An unexplained failure, missing artifact or unverified essential behavior prevents completion.

**Exit demonstration:**

Given a simple program running on the course computer model, the learner can explain, step by step, what happens from instruction fetch through processor operations, memory access, and external I/O.
