# B5 — *The Linux Programming Interface*

**Author:** Michael Kerrisk · **Edition:** 1st, 2010 · **Level:** intermediate to advanced · **Pages:** ~1,500

The definitive reference for Linux/UNIX system programming. It is too large to read cover to cover. Use it as a guided reference: read the assigned chapter before a lab, then return when a syscall surprise appears. The book predates some modern Linux features, so verify flags and behaviour with `man` pages for your kernel.

## Structure

| Part | Chapters | Theme |
| --- | --- | --- |
| Fundamentals | 1–12 | Concepts, file I/O, processes, memory, users, time, limits, `/proc` |
| Files and directories | 13–19 | Buffering, filesystems, attributes, ACLs, directories, inotify |
| Signals and processes | 20–28 | Signals, timers, fork/exec, wait, program execution |
| Threads | 29–33 | Threads, synchronization, thread safety, cancellation |
| Processes and scheduling | 34–37 | Groups/sessions, priorities, resources, daemons |
| Security and capabilities | 38–40 | Privileged programs, capabilities, login accounting |
| Shared libraries | 41–42 | Linking, dynamic loading |
| IPC | 43–55 | Pipes, SysV/POSIX IPC, mappings, file locking |
| Sockets and terminals | 56–64 | Sockets, TCP/IP, server design, alternative I/O, pty |

## Exact course assignments

| Course | Chapters/sections | Why | Check |
| --- | --- | --- | --- |
| [S1](../systems/S1-computer-systems-foundations.md) | **2–7, 24–27** | Concepts, file I/O, processes, memory, fork/exec/wait | Trace a process and its descriptors |
| [S5](../systems/S5-virtual-memory.md) | §§**6.3–6.4**, Ch. **49–50** | Memory allocation, mappings, VM operations | Map a file and observe page faults |
| [S6](../systems/S6-concurrency-atomics-and-memory-models.md) | Ch. **29–33, 53** | Threads, synchronization, thread safety, cancellation, POSIX semaphores | Implement a bounded queue |
| [S8](../systems/S8-numa-and-memory-topology.md) | §**35.4** | CPU affinity and scheduling | Pin a process and measure |
| [S9](../systems/S9-performance-engineering-and-observability.md) | §**10.7**, Ch. **12, 35–36** | Clocks/timers, `/proc`, priorities, resources | Measure CPU/memory and explain a counter |
| [S10](../systems/S10-linux-systems-programming-and-networking.md) | Ch. **4–5, 13–14, 18, 20–27, 29–30, 34–37, 43–44, 56–64** | I/O, files, signals, processes, threads, daemons, IPC, sockets, pty | Build a multi-client service |
| [S11](../systems/S11-distributed-systems.md) | Ch. **43–44, 56, 59–61** | IPC, sockets, protocols, server design | Implement RPC framing and timeouts |
| [S12](../systems/S12-data-systems-and-storage-engines.md) | Ch. **13–14, 49–50, 55** | Buffering, filesystems, mappings, file locking | Explain `fsync` and a durable rename |
| [S14](../systems/S14-containers-virtualization-and-cloud-operations.md) | Ch. **2–3, 6–7, 38–39** (selected) | Process model, credentials, capabilities | Explain what a container shares |
| [S16](../systems/S16-networking-and-protocols-deep-dive.md) | Ch. **56–61** | Sockets, TCP/IP, server design | Diagnose a connection with `ss`/`tcpdump` |
| [D1](../security/D1-security-foundations-and-threat-modeling.md) | Ch. **8–9, 15, 17, 38–39** | Users, credentials, attributes, ACLs, privileged programs, capabilities | Audit a file/process permission |
| [D2](../security/D2-memory-corruption-and-binary-exploitation.md) | Ch. **6–7**, §**38.9** | Memory allocation, virtual memory, secure privileged programs | Explain a memory-safety failure |
| [D3](../security/D3-network-and-web-application-security.md) | Ch. **38, 56–61** | Secure privileged programs, sockets, protocols | Explain a network trust boundary |
| [D4](../security/D4-systems-and-infrastructure-penetration-testing.md) | Ch. **37–39, 56–63** | Daemons, credentials, capabilities, sockets, server design | Assess a local service safely |

## Reading route

1. **S1:** Ch. 2–7, then 24–27. Type the examples; use `strace` on each.
2. **S5:** §6.3–6.4 and Ch. 49–50. Map a file, fault it, and measure.
3. **S6:** Ch. 29–33. Implement mutex/condvar/semaphore exercises before touching Rust atomics.
4. **S10:** Ch. 56–61 first, then the process/signal chapters as needed. Build the service early; use the book as a reference.
5. **S11:** Ch. 43–44 and 56, then 59–61. Focus on framing, timeouts, and partial I/O.
6. **S12:** Ch. 13–14, 49–50, 55. Connect `msync`, `fsync`, and file locking to your WAL.
7. **Security:** D1/D2/D3/D4 reading is targeted; do not read Ch. 38–39 once and assume you can write privileged code.

## High-value tables and APIs

- `open(2)` flags and `O_CLOEXEC`
- `read`/`write` partial-I/O and `EINTR`
- `fork`/`execve`/`waitpid` semantics
- `sigaction` and async-signal-safe functions
- `pthread_create`, mutexes, condition variables
- `mmap`, `msync`, `mprotect`
- `epoll` and alternative I/O models
- `getaddrinfo`, `socket`, `bind`, `listen`, `accept`
- `SO_REUSEADDR`, `TCP_NODELAY`, `SO_KEEPALIVE`
- `capabilities(7)` and least privilege

## Edition warning

The 1st edition is from 2010. Modern Linux adds:

- `io_uring` (Ch. 63 is older alternative I/O, not io_uring);
- newer `clone3`, `pidfd`, and `seccomp` APIs;
- cgroup v2 details;
- changed default socket and filesystem behaviour.

Always check `man 2`/`man 7` for your kernel. Record the kernel version in your lab README.

## Acquisition

Purchase or borrow a legal copy. Do not commit a PDF. The ISBN is 978-1593272203. The book's example code is available from the publisher; do not paste it into your repo without understanding it.
