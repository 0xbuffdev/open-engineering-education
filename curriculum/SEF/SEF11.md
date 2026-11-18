# SEF11 — Discrete Mathematics for Computing

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** [SEF2](SEF2.md)
**Duration:** 10–14 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–15 focused hours/week (provisional; mathematical bridge and reassessment may require more time)

> [Software Engineering Foundations](README.md) · [Course format](../../spec/course-format.md) · [Accepted architecture RFC](../../rfcs/0003-sef-academic-progression.md)

## Overview

Establish the exact mathematical reasoning needed to study algorithms, data structures, and software engineering without hidden prerequisites. Begin with number sense and elementary algebra, then develop logic, sets, functions, relations, proof and induction before using those methods for counting, asymptotic reasoning, recurrences, finite graphs, and state models. Learners must not merely recognize notation: they must independently solve, explain, prove or refute claims on unfamiliar examples, and distinguish a finite computation from a mathematical proof.

**No prior formal mathematics course is required.** SEF2 is the only course prerequisite. An **ungraded entry diagnostic** examines basic arithmetic, fractions, signed values, proportions, equations and input-output tables; it directs individual bridge practice and may not exclude learners or impose a fixed number of attempts. A learner who demonstrates readiness may move ahead without completing redundant practice. Core readiness competencies still must be demonstrated in required evaluation before the modules that depend on them.

Hand-written, typed, spoken or equivalently accessible mathematics is acceptable. Learners may verify small instances with Python 3.11+ standard-library modules such as `fractions`, `math`, `itertools` and `unittest`, but verification cannot replace a general proof. No NumPy, paid book, hosted account, proprietary evaluator or network access is required. Use small public, synthetic examples, document assumptions and preserve independent expected values.

The 10–14-week duration is a **provisional planning range**, not a readiness prediction for all beginners; the mathematical bridge is self-paced. Every module has optional formative practice, but only the six published summative assessments establish course completion. The course remains `draft` until reviewed learner evidence supports a higher status.

## Learning outcomes

- **SEF11-O1:** Calculate and interpret whole and signed numbers, fractions, decimals, percentages, ratios, rates, units, powers and estimates, including invalid operations and correct order of operations.
- **SEF11-O2:** Model simple equations, inequalities, algebraic expressions, discrete functions, domains, coordinate tables and graphs; solve, substitute and check results using unfamiliar values.
- **SEF11-O3:** Build and interpret propositional truth tables, implications, quantified statements and correct negations, distinguishing valid arguments from unsupported conclusions.
- **SEF11-O4:** Analyze finite sets, operations, functions and relations, including injectivity, composition, equivalence, partial orderings and counterexamples to assumed properties.
- **SEF11-O5:** Derive and check counting arguments using sum/product rules, permutations, combinations, elementary inclusion-exclusion and pigeonhole reasoning with clear assumptions.
- **SEF11-O6:** Construct or critique direct proofs, proofs by contradiction, mathematical induction and elementary divisibility/modular arguments; separate a universal proof from testing examples.
- **SEF11-O7:** Derive, compare and qualify asymptotic growth bounds and solve elementary recurrences, stating input domains, termination and the difference between worst, expected and amortized costs.
- **SEF11-O8:** Reason about finite graphs, degree, paths, connectivity, and deterministic finite-state transitions, and justify elementary invariants and reachability claims.
- **SEF11-O9:** Independently verify or falsify mathematical claims using a hand-derived oracle, bounded enumeration, optional exact Python calculations, and explicit counterexamples without confusing empirical evidence with proof.
- **SEF11-O10:** Integrate arithmetic, logical, combinatorial, proof and graph reasoning in a reviewable unfamiliar computing example and defend assumptions, corrections and limitations.

## Modules

### Module 1 — Number Sense and Mathematical Readiness

#### Outcomes

- SEF11-O1
- SEF11-O9

#### Lessons

1. **Course purpose and diagnostic** — Explain how mathematics supports correct computing, locate individual starting gaps with an ungraded diagnostic and distinguish practice from summative readiness.
2. **Numbers and place value** — Use number lines, whole numbers, signs, absolute value and order correctly.
3. **Arithmetic and estimation** — Compute with grouping, precedence, multiplication, division, rounding and reasonableness checks.
4. **Fractions and decimals** — Normalize and operate on rational quantities, including zero denominators and exact versus approximate forms.
5. **Percentages and proportions** — Convert percentages and fractions, compute ratios, rates and changes with meaningful denominators.
6. **Units and scaling** — Carry and check units through dimensional conversions, proportions and comparison of quantities.
7. **Powers and roots** — Evaluate integer exponents, roots, powers of ten and scientific notation.
8. **Independent numerical checks** — Predict by hand and then verify small examples in Python, distinguishing a round-off artifact from a conceptual mistake.

*Optional practice:* Solve unfamiliar signed, fraction, ratio and power problems; diagnose and correct a deliberately incorrect computation. Continue bridge practice as needed without a fixed attempt limit.

### Module 2 — Algebra, Functions and Discrete Models

#### Outcomes

- SEF11-O2
- SEF11-O9

#### Lessons

1. **Symbols and expressions** — Translate written conditions into variables, equations and simple formulas.
2. **Equations and inequalities** — Solve elementary linear cases, verify by substitution and preserve inequality direction correctly.
3. **Functions and domains** — Distinguish input, output, domain, codomain and range; evaluate function tables.
4. **Coordinates and graphs** — Interpret discrete and simple linear graphs, slopes, intercepts and rate relationships.
5. **Function composition** — Compute and compare composed functions, including undefined intermediate values.
6. **Computing models** — Model sizes, indexes, bounds and runtime quantities with algebraic expressions.

*Optional practice:* Derive a cost function from a tiny loop and check its values against a hand-worked table.

### Module 3 — Logic and Quantified Reasoning

#### Outcomes

- SEF11-O3
- SEF11-O9

#### Lessons

1. **Statements and truth values** — Distinguish propositions from open predicates and informal assertions.
2. **Boolean connectives** — Construct complete truth tables for AND, OR, NOT, implication and equivalence.
3. **Logical equivalence** — Verify De Morgan laws, implication rewrites, converse and contrapositive.
4. **Quantifiers** — Interpret universal and existential claims over an explicit domain.
5. **Negating quantified statements** — Correctly swap quantifiers and negate predicates; supply counterexamples.
6. **Arguments and inference** — Separate valid logical steps from a true conclusion reached by invalid reasoning.
7. **Computing contracts** — Express small input preconditions, postconditions and invariant candidates as precise propositions.

*Optional practice:* Translate ambiguous program specifications into quantified statements and refute an over-broad claim.

### Module 4 — Sets, Functions and Relations

#### Outcomes

- SEF11-O4
- SEF11-O3
- SEF11-O9

#### Lessons

1. **Finite sets** — Define membership, subsets, union, intersection, difference and complement relative to a declared universe; test set equalities or refute them with a particular element.
2. **Finite mappings and their properties** — Distinguish domain, codomain, and actual image/range; inspect a complete finite function table for output uniqueness, repeated images, and missing codomain values to establish or refute injectivity, surjectivity and bijectivity.
3. **Composition and inverse conditions** — Compose two finite mappings only when their input/output sets are compatible, calculate a result for each declared input, and explain with a collision or uncovered element why a non-bijection cannot have a two-sided inverse.
4. **Relations and counterexamples** — Classify small finite relations for reflexivity, symmetry, antisymmetry and transitivity, supplying a witnessing pair or triple where a property fails.
5. **Equivalence classes** — Produce partitions from valid equivalence relations and detect an invalid proposed partition using the properties actually required.
6. **Order relations** — Distinguish partial and total orders; identify incomparable pairs and explain why a prerequisite relation is not automatically a total order.
7. **Computing data contracts** — Relate sets, mappings, relations and ordering to stated programming constraints; independently verify small finite tables while distinguishing exhaustive verification of a finite fixture from proof of an unrestricted theorem.

*Optional practice:* Given two finite function tables with declared domains and codomains, find collisions, missing images and a valid composition; separately analyze a small dependency relation for the required relation properties.

### Module 5 — Proof, Induction and Elementary Number Theory

#### Outcomes

- SEF11-O6
- SEF11-O3
- SEF11-O9

#### Lessons

1. **What a proof establishes** — State hypotheses and conclusion, and distinguish an example from a universal argument.
2. **Direct proofs** — Establish implications using definitions and algebraic transformations.
3. **Counterexamples and contradiction** — Refute a universal false claim and prove a suitable statement by contradiction.
4. **Mathematical induction** — Supply a base case, induction hypothesis and justified induction step.
5. **Strong induction and recursive definitions** — Reason about recursive construction and termination on finite inputs.
6. **Divisibility and greatest common divisors** — Use divisibility definitions and the Euclidean algorithm on small integers.
7. **Modular arithmetic** — Compare congruence classes and connect fixed-width wraparound to explicit moduli.
8. **Proof review** — Identify invalid steps, unsupported assumptions, circular reasoning and missing boundary cases.

*Optional practice:* Prove the sum of the first `n` odd positive numbers is `n²`; explain why testing ten values alone is insufficient.

### Module 6 — Combinatorics and Counting

#### Outcomes

- SEF11-O5
- SEF11-O9

#### Lessons

1. **Sum and product principles** — Count disjoint alternatives by addition and successive choices by multiplication when the number of options is fixed for each stage; split into cases when later options depend on an earlier choice, rather than incorrectly assuming probabilistic independence.
2. **Factorials and arrangements** — Count permutations with clearly stated constraints.
3. **Combinations** — Count unordered selections and distinguish them from ordered pairs.
4. **Repetition and restrictions** — Account for repeated choices and forbidden configurations.
5. **Inclusion-exclusion** — Derive counts for two overlapping finite sets.
6. **Pigeonhole proofs** — Use the earlier proof methods to establish the capacity contradiction behind the pigeonhole principle; state the number of objects and containers and handle the boundary where no repetition is forced.
7. **Exact checking** — Verify a small count with `itertools` enumeration, without treating enumeration as a universal proof.

*Optional practice:* Contrast five-choose-two (10 unordered choices) with five-times-four (20 ordered choices); trace where double counting occurs.

### Module 7 — Asymptotic Growth and Recurrences

#### Outcomes

- SEF11-O7
- SEF11-O6
- SEF11-O9

#### Lessons

1. **Function growth** — Compare constants, logarithms, polynomials and exponentials with declared input domains.
2. **Big-O, Omega and Theta** — Explain asymptotic bounds and justify or refute proposed bounds analytically.
3. **Proof with inequalities** — Supply constants and thresholds for simple asymptotic claims.
4. **Recursive cost equations** — Translate a shrinking problem into an elementary recurrence with a base case.
5. **Recurrence solutions** — Reason with substitution, expansion or a recursion tree on simple examples.
6. **Worst-case, expected and amortized claims** — State what input constraints and probability assumptions (if any) each cost statement requires; distinguish worst-case cost of one operation, expected cost under a specified distribution, and a deterministic average bound over an entire sequence. A timing graph is not a mathematical proof.
7. **Aggregate analysis of a growing buffer** — For a conceptual capacity-one array that doubles when full, count unit insertions and element copies across `n` appends, justify a geometric-sum bound on total work, and distinguish one expensive resize from constant amortized work per append without assuming random inputs. This prepares the correctness and cost analysis of [SEF4](SEF4.md), not a new coding requirement.

*Optional practice:* Expand `T(n)=T(n/2)+1` for powers of two; justify a logarithmic bound and verify several small instances independently.

### Module 8 — Finite Graphs and State Transitions

#### Outcomes

- SEF11-O8
- SEF11-O6
- SEF11-O9

#### Lessons

1. **Graphs and representations** — Define vertices, edges, directedness, loops and finite adjacency structures.
2. **Degree and counting** — Prove the handshaking identity for finite undirected graphs under declared assumptions.
3. **Paths and connectivity** — Distinguish walks, paths, cycles, connected components and reachability.
4. **Directed dependency graphs** — Reason about directions, prerequisites and cycles without requiring a full topological-sort implementation.
5. **Finite-state models** — Trace states, allowed transitions, initial state, reachable states and terminal/fault states.
6. **Inductive invariants and reachability** — State the initial-state claim, prove that every allowed transition preserves it and identify a violating transition or counterexample when it does not hold; distinguish this argument for all reachable states from merely observing several successful traces.

*Optional practice:* Trace a tiny finite-state parser or access policy by hand and identify unreachable transitions.

### Module 9 — Integrated Discrete Reasoning Investigation

#### Outcomes

- SEF11-O1
- SEF11-O2
- SEF11-O3
- SEF11-O4
- SEF11-O5
- SEF11-O6
- SEF11-O7
- SEF11-O8
- SEF11-O9
- SEF11-O10

#### Lessons

1. **Mathematical specification** — Turn a bounded computing problem into explicit domains, constraints, functions and predicates.
2. **Correctness argument** — Select suitable proof forms and identify assumptions, invariants and counterexamples.
3. **Quantitative reasoning** — Count relevant cases, analyze a small recurrence and justify asymptotic claims.
4. **Independent checks** — Construct a hand oracle and optional exhaustive small-case verifier, then expose limits.
5. **Technical defense** — Explain an unfamiliar variation, correct a detected error and defend the result without a hidden solver.

*Optional practice:* Outline a dependency-checking or bounded state-machine investigation using already assessed mathematical reasoning.

## Completion requirements

### Assessment environment and evidence

Six required summative assessments collectively evaluate the published outcomes. The arithmetic/algebra bridge is assessed for demonstrated mastery, **not** entry admission: the initial diagnostic remains ungraded; learners may practice and reassess an unmet essential category with new numbers and no fixed attempt limit.

Submit reviewable handwritten, typed, spoken or equivalent accessible reasoning. For optional verification code use Python 3.11+ standard-library tools only, record exact inputs and commands, and distinguish independent expected results from generated output. A complete proof must justify a general claim under stated assumptions; a finite test, screenshot or code run does not by itself prove the theorem. An uncorrected foundational error blocks the corresponding required assessment. Existing competent evidence may be reused without manufacturing extra identical assignments.

### Required summative assessments

- **SEF11-AS1** (required arithmetic and algebra readiness)
  - Outcomes: SEF11-O1, SEF11-O2, SEF11-O9
  - Work: After an optional ungraded diagnostic, solve unfamiliar signed/fraction arithmetic, percentages, unit ratios, exponents, a linear equation and inequality, and a function table including an out-of-domain input. Estimate an answer before calculation; check the equation by substitution, reject division by zero, and independently reproduce selected exact fractions using Python or hand calculation. Find and explain one intentionally flawed worked solution.
  - Criteria: Essential number operations, order of operations, units, equation/inequality reasoning, functions and bounds are correct with no hidden algebra prerequisites; invalid input is not turned into a plausible value. The learner explains rather than guesses results, and may reassess an unmet essential category on equivalent new cases. The diagnostic is not graded.
  - Evidence: Hand-derived work, assumptions/units, substitution and boundary checks, invalid case, before/after error explanation, optional exact-code check and documented assessment decisions.

- **SEF11-AS2** (required logic, sets, functions and relations)
  - Outcomes: SEF11-O3, SEF11-O4, SEF11-O9
  - Work: Derive full truth tables for implication and its disjunction form, correctly negate a quantified predicate, compute specified finite-set operations, and classify small relations for reflexivity, symmetry, antisymmetry and transitivity. Using two small declared finite function tables, determine whether each mapping is injective, surjective or bijective, compute a defined composition, and identify a collision, missing codomain image or incompatible mapping when an asserted property fails. Construct one equivalence-class partition, one incomparable pair in a partial order and one counterexample to an invalid proposed property. Reuse the same reviewable finite tables rather than create another unrelated submission.
  - Criteria: Truth-table rows and quantified negations follow an explicitly stated domain. The domain and codomain of each function are clear; injectivity is justified by unique images or a specific collision, surjectivity by codomain coverage or a missing image, and finite composition by compatible input/output sets and correct evaluated values. Set and relation-property classifications are correct, with counterexamples and independently checked entries. The learner distinguishes an implication from its converse.
  - Evidence: Truth tables, quantified reasoning, finite-set/relationship and function-composition tables, a collision or missing-image witness where applicable, partition and partial-order explanation, independent validation and one corrected misconception.

- **SEF11-AS3** (required combinatorics and exact counting)
  - Outcomes: SEF11-O5, SEF11-O9
  - Work: Derive ordered and unordered two-of-five selection counts (20 and 10), explain their different sample spaces, derive a constrained product-rule count, use inclusion-exclusion for two overlapping sets, and prove a pigeonhole claim with a declared number of containers. Verify at least two small results through a separately derived enumeration and reject invalid counting parameters.
  - Criteria: No silent double counting; counts correctly use order, replacement and disjointness assumptions. Inclusion-exclusion accounts for overlap, the pigeonhole proof follows capacity constraints, and code is not presented as general proof.
  - Evidence: Written arguments, count table, explicit constraints, enumeration results, invalid cases and a counterexample or corrected counting error.

- **SEF11-AS4** (required proof, induction and modular reasoning)
  - Outcomes: SEF11-O6, SEF11-O3, SEF11-O9
  - Work: Give a complete induction proof that the sum of the first n positive odd integers equals n squared for positive n. Prove an elementary parity/divisibility statement directly, justify a simple Euclidean-algorithm example and a modular wraparound identity, and use a counterexample or contradiction to reject a false general claim. Identify and repair a supplied invalid induction step.
  - Criteria: Every proof states the domain, base or hypotheses, justified inference and conclusion; induction does not assume the desired next case. Congruence and divisibility calculations are valid under the stated modulus. Small enumeration is only a check.
  - Evidence: Written proof steps, modular calculations, reviewed false-claim counterexample, corrected flawed proof and independent small-case checks.

- **SEF11-AS5** (required growth, recurrence, graph and state reasoning)
  - Outcomes: SEF11-O7, SEF11-O8, SEF11-O6, SEF11-O9
  - Work: Prove a logarithmic bound for `T(n)=T(n/2)+1` on powers of two with a stated base case. Give a valid Big-O witness for a polynomial bound. For a conceptual dynamic array initially holding zero elements with capacity one and doubling whenever full, charge one unit for each append plus one for every element copied during a resize; derive a valid upper bound on total work across `n` appends for `n >= 1`. Explain why one append can cost linear work while the sequence has constant amortized work per append, and why this is not an expected-case probabilistic claim. Prove the handshaking identity for a finite undirected graph; draw and analyze a directed graph with an unreachable vertex and a cycle. Trace a small deterministic state machine and justify a reachable-state invariant, including a deliberately invalid transition.
  - Criteria: Cost bounds follow valid reasoning rather than measurements; recurrence assumptions and Big-O witnesses are correct. The declared buffer model's total insert/copy cost is bounded by a valid geometric-series or equivalent aggregate argument, and the learner distinguishes worst-case, amortized and distribution-dependent expected claims without conflating them. Graph definitions and edge counts are correct. Reachability and state changes match the declared model; the invariant proof covers the initial state and preservation under every permitted transition, and faults are not silently accepted.
  - Evidence: Recurrence derivation, constants/thresholds, an append-and-copy cost table and aggregate bound, graph-degree argument, directed graph and state tables, initial/preservation invariant proof, invalid case, independently checked finite instances and correction record.

- **SEF11-AS6** (required integrated discrete computing investigation and defense)
  - Outcomes: SEF11-O1, SEF11-O2, SEF11-O3, SEF11-O4, SEF11-O5, SEF11-O6, SEF11-O7, SEF11-O8, SEF11-O9, SEF11-O10
  - Work: Assemble prior assessed reasoning into one bounded, inspectable investigation of a dependency graph, finite-state workflow, or equivalent computation problem. State domains and numeric constraints, express logical preconditions, count small cases, present a direct/inductive invariant or counterexample, analyze an elementary recurrence, and trace graph/state behavior. Reuse earlier valid evidence instead of re-solving unrelated worksheets. A reviewer chooses an unfamiliar bounded variation and one wrong claim to diagnose.
  - Criteria: Every required competency is linked to actual independently checkable evidence. The unfamiliar variation is reasoned from the given rules; false generalizations are rejected, missing proof steps corrected and logical/numeric assumptions explicit. The learner can justify any optional verifier and distinguish its bounded coverage from proof. No proprietary evaluator, paid resource, or advanced programming library is needed.
  - Evidence: Consolidated written or recorded explanation, diagrams/state tables, proofs, exact-check fixtures, outcome-to-evidence map, corrections, reviewer challenge and a reviewable defense.

### Completion decision

All six required assessments must demonstrate SEF11-O1 through SEF11-O10. Optional examples and the **ungraded entry diagnostic** never add hidden pass requirements; an essential missing skill is remediated and reassessed with equivalent unfamiliar examples rather than ignored. Assessment evidence must remain reproducible and reviewable using public material and the learner's accessible chosen format.

Completion of SEF11 establishes the required discrete mathematics preparation for SEF4 and SEF8; work from another course does not automatically satisfy these assessments without an explicit evidence-based equivalence decision. This course remains `draft` until the [readiness requirements](../../spec/status-labels.md) are satisfied.

### Academic review and prior evidence

This competency-derived realignment preserves the existing ten published outcome identities, six required assessment identities, course prerequisite and ungraded/self-paced arithmetic-and-algebra bridge. Proof methods now precede the combinatorial proofs that use them. The existing SEF11-O4/SEF11-O7 expectations are made directly inspectable in SEF11-AS2 (finite functions, composition and counterexamples) and SEF11-AS5 (a bounded aggregate-cost argument), without adding another separate examination, paid dependency or programming prerequisite.

Earlier assessed work remains associated with the **course revision under which it was evaluated**; no previous pass is silently invalidated or treated as evidence for newly explicit examples. A reviewer may recognize evidence of the same published competence under an approved, genuinely assessed equivalence decision, or request an unfamiliar equivalent case when necessary. The current source remains `draft`; restructuring and structural validation do not establish tested or verified educational readiness.
