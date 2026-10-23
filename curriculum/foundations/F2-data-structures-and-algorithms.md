# F2 — Data Structures & Algorithms

**Track:** Foundations · **Prerequisite:** F1 · **Core** · **Time:** 10 weeks, 150 hours · **Project:** P1 query/index increment

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../progress.md)

## Purpose

Learn to choose and implement the right data structure, analyse cost, and prove correctness. This is the course that separates "I can write Python" from "I can engineer software." The old curriculum asked for 30 problems and eight implementations; that is not enough for professional fluency. This version asks for the full core toolkit and 80–100 problems.

## Outcomes

You can:

- derive time and space complexity from code and recurrences;
- implement arrays, linked lists, stacks, queues, hash tables, trees, heaps, graphs, and tries;
- explain collisions, resizing, balancing, and amortization;
- traverse graphs with BFS/DFS and solve shortest-path, topological, and connectivity problems;
- implement merge sort, quicksort, heapsort, and a non-comparison sort;
- recognize and apply greedy, divide-and-conquer, dynamic programming, and backtracking;
- choose a structure from requirements, not habit;
- trace recursion and prove loop invariants.

## Required reading

Choose **one** primary DS&A text and one practice platform, and record them in `notes/foundations/F2/resources.md`.

| Source | Use |
| --- | --- |
| [MIT 6.006](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) | Primary course if you want lectures and problem sets |
| *Introduction to Algorithms* (CLRS, 4th ed.) | Reference for proofs and deeper treatment; not a first read |
| *Algorithms* (Sedgewick & Wayne, 4th ed.) | Implementation-oriented alternative |
| [VisuAlgo](https://visualgo.net/) | Visualize structures and traces |
| [NeetCode](https://neetcode.io/) / LeetCode | Practice problems with labelled categories |

**Rule:** one primary source. Do not mix three curricula in the same week.

## Modules

### 1. Complexity and correctness

- RAM model, input size, best/worst/average case;
- asymptotic notation: O, Θ, Ω, little-o;
- recurrence relations and the Master Theorem (intro);
- amortized analysis (dynamic array, hash table);
- loop invariants and exchange arguments;
- space complexity and recursion depth;
- empirical timing vs asymptotic prediction.

### 2. Linear structures

- static and dynamic arrays, resizing, cache behaviour;
- singly/doubly linked lists, sentinels, cycle detection;
- stacks, queues, deques;
- monotonic stack and sliding-window patterns;
- implementation with tests and invariant checks.

### 3. Hashing and sets

- hash functions, collisions, chaining, open addressing;
- load factor, resizing, tombstones;
- `dict`/`set` implementation and iteration order;
- hashable vs mutable keys;
- counting, deduplication, grouping, and prefix-sum patterns.

### 4. Trees and heaps

- binary trees, traversals (pre/in/post/level);
- binary search trees: search, insert, delete, duplicates;
- balanced trees: AVL rotations, red-black properties (concept + one implementation);
- B-trees (concept; used in databases);
- binary heaps, `heapq`, priority queues, heapify, top-k;
- tries and prefix search;
- segment trees / Fenwick trees (optional depth).

### 5. Graphs

- representations: adjacency list, matrix, edge list;
- BFS, DFS, connected components, bipartite check;
- topological sort (Kahn and DFS);
- shortest paths: Dijkstra, Bellman–Ford, Floyd–Warshall (overview);
- minimum spanning trees: Kruskal (union-find) and Prim;
- union-find with path compression and union by rank;
- cycle detection, bridges/articulation points (optional).

### 6. Sorting and searching

- insertion, selection, bubble (for understanding);
- merge sort, quicksort, heapsort;
- stability, in-place, adaptive properties;
- lower bound for comparison sorting;
- counting/radix sort;
- binary search on arrays and on the answer;
- search in rotated arrays, lower/upper bound.

### 7. Algorithm paradigms

- greedy: interval scheduling, Huffman, coin change counterexample;
- divide and conquer: mergesort, quicksort, closest pair (intro);
- dynamic programming: memoization vs tabulation, 1D/2D, knapsack, LCS, edit distance, LIS, grid paths;
- backtracking: subsets, permutations, N-queens, pruning;
- randomized algorithms: quickselect, reservoir sampling;
- NP-completeness awareness: reduction examples, why exact solutions may be infeasible.

### 8. Strings and pattern matching

- string representation, immutability, encodings;
- KMP, Rabin–Karp, Z-algorithm (intro);
- tries for autocomplete;
- anagram/palindrome/substring patterns.

## Labs

### Lab 1 — Structure-choice study

Implement a contact/index lookup with a list, a sorted list, and a hash map. Count operations or measure time on deterministic inputs of increasing size. Explain when each choice wins and why.

### Lab 2 — Implement the core toolkit

Implement and test, without substituting a library equivalent:

- dynamic array;
- singly and doubly linked list;
- stack, queue, deque;
- hash table with chaining and resizing;
- BST with insert/delete/traversal;
- binary heap / priority queue;
- trie;
- graph with BFS/DFS/topological sort;
- union-find;
- merge sort, quicksort, heapsort, counting sort;
- binary search (iterative and recursive).

Each implementation needs normal, boundary, and invalid-case tests.

### Lab 3 — Graph route finder

Build an adjacency-list graph and find the shortest unweighted path with BFS. Add an unreachable target, a malformed graph, and a path reconstruction. Extend to weighted Dijkstra with a priority queue.

### Lab 4 — Dynamic programming notebook

Solve five DP problems from scratch: climbing stairs, coin change, LIS, edit distance, and 0/1 knapsack. For each, write the recurrence, base cases, order of evaluation, complexity, and one failed approach.

### Lab 5 — Benchmark and explain

Benchmark list vs set membership, BST vs hash map lookup, and merge sort vs quicksort on sorted/duplicate-heavy input. Predict the result before measuring; explain every surprise.

## Exercises

Complete **80–100 labelled problems**:

- 20 arrays/strings/two pointers;
- 15 maps/sets/prefix sums;
- 15 linked lists/stacks/queues;
- 15 trees/heaps/tries;
- 15 graphs/search;
- 10 dynamic programming/greedy;
- 10 mixed interview-style problems.

For at least 15 problems, record the first failed approach and why it failed. Re-solve 10 problems from scratch after two weeks.

## Project increment — P1 query/index

Extend `ledgerlab` with:

- an in-memory index for fast lookup by date/category/text;
- a documented choice between hash index, sorted index, and B-tree-like index;
- a benchmark showing the trade-off;
- tests for duplicates, missing keys, and large inputs.

**Brief:** [P1 — ledgerlab](../projects/project-ladder.md#p1--ledgerlab)

## Exit check

- [ ] choose and defend a data structure for a new problem;
- [ ] derive operation costs and space usage;
- [ ] trace a recursive call stack by hand;
- [ ] implement a graph algorithm and explain its invariant;
- [ ] solve an unseen medium problem in 45 minutes with tests;
- [ ] explain one case where the theoretically better structure loses in practice.

## Common failure modes

- Memorizing solutions instead of patterns. Re-derive from the invariant.
- Using `list` for membership tests in a loop.
- Forgetting recursion depth and stack overflow.
- Writing a hash table without handling resizing or deletion.
- Treating average-case as worst-case.
- Benchmarking with inputs that fit in cache and concluding "it's fast."

## Evidence to commit

- `labs/foundations/F2/` with implementations, benchmarks, and reports
- `exercises/foundations/F2/` with problem solutions and tests
- P1 query/index increment
- `notes/foundations/F2/summary.md`
- `notes/foundations/F2/resources.md` naming the primary source

## Optional depth

- CLRS chapters on amortized analysis, red-black trees, and NP-completeness.
- *Algorithm Design Manual* (Skiena) for practical heuristics.
- Segment trees, Fenwick trees, and sqrt decomposition.
- Competitive-programming patterns if you enjoy them, but do not confuse speed with engineering.
