# S5 — Virtual Memory

**Track:** Systems · **Prerequisite:** S3 · **Core** · **Time:** 5 weeks, 75 hours · **Project:** P2 mmap/page-fault lab

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../progress.md)

## Purpose

Virtual memory is the abstraction that gives every process a private address space, enables isolation, demand paging, memory-mapped files, copy-on-write, and much of the performance behaviour you measured in S3/S4. This course makes the page table, TLB, and page fault concrete.

## Outcomes

You can:

- explain virtual-to-physical translation with a multi-level page table;
- distinguish a page-table walk, TLB miss, and page fault;
- calculate page-table size and the cost of a context switch;
- use `mmap`, `munmap`, `mprotect`, `madvise`, and `fork` copy-on-write;
- explain demand paging, swapping, and the OOM killer;
- use huge pages and explain their trade-offs;
- observe page faults and memory usage with `/proc` and `perf`;
- explain isolation and permission implications.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| B3 | §**8.4** | Virtual memory, address translation, page table, TLB, protection |
| B4 *OSTEP* | Ch. **13–24** | Address spaces through complete VM systems |
| B5 *TLPI* | §§**6.3–6.4**, Ch. **49–50** | Process memory layout, VM management, memory mappings, VM operations |
| B6 | Ch. **4** | Virtual memory implementation and TLB optimization |
| CS:APP | Ch. **9** | Virtual memory, address translation, memory mapping, dynamic allocation |
| [Linux `mm` documentation](https://docs.kernel.org/admin-guide/mm/index.html) | Selected pages | Current Linux behaviour |

## Modules

### 1. Address translation

- virtual vs physical addresses;
- page, frame, offset;
- single-level and multi-level page tables;
- page-table entries: present, read/write, user/supervisor, accessed, dirty, NX;
- TLB and TLB shootdown;
- page-table walks and caching;
- inverted page tables (concept);
- 32-bit vs 64-bit address spaces.

### 2. Processes and isolation

- address space per process;
- `fork` and copy-on-write;
- `exec` and address-space replacement;
- `mmap` private/shared, anonymous/file-backed;
- `mprotect` and guard pages;
- stack growth;
- ASLR;
- `/proc/<pid>/maps`, `smaps`, `statm`, `status`.

### 3. Paging and memory pressure

- demand paging;
- page fault types: minor, major, invalid;
- swap;
- page reclaim, LRU approximations;
- OOM killer;
- overcommit;
- `madvise` (`MADV_DONTNEED`, `MADV_HUGEPAGE`, `MADV_SEQUENTIAL`);
- huge pages and THP;
- memory cgroups (preview of S14).

### 4. Allocation

- `brk`/`sbrk` vs `mmap`;
- `malloc` arenas, bins, and fragmentation;
- `mmap`-backed large allocations;
- memory leaks vs address-space leaks;
- RSS vs VSZ vs PSS;
- `valgrind massif` and `heaptrack`.

### 5. Performance and security

- TLB reach and huge pages;
- page-fault cost;
- NUMA first-touch (preview of S8);
- W^X, NX, and memory protection;
- speculative execution side channels (concept);
- kernel/user isolation.

## Labs

### Lab 1 — Address translation simulator

Implement a multi-level page-table simulator with configurable levels, page size, and TLB size. Feed virtual addresses, report VPN/offset, TLB hit/miss, page-table walk, and frame. Test with hand-computed cases.

### Lab 2 — mmap and COW

Write a C program that:

- maps a file read-only and reads it;
- maps a file shared and modifies it;
- forks and observes copy-on-write;
- uses `mprotect` to make a page read-only and triggers a fault;
- prints `/proc/self/maps` before/after.

### Lab 3 — Page faults

Trigger minor and major faults (or as close as your environment allows). Measure with `perf stat -e page-faults` and `/usr/bin/time -v`. Explain the difference between RSS, VSZ, and page faults.

### Lab 4 — Huge pages

Run a memory-bound workload with and without transparent huge pages (if available). Measure TLB misses and runtime. Explain the trade-off and why huge pages can increase memory waste.

### Lab 5 — OOM and overcommit

In a disposable VM/container with a memory limit, allocate beyond the limit and observe the OOM behaviour. Record what was killed, why, and how to prevent it. Do not do this on your host.

## Exercises

1. Calculate the number of page-table entries for a 48-bit address space with 4 KiB pages.
2. Trace a two-level page-table walk.
3. Explain the difference between a TLB miss and a page fault.
4. Explain copy-on-write with a timeline.
5. Compare private and shared mappings.
6. Explain RSS vs VSZ vs PSS.
7. Calculate the memory overhead of a page table.
8. Explain why `malloc` may use `mmap` for large allocations.
9. Explain one security benefit and one performance cost of ASLR.
10. Explain why huge pages can reduce TLB misses but increase fragmentation.

## Project increment — P2 mmap/page-fault lab

Add `sysprobe vm`:

- print memory maps and RSS/VSZ/PSS;
- map a file and show the mapping;
- count page faults for a small workload;
- compare anonymous vs file-backed memory;
- include a report with measurements.

**Brief:** [P2 — sysprobe](../projects/project-ladder.md#p2--sysprobe)

## Exit check

- [ ] explain a page-table walk, TLB miss, and page fault separately;
- [ ] demonstrate `mmap` and copy-on-write;
- [ ] calculate page-table size and translation fields;
- [ ] measure page faults and explain the result;
- [ ] explain isolation and one performance implication;
- [ ] state when huge pages help and when they hurt.

## Common failure modes

- Confusing virtual address with physical address.
- Thinking a page fault always means an error.
- Forgetting that `fork` is copy-on-write, not eager copy.
- Measuring VSZ and calling it memory usage.
- Assuming huge pages are always faster.
- Running OOM tests on the host instead of a disposable VM/container.

## Evidence to commit

- `labs/systems/S5/` with simulator, mmap/COW lab, page-fault measurements, huge-page report
- P2 `sysprobe vm`
- `notes/systems/S5/summary.md`

## Optional depth

- B4 Ch. 21–23 in detail.
- CS:APP Ch. 9 malloc lab.
- *Understanding the Linux Kernel* memory chapters.
- `perf mem` and `perf c2c` for memory access analysis.
