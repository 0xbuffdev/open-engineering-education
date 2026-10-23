# B1 — *But How Do It Know?*

**Author:** J. Clark Scott · **Edition:** 1st, 2009 · **Structure:** named sections, no numbered chapters · **Level:** absolute beginner

This book builds a small computer from a NAND gate upward. It is the gentlest bridge from "electricity and bits" to "CPU, RAM, instructions, OS, files, and boot." Read it in order; later sections assume the exact machine built earlier.

## How to navigate

The sections are not numbered. Use the exact bold/italic title in the running text and the book's own contents page. If your copy is a PDF with a different pagination, ignore page numbers.

```text
Part I — bits and gates
  Introduction → Just the Facts Ma'am → Speed → Language → Just a Little Bit
  → What the...? → Simple Variations → Diagrams → Remember When
  → What Can We Do With A Bit? → A Rose by Any Other Name → Eight Is Enough
  → Codes → Back to the Byte → The Magic Bus → More Gate Combinations

Part II — the machine
  First Half of the Computer → Numbers → Addresses → The Other Half of the Computer
  → More Gates → Messing with Bytes → The Left and Right Shifters → The NOTter
  → The ANDer → The ORer → The Exclusive ORer → The Adder
  → The Comparator and Zero → Logic → The Arithmetic and Logic Unit
  → More of the Processor → The Clock → Doing Something Useful → Step by Step
  → Everything's Under Control → Doing Something Useful, Revisited → What's Next?
  → The First Great Invention → Instructions → The Arithmetic or Logic Instruction
  → The Load and Store Instructions → The Data Instruction → The Second Great Invention
  → Another Way to Jump → The Third Great Invention → The Clear Flags Instruction
  → Ta Daa! → A Few More Words on Arithmetic

Part III — I/O and software
  The Outside World → The Keyboard → The Display Screen → Another Code
  → The Final Word on Codes → The Disk → Excuse Me Ma'am → That's All Folks
  → Hardware and Software → Programs → The Operating System → Languages
  → The File System → Errors → Computer Diseases? → Firmware → Boots
  → Digital vs. Analog → I Lied — Sort of → Full Disclosure → Philosophy
```

## Course map

| Course | Read | Why | Check |
| --- | --- | --- | --- |
| [F1](../foundations/F1-programming-i-python.md) | Introduction → The Magic Bus | Bits, bytes, ASCII/Unicode, gates, bus; no programming prerequisite | Draw a byte and explain why a bus is a bundle of wires |
| [F3](../foundations/F3-engineering-practice.md) | Hardware and Software → Boots | Programs, OS, languages, file system, errors, firmware, boot | Map each section to something you can observe on Linux |
| [S1](../systems/S1-computer-systems-foundations.md) | The Outside World → The Disk; Excuse Me Ma'am → Boots | I/O, keyboard, display, disk, OS, files, firmware, boot | Trace a keystroke from device to program |
| [S2](../systems/S2-machine-code-cpu-and-architecture.md) | More Gate Combinations → Ta Daa!; A Few More Words on Arithmetic | ALU, registers, clock, control, instruction set | Explain one instruction from fetch to write-back |

## Reading route

1. **First pass (F1):** Introduction through The Magic Bus. Do not memorize gate diagrams; be able to explain what a bit, byte, code, register, and bus are.
2. **Second pass (S2):** More Gate Combinations through Ta Daa!. Build the machine on paper: ALU, registers, clock, control unit, instruction decode.
3. **Third pass (S1/F3):** The Outside World through Boots. Connect the toy machine to a real Linux system.

## What to write in your notes

- One diagram of the 8-bit machine and its bus.
- One worked instruction: fetch, decode, execute, write-back.
- One table mapping book terms (RAM, MAR, instruction register, clock) to Linux/CPU terms.
- One paragraph on what the book simplifies compared with a modern out-of-order CPU.

## Limits

The book predates modern multicore, virtual memory, and security. It teaches the conceptual machine, not x86/ARM or kernel internals. Pair it with B3 (architecture) and B4/B5 (OS/Linux) for those.

## Acquisition

Buy or borrow a legal copy. Do not commit a scanned or downloaded PDF. The map is sufficient to follow the reading order once you have the book.
