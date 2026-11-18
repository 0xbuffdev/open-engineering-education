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

The original competency areas remain intact, but the teaching sequence is now constructed around their dependencies: **one mathematical bridge to implementation and verification**, then concrete structures, recursive trees, searching/sorting, priority scheduling, graph algorithms, design strategies and integration. Correctness and cost methods are introduced once, then reapplied and independently checked where each algorithm demands them. The existing **seven required summative assessments** cover the independently important capabilities and may **reuse the same tested implementations** as a small portfolio and integrated tool. No universal module quiz/lab pair or extra final lab is required. An explicit, separately reviewable assessment decision—rather than a lesson count or passing screenshot—establishes each required outcome.

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

### Module 1 — From Mathematical Claims to Verified Algorithms

#### Outcomes

- SEF4-O5
- SEF4-O7
- SEF4-O12
- SEF4-O14

#### Lessons

1. **Course orientation and algorithmic responsibility** — Connect the history and practical uses of searching, sorting and data organization to executable procedures; explain why a plausible output or faster benchmark cannot establish correctness, and identify where SEF11 proof and SEF2 Python skills enter the course.
2. **Contracts, domains and representations** — Translate an unfamiliar problem into explicit input domains, preconditions, postconditions and representation assumptions; distinguish a mathematical sequence from a mutable Python collection and reject hidden sortedness requirements.
3. **Loop invariants and exit reasoning** — Identify initialization, preservation and the postcondition at exit for a loop using a bounded half-open interval; provide a counterexample when a claimed invariant is insufficient.
4. **Termination variants and recursion** — Identify a natural-valued termination variant and a strictly smaller recursive subproblem; distinguish mathematical termination from Python's finite recursion-depth limit.
5. **Algorithmic cost models** — Choose input-size parameters, counted operations and storage assumptions; explain why a Python slice, dictionary lookup or graph representation must not be treated as constant-time without a justified model.
6. **Recurrence and asymptotic proof** — Obtain a recurrence and base case from actual recursive work, justify a bound with expansion/induction and distinguish the witness for Big-O from finite timing evidence.
7. **Worst, expected and amortized reasoning** — State the quantifiers and assumptions for worst-case inputs, a genuine input/pivot distribution and a whole-operation-sequence amortized bound; separate these claims from measured averages.
8. **Independent oracles and test design** — Derive a small exhaustive or hand-checked reference, choose deterministic edge/adversarial cases and explain why two implementations sharing an incorrect helper are not independent checks.
9. **Evidence and falsification** — Distinguish proof of a general claim, exhaustive verification of a finite domain, randomized tests and repeatable benchmarks; diagnose one failed claim on an unfamiliar input and defend the minimal correction.

*Optional practice:* For a sorted sequence, hand-trace a lower-bound interval invariant and identify a case that refutes a broken update. The detailed implementation and assessment occur later in the course.

### Module 2 — Linear Containers, Linked Lists, Hashing and Growth

#### Outcomes

- SEF4-O1
- SEF4-O2
- SEF4-O7
- SEF4-O12

#### Lessons

1. **Select an interface from operations** — Specify required order, observation, insertion, removal and empty-state behavior for a stack, queue and linked list before choosing their representation.
2. **Arrays and indexed sequence costs** — Trace indexing, insertion, deletion and copying in a contiguous-array model; distinguish a Python list's useful semantics from a claimed universal time bound.
3. **Stacks and LIFO invariants** — Implement push, pop and peek under a published empty-container policy; validate operations against a separately built reference model.
4. **Queues, FIFO and deques** — Implement a queue with a justified O(1)-amortized or worst-case operation policy, avoiding repeated head removal from a Python list when it would impose a different cost.
5. **Singly linked nodes** — Implement insertion, removal and traversal with valid next-links, head/tail or size invariants and bounded behavior for empty, singleton and duplicate-element cases.
6. **Mutation and representation safety** — Diagnose a stale head, accidental shared node or size mismatch from seeded operation sequences, distinguishing equality of data from identity of a node.
7. **Geometric capacity and aggregate analysis** — Build a simple resizing model and derive the number of copied elements across a sequence, transferring SEF11's amortized proof to an implemented container rather than assuming a timing chart proves it.
8. **Hash tables and collisions** — Explain hash-to-bucket mapping, a collision strategy and lookup/insert behavior under an explicit load factor and hash distribution; use a small instrumented model rather than a production map rewrite.
9. **Expected versus pathological hashing** — Contrast expected constant-time under a stated distribution/resizing policy with deliberately colliding keys and a worst-case linear chain or probe sequence; do not promise constant-time access for adversarial input.
10. **Model-based regression and trade-offs** — Test deterministic mixed operations against independent list/deque outcomes, correct a seeded error and defend when a stack, FIFO, linked list or hash-backed structure fits the workload.

*Optional practice:* Compare a stack and a queue under the same operation sequence, then inspect a forced-collision hash model with a separately calculated expected lookup cost.

### Module 3 — Recursive Algorithms and Binary Search Trees

#### Outcomes

- SEF4-O3
- SEF4-O7
- SEF4-O12

#### Lessons

1. **Recursive contract and decreasing input** — Specify a base case and smaller recursive argument, then prove termination for a finite input domain rather than relying on sample runs.
2. **Call frames and resource limits** — Trace a call stack for a bounded recursive program and distinguish mathematical recursion depth, Python's recursion limit and heap memory used by data nodes.
3. **Tree structure and invariants** — Represent a rooted binary tree using node links; distinguish height, depth, leaf and subtree, including an empty tree and a one-node tree.
4. **Traversal orders** — Implement recursive and, where useful, iterative preorder/inorder/postorder traversal; independently predict the outputs for an unfamiliar tree.
5. **Binary search tree insertion** — Implement insert and lookup with an explicit key-comparison and duplicate-key policy, preserving each node's left/right ordering invariant.
6. **Missing keys, duplicates and mutation** — Check behavior after repeated inserts and missing lookups; diagnose a broken child link or duplicate-policy violation using an independent set or sorted-key oracle.
7. **Degenerate tree costs** — Explain why BST height, not the name “BST,” controls search and insertion time; compare skewed and balanced fixture shapes without requiring a balancing implementation.
8. **Recursive proof and reproducible tests** — Give a base/step correctness argument for one traversal or BST operation, verify it with empty/singleton/skewed fixtures and repair one observed failure.

*Optional practice:* Insert the same distinct keys in two orders and predict why the resulting BST heights differ while the sorted inorder keys agree.

### Module 4 — Lower-Bound Search, Sorting and Qualified Costs

#### Outcomes

- SEF4-O5
- SEF4-O6
- SEF4-O7
- SEF4-O12
- SEF4-O14

#### Lessons

1. **Linear search as a reference** — Implement a simple independently readable linear lower-bound oracle and distinguish a first matching element from the first index whose value is at least a target.
2. **Lower-bound contract and invariants** — Require nondecreasing sorted input; maintain a half-open search interval with proven facts about items before `lo` and at/after `hi`, returning the sequence length when no qualifying item exists.
3. **Shrinking search updates** — Justify `lo = mid + 1` or `hi = mid` against the invariant and a strictly decreasing interval length, including empty, duplicate-heavy and absent-target cases.
4. **Merge sort and structural recursion** — Implement stable merging with a declared equal-key tie policy; derive a valid recurrence, termination and memory cost from actual temporary buffers.
5. **Quicksort partition and pivot assumptions** — Implement an explicit partition/pivot strategy, state equal-key behavior and prove that recursive partitions progress on every tested input.
6. **Worst/expected sorting bounds** — Compare merge sort's standard worst-case `O(n log n)` with quicksort's `O(n²)` worst case, qualifying expected behavior by a distribution or randomized-pivot assumption rather than equating it with average measured time.
7. **Stability, identity and permutation** — Use labeled equal-key records to verify actual stability, compare element multisets and demonstrate why correct key order alone is not full sorting correctness.
8. **Auxiliary space and recursion depth** — Account for merge buffers, in-place partition choices, call frames and the possible recursion-depth hazards of a naive Python quicksort.
9. **Independent oracles and adversarial cases** — Compare lower-bound with linear scan and sorting with standard-library references across empty, singleton, ordered, reversed, duplicate and seeded random fixtures; repair a deliberate off-by-one defect.
10. **Honest performance observations** — Time both sorting methods over several sizes and input shapes with repeated trials, record real run conditions, and explain why a finite benchmark cannot prove asymptotic complexity.

*Optional practice:* Reproduce an incorrect lower-bound result on a repeated-key fixture and explain the single branch update that violates the loop invariant.

### Module 5 — Binary Heaps and Deterministic Priority Queues

#### Outcomes

- SEF4-O8
- SEF4-O7
- SEF4-O12

#### Lessons

1. **A complete tree in an array** — Derive zero-based parent/child index formulas and distinguish heap structural completeness from BST value ordering.
2. **The min-heap invariant** — Specify that each existing parent key is no greater than its children; inspect a proposed array and identify the exact violating edge.
3. **Insert, peek and extraction** — Implement sift-up and sift-down after state changes, including empty, one-item, repeated-priority and negative-priority cases.
4. **Bottom-up heapify and cost** — Construct a heap from an arbitrary array and justify linear-time heap construction with a sum over node heights rather than incorrectly inferring `O(n log n)` is tight.
5. **Stable priority tie policy** — Order records by `(priority, sequence, task_id)` and show why the unique sequence produces deterministic extraction even for equal priorities.
6. **Cancellation and obsolete events** — Either reject unsupported rescheduling/cancellation with a documented error or use explicit stale-entry invalidation; never execute a cancelled or superseded task silently.
7. **Independent extraction tests** — Compare a seeded sequence with a separately sorted reference, assert the heap invariant after every mutation and repair one faulty sift or stale-entry case.

*Optional practice:* Predict every array state while extracting an element from a small heap, then check your trace against an independently sorted output sequence.

### Module 6 — Graph Traversal, Shortest Paths and Dependencies

#### Outcomes

- SEF4-O4
- SEF4-O8
- SEF4-O9
- SEF4-O10
- SEF4-O7
- SEF4-O12

#### Lessons

1. **A precise graph contract** — Distinguish directed edges, vertex IDs, cycles, self-loops, parallel edges, isolated vertices and optional nonnegative weights under an explicit finite input model.
2. **Adjacency representation and costs** — Build adjacency lists, compare their `O(V+E)` storage to an adjacency matrix's `O(V²)`, and document any neighbor-order promise.
3. **Breadth-first search and reachable levels** — Implement BFS using a FIFO queue and a visited policy, explaining why each reachable vertex gets the minimal number of edges from the source in an unweighted graph.
4. **Depth-first search and cycles** — Implement iterative or bounded recursive DFS with visited-set discipline, deterministic neighbor iteration when claimed and termination on a cycle or self-loop.
5. **Disconnected and unreachable vertices** — Distinguish a single-source traversal from scanning every component; validate results against an independent finite reachability oracle.
6. **Weighted path definitions** — Define a nonnegative edge-weight contract, path sum, source-to-self distance zero and unreachable targets separately from a zero-weight route.
7. **Dijkstra with a priority queue** — Reuse the preceding heap/priority queue, justify settling a minimum tentative distance under nonnegative weights, and handle repeated or stale candidate entries explicitly.
8. **Negative-edge and tie limitations** — Reject unsupported negative weights before claiming Dijkstra's guarantee; handle zero weights, equal distances and parallel edges while distinguishing correctness of cost from a unique path preference.
9. **Independent distance and path reconstruction** — Check distances with a small Bellman–Ford or equivalent reference; verify predecessor chains, actual summed weights and unreachable-vertex behavior.
10. **Topological ordering and cycles** — Implement prerequisite-before-dependent ordering for a finite DAG, validate each edge constraint and reject cycles instead of returning a partial success.
11. **Graph proof and complexity defense** — Show termination, reachability coverage, nonnegative shortest-path assumptions and graph representation/heap-dependent running costs on normal and failing fixtures.

*Optional practice:* Draw a cyclic graph with an unreachable vertex, compare BFS/DFS from one source, then add weights and identify which claims require Dijkstra rather than ordinary BFS.

### Module 7 — Greedy Counterexamples, Exhaustive Search and Dynamic Programming

#### Outcomes

- SEF4-O11
- SEF4-O7
- SEF4-O12
- SEF4-O14

#### Lessons

1. **Algorithm design from a problem contract** — Identify objective, valid inputs, constraints, admissible output and a trusted finite reference before selecting greedy, exhaustive or dynamic-programming reasoning.
2. **Greedy choices and falsification** — Implement largest-first selection for positive coin denominations, demonstrate why `{1,3,4}` with target `6` defeats its optimality and distinguish a useful heuristic from an independently proved strategy.
3. **Bounded exhaustive or backtracking oracle** — Explore small targets or candidate sequences with explicit pruning/termination and use the resulting independent minimum as a reference, not a scalability claim.
4. **Dynamic-programming state and recurrence** — Define `dp[t]` as a documented minimum count or unreachable value, use `dp[0] = 0` and positive-denomination transitions, and derive a table in valid dependency order.
5. **Reconstruction, unreachable and invalid targets** — Test target zero, no usable coins, zero/negative denomination rejection and targets not representable when 1 is absent; avoid silently inventing an optimal solution.
6. **Correctness from subproblem optimality** — Explain why the recurrence considers every possible final coin and how induction on target size establishes correctness under the declared unbounded-use model.
7. **Pseudo-polynomial complexity** — Derive `O(target × denominations)` time and `O(target)` space for a one-dimensional table, noting that numeric target magnitude may be exponential in its binary input length.
8. **Independent strategy comparison and correction** — Challenge greedy and DP with unfamiliar bounded coin systems, locate a faulty transition or mistaken optimality claim, and defend which approach suits each stated constraint.

*Optional practice:* Compare greedy and the independent DP table for several small coin sets, including an unreachable target and a duplicate denomination.

### Module 8 — Integrated Algorithm Toolkit and Technical Defense

#### Outcomes

- SEF4-O1
- SEF4-O3
- SEF4-O4
- SEF4-O5
- SEF4-O6
- SEF4-O8
- SEF4-O9
- SEF4-O10
- SEF4-O11
- SEF4-O12
- SEF4-O13
- SEF4-O14

#### Lessons

1. **Reuse verified implementations** — Expose a documented toolkit of previously assessed containers, BST, search/sort, heap, graph and DP functions; keep their existing independent tests and invariant claims without duplicating all assessments.
2. **One bounded application contract** — Choose a small dependency-aware task planner, specify the meaning of dependency edges, task eligibility, priority ties and invalid/missing tasks before choosing structures.
3. **Join topological and priority behavior** — Reject cycles, release eligible tasks only after prerequisites are met and use deterministic priority order without executing blocked tasks prematurely.
4. **Cross-module failure isolation** — Inject an incorrect dependency or stale priority record, explain which invariant was violated and retain a regression that catches the integration error without hiding it behind a successful final report.
5. **Resource and reproducibility claims** — Compare two actual choices with independent reference outcomes and previously collected timings; document interpreter, workload, graph size, call-stack limitations and the assumptions that bound complexity.
6. **Evidence map and unfamiliar defense** — Link all seven published assessment outcomes to inspectable artifacts, reproduce one clean start and respond to a reviewer-chosen edge case or change, distinguishing proof from tested finite behavior.

*Optional practice:* Predict a dependency-aware task execution order with equal priorities and an unrelated isolated task, then verify why no blocked task was released early.

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

The change introduces one explicit introductory mathematical-transfer module, reorders existing analysis before proof-intensive searching and sorting, expands formative lesson guidance, and publishes an explanatory prerequisite/evidence crosswalk. The provisional duration changes from 10 to 12–14 weeks, to be calibrated against actual learner work. This is a teaching-sequence revision, **not a new completion contract or automatic reassessment** of historical learner evidence. The prerequisite remains SEF11, with SEF2 programming competence transitively established. At the time of this SEF4 revision, no downstream completion contract was amended **by this SEF4 change**. Subsequent separately approved [SEF6](SEF6.md) and [SEF10](SEF10.md) revisions have their **own current public contracts** (including SEF10's added O9/O10 and AS4); this historical statement must not be read as claiming those later courses are unchanged today. No paid resource, advanced library, global OEE spec rule or status promotion is introduced.

**Subsequent competency-derived SEF4 review:** The earlier nine-module arrangement duplicated general invariant/recurrence instruction in two separate modules and separated BFS/DFS from the shortest-path and dependency-graph reasoning that consumes it. The present instructional revision consolidates those boundaries and replaces isolated noun-style lessons with demonstrable algorithm tasks. This changes **only teaching organization**, not the fourteen published outcome definitions or any of the seven summative Work/Criteria/Evidence contracts. Previously completed work remains pinned to the revision actually assessed; no automatic equivalence or readiness promotion is inferred from this editorial review.
