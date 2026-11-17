# AI6 — Sequential Decision Making & Reinforcement Learning

**Program:** AI — AI Engineering
**Type:** course
**Prerequisites:** [AI3](AI3.md) — Classical Artificial Intelligence, Search & Reasoning; [AI5](AI5.md) — Deep Learning & Representation Learning (both completed)
**Duration:** 20–28 weeks
**Status:** draft
**Specification:** v0.2.0
**Expected workload:** 10–15 focused hours/week (provisional; approximately 200–420 focused hours)

> [AI Engineering](README.md) · [Curriculum design guide](../DESIGN-GUIDE.md) · [Course format](../../spec/course-format.md) · [Evidence rules](../../spec/evidence-rules.md)

## Overview

**AI6 develops the ability to reason about, implement, evaluate and defend agents learning from sequences of actions and delayed outcomes.** Its central problem is not fitting a static label or computing a fixed plan: actions can alter future observations and rewards, data depend on the behavior policy, and performance must be evaluated over explicitly defined sequential tasks. Learners design finite Markov decision processes (MDPs), derive value/Bellman relations, solve known small models, learn values and policies from trajectories, investigate exploration and feedback, inspect stable and unstable function-approximation methods, and establish when policy-evaluation evidence is insufficient or unsafe. They must independently verify numeric updates and state transitions instead of treating an environment's printed score as proof.

**Scientific and historical context, use and limitations.** Sequential decision making links dynamic programming, Markov modeling and control to behavioral learning. Bandits isolate action-dependent feedback; tabular reinforcement learning learns action values without a supplied transition model; policy gradients optimize stochastic decision rules using sampled returns; approximate and deep RL make larger state representations possible while introducing instability. These methods appear in simulations, games, resource allocation, constrained scheduling research and control experiments. They do not imply that deploying exploratory policies in actual infrastructure, hospitals, vehicles or user-facing services is permitted or safe. Reward is a *declared proxy*, not evidence that the learner optimized human welfare.

**Assessed entry readiness and course ownership.** Entry requires completed [AI3](AI3.md) **and** [AI5](AI5.md). AI3 already assesses state/action/goal modeling, deterministic plans, search, finite beliefs, probabilistic inference and **one-step** expected-utility decisions; AI6 extends them to stochastic transitions, delayed rewards, learned policies and multi-step belief-conditioned consequences. AI5 already assesses differentiable networks, PyTorch or equivalent autograd, gradients, optimization diagnostics, checkpoints and unbiased baseline comparison; AI6 applies those to value/policy approximation and tests their additional sequential-data failure modes. Through AI5 the learner has assessed AI4 classical statistical evaluation, AI2 mathematics, AI1 scientific data and the entire SEF program. **Do not repeat** basic probability, gradient descent, Python, planning search, ordinary train/test mechanics or elementary neural layers as a second course. No APP or SYS course is needed, and completing AI3 alone is insufficient for the deep RL assessments.

**Deliberate scope limits.** AI6 owns bandits, finite MDPs, DP on *known* transition models, Monte Carlo/temporal difference learning, exploration, on/off-policy control, value approximation, bounded DQN, policy gradients/actor–critic, elementary model-based RL, partial observability and offline policy-evaluation limits. AI10 will own general-purpose advanced model adaptation, scaled optimization and large-model training engineering; AI12 will own LLM tool-using application agents; AI13 will own system-wide AI assurance, testing and operational evaluation; AI14 will own broader AI security, ethics and governance; AI15 will own deployed AI service reliability. [AI18](README.md) later specializes in robotics/embodied interaction and real physical constraints. This course does not assess high-dimensional robotics, extensive continuous-control suites, distributed model training, language-model post-training or unapproved real-world actuation. A bounded policy-gradient and actor–critic implementation **is required**; PPO/SAC algorithms may be compared conceptually but are not hidden implementation gates.

**Teaching and computational conditions.** All mandatory tasks use **small synthetic, locally specified** bandits, state machines, trajectories and tabular data that can be hand-checked and simulated with Python 3's standard library. For the deep approximation component, a small CPU-only PyTorch or equivalent open autograd library is acceptable, but no GPU, cloud credit, commercial environment, remote account, paid benchmark, vendor API or unreleased dataset can be required. Gymnasium is an optional compatible convenience, **not** the authority for the state semantics. The learner must define observation/action/reward units, transition probabilities, horizon/discount, initialization, random-state ownership, behavior policy, policy evaluation protocol and correct distinctions among **termination, time-limit truncation, safety stop and invalid action**. Accessible transition tables, event traces and text descriptions must convey information otherwise shown graphically. All experiments declare seed lists, episode/update budget, reward convention, evaluation confidence limits and negative controls. A single seeded episode, simulator test, or high nominal return is never a generalization or safety guarantee.

**Learning, progression and assessment.** Thirteen competency-derived modules progress from modeling to analysis, data-driven learning, approximation, policy optimization, offline evaluation and independent engineering defense. Lesson numbers follow conceptual necessity rather than a fixed uniform count. Nine required cumulative assessments establish **22 observable course outcomes** using shared code and evidence rather than nine unrelated full systems: finite model and Bellman reasoning, bandits/exploration, Monte Carlo/TD, policy control, approximate/deep Q learning, policy gradient/actor–critic, model-based/partial observation, logged-policy risk, and an unfamiliar end-to-end change. Exact examples and separately checkable oracles are published below. The 20–28-week estimate is provisional and includes derivation, simulation, implementation, debugging, repeated evaluation, review and corrections; no learner-tested duration or course status promotion is claimed.

## Learning outcomes

- **AI6-O1:** Specify a bounded sequential decision problem with agent/environment boundary, state versus observation, legal action, reward/cost, horizon, transition assumptions, decision permission, comparator and intended performance claim.
- **AI6-O2:** Construct and independently validate a finite MDP with normalized transition distributions, rewards, initial-state distribution, terminal states and explicit finite-horizon or discounted-return semantics.
- **AI6-O3:** Derive discounted episodic returns, state/action values and Bellman expectation/optimality relations under the declared reward timing, discount and terminal conventions.
- **AI6-O4:** Perform and verify exact small-model policy evaluation, value iteration and policy improvement, explaining contraction/optimality conditions, stopping and counterexamples when assumptions fail.
- **AI6-O5:** Analyze finite stochastic multi-armed bandits, action-value estimates, exploration policies, feedback selection and expected regret with explicit stationarity and comparator assumptions.
- **AI6-O6:** Generate and validate sequential trajectory evidence with behavior-policy probabilities, actual observations/actions/rewards, state-reset rules, terminal/truncation distinctions and controlled randomness.
- **AI6-O7:** Calculate and implement first-/every-visit Monte Carlo returns and bounded on-policy prediction, distinguishing full returns, finite samples, variance and missing/censored episodes.
- **AI6-O8:** Calculate, implement and compare one-/multi-step temporal-difference prediction and eligibility-trace mechanisms, distinguishing bootstrapped targets, trace decay, online update order and bias/variance limitations.
- **AI6-O9:** Implement and independently verify tabular SARSA and Q-learning control updates with correct action-policy/target distinction, terminal handling, tie behavior and explicit convergence limitations.
- **AI6-O10:** Design and analyze exploration versus exploitation and on-/off-policy behavior, including probability support, epsilon schedules, state-action coverage, prohibited exploratory actions and mismatched data distributions.
- **AI6-O11:** Construct finite-state features or value-function approximations and diagnose the interaction of off-policy data, bootstrapping and function approximation without assuming general convergence.
- **AI6-O12:** Implement and independently check a tiny deep value learner using replay, stable target-network handling, valid terminal/truncation masks, controlled update/gradient flow and appropriate resource limits.
- **AI6-O13:** Derive and independently check a bounded stochastic policy-gradient/log-probability update with return or advantage weighting, baseline interpretation and normalization conventions.
- **AI6-O14:** Implement or rigorously inspect a simple actor–critic scheme with valid critic/actor targets, shared or separated computation, on-policy sampling assumptions and failure/variance diagnostics.
- **AI6-O15:** Compare planning with a known dynamics model and learning an estimated transition/reward model from finite interaction, testing model bias and error propagation into rollout decisions.
- **AI6-O16:** Model a small partially observable sequential task with explicit observation likelihoods, finite belief updates and policy-relevant uncertainty, distinguishing a belief state from a hidden true state or an unjustified causal claim.
- **AI6-O17:** Derive and calculate logged-data/off-policy policy-evaluation estimators for bounded support-valid cases, identifying importance-weight variance, unsupported target actions, trajectory mismatch and estimator failure.
- **AI6-O18:** Design fair, reproducible sequential-policy experiments with baselines, independent evaluation episodes, seeds, variability/uncertainty, sample efficiency and appropriate training/evaluation data boundaries.
- **AI6-O19:** Implement and verify valid environment/reset/step interfaces and evaluation oracles, distinguishing natural termination from exogenous truncation and applying correct bootstrap and reward accounting.
- **AI6-O20:** Identify reward-design defects, proxy/reward exploitation, unsafe exploration, hidden constraints, overclaimed offline evidence and actual action permissions, demonstrating explicit synthetic guard/failure conditions.
- **AI6-O21:** Produce one clean-state reproducible, CPU-feasible sequential agent investigation with transparent model/policy/configuration lineage, independently checked state/update oracles and measured compute/interaction costs.
- **AI6-O22:** Respond to an unfamiliar bounded environment, reward, transition, termination, behavior-propensity, policy, observation or safety change by independently predicting its effect, repairing or refusing unsupported behavior and defending the remaining limits.

## Modules

### Module 1 — Sequential Learning as an Engineering Problem

#### Outcomes

- AI6-O1
- AI6-O2
- AI6-O20

#### Lessons

1. **From supervised prediction to action-dependent data** — Distinguish a fixed train/test labeled table from a sequence whose actions change subsequent observations and feedback.
2. **History, applications and why reward is not a requirement** — Locate bandits, dynamic programming and RL in bounded scheduling/game/simulation applications, and explain why high reward can conflict with actual objectives.
3. **Agent, environment and observer** — Define decision authority, available observations, hidden environment state, action effects, exogenous processes and what a simulator can or cannot establish.
4. **Policies, plans, trajectories and value** — Contrast AI3's fixed action plan and one-step expected choice with a contingent multi-step stochastic policy and its expected return.
5. **Known model versus sampled experience** — Separate an available transition/reward specification from logged events produced by a behavior policy; do not treat a model learner's estimates as ground truth.
6. **Finite and continuing task contracts** — Specify start distribution, horizon/episode handling, reward units, action constraints and a precise comparator (fixed baseline or oracle).
7. **Evidence and permission boundaries** — Define independent oracle, CPU/interaction budget, reward-hacking negative control, no real-world actuation and explicit refusal under unsafe/unsupported conditions.

*Optional feedback:* In a two-step simulator, identify which variable is hidden state, which is observation, which data were generated by the behavior policy, and why a superficially “successful” one-step action may have worse long-run return.

### Module 2 — Finite MDPs, Returns and Bellman Semantics

#### Outcomes

- AI6-O2
- AI6-O3
- AI6-O6
- AI6-O19

#### Lessons

1. **Markov property and sufficient state** — Declare when next-state/reward distributions depend on the current state and action rather than on an unrecorded history; identify an omitted timer or resource variable that violates this assumption.
2. **Finite transitions and legal actions** — Construct P(s',r | s,a) with all outcomes and normalized probabilities; reject zero-sum/incomplete rows and actions without a declared transition.
3. **Terminal state versus restart observation** — Explain why a task-complete terminal transition has no next-step continuation value, irrespective of a simulator's next reset output.
4. **Reward timing and discounted return** — Derive G_t=R_(t+1)+gamma G_(t+1) on a finite trajectory with explicitly assigned reward to transitions; distinguish gamma=0, discounted continuing and finite horizon.
5. **Value and action-value definitions** — Write V^pi(s) and Q^pi(s,a) as expectation over legitimate future trajectories with specified start/policy assumptions, rather than a single observed score.
6. **Bellman expectation equations** — Derive a stochastic fixed-policy expectation update using normalized probabilities and policy action weights; make all state, reward and discount conventions visible.
7. **Optimal action values and feasible decisions** — Derive the Bellman optimality maximization over **authorized** legal actions only; explain why maximizing a numeric reward cannot override an external safety prohibition.
8. **Horizon and remaining time in state** — Show why a finite horizon can make an otherwise identical observed location have a different optimal choice, requiring time-to-go in the state or explicit time indexing.
9. **Hand-checkable MDP contract** — Independently verify every row, return and terminal behavior for the public M1 fixture and demonstrate an invalid nonnormalized/negative-cost claim without silently changing the task.

### Module 3 — Planning with a Known MDP and Exact Policy Improvement

#### Outcomes

- AI6-O3
- AI6-O4
- AI6-O19

#### Lessons

1. **Evaluation of a fixed stochastic policy** — Derive the finite-state linear Bellman equations when policy and environment dynamics are known and solve a tiny nontrivial self-loop case.
2. **Iterative policy evaluation** — Apply repeated expectation backups from specified initial values; explain stopping tolerance and the role of discount/contraction conditions.
3. **Value iteration as optimality backup** — Trace simultaneous (not silently in-place asynchronous) updates from V0 and predict when the optimal choice changes across iterations.
4. **Policy improvement theorem boundaries** — Select a greedy action against a correctly evaluated current policy and explain why it improves or preserves its value only under suitable finite discounted MDP assumptions.
5. **Policy iteration and stable stopping** — Alternate exact/sufficient evaluation and improvement with specified tie policy, treating an unchanged policy as a candidate fixed point under declared conditions.
6. **Optimality and reward scale** — Investigate a changed gamma or reward and explain which results remain valid and which policy ranking changes; distinguish an exact model proof from a simulator estimate.
7. **Stochastic dynamics and expected backups** — Calculate a transition-weighted Bellman target rather than choosing the most likely single next state and treating it as certainty.
8. **Unreachable states and invalid model conditions** — Distinguish states absent under the initial policy from states impossible by model; catch an invalid transition kernel and unsupported claims at gamma=1 for continuing nonterminating tasks.
9. **Independent solver comparison** — Verify evaluation, value iteration and a policy-improvement result against a separately computed exact M1 oracle; do not infer correctness from agreement between two implementations sharing the same bug.

### Module 4 — Bandit Feedback, Exploration and Expected Regret

#### Outcomes

- AI6-O5
- AI6-O10
- AI6-O18

#### Lessons

1. **One-step bandit versus full MDP** — Formalize repeated choices with immediate action-dependent feedback and no action-induced evolving state, and explain what sequential dependence this abstraction deliberately omits.
2. **Stationary reward distributions** — Define an arm's reward expectation and observed samples; distinguish an unknown fixed mean from a realized reward in a small Bernoulli experiment.
3. **Sample-average and constant-step estimates** — Trace incremental action-value updates with correct denominators or learning rate, reporting how untried arms are represented.
4. **Epsilon-greedy exploration** — Distinguish the greedy probability from the uniform exploration branch, including cases where exploration chooses the greedy action as well.
5. **Optimism and confidence-based exploration** — Explain optimistic initialization and a UCB-style confidence term under its own observation/count/stationarity assumptions, without universal regret claims.
6. **Expected regret with an oracle comparator** — Derive difference between optimal mean and the behavior policy's mean, and distinguish expected cumulative regret from a particular noisy reward sequence.
7. **Nonstationarity and sample recency** — Compare sample-average and constant-step tracking under a documented changing arm mean, and explain why a stationary guarantee is then inapplicable.
8. **Constrained action sets** — Enforce a forbidden arm or cost budget before exploration and state why the learning algorithm cannot legalize an action through optimism or high predicted reward.

*Optional feedback:* Under uniform random selection between two fixed Bernoulli arms with means 3/4 and 1/4, derive expected per-step regret without simulating four sample outcomes.

### Module 5 — Logged Trajectories and Monte Carlo Policy Evaluation

#### Outcomes

- AI6-O6
- AI6-O7
- AI6-O18
- AI6-O19

#### Lessons

1. **Episodes and record ownership** — Store initial state, behavior policy, action probability, reward, successor, termination/truncation and stable episode identity; reject impossible transitions and mismatched resets.
2. **Generating a trajectory under a policy** — Explain which stochastic choices belong to the environment and which belong to the action selector, preserving their seed streams separately.
3. **Return-to-go computation** — Compute Monte Carlo returns backward from the end of a *truly terminal* episode and account for gamma and each transition's observed reward.
4. **First- versus every-visit estimates** — Trace a repeated-state episode and show exactly which returns contribute to each estimator under declared visit convention.
5. **Policy evaluation using complete episodes** — Calculate empirical average return for a fixed policy, distinguishing estimated expected value, episode-level variance and unequal initial-state distributions.
6. **Exploring starts and policy coverage** — Explain why an unvisited state-action has no direct return evidence and how on-policy data collection can change its visitation frequencies.
7. **Truncated and incomplete episodes** — Distinguish a true task terminal state from a data-collection stop; describe why naive zeroing of all truncated returns biases the intended continuing-task value.
8. **Independent trajectory audits** — Validate a small exact M1 trajectory with hand-calculated G_t; test a missing reward, illegal action and incorrect terminal flag as independent error cases.

### Module 6 — Temporal Difference Learning, n-Step Targets and Traces

#### Outcomes

- AI6-O7
- AI6-O8
- AI6-O19

#### Lessons

1. **Bootstrap target versus full sampled return** — Derive delta_t=r_(t+1)+gamma V(s_(t+1))−V(s_t), with no continuation value for a truly terminal successor.
2. **TD(0) update order** — Hand-calculate the public T1 two-episode online updates using *current* estimates rather than an accidentally simultaneous or future value.
3. **Monte Carlo and TD bias/variance** — Explain why full returns and bootstrap estimates rely on different information and why neither universally dominates across tasks.
4. **n-step bootstrapped return** — Derive the sum of up to n discounted rewards plus gamma^n V at the valid bootstrap boundary, handling a real terminal within the window.
5. **Truncation-aware TD** — Show why a time-limit cutoff in a continuing task generally still permits bootstrapping from the last true observation, while true termination does not.
6. **Eligibility traces and credit assignment** — Compute a small accumulating trace using e_t(s)=gamma lambda e_(t−1)(s)+1{s_t=s}, with stated update ordering and why λ changes how past states receive correction.
7. **Off-policy and implementation constraints** — Explain why naive traces from behavior-policy samples do not automatically become an unbiased target-policy algorithm and why stale overwritten values matter.
8. **Step size, coverage and nonstationarity** — Inspect alpha choices and online dependence, distinguishing textbook convergence under restrictive sampling/step-size conditions from finite observed success.
9. **TD negative-case forensics** — Catch an off-by-one reward, an unintended reset, an incorrect gamma power or stale successor value; provide an independent exact corrected update before rerunning code.

### Module 7 — Tabular Control, Behavior Policies and Action-Value Learning

#### Outcomes

- AI6-O9
- AI6-O10
- AI6-O19
- AI6-O18

#### Lessons

1. **Action values and control improvement** — Extend state-value prediction to Q(s,a), legal action restrictions and an epsilon-greedy behavior policy.
2. **On-policy SARSA update** — Calculate r+gamma Q(s',a') using the *actual next action sampled from the current behavior policy*, and demonstrate that a nongreedy next action changes the target.
3. **Off-policy Q-learning update** — Calculate r+gamma max_a Q(s',a) regardless of exploratory next behavior action; explain why this does not remove requirements about state-action exploration and stationarity.
4. **Expected SARSA expectation** — Compute the behavior-policy weighted successor Q rather than a sampled a' or max alone, specifying the correct epsilon action probabilities including tied greedy actions.
5. **Online update chronology** — Walk through the M1-related T2 two-episode trace; distinguish a target computed before the next state's Q update from a value already modified by later steps.
6. **Tie-breaking, invalid actions and coverage** — Implement declared deterministic/stochastic ties, legal-action masking and no coverage claims about actions the behavior never tries.
7. **Exploration and control tension** — Compare optimistic, fixed epsilon and decaying epsilon behaviors on a tiny stochastic/unsafe branch, stating effects observed and which theoretical guarantees are absent.
8. **Convergence limits** — Identify finite tabular discounted assumptions, sufficient state-action coverage and learning-rate conditions behind familiar convergence results, rejecting an assertion that a constant-alpha finite run always converges.
9. **Policy comparison against exact MDP** — Compare sampled policy value on independent evaluation episodes with M1's true optimum and disclose sample variance and model correctness assumptions.

### Module 8 — Approximate Value Functions and Instability Mechanisms

#### Outcomes

- AI6-O11
- AI6-O18
- AI6-O21

#### Lessons

1. **Why tabular enumeration can fail** — Identify state-space dimensionality and representation requirements without assuming any arbitrary neural architecture is justified.
2. **Features for value approximation** — Fit a small linear V(s)=theta·phi(s) or Q(s,a) representation with explicitly named feature/parameter dimensions and a separately checkable prediction.
3. **Semi-gradient TD** — Distinguish treating a bootstrap target as fixed during the update from differentiating through every model component, including where the approximation changes the theoretical objective.
4. **Projection and distribution dependence** — Explain how representation restricts reachable value functions and how the behavior-policy state distribution affects approximation loss.
5. **Deadly-triad interaction** — Identify **off-policy sampling + bootstrapping + function approximation** as a potential divergence configuration and explain why using each individually does not imply identical failure.
6. **Stability is a measured property here** — Compare one stable and one unstable or badly specified learning configuration on a bounded fixture with explicit observed values, avoiding a fabricated universal divergence demonstration.
7. **Confidence and extrapolation failure** — Show that a feature-based Q predictor may return unjustified values for unvisited actions or states, especially when trained on different behavior-policy data.
8. **Independent function-value checks** — Derive a linear prediction and its changed-feature value exactly; separately verify error and resource behavior without treating neural output as proof.

### Module 9 — A Bounded Deep Q Learner

#### Outcomes

- AI6-O11
- AI6-O12
- AI6-O19
- AI6-O21

#### Lessons

1. **State representation and discrete action Q head** — Build a tiny CPU-scale network mapping a finite state-feature vector to legal-action Q values, with explicit output order, shape and invalid-action policy.
2. **Bellman target versus prediction** — Derive the target y=r+gamma(1−terminated)max_a Q_target(s',a) and distinguish it from the current network's differentiable Q(s,a).
3. **Gradient flow and stop-gradient** — Explain why target computations should not silently backpropagate through the target network and why a learnable online prediction differs from a fixed teaching signal.
4. **Replay transition provenance** — Store state, action, reward, next state, real terminal and time-limit truncation with behavior origin and version; detect invalid transitions and sampling correlations.
5. **Experience replay and its limits** — Sample bounded replay batches, report state-action coverage and explain why decorrelation/reuse is not a universal unbiasedness or convergence guarantee.
6. **Target-network copy/lag** — Trace fixed target copies or slow updates and their intended stabilization role; compare a deliberately unstable shared-target variation with recorded rather than assumed outcomes.
7. **Double-estimation intuition** — Analyze a small case where maximization of noisy Q estimates leads to optimism, then explain a double-Q target's action-selection/evaluation separation without making Double DQN a separate mandatory package project.
8. **Episode handling and finite compute** — Implement deterministic reset evaluation, stop on true termination/truncation appropriately and handle continuing-task bootstrap semantics at collection cutoff.
9. **Tiny independent training study** — Reproduce a small deep value-policy learning run on a synthetic MDP, compare against tabular/exact reference with actual scores and measure replay size, parameters, CPU update time and failure behavior.

### Module 10 — Stochastic Policy Gradients and Actor–Critic Estimation

#### Outcomes

- AI6-O13
- AI6-O14
- AI6-O18

#### Lessons

1. **Direct parameterization of actions** — Map a finite state feature to a categorical policy with valid normalized probabilities, legal-action masking and explicit log-probability conventions.
2. **Log-derivative identity** — Derive the score-function form of the policy gradient under declared trajectory and reward assumptions; distinguish maximizing expected return from differentiating through sampled environment actions.
3. **One-sample policy-gradient arithmetic** — Work P1's exact logistic policy update on a single sampled action with a declared step size, and show why a particular sample cannot guarantee improvement.
4. **Reward-to-go and variance** — Compare weighting a log-action gradient by total episode return versus causally appropriate future return with explicit discount conventions and known limitations.
5. **Baselines and advantage** — Explain how an action-independent state baseline can reduce variance under correct weighting without changing the true expected score-function gradient when assumptions hold.
6. **Value critic fitting** — Construct a one-step TD critic target and diagnose leakage/bootstrapping changes in the critic's own estimation, using AI5's autograd infrastructure.
7. **Actor–critic integration** — Trace a small actor update weighted by an advantage estimate and a separate critic value update, explicitly controlling gradient ownership and stale estimator behavior.
8. **On-policy data freshness** — Explain why a Vanilla Policy Gradient rollout gathered under an earlier policy cannot simply be reused under a changed policy without additional correction or changed objective.
9. **Entropy regularization and collapse** — Investigate the effect of an entropy incentive or overly decisive early policy on action coverage, documenting the chosen coefficient, legitimate action set and actual measurements.
10. **Independent policy evidence** — Compare a policy-gradient or actor–critic small run to a fixed/random/tabular baseline on independently seeded evaluation episodes, reporting variability, instability and the lack of a safety guarantee.

### Module 11 — Model-Based Interaction and Partial Observability

#### Outcomes

- AI6-O15
- AI6-O16
- AI6-O20

#### Lessons

1. **Known model planning versus estimated dynamics** — Distinguish AI3's deterministic modeled plan, Module 3's known stochastic MDP and a transition model estimated from action-conditioned interaction.
2. **Transition/reward counts and uncertainty** — Estimate a finite categorical next-state distribution from declared counts, explain unseen state-action pairs and why smoothing priors are assumptions rather than observed outcomes.
3. **Model error in value backups** — Compare exact M1 and a deliberately biased transition estimate and calculate the effect on one Bellman target and action choice.
4. **Dyna-style real and imagined updates** — Trace one actual interaction, one model-estimation update and one synthetic planning update, identifying where a wrong model can amplify erroneous value estimates.
5. **State versus observation under partial observability** — Introduce finite hidden-state dynamics, observation likelihoods and an action-dependent belief update; a single raw observation is not necessarily Markov.
6. **Small Bayesian belief filter** — Compute public P2 prior-to-posterior update exactly and explain what additional transition information would be required for multi-step belief prediction.
7. **Uncertainty, safe observation and abstention** — Compare acting under a point guess versus a belief distribution and describe when restrictions on sensing/action/uncertainty require refusal despite attractive expected returns.
8. **Boundary to robotics and large-scale control** — Identify unresolved dynamics, continuous observations/actions, sensors, physical hazards and sim-to-real mismatch; reserve engineering of actual embodied systems for AI18.

### Module 12 — Offline Policy Evidence, Generalization and Safety

#### Outcomes

- AI6-O6
- AI6-O10
- AI6-O17
- AI6-O18
- AI6-O19
- AI6-O20

#### Lessons

1. **Logging policy and target policy** — Declare behavior-policy action probabilities and a target policy for the same state/context, distinguishing the policy that generated a record from the one being evaluated.
2. **Support/positivity and identifiability** — Explain why a target action with zero probability under the logging policy has no direct counterfactual reward evidence, regardless of the target network's confidence.
3. **One-step importance weighting** — Derive and compute P3's ordinary inverse-propensity estimator with exact recorded probabilities and an honest out-of-range finite-sample result.
4. **Self-normalization and variance** — Compute the same tiny example using self-normalized weights, explain its distinct bias/variance behavior and why neither point estimate is a reliable guarantee with two records.
5. **Sequential behavior mismatch** — Explain why a multi-step trajectory weight is a product of action ratios along the observed history and why unsupported paths and long horizons cause severe variance.
6. **Model-based and doubly robust intuition** — Compare supervised fitted-Q/model-based evaluation with inverse-propensity weighting under explicit assumptions; no unimplemented large-scale statistical theorem is implied.
7. **Independent held-out evaluation episodes** — Fix evaluation policies after selection, use fresh start-state and environment seeds, report return distribution, episode length, constraint violations and a justified uncertainty summary.
8. **Reward hacking, proxy failure and forbidden actions** — Demonstrate a synthetic agent exploiting an incomplete reward (e.g. repeated locally rewarded action that violates an external task constraint), and enforce declared hard limits independent of learned Q.
9. **Termination, truncation and auditability** — Use an explicit step API that distinguishes task termination, time-limit data cutoff, invalid action and safety stop; show the different target/bootstrap and decision consequences.
10. **Claim discipline and rollback conditions** — Define unsupported generalization, offline confidence, exploration harm, compute/inference constraints and human stop controls; a bounded simulator result authorizes no external actuation.

### Module 13 — Integrated Sequential-Agent Study and Unfamiliar Defense

#### Outcomes

- AI6-O1
- AI6-O18
- AI6-O19
- AI6-O20
- AI6-O21
- AI6-O22

#### Lessons

1. **Select one finite local decision system** — Specify a synthetic task with observation/state/action/reward/termination, intended start population, safe action set and a meaningful nonlearning baseline.
2. **Reuse independent algorithmic evidence** — Collect previous MDP/DP, bandit, TD, tabular, deep and policy-gradient work as legitimate references, selecting only the mechanisms needed for a coherent final investigation rather than rebuilding all of them.
3. **Implement and audit a learner–environment contract** — Make reset, legal actions, state transitions, numerical reward and termination/truncation visible through a separate exact finite oracle.
4. **Fit and compare under a real interaction budget** — Run a tabular RL or small neural policy method appropriate to the task, compare with exact/planning or fixed-policy reference under reserved evaluation seeds and disclose actual outcomes.
5. **Perform a negative and safety experiment** — Diagnose a bad bootstrap mask, policy-support hole, stale target, missing state, reward loophole or prohibited action, recording the incorrect behavior and real repaired outcome.
6. **Review data and computational provenance** — Document behavior/target policies, sample/episode IDs, policy checkpoint, random seeds, library/environment versions, CPU time, number of interactions, and evaluation/selection separation.
7. **Unfamiliar bounded reviewer variation** — Independently predict the effect of a changed reward, transition distribution, time limit, action restriction, behavior propensity, observation model or evaluation population; compute a new reference value or justify inability to infer and repair or safely refuse the case.
8. **Individual technical defense** — Explain exact versus sampled evidence, why chosen learning mechanisms are warranted, what the observed returns do not prove and how a reader can reproduce every declared outcome without private resources.

These modules are instructional stages rather than thirteen forced submissions. Optional exercises and diagnostics support learning; **the nine assessments below**, not the number of lessons completed, establish the summative evidence contract.

## Completion requirements

### Public synthetic fixtures and independently checkable reference values

All mandatory cases are locally reproducible with small, openly specified arrays and finite random generators. Exact expected values apply only to the declared model, policy, reward convention and update order. Experimental returns and neural policies must be **actually run and reported**; no predetermined performance claim is accepted as a substitute for observed evidence.

**M1 — Three-state finite discounted MDP with an optional loop (known model).** States are S (start), B (intermediate) and T (terminal); gamma=1/2. Legal S actions: Stop -> T with immediate reward 1, or Go -> B with immediate reward 0. Legal B actions: Finish -> T with reward 4, or Wait -> B with reward 1. T has no actions, no further reward and V(T)=0. Every listed transition is deterministic and all actions have probability 1 for their listed successor. The optimal B action is Finish, V*(B)=4; its alternative Q*(B,Wait)=1+(1/2)4=3. The optimal S action is Go, V*(S)=2; Stop has value 1. With synchronous value iteration V0(S)=V0(B)=0, **V1(S)=1,V1(B)=4**, then **V2(S)=2,V2(B)=4** and these values persist. Under the *fixed policy* π(S)=Go, π(B)=Wait, Vπ(B)=1+(1/2)Vπ(B)=2 and Vπ(S)=(1/2)2=1. Replacing B's action with Finish improves S's Go-return to 2. The exact two-transition trajectory S–Go/r0–B–Finish/r4–T has undiscounted observed rewards (0,4) and **discounted returns G_S=2, G_B=4**. An alternative S action or invalid B reward cannot be silently inserted into the model.

**B1 — Bandit expectation and regret.** Two *stationary independent Bernoulli* arms have true means μ_A=3/4 and μ_B=1/4, unknown to a learning agent. A predetermined uniform action selector has expected reward (μ_A+μ_B)/2=**1/2** per round, whereas the oracle always selecting A has expected reward **3/4**. Uniform selection's expected pseudo-regret is **1/4 per round** or **1 over four rounds** under these assumptions. A realized four-round reward sequence is random and is **not** required to total its expectation. A learner's exploration schedule, empirical arm estimates and untried actions must be recorded to support any additional claims.

**T1 — Sequential TD and tabular control arithmetic.** Reuse M1 with V(S)=V(B)=0 and TD(0) step size α=1/4, visiting S–Go/r0–B–Finish/r4–T **twice in the same order**, updating immediately after each transition. On episode 1 the S update leaves V(S)=0 and the B terminal update gives V(B)=1. On episode 2, the S TD target is (1/2)1=1/2 and its update gives **V(S)=1/8**; the B target is 4 and B updates to **V(B)=7/4**. For a **separate** Q-learning trace, Q initially zero and α=1/2: on episode 1 the S–Go update stays 0 and B–Finish becomes **2**; on episode 2 S–Go becomes **1/2** and B–Finish becomes **3**. Explain why these finite learning traces do **not** equal the optimal M1 values yet. For SARSA using a different actually sampled next action at B, the target uses that action's Q, not max Q; give one independently calculated contrasting action-value fixture.

**D1 — Deep Q target and terminal/truncation mask.** On a nonterminal S–Go/r0–B transition with gamma=1/2, a separate, temporarily fixed target network reports Q_target(B,Finish)=4 and Q_target(B,Wait)=3, so the correct DQN target is **2**. If the same reward-0 transition is truly terminal, target=**0**. If an exogenous *data-collection* time limit truncates a continuing MDP at B, the continuation bootstrap remains **2** when B is the valid final observation and the time limit is not modeled as a task terminal; treating truncated=True as terminated=True and forcing zero would be incorrect. Conversely, if the finite-horizon task explicitly ends at a time limit, that is a genuine horizon transition and time-to-go must be modeled appropriately. The Q target has no gradient path through the fixed target network. No sampled deep-Q training run is guaranteed to converge to these figures absent a matching fixed model and weights.

**P1 — Bounded stochastic policy-gradient update.** At one state, let the stochastic policy choose A with pθ(A)=sigmoid(θ), B otherwise; start θ=0 so p(A)=1/2. A sampled A has return 1 and baseline b=0; the derivative of log pθ(A) with respect to θ is 1−p(A)=**1/2**. Under the explicitly specified *one-sample gradient ascent update* θ_new=θ+α(R−b)∇θlogp(A) with α=1/5, θ_new=**1/10**. A sampled B would have derivative −p(A)=−1/2, not +1/2. This is one sampled gradient estimate, not a proof that a policy or baseline will improve every individual rollout. For an actor–critic trace, identify the actor/critic parameter sets and separately independently derive the chosen critic target and advantage.

**P2 — Partial-observation belief update.** A hidden binary fault F has prior P(F=1)=1/5. A synthetic positive sensor reading + has likelihood P(+|F=1)=4/5 and P(+|F=0)=1/5. Then P(+)= (1/5)(4/5)+(4/5)(1/5)=**8/25**, and P(F=1|+)=((1/5)(4/5))/(8/25)=**1/2**. An observation is not the hidden fault, and the updated belief is a model-dependent posterior; an additional action/time step requires a declared transition kernel and observation update. This example reuses AI3's Bayes arithmetic as an input to a *sequential belief-state* problem, not a separate generic probability prerequisite.

**P3 — Offline bandit importance-weight failure.** A logging policy b(A)=1/4, b(B)=3/4 generates two records: (chosen A, reward 1, logged propensity 1/4) and (chosen B, reward 0, logged propensity 3/4). Target π always chooses A, so importance ratios π(a)/b(a) are **4** and **0**. The **ordinary IPS average** (4·1+0·0)/2=**2**, even though individual rewards are in [0,1], illustrating a high-variance finite-sample estimate, not a feasible actual expected reward of 2. The **self-normalized** value is (4·1)/(4)=**1** on these two records, still highly uncertain and with its own bias. If behavior probability of A were zero while the target chose A, target-policy value is **not identified from these logs**; do not divide by zero, invent unsupported reward information or report a confidence guarantee. This is a **single-step logged bandit** case: extending it to MDP trajectories requires full history-dependent action ratios, reward timing and state visitation assumptions, not this single-step shortcut.

**C1 — Reward and action-constraint counterexample.** On a continuing synthetic state B with gamma=1/2, a repeated Wait yielding reward 1 forever has return 1+1/2+1/4+…=**2**. An immediate Finish yielding reward 4 has return **4**; this particular reward model favors Finish. Changing the proxy to reward 5 for Wait would instead give a repeated-Wait return **10**, even if a separately stated hard requirement demanded completion. The correct response is to identify the proxy failure and enforce the external feasibility/completion constraint rather than claim that value maximization certifies a safe outcome. Prohibited actions must be blocked before exploration; a learned value cannot authorize them.

**Evaluation and reproducibility rules.** A learner may use equivalent small synthetic fixtures if their mathematical conventions, finite expected answers, negative cases and reviewer variation remain public and independently inspectable. Record start-state distribution, exact transition/reward tables and policy probabilities, relevant behavioral logging, episode identity, action legality, true terminal and exogenous truncation conditions, update chronology, randomness and resource limits. Assessors may substitute bounded unfamiliar numeric cases while preserving the published outcome/evidence criteria. The final learning result is a **reported, reproducible observed measurement** with uncertainty and limitations, not a promised accuracy, episode count or global RL convergence theorem. No physical robot, cloud service, production permission, secret benchmark or expensive simulator can be compulsory.

### Required summative assessments

- **AI6-AS1** (finite MDP modeling, Bellman proof and exact dynamic programming)
  - **Outcomes:** AI6-O1, AI6-O2, AI6-O3, AI6-O4, AI6-O19.
  - **Work:** Define a bounded two-step or looping decision problem with full state/action/transition/reward/terminal/horizon and legal-action semantics. Independently verify M1 row normalization, compute its fixed-policy values and optimal action-values, trace two synchronous value-iteration backups, and justify a valid policy improvement. Modify a gamma, reward, transition probability or terminal condition and re-derive the expected result. Demonstrate an invalid transition row or omitted state variable and explain why a solver returning a value does not automatically make the result meaningful.
  - **Criteria:** M1 yields V*(S)=2, V*(B)=4, Q*(B,Wait)=3, policy Go/Wait values (1,2), V1=(1,4) and V2=(2,4) in S,B order. All numbers follow the declared reward timing and gamma=1/2; terminal T has no bootstrap. Exact-policy and optimal-policy claims state finite discounted conditions, and changed-case reasoning is independently derived rather than copied from code. Illegal transitions and missing state/horizon assumptions receive explicit error/unsupported outcomes.
  - **Evidence:** State and transition tables, Bellman derivations and exact independent oracle, verified legal paths/updated policies, source or complete hand calculation, normal and invalid/changed cases and bounded interpretation of optimality.

- **AI6-AS2** (bandit learning, exploration and constrained regret)
  - **Outcomes:** AI6-O5, AI6-O10, AI6-O18, AI6-O20.
  - **Work:** Derive B1 expected reward and regret before simulation. Implement or transparently trace an incremental sample-average bandit and two justified exploration methods (for example epsilon-greedy versus optimistic or upper-confidence exploration) on a finite synthetic stationary and one deliberately nonstationary case. Record actual arm counts/observed rewards and compare under identical reward stream or independently seeded and disclosed replicates, explaining what cannot be concluded from one sample. Add a prohibited arm and show that the exploration policy never executes it.
  - **Criteria:** B1 uniform expected reward 1/2, optimal expected 3/4 and expected regret 1/4 per step or 1 over four steps are correctly derived; realized returns are not forced to equal expectations. Arm estimates use correct counts or alpha, the exploration probability includes random selection of the greedy arm, and comparisons identify variance, nonstationarity and sample budget. An external hard action prohibition survives any high predicted reward.
  - **Evidence:** Expected-value derivations, seeded generators/arm histories, update trace and measured regret/coverage with counts, comparable experimental protocol, invalid/forbidden case and limitations/constraint report.

- **AI6-AS3** (trajectory collection, Monte Carlo and TD/trace updates)
  - **Outcomes:** AI6-O6, AI6-O7, AI6-O8, AI6-O19.
  - **Work:** Implement or inspect a bounded trajectory collector that records initial state, behavior probabilities, transition reward, successor, terminal and cutoff; calculate M1 full returns. Independently reproduce T1's sequential TD(0) two-episode trace and compare with a first-/every-visit Monte Carlo estimate on a repeated-state finite episode. Derive one explicitly described 2-step target and one accumulating-eligibility-trace update at an exact small state trajectory; vary gamma/alpha/lambda or the terminal flag and predict the corrected numbers before execution. Demonstrate why a time-limit truncation of a continuing process cannot always be substituted for a natural terminal.
  - **Criteria:** M1 returns 2 at S and 4 at B; T1 TD produces V(S)=1/8 and V(B)=7/4 after the specified two episodes, with correct online ordering. A 2-step and trace calculation follows its own documented recurrence and initial values, and a repeated state is treated differently by first- and every-visit MC under the declared policy. The collector rejects illegal/missing data, preserves episode boundaries, and never blindly zeros continuation at all truncated observations.
  - **Evidence:** Hand-derived returns/TD/traces, local source and actual transition record, independently checked normal and malformed/cutoff variants, seed/episode contract and explanation of sampling/bootstrapping limitations.

- **AI6-AS4** (tabular SARSA/Q control and policy coverage)
  - **Outcomes:** AI6-O9, AI6-O10, AI6-O18, AI6-O19.
  - **Work:** Build a small tabular learner supporting legal-action epsilon-greedy selection, SARSA (sampled next action) and Q-learning (greedy target). Independently verify T1's two-episode Q-learning arithmetic; construct a next-state choice where the behavior selects a lower-Q action and show SARSA's different numerical target. Include correct terminal and exogenous cutoff handling, a deterministic tie policy, an unsupported action and an explicit low-coverage state. Compare learned policies against M1's exact known optimum and a fixed/random baseline with actual independently seeded evaluation runs.
  - **Criteria:** The Q-learning trace produces first B–Finish Q=2, then S–Go=1/2 and B–Finish=3 under the specified order; SARSA uses actual next action value and Q-learning uses max among legal actions, neither arbitrary future estimates. Invalid actions are unavailable to both exploration and maximization; finite sample and constant alpha do not claim exact convergence. Evaluation episodes are isolated from exploration/training decisions.
  - **Evidence:** Independent Q update calculations, local source/policy logs, correct and deliberately defective successor-action traces, terminal/truncation test, actual seeded performance/coverage and bounded comparison to exact optimum.

- **AI6-AS5** (approximate values and bounded deep Q stabilization)
  - **Outcomes:** AI6-O11, AI6-O12, AI6-O19, AI6-O21.
  - **Work:** Derive a small feature-based value prediction and one semi-gradient TD update, then implement a tiny CPU-only Q network with distinct online and target computations, finite replay buffer, reproducible action encoding and proper legal-action/bootstrap masks. Independently check D1 nonterminal, terminal and exogenous cutoff targets, verify target values are not in the trainable gradient path, and compare two actual configurations involving replay/target lag or an explicitly constructed stale/unstable target case. Test wrong shape, invalid replay transition, unsupported action and CPU budget failure with explicit dispositions.
  - **Criteria:** D1 target is 2 for nonterminal, 0 for true terminal, and 2 for an exogenous cutoff where the continuing-state value is legitimate; a finite-horizon true end is handled as a different model. Target-network gradients do not silently update; tensor/action dimensions and replay provenance are correct. A function-approximation divergence risk is explained under the proper off-policy/bootstrap/approximation interaction rather than asserted to occur on every run. Learning outcomes are actual reproducible observations and no GPU is required.
  - **Evidence:** Feature/Q exact oracle, model and replay schema, training source and parameter/gradient trace, seeded measured comparison, negative masks/invalid action or budget case, CPU resource report and instability limitations.

- **AI6-AS6** (stochastic policy gradients and actor–critic mechanisms)
  - **Outcomes:** AI6-O13, AI6-O14, AI6-O18.
  - **Work:** Derive P1's categorical-logistic policy gradient and one-sample ascent update independently, including contrasting sampled B and state-baseline conditions. Implement a small stochastic policy and a bounded actor–critic or equivalent inspectable policy/value scheme with correctly separated actor and critic targets, state/return handling, log-probability/advantage weighting and honest on-policy data collection. Diagnose a wrong log sign, detached log probability, stale rollout policy or critic target error. Compare actual seeded returns, action coverage and update/variance behavior with an appropriate fixed or tabular reference.
  - **Criteria:** P1 derivative for sampled A is 1/2 and θ_new=1/10 at α=1/5; B has derivative −1/2. An action-independent baseline is not represented as changing the true expected gradient under valid assumptions; actor and critic gradients/updates use their declared objectives and separate parameter ownership. A changed-policy rollout is not silently reused as if on-policy. Observed stochastic results do not assert universal improvement or production fitness.
  - **Evidence:** Exact log-probability/parameter trace, source with distinct actor/critic state and sampled data provenance, independent negative-gradient check, measured policy comparison, failure example and statistical limitations.

- **AI6-AS7** (estimated dynamics, belief updates and planning failure)
  - **Outcomes:** AI6-O2, AI6-O15, AI6-O16, AI6-O20.
  - **Work:** Build a finite action-conditioned transition estimator from a small synthetic count table, contrast it with known M1 dynamics, calculate the changed expected Bellman target and inspect one model-based or Dyna-style simulated update. Independently derive P2 sensor evidence probability and posterior, then show one belief-state or missing-observation case whose action should change or be held due to uncertainty. Demonstrate a model error/unsupported transition or forbidden action and explain why an imaginary rollout is not a new independent real experience.
  - **Criteria:** Estimated dynamics/CPD rows are normalized and state-action sampling coverage is disclosed; P2 gives P(+)=8/25 and posterior fault probability 1/2 with declared likelihoods. Any model-based value claim identifies whether a transition was known, sampled or estimated, and documents uncertainty and compounding model error. An observation is not equated with the hidden state, and no real-world actuation, safety permission or causal certainty is inferred from the synthetic posterior.
  - **Evidence:** Model/count tables, independently checked one-step planning and Bayes calculations, observed/simulated trace with explicit provenance, negative unsupported/unreliable-state case and bounded model/safety analysis.

- **AI6-AS8** (off-policy logged evaluation, sequential protocol and safety)
  - **Outcomes:** AI6-O6, AI6-O10, AI6-O17, AI6-O18, AI6-O19, AI6-O20.
  - **Work:** Explicitly distinguish logging behavior policy and target policy; derive P3's ordinary and self-normalized importance-weighted estimates, explain why the ordinary result may exceed the reward range on a finite sample, and produce a support-violating target example with correct nonidentifiability response. Derive a small two-step trajectory likelihood ratio from published per-step policy propensities, explaining why multiplying ratios and handling state-dependent histories matters. Compare offline estimates (with visible limitations) and actual direct simulation evaluation on a separate supported synthetic task. Diagnose reward hacking using C1, forbid unsafe exploration, and test a terminated versus truncated episode with correct bootstrap, failure and stop/review conditions.
  - **Criteria:** P3 ratios 4/0 yield IPS 2, SNIPS 1, both explicitly qualified by two-log high variance/possible bias and **neither** called the true value. Behavior support zero for a target action causes an unidentifiable logged counterfactual, not a numeric division workaround. Multi-step importance weights reflect the target/behavior ratios along each *actual* history and reward timing, and no result asserts a guarantee without support and sampling assumptions. C1 yields Wait value 2 at reward1, changed proxy Wait value10 at reward5 versus Finish4 while hard completion constraints remain binding. Invalid acts are blocked before policy scoring.
  - **Evidence:** Behavior/target propensity tables, independent IPS and sequential-ratio arithmetic, local valid/missing-support fixtures, independently seeded supported-policy comparison, documented termination/truncation and reward-proxy negative tests, uncertainty and hard-constraint report.

- **AI6-AS9** (integrated local sequential agent and unfamiliar technical defense)
  - **Outcomes:** AI6-O1, AI6-O18, AI6-O19, AI6-O20, AI6-O21, AI6-O22.
  - **Work:** Consolidate and reuse legitimately assessed AI6-AS1–AS8 code, explanations and reference fixtures in **one coherent learner-owned local experiment**, not nine independent full-scale projects. Select one finite/synthetic environment with a clear observation/transition/reward and safe legal-action contract; choose an appropriate tabular or small neural learning method, compare against an exact/deterministic or fixed-policy baseline with fresh seeded evaluation, and publish actual sample/resource budgets, return/constraint statistics and independent normal and negative oracles. The reviewer supplies one unfamiliar bounded change (reward sign/scale, transition probability, terminal/cutoff policy, legal action, behavior propensity, observation likelihood or evaluation starting distribution). Before executing, calculate the expected changed return/update where identifiable, or state precisely why missing evidence prevents one. Then implement a verified repair or safe refusal and explain how the previous unaffected contract remains tested. Provide individually attributable technical defense by accessible text, recording or review.
  - **Criteria:** An independent reviewer can reproduce observed results from clean synthetic inputs without GPU, private service, purchased data or unspecified grader. Source tests check actual states, rewards, policy probabilities, bootstrap masks, legal actions and resource limits independently from the learner under test; training and evaluation episodes/policies are separated. The unfamiliar case has a correct independent expectation or justified nonidentifiability decision and a verified response. No production, hardware-safety, causal, universally optimal or unearned transfer claim passes. Prior specialist outcomes require their *own actual* AI6-AS1–AS8 evidence, not generic inclusion in the final repository.
  - **Evidence:** One versioned and independently executable source/evidence collection, environment/model and policy contracts, exact small oracles, traces and actual results for chosen baseline/learner, seed/CPU/interaction records, normal/adverse/unfamiliar cases, limitations and independently inspectable individual defense.

### Required outcome-to-assessment coverage

| Required outcome | Summative evidence |
| --- | --- |
| AI6-O1 | AI6-AS1, AI6-AS9 |
| AI6-O2 | AI6-AS1, AI6-AS7 |
| AI6-O3 | AI6-AS1 |
| AI6-O4 | AI6-AS1 |
| AI6-O5 | AI6-AS2 |
| AI6-O6 | AI6-AS3, AI6-AS8 |
| AI6-O7 | AI6-AS3 |
| AI6-O8 | AI6-AS3 |
| AI6-O9 | AI6-AS4 |
| AI6-O10 | AI6-AS2, AI6-AS4, AI6-AS8 |
| AI6-O11 | AI6-AS5 |
| AI6-O12 | AI6-AS5 |
| AI6-O13 | AI6-AS6 |
| AI6-O14 | AI6-AS6 |
| AI6-O15 | AI6-AS7 |
| AI6-O16 | AI6-AS7 |
| AI6-O17 | AI6-AS8 |
| AI6-O18 | AI6-AS2, AI6-AS4, AI6-AS6, AI6-AS8, AI6-AS9 |
| AI6-O19 | AI6-AS1, AI6-AS3, AI6-AS4, AI6-AS5, AI6-AS8, AI6-AS9 |
| AI6-O20 | AI6-AS2, AI6-AS7, AI6-AS8, AI6-AS9 |
| AI6-O21 | AI6-AS5, AI6-AS9 |
| AI6-O22 | AI6-AS9 |

**Completion decision.** All 22 outcomes require satisfactory individually reviewable evidence through the nine assessments under the correct source revision. Many assessments may reuse one codebase or one trajectory/oracle when that evidence truly tests multiple distinct skills. The course cannot be completed by attendance, elapsed week count, mere experiment submission, an opaque deep learning checkpoint, a library printout or reward maximization without proof of task legality and reviewable method. A formative exercise or optional university resource cannot become an undocumented graduation threshold. Reviewers must distinguish theoretical guarantees for a mathematical fixture, stochastic observations under tested seeds, learner-independent reproducibility and claims that remain unsupported. Source validation and successful CI do **not** promote this draft's educational readiness.

### Optional open academic and primary references

- [Reinforcement Learning: An Introduction, Sutton and Barto (MIT Press)](https://mitpress.mit.edu/9780262039246/reinforcement-learning/) — foundational Bellman, bandit, MC/TD, control, approximation and planning context; purchasing the book is not required.
- [OpenAI Spinning Up — Key Concepts in RL](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html) — policy/value/trajectory definitions and discounted returns.
- [OpenAI Spinning Up — Policy Optimization](https://spinningup.openai.com/en/latest/spinningup/rl_intro3.html) — policy-gradient and advantage identities, with assumptions.
- [UC Berkeley CS285 — graduate reinforcement learning course](https://www2.eecs.berkeley.edu/Courses/CS285/) — broad model-free, model-based and offline learning course coverage, not a mandate for equivalent course length/hardware.
- [PyTorch Deep Q Learning tutorial](https://docs.pytorch.org/tutorials/intermediate/reinforcement_q_learning) — neural target/replay handling as an optional reference implementation rather than a required environment.
- [Gymnasium — Handling Time Limits](https://gymnasium.farama.org/tutorials/gymnasium_basics/handling_time_limits/) — termination versus truncation and bootstrap implications; Gymnasium installation is optional.
- [Gymnasium Environment API](https://gymnasium.farama.org/introduction/basic_usage/) — reset/step and boundary semantics.
- [Deep Reinforcement Learning and the Deadly Triad](https://arxiv.org/abs/1812.02648) — research examination of instability from approximation, bootstrap and off-policy learning.

All listed references are supplemental. The published assessments and source contracts above are the full mandatory OEE learning and evaluation requirements; no paid or proprietary external curriculum is necessary.
