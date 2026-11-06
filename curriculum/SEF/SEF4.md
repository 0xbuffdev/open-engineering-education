# SEF4 — Data Structures & Algorithms

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** [SEF2](SEF2.md)
**Duration:** 10 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

This course develops core data structures and algorithms through implementation, correctness arguments and measured behavior. Learners build linear containers, hash maps, trees, heaps and graph algorithms; analyze recursion, search, sorting, dynamic programming and greedy counterexamples; and defend implementation choices with independently reproducible tests and evidence.

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
   - Binary heap and priority queue
   - Dijkstra shortest path with nonnegative weights
   - Topological ordering with cycle detection
   - A dynamic-programming optimization exercise

   Then integrate two structures in a runnable task-oriented tool, benchmark selected operations and justify correctness and complexity with evidence from the completion requirements.

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

**Required assessment and laboratory contract:**

The following checkpoints and labs are mandatory for SEF4. Every checkpoint question is a worked review prompt with the expected reasoning described below. Reviewers may use equivalent unfamiliar questions testing the same outcome, but must retain the acceptance criteria. A learner must correctly explain **all critical invariants, algorithm assumptions and correctness conditions** for each checkpoint; partial terminology recall alone does not pass. Incorrect answers are remediated and reassessed before course completion.

**Shared laboratory environment:**

Use Python 3.11 or later and its standard library on a local nonprivileged environment. Record the exact Python version and operating system; use `python3 -m unittest discover -s tests -v` as the default automated test command, or document an equivalent reproducible command. Use fixed seeds for generated cases, and never depend on a paid service.

**Shared evaluation rules:**

- Checkpoint acceptance: answer both questions in each module with the stated result and a defensible explanation; demonstrate the relevant algorithm or mathematical invariant when applicable.
- Lab acceptance: meet the module's expected behavior, produce passing normal and boundary tests, reproduce a negative/failure case, and submit the required evidence.
- Reviewer process: identify the submitted commit and commands, reproduce tests independently, compare expected and observed results, and record outstanding limitations.
- Evidence per module: source/fixture versions, executed commands, actual outputs, tests, reasoning, an investigated failure and its repair. Include input sizes, repetitions and variance for any benchmark.
- Failing a required invariant or safety assumption blocks completion of that module regardless of passing unrelated tests.

**Module 1 — Data Organization: checkpoint** — Required assessment details

- **Q1 (free):** A dynamically resized array doubles its capacity when full. Explain the worst-case cost of a single append and the amortized cost over n appends.
  - Expected answer and scoring: A resize copies O(n) items in the worst single append; geometric resizing yields O(1) amortized append over a sequence. A correctness argument must state the growth assumption.
- **Q2 (free):** For a hash table, what changes when all keys collide? Compare a hash map lookup with an unsorted list, and identify why an expected O(1) lookup is not a worst-case guarantee.
  - Expected answer and scoring: With pathological collisions, lookup can degrade to O(n); expected O(1) requires suitable distribution and load management. Unsorted-list search is O(n) worst case.

**Module 1 — Stack and queue costs: required lab** — Required assessment details

- **Objective:** Build and verify stack and FIFO queue behavior including their mutation and boundary contracts.
- **Prerequisites:** Complete this module's lessons, be able to explain the checkpoint answers and have a local Python environment ready.
- **Environment:** Use Python 3.11 or later and its standard library on a local nonprivileged environment. Record the exact Python version and operating system; use `python3 -m unittest discover -s tests -v` as the default automated test command, or document an equivalent reproducible command. Use fixed seeds for generated cases, and never depend on a paid service.
- **Procedure:**
  1. Implement a stack with push, pop and peek and a FIFO queue with enqueue, dequeue and peek using Python lists and/or collections.deque; document which backing implementation you chose.
  2. Create a small independent list-based reference model and verify 100 seeded operation sequences including repeated values.
  3. Test empty removal, one-element transition, alternating insert/remove and preservation of FIFO/LIFO order.
  4. Compare operation costs at increasing sizes; use a workload that exposes the difference between deque.popleft() and list.pop(0).
- **Expected result:** Every valid operation returns the reference-model value; documented empty-operation behavior is deterministic. The report distinguishes amortized array append, deque operations and list-front removal.
- **Verification:** Run unittest cases across seeded sequences and record comparison counts and repeated timing measurements; no claim about complexity follows from timing alone.
- **Evidence:** Source files, deterministic input fixtures, test logs including failures and reruns, a reasoning trace, and relevant performance measurements.
- **Failure analysis:** Explain an observed empty-container error or ordering defect and show the failing seed before repair.
- **Acceptance:** All specified behavior and negative-path checks pass under the recorded environment; an independent reviewer can reproduce the evidence. Any unresolved limitation must be disclosed, and an unmet required behavior fails the lab.

**Module 2 — Trees, Graphs & Recursion: checkpoint** — Required assessment details

- **Q1 (free):** Traverse adjacency list A:[B,C], B:[D], C:[D], D:[] using BFS and DFS. State a valid BFS order and why a visited set is necessary.
  - Expected answer and scoring: For the given neighbor order, BFS A,B,C,D; recursive preorder DFS A,B,D,C. A visited set prevents processing D twice and prevents infinite traversal on cycles. Other DFS orders require explicit neighbor ordering.
- **Q2 (free):** Explain the space implications of depth-first recursion on a chain of n nodes and compare adjacency-list and adjacency-matrix storage.
  - Expected answer and scoring: Recursive DFS may use O(n) call-stack space on a chain; adjacency list O(V+E) versus matrix O(V^2), under standard representations.

**Module 2 — Traverse a graph: required lab** — Required assessment details

- **Objective:** Implement cycle-safe BFS and DFS on arbitrary finite directed graphs.
- **Prerequisites:** Complete this module's lessons, be able to explain the checkpoint answers and have a local Python environment ready.
- **Environment:** Use Python 3.11 or later and its standard library on a local nonprivileged environment. Record the exact Python version and operating system; use `python3 -m unittest discover -s tests -v` as the default automated test command, or document an equivalent reproducible command. Use fixed seeds for generated cases, and never depend on a paid service.
- **Procedure:**
  1. Represent directed graphs with adjacency lists; document whether neighbors retain insertion order.
  2. Implement BFS and DFS with an explicit visited policy and return visitation orders.
  3. Test empty graphs, single vertices, cycles A→B→C→A, unreachable vertices and disconnected components.
  4. Compare outputs with hand-calculated traversal orders for a fixed adjacency order; demonstrate recursion-depth limitations or use iterative DFS.
- **Expected result:** Every reachable vertex is visited once and no unreachable vertex is included in a single-source traversal. Cycles terminate.
- **Verification:** Compare BFS levels to independently computed expected distances; verify set of reached vertices and no duplicate visits for each fixture.
- **Evidence:** Source files, deterministic input fixtures, test logs including failures and reruns, a reasoning trace, and relevant performance measurements.
- **Failure analysis:** Reproduce a recursive infinite traversal or duplicate-visit bug and document the correction.
- **Acceptance:** All specified behavior and negative-path checks pass under the recorded environment; an independent reviewer can reproduce the evidence. Any unresolved limitation must be disclosed, and an unmet required behavior fails the lab.

**Module 3 — Searching, Sorting & Complexity: checkpoint** — Required assessment details

- **Q1 (free):** Why does binary search require a sorted sequence? Analyze its worst-case comparison count for n elements.
  - Expected answer and scoring: The elimination rule depends on sorted order; comparison count grows O(log n) for n≥1, versus O(n) linear search. Discuss empty input separately.
- **Q2 (free):** Are merge sort and quicksort both always O(n log n) in the worst case? Explain sorting stability and auxiliary-space assumptions.
  - Expected answer and scoring: Standard merge sort O(n log n) worst-case with O(n) auxiliary space for arrays and stable when implemented accordingly. Typical in-place quicksort has O(n^2) worst-case and is generally unstable; expected cost depends on pivot strategy.

**Module 3 — Benchmark two sorts: required lab** — Required assessment details

- **Objective:** Compare correctness and performance of merge sort and quicksort without confusing experimental results with mathematical bounds.
- **Prerequisites:** Complete this module's lessons, be able to explain the checkpoint answers and have a local Python environment ready.
- **Environment:** Use Python 3.11 or later and its standard library on a local nonprivileged environment. Record the exact Python version and operating system; use `python3 -m unittest discover -s tests -v` as the default automated test command, or document an equivalent reproducible command. Use fixed seeds for generated cases, and never depend on a paid service.
- **Procedure:**
  1. Implement both algorithms without using a library sort inside the algorithm; use built-in sorted only as an independent oracle.
  2. Test empty, singleton, sorted, reverse, duplicate-heavy and random lists; verify output and that the input multiset is unchanged.
  3. Use documented sizes (for example 100, 1,000 and 5,000) and a fixed random seed; repeat trials and record median plus variability.
  4. Discuss pivot policy, recursion depth, temporary memory and effects of different input shapes.
- **Expected result:** Both produce the same correctly sorted output for every fixture. The report states merge sort and quicksort bounds under the actual implementations.
- **Verification:** Automate correctness checks and retain per-run timing data; compare raw runs and summary statistics under a named Python runtime.
- **Evidence:** Source files, deterministic input fixtures, test logs including failures and reruns, a reasoning trace, and relevant performance measurements.
- **Failure analysis:** Explain a worst-case quicksort input or recursion failure, including why measuring only random input could hide it.
- **Acceptance:** All specified behavior and negative-path checks pass under the recorded environment; an independent reviewer can reproduce the evidence. Any unresolved limitation must be disclosed, and an unmet required behavior fails the lab.

**Module 4 — Algorithm Analysis & Correctness: checkpoint** — Required assessment details

- **Q1 (free):** State a valid loop invariant for lower-bound binary search over the half-open interval [lo, hi). Explain termination.
  - Expected answer and scoring: The sought insertion position remains within [lo,hi]; update lo=mid+1 if a[mid]<target else hi=mid, with mid=lo+(hi-lo)//2 and loop while lo<hi. Interval shrinks each iteration.
- **Q2 (free):** For T(n)=2T(n/2)+n on powers of two, derive a tight asymptotic upper/lower characterization and distinguish recursion-stack space.
  - Expected answer and scoring: T(n)=Θ(n log n) assuming constant base cost. The recursion depth is Θ(log n), while full working memory depends on implementation, such as whether arrays are copied.

**Module 4 — Verify binary-search invariants: required lab** — Required assessment details

- **Objective:** Prove and test a correct lower-bound implementation and expose a boundary defect.
- **Prerequisites:** Complete this module's lessons, be able to explain the checkpoint answers and have a local Python environment ready.
- **Environment:** Use Python 3.11 or later and its standard library on a local nonprivileged environment. Record the exact Python version and operating system; use `python3 -m unittest discover -s tests -v` as the default automated test command, or document an equivalent reproducible command. Use fixed seeds for generated cases, and never depend on a paid service.
- **Procedure:**
  1. Implement lower_bound returning the first index whose element is at least the target, or len(items) if none exists.
  2. State the interval invariant and explain how each branch preserves it and guarantees termination.
  3. Inject an off-by-one error into a separate demonstration version and capture a counterexample.
  4. Test empty arrays, duplicates, all-smaller, all-greater, singleton, negative values, and randomized sorted arrays against a simple linear oracle.
- **Expected result:** The result lies between 0 and len(items), elements before the index are smaller than target, and elements at/after the index are at least target.
- **Verification:** Check returned indices against the oracle and programmatically assert the partition property for each seeded input.
- **Evidence:** Source files, deterministic input fixtures, test logs including failures and reruns, a reasoning trace, and relevant performance measurements.
- **Failure analysis:** Document the failing boundary case, its invariant violation and the repaired test.
- **Acceptance:** All specified behavior and negative-path checks pass under the recorded environment; an independent reviewer can reproduce the evidence. Any unresolved limitation must be disclosed, and an unmet required behavior fails the lab.

**Module 5 — Heaps & Priority Queues: checkpoint** — Required assessment details

- **Q1 (free):** For a zero-indexed binary heap, state parent and child indices and the min-heap invariant.
  - Expected answer and scoring: For i>0 parent=(i−1)//2, children=2i+1 and 2i+2 when in range. Each parent priority is at most those of its children, with documented tie ordering.
- **Q2 (free):** Compare inserting n items individually with bottom-up heap construction. Include a cost bound.
  - Expected answer and scoring: Successive O(log n) insertion yields O(n log n) upper bound; bottom-up heapify is O(n) for a binary heap under standard assumptions.

**Module 5 — Build a priority-queue scheduler: required lab** — Required assessment details

- **Objective:** Implement correct scheduling with deterministic ties and stale/rescheduled event handling.
- **Prerequisites:** Complete this module's lessons, be able to explain the checkpoint answers and have a local Python environment ready.
- **Environment:** Use Python 3.11 or later and its standard library on a local nonprivileged environment. Record the exact Python version and operating system; use `python3 -m unittest discover -s tests -v` as the default automated test command, or document an equivalent reproducible command. Use fixed seeds for generated cases, and never depend on a paid service.
- **Procedure:**
  1. Implement a min-heap of (timestamp, sequence_number, task_id) records, with monotonically increasing sequence numbers for deterministic ties.
  2. Support enqueue, peek and extract; if rescheduling is implemented, invalidate stale records by version or remove/reinsert them safely.
  3. Exercise empty extraction, equal timestamps, cancellations/rescheduling, negative timestamps and hundreds of seeded operations.
  4. After each mutation, assert heap invariants and compare extracted events to a reference sorted sequence.
- **Expected result:** No earlier valid event is extracted after a later one; tie behavior is stable by insertion order; invalidated events never execute.
- **Verification:** Run independent model-based tests and verify the binary-heap invariant after every operation.
- **Evidence:** Source files, deterministic input fixtures, test logs including failures and reruns, a reasoning trace, and relevant performance measurements.
- **Failure analysis:** Reproduce and repair stale-event execution or incorrect sift-down/parent-index behavior.
- **Acceptance:** All specified behavior and negative-path checks pass under the recorded environment; an independent reviewer can reproduce the evidence. Any unresolved limitation must be disclosed, and an unmet required behavior fails the lab.

**Module 6 — Weighted Graphs & Dependencies: checkpoint** — Required assessment details

- **Q1 (free):** Can Dijkstra's algorithm correctly handle arbitrary negative-weight edges? How does BFS differ on weighted versus unweighted paths?
  - Expected answer and scoring: Standard Dijkstra requires nonnegative edge weights; BFS finds minimum hop count and shortest paths only for unweighted or equal-weight graphs.
- **Q2 (free):** For dependencies A→C, B→C and C→D, give a valid topological order and explain what happens if D→A is added.
  - Expected answer and scoring: A,B,C,D or B,A,C,D are valid when edges mean prerequisite precedes dependent. Adding D→A creates a cycle A→C→D→A; no topological ordering exists.

**Module 6 — Implement routing and dependency checks: required lab** — Required assessment details

- **Objective:** Produce shortest paths under documented nonnegative-weight assumptions and verify an acyclic dependency plan.
- **Prerequisites:** Complete this module's lessons, be able to explain the checkpoint answers and have a local Python environment ready.
- **Environment:** Use Python 3.11 or later and its standard library on a local nonprivileged environment. Record the exact Python version and operating system; use `python3 -m unittest discover -s tests -v` as the default automated test command, or document an equivalent reproducible command. Use fixed seeds for generated cases, and never depend on a paid service.
- **Procedure:**
  1. Implement Dijkstra with a binary heap and reject any negative edge; provide clear behavior for unreachable targets.
  2. Implement a topological ordering routine for a directed prerequisite graph and detect cycles.
  3. Test disconnected graphs, parallel edges, zero weights, equal shortest distances, empty graph and a deliberate cycle.
  4. Compare shortest routes against a small exhaustive-path or Bellman–Ford reference on tiny nonnegative graphs; compare topological output against every input precedence edge.
- **Expected result:** Distances and reconstructed paths agree with the oracle; unreachable vertices are identified; cycle detection rejects impossible schedules.
- **Verification:** Use deterministic fixtures and assert the weight of every returned path equals its reported minimum distance.
- **Evidence:** Source files, deterministic input fixtures, test logs including failures and reruns, a reasoning trace, and relevant performance measurements.
- **Failure analysis:** Explain an invalid negative-edge assumption, path reconstruction defect or cycle missed by a faulty visited policy.
- **Acceptance:** All specified behavior and negative-path checks pass under the recorded environment; an independent reviewer can reproduce the evidence. Any unresolved limitation must be disclosed, and an unmet required behavior fails the lab.

**Module 7 — Algorithm Design Strategies: checkpoint** — Required assessment details

- **Q1 (free):** For coin values {1,3,4} and target 6, show why selecting the largest available coin at each step is not optimal.
  - Expected answer and scoring: Greedy yields 4+1+1 (three coins); 3+3 uses two coins. This is a counterexample to greedy optimality for this coin system.
- **Q2 (free):** Define a dynamic-programming state and transition for the minimum-number-of-coins problem. State base and unreachable cases.
  - Expected answer and scoring: dp[0]=0; dp[t]=1+min(dp[t−c]) over allowed coins c≤t where predecessor reachable; no valid predecessor means unreachable. Target n cost O(nk) for k denominations with O(n) space.

**Module 7 — Disprove a greedy solution: required lab** — Required assessment details

- **Objective:** Implement an exact baseline and a dynamic program, then expose failure of a plausible greedy heuristic.
- **Prerequisites:** Complete this module's lessons, be able to explain the checkpoint answers and have a local Python environment ready.
- **Environment:** Use Python 3.11 or later and its standard library on a local nonprivileged environment. Record the exact Python version and operating system; use `python3 -m unittest discover -s tests -v` as the default automated test command, or document an equivalent reproducible command. Use fixed seeds for generated cases, and never depend on a paid service.
- **Procedure:**
  1. Implement greedy largest-first for coins [1,3,4], target 6 and state its result.
  2. Implement minimum-coin DP with input checks for positive denominations and nonnegative target.
  3. Implement exhaustive enumeration or BFS on small targets as a separate correctness oracle.
  4. Compare all approaches across small targets and randomized valid coin systems; describe how optimality and performance change.
- **Expected result:** Greedy returns three coins for target six, while DP and exhaustive oracle return two; all tested DP results match the independent oracle.
- **Verification:** Retain counterexamples, recurrence, boundary tests and repeated comparisons with the independent solver.
- **Evidence:** Source files, deterministic input fixtures, test logs including failures and reruns, a reasoning trace, and relevant performance measurements.
- **Failure analysis:** Explain an invalid recurrence, missing unreachable sentinel or negative/zero coin-value hazard.
- **Acceptance:** All specified behavior and negative-path checks pass under the recorded environment; an independent reviewer can reproduce the evidence. Any unresolved limitation must be disclosed, and an unmet required behavior fails the lab.

**Module 8 — Algorithm Toolkit: checkpoint** — Required assessment details

- **Q1 (free):** A solution passes happy-path tests but fails an empty-input case. Is its completion criterion met?
  - Expected answer and scoring: No. Required edge and invalid cases, invariants and integration evidence must be satisfied; explain and repair the defect.
- **Q2 (free):** Why can a benchmark not prove the asymptotic complexity class of an algorithm?
  - Expected answer and scoring: It measures finite workloads under specific conditions; a bound requires analysis of operations or formal reasoning under stated assumptions.

**Module 8 — Algorithm Toolkit: required lab** — Required assessment details

- **Objective:** Integrate and defend a reproducible algorithmic library plus a small application exercising its interfaces.
- **Prerequisites:** Complete this module's lessons, be able to explain the checkpoint answers and have a local Python environment ready.
- **Environment:** Use Python 3.11 or later and its standard library on a local nonprivileged environment. Record the exact Python version and operating system; use `python3 -m unittest discover -s tests -v` as the default automated test command, or document an equivalent reproducible command. Use fixed seeds for generated cases, and never depend on a paid service.
- **Procedure:**
  1. Implement stack, queue, linked list, BST, heap/priority queue, BFS, DFS, binary search, merge sort, quicksort, nonnegative weighted shortest path and topological ordering.
  2. Demonstrate at least one integrated tool: for example, a task planner whose dependencies use topological ordering and whose ready tasks use a priority queue.
  3. Retain unit tests for all structures and algorithms, reference-model/property-style tests for tricky invariants, and invalid-input/boundary fixtures.
  4. Run repeatable benchmarks on at least two relevant operations, identify the conditions and explain results against analytical expectations.
  5. Prepare a clean-checkout README with exact commands, a capability-to-evidence matrix and a technical retrospective documenting an investigated defect.
- **Expected result:** Required algorithms agree with independent oracles on tested fixtures; the integrated tool enforces dependency order and deterministic priorities; all stated invalid cases fail clearly.
- **Verification:** Reviewer can build/run/test from a fresh checkout; no required feature depends on hidden resources; every stated success criterion has an inspectable artifact.
- **Evidence:** Source files, deterministic input fixtures, test logs including failures and reruns, a reasoning trace, and relevant performance measurements.
- **Failure analysis:** Describe a real defect or incorrect complexity assumption, reproduction steps, resolution and evidence that the regression is prevented.
- **Acceptance:** All specified behavior and negative-path checks pass under the recorded environment; an independent reviewer can reproduce the evidence. Any unresolved limitation must be disclosed, and an unmet required behavior fails the lab.

**Exit demonstration:**

Given a new problem, the learner must:

- Choose an appropriate data structure
- Propose an algorithm
- Derive its complexity
- Explain why an obvious alternative approach is less suitable
