# SEF4 — Data Structures & Algorithms

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** [SEF2](SEF2.md)
**Duration:** 10 weeks
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
- Analyze data-structure invariants and amortized operation cost; use heaps, weighted graphs, and algorithmic design strategies on unfamiliar problems.

## Modules

### Module 1 — Data Organization

#### Outcomes

- Explain how arrays, linked lists, stacks, queues, maps, and sets store data and what each operation costs.
- Choose a data structure from the requirements of a problem.

- Prove container invariants and compare measured operation costs.

#### Lessons

1. **Course introduction: Data Structures & Algorithms** — `lesson`

   Every program stores and processes data, and the choice of structure and algorithm decides whether it is fast or unusable. This course teaches the standard structures and algorithms, how to implement them, and how to compare them.
2. **Arrays and lists** — `lesson`
3. **Linked lists** — `lesson`
4. **Stacks** — `lesson`
5. **Queues and deques** — `lesson`
6. **Maps and hash tables** — `lesson`
7. **Sets** — `lesson`
8. **Capacity, resizing, and amortized array append** — `lesson`
9. **Hash collisions, probing, and load factors** — `lesson`
10. **Invariants and mutation edge cases** — `lesson`
11. **Choosing structures** — `test`
12. **Stack and queue costs** — `lab`

### Module 2 — Trees, Graphs & Recursion

#### Outcomes

- Write recursive solutions and trace recursive calls.
- Implement trees, binary search trees, and graphs, and traverse them with breadth-first and depth-first search.

- Trace recursion on a cyclic graph and justify representation choice.

#### Lessons

1. **Recursion** — `lesson`
2. **Trees** — `lesson`
3. **Tree traversal** — `lesson`
4. **Binary search trees** — `lesson`
5. **Graphs** — `lesson`
6. **Breadth-first search** — `lesson`
7. **Depth-first search** — `lesson`
8. **Recursive termination, stack depth, and memory** — `lesson`
9. **Adjacency lists, adjacency matrices, and disconnected graphs** — `lesson`
10. **Cycle detection and traversal correctness** — `lesson`
11. **Recursion and graphs** — `test`
12. **Traverse a graph** — `lab`

### Module 3 — Searching, Sorting & Complexity

#### Outcomes

- Express the time and space cost of an algorithm in Big-O notation.
- Implement, compare, and choose between searching and sorting algorithms.

- Explain analytical bounds separately from experimental run times.

#### Lessons

1. **Counting operations** — `lesson`
2. **Big-O notation** — `lesson`
3. **Linear search** — `lesson`
4. **Binary search** — `lesson`
5. **Merge sort** — `lesson`
6. **Quicksort** — `lesson`
7. **Comparing sorts** — `lesson`
8. **Best-, average-, and worst-case analysis** — `lesson`
9. **Sorting stability and input-sensitive cost** — `lesson`
10. **Space/time trade-offs and fair benchmarking** — `lesson`
11. **Complexity** — `test`
12. **Benchmark two sorts** — `lab`

### Module 4 — Algorithm Analysis & Correctness

#### Outcomes

- State and test algorithm invariants, termination and resource bounds.
- Demonstrate reasoning with both ordinary and deliberately failing inputs.

#### Lessons

1. **Preconditions, postconditions, and loop invariants** — `lesson`
2. **Induction and recursive proofs** — `lesson`
3. **Recurrence relations and recursion trees** — `lesson`
4. **Worst-case, expected, and amortized analysis** — `lesson`
5. **Auxiliary space, recursion depth, and input constraints** — `lesson`
6. **Algorithm Analysis & Correctness reasoning and diagnosis** — `test`
7. **Verify binary-search invariants** — `lab`

### Module 5 — Heaps & Priority Queues

#### Outcomes

- Implement and defend a binary heap under changing workload.
- Demonstrate reasoning with both ordinary and deliberately failing inputs.

#### Lessons

1. **Array representation of a complete binary tree** — `lesson`
2. **Heap insert, sift, extract, and heapify** — `lesson`
3. **Priority queue contracts, tie-breaking, and complexity** — `lesson`
4. **Heapsort and scheduling applications** — `lesson`
5. **Heaps & Priority Queues reasoning and diagnosis** — `test`
6. **Build a priority-queue scheduler** — `lab`

### Module 6 — Weighted Graphs & Dependencies

#### Outcomes

- Select graph algorithms based on edge weights, reachability and cycle assumptions.
- Demonstrate reasoning with both ordinary and deliberately failing inputs.

#### Lessons

1. **Directed, undirected and weighted graphs** — `lesson`
2. **Reachability and graph components** — `lesson`
3. **Shortest paths with BFS for unweighted graphs** — `lesson`
4. **Dijkstra algorithm and nonnegative weights** — `lesson`
5. **Topological ordering of a directed acyclic graph** — `lesson`
6. **Cycle detection and unreachable nodes** — `lesson`
7. **Weighted Graphs & Dependencies reasoning and diagnosis** — `test`
8. **Implement routing and dependency checks** — `lab`

### Module 7 — Algorithm Design Strategies

#### Outcomes

- Compare greedy, dynamic programming and exhaustive reasoning for correctness and cost.
- Demonstrate reasoning with both ordinary and deliberately failing inputs.

#### Lessons

1. **Divide and conquer and recurrence structure** — `lesson`
2. **Greedy choices and counterexamples** — `lesson`
3. **Dynamic programming and memoization** — `lesson`
4. **Backtracking, pruning and search space** — `lesson`
5. **Algorithm selection from constraints** — `lesson`
6. **Algorithm Design Strategies reasoning and diagnosis** — `test`
7. **Disprove a greedy solution** — `lab`

### Module 8 — Algorithm Toolkit

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

Complete these required exercises:

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

**Expanded assessment and lab criteria:**

- **Module 1 checkpoint:** Prove container invariants and compare measured operation costs.
- **Module 2 checkpoint:** Trace recursion on a cyclic graph and justify representation choice.
- **Module 3 checkpoint:** Explain analytical bounds separately from experimental run times.

- **Module 4 — Verify binary-search invariants:**
  - Objective: State and test algorithm invariants, termination and resource bounds.
  - Prerequisites: Complete the teaching lessons and conceptual checkpoint.
  - Environment: Record the language/runtime and tool versions and provide self-contained safe input fixtures.
  - Work: Derive an invariant for binary search, inject an off-by-one defect, and verify a corrected algorithm with empty and boundary fixtures.
  - Verification: Compare theoretical bounds against observed inputs; produce tests and a reasoning trace.
  - Evidence: Counterexamples, code, trace and complexity justification.
  - Failure analysis: Explain at least one incorrect result, boundary condition or runtime failure and the correction.
- **Module 5 — Build a priority-queue scheduler:**
  - Objective: Implement and defend a binary heap under changing workload.
  - Prerequisites: Complete the teaching lessons and conceptual checkpoint.
  - Environment: Record the language/runtime and tool versions and provide self-contained safe input fixtures.
  - Work: Implement a min-heap for scheduled tasks including ties, rescheduling and empty queue behavior.
  - Verification: Validate heap order after each mutation and compare extraction order with a simple reference.
  - Evidence: Scheduler, invariant tests and complexity note.
  - Failure analysis: Explain at least one incorrect result, boundary condition or runtime failure and the correction.
- **Module 6 — Implement routing and dependency checks:**
  - Objective: Select graph algorithms based on edge weights, reachability and cycle assumptions.
  - Prerequisites: Complete the teaching lessons and conceptual checkpoint.
  - Environment: Record the language/runtime and tool versions and provide self-contained safe input fixtures.
  - Work: Implement a shortest-route example and a dependency ordering routine, including disconnected and cyclic fixtures.
  - Verification: Reject unsupported negative weights and cyclic dependency inputs; match hand-calculated results.
  - Evidence: Graph fixtures, route proofs, tests and failure trace.
  - Failure analysis: Explain at least one incorrect result, boundary condition or runtime failure and the correction.
- **Module 7 — Disprove a greedy solution:**
  - Objective: Compare greedy, dynamic programming and exhaustive reasoning for correctness and cost.
  - Prerequisites: Complete the teaching lessons and conceptual checkpoint.
  - Environment: Record the language/runtime and tool versions and provide self-contained safe input fixtures.
  - Work: Construct a counterexample where greedy fails, implement dynamic programming, and compare on small inputs to exhaustive solutions.
  - Verification: Show a counterexample, correct recurrence and tested optimality on bounded fixtures.
  - Evidence: Counterexample, code, recurrence, measurements and evaluation.
  - Failure analysis: Explain at least one incorrect result, boundary condition or runtime failure and the correction.

**Final integration lab extension:**

- The final integrated lab must demonstrate the existing course outcomes and the additional outcomes in this expanded algorithm pathway.
- Provide explicit negative tests, clean-checkout reproduction, explanation of assumptions, and a technical retrospective.

**Exit demonstration:**

Given a new problem, the learner must:

- Choose an appropriate data structure
- Propose an algorithm
- Derive its complexity
- Explain why an obvious alternative approach is less suitable
