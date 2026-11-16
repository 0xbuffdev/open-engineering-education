# SEF4 — Data Structures & Algorithms

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** [SEF11](SEF11.md)
**Duration:** 12–14 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–15 focused hours/week (provisional; calibrate with learner evidence)

> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Learn to select, implement, test, and explain core data structures and algorithms. Build linear containers, linked lists, search trees, and graph traversals; compare sorting and search procedures; reason about invariants, asymptotic and amortized cost, heap-based scheduling, shortest paths, dependency graphs, and dynamic programming. The emphasis is on **demonstrated correctness and an honest analysis of trade-offs**, not a collection of completed coding exercises.

Python 3.11 or later and its standard library are the reference environment. All required work can be completed offline in a learner-controlled, nonprivileged environment without purchased material, private grading software or network access. Learners may use `unittest`, `collections`, `random`, `timeit`, and other standard-library tools for fixtures, oracles, and measurements. Built-in `sorted` and `heapq` may be used as *independent references* but cannot replace an algorithm that the assessment explicitly asks the learner to implement. Record the actual interpreter version, platform, test commands, deterministic seeds, and performance-measurement limitations.

The original eight topic areas remain intact, but the course now begins with an **explicit mathematics-to-algorithm bridge** and teaches complete correctness and cost arguments before the most proof-intensive searching and sorting applications. Nine instructional modules form the revised sequence. The existing **seven required summative assessments** still cover the independently important capabilities and may **reuse the same tested implementations** as a small portfolio and integrated tool. No universal module quiz/lab pair or extra final lab is required. An explicit, separately reviewable assessment decision—rather than a lesson count or passing screenshot—establishes each required outcome.

Foundational discrete mathematics is assessed in [SEF11](SEF11.md) before this course: logic, sets, functions, counting, elementary proofs and induction, graph mathematics, asymptotic notation and recurrences. SEF4 applies and deepens those capabilities through implemented algorithms; it does not silently assume simultaneous mathematical study is equivalent to demonstrated readiness. Python programming competence from SEF2 is inherited through SEF11.

The revised 12–14-week duration and expected 10–15 focused hours per week are planning estimates pending learner calibration, not evidence that every beginner can complete this material on that schedule. This course remains `draft` until the evidence for a higher course-readiness label is reviewed.

### Transfer of SEF11 mathematical readiness to SEF4

The following is a **teaching and evidence crosswalk**, not an extra entry examination or a new completion requirement. Each SEF11 capability is already assessed through the SEF11 prerequisite. SEF4 demands its *application to implemented algorithms* through the existing seven SEF4 assessments.

| Prerequisite evidence in SEF11 | First applied teaching in SEF4 | Existing required SEF4 evidence |
| --- | --- | --- |
| [Logic, quantifiers and proof](SEF11.md) (`SEF11-O3`, `SEF11-O6`; `SEF11-AS2`, `SEF11-AS4`) | Preconditions, postconditions, loop invariants, initialization, preservation, exit and decreasing termination measures | `SEF4-O5`, `SEF4-O7`; lower-bound search proof in `SEF4-AS3` |
| Functions, sets and relations (`SEF11-O2`, `SEF11-O4`; `SEF11-AS2`) | Declared domains, duplicate policies, data-structure invariants and dependency orderings | `SEF4-O1`, `SEF4-O3`, `SEF4-O10`; `SEF4-AS1`, `SEF4-AS2`, `SEF4-AS5` |
| Growth and recurrences (`SEF11-O7`; `SEF11-AS5`) | Cost models, recursion trees, asymptotic witnesses, amortized growth and worst/expected-case assumptions | `SEF4-O2`, `SEF4-O6`, `SEF4-O7`; `SEF4-AS1`, `SEF4-AS3`, `SEF4-AS4`, `SEF4-AS6` |
| Finite graphs and state reasoning (`SEF11-O8`; `SEF11-AS5`) | Visited-set invariants, reachable vertices, nonnegative weighted paths and DAG constraints | `SEF4-O4`, `SEF4-O9`, `SEF4-O10`; `SEF4-AS2`, `SEF4-AS5` |
| Independent checking and counterexamples (`SEF11-O9`, `SEF11-O10`; `SEF11-AS5`, `SEF11-AS6`) | Model-based and exhaustive small-case oracles, metamorphic properties, unfamiliar reviewer changes and limits of bounded testing | `SEF4-O12`, `SEF4-O14`; existing `SEF4-AS1`–`SEF4-AS7` evidence |

A **proof** addresses all inputs satisfying declared assumptions; a finite oracle or benchmark is evidence only for the cases it actually checks. Teaching may use the same examples and extend or reuse already-reviewed work, without repeating SEF11's summative mathematics submissions. The prerequisite is [SEF11](SEF11.md), not concurrent enrollment in SEF8. For an optional public academic comparison, [MIT OpenCourseWare 6.006](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/pages/syllabus/) similarly pairs programming and discrete mathematics with correctness explanations and complexity analysis; it is not a paid textbook or an OEE assessment requirement.

## Learning outcomes

- **SEF4-O1:** Implement and verify stack, queue, and linked-list interfaces with stated operation behavior, empty-input handling, and representation invariants; choose a suitable container for a given workload.
- **SEF4-O2:** Explain and justify array-resizing amortized costs and the expected versus worst-case behavior of hashing, including collision and load-factor assumptions.
- **SEF4-O3:** Build and reason about recursive algorithms and binary search trees, including termination, structural invariants, and space used by a recursive call stack.
- **SEF4-O4:** Represent and traverse finite directed graphs using breadth-first and depth-first search, accounting for cycles, disconnected vertices, deterministic neighbor order, and complexity.
- **SEF4-O5:** Implement lower-bound binary search with explicit preconditions, a maintained interval invariant, a terminating update rule, and independently checked boundary behavior.
- **SEF4-O6:** Implement and compare merge sort and quicksort under declared pivot, stability, input-distribution, time and auxiliary-space assumptions.
- **SEF4-O7:** Analyze algorithm correctness and resource use with invariants, recurrence reasoning, worst/expected/amortized bounds, and measurements distinguished from asymptotic proof.
- **SEF4-O8:** Implement a binary heap and priority queue with correct parent/child invariants, deterministic ties, and explicit handling of empty and stale-event cases.
- **SEF4-O9:** Compute and reconstruct shortest paths on nonnegative weighted graphs, detect unreachable vertices, and reject invalid negative-weight assumptions.
- **SEF4-O10:** Produce a valid topological order for a directed acyclic dependency graph and detect and explain cycles rather than inventing an order.
- **SEF4-O11:** Compare greedy, exhaustive/backtracking, and dynamic-programming approaches using a counterexample, a correct state transition, and time/space reasoning.
- **SEF4-O12:** Design independent test oracles and deterministic fixtures for algorithms and data structures, including invalid, edge, mutation, and adversarial cases.
- **SEF4-O13:** Choose and combine suitable structures and algorithms in a reproducible small application, explaining their interfaces, constraints, and trade-offs.
- **SEF4-O14:** Defend an algorithmic claim using reproducible source, a correctness argument, failure and repair evidence, and carefully controlled performance observations.

## Modules

### Module 1 — Mathematical Reasoning for Executable Algorithms

#### Outcomes

- SEF4-O5
- SEF4-O7
- SEF4-O12
- SEF4-O14

#### Lessons

1. **From SEF11 to algorithm claims** — Translate a finite mathematical domain, relation or predicate into an input/output contract; check the exact assumptions of a claimed algorithm, not merely its sample output.
2. **Preconditions and postconditions** — Write quantified requirements for empty, singleton, duplicate, invalid and ordered input; produce a counterexample when a precondition is missing.
3. **Proof of a loop** — Separate invariant initialization, preservation, termination variant and postcondition at exit; trace a half-open interval on a small lower-bound search without treating the trace as the proof.
4. **Proof of recursion** — Relate base cases and strictly smaller subproblems to induction, termination and resource use, including a recursion-depth limit in a concrete Python implementation.
5. **Cost model and input size** — Choose the operations to count and explain the effect of input representation, Python built-in operation assumptions, graph vertices/edges and numeric encoding.
6. **Recurrences in running programs** — Obtain a recurrence from recursive source, state its base case and solve a simple expansion or recursion tree with a justified asymptotic bound.
7. **Worst, expected and amortized are different** — Distinguish worst input from input distributions, randomized pivot assumptions, geometric resizing and a single costly operation.
8. **Independent oracles and falsification** — Design a different small reference algorithm or hand-derived expected set; explain when a shared helper would make two implementations fail together.
9. **Proof, test and benchmark boundaries** — Compare a logical correctness argument, an exhaustive *finite* check, a seeded randomized test and a finite timing experiment, stating what each can and cannot establish.
10. **Unfamiliar-variation diagnosis** — Review a flawed proof with an unstated sorted-input assumption or nondecreasing termination measure; propose the minimal correction and appropriate regression evidence.

*Optional practice:* State and check the three parts of an invariant proof for lower-bound binary search on a small sorted sequence, then identify a new input that breaks an intentionally weakened hypothesis. This is mathematical transfer practice, **not** an extra compulsory assessment.

### Module 2 — Data Organization

#### Outcomes

- SEF4-O1
- SEF4-O2
- SEF4-O7
- SEF4-O12

#### Lessons

1. Course introduction: Data Structures & Algorithms
2. Arrays and lists
3. Linked lists
4. Stacks
5. Queues and deques
6. Maps and hash tables
7. Sets
8. Capacity, resizing, and amortized array append
9. Hash collisions, probing, and load factors
10. Invariants and mutation edge cases
11. **Model-based operation sequences** — Derive expected stack/queue/list state from a reference model and identify whether a copied implementation shares a defect.
12. **Growth arguments with explicit assumptions** — Compare geometric resizing with one expensive append, and a hash-table collision case with a justified expected-case model.

*Optional practice:* Compare a Python list-backed stack, a deque-backed FIFO queue, and a simple linked-list node model; trace one invalid removal and a collision-heavy lookup with explicit assumptions.

### Module 3 — Trees, Graphs & Recursion

#### Outcomes

- SEF4-O3
- SEF4-O4
- SEF4-O12

#### Lessons

1. Recursion
2. Trees
3. Tree traversal
4. Binary search trees
5. Graphs
6. Breadth-first search
7. Depth-first search
8. Recursive termination, stack depth, and memory
9. Adjacency lists, adjacency matrices, and disconnected graphs
10. Cycle detection and traversal correctness
11. **Traversal proof obligations** — Explain visited-set preservation, reachability coverage, termination and why BFS level distances require a FIFO queue.
12. **BST performance claims** — Separate tree height and degeneration from the behavior of a balanced search tree that the course does not require learners to implement.

*Optional practice:* Trace recursive call frames on a small tree and compare BFS/DFS visit order for a cycle and an unreachable vertex.

### Module 4 — Algorithm Correctness & Cost Arguments

#### Outcomes

- SEF4-O5
- SEF4-O7
- SEF4-O12
- SEF4-O14

#### Lessons

1. **Formal contracts** — State finite input domains, sortedness, edge-weight and mutation assumptions without hiding preconditions in test code.
2. **Loop proof obligations** — Show initialization, preservation and how exit plus the invariant establishes the postcondition.
3. **Termination measures** — Select a natural-valued variant that strictly decreases, and reject a wrong update that can make no progress.
4. **Recursive correctness** — Establish base cases and justify the induction hypothesis on strictly smaller arguments.
5. **Recurrences and recursion trees** — Derive a recurrence from actual work and split behavior, identify the base case and solve a representative bound.
6. **Worst, expected and amortized costs** — Identify the quantified claim and the distribution or resizing policy that licenses it; separate average over input samples from a proved expectation.
7. **Auxiliary space and recursion depth** — Include stack frames, graph representation and temporary buffers in a bounded resource claim.
8. **Algorithm-specific proof sketches** — Adapt the general method to binary search, heap order, BFS reachability and greedy/DP counterexamples.
9. **Independent falsification** — Identify a shared-oracle mistake, biased generator or benchmark that appears to prove a false claim; repair the checking approach.

*Optional practice:* Write a half-open-interval invariant for lower-bound search; repair an intentionally faulty boundary update on an empty or duplicate-heavy input.

### Module 5 — Searching, Sorting & Complexity

#### Outcomes

- SEF4-O5
- SEF4-O6
- SEF4-O7

#### Lessons

1. Counting operations
2. Big-O notation
3. Linear search
4. Binary search
5. Merge sort
6. Quicksort
7. Comparing sorts
8. Best-, average-, and worst-case analysis
9. Sorting stability and input-sensitive cost
10. Space/time trade-offs and fair benchmarking
11. **Lower-bound search variants** — Derive interval-preservation and strictly shrinking bounds for the first index at least a target, with empty and duplicate-heavy inputs.
12. **Stable sorting evidence** — Use labeled equal-key records to distinguish a stable algorithm from correct key order alone and from a promise unsupported by the actual quicksort code.

*Optional practice:* Compare linear and binary search on sorted input; contrast the behavior of two sorts on repeated keys and input that is already ordered.

### Module 6 — Heaps & Priority Queues

#### Outcomes

- SEF4-O8
- SEF4-O7
- SEF4-O12

#### Lessons

1. Array representation of a complete binary tree
2. Heap insert, sift, extract, and heapify
3. Priority queue contracts, tie-breaking, and complexity
4. Heapsort and scheduling applications
5. **Heap invariant and repair reasoning** — Trace sift-up/sift-down before and after a mutation, including empty state and deterministic tie-breaking.
6. **Bottom-up heapify cost** — Explain why only counting the height of the root gives an unjustified `O(n log n)` upper bound but a height-sum argument gives `O(n)` for heap construction.

*Optional practice:* Draw the zero-indexed heap parent/child relationships and compare successive inserts against bottom-up heap construction.

### Module 7 — Weighted Graphs & Dependencies

#### Outcomes

- SEF4-O4
- SEF4-O9
- SEF4-O10
- SEF4-O12

#### Lessons

1. Directed, undirected and weighted graphs
2. Reachability and graph components
3. Shortest paths with BFS for unweighted graphs
4. Dijkstra algorithm and nonnegative weights
5. Topological ordering of a directed acyclic graph
6. Cycle detection and unreachable nodes
7. **Shortest-path justification** — Explain why the settled-distance argument depends on nonnegative weights, and how a small Bellman–Ford reference provides an independent check.
8. **Topological order proof obligations** — Link prerequisite direction to edge constraints, justify cycle detection and distinguish one valid DAG order from the only possible order.

*Optional practice:* Trace a shortest path and a dependency graph by hand; change an edge to introduce an unreachable target or a cycle.

### Module 8 — Algorithm Design Strategies

#### Outcomes

- SEF4-O11
- SEF4-O7
- SEF4-O12

#### Lessons

1. Divide and conquer and recurrence structure
2. Greedy choices and counterexamples
3. Dynamic programming and memoization
4. Backtracking, pruning and search space
5. Algorithm selection from constraints
6. **Dynamic-programming invariants** — Explain valid states, base conditions, transitions and why a solved smaller subproblem supports an optimal larger result.
7. **Numeric encoding and pseudo-polynomial time** — Distinguish `O(target × denominations)` from a bound polynomial in the bit-length of a potentially large numeric target.

*Optional practice:* Show a failing greedy coin choice with denominations 1, 3, 4 and target 6; compare with an independently checked dynamic program.

### Module 9 — Algorithm Toolkit

#### Outcomes

- SEF4-O12
- SEF4-O13
- SEF4-O14

#### Lessons

1. Algorithm Toolkit boundaries and test oracles
2. Integrating dependency ordering with priority queues
3. Repeatable benchmarks and honest complexity claims
4. Clean-start documentation and engineering defense
5. **Capability-to-evidence crosswalk** — Locate the same existing assessments, independent oracle results, invariants and cost arguments without inventing duplicate mastery tasks.
6. **Unfamiliar algorithm claim** — Predict one new boundary input or changed contract before running it, then explain what the observed results mean and what remains unproved.

*Optional practice:* Sketch a dependency-aware scheduler and plan the tests, performance checks, documentation and technical defense before implementing it.

## Completion requirements

### How the existing assessments demonstrate mathematical transfer

This table **clarifies the evidence already required** in `SEF4-AS1`–`AS7`. It does not add a new rubric, submission, exam, prerequisite, or completion gate. The operative Work, Criteria and Evidence fields remain unchanged.

| Existing assessment | Correctness or mathematical argument already required | Independent checking already required |
| --- | --- | --- |
| `SEF4-AS1` | Stack/queue/link invariants; geometric-growth amortization and collision assumptions | Seeded operation sequences against independent list/deque models |
| `SEF4-AS2` | Recursive termination, BST ordering, visited-set reachability and BFS level behavior | Independently checked reachable sets, BFS levels and tree fixtures |
| `SEF4-AS3` | Lower-bound interval invariant and progress; sorting correctness, stability and qualified time/space costs | Linear-search and library-sort references, boundary cases and repeated timings |
| `SEF4-AS4` | Heap order, tie policy, sift and bottom-up heapify bounds | Deterministic independent sorted extraction model |
| `SEF4-AS5` | Nonnegative-weight shortest paths and dependency precedence on acyclic graphs | Bellman–Ford or equivalent small reference and edge-validated DAG ordering |
| `SEF4-AS6` | Counterexample disproving general greedy optimality, valid DP state recurrence and target-size cost | Exhaustive or BFS small-target reference on unfamiliar coin systems |
| `SEF4-AS7` | Algorithm selection, resource trade-offs and integrated dependency/priority contract | Reused capability-to-evidence matrix and independently checked integrated workflow |

### Assessment setup and evidence

Use Python 3.11 or later, its standard library, synthetic datasets, and a learner-controlled local repository or portable source tree. Provide a clean-start README, exact test commands, deterministic random seeds when generating fixtures, version/environment notes, inspectable inputs and actual observed results. Tests should use an independent expected-value source, small exhaustive oracle, reference implementation, hand-derived case, or stated invariant that does not simply re-run the implementation under review.

For each required assessment, preserve the source revision, declared interface and assumptions, normal and edge/invalid cases, an investigated failure or counterexample as applicable, and a concise explanation of why the evidence meets the published criteria. For benchmarks, retain raw repeated timings, inputs and machine/interpreter notes, summarize variability, and explain that finite measurements do **not** prove asymptotic complexity. All reasoning and technical defenses can be reviewed in an accessible written, recorded, live or other equivalent form.

A learner cannot pass a required assessment with an uncorrected invariant violation, incorrect output on a required case, unsupported complexity claim, or unreproducible evidence. The reviewer may introduce equivalent unfamiliar fixtures under the published criteria. Reuse earlier assessed source and evidence wherever appropriate; the purpose is competency, not duplicate implementations or mandatory extra tests per module.

### Required summative assessments

- **SEF4-AS1** (required linear structures, interfaces, and amortized analysis)
  - Outcomes: SEF4-O1, SEF4-O2, SEF4-O7, SEF4-O12
  - Work: Implement a stack, FIFO queue, and singly linked list with documented insertion, removal, observation, and empty-container behavior. State and assert their order, node-link and size invariants, and test mutation boundaries with seeded sequences against separate Python list or deque reference models. Compare a dynamically resized array's worst single append with amortized append under geometric growth, and analyze hash-table lookup with ordinary keys and deliberately colliding keys, including the assumptions needed for expected constant-time behavior. The hash study may use a small instrumented collision model rather than a production hash-table reimplementation.
  - Criteria: Operations preserve LIFO/FIFO order, linked-list connectivity and accurate counts; empty removal follows the documented error/return contract; repeated values and one-element transitions are correct. Independent model tests expose a seeded defect or counterexample. The learner distinguishes amortized from worst-case append cost and expected from pathological hash lookup, stating resize, collision and load-factor assumptions without inferring complexity from timing alone.
  - Evidence: Source and interface contracts, container invariant statements, seeded operation fixtures and oracle output, reproducible boundary/invalid tests, a specific defect and correction, collision example, and a short amortized-cost explanation.

- **SEF4-AS2** (required recursion, trees, and cycle-safe traversal)
  - Outcomes: SEF4-O3, SEF4-O4, SEF4-O7, SEF4-O12
  - Work: Implement a binary search tree with insert and lookup under a documented duplicate-key policy, and trace a recursive search or traversal with its base case, invariant and stack-depth limit. Represent directed graphs using adjacency lists and implement BFS and DFS with a visited policy and explicit neighbor iteration order; an iterative DFS may replace recursive graph traversal. Use known small graphs with cycles, disconnected components, self-loops and unreachable vertices. Compare the two traversals' results against independently derived reachable sets and BFS levels.
  - Criteria: BST shape and key-order invariants hold after every insertion; duplicate and missing-key behavior follows the policy. The recursion terminates for all required finite inputs and its depth/space claims match the chosen implementation. BFS and DFS visit each reachable vertex exactly once, terminate on cycles, and exclude unreachable vertices in a single-source traversal; expected order is asserted only with a specified neighbor order. The learner distinguishes adjacency-list and matrix storage complexity under stated graph assumptions.
  - Evidence: BST and graph source, diagrams or traces of recursive calls and a sample traversal, fixtures with independently checked reachability/levels, boundary and negative tests, a corrected traversal or tree defect, and a complexity note for recursion and graph representation.

- **SEF4-AS3** (required searching, sorting, proof, and benchmarking)
  - Outcomes: SEF4-O5, SEF4-O6, SEF4-O7, SEF4-O12, SEF4-O14
  - Work: Implement lower-bound binary search on sorted input, returning the first index whose element is at least the target or the sequence length when absent. State an invariant for its half-open search interval, branch preservation, and termination. Implement merge sort and quicksort without calling a library sort inside either algorithm; state the chosen pivot strategy, whether each version is stable, and its worst/expected time and auxiliary-space assumptions. Test empty, singleton, sorted, reverse-sorted, duplicate-heavy and seeded random arrays against an independent linear-search oracle and `sorted`; verify that the output multiset is unchanged. Deliberately inject and repair an off-by-one defect. Benchmark both sorts on at least three increasing input sizes and at least two different input shapes using repeat trials.
  - Criteria: Every tested lower-bound result satisfies the partition property and independent reference index; the invariant is preserved and the interval shrinks. Sorting outputs agree with the reference and preserve the input multiset; stability claims reflect the actual implementation, not the algorithm name alone. The learner correctly distinguishes merge sort's standard `O(n log n)` worst-case from quicksort's possible `O(n²)` worst case and discusses measured data, variance, recursion depth, memory and pivot policy without using timing as a proof.
  - Evidence: Source, loop-invariant and termination argument, counterexample and repaired regression, test fixtures and oracle comparisons, raw and summarized timings with environment/seed details, and a correctness/cost explanation tied to the implementations.

- **SEF4-AS4** (required binary heap and deterministic priority scheduling)
  - Outcomes: SEF4-O2, SEF4-O7, SEF4-O8, SEF4-O12
  - Work: Implement a binary min-heap with insert, peek, extract and a bottom-up heapify operation, and wrap it in a priority queue of `(priority, sequence, task_id)` records for deterministic ties. Define an empty-queue contract. If the queue supports cancellation or rescheduling, implement stale-entry invalidation; otherwise explicitly reject unsupported operations without silently executing an obsolete record. Exercise repeated priorities, negative values, empty/one-item cases and seeded operation sequences, comparing extraction order with an independently sorted reference model. Reproduce and repair a faulty sift or stale-entry defect.
  - Criteria: All in-range parent and child indices satisfy the min-heap invariant after mutation, extracted priorities never decrease, ties follow the declared sequence order, and invalid or stale records never execute unnoticed. The learner explains the `O(log n)` insert/extract bounds and bottom-up `O(n)` heapify under standard assumptions, distinguishing these bounds from measured times. The independent model and negative tests detect the seeded defect and pass after correction.
  - Evidence: Source, invariant checks and a trace of an inserted/extracted record, deterministic reference-model tests and boundary cases, failure/fix record, documented tie/cancellation policy, and cost analysis.

- **SEF4-AS5** (required weighted routing and dependency validation)
  - Outcomes: SEF4-O4, SEF4-O7, SEF4-O8, SEF4-O9, SEF4-O10, SEF4-O12
  - Work: Using a priority queue, implement Dijkstra shortest paths for nonnegative-weight directed graphs, with an explicit invalid-negative-edge policy, unreachable-vertex behavior, and path reconstruction from a selected source. Separately implement topological ordering for directed prerequisite edges (prerequisite before dependent), returning a clear cycle error instead of a partial success. Test zero weights, equal distances, parallel edges, isolated and unreachable nodes, disconnected graphs, empty input, and at least one deliberate cycle. Compare distances against an independent small-graph reference (for example Bellman–Ford on nonnegative fixtures) and check every returned topological order against all precedence edges.
  - Criteria: Every reported path is a valid route whose summed weights equal the reported distance; shortest distances agree with the independent oracle, and unreachable targets are explicitly distinguished from zero-length paths. Negative edges are rejected before claiming Dijkstra's guarantee. A valid DAG order honors every edge, and cycles produce a detectable failure rather than an invented schedule. Performance claims are qualified by heap choice, graph representation and input assumptions.
  - Evidence: Code, labeled fixture graphs, reference distances, reconstructed path checks, cycle and negative-edge failures, deterministically tested order constraints, a diagnosed defect or incorrect assumption, and a justified routing/dependency complexity analysis.

- **SEF4-AS6** (required algorithm-design strategy and counterexample)
  - Outcomes: SEF4-O7, SEF4-O11, SEF4-O12, SEF4-O14
  - Work: For the unbounded minimum-coin problem with positive denominations, implement largest-first greedy selection, a dynamic program with an explicit state, transition, base and unreachable cases, and an independent small-target exhaustive or breadth-first oracle. Show why denominations `{1,3,4}` and target `6` refute greedy optimality (three greedy coins versus two optimal coins). Compare the approaches for empty/invalid denominations, target zero, unreachable targets when coin `1` is absent, and several additional deterministic coin systems. Explain when a greedy correctness proof would be necessary and relate dynamic-programming complexity to target size and number of denominations.
  - Criteria: The documented counterexample is reproduced; the DP agrees with the independent oracle on the required valid cases; invalid, zero-target and unreachable behavior follows a clear contract. The learner states why local greedy choices do not guarantee global optimality for arbitrary denominations and explains the DP recurrence, termination and `O(target × denominations)` time with `O(target)` space for the described tabulation. Independent test results and a diagnosed failure or counterexample support the claim.
  - Evidence: Greedy, DP and oracle code, the hand-worked counterexample, input validation and unreachable policy, deterministic cross-checks, state/transition explanation, failure/correction account and time/space reasoning.

- **SEF4-AS7** (required integrated algorithm toolkit and engineering defense)
  - Outcomes: SEF4-O1, SEF4-O3, SEF4-O4, SEF4-O5, SEF4-O6, SEF4-O8, SEF4-O9, SEF4-O10, SEF4-O11, SEF4-O12, SEF4-O13, SEF4-O14
  - Work: Assemble the assessed stack, queue, linked list, BST, BFS/DFS, lower-bound search, merge sort, quicksort, binary heap, nonnegative shortest-path, topological-order, and dynamic-programming implementations into a documented toolkit. A learner may reuse the exact already-assessed implementations and test artifacts from SEF4-AS1–AS6. Build one small task-oriented application; for example, a dependency-aware work planner that uses topological ordering to reject cycles and a priority queue to select eligible tasks, while preventing premature execution of blocked tasks. Document interfaces, invalid cases, ordering and priority policy, and test a complete workflow against a separate expected-result fixture. Compare at least two algorithmic choices using existing reproducible benchmark evidence. Diagnose one integration or specification defect and present a reviewable technical defense of correctness, complexity, limits and design trade-offs.
  - Criteria: The toolkit exposes usable, documented interfaces and independent regression tests for each required capability; an integrated task workflow honors dependency constraints, selected priority policy, repeatable execution and explicit error behavior. No uncovered core capability is assumed correct solely from integration output. The learner can demonstrate a clean setup, explain why the selected structures fit the task, and defend an unfamiliar boundary or failure case against published criteria. Reused assessments satisfy requirements without extra unrelated projects or duplicative benchmark submissions.
  - Evidence: Versioned or portable source, clean-start README and exact commands, capability-to-test/evidence matrix, reference fixtures and observed integration outputs, normal/boundary/negative test logs, measured trade-off summary with limitations, an investigated failure and correction, and an accessible technical defense.

### Completion decision

A learner completes SEF4 only when **all seven required assessments** satisfy their published criteria and collectively demonstrate SEF4-O1 through SEF4-O14. Early assessment artifacts may be revised and reused in the integrated toolkit; learners are not required to submit seven unrelated projects, pass a quiz/lab pair in every module, or reimplement previously verified data structures solely for the final evaluation. Extra drills, sample algorithms and practice checkpoints are formative work, not hidden summative gates.

Reviewers must record their assessment decisions and the evidence that substantiates them. Where an unfamiliar input exposes an unmet requirement, the implementation or explanation must be corrected and reassessed; a passing benchmark alone cannot override a failed correctness check. A defense may be written, recorded, live or otherwise accessible while evaluating the same published outcomes. The course remains `draft`; structural checker success never makes the course `tested` or `verified`. See [Status Labels](../../spec/status-labels.md) for the distinct educational-readiness rules.

### Revision record: mathematical alignment without changing required contracts

This course-level academic hardening implements the SEF4 follow-up in [accepted RFC 0003](../../rfcs/0003-sef-academic-progression.md). The historical version is [SEF4 at OEE commit `c66ccd3da563fb308dd46a7ce6513d2145490040`](https://github.com/0xbuffdev/open-engineering-education/blob/c66ccd3da563fb308dd46a7ce6513d2145490040/curriculum/SEF/SEF4.md). **All fourteen `SEF4-O1`–`O14` descriptions and all seven `SEF4-AS1`–`AS7` assessment definitions (including Work, Criteria, Evidence and reviewer variations) are retained exactly.** No outcome or assessment ID is replaced, reinterpreted or added, because the existing seven assessments already measure the required proof, performance and oracle competencies.

The change introduces one explicit introductory mathematical-transfer module, reorders existing analysis before proof-intensive searching and sorting, expands formative lesson guidance, and publishes an explanatory prerequisite/evidence crosswalk. The provisional duration changes from 10 to 12–14 weeks, to be calibrated against actual learner work. This is a teaching-sequence revision, **not a new completion contract or automatic reassessment** of historical learner evidence. The prerequisites remain SEF11, with prior SEF2 programming competence transitively established; the SEF6 and SEF10 downstream course contracts are unchanged. No paid resource, advanced library, global OEE spec rule or status promotion is introduced.
