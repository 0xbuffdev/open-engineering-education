# F1 — Programming I: Python

**Track:** Foundations · **Prerequisite:** F0 · **Core** · **Time:** 8 weeks, 120 hours · **Project:** P1 ledgerlab v1

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../progress.md)

## Purpose

Learn to turn a problem into a small, tested, readable program. Python is the teaching language because it lets you focus on logic, data, and interfaces without manual memory management. You will still learn what the interpreter does and where Python hides costs.

## Outcomes

You can:

- write functions, loops, conditionals, and collection transformations without a template;
- choose lists, dicts, sets, tuples, and comprehensions appropriately;
- read and write files safely, including malformed input;
- raise, catch, and design exceptions;
- structure a program into modules and a package;
- write unit tests with `pytest` and debug with a debugger;
- use `argparse`, `pathlib`, `json`, and `csv` to build a CLI;
- explain source → bytecode → interpreter and the cost of a Python loop;
- use Git for small, focused commits.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| [Python Tutorial](https://docs.python.org/3/tutorial/) | Ch. 1–9, 11–12 | Language core, data structures, modules, errors, stdlib |
| [Python Tutorial](https://docs.python.org/3/tutorial/) | Ch. 10, 13 | Brief stdlib tour and virtual environments |
| [CS50x](https://cs50.harvard.edu/x/) or [CS50P](https://cs50.harvard.edu/python/) | Weeks 0–6, or CS50P weeks 0–8 | Guided practice and problem-solving habits |
| B1 *But How Do It Know?* | “Introduction” through “The Magic Bus” | Bits, gates, bytes, codes, and the bus; no programming prerequisite |
| [pytest docs](https://docs.pytest.org/) | “Get Started” and “Assertions” | Testing from the first week |
| [Ruff](https://docs.astral.sh/ruff/) and [mypy](https://mypy.readthedocs.io/) | Quick start | Formatting, linting, type checking |

**Reading rule:** read the Python Tutorial section *before* the lab that uses it. Do not read all 13 chapters in one sitting.

## Modules

### 1. Values, control flow, functions

- integers, floats, strings, booleans, `None`;
- operators, precedence, truthiness, short-circuiting;
- `if`/`elif`/`else`, `for`, `while`, `break`, `continue`;
- functions, arguments, return values, default arguments, keyword arguments;
- scope, local/global, `nonlocal`;
- recursion basics;
- docstrings and naming.

### 2. Collections and data modelling

- lists, tuples, dicts, sets;
- slicing, unpacking, iteration;
- comprehensions and generator expressions;
- sorting with `key`, `sorted`, `min`, `max`;
- `collections` (`Counter`, `defaultdict`, `deque`, `namedtuple`);
- `dataclasses`;
- mutability, aliasing, copying;
- hashability and why mutable keys fail.

### 3. Files, errors, and data formats

- `pathlib.Path`, text vs binary, encodings (UTF-8), newlines;
- `open`, context managers, reading/writing/append;
- `csv` and `json`;
- exceptions: `try`/`except`/`else`/`finally`, custom exceptions;
- validating untrusted input;
- atomic writes and why "write then rename" matters;
- logging instead of `print`.

### 4. Modules, packaging, and CLI

- modules, packages, `__init__.py`, imports;
- `pyproject.toml`, editable install, dependency pinning;
- `argparse` subcommands, help text, exit codes;
- `pathlib`, `os`, `sys`, `subprocess` basics;
- environment variables and configuration;
- `ruff`, `mypy`/`pyright`, `pytest`, coverage;
- Git commits, branches, `.gitignore`.

### 5. How Python runs

- source → tokens → AST → bytecode → CPython VM;
- `dis` and bytecode inspection;
- reference counting, garbage collection, and why memory can grow;
- the GIL and when it matters;
- list/dict implementation costs;
- vectorization vs loops (preview of AI1).

## Labs

### Lab 1 — Bits and bytes

Encode a short ASCII and UTF-8 message by hand. Inspect the bytes with Python. Show one invalid byte sequence and how a decoder handles it. Explain why `len("é")` can differ from the number of bytes.

**Evidence:** table of characters → code points → bytes, plus a small script.

### Lab 2 — Twelve small programs

Implement twelve programs, each with a normal and an invalid/boundary test:

1. unit conversion with integer/float edge cases;
2. grade or tariff calculation with conditionals;
3. loop-driven number statistics;
4. string normalization and word counting;
5. list/dict aggregation;
6. a pure function with docstring and tests;
7. a function that raises a useful exception;
8. CSV reader that rejects malformed rows;
9. JSON round trip with schema validation;
10. CLI argument parsing without global state;
11. a deliberately broken off-by-one program and diagnosis;
12. a deliberately broken file-handling program and diagnosis.

### Lab 3 — Habit tracker CLI v1

Build `habit` with `add`, `list`, `done`, and `stats` commands. Persist to JSON or CSV. Requirements:

- validate the file and reject malformed records with a clear message;
- write atomically (temp file + rename);
- include `--help` and useful exit codes;
- test normal, boundary, and invalid inputs;
- run from a clean virtual environment.

**Evidence:** repository, tests, transcript, README with setup and failure example.

### Lab 4 — Debugger and profiler

Take a buggy program, reproduce the bug, use a debugger to inspect variables and the call stack, fix it, and add a regression test. Then profile a slow loop with `cProfile` or `timeit` and explain one optimization.

**Evidence:** before/after output, debugger transcript, timing table.

## Exercises

- 30 short problems across strings, lists, dicts, sets, files, exceptions, and functions.
- 5 problems that require reading a traceback and fixing the root cause.
- 3 problems that require writing a test before the implementation.
- 2 problems that compare a loop with a comprehension/generator for memory and speed.
- 1 written explanation of mutable default arguments and one of late binding in closures.

## Project increment — P1 ledgerlab v1

Build the first version of a personal ledger CLI:

- import a CSV expense/measurement log;
- validate it against a documented schema;
- normalize to JSONL or SQLite;
- produce deterministic summaries;
- include tests, README, and a failure/recovery example.

Full brief: [../projects/project-ladder.md](../projects/project-ladder.md#p1--ledgerlab).

## Exit check

Without a template, build a small program that uses functions, loops, conditionals, a collection, file I/O, and error handling. Then:

- [ ] explain how the source becomes a running process;
- [ ] show a test suite and a failing test you fixed;
- [ ] explain one Python performance cost and how you measured it;
- [ ] demonstrate the habit tracker from a clean environment;
- [ ] show a Git history with focused commits.

## Common failure modes

- Copying code from a tutorial and calling it done. Rebuild it from a blank file.
- Using `except Exception: pass`. Catch specific errors and handle or re-raise.
- Mutating a list while iterating over it.
- Using a list where a set/dict gives O(1) lookup.
- Ignoring encodings until a non-ASCII file breaks.
- Writing one giant `main()` with no tests.

## Evidence to commit

- `labs/foundations/F1/` with the bits lab and debugger/profiler report
- `exercises/foundations/F1/` with 30 problems and tests
- P1 v1 repository or a link to it
- `notes/foundations/F1/summary.md`
- `notes/foundations/F1/resources.md`

## Optional depth

- *Fluent Python* chapters on data model, iterators, and generators.
- *Automate the Boring Stuff with Python* for practical scripting.
- `pytest` fixtures, parametrization, and `hypothesis`.
- `click` or `typer` after you can build the CLI with `argparse`.
