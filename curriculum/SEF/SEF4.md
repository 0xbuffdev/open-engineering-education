> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

# SEF4 — Data Structures & Algorithms

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** SEF2
**Duration:** 6 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

## Overview

This course teaches the implementation of core data structures and algorithms: lists, stacks, queues, linked lists, trees, graphs, searching, sorting, and recursion. Learners analyze their time and space complexity and choose an approach that fits the problem.

## Course brief

The course introduction is the first lesson of the first module. It combines the overview above with these fields.

- **Introduction:** Every program stores and processes data, and the choice of structure and algorithm decides whether it is fast or unusable. This course teaches the standard structures and algorithms, how to implement them, and how to compare them.
- **History:** The word algorithm comes from the name of the ninth-century scholar al-Khwarizmi. Donald Knuth began The Art of Computer Programming in 1962, and its first volume, published in 1968, established the analysis of algorithms as a discipline.
- **Usage:** The learner implements each structure, measures its behavior, and chooses between alternatives from the requirements of a problem.
- **Applications:** Databases, search engines, operating systems, compilers, networks, and every program that handles a lot of data.
- **Strengths:** Standard structures and algorithms are well understood, and their costs can be stated precisely.
- **Limitations:** Asymptotic analysis ignores constant factors and hardware effects, and the best structure depends on the real workload, so measurement is also needed.
- **Key concepts:** array; linked list; stack; queue; hash table; set; tree; graph; recursion; search; sort; Big-O

## Prerequisites

- [**SEF2 — Programming & Computational Thinking**](SEF2.md)

## Learning outcomes

By the end of the course, the learner will be able to:

- Implement and use lists, stacks, queues, linked lists, trees, and graphs.
- Implement and compare searching and sorting algorithms.
- Use recursion and trace recursive execution.
- Analyze time and space complexity using Big-O notation.
- Select data structures and algorithms based on problem requirements.
- Explain and defend algorithmic trade-offs.

## Modules

### Module 1 — Data Organization

#### Module brief

- **Introduction:** How data is stored decides how fast a program can find and change it. This module compares the basic ways of organizing data.
- **Overview:** It covers array-based sequences, linked lists, stacks, queues and deques, maps and hash tables, and sets, together with the cost of each operation.
- **History:** Allen Newell, Cliff Shaw, and Herbert Simon developed linked lists in 1955 and 1956, and Hans Peter Luhn at IBM developed hashing in 1953.
- **Strengths:** Each structure makes some operations cheap.
- **Limitations:** Each also makes others expensive: arrays are slow to insert into in the middle, linked lists are slow to index, and hash tables have no order and degrade when keys collide.
- **Key concepts:** array; linked list; stack; queue; deque; hash table; set; operation cost

#### Module outcomes

By the end of this module, the learner can:

- Explain how arrays, linked lists, stacks, queues, maps, and sets store data and what each operation costs.
- Choose a data structure from the requirements of a problem.

1. **Course introduction: Data Structures & Algorithms** — what the subject is, where it came from, where it is used, and its strengths and limits
2. **Introduction: Data Organization** — what the topic is, where it is used, and its strengths and limits
3. **Arrays and lists**
4. **Linked lists**
5. **Stacks**
6. **Queues and deques**
7. **Maps and hash tables**
8. **Sets**
9. **Choosing structures**
   - kind: `test`
10. **Stack and queue costs**

- kind: `lab`

### Module 2 — Trees, Graphs & Recursion

#### Module brief

- **Introduction:** Many problems are naturally hierarchical or connected. Trees and graphs model them, and recursion is the natural way to process them.
- **Overview:** It covers recursion, trees and traversals, binary search trees, graphs, and breadth-first and depth-first search.
- **History:** Leonhard Euler founded graph theory in 1736 with the Königsberg bridge problem, and recursion became central to programming with Lisp in 1958.
- **Strengths:** They model relationships directly, and the traversals are general-purpose.
- **Limitations:** Recursion uses stack space and can overflow, an unbalanced tree degrades to a list, and graphs can use a lot of memory.
- **Key concepts:** recursion; base case; tree; traversal; binary search tree; graph; breadth-first search; depth-first search

#### Module outcomes

By the end of this module, the learner can:

- Write recursive solutions and trace recursive calls.
- Implement trees, binary search trees, and graphs, and traverse them with breadth-first and depth-first search.

1. **Introduction: Trees, Graphs & Recursion** — what the topic is, where it is used, and its strengths and limits
2. **Recursion**
3. **Trees**
4. **Tree traversal**
5. **Binary search trees**
6. **Graphs**
7. **Breadth-first search**
8. **Depth-first search**
9. **Recursion and graphs**
   - kind: `test`
10. **Traverse a graph**

- kind: `lab`

### Module 3 — Searching, Sorting & Complexity

#### Module brief

- **Introduction:** Two correct programs can differ a million times in speed. This module teaches how to measure and compare algorithms.
- **Overview:** It covers counting operations, Big-O notation, linear and binary search, merge sort, quicksort, and comparing sorting algorithms.
- **History:** John von Neumann described merge sort in 1945, Tony Hoare invented quicksort in 1959, and Donald Knuth popularized Big-O notation in computer science in the 1970s.
- **Strengths:** Asymptotic analysis predicts behavior without running the code.
- **Limitations:** It ignores constant factors and hardware effects, so real programs also need measurement.
- **Key concepts:** operation count; Big-O; linear search; binary search; merge sort; quicksort; benchmarking

#### Module outcomes

By the end of this module, the learner can:

- Express the time and space cost of an algorithm in Big-O notation.
- Implement, compare, and choose between searching and sorting algorithms.

1. **Introduction: Searching, Sorting & Complexity** — what the topic is, where it is used, and its strengths and limits
2. **Counting operations**
3. **Big-O notation**
4. **Linear search**
5. **Binary search**
6. **Merge sort**
7. **Quicksort**
8. **Comparing sorts**
9. **Complexity**
   - kind: `test`
10. **Benchmark two sorts**

- kind: `lab`

### Module 4 — Algorithm Toolkit

#### Module brief

- **Introduction:** This lab integrates the course. The learner implements the core structures and algorithms and explains their measured behavior.
- **Overview:** It combines stacks, queues, linked lists, trees, graph traversal, searching, and sorting in one tested toolkit with a benchmark report.
- **Applications:** Libraries, interview-level problem solving, and the internals of databases and language runtimes all rest on these structures.
- **Key concepts integrated:** data structure choice; traversal; recursion; Big-O; benchmarking; testing

1. **Algorithm Toolkit**
   - kind: `lab`

## Topics

- Arrays/lists
- Maps and sets
- Stacks and queues
- Linked lists
- Trees
- Graphs
- Recursion
- Searching
- Sorting
- Big-O time and space complexity
- Choosing data structures from requirements

## Small exercises

- Implementation drills
- Tracing exercises
- Complexity analysis
- Recursive-call tracing
- Algorithm comparison

## Practical exercises

2. Implement a stack and queue.
3. Compare linear search and binary search.
4. Implement BFS and DFS.
5. Measure sorting algorithms on increasingly large inputs.

## Course lab

**Algorithm Toolkit**

Implement and test:

- Stack
- Queue
- Linked list
- BST
- BFS
- DFS
- Binary search
- Merge sort
- Quicksort

Then benchmark selected operations and explain the results.

## Exit check

Given a new problem, the learner must:

2. Choose an appropriate data structure
3. Propose an algorithm
4. Derive its complexity
5. Explain why an obvious alternative approach is less suitable
