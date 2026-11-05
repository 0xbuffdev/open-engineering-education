# SEF4 — Data Structures & Algorithms

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** [SEF2](SEF2.md)
**Duration:** 6 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

This course teaches the implementation of core data structures and algorithms: lists, stacks, queues, linked lists, trees, graphs, searching, sorting, and recursion. Learners analyze their time and space complexity and choose an approach that fits the problem.

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

#### Outcomes

- Explain how arrays, linked lists, stacks, queues, maps, and sets store data and what each operation costs.
- Choose a data structure from the requirements of a problem.

#### Lessons

1. **Course introduction: Data Structures & Algorithms** — `lesson`

   Every program stores and processes data, and the choice of structure and algorithm decides whether it is fast or unusable. This course teaches the standard structures and algorithms, how to implement them, and how to compare them.
2. **Arrays and lists** — `lesson`
3. **Linked lists** — `lesson`
4. **Stacks** — `lesson`
5. **Queues and deques** — `lesson`
6. **Maps and hash tables** — `lesson`
7. **Sets** — `lesson`
8. **Choosing structures** — `test`
9. **Stack and queue costs** — `lab`

### Module 2 — Trees, Graphs & Recursion

#### Outcomes

- Write recursive solutions and trace recursive calls.
- Implement trees, binary search trees, and graphs, and traverse them with breadth-first and depth-first search.

#### Lessons

1. **Recursion** — `lesson`
2. **Trees** — `lesson`
3. **Tree traversal** — `lesson`
4. **Binary search trees** — `lesson`
5. **Graphs** — `lesson`
6. **Breadth-first search** — `lesson`
7. **Depth-first search** — `lesson`
8. **Recursion and graphs** — `test`
9. **Traverse a graph** — `lab`

### Module 3 — Searching, Sorting & Complexity

#### Outcomes

- Express the time and space cost of an algorithm in Big-O notation.
- Implement, compare, and choose between searching and sorting algorithms.

#### Lessons

1. **Counting operations** — `lesson`
2. **Big-O notation** — `lesson`
3. **Linear search** — `lesson`
4. **Binary search** — `lesson`
5. **Merge sort** — `lesson`
6. **Quicksort** — `lesson`
7. **Comparing sorts** — `lesson`
8. **Complexity** — `test`
9. **Benchmark two sorts** — `lab`

### Module 4 — Algorithm Toolkit

#### Outcomes

- Complete and explain the **Algorithm Toolkit** integration lab, demonstrating the relevant course outcomes and retained evidence.

#### Lessons

1. **Algorithm Toolkit** — `lab`

   **Final integration lab — required work**

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

## Completion requirements

- Complete the required course exercises, checkpoints and evaluated labs below.
- Complete the final integrated `lab` in the last module and meet its observable exit criteria.
- Retain reproducible artifacts, verification results, design explanations, and a technical retrospective as required by the [OEE Evidence Rules](../../spec/evidence-rules.md).

**Required exercises**

**Conceptual practice:**

- Implementation drills
- Tracing exercises
- Complexity analysis
- Recursive-call tracing
- Algorithm comparison

**Practical practice:**

- Implement a stack and queue.
- Compare linear search and binary search.
- Implement BFS and DFS.
- Measure sorting algorithms on increasingly large inputs.

**Exit demonstration:**

Given a new problem, the learner must:

- Choose an appropriate data structure
- Propose an algorithm
- Derive its complexity
- Explain why an obvious alternative approach is less suitable
