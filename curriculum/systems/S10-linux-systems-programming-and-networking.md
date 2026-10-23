# S10 — Linux Systems Programming & Networking

**Track:** Systems · **Prerequisite:** S1, S6 · **Core** · **Time:** 7 weeks, 105 hours · **Project:** P4 workbenchd

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../progress.md)

## Purpose

Build real Linux programs that own resources, handle signals, and serve multiple clients over sockets. This is the bridge from "I understand syscalls" to "I can write a service that survives partial I/O, disconnects, overload, and shutdown."

## Outcomes

You can:

- write a multi-file C program with a Makefile and tests;
- use `fork`/`exec`, pipes, FIFOs, and file locking correctly;
- handle signals with `sigaction`, self-pipes, and `signalfd`;
- build a TCP client/server with correct partial read/write handling;
- use `epoll` (and know when `select`/`poll` are enough);
- design a length-delimited or line-delimited protocol;
- handle timeouts, disconnects, backpressure, and graceful shutdown;
- use `getaddrinfo`, `SO_REUSEADDR`, `TCP_NODELAY`, and socket options correctly;
- test with `nc`, `curl`, `strace`, and a load generator.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| B2 | Ch. **8** | UNIX system interface: descriptors, low-level I/O, directories, allocator |
| B5 | Ch. **4–5, 13–14, 18, 20–27, 29–30, 34–37, 43–44, 56–64** | File I/O, filesystems, signals, processes, threads, daemons, IPC, sockets, alternative I/O, pty |
| B4 | Ch. **33** | Event-based concurrency |
| [Beej's Guide to Network Programming](https://beej.us/guide/bgnet/) | Ch. 1–8 | Sockets, client/server, advanced topics |
| CS:APP | Ch. **10–11** | System-level I/O, network programming |
| [Linux `epoll` man page](https://man7.org/linux/man-pages/man7/epoll.7.html) | Full | Event loop semantics |

## Modules

### 1. Files and processes

- `open` flags, `O_CLOEXEC`, `O_NONBLOCK`, `O_SYNC`;
- partial I/O, `EINTR`, `EAGAIN`;
- `pread`/`pwrite`, `readv`/`writev`, `sendfile`;
- `fsync`/`fdatasync` and durability;
- `fork`/`exec`/`wait`; process groups and sessions;
- daemons, double-fork, `setsid`, logging;
- `systemd` units and socket activation (intro).

### 2. Signals and timers

- signal dispositions, masks, pending signals;
- `sigaction`, `SA_RESTART`, `SA_SIGINFO`;
- async-signal-safe functions;
- self-pipe trick and `signalfd`;
- `SIGCHLD` and child reaping;
- timers: `alarm`, `setitimer`, `timerfd`, `clock_nanosleep`;
- graceful shutdown via `SIGTERM`/`SIGINT`.

### 3. IPC

- pipes and FIFOs;
- UNIX domain sockets;
- shared memory (`mmap`, POSIX shm);
- semaphores and file locks;
- message queues (awareness);
- when to use each.

### 4. Sockets and protocols

- TCP vs UDP vs UNIX domain;
- `socket`, `bind`, `listen`, `accept`, `connect`;
- `getaddrinfo`, IPv4/IPv6, dual-stack;
- byte order, `htonl`/`ntohl`;
- partial reads/writes and message framing;
- length-delimited vs line-delimited protocols;
- timeouts, keepalive, `TCP_NODELAY`;
- `SO_REUSEADDR`, `SO_REUSEPORT`;
- DNS basics and failure modes;
- TLS overview (terminate at proxy or use a library).

### 5. Event-driven servers

- blocking vs nonblocking;
- `select`/`poll`/`epoll` (level vs edge triggered);
- event loop structure;
- accept loop and thundering herd;
- per-connection state machines;
- backpressure and bounded buffers;
- slowloris and idle timeouts;
- graceful shutdown;
- thread-per-connection vs event loop vs hybrid;
- `io_uring` overview.

## Labs

### Lab 1 — C CLI toolkit

Build a multi-file C CLI with subcommands, a Makefile, tests, and a man-page-style README. Include one command that reads a file in chunks and one that spawns a child.

### Lab 2 — TCP echo server

Implement a single-threaded blocking TCP echo server. Test with `nc`. Then break it deliberately with a client that sends half a message and a client that disconnects mid-write. Fix the handling.

### Lab 3 — Multi-client event loop

Rewrite the server with `epoll` and nonblocking sockets. Support:

- multiple clients;
- partial reads/writes;
- per-client output buffer with a cap;
- idle timeout;
- `SIGTERM` graceful shutdown;
- a simple metrics log.

### Lab 4 — Protocol and backpressure

Define a length-delimited protocol. Add a bounded queue per client and reject/drop policy when full. Write a load generator that sends faster than the server can process. Show that memory stays bounded.

### Lab 5 — Rust service

Rewrite the event loop in Rust with `tokio` or `mio`. Compare safety, complexity, and performance. Do not hide the syscalls; explain what the runtime does.

## Exercises

1. Explain partial read/write with a timeline.
2. Implement `readn`/`writen` and test with a pipe.
3. Explain `EINTR` and `SA_RESTART`.
4. Compare `select`, `poll`, and `epoll`.
5. Explain level vs edge triggered.
6. Design a framing protocol for variable-length messages.
7. Explain how a slow client causes memory growth and how to bound it.
8. Explain `SO_REUSEADDR` and one misuse.
9. Explain graceful shutdown with in-flight requests.
10. Debug a connection reset with `strace` and `tcpdump`.

## Project increment — P4 workbenchd

Build the service:

- length-delimited protocol;
- multi-client;
- bounded work queue and worker pool;
- per-client limits;
- metrics endpoint/logs;
- timeouts and backpressure;
- graceful shutdown;
- tests for partial I/O, malformed requests, disconnect, overload, shutdown;
- load test with p50/p95/p99.

**Brief:** [P4 — workbenchd](../projects/project-ladder.md#p4--workbenchd)

## Exit check

- [ ] explain all owned resources and demonstrate clean shutdown without leaks or hung clients;
- [ ] handle partial I/O, malformed input, disconnect, and overload;
- [ ] implement a multi-client event loop;
- [ ] explain backpressure and show bounded memory;
- [ ] test with a real client and a load generator;
- [ ] explain one difference between the C and Rust versions.

## Common failure modes

- Assuming one `read` returns a whole message.
- Ignoring `EINTR` and `EAGAIN`.
- Blocking the event loop with a slow operation.
- Unbounded per-client buffers.
- Closing a socket while another thread uses it.
- Shutting down without draining in-flight work.
- Using `SO_REUSEADDR` to "fix" a real bind conflict.

## Evidence to commit

- `labs/systems/S10/` with C CLI, TCP echo, epoll server, load test, Rust service
- P4 workbenchd
- `notes/systems/S10/summary.md`

## Optional depth

- *UNIX Network Programming, Volume 1* (Stevens) selected chapters.
- *The Linux Programming Interface* Ch. 63 and 64 in full.
- `io_uring` and `liburing` documentation.
- TLS with OpenSSL/rustls and certificate validation.
