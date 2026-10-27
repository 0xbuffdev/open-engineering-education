# S1 — Computer Systems Foundations

**Track:** Systems · **Prerequisite:** F3, F5 · **Core** · **Time:** 6 weeks, 90 hours · **Project:** P2 sysprobe
**Status:** `draft` · [status labels](../../spec/status-labels.md)

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../templates/progress.md)

## Purpose

Connect the Python/C/Rust program on your screen to the operating system services underneath it. You will learn how source becomes a process, how that process owns memory and file descriptors, how syscalls cross the kernel boundary, and how the toolchain produces an executable.

## Outcomes

You can:

- explain the path from source file to running process;
- use `gcc`/`clang`, `ld`, `objdump`, `readelf`, `nm`, `ldd`, and `strace`;
- explain ELF sections, symbols, relocations, static vs shared linking, and the ABI;
- describe a process's virtual address space and the roles of text/data/heap/stack;
- use file descriptors, `open`/`read`/`write`/`close`, and `fork`/`exec`/`wait`;
- explain a syscall vs a library call and how errors are reported;
- identify owned resources and reason about leaks;
- write a C probe and a safe-Rust equivalent, then compare guarantees.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| B2 *The C Programming Language* | Ch. **4–6**, §§**7.5–7.8**, §§**8.1–8.7** | Functions, pointers, structs, file I/O, syscalls, allocator |
| B4 *Operating Systems: Three Easy Pieces* | Ch. **2, 4–6** | OS introduction, processes, process API, limited direct execution |
| B5 *The Linux Programming Interface* | Ch. **2–7, 24–27** | OS concepts, syscalls, file I/O, processes, memory, fork/exec/wait |
| B1 *But How Do It Know?* | “The Outside World” through “The Disk”; “Excuse Me Ma’am” through “Boots” | I/O, keyboard, display, disk, software, OS, files, firmware, boot |
| *Computer Systems: A Programmer's Perspective* (CS:APP) | Ch. **1–3, 7, 9** | Programmer's view, data representation, assembly, linking, virtual memory |

## Modules

### 1. From source to process

- preprocessing, compilation, assembly, linking, loading;
- translation units, headers, declarations vs definitions;
- object files, symbols, relocations;
- static vs shared libraries, `ldd`, `LD_LIBRARY_PATH`;
- position-independent code, PLT/GOT (concept);
- `main`, `argc`/`argv`, `envp`, `_start`, libc startup;
- exit status and `atexit`.

### 2. Program memory

- virtual address space layout;
- text, rodata, data, BSS, heap, stack, shared libraries;
- stack frames, return addresses, calling convention;
- heap allocator metadata and fragmentation;
- `sbrk`/`brk` vs `mmap`;
- alignment and padding;
- `/proc/<pid>/maps`, `/proc/<pid>/smaps`.

### 3. System calls and the kernel boundary

- user mode vs kernel mode;
- syscall numbers, arguments, return values, `errno`;
- libc wrappers vs raw syscalls;
- `strace` and `ltrace`;
- files: `open`, `read`, `write`, `lseek`, `close`, `fsync`;
- processes: `fork`, `execve`, `waitpid`, `exit`;
- signals: basic disposition and `SIGCHLD`;
- time: `clock_gettime`, monotonic vs wall clock.

### 4. Resource ownership

- file descriptor table, `dup`, `dup2`, inheritance across `fork`/`exec`;
- memory ownership and lifetime;
- child processes and zombies;
- locks, sockets, and other kernel objects;
- RAII in Rust, `Drop`, and explicit cleanup in C;
- leak detection and resource accounting.

### 5. Toolchain and binary inspection

- `file`, `size`, `nm`, `objdump -d`, `readelf -a`, `strings`;
- disassembly and symbol demangling;
- debug vs release builds, `-g`, `-O0` vs `-O2`;
- sanitizers and how they change layout;
- reproducible builds (intro).

## Labs

### Lab 1 — C syscall probes

Write C programs that:

- print PID, PPID, UID, GID, and current working directory;
- open a file, read it in chunks, handle partial reads, and close it;
- create a child with `fork`, run a command with `exec`, and wait for it;
- allocate with `malloc`, touch the pages, and print `/proc/self/maps`;
- trigger one syscall error and print `errno` + `strerror`.

### Lab 2 — ELF and linking

Build the same program as a static binary and a shared-linked binary. Inspect sections, symbols, and dependencies. Explain the size difference and one deployment trade-off.

### Lab 3 — Resource leak hunt

Write a program that leaks a file descriptor and a child process. Diagnose with `/proc`, `lsof`, `strace`, and `valgrind`. Fix it and add a regression test.

### Lab 4 — Rust rewrite

Rewrite the syscall probes in safe Rust. Compare:

- which operations are safe by construction;
- where `unsafe` or `libc` is still required;
- what the Rust version prevents and what it does not.

### Lab 5 — Boot and filesystem context

Trace the boot sequence on your Linux machine (firmware → bootloader → kernel → init/systemd → login). Map B1's “Firmware”/“Boots” sections to what you observe. Identify the root filesystem, mount points, and one system service.

## Exercises

1. Draw the address space of a running process and label five regions.
2. Explain the difference between a segmentation fault and a page fault.
3. Trace `fork` + `exec` + `wait` with a diagram.
4. Explain why `write` can write fewer bytes than requested.
5. Inspect a binary and identify its entry point and one imported symbol.
6. Explain static vs dynamic linking in one paragraph each.
7. Find a file descriptor leak with two different tools.
8. Explain what `errno` is and why checking it matters.
9. Compare C `malloc`/`free` with Rust ownership for one example.
10. Map one B1 chapter to a real Linux observation.

## Project increment — P2 sysprobe

Build the first complete `sysprobe`:

- `sysprobe info` — PID, UID, cwd, environment summary;
- `sysprobe fds` — open descriptors and targets;
- `sysprobe maps` — memory regions;
- `sysprobe trace <cmd>` — run a command and summarize syscalls (optional; use `strace`).

C and Rust versions, with tests and a README.

**Brief:** [P2 — sysprobe](../projects/project-ladder.md#p2--sysprobe)

## Exit check

- [ ] explain `main()` to OS services with a diagram;
- [ ] demonstrate a real C failure mode and the Rust rewrite that prevents it;
- [ ] inspect an ELF binary and explain its sections and dependencies;
- [ ] trace a program's syscalls and identify an error path;
- [ ] explain file descriptor ownership and inheritance;
- [ ] show `/proc` evidence for memory and descriptors.

## Common failure modes

- Memorizing syscall names without understanding the kernel boundary.
- Ignoring partial reads/writes and `EINTR`.
- Forgetting to close descriptors or reap children.
- Assuming `malloc` returns zeroed memory.
- Treating a pointer as an integer without alignment/provenance concerns.
- Using `strace` output without correlating it to source lines.

## Evidence to commit

- `labs/systems/S1/` with C probes, ELF report, leak hunt, Rust rewrite, boot trace
- P2 sysprobe v1
- `notes/systems/S1/summary.md`

## Optional depth

- CS:APP Ch. 7 (linking) and Ch. 9 (virtual memory) in full.
- *Linkers and Loaders* (Levine).
- `perf trace` and `bpftrace` for syscall observation.
- Read the kernel's `Documentation/` on `proc` and `sysfs`.
