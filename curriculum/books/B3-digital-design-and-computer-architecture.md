# B3 — *Digital Design and Computer Architecture*

**Authors:** David Money Harris & Sarah L. Harris · **Edition:** 2nd, 2012 (MIPS edition) · **Level:** intermediate

A rigorous bridge from digital logic to a pipelined MIPS processor and its memory system. The 2nd edition uses MIPS; the later RISC-V edition has different chapters. Use the MIPS edition unless your course explicitly says RISC-V, and do not mix section numbers between editions.

**Title note:** Some printings title Chapter 8 “Memory Systems”; the 2nd-edition table of contents also lists “Memory and I/O Systems” because §8.5–8.9 cover I/O. This map uses §8.1–8.4, which are the memory sections in both.

## Structure

| Chapter | Title | Use |
| --- | --- | --- |
| 1 | From Zero to One | Digital abstraction, number systems, gates, CMOS |
| 2 | Combinational Logic Design | Boolean algebra, timing, building blocks |
| 3 | Sequential Logic Design | Latches, flip-flops, FSMs, metastability |
| 4 | Hardware Description Languages | Verilog/VHDL, simulation, synthesis |
| 5 | Digital Building Blocks | Adders, ALU, memory arrays, PLAs/FPGAs |
| 6 | Architecture | MIPS assembly, machine code, addressing, compilation |
| 7 | Microarchitecture | Single-cycle, multicycle, pipelined, advanced |
| 8 | Memory Systems / Memory and I/O Systems | Performance, caches, virtual memory, I/O |
| A | Digital System Implementation | 74xx, PLDs, FPGAs, ASICs, transmission lines |
| B | MIPS Instructions | Reference |

## Exact sections used by the curriculum

| Section | Title |
| --- | --- |
| 5.5 | Memory Arrays (5.5.1–5.5.8: SRAM, DRAM, register files, ROM) |
| 6.2 | Assembly Language |
| 6.3 | Machine Language |
| 6.4 | Programming |
| 6.5 | Addressing Modes |
| 6.6 | Compiling, Assembling, and Loading |
| 7.2 | Performance Analysis |
| 7.3 | Single-Cycle Processor |
| 7.4 | Multicycle Processor |
| 7.5 | Pipelined Processor |
| 7.7 | Exceptions |
| 7.8.1 | Deep Pipelines |
| 7.8.2 | Branch Prediction |
| 7.8.3 | Superscalar |
| 7.8.4 | Out of Order |
| 7.8.5 | Register Renaming |
| 7.8.6 | SIMD |
| 7.8.7 | Multithreading |
| 7.8.8 | Multiprocessors |
| 8.1 | Introduction |
| 8.2 | Memory System Performance Analysis |
| 8.3 | Caches (8.3.1–8.3.5) |
| 8.4 | Virtual Memory (8.4.1–8.4.6) |
| 8.5 | I/O Introduction |
| 8.6 | Embedded I/O Systems |
| 8.7 | PC I/O Systems |

## Course map

| Course | Read | Why | Check |
| --- | --- | --- | --- |
| [S2](../systems/S2-machine-code-cpu-and-architecture.md) | Ch. **1, 5–7**; emphasize §§**6.2–6.6**, **7.2–7.8** | Gates, building blocks, ISA, pipelining, hazards | Trace one instruction through a pipeline |
| [S3](../systems/S3-memory-hierarchy-and-locality.md) | §**5.5**, §§**8.1–8.3** | SRAM/DRAM, memory performance, caches | Calculate AMAT for a small cache |
| [S4](../systems/S4-cpu-caches.md) | §§**8.2–8.3** | Cache organization and performance | Simulate a cache and explain misses |
| [S5](../systems/S5-virtual-memory.md) | §**8.4** | Address translation, page tables, TLB, protection | Walk a page table and a TLB miss |
| [S7](../systems/S7-cache-coherence-and-false-sharing.md) | §**7.8.8** | Multiprocessors and coherence context | Explain a coherence state transition |
| [S13](../systems/S13-ai-infrastructure-systems-lens.md) | §§**7.8.6–7.8.7**, §§**8.2–8.3** | SIMD, multithreading, memory performance | Connect GPU/SIMT to CPU SIMD concepts |
| [S17](../systems/S17-compilers-and-language-runtimes.md) | Ch. **6–7** (revisit) | ISA, calling convention, pipeline/ABI context | Generate/read assembly and explain a frame |

## Reading route

1. **S2:** Ch. 1 quickly if you already know gates; spend the time on Ch. 6–7. Build the single-cycle datapath on paper, then the pipelined one.
2. **S3–S5:** §5.5 and Ch. 8. Work the performance examples by hand; do not just read them.
3. **S7:** §7.8.8 after S4 and S6; connect multiprocessor coherence to real `perf` experiments.
4. **S13:** §7.8.6–7.8.7 as the CPU analogue of SIMT/warps; do not pretend CPU SIMD is a GPU.

## Labs that pair well

- Build a 1-bit ALU and a small register file in Logisim or Verilog.
- Extend the single-cycle MIPS processor with one instruction.
- Pipeline the processor and measure a hazard.
- Write a cache simulator from §8.3 and validate it against a trace.
- Implement a two-level page-table walk from §8.4.

## Edition warning

The 2nd edition is MIPS. The RISC-V edition (Harris & Harris, 2021) reorganizes chapters and changes the ISA. If you own RISC-V:

- use its architecture/microarchitecture chapters for S2/S17;
- use its memory chapter for S3–S5;
- record the edition and section mapping in your study workspace's `notes/systems/*/resources.md`;
- never cite MIPS section numbers for a RISC-V edition.

## Acquisition

Purchase or borrow a legal copy. Do not commit a PDF. The 2nd-edition ISBN is 978-0123944245.
