# AI3 — Classical Artificial Intelligence, Search & Reasoning

**Program:** AI — AI Engineering
**Type:** course
**Prerequisites:** [AI1](AI1.md) — Scientific Computing & Data Engineering for AI (completed)
**Duration:** 18–24 weeks
**Status:** draft
**Specification:** v0.2.0
**Expected workload:** 10–15 focused hours/week (provisional; approximately 180–360 focused hours)

> [AI Engineering](README.md) · [Curriculum design guide](../DESIGN-GUIDE.md) · [Course format](../../spec/course-format.md) · [Evidence rules](../../spec/evidence-rules.md)

## Overview

**AI3 develops the ability to model, solve, verify and defend bounded intelligent decision and reasoning problems when a trained predictive model is not the appropriate primary abstraction.** Learners formalize states, observations, actions, constraints, knowledge, goals and uncertainty; then implement and reason about heuristic search, constraint satisfaction, adversarial choice, logical inference, deterministic planning and finite probabilistic belief models. The unifying competence is to make an intelligent system's assumptions, inferred conclusions, chosen actions, computational limits and failure modes inspectable. A valid answer is not merely one returned by a library: the learner must show what the answer means, why the mechanism can produce it, and which guarantees do not follow.

**Introduction, history, usage and applications.** Classical AI includes symbolic and state-space approaches to problem solving, long predating modern neural networks. State-space search supports routing and automated planning; constraint solving supports scheduling and configuration; adversarial search supports bounded games and competing choices; logical systems support explicit, reviewable rule conclusions; probabilistic graphical models support inference under uncertain observations. Different problems require different representations and proof obligations. Symbolic methods can be precise about defined rules yet fail when the rules or observations are wrong; heuristic methods can be practical yet sacrifice guarantees when their assumptions are broken. AI3 teaches when and why to choose these methods, not an historical ranking of symbolic versus learned approaches.

**Actual prerequisite closure.** AI entry already entails assessed completion of all eleven [SEF](../SEF/README.md) courses through SEF10. [SEF11](../SEF/SEF11.md) establishes propositional logic, quantified statements, sets, relations, induction, finite graphs and proof reasoning; [SEF4](../SEF/SEF4.md) assesses BFS/DFS, weighted shortest paths, heaps, recursion, invariants and algorithmic complexity. [SEF8](../SEF/SEF8.md) assesses probability and Bayes' rule, and SEF5/SEF9 establish tested software and responsible evidence. [AI1](AI1.md) adds explicit scientific-data integrity, observation identities, provenance and clean reproducibility. This course **does not re-teach** elementary graph traversals, Python, probability arithmetic, data cleaning or generic testing. It extends their assessed foundation into **AI-specific** states/goals, heuristic quality, constraints and propagation, opposing decisions, knowledge entailment, action effects and probabilistic dependencies.

**Parallel AI2 study is valid.** [AI2](AI2.md) develops mathematics of statistical and neural models and does not need to precede AI3. No gradient-based training, statistical learning theory, supervised model fitting, deep networks, LLMs or vendor agent SDK is assumed. The AI3 mathematical cases are small and use only the prerequisite probability and discrete reasoning. Sequential stochastic control and reinforcement learning belong to future AI6; AI3's one-step decision under uncertain evidence **is not** an MDP or learned policy. AI12 later uses these planning and reasoning foundations for tool-using software systems, but AI3 does not teach hosted LLM tools or autonomous high-impact execution. APP and SYS courses are not entry requirements.

**Feasibility, accessibility and scope.** All required exercises use compact, published synthetic state spaces, logical facts, finite probability tables and optional local Python 3 standard-library code (including heapq, itertools, collections and fractions). Code must be understandable and reproducible with ordinary CPU resources and no paid account, GPU, internet service, proprietary solver or instructor-only grading platform. Learners may implement equivalent algorithms in another language if they demonstrate the same public behaviors, reasoning and resource bounds. Decision traces, state tables, accessible textual graphs and written proofs are valid review media; no visual-only representation is compulsory. If an example could affect safety, privacy or external services, it must operate on synthetic/local data without real-world actuation or sensitive records.

**Learning versus evaluation.** Modules provide mechanisms, worked examples, negative cases, focused observations and optional formative feedback; they are not interchangeable compulsory quiz/lab templates. Seven required summative assessments use public independent oracles and a small set of reusable implementations or explanations, with a final unfamiliar variant and individually attributable technical defense. Learners need not build one enormous application implementing every classical AI technique: an integrated project selects **two substantively interacting mechanisms** and separately relies on the prior course evidence for the remaining competencies. Outcomes and tests, not elapsed time or feature count, govern completion. The 18–24-week duration is an untested planning estimate and does not justify raising the educational status above draft.

## Learning outcomes

- **AI3-O1:** Formulate an intelligent task with explicit state/observation/action vocabulary, initial conditions, legal transitions, goal or decision criterion, resource budget, environmental assumptions and claims that cannot be inferred.
- **AI3-O2:** Construct a finite state-space model, distinguish states from paths and histories, specify transition costs and duplicate-state policy, and validate a solution trace against independently defined legality and goal conditions.
- **AI3-O3:** Select and analyze uninformed and cost-sensitive state-space search under declared assumptions, distinguishing completeness, optimality, termination, expansion costs and false guarantees for cyclic, negative-cost or resource-limited problems.
- **AI3-O4:** Derive, check and compare admissible and consistent heuristics for bounded goal search; explain when graph-search A* is optimal, why reopen/termination policies matter, and how an invalid heuristic changes the evidence.
- **AI3-O5:** Implement bounded, deterministic, auditable AI search with correct priority and cost handling, independent expected answers, negative cases and explicit time/memory/exhaustion dispositions.
- **AI3-O6:** Formulate a finite constraint-satisfaction problem with variables, domains and constraints; apply consistent backtracking, variable/value ordering and justified propagation to find, count, reject or prove exhaustion of solutions.
- **AI3-O7:** Evaluate finite deterministic adversarial game trees using minimax and sound alpha–beta pruning assumptions, explaining payoff conventions, move ordering, cutoff evaluation and the limits of opponent models.
- **AI3-O8:** Express finite knowledge and queries in propositional logic, distinguish syntax, interpretations, satisfiability and logical entailment, and independently demonstrate sound conclusions or countermodels.
- **AI3-O9:** Use a bounded first-order or definite-Horn-rule representation with explicit domains, variable substitutions and inference rules to derive and explain legitimate conclusions without conflating absent facts with false ones.
- **AI3-O10:** Identify and contain contradictions, unsupported premises, incomplete observations, invalid rule applications and provenance errors in a knowledge-based system, stating what its inference results cannot establish.
- **AI3-O11:** Model a deterministic classical planning problem with typed or grounded action preconditions, add/delete effects, state invariants, resource assumptions and explicit goal satisfaction.
- **AI3-O12:** Generate or inspect a bounded plan, verify every transition and goal against an independent simulator/oracle, diagnose an invalid/unreachable case and defend an alternative or partial result.
- **AI3-O13:** Define a finite Bayesian network with normalized local conditional-probability tables and correct joint factorization, distinguishing directed influence assumptions from observational causation and graph-conditional independence.
- **AI3-O14:** Compute and verify exact prior, marginal and posterior queries by enumeration or factor elimination; handle zero-probability evidence, observed collider effects and the relevant computational and independence limits.
- **AI3-O15:** Compare bounded one-step choices by expected utility and evidence-dependent thresholds while disclosing loss assumptions, decision constraints and the boundary with sequential RL/MDPs and consequential real-world actions.
- **AI3-O16:** Integrate at least two appropriate classical-AI mechanisms into one local, independently reproducible solution with explicit interfaces, diagnostic traces, resource budgets, invalid cases, and proportionate evidence of the actual claimed capability.
- **AI3-O17:** Diagnose an unfamiliar bounded variation in a search, constraint, game, knowledge, planning or probabilistic model; derive a new independent expected result, repair or safely refuse the case and defend remaining limits.

## Modules

### Module 1 — Problem Formulation, Knowledge and Goal-Directed Systems

#### Outcomes

- AI3-O1
- AI3-O2
- AI3-O10

#### Lessons

1. **Classical AI's engineering scope** — Connect the history and current uses of symbolic, goal-based and probabilistic systems to a real bounded scheduling, navigation or diagnosis decision; explain what differs from a generic graph problem or learned prediction.
2. **Environment and agent boundaries** — Distinguish observable inputs, hidden state, action permissions, external transitions and local computation; explain why an agent's observation is not identical to the world's full state.
3. **States, actions and goals** — Define legal states, initial state, state-transition function, success predicate and impossible actions for a small synthetic environment, with falsifiable expected behavior.
4. **Paths, plans, policies and conclusions** — Contrast a path through an action graph, a constrained assignment, a conditional rule conclusion and a policy contingent on observations; reject treating all of them as interchangeable outputs.
5. **Objective and cost semantics** — Distinguish reachability, least accumulated cost, feasibility, adversarial payoff and expected utility; identify what units, tie rules and problem assumptions each objective needs.
6. **Explicit search and inference budgets** — Specify finite memory, state expansion, step and time budgets, and define whether exhaustion, budget stop, contradiction and invalid input are distinct outcomes.
7. **Specification and counterexample** — Write a small public contract for one AI problem and produce a plausible counterexample to an unjustified claim of optimality, legality or real-world truth.

*Optional feedback:* Given a delivery robot with incomplete room observations, name which facts are state, observation and assumption; identify a possible unsafe action before choosing a search algorithm.

### Module 2 — State-Space Search Beyond Graph Traversal

#### Outcomes

- AI3-O1
- AI3-O2
- AI3-O3
- AI3-O5

#### Lessons

1. **Implicit search-space construction** — Represent a problem by a successor generator and legal-state predicate instead of materializing every vertex; distinguish finite reachable state counts from potentially unbounded histories.
2. **Node records and frontier contracts** — Separate a problem state from a path node with parent, depth, action and accumulated cost; show how two paths reach the same state without becoming the same history.
3. **Uninformed search guarantees** — Use existing SEF4 BFS/DFS competence to derive when breadth-first minimizes **step count** rather than weighted path cost; state completeness limits of depth-first search with cycles and infinite branches.
4. **Uniform-cost search and weighted-route comparison** — Trace priority by accumulated cost, goal testing when a minimum-cost entry is removed, and correct best-cost/stale-entry handling on the synthetic S1 graph. Compare BFS's deterministic shortest-edge route with the cheaper, longer weighted route; explain why negative edges invalidate the usual UCS optimality claim and why a plausible path cost cannot replace proof of its legality.
5. **Graph-search duplicate and reopen behavior** — Contrast explored-on-generation, discovered-on-pop and best-known-cost policies; construct a counterexample where prematurely marking a state closed discards a cheaper later route.
6. **Cycles, unreachable goals and bounded termination** — Return a distinguished no-solution result on a fully exhausted finite reachable graph and a distinct resource-budget-exceeded result on a cut-off search.
7. **Independent path validation** — Check every returned edge, accumulated weight and goal independently of the solver's parent chain; reject fabricated or incorrectly costed paths even when the displayed cost is plausible.

*Optional feedback:* Predict the wrong answer from marking a node visited before a lower-cost alternative is processed; distinguish wrong optimality from malformed state encoding.

### Module 3 — Heuristic Search and Validity of Guarantees

#### Outcomes

- AI3-O3
- AI3-O4
- AI3-O5

#### Lessons

1. **Heuristics as estimates, not facts** — Define an estimate of remaining goal cost with a fixed cost model; distinguish an admissible lower bound from a learned or arbitrary ranking signal.
2. **Constructing a lower bound** — Derive a safe heuristic from a relaxed problem, known minimum movement cost or permitted operator subset, and document precisely which constraints are relaxed.
3. **Consistency over every legal edge** — Check h(s) ≤ c(s,s') + h(s') for each reachable edge and h(goal) = 0 under the chosen convention; relate consistency to nondecreasing f values along a path.
4. **A* priority and goal extraction** — Work f = g + h, tie-breaking and correct goal-on-pop behavior on a finite nonnegative graph; explain the graph-search conditions for an optimal reported route.
5. **Admissible versus inconsistent cases** — Construct a heuristic that is admissible but violates consistency and explain the need for appropriate reopening when a better g reaches a previously expanded state.
6. **Overestimating and incorrectly pruning** — Demonstrate that an overestimate or unjustified closed-list rule can remove an optimality guarantee, even when a sample run happens to return the optimum.
7. **Zero, weighted and resource-limited heuristics** — Compare h = 0 with uniform-cost behavior and a deliberately inflated heuristic on controlled small fixtures. Report expanded states, frontier memory and path cost under an explicit tie/reopen/budget policy; distinguish empirical effort reduction from a proof of optimality or completeness, and do not claim one heuristic always dominates.

### Module 4 — Constraint Satisfaction, Propagation and Exhaustive Evidence

#### Outcomes

- AI3-O1
- AI3-O6
- AI3-O5

#### Lessons

1. **Variables, domains and constraints** — Convert a finite scheduling or assignment problem into a CSP, naming domains, unary/binary/global constraints and the meaning of a valid solution.
2. **Constraint graphs and local scope** — Explain which variables a binary relation couples and when an all-different condition cannot be reduced to one unspecified pairwise rule without preserving meaning.
3. **Backtracking and consistency checks** — Implement systematic assignment with deterministic ordering and rejection of inconsistent partial states; explain why an early rejection is safe only for constraints already decidable.
4. **Variable selection and value ordering** — Compare fixed order, minimum-remaining-values and degree/value heuristics, identifying ties and which choices can change work without changing the set of valid solutions.
5. **Forward checking with reversibility** — Remove invalid values from future domains after assignment, restore them on backtracking, and reproduce a failure caused by destructive nonrestored domain edits.
6. **Arc consistency and AC-3 reasoning** — Revise a directed arc by removing values without support in its neighbor, explain the propagation queue and why pairwise arc consistency does not generally establish global satisfiability.
7. **Solution counting and independent CSP evidence** — Enumerate or rigorously establish all solutions on a bounded fixture, reject invalid/duplicate assignments, and verify legal assignments and the completeness claim independently of the solver. Contrast exhausted unsatisfiability with budget-limited unknown; report representative rejected partial states, reversible domain changes and whether propagation preserved the answer set rather than treating its trace as proof.
8. **Problem symmetry and overconstraint** — Show a safe symmetry break only when an actual permutation symmetry exists; identify how a falsely assumed symmetry could remove legitimate solutions.

*Optional feedback:* Under A < C and domains {1,2}, predict which domain values arc consistency removes and explain why the result does not solve every CSP.

### Module 5 — Adversarial Search and Bounded Rational Choice

#### Outcomes

- AI3-O1
- AI3-O7
- AI3-O5

#### Lessons

1. **Two-player adversarial model** — Specify alternating turns, legal moves, terminal conditions, shared payoff convention, information available to each player and the strict zero-sum assumption.
2. **Minimax backups** — Compute MAX and MIN values from terminal utilities on a finite tree; explain why locally attractive immediate rewards need not dominate a complete adversarial continuation.
3. **Tie-breaking and strategy reconstruction** — Reconstruct the selected root action and a defensible continuation when leaves tie, noting that a single displayed leaf value does not establish the optimal move.
4. **Alpha–beta bounds and move ordering** — Trace alpha and beta updates to exhibit a branch whose unseen leaves cannot affect the backed-up minimax choice; compare leaf visit counts under fixed and favorable ordering, retain the exact minimax value, and explain why pruning effectiveness depends on the search order rather than guaranteeing one universal complexity.
5. **Cutoff evaluation and horizon failures** — Introduce a finite-depth approximate utility and show how its error or horizon can change the recommended move; label heuristic evaluation rather than claiming exact optimal play.
6. **Non-zero-sum and incomplete-information boundaries** — Explain why minimax of a fixed shared utility may not model coordination, hidden information, multiple agents or arbitrary real opponents; reserve belief and sequential learning models for their appropriate owners.

### Module 6 — Propositional Knowledge and Valid Inference

#### Outcomes

- AI3-O8
- AI3-O10

#### Lessons

1. **Knowledge representation is a modeling choice** — Translate a bounded domain into named atomic propositions; distinguish observed facts, stated rules, defaults and unsupported assumptions.
2. **Models and satisfaction** — Interpret truth assignments and conjunction, disjunction, negation, implication and equivalence using SEF11 logic without re-teaching generic truth-table syntax; apply the semantics to a concrete KB.
3. **Entailment versus plausible explanation** — Show that a formula is entailed only if it is true in every model of the knowledge base; construct a countermodel when a purported consequence is not entailed.
4. **Sound inference steps** — Trace modus ponens and basic resolution on a finite clause set, identifying the rule premises and what has genuinely been derived.
5. **Normal forms and satisfiability checks** — Convert a small proposition to logically equivalent CNF and use a finite SAT check with an independently verifiable satisfying assignment or contradiction.
6. **Inconsistency and explosion** — Identify a KB containing both a claim and its negation; explain why a classical inconsistent KB is not a reliable source of informative unrestricted entailment and require a visible inconsistency decision.
7. **Open-world and closed-world assumptions** — Distinguish lack of a recorded fact from evidence of its negation; explain when a controlled local database uses a closed-world policy and why that assumption must be declared.
8. **Rule provenance and correction** — Associate each conclusion with premise/rule references, demonstrate how a changed or withdrawn premise affects the supported answer and reject a query unsupported by the current KB.

### Module 7 — First-Order Relations and Bounded Rule Systems

#### Outcomes

- AI3-O8
- AI3-O9
- AI3-O10

#### Lessons

1. **Objects, relations and variable scope** — Model a small typed domain using constants, predicates and explicit quantifiers; distinguish a fact about one object from a universal rule over a domain.
2. **Free variables and substitution hygiene** — Identify bound versus free occurrences, prevent variable capture during substitution and diagnose an incorrect substitution that changes the meaning of a statement.
3. **Unification and occurs-check intuition** — Compute substitutions for simple ground or variable-containing terms; reject conflicting constants and explain why careless recursive term unification can be invalid without suitable safeguards.
4. **Definite Horn clauses** — Represent a finite implication with conjunction of positive premises and a single positive conclusion; distinguish what cannot be represented faithfully without negation/disjunction or additional logic.
5. **Forward chaining with traceable provenance** — Derive new ground facts to a fixed point from finite, function-free rules, recording applied rule IDs, exact substitutions and supporting premises. Check a multi-step relation conclusion against an independently enumerated finite reference and disclose why an unsupported query cannot be asserted from these rules.
6. **Backward queries, recursion and independent failures** — Resolve a bounded goal into required subgoals, trace substitutions and premises against the actual fact base, and show how memoization or visited-goal handling stops cyclic derivations. Give an unsupported-query counterexample or open-world explanation instead of mistaking a missing proof for a false relation.
7. **Existential evidence and missing facts** — Explain the difference between an existential witness, a named entity and a guess, and do not infer a negative relation simply because a positive fact is absent.

*Optional feedback:* Derive Grandparent(Ada,Cy) from Parent(Ada,Bo) and Parent(Bo,Cy) under the declared rule, then explain why absence of Parent(Cy,D) cannot entail its negation.

### Module 8 — Classical Planning, Action Semantics and Plan Verification

#### Outcomes

- AI3-O1
- AI3-O11
- AI3-O12
- AI3-O5

#### Lessons

1. **Plans are sequences of state changes** — Distinguish planning with modeled actions from graph traversal with arbitrary unlabeled edges; define state fluents, initial world, goal facts and the frame assumptions.
2. **Grounded action contracts, preconditions and effects** — Specify required positive/negative preconditions and deterministic add/delete effects, execute one grounded action against a declared state, and reject an inapplicable action rather than silently ignoring its guard. Verify that a valid action preserves unrelated fluents and that a malformed add/delete description or contradictory effect does not produce an accepted transition.
3. **Goal conjunctions and regressions** — Identify required conditions for a chosen goal and calculate an appropriate predecessor-goal regression or alternative forward state plan.
4. **Resource and mutual-exclusion invariants** — Express capacity, one-location or one-carried-object restrictions and show which apparently valid state transitions violate them.
5. **Search in a planning domain** — Select a goal-directed state-space search or constrained planning strategy; distinguish sound plan validity from optimal plan length or cost.
6. **Failure, unreachable goals and partial plans** — Explain why missing required operators or contradictory invariants make a declared goal unreachable, and return an explicit failure without inventing a completed action sequence.
7. **Action-trace validation** — Use a separate tiny transition checker to verify every action's preconditions, effects and final goal, including an invalid order or conflicting resource condition.

### Module 9 — Bayesian Networks and Exact Belief Inference

#### Outcomes

- AI3-O13
- AI3-O14
- AI3-O10

#### Lessons

1. **From independent samples to related variables** — Represent uncertainty in linked finite variables with a directed acyclic graph; distinguish modeled dependence from confirmed causation.
2. **Conditional probability tables** — Construct local CPDs with explicit parents, possible values and normalized entries for every parent assignment, and reject invalid or incomplete rows.
3. **Joint factorization** — Derive the joint probability as the product of local conditional factors under the stated graph factorization and check total normalization by hand on a tiny network.
4. **Enumeration and marginalization** — Sum over hidden variable assignments to produce exact prior/marginal evidence probabilities and distinguish query variables from observed conditions.
5. **Posterior queries and zero evidence** — Compute P(query | evidence) from joint/marginal terms and explain why conditioning on zero-probability evidence is undefined under the model.
6. **Conditional independence and colliders** — Identify when a path is blocked or activated by conditioning; show an explaining-away example where two independent causes become dependent after observing a shared effect.
7. **Factor operations and variable elimination** — Multiply and sum out finite factors, showing how intermediate factor size depends on elimination order; compare with a small independent-enumeration oracle rather than assuming the output is correct.
8. **Model and observation failure** — Test an incorrect CPD, reversed dependence interpretation, omitted cause, incompatible evidence and unearned independence assumption; separate mathematical posterior validity from a scientifically validated model.

*Optional feedback:* For the public two-variable Bayesian network, calculate the evidence probability and posterior using exact fractions; challenge the graph's conditional independence claim with a different model.

### Module 10 — One-Step Decisions Under Uncertainty and Safe Boundaries

#### Outcomes

- AI3-O1
- AI3-O13
- AI3-O14
- AI3-O15

#### Lessons

1. **Belief, action, loss and one-step scope** — Distinguish posterior belief about a finite event, allowed actions, state-dependent utility, observation availability and a hard action limit. This is a single-decision model, not an MDP, partially observable sequential policy or reinforcement-learning algorithm; those require different transition and feedback evidence in AI6.
2. **Expected utility with transparent outcomes** — Compute the expected value of each bounded action by weighting its explicit consequences; justify why a lower expected loss can be preferred to a higher immediate positive payoff.
3. **Decision thresholds** — Derive the posterior threshold where two options have equal expected value, and test both sides of the threshold using exact small probabilities.
4. **Information value and its assumptions** — Estimate the value of a perfect hypothetical observation and a specified imperfect test, separating intrinsic signal quality, observation cost and the action changed by the result.
5. **Model uncertainty and decision robustness** — Change a prior, an observation likelihood or a utility entry and show whether the preferred action changes; do not hide a brittle threshold behind a single point estimate.
6. **Abstention, hard constraints and human control** — Distinguish expected-utility ranking from permission to act; apply declared hard safety/authorization rules even when a numerical payoff favors an unsafe action.

### Module 11 — Integrated Reasoning System and Unfamiliar Technical Defense

#### Outcomes

- AI3-O1
- AI3-O5
- AI3-O16
- AI3-O17

#### Lessons

1. **One credible bounded use case** — Select a local scheduling/assignment, diagnostic, route-planning or rule-guided decision problem and explain why two different AI mechanisms actually contribute, rather than collecting unrelated algorithms in one program.
2. **Interface contracts and genuinely new integration** — Specify inputs, outputs, assumptions, evidence traces, error types and resource budgets for two substantively interacting mechanisms. Extend legitimate prior assessed source where appropriate while identifying the new integration, source provenance and reviewer-visible responsibilities; do not require resubmission of unrelated predecessor assessments.
3. **Independent positive, adverse and bounded evidence** — Run a reproducible normal case and a deliberately malformed, infeasible, contradictory or uncertain case that tests a real invariant using independent expected answers. Record expansion/time/memory limits and distinct invalid, exhausted, unknown and budget-stop dispositions; explain remaining model, provenance and safety limitations without claiming production certification.
4. **Changed problem supplied by a reviewer** — Handle an unfamiliar small graph edge, CSP restriction, logical fact, action precondition or probability entry; predict the expected change independently and repair or refuse safely.
5. **Individual defense and handoff** — Explain the chosen representation, two interacting mechanisms, verification strategy, result limitations and a transfer case in a written, recorded or live form a reviewer can inspect without private tools.

The lessons above are instructional stages, not eleven separate required submissions. Work may reuse tested source, diagrams, proofs and explanations where a new outcome is genuinely evaluated.

## Completion requirements

### Shared public reference problems and independent oracles

The fixtures below are intentionally tiny so a learner and independent assessor can establish expected behavior without trusting a solver under evaluation. The same criteria apply to reviewer-supplied bounded variants. All state names, costs, logical rules and probabilities are illustrative synthetic data and must not be interpreted as facts about real people or systems.

**Search fixture S1 — weighted directed graph.** States are S (start), A, B, C and G (goal), with only these directed edges and nonnegative costs: S→A (2), S→B (1), A→G (4), B→C (1), B→G (8), C→G (2). Successor iteration at S lists A before B, and at B lists C before G. Valid simple goal paths are S–A–G (cost 6), S–B–G (cost 9), and S–B–C–G (**optimal weighted cost 4**). Breadth-first with this deterministic successor order returns S–A–G as a **two-edge** goal path; it is not cost optimal. Correct uniform-cost search returns cost 4 when goal-testing occurs on minimum-cost removal, with an appropriate best-cost/stale-entry policy. A consistent heuristic is h(S)=4, h(A)=4, h(B)=3, h(C)=2 and h(G)=0: h(G)=0 and h(u)≤cost(u,v)+h(v) for every listed edge. A* using f=g+h returns weighted cost 4 under the stated nonnegative finite graph assumptions. State that expansion counts depend on tie-breaking and implementation details, and never manufacture an exact count without publishing those policies.

**Constraint fixture C1 — assignment.** Three integer variables A, B, C each have domain {1,2,3}, with constraints A≠B, B≠C and A<C. Exactly three complete solutions exist, in (A,B,C) order: **(1,3,2), (1,2,3), (2,1,3)**. An assignment such as (1,2,2) violates B≠C; forcing A=3 makes the CSP unsatisfiable because A<C is then impossible in the domain. For the **separate two-variable arc-consistency subcase** with domains A=C={1,2} and only A<C, AC-3 reduces A to {1}, C to {2}. A solver claiming an additional solution must show the violated or missing constraint; a budget stop is not a proof of unsatisfiability.

**Game fixture G1 — two-ply game tree.** At a MAX root, action L leads to a MIN node with terminal payoffs [3,5] in that order; action R leads to a MIN node with payoffs [2,9] in that order. MIN chooses 3 under L and 2 under R, so minimax chooses **L with value 3**. With left-to-right expansion and conventional alpha/beta updates, after finishing L the first R leaf yields an upper bound 2≤root alpha 3, so R's second leaf 9 can be safely pruned. Incorrectly taking the maximum of the R leaves or assuming a non-zero-sum game is an invalid conclusion.

**Logic fixture K1 — finite entailment.** A propositional knowledge base contains A, A→B, B→C, so it **entails C**. Without A, the remaining two implications do **not** entail C; the model A=false, B=false, C=false is a countermodel. Adding ¬C to the original KB makes it inconsistent; a classical SAT-style checker must flag unsatisfiability rather than claim useful new evidence. For a **separate definite-Horn relation** set with Parent(Ada,Bo), Parent(Bo,Cy) and a rule Parent(x,y)∧Parent(y,z)→Grandparent(x,z), derive **Grandparent(Ada,Cy)** using an explicit substitution. The lack of Parent(Cy,D) does not entail ¬Parent(Cy,D) under an open-world reading. Do not conflate this predicate relation with the letter-valued CSP or graph states.

**Planning fixture P1 — robot and package.** Initially AtRobot(L), PackageAt(L) and HandsFree are true, with no other positive state fluents. The goal is PackageAt(R). Actions are: Pickup(L), requiring AtRobot(L), PackageAt(L), HandsFree; adding Carrying; deleting PackageAt(L), HandsFree. Move(L,R), requiring AtRobot(L); adding AtRobot(R); deleting AtRobot(L). Drop(R), requiring AtRobot(R), Carrying; adding PackageAt(R), HandsFree; deleting Carrying. The valid **three-action** plan is Pickup(L), Move(L,R), Drop(R). Drop(R) in the initial state is invalid. A model with no reverse Move or other reset actions must not silently assume extra movement operators. A separate plan checker must reject an action when its required positive preconditions are absent and verify the final goal and one-location/carrying invariants.

**Bayesian fixture B1 — a small directed graphical model.** Let A and B be binary, with A→B, P(A=1)=1/5, P(B=1|A=1)=9/10, P(B=1|A=0)=1/10. Then P(B=1)=13/50 and **P(A=1|B=1)=9/13**. Every local CPD is normalized and P(B=1)>0. For a separate collider example, X and Y are independent fair binary variables and Z is the deterministic logical OR of X and Y. Then P(X=1|Z=1)=2/3 whereas P(X=1|Z=1,Y=1)=1/2. These are conditional-dependence statements under the **specified mathematical model**, not causal findings from observed field data.

**Decision fixture D1 — one-step release/hold choice.** For a synthetic system with binary hidden fault F, Release yields utility +3 if no fault and −12 if fault; Hold yields utility 0 in either state. For posterior fault probability p, EU(Release)=3−15p and EU(Hold)=0; Release is preferred if **p<1/5**, Hold if p>1/5, and they tie at p=1/5. At p=1/4, Release has expected utility −3/4, so Hold is preferred. A hypothetical perfect costless observation has value 9/4 before its cost at p=1/4, because one would Release only in the no-fault case; a perfect test costing 1/2 has net value 7/4 versus Hold. Real-world release action is not authorized by this arithmetic; legal, safety and human controls remain separate.

**Environment and verification.** Python 3 with standard library, hand calculation and text-based evidence suffice. Reasonable substitutes may use other programming languages if the public oracle and behavior are preserved. For numeric evidence, state rational or floating precision and tolerances. No production API, external actuation, private personal data or proprietary dependency is required. Invalid inputs, zero-probability evidence, contradictory facts and capacity exhaustion must have explicit dispositions, not be passed off as completed solutions.

### Required summative assessments

- **AI3-AS1** (required AI search formulation, optimality and failure investigation)
  - **Outcomes:** AI3-O1, AI3-O2, AI3-O3, AI3-O4, AI3-O5.
  - **Work:** Specify an AI search problem with states, legal successors, cost and goal, using S1 or a justified equivalent. Independently list legal goal paths and their weights; trace BFS, uniform-cost search and A* with an explicit tie/goal/deduplication policy, showing why BFS's minimum-edge answer differs from the least-cost solution. Construct and check the provided consistent heuristic, and then test a deliberately overestimating or admissible-but-inconsistent alternative with a defensible policy discussion. Exercise a malformed edge, unreachable goal and a resource-budget stop; demonstrate a correctly calculated path cost and failure result. For the selected algorithm, implement or inspect a bounded solver with audit-ready expansion traces.
  - **Criteria:** S1's three listed simple goal paths cost 6, 9 and 4, and least weighted cost is 4; BFS under the fixed successor order yields the cost-6 two-edge path; a correct best-cost UCS/A* returns cost 4. Heuristic inequality holds edge by edge, and optimality claims are limited to their actual conditions. The solver never treats negative-cost, an invalid edge or a budget exhaustion as an ordinary optimal solution; path legality and weighted cost are independently checked rather than inferred from the solver itself.
  - **Evidence:** Model contract, hand-derived routes/costs and heuristic inequalities, source/commands or equivalent transparent algorithm trace, deterministic normal and negative test runs, resource-limit behavior and a brief explanation of algorithmic guarantees and limitations.

- **AI3-AS2** (required CSP formulation, propagation and exhaustive solution decision)
  - **Outcomes:** AI3-O1, AI3-O5, AI3-O6.
  - **Work:** Specify finite variables, domains and relationships for C1. Solve by deterministic backtracking with at least one justified inference or ordering improvement, showing representative rejected partial states and reversible domain changes. Enumerate all valid assignments (or produce an independently justified exact count), derive the AC-3 subcase without mistaking pairwise consistency for global solution, and demonstrate a genuinely unsatisfiable constraint variant and a distinct incomplete/budget-limited result.
  - **Criteria:** C1 has exactly the three published ordered solutions and the A=3 restriction yields exhausted unsatisfiability; the two-variable A<C propagation yields A={1}, C={2}. All returned assignments satisfy each constraint independently; pruning never removes a valid solution. Restoring domains on backtrack, unknown-versus-unsatisfiable disposition, and resource limitations are justified without asserting that propagation always solves a general CSP.
  - **Evidence:** CSP definitions, independently verified assignment oracle or proof/count, selected search/propagation trace, correct/invalid/unsatisfiable cases, bounded reproducible code or equivalent complete derivation and an explanation of any optimization claim.

- **AI3-AS3** (required adversarial-tree inference and pruning defense)
  - **Outcomes:** AI3-O1, AI3-O5, AI3-O7.
  - **Work:** Model a finite deterministic two-player zero-sum game using G1. Compute minimax backed-up values, root choice and a valid alpha–beta bound trace with fixed child ordering; compare visited leaves before and after pruning. Change one leaf or move order to investigate whether correctness or pruning effort changes. Introduce a depth-cutoff approximation and state what its value does not prove.
  - **Criteria:** Original minimax values are L=3, R=2 and root choice L=3; under the specified traversal, R's second leaf can be pruned after observing 2. A chosen pruning policy preserves the exact minimax value; altered move ordering changes work but is not falsely described as changing the exact value. A cutoff answer is identified as heuristic, and any unknown opponent or non-zero-sum setting is outside the published guarantee.
  - **Evidence:** Tree/payoff contract, independent MAX/MIN backup table, alpha/beta decisions and leaf-count convention, a changed-case trace, negative/cutoff analysis and source or checkable worked reasoning.

- **AI3-AS4** (required propositional and relational knowledge reasoning)
  - **Outcomes:** AI3-O8, AI3-O9, AI3-O10.
  - **Work:** Represent K1's implication KB and finite relation rule in an explicit syntax with semantic conventions. Derive C by sound inference and independently verify entailment; remove A and produce the published countermodel; introduce ¬C and detect inconsistency. For the finite Horn rule, derive Grandparent(Ada,Cy) with explicit substitutions and explain why missing facts are not classical negations. Include provenance of each used premise and a malformed/unsafe rule or substitution counterexample.
  - **Criteria:** C follows only under the relevant KB assumptions; the countermodel falsifies entailment after removing A; adding ¬C to the original KB is flagged as inconsistent, not treated as informative independent confirmation. The relation conclusion uses a correct variable substitution and no fabricated Parent relation. The finite engine terminates under its stated domain restrictions, and the learner distinguishes sound inference from real-world premise truth and open-world ignorance from a negative fact.
  - **Evidence:** Explicit formulas/rules, satisfiability/countermodel witness or independent truth assignment oracle, finite inference and substitution traces, provenance, contradiction/unknown cases and a concise statement of model limitations.

- **AI3-AS5** (required classical planning model and independent action verification)
  - **Outcomes:** AI3-O1, AI3-O5, AI3-O11, AI3-O12.
  - **Work:** Define P1's fluents, initial state, goal, grounded actions, preconditions, add/delete effects and invariants. Derive and execute its three-action plan with a separate plan validator, showing all intermediate states. Reject an illegal initial Drop(R); analyze a modified precondition, missing Pickup operator or blocked movement case and distinguish incomplete search from proven unreachability. If using search to find a plan, separately justify and verify claimed optimality or refrain from asserting it.
  - **Criteria:** Pickup(L), Move(L,R), Drop(R) is legal and achieves PackageAt(R) in the declared model; attempted initial Drop(R) is refused; no unlisted action is invented to make a failed trace work. The validation oracle checks every precondition, effect, invariant and final goal rather than trusting a planner-generated script; claimed shortest-step guarantees state the permissible operators and assumptions.
  - **Evidence:** Action schema, exact state traces, independent oracle, normal/invalid/changed-case results, executable local source or equivalent explicit derivation and bounded explanation of action-model limitations.

- **AI3-AS6** (required Bayesian inference and one-step decision justification)
  - **Outcomes:** AI3-O1, AI3-O13, AI3-O14, AI3-O15.
  - **Work:** Declare B1's graph, complete CPDs and factorization; use exact enumeration (and a separate factor-elimination trace or independently equivalent calculation) to compute evidence/marginal/posterior. Derive the collider explaining-away result under the distinct X,Y,Z model. Demonstrate a missing/unnormalized CPD, a zero-probability evidence event or another clearly invalid model case. Apply D1's action utility to derive the decision threshold, the decision at p=1/4 and the idealized value of perfect information including the stated hypothetical test cost. Explain why neither the graph nor a utility table establishes causation or permits a high-impact external action.
  - **Criteria:** B1 yields P(B=1)=13/50 and P(A=1|B=1)=9/13; the collider probabilities are 2/3 and 1/2 under the specified conditioning. D1 yields threshold p=1/5, Hold at p=1/4, expected Release utility −3/4 and perfect-information value 9/4 before and 7/4 after cost 1/2; cases with impossible conditioning are rejected as undefined. Factors/CPDs normalize, the posterior is justified independently, and the analysis does not claim a sequential RL policy or real-world validated risk.
  - **Evidence:** Small CPD/factor tables, independently calculated exact probabilities, implementation or transparent factor traces, positive/negative/zero-evidence checks, utility/threshold derivation, model and safety boundaries and a concise interpretation.

- **AI3-AS7** (required integrated local reasoning artifact and unfamiliar technical defense)
  - **Outcomes:** AI3-O1, AI3-O5, AI3-O16, AI3-O17.
  - **Work:** Build or consolidate **one bounded learner-owned** synthetic/local decision or problem-solving artifact integrating **at least two genuinely interacting mechanisms** drawn from this course (for example, constraint propagation before a plan search, rule eligibility before state-space routing, or Bayesian fault belief before a gated one-step decision). Reuse prior assessed source and proofs as appropriate; do **not** reimplement all six preceding assessments. Publish the problem contract, observable source-to-decision trace, clear component boundaries, independent normal and adverse expected results, a limited expansion/time/memory budget, safe failure handling and realistic operator/nonexpert limitations. An independent reviewer supplies one **unfamiliar bounded** change to a graph edge, constraint, fact, rule, action, observation or probability; predict its consequence **before** running any solver, then demonstrate correct repair or justified safe refusal. Defend individual authorship and the actual evidence in an accessible form.
  - **Criteria:** The two mechanisms materially affect a single defensible outcome, while each specialty outcome remains assessed by AI3-AS1–AS6; clean-state reproduction is possible without hidden fixtures, special hardware, paid APIs or real external actions. A reviewer can independently verify the positive case, adverse case and unfamiliar change; no state, cost, logical consequence, plan or posterior is accepted merely because the learner's code printed it. Exhaustion, unknown/budget failure, inconsistency and invalid inputs have distinct honest behavior. A qualified explanation and new evidence establish independent transfer, not a second full set of six separate projects.
  - **Evidence:** Coherent versioned source or inspectable equivalent, setup/test commands and synthetic fixtures, interface/state/evidence traces, independent outcome oracles, recorded controlled failure and unfamiliar-case before/after results, resource/safety assumptions and individually reviewable written/recorded/live technical defense.

### Required outcome-to-assessment coverage

| Outcome | Required summative evidence |
| --- | --- |
| AI3-O1 | AI3-AS1, AI3-AS2, AI3-AS3, AI3-AS5, AI3-AS6, AI3-AS7 |
| AI3-O2 | AI3-AS1 |
| AI3-O3 | AI3-AS1 |
| AI3-O4 | AI3-AS1 |
| AI3-O5 | AI3-AS1, AI3-AS2, AI3-AS3, AI3-AS5, AI3-AS7 |
| AI3-O6 | AI3-AS2 |
| AI3-O7 | AI3-AS3 |
| AI3-O8 | AI3-AS4 |
| AI3-O9 | AI3-AS4 |
| AI3-O10 | AI3-AS4 |
| AI3-O11 | AI3-AS5 |
| AI3-O12 | AI3-AS5 |
| AI3-O13 | AI3-AS6 |
| AI3-O14 | AI3-AS6 |
| AI3-O15 | AI3-AS6 |
| AI3-O16 | AI3-AS7 |
| AI3-O17 | AI3-AS7 |

**Course completion.** An independent reviewer must make a satisfactory, inspectable decision for **all seventeen AI3 outcomes** through the seven required assessments under the relevant course revision. The same verified code, derivations and traces can legitimately support several outcomes when distinct criteria are actually met. Optional exercises, elapsed weeks, completion checkboxes, a solver's own output, external credentials and copied example solutions never establish mastery alone. The integrated defense is **new transfer evidence**; it cannot waive failed or missing predecessor evidence or be used to assert competence not assessed by the actual criteria. The public assessment and evaluation contract remains independent of OEE Workspace, 0xNAND and any private implementation.

### Optional open academic and technical references

- [Stanford CS221, Autumn 2026](https://stanford-cs221.github.io/autumn2026/) — disciplinary context for search, games, constraints, graphical models and logical reasoning, not a mandate to duplicate course packaging.
- [UC Berkeley CS188](https://inst.eecs.berkeley.edu/~cs188/textbook/) — public introductory AI textbook covering problem solving, representation, uncertainty and decision making.
- [Artificial Intelligence: A Modern Approach, public Python examples](https://aimacode.github.io/aima-python/index.html) — algorithm vocabulary, implementation choices and examples; any referenced example must be independently verified against this course's own published oracle.
- [CS2023](https://csed.acm.org/) — broader computer-science competency guidance, not formal endorsement or automatic accreditation.

References are optional and free to access; public OEE requirements above are sufficient to understand every compulsory competency and assessment. No proprietary textbook edition or course-specific login is an admission or completion condition.
