# SEF2 — Lesson authoring notes

> Optional instructional context preserved from the original source. These notes are not additional course metadata, assessment criteria, or required module briefs.

## Course orientation

- **Introduction:** Programming is the central skill of the curriculum. This course teaches it from the first terminal command to a finished command-line application, with an emphasis on understanding what the computer does at each step.
- **History:** Guido van Rossum began Python in the late 1980s and released it in 1991. Python 3, a deliberate redesign, followed in 2008. The name refers to the comedy group Monty Python.
- **Usage:** The learner writes programs in a terminal and an editor, runs them with the Python interpreter, and tests and debugs them.
- **Applications:** Python is used for web back ends, automation, data analysis, scientific computing, and machine learning.
- **Strengths:** Its syntax is readable, its standard library is large, and it lets beginners concentrate on programming concepts.
- **Limitations:** Python programs usually run more slowly than compiled programs, and many type errors appear only when the code runs.
- **Key concepts:** program; source code; interpreter; value; type; variable; binding; condition; loop; function; collection; mutability; file; exception; test; command-line application

## Module 1 — Software, Code & Languages

- **Introduction:** Before writing code it helps to know what code is. This module explains what software, a program, coding, and software engineering are, and how a program written for people becomes something a machine runs.
- **Overview:** It covers languages, source code, interpreters and compilers, and how CPython compiles source to bytecode and runs it on a virtual machine.
- **History:** FORTRAN, released in 1957, was the first widely used high-level language, C appeared in 1972, and Guido van Rossum released Python in 1991.
- **Key concepts:** software; program; source code; high-level and low-level languages; interpreter; compiler; bytecode; virtual machine

## Module 2 — Your Workspace

- **Introduction:** Programming happens in an environment you control. This module sets up and explains the three tools used every day: the terminal, a code editor, and the Python interpreter.
- **Overview:** It covers the shell and basic commands, installing Python, editing and running a file, the interactive prompt, and reading a first error message.
- **Key concepts:** terminal; shell; prompt; directory and path; editor; interpreter; error message

## Module 3 — Thinking in Programs

- **Introduction:** A program is a sequence of steps acting on values. This module builds that idea from the smallest pieces.
- **Overview:** It covers values and types, expressions, variables, output, how a name is bound to an object, and tracing a program by hand.
- **Key concepts:** value; type; expression; variable; binding; object; reference; heap; state; trace

## Module 4 — Conditions & Loops

- **Introduction:** Programs become useful when they choose and repeat. This module teaches conditions and loops.
- **Overview:** It covers Boolean expressions, if statements, while and for loops, and common loop patterns.
- **History:** The earliest machine languages already had conditional jumps, which compose into loops. Structured control flow became standard after Edsger Dijkstra's 1968 letter criticizing the goto statement.
- **Key concepts:** Boolean; condition; if and else; while; for; range; break and continue; loop patterns

## Module 5 — Functions & Decomposition

- **Introduction:** Large problems become manageable when split into named pieces. Functions are the basic tool.
- **Overview:** It covers defining and calling functions, parameters and arguments, return values, local variables and scope, call frames on the call stack, decomposition, and modules.
- **Key concepts:** function; parameter; argument; return value; scope; call stack; frame; interface; decomposition; module

## Module 6 — Strings & Collections

- **Introduction:** Real programs handle many values at once. This module introduces Python's built-in containers and the rules for choosing among them.
- **Overview:** It covers strings, lists, dictionaries, tuples, and sets, mutable and immutable objects, aliasing, and copying.
- **Strengths:** Built-in collections are fast, well tested, and expressive.
- **Limitations:** A mutable collection can be changed through any name that refers to it, and a poor choice, such as searching a list instead of a set, makes programs slow.
- **Key concepts:** string; list; dictionary; tuple; set; mutable and immutable; alias; shallow copy

## Module 7 — Files & Data

- **Introduction:** A program that forgets everything when it stops is limited. This module covers reading and writing files and storing structured data.
- **Overview:** It covers reading and writing text files, paths and directories, and the JSON format.
- **History:** Douglas Crockford specified JSON in the early 2000s from JavaScript's object notation, and it was later standardized as ECMA-404.
- **Key concepts:** file; path; reading and writing; text encoding; JSON; serialization

## Module 8 — Errors & Debugging

- **Introduction:** Every program fails. This module teaches how to read failures, handle expected ones, and find unexpected ones systematically.
- **Overview:** It covers tracebacks, exceptions, validating input, and debugging as forming and testing hypotheses.
- **History:** The word bug was used for faults in machines long before computers. A moth found in the Harvard Mark II in 1947 is a famous logbook entry.
- **Limitations:** Catching exceptions too broadly hides real faults, and validation cannot foresee every bad input.
- **Key concepts:** traceback; exception; try and except; raise; validation; hypothesis; reproduction

## Module 9 — Command-Line Task Manager

- **Introduction:** This module turns separate skills into one tool that people can run from a terminal. It also introduces the habits that keep it working: tests and logs.
- **Overview:** It covers command-line arguments, automated checks with doctest and unittest, logging, and the course lab.
- **Key concepts:** command-line argument; exit status; test; assertion; logging; persistence

## Original topic inventory

- Software, programming, and software engineering
- Programming languages, source code, interpreters, and compilers
- Bytecode and the Python virtual machine
- The terminal, installing Python, and code editors
- The Python prompt and running files
- Reading error messages
- Steps and programs
- Values and types
- Expressions and variables
- Names, objects, and references
- The call stack and the heap, at Python level
- Mutable and immutable objects, aliasing
- Conditionals, `while` loops, and `for` loops
- Functions, parameters, and scope
- Return values and decomposition
- Modules and imports
- Strings, lists, dictionaries, tuples, and sets
- Reading and writing files
- Structured data and JSON
- Paths and directories
- Tracebacks and exceptions
- Input validation
- Debugging as a reasoning process
- Command-line arguments
- Automated checks with doctest and unittest
- Logging
