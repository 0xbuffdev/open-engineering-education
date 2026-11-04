# SEF1 — Lesson authoring notes

> Optional instructional context preserved from the original source. These notes are not additional course metadata, assessment criteria, or required module briefs.

## Course orientation

- **Introduction:** Every later topic in the curriculum runs on a computer, and most difficulties in programming come from treating that computer as magic. This course builds a small computer from a single bit and leaves the learner able to explain what happens when a program runs.
- **History:** The first electronic stored-program computers ran in 1948 and 1949. The transistor, invented at Bell Labs in 1947, and the integrated circuit, developed in 1958 and 1959, made computers smaller and cheaper, and Intel's 4004 of 1971, the first commercial microprocessor, led to personal computers.
- **Usage:** The learner builds gates, memory, and an ALU in a hardware simulator, traces instructions by hand, and follows a program from storage through the processor to the screen.
- **Applications:** The model applies to every computer, from phones and laptops to servers and embedded devices, and it underlies later study of performance, operating systems, and security.
- **Strengths:** A small, complete model makes each part understandable, and building the parts shows why they have the shape they have.
- **Limitations:** The model is much simpler than a modern processor, which has caches, pipelines, and several cores. SYS1 adds those.
- **Key concepts:** bit; byte; code; logic gate; register; memory; bus; ALU; instruction; fetch, decode, execute; operating system; booting

## Module 1 — Inside the Machine

- **Introduction:** A computer looks complicated because it does an enormous number of very simple things very fast. This module shows that the whole machine rests on one idea: a physical object that can be in one of two states.
- **Overview:** It defines the bit, shows how bits are stored and moved, and groups eight of them into a byte, the unit used throughout the rest of the course.
- **History:** The word bit, short for binary digit, is credited to John Tukey in 1947 and was made famous by Claude Shannon's 1948 paper on information theory. Werner Buchholz coined byte in 1956, and the eight-bit byte became the standard unit with IBM's System/360 in the 1960s.
- **Key concepts:** two-state systems; bit; byte; the number of patterns n bits can form

## Module 2 — Codes, Numbers & Addresses

- **Introduction:** Bits become useful only when everyone agrees what a pattern means. This module explains the agreements that turn patterns into letters, numbers, and locations.
- **Overview:** It covers codes for text, binary numbers, and addresses that name a byte's place in memory, and it shows how one pattern can mean different things.
- **History:** ASCII was first published in 1963 as a seven-bit code for English text. Unicode began in the late 1980s to cover every writing system, and UTF-8, designed in 1992 by Ken Thompson and Rob Pike, became the dominant way to store it.
- **Key concepts:** code (encoding); binary and decimal; unsigned values; address; interpretation of the same bits

## Module 3 — Gates & Circuits

- **Introduction:** Hardware makes decisions by combining signals with logic gates. This module builds the gates and shows that one gate, NAND, is enough to build all the others.
- **Overview:** Learners study truth tables, combine gates into larger circuits, and describe circuits in a hardware description language that a simulator can test.
- **History:** George Boole published his algebra of logic in the 1840s and 1850s. In 1937 Claude Shannon showed that it describes switching circuits, and in 1913 Henry Sheffer had shown that a single operation can express all the others.
- **Key concepts:** truth table; AND, OR, NOT, NAND; composition; hardware description language; simulation

## Module 4 — Registers & Memory

- **Introduction:** A computer must remember. This module shows how gates can hold a bit, how eight held bits become a register, and how many registers become memory.
- **Overview:** It covers storing a bit, enabling a register to load or hold a value, moving bytes over a shared bus, and selecting one of many bytes by address.
- **History:** Early computers stored data in relay circuits, vacuum tubes, delay lines, and magnetic cores. Dynamic RAM, invented by Robert Dennard at IBM in 1966, made large and cheap memory practical.
- **Key concepts:** stored bit; register; enable signal; bus; RAM; address selection

### Additional lesson context

- **Build memory:** Registers can be built by combining memory bits with an enabler; a bus enables bytes to be copied between registers.

## Module 5 — How Hardware Computes

- **Introduction:** Arithmetic is logic applied to bits. This module builds the circuits that add, compare, and combine bytes, and assembles them into the arithmetic and logic unit.
- **Overview:** It covers shifting, bitwise operations, the adder, comparison and zero detection, and how a control input selects the operation the ALU performs.
- **Key concepts:** bitwise logic; shifting; half adder and full adder; carry; zero flag; operation selection

## Module 6 — Building the Processor

- **Introduction:** A processor is registers, an ALU, and control logic that step through actions in time. This module shows how a clock and control signals make those parts cooperate.
- **Overview:** It covers the clock, control signals, the fetch, decode, and execute cycle, and how one instruction is carried out as a sequence of small steps.
- **History:** John von Neumann described the stored-program idea, in which instructions and data share one memory, in 1945, and the Manchester Baby first ran a stored program in 1948.
- **Key concepts:** clock; control signal; instruction register; instruction address; fetch, decode, execute

## Module 7 — Instructions & Programs

- **Introduction:** A program is a list of instructions stored as bytes. This module shows what those bytes mean and how jumps let a program repeat and decide.
- **Overview:** It covers instruction formats, arithmetic and logic instructions, load and store, data instructions, jumps and flags, and reading short machine-language programs.
- **History:** The first programmers wrote numeric codes directly. Assembly languages replaced them with readable names in the late 1940s, and high-level languages followed in the 1950s.
- **Strengths:** Machine language gives complete control and leaves no ambiguity about what the hardware does.
- **Limitations:** It is tedious, error-prone, and specific to one processor family, which is why most people write in higher-level languages.
- **Key concepts:** instruction; opcode and operands; load and store; jump and flags; machine language; assembly

### Additional lesson context

- **A tiny program:** Stored instruction bytes let a machine choose which hardware operations to execute next.

## Module 8 — Hardware, Software & Booting

- **Introduction:** The earlier modules built a processor. This one explains how a complete computer gets input and output, stores data on disk, and starts itself and its software.
- **Overview:** It covers adapters and peripherals, hardware versus software, programs, operating systems, files, firmware, and the boot sequence.
- **History:** Early machines were operated directly by people. Operating systems appeared in the 1950s and 1960s to run programs automatically, and Unix, begun in 1969 at Bell Labs, shaped most modern systems.
- **Key concepts:** peripheral; adapter; hardware and software; operating system; file system; firmware; boot

### Additional lesson context

- **Tiny computer model:** Peripherals exchange bytes with the computer through adapters, connecting hardware to software, operating systems, files, firmware, and booting.

## Original topic inventory

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

## Original module-design rationale

This course does not need an additional lab-only module. Its hands-on work is distributed through Modules 2–7 as focused micro-labs, while Module 8 ends with the **Tiny Computer Model** course lab. That preserves the curriculum rule that the final module ends with the course lab without adding an otherwise redundant ninth module.
