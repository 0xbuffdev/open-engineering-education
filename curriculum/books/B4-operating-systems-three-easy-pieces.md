# B4 — *Operating Systems: Three Easy Pieces*

**Authors:** Remzi H. Arpaci-Dusseau & Andrea C. Arpaci-Dusseau · **Version:** 1.10, November 2023 · **Level:** beginner to intermediate · **Access:** [free online](https://pages.cs.wisc.edu/~remzi/OSTEP/)

This is the primary operating-systems narrative for S1, S5, S6, S11, and S12. It is free, chapter-based, and full of simulators and homework. Read the assigned chapters before the corresponding lab; do the simulation homework where offered.

## Structure (v1.10)

The chapter numbers below are the numbered chapter form on the OSTEP site. Some older printings and PDFs number the dialogues differently. Use titles as the fallback.

| Part | Chapters | Theme |
| --- | --- | --- |
| Introduction | 1–2 | Dialogue, introduction |
| Virtualization: CPU | 3–11 | Processes, API, direct execution, scheduling |
| Virtualization: Memory | 12–24 | Address spaces, paging, TLBs, swapping, complete VM |
| Concurrency | 25–34 | Threads, locks, condition variables, semaphores, bugs, events |
| Persistence | 35–46 | I/O, disks, RAID, files, FFS, journaling, LFS, SSD, integrity |
| Distribution | 47–51 | Distributed systems, NFS, AFS |
| Security | 52–56 | Dialogue, intro, authentication, access control, cryptography |
| Appendices | A1–A8 | Virtual machines, monitors, labs |

**Numbering caution:** the site's table places “57 Distributed” in the security column, but the free chapter list treats distribution as 47–51 and security as 52–56. The curriculum uses the titles, not 57.

## Exact course assignments

| Course | Chapters | Why | Check |
| --- | --- | --- | --- |
| [S1](../systems/S1-computer-systems-foundations.md) | **2, 4–6** | OS introduction, processes, process API, limited direct execution | Trace `fork`/`exec`/`wait` |
| [S5](../systems/S5-virtual-memory.md) | **12–24** | Address spaces, segmentation, paging, TLB, swapping | Walk a page table and a TLB miss |
| [S6](../systems/S6-concurrency-atomics-and-memory-models.md) | **25–34** | Threads, locks, condition variables, semaphores, bugs, events | Implement a bounded queue and explain a race |
| [S10](../systems/S10-linux-systems-programming-and-networking.md) | **33** | Event-based concurrency | Compare an event loop with threads |
| [S11](../systems/S11-distributed-systems.md) | **47–50** | Distributed systems, RPC, NFS, AFS | Explain a partial-failure guarantee |
| [S12](../systems/S12-data-systems-and-storage-engines.md) | **36–45** | I/O, disks, RAID, files, FFS, journaling, LFS, SSD, integrity | Explain a crash-consistency mechanism |
| [S14](../systems/S14-containers-virtualization-and-cloud-operations.md) | **2, 4–6**; Appendix **A1–A2** | Process/VM model and virtual machines | Explain container vs VM isolation |
| [S15](../systems/S15-reliability-incident-response-and-sre.md) | **36–45** (selected) | I/O and storage failure behaviour | Explain a durability/restore limitation |
| [D2](../security/D2-memory-corruption-and-binary-exploitation.md) | **13–24** | Address spaces, paging, protection | Explain how a memory bug violates a boundary |
| [S17](../systems/S17-compilers-and-language-runtimes.md) | **4–6, 13–14** (selected) | Process, address space, memory API | Connect runtime objects to OS memory |

## Reading route

1. **S1:** Ch. 2, 4, 5, 6. Run the `fork`/`exec` exercises on Linux.
2. **S5:** Ch. 12–24. Do the paging and TLB homework with the simulator.
3. **S6:** Ch. 25–34. Implement a lock and a condition-variable queue; break them deliberately.
4. **S12:** Ch. 36–45. Focus on journaling, LFS, SSDs, and integrity. Connect to your WAL.
5. **S11:** Ch. 47–50. Then read DDIA and the Raft paper; OSTEP is the warm-up, not the full distributed course.
6. **S14/S15:** revisit Ch. 2, 4–6, 36–45 with containers, backups, and failure drills.

## Homework and simulators

- `cpu-sched`, `vm-paging`, `vm-tlb`, `threads-*`, `file-*` simulators are on the OSTEP homework page.
- Run each simulator with `-c` to check your answer; do not just read the solution.
- For concurrency homework, keep a failing schedule and explain the interleaving.
- For file-system homework, record the crash point and the resulting state.

## Limits

- The distributed-systems part is introductory; use DDIA, MIT 6.5840, and the Raft paper for S11.
- Security chapters are conceptual; use D1–D5 for engineering practice.
- The book is Linux-adjacent but not a Linux syscall reference; use B5 for that.
- v1.10 has free security chapters by Peter Reiher. Verify the chapter numbering on the site if your PDF differs.

## Acquisition

Free online at <https://pages.cs.wisc.edu/~remzi/OSTEP/>. A paid PDF and print versions support the authors. Do not commit a downloaded copy; link to the official site from your notes.
