# SEF6 — Required practical work and evaluation

> Public draft requirements preserved from the source. Independent learners can use these without a 0xNAND subscription. Detailed lab procedures and verification fields still require conformance review.

## Practical exercises

- Inspect the bytes of values of different types.
- Trace a pointer program by hand and compare it with real output.
- Repair a program with a leak, a double free, and an overrun.
- Compile and inspect object files.
- Diagnose a segmentation fault with a debugger.

## Course lab

### C Data-Structure Library

Implement a small, tested library in C containing a dynamic array, a linked list, and a hash map, each with a documented interface. The library must include:

- Separate header and source files with a Makefile
- A test program that exercises normal use and failure cases
- A clean run under a memory sanitizer, with no leaks or errors
- A short written comparison of how the same structures manage memory in Python and in C

## Exit check

The learner can write a multi-file C program, explain every allocation and its lifetime, and explain the path from source code to a running process.
