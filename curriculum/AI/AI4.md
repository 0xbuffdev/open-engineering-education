# AI4 — Machine Learning & Statistical Learning Theory

**Program:** AI — AI Engineering
**Type:** course
**Prerequisites:** [AI2](AI2.md) — Mathematics of Statistical and Neural Models (completed)
**Duration:** 20–26 weeks
**Status:** draft
**Specification:** v0.2.0
**Expected workload:** 10–15 focused hours/week (provisional; approximately 200–390 focused hours)

> [AI Engineering](README.md) · [Curriculum design guide](../DESIGN-GUIDE.md) · [Course format](../../spec/course-format.md) · [Evidence rules](../../spec/evidence-rules.md)

## Overview

**AI4 establishes statistical machine-learning competence: choosing a meaningful empirical question, constructing defensible classical learning baselines and model families, measuring their behavior under valid sampling conditions, and explaining why apparent improvement may fail to generalize.** A learner must independently reproduce fitted models, metric calculations and evaluation splits, then defend whether the observed evidence actually supports a model choice. The central question is not “Can the package fit the data?” but “What population claim can this experiment support, with which assumptions, failure modes and uncertainty?”

**Competency ownership and prerequisites.** Assessed [SEF10](../SEF/SEF10.md) completion closes the full SEF program. [AI1](AI1.md) assesses data contracts, reproducible scientific arrays, dataset transformations, provenance, leakage-resistant partitions and observation integrity. [AI2](AI2.md) establishes design matrices, likelihood, gradients, Bayesian updates, log loss, regularization, numerical stability and mathematical uncertainty. AI4 **applies and extends**, rather than re-teaches, those subjects to learner selection, statistical generalization, classical model families, calibrated prediction, resampling and reproducible comparison. [AI3](AI3.md) is an independent classical search/reasoning branch and is **not** a prerequisite for AI4; neither APP nor SYS is required here.

**Boundaries with later courses.** AI5 owns computational graphs across deep neural architectures, representation learning and full neural training; AI7 owns NLP and information retrieval; AI8 owns computer vision and multimodal evaluation; AI9 owns transformers/generative models; AI13 owns system-level AI evaluation, adversarial/reliability testing and production-facing evaluation governance. AI4 teaches rigorous **statistical evaluation of bounded, classical models** rather than those domain-specific systems. Neural networks can be mentioned as a contrasting hypothesis class but are not a required architecture, model API, PyTorch project or GPU prerequisite. AI6 sequential decision/RL, AI19 causal inference and AI20 graph representation learning also retain separate specialist competencies. A data-driven correlation or subgroup gap here is not evidence of a causal mechanism or an independently demonstrated responsible-AI program.

**Teaching and engineering environment.** Public synthetic or appropriately licensed small datasets are sufficient. A local CPU-based Python 3 environment with NumPy, pandas and scikit-learn (or transparent language/library equivalents) supports practical experiments; learners must reproduce small reference cases with hand calculations or independent miniature code, not merely trust estimator outputs. Pure standard-library derivations are accepted when they demonstrate the same assessed mechanism. Explicit package version, random seeds, preprocessing fit boundary, fold identifiers, score orientation and decision thresholds must accompany numerical claims. No GPU, cloud credit, paid platform, private data, hidden benchmarking dataset or remote LLM inference is compulsory. All figures need accessible tables/text equivalents. No real-world automated decisions on consequential cases are required.

**Course structure and honest evidence.** Twelve conceptually distinct stages connect empirical modeling, hypothesis selection, generalization, evaluation and error investigation. Closely related fit-boundary checks, negative cases and verification steps are taught with the mechanisms they test rather than repeated as separate lessons. Eight required summative assessments reuse a versioned evidence portfolio and award **21 independently reviewable outcomes**. Some assessments use compact exact fixtures; broader model comparisons use bounded seeded experiments where numeric results depend on a learner's environment and data-generation choices. Such experimental outcomes must be reported as observed, never invented or imposed as universal numeric targets. An unfamiliar reviewer variation checks whether the learner can revise a workflow without leaking the test set or overclaiming performance. Time is provisional; educational status remains draft until authentic learner/reviewer evidence warrants revision.

## Learning outcomes

- **AI4-O1:** Specify a bounded supervised or unsupervised learning question with population, sampling unit, target semantics, feasible decisions, cost of error, fit/evaluation boundary and unsupported claims.
- **AI4-O2:** Construct meaningful constant, prevalence, heuristic and transparent parametric baselines using only information available at the correct fitting boundary, then justify the strength and limitations of each comparison.
- **AI4-O3:** Fit, interpret and independently check small regression and probabilistic classification models, including coefficient/intercept conventions, objective behavior, residual/decision evidence and invalid-input cases.
- **AI4-O4:** Construct and evaluate instance-based and probabilistic classical classifiers, diagnosing distance scaling, neighborhood choices, likelihood independence assumptions, smoothing and distributional failure.
- **AI4-O5:** Build and analyze classification/regression trees with explicit split/impurity, leaf, stopping and pruning rules; explain instability, memorization and limits of apparent interpretability.
- **AI4-O6:** Implement or rigorously inspect bagging, random forests and additive boosting on bounded datasets, distinguishing bootstrap/feature randomness, sequential fitting, out-of-bag limits and overfitting.
- **AI4-O7:** Explain and compare maximum-margin and kernel methods with correct geometric assumptions, regularization, support-vector/feature-space behavior and computational or interpretability limitations.
- **AI4-O8:** Engineer and select model-specific representations with training-only transformations and appropriately fitted preprocessing, diagnosing feature leakage, unstable encodings, missingness and dimensionality trade-offs.
- **AI4-O9:** Formulate empirical versus expected risk, hypothesis-class complexity and inductive bias, distinguishing optimization of a finite training sample from defensible prediction on an intended population.
- **AI4-O10:** Derive and interpret a small valid finite-hypothesis uniform-convergence argument or concentration bound under explicit sampling/bounded-loss assumptions; identify cases where its guarantee does not apply.
- **AI4-O11:** Diagnose bias, variance, irreducible uncertainty and overfitting/underfitting using controlled experiments and regularization/complexity changes without treating a single learning curve as proof.
- **AI4-O12:** Design train/validation/test, grouped, temporal, cross-validation and nested selection protocols with correct unit-of-independence and fold-specific fitting, stating when a particular protocol fails.
- **AI4-O13:** Detect and correct train/test contamination, target-dependent transformations, cross-fold leakage, tuning on final evaluation, repeated-selection bias and a violated data-generating assumption.
- **AI4-O14:** Independently compute, interpret and select regression/classification metrics under class imbalance and consequential error costs, including explicitly undefined metric cases and aggregation conventions.
- **AI4-O15:** Evaluate probabilistic scores, empirical calibration, action thresholds and cost-sensitive choices using independent checks, distinguishing score ranking from reliable probabilities and deployment authorization.
- **AI4-O16:** Perform systematic error and subgroup/shift analysis with denominators, uncertainty, sparse-group limitations and counterexamples, distinguishing measured disparity from a causal or operationally safe conclusion.
- **AI4-O17:** Compare candidate models with fair data/metric protocols, fold-level variability, selection uncertainty, resource accounting and bounded claims rather than an unexplained leaderboard.
- **AI4-O18:** Formulate, fit and investigate bounded clustering models with distance/objective assumptions, initialization effects, cluster labeling ambiguity and external-validation limitations.
- **AI4-O19:** Calculate and interpret basic principal-component or singular-value-based dimension reduction with correct centering, projection, explained-variance and data-dependent-fit rules, including a degenerate case.
- **AI4-O20:** Produce clean-state executable and independently checkable statistical-ML evidence with versioned fixtures, baseline/model contracts, reproducible folds, negative controls, model reporting and honest limitations.
- **AI4-O21:** Investigate an unfamiliar bounded learning/evaluation defect or changed sampling requirement, independently predict its effect, repair or safely decline an invalid claim and defend the decision.

## Modules

### Module 1 — Statistical Learning Questions and Evidence Contracts

#### Outcomes

- AI4-O1
- AI4-O2
- AI4-O9
- AI4-O20

#### Lessons

1. **From statistical learning to a reproducible prediction contract** — Connect estimation and empirical-risk minimization to classical predictive methods: linear models, nearest neighbors, trees and ensembles offer distinct assumptions for forecasting, inspection or triage, while unsupervised structure is not a verified class label. Extend an AI1-qualified table into a defensible task by naming observation unit, prediction time, target source, permitted features, split and seed versions, CPU environment, evaluation metric and population limits. Separate independently checked numerical expectations from measured model performance; a fitted score does not establish causation or safe deployment.
2. **Population, sampling and risk** — Distinguish observed rows from independent sampling units and the intended deployment population, including repeated entities and time dependence; connect empirical training loss to target-population risk without treating the observed sample minimum as a proven population result. State which sampling/selection assumptions would have to hold.
3. **Learning task taxonomy** — Distinguish regression, binary/multiclass classification, unsupervised description and a downstream decision; specify which labels are truly observed and which are assumptions.
4. **Measurable baseline and decision consequence** — Define a baseline a learner could actually beat, including no-change, majority, training-mean and appropriate deterministic heuristics; clarify what a score cannot tell a decision-maker.
5. **Permitted information at inference time** — Challenge a model that uses a future event, fold-wise aggregate, identity leakage or a target-derived feature that would not exist when making a real prediction.

*Optional feedback:* For a repeat-customer dataset, distinguish row count from customer count and explain which unit a new-customer generalization claim requires.

### Module 2 — Regression and Generalized Linear Classification

#### Outcomes

- AI4-O2
- AI4-O3
- AI4-O8
- AI4-O14

#### Lessons

1. **Constant and simple linear baselines** — Compute a train-only mean predictor and compare it with a fitted linear response; a perfect fit on the same observations is not held-out validation.
2. **Fitted coefficients, residuals and independent checks** — Apply AI2's linear objective to an actual bounded regression fit; independently verify predictions and residual structure, distinguish intercept and slopes under declared feature units, and diagnose scaling, collinearity and extrapolation limits without repeating the full gradient derivation.
3. **Regularized linear models** — Compare unpenalized, ridge and sparse-penalty alternatives while controlling feature scaling, held-out selection and intercept handling; do not repeat AI2's full gradient derivation.
4. **Logistic probabilities, thresholds and the baseline** — Convert a binary linear score to a conditional probability under a declared link, compare with training prevalence, and distinguish a fitted score/probability, log loss and a separately justified decision threshold. Do not treat the package's default hard label as the decision objective or claim calibration merely from optimization.
5. **Coefficient strength and uncertainty limits** — Explain why coefficient magnitude, predictive value, correlation and causal effect are distinct; record unstable estimates under correlated predictors.
6. **Multiclass softmax/one-vs-rest interpretation** — Clarify label support, mutually exclusive categories, score normalization and difference between probability vectors and uncalibrated margins.
7. **Failure/diagnostic comparison** — Inspect outliers, nonlinear misspecification, separated classification, class imbalance and invalid/missing feature input without giving a general model preference unsupported by evidence.

### Module 3 — Instance-Based and Probabilistic Classical Learners

#### Outcomes

- AI4-O4
- AI4-O2
- AI4-O8
- AI4-O17

#### Lessons

1. **Nearest neighbors, scaling and distance semantics** — Independently calculate Euclidean/Manhattan distances, nearest-neighbor labels and deterministic ties on a declared feature space. Show how one high-range feature can dominate distance, and fit any learned centering/scaling on training data alone; a correct distance calculation with a leaked transform is not a valid holdout prediction.
2. **Neighborhood size as inductive bias** — Compare k=1, small odd k and a large k; explain sensitivity to noise, smoothness and class prevalence instead of claiming one k is optimal everywhere.
3. **Nearest-neighbor regression and costs** — Explain weighted/unweighted neighbor aggregation, memory and query cost, extrapolation limitations and when data volume changes feasibility.
4. **Generative versus discriminative learning** — Contrast modeling class-conditional feature likelihoods and priors with learning a direct decision boundary; state what assumptions each estimate requires.
5. **Naïve Bayes conditional independence** — Calculate a finite categorical likelihood product and posterior ranking, then build a correlated-feature counterexample where multiplication exaggerates evidence.
6. **Smoothing and unseen categories** — Compare zero-count likelihood with a documented additive-smoothing rule on a small frequency table and explain why the smoothing choice alters predictions.
7. **Comparable model-family experiment** — Evaluate a baseline, a neighbor method and a probabilistic classifier on one valid split, reporting the exact feature contract, failure cases, performance and resource use.

### Module 4 — Decision Trees and Ensemble Methods

#### Outcomes

- AI4-O5
- AI4-O6
- AI4-O8
- AI4-O11

#### Lessons

1. **Recursive partitioning as a model** — Explain how a tree divides feature space into leaves and why axis-aligned boundaries differ from a linear hypothesis.
2. **Classification impurity and information gain** — Compute Gini/entropy reductions on a tiny labeled set with explicit parent/child sample counts and reject a split that does not improve the declared objective.
3. **Regression tree splitting** — Calculate within-leaf squared-error reduction for a small numerical target, comparing leaf means with an independently derived baseline.
4. **Stopping, pruning and overfit diagnosis** — Compare depth, leaf size, rare/categorical branches, missing values and appropriate validation-based pruning. Reproduce one deliberately memorizing tree or noise-sensitive configuration and explain why an improved training impurity/accuracy does not establish better held-out performance. Preserve the distinct objective of conditional stopping and leaf reliability.
5. **Pruning and feature importance caveats** — Relate complexity pruning to validation evidence; explain why impurity-based feature importance may be biased by high-cardinality predictors and is not causal.
6. **Bootstrap sampling and bagging** — Derive a bootstrap sample with repeated/omitted original indices and explain how individual-tree variability can be reduced by aggregation.
7. **Random forests** — Explain additional feature randomness, dependence among trees, out-of-bag prediction eligibility and why a sample absent from one tree is not necessarily out-of-bag for a forest-level score.
8. **Additive boosting as sequential correction** — Trace one or two small stage-wise updates on residuals or negative gradients, identifying learning rate, weak learner capacity and holdout-dependent stopping.

### Module 5 — Large-Margin Learners and Kernel Methods

#### Outcomes

- AI4-O7
- AI4-O9
- AI4-O11
- AI4-O17

#### Lessons

1. **Geometric separating hyperplane** — Compute signed distance and decision-side convention for a small labeled 2D dataset; distinguish a margin from a predicted probability.
2. **Hard-margin assumptions** — Construct a separable one-dimensional example and explain why an infeasible/nonseparable dataset invalidates a hard-margin formulation.
3. **Soft margin and hinge loss** — Trace margin violations and regularization trade-offs, comparing a small parameter norm with classification errors and an independent count of violations.
4. **Support vectors and decision influence** — Identify points at or inside the relevant margin in a simple example; explain why changing non-support points may or may not affect the fit under specific conditions.
5. **Kernels and similarity matrices** — Explain a positive-semidefinite Gram matrix and how a kernel can implicitly represent nonlinear boundaries without explicitly building a vast feature vector.
6. **Kernel choice and computational scaling** — Compare linear and radial-basis similarity conceptually, state hyperparameter/scale assumptions and inspect kernel-matrix memory costs.
7. **Separation, calibration and failure modes** — Explain why SVM decision-function magnitude is not automatically a probability; document effects of outliers, unscaled dimensions and poorly selected kernels.

### Module 6 — Statistical Learning Theory and Generalization

#### Outcomes

- AI4-O9
- AI4-O10
- AI4-O11
- AI4-O17

#### Lessons

1. **Empirical risk minimization under assumptions** — Define a finite hypothesis class, bounded loss, iid sampling process and the empirical-risk minimizer; state what the training minimization does and does not guarantee.
2. **Training and generalization gaps** — Build a small example where selection improves empirical risk but worsens held-out risk; distinguish selection from estimating fixed-hypothesis performance.
3. **Hoeffding for a precommitted hypothesis** — Apply a valid bounded independent-loss concentration inequality, distinguishing probability over draws from an observed model's posterior certainty.
4. **Finite-class union bounds and sample complexity** — Extend a fixed-hypothesis Hoeffding guarantee to a predeclared H-hypothesis class with a union bound; independently evaluate the public n=100, H=10 confidence fixture, explaining how hypothesis count and sample size change the bound. State why adapting the class after inspecting evaluation outcomes invalidates this simple argument, and why a loose bound does not establish that a particular learner fails.
5. **Bias, variance and irreducible error** — Decompose expected squared prediction error under explicit squared-loss assumptions, and distinguish this statement from a universal decomposition for any loss/classification problem.
6. **Inductive bias and approximation capacity** — Compare an overly restrictive line, an unstable high-degree polynomial or deep tree, and a constrained learner under matched data generation and honest resampling.
7. **Learning curves and effective sample count** — Interpret training/validation gaps, fit instability and repeated observations; show why more rows of the same person need not supply independent evidence.
8. **Guarantee boundary audit** — Identify where dependence, distribution shift, unbounded losses, label noise or data-driven repeated selection breaks a claimed numerical or asymptotic guarantee.

### Module 7 — Feature Representations and Model Selection Inputs

#### Outcomes

- AI4-O8
- AI4-O11
- AI4-O12
- AI4-O13

#### Lessons

1. **Domain features and time-of-information** — Separate legitimate predictors from post-outcome metadata, proxies for the label and attributes with unavailable inference-time values.
2. **Fold-safe fitted preprocessing, including unsupervised transforms** — Learn imputation, means, scales and any PCA or related data-dependent transform on training observations only, separately for every fold. Apply the frozen state to validation/test; demonstrate how even pooled label-free scaling or PCA contaminates an out-of-sample score, and distinguish this from permissible deterministic feature functions.
3. **Categorical encoding and unseen values** — Design one-hot, ordinal and bucket encodings with fixed fit-time category vocabulary and explicit handling for novel inputs.
4. **Learned polynomial and interaction features** — Introduce controlled expressive features for a baseline while reporting dimensionality and the additional hypothesis complexity.
5. **Selection with the target is model fitting** — Show why univariate target-based feature selection on all folds leaks evaluation labels even when the downstream estimator appears to be correctly cross-validated.
6. **High-cardinality encodings and target statistics** — Explain why target encoding requires fold-safe or cross-fitted construction and why a unique identifier can misleadingly act as an easy feature.
7. **Auditable fold-safe pipelines and ablation** — Construct a preprocessing-plus-model pipeline and inspect fit calls, learned state and fold identities to ensure no held-out information influenced a training decision. Remove a suspect feature or representation under the same valid comparison protocol, and interpret a small observed score difference as bounded evidence rather than a universal improvement.

### Module 8 — Resampling, Cross-Validation and Leakage-Safe Selection

#### Outcomes

- AI4-O12
- AI4-O13
- AI4-O17
- AI4-O20

#### Lessons

1. **Train, development and final-test information boundaries** — Designate which records can fit weights, transformations, hyperparameters and thresholds, and reserve genuinely untouched data for final evaluation. Trace repeated manual test-set checks as adaptive fitting: after such reuse, the former test set is no longer an independent estimate, even if a model was never directly fit on its labels.
2. **k-fold cross-validation mechanics** — Draw a complete fixed-fold index table, train a new estimator and every learned transform per fold, and aggregate correctly across scores and fold sizes.
3. **Stratification and estimand caveats** — Explain why label-proportion balancing may be helpful for sparse classes but does not cure duplication, temporal dependence or selection bias.
4. **Group-preserving partitions and independent overlap checks** — Ensure every entity/group lies on one side of each validation boundary and justify which population the grouping approximates. Construct a deliberately changed grouping or duplicated-identity case, independently verify zero overlap after repair, and distinguish a no-overlap proof from sufficient population representativeness.
5. **Time-ordered evaluation and changed data availability** — Fit only on the past when predicting later observations, enforcing realistic label-availability windows, gaps or embargoes where justified. Inspect a shifted timestamp or unavailable future feature as an actual violation; repair the fold/feature contract without treating a chronology-respecting score as a guarantee under deployment shift.
6. **Hyperparameter search is part of fitting** — Compare simple grid/randomized selection on inner folds and identify how selecting the maximum of noisy validation scores introduces optimism.
7. **Nested cross-validation or separate untouched test** — Separate outer evaluation folds from inner tuning/threshold decisions, and explain what the outer estimate measures under a declared sampling scheme.
8. **Cross-validation uncertainty and small samples** — Report per-fold support and performance variability without pretending that correlated fold scores are independent draws or that a naïve standard error always gives valid coverage.

*Optional feedback:* Given repeated records for each customer, identify why a row-random 5-fold score is not evidence for a new-customer population and propose a group-aware alternative.

### Module 9 — Regression, Classification Metrics and Decision Costs

#### Outcomes

- AI4-O14
- AI4-O15
- AI4-O17

#### Lessons

1. **Regression losses and units** — Compute MAE, MSE and RMSE with the correct denominator and physical units; explain different outlier sensitivity and target distributions.
2. **R-squared and baseline interpretation** — Define total versus residual variation and explain when an R-squared result is undefined, poor or negative on a held-out set.
3. **Confusion matrix conventions** — Assign TP, FP, FN, TN to a named positive class with explicit prediction threshold and independently reproduce the class counts.
4. **Precision, recall, specificity and prevalence** — Derive the ratios and show why prevalence and differing error costs can make accuracy an inadequate primary measure.
5. **F-scores, class aggregation and undefined cases** — Compute F1 and macro/micro/weighted variants with explicit class support, frequency weighting and declared zero-division conventions. Demonstrate zero predicted positives or a missing class without silently substituting a valid precision or recall where it is mathematically undefined.
6. **Ranking metrics, base rates and degenerate samples** — Contrast ROC-AUC and precision-recall summaries, score ranking and threshold choices under rare positives. Explain why a one-class evaluation makes standard ROC-AUC undefined and why low-support samples or tiny subgroups cannot support confident comparisons; do not replace absent evidence with an invented score.
7. **Probability and scoring rules** — Compare log loss and Brier score with the hard-label decision, including zero-probability and clipping/precision conventions.
8. **Threshold choice on valid data** — Derive a simple expected-value decision threshold from explicit costs/probabilities and choose it using training/validation evidence, not by optimizing the reported test set.

### Module 10 — Calibration, Error Analysis, and Robust Claims

#### Outcomes

- AI4-O14
- AI4-O15
- AI4-O16
- AI4-O17
- AI4-O20

#### Lessons

1. **Calibration, ranking and proper-score interpretation** — Distinguish ranking quality, calibrated population probabilities and threshold-dependent accuracy; compare Brier and log loss as proper probabilistic scores whose values reflect more than calibration alone, including error severity and uncertainty. Explain why improving a score need not improve an action under a different error cost and why an optimized loss alone does not certify calibration.
2. **Reliability tables and binning** — Compute within-bin observed frequencies and mean predicted probabilities on a small labeled set; label bin choice and small-sample variability.
3. **Post-hoc calibration without contamination** — Fit Platt/logistic or isotonic calibration on appropriate disjoint or cross-validated training data and assess against an untouched evaluation partition; do not claim calibration on the fitting records.
4. **Structured error taxonomy** — Categorize false positives/negatives and large residuals by meaningful task-specific failure families rather than listing anecdotes or assuming independent subgroup membership.
5. **Subgroup denominators and sparse cells** — Report confusion and performance with actual group counts, disclose absent/underrepresented groups and avoid global disparity or fairness certification from tiny samples.
6. **Shift diagnosis** — Distinguish covariate shift, prior/base-rate changes and concept/label changes with transparent synthetic experiments; state that a simulated shift is not a verified deployment environment.
7. **Sensitivity and negative controls** — Vary random seed, train size, regularization or an irrelevant feature under a fair protocol, recording the actual behavior and explaining what remains untested.
8. **Honest model report** — Document task, sample and split boundaries, intended use, metrics and uncertainty, failure populations, relevant access/privacy limits and explicit non-causal/nonproduction claims.

### Module 11 — Clustering and Unsupervised Representation Analysis

#### Outcomes

- AI4-O1
- AI4-O18
- AI4-O19
- AI4-O8
- AI4-O20

#### Lessons

1. **Unsupervised question and permitted fit scope** — Distinguish exploratory similarity-driven grouping from supervised prediction; define the observations, feature units, distance, intended interpretation and authorized fit/evaluation partition. If cluster assignments are used as downstream features, show why fitting the clustering model on final-test records contaminates the claim.
2. **k-means objective and updates** — Compute assignments and centroids on a small point set, examine empty clusters and identify sensitivity to starting centroids and k.
3. **Cluster validation and label ambiguity** — Explain that cluster IDs can be permuted without changing the partition; distinguish inertia, silhouette-type evidence and external task truth.
4. **Alternative clustering biases** — Contrast density-based, hierarchical and centroid methods on unequal-density, elongated or noise-contaminated synthetic examples; explain one family for which k-means is a poor fit.
5. **Centering and covariance for PCA** — Derive sample mean and covariance for a two-feature small matrix, and check the chosen sample versus population normalization explicitly.
6. **Principal components, reconstruction and fold-safe transformation** — Solve a small centered covariance eigenproblem, identify eigenvector sign ambiguity, compute a one-dimensional projection and its reconstruction error. Fit the centering and PCA directions using only permitted training records or each training fold, and explain why pooled held-out information can change the chosen projection.
7. **Explained variance, degeneracy and limited comparison** — Handle zero-variance columns, repeated eigenvalues and nonunique principal directions; compare a justified PCA/clustering feature representation with a baseline using valid fit boundaries. A favorable finite metric or plotted cluster is not a new verified semantic label or a guarantee of downstream generalization.

### Module 12 — Integrated Empirical Study and Unfamiliar Defense

#### Outcomes

- AI4-O1
- AI4-O2
- AI4-O12
- AI4-O13
- AI4-O14
- AI4-O15
- AI4-O16
- AI4-O17
- AI4-O20
- AI4-O21

#### Lessons

1. **One bounded question and predeclared comparison protocol** — Choose a small public/synthetic regression or classification task with explicit observation units, intended population, chronology/group restrictions, information availability, error costs and ethical limits. Define the training-only baseline, at least two substantively different classical candidate families, preprocessing, permitted tuning budget, primary metric, thresholds where applicable and a genuinely untouched final evaluation before fitting.
2. **Clean independent execution** — Rebuild training-only preprocessing, candidate models, fold assignments and exactly reproducible commands from a new local environment.
3. **Independent comparisons, diagnostic evidence and action limits** — Report baseline and candidate models, genuine per-fold/effective-unit scores, CPU/fit costs, numerical and qualitative failures and appropriate uncertainty. Where probability estimates permit a decision, assess calibration and an independently justified threshold without tuning on the final test; otherwise document the reason to abstain. Use the same artifact for evidence already evaluated in earlier AI4 assessments rather than creating another mandatory project.
4. **Controlled ablation and negative control** — Change a suspect feature, dependency structure or hyperparameter under the valid selection protocol; record supported conclusions without test-set tuning.
5. **Unfamiliar reviewer modification** — Predict consequences of a new group, shifted prevalence, duplicate identity, changed error cost, unseen category, revised fold plan or compromised test feature and repair the pipeline or refuse false claims.
6. **Technical defense and handoff** — Reproduce the final artifact; defend assumptions, mathematical/statistical evidence, independent expected values, practical limitations, rejected alternatives and transfer under the reviewer variation.

Module exercises and informal checks are formative. They are **not** one mandatory quiz-plus-lab for every module; all compulsory evidence is specified by the eight summative assessments below.

## Completion requirements

### Shared public reference fixtures and explicit checking conventions

These compact synthetic fixtures make small mathematical, model, split and decision claims independently checkable. The learner may choose equivalent public fixtures when their hand-derived or independent reference answers, model assumptions and invalid cases are just as explicit. For model fit and generalization, a compact fixture demonstrates **mechanics only**; the empirical experiment must report honestly obtained out-of-sample scores on a separate valid sampling protocol.

**R1 — Regression training-fixture arithmetic, not a test set.** Inputs x=(0,1,2,3), observed targets y=(1,3,5,7). The training-target mean is 4, so a constant baseline on these **same fit records** has absolute errors (3,1,1,3), **MAE=2**, squared errors (9,1,1,9), **MSE=5** and **RMSE=sqrt(5)**. The affine model prediction 1+2x has zero residual on these fit records. No holdout or population claim follows. For any independent follow-up dataset, recompute the metrics on actual held-out targets and never refit the baseline mean using those target values.

**N1 — Nearest-neighbor trace.** Four one-dimensional training points are (x,label)=(0,0),(2,0),(8,1),(10,1), using absolute distance and no feature scaling. For query x=7, nearest neighbor is x=8 (label 1); with k=3 the sorted closest points are x=8, x=10 and x=2, so the majority label is 1. With k=4 the vote ties 2–2, so an explicitly declared tie policy must apply, or the learner must return a defined ambiguous result; the query is not ground truth for any unobserved target. For Naïve Bayes or another probabilistic learner, the learner must publish a similarly tiny class/likelihood table with independently calculated expected outputs and a zero-count or correlated-feature counterexample.

**T1 — Tree and bootstrap trace.** Eight labeled observations contain exactly four negatives and four positives, so the root's **binary Shannon entropy is 1 bit**. A hypothetical feasible split placing all four negatives in one child and all four positives in the other yields **weighted child entropy 0** and **information gain 1 bit** under that convention. Such a perfect split on one small training set is not proof of generalization. For a four-record bootstrap sample with drawn indices (0,0,2,3), record 1 is absent and hence out-of-bag **for that one fitted tree**; this does not establish an entire forest-level out-of-bag prediction or coverage for every record. For a learner-selected boosting update, publish its exact residual/gradient or weighted-error trace instead of claiming a package's printed stage weights are an independent oracle.

**M1 — Margin and kernel sanity.** In one dimension the two nearest training points are x=-1 with label -1 and x=+1 with label +1; with additional examples x=-2 and x=+2 of the corresponding labels, the separating function f(x)=x (w=1, intercept=0) has **functional margin 1** at the nearest support points and positive geometric margin 1 to the hyperplane on either side; the distance between the support hyperplanes is **2**. The linear Gram matrix for feature coordinates (1,2) is [[1,2],[2,4]], positive semidefinite and rank one; matrix [[1,2],[2,1]] has negative eigenvalue -1 and cannot be a valid positive-semidefinite kernel Gram matrix under the ordinary SVM assumptions. This is a toy **separable** mathematical check, not a calibrated probability or real-world margin certificate.

**L1 — Finite-hypothesis concentration and its conditions.** For an iid evaluation sample with **n=100** independent observations and bounded zero-one loss, a fixed precommitted hypothesis satisfies the Hoeffding two-sided deviation statement P(|Rhat-R|≥epsilon) ≤ 2 exp(-2 n epsilon squared). For epsilon=0.2 this gives **2 exp(-8)**, approximately **0.000671**. For a predeclared finite class of **H=10** hypotheses, union bounding across that class gives **20 exp(-8)**, approximately **0.006709**, for the probability that at least one empirical risk differs from its population risk by at least 0.2 under the same assumptions. At confidence at least 95%, an elementary simultaneous error tolerance solves epsilon=sqrt(ln(2H/0.05)/(2n))=sqrt(ln 400/200), approximately **0.1731**. These are guarantees over repeated iid sample draws, not observed certainty, and do not apply without modification to dependent-group records, arbitrary unbounded losses, an adaptively enlarged hypothesis class selected using test feedback, or shifted deployment data.

**V1 — Group leak and fit boundary.** The source has entities A, B, C, D, each with exactly two records (A1,A2; B1,B2; C1,C2; D1,D2). Labels are 0 for both A and C records and 1 for both B and D records. Training on (A1,B1,C1,D1) and testing on (A2,B2,C2,D2) **shares all four identities across the split** and is invalid for a *new-entity* generalization claim. A grouped holdout trained on (A1,A2,B1,B2) and tested on (C1,C2,D1,D2) has **zero group overlap**, although the small and artificial dataset still cannot substantiate stable external performance. In a separate scalar feature example, training values (0,2) give **training mean 1**; the unseen held-out value 100 must be centered by 1 to yield 99. Fitting the mean on all three gives 34 and transforms the held-out observation to 66; this has contaminated preprocessing even without consulting test labels.

**C1 — Classification decision arithmetic.** Twelve binary labeled examples contain four actual positives and eight negatives. A candidate has TP=2, FP=1, FN=2 and TN=7. Accordingly **accuracy=9/12=3/4**, **precision=2/3**, **recall=1/2**, **specificity=7/8**, **F1=4/7**, and **balanced accuracy=11/16**. A fixed all-negative predictor has accuracy **8/12=2/3** and positive recall zero; precision is formally undefined with zero positive predictions and may be reported as zero **only under an explicitly declared convention**. Under task-specific utilities TP=+5, FP=-2, FN=-6, TN=0, the candidate total utility is **-4** and the all-negative comparator total is **-24** on these twelve observations; these are bounded sample utility calculations, not proof that the candidate is safe or cost-effective at a different prevalence.

**P1 — Probabilistic calibration and Brier score.** Four forecast/label pairs are (0.2,0), (0.2,1), (0.8,1), (0.8,1). Their binary **Brier score is (0.04+0.64+0.04+0.04)/4=0.19**. Under exactly two predeclared score bins separating 0.2 from 0.8, mean predicted probabilities are 0.2 and 0.8; positive frequencies are 1/2 and 1, respectively. The two-bin frequency-weighted absolute calibration-gap statistic (an ECE-style estimate) is **(1/2)|0.2-0.5|+(1/2)|0.8-1|=0.25**. It changes under bin choices and finite-sample variation and is not a proven population calibration error, trustworthy real-world probability guarantee or deployment authorization.

**U1 — PCA and clustering boundary.** For points (0,0),(1,0),(2,0), the sample mean is (1,0) and the **sample covariance with denominator n-1=2** is [[1,0],[0,0]]. The leading principal direction is along the x-axis, with arbitrary global sign and full captured sample variance for one component. Zero second-component variance means any interpretation of a distinct useful y-axis component is false for this fixture. In contrast, for symmetric points (0,0),(2,0),(0,2),(2,2), the sample covariance is diagonal with both eigenvalues **4/3** and the leading 1D direction is **not unique**. For clustering, compare the groups near (0,0),(0,1) and (10,10),(10,11) using a declared distance and initialization; report the actual chosen centroid/assignment trace and note that a numeric cluster ID or low inertia is not an independently verified semantic class.

**Scope and scoring guardrails.** Deterministic reference numbers are assessed under the stated finite fixture and convention, with reasoned floating-point tolerance. Non-deterministic model-selection performance must be reported from real executed experiments with seeds, folds and data-generation details; no fixed accuracy is promised by the course. A missing value, unseen category, undefined metric, impossible calibration bin, invalid kernel, inconsistent sampling unit or exhausted resource budget requires documented handling. Every reported result must name exactly what it measures. Independent reproduction cannot rely on secret course materials or paid platforms.

### Required summative assessments

- **AI4-AS1** (supervised learning contracts, baselines and linear models)
  - **Outcomes:** AI4-O1, AI4-O2, AI4-O3, AI4-O8, AI4-O14.
  - **Work:** Define a bounded regression and a binary classification question, including population, observation unit and prediction-time feature availability. Derive R1 mean baseline metrics and the affine fit on fit records by independent calculation, then compare a train-only regression baseline and a linear model using an honest separate evaluation partition. Fit a small regularized linear classifier or logistic model under a declared loss, explain the intercept, coefficient/feature scaling and output probability versus threshold conventions, and test an invalid/unseen input or unreasonable extrapolation. The source must distinguish exact reference results from observed holdout performance.
  - **Criteria:** R1 yields mean 4, MAE 2, MSE 5 and RMSE sqrt(5) for the **training fixture**; zero residual of 1+2x on these rows is **not** presented as generalization. The baseline never uses held-out target statistics in fitting; model parameters and decision thresholds have explained meaning; the classification trace handles uncalibrated score or probability assumptions honestly. A model that prints a low training loss but fails the evidence boundary does not pass.
  - **Evidence:** Public input/target contract, hand-computed arithmetic, versioned source and commands or equivalent transparent computation, fit/holdout identity log, normal and invalid cases, descriptive error report and honest limitations.

- **AI4-AS2** (instance, probability, margin and kernel learners)
  - **Outcomes:** AI4-O2, AI4-O4, AI4-O7, AI4-O8, AI4-O17.
  - **Work:** Independently compute N1 k-neighbor predictions and tie handling; fit a valid train-only preprocessing-plus-neighbor pipeline and a finite Naïve Bayes likelihood example with an explicit correlated-feature or unseen-category failure. Explain and verify the M1 hard-margin and PSD Gram-matrix calculations, fit a bounded linear or kernel margin learner with a declared regularization/scaling protocol, and compare at least two meaningfully different families against a baseline on valid independent evaluation records. Report failures and CPU/fit constraints; none of the margin output values may be presented as calibrated probabilities by default.
  - **Criteria:** N1 yields label 1 at k=1 and k=3 with a documented k=4 tie; exact N1 distances and M1 separating/margin/kernel calculations match the published conventions. Naïve Bayes probability assumptions and smoothing are mathematically specified, not only exposed as library options; held-out transforms are not trained on test records. Comparison and claimed improvement are bounded by actual evaluation results and fit budgets, with no assertion of global winner.
  - **Evidence:** Tiny independent distance/likelihood/margin/kernel oracle, model setup, train-only fit tracing, test/failure examples, actual comparative experiment records, reproducible commands and limitations.

- **AI4-AS3** (tree learners, ensembles and fit-versus-generalize distinction)
  - **Outcomes:** AI4-O2, AI4-O5, AI4-O6, AI4-O11, AI4-O17.
  - **Work:** Derive T1 root entropy, a justified alternative split if appropriate, and the meaning of a zero-impurity leaf. Trace the published bootstrap draw and identify which indices are out-of-bag **for one tree**. Fit a shallow single tree, at least one bagged/random-forest configuration and a bounded additive boosting variant or independently derived stage update, controlling split/model-selection rules. Compare train and valid held-out behavior and vary one depth, bag size or learning-rate parameter under a fair protocol. Show one negative case where a tree or ensemble memorizes noise or leakage.
  - **Criteria:** T1 yields root entropy 1 bit, ideal split gain 1 bit, and only original index 1 absent from the specified one-tree bootstrap draw; claims about full forest OOB scoring must use actual tree eligibility. Candidate model and comparison results follow a consistent evaluation contract; learner distinguishes ensemble variance reduction from a universal guarantee and explains why boosting can overfit. No impurity importance is treated as causal attribution.
  - **Evidence:** Hand-derived split and bootstrap oracle, source with trained configurations, seeds/splits, train/holdout measurements, negative/noise case and a compact engineering/statistical interpretation.

- **AI4-AS4** (generalization theory and complexity investigation)
  - **Outcomes:** AI4-O9, AI4-O10, AI4-O11, AI4-O17.
  - **Work:** Define empirical versus population risk for a finite predeclared binary-loss hypothesis class and derive the fixed-hypothesis concentration/union-bound reasoning behind L1, including its assumptions. Compute the n=100, epsilon=0.2, H=10 values and confidence tolerance independently. Investigate a synthetic capacity/regularization comparison using repeated honest draws or folds, recording bias/variance-relevant behavior and a counterexample in which more training fit does not imply better out-of-sample generalization. Explain what inference collapses under duplicated entities, unbounded loss or adaptive reuse of the final test sample.
  - **Criteria:** L1 yields 2 exp(-8), 20 exp(-8), and sqrt(ln 400/200) with correct interpretation and numeric tolerances. The proof sketches distinguish a fixed hypothesis from a predeclared finite class and state the iid and bounded-loss requirements. A plot or simulated observation is described as empirical, not a substitute for the inequality's assumptions; selection uncertainty and competing interpretations are disclosed.
  - **Evidence:** Independently checkable mathematical argument and numerical evaluation, small declared synthetic experiment with executed output, counterexample, assumptions table and written generalization-limits defense.

- **AI4-AS5** (leakage-safe selection and validation protocol)
  - **Outcomes:** AI4-O1, AI4-O8, AI4-O12, AI4-O13, AI4-O17, AI4-O20.
  - **Work:** Construct an explicit training, hyperparameter-selection and final-evaluation protocol for repeated-entity data. Diagnose the invalid row split and pooled centering in V1, then produce corrected group-preserving assignments and fit-time transforms. Demonstrate k-fold and a nested or independent untouched-test selection procedure with no target-derived feature or fold leakage, and compare its interpretation with a chronological split when labels arrive later. Include a deliberately leaky fitting or selection path, show which operation violates the boundary and repair it without consulting the final scores for model choice.
  - **Criteria:** Original V1 split shares all four entities, corrected grouped split shares none, training-only center 1 yields held-out feature 99, and pooled center 34 yields contaminated 66. Every preprocessing/feature selection/calibration/hyperparameter operation is assigned to permitted data, with a demonstrably untouched test boundary. Fold scores and selection uncertainties are interpreted in the context of intended population; no repaired score is asserted to be universally better before actual measurement.
  - **Evidence:** Source identity/split tables, exact V1 references, executable pipelines and per-fold learned-state record, legal/leaky branch diagnosis, repeated/temporal test cases, selection trail and independently reproducible commands.

- **AI4-AS6** (metrics, calibration, decision threshold and error analysis)
  - **Outcomes:** AI4-O1, AI4-O14, AI4-O15, AI4-O16, AI4-O17, AI4-O20.
  - **Work:** Independently calculate C1's confusion-derived metrics and compare the declared all-negative baseline and a synthetic cost-sensitive utility. Evaluate P1's Brier score and fixed-bin calibration gap, stating which calibration property the four observations cannot establish. On a separate valid held-out experiment, report classification/regression metrics appropriate to the task, probability/scoring behavior, threshold policy selected without tuning on final evaluation, and a named error/subgroup slice with actual denominators and uncertainty/shift limits. Demonstrate an undefined metric or low-support group without filling absent evidence with invented scores.
  - **Criteria:** C1 yields exactly TP2/FP1/FN2/TN7 and published derived metrics; the utility totals are -4 and -24 under the stated *sample utility*, not universal decision correctness. P1 Brier is 0.19 and two-bin gap is 0.25 with the given bin policy; this is not presented as proven population calibration. The held-out report states counts/metric orientation, threshold selection source, support, limitations and a meaningful counterexample. No apparent high aggregate accuracy conceals zero recall or sparse-group invalidity.
  - **Evidence:** Hand-computed confusion and probability references, deterministic test source, actual held-out metric/fold values, exact denominator and threshold documentation, negative cases, bounded subgroup/shift discussion and limitations report.

- **AI4-AS7** (unsupervised clustering and dimension reduction)
  - **Outcomes:** AI4-O1, AI4-O8, AI4-O18, AI4-O19, AI4-O20.
  - **Work:** Define a bounded unlabeled representation question and calculate U1's mean, sample covariance and leading component by hand or an independent exact reference. Analyze the symmetric equal-eigenvalue variant and explain nonuniqueness; implement/inspect one small k-means assignment-plus-update with documented initialization and compare a non-centroid clustering limitation or alternate method. If PCA/clustering informs downstream classification, fit all transforms only in the permitted training folds and explain why an unsupervised fit on held-out records still contaminates evaluation.
  - **Criteria:** U1 first covariance is diag(1,0), symmetric example covariance is diag(4/3,4/3), and the principal direction's sign/nonuniqueness caveats are correct. Cluster assignments follow the declared distance, initial seeds and algorithm rather than a presumed semantic ground truth. Training boundaries and numeric stability are explicit, and silhouette/inertia is not marketed as proof of useful real-world classes.
  - **Evidence:** Independently computed covariance/eigen/projection work, finite clustering trace, local reproducible source/configuration, initialization comparison, degenerate or malformed case and fit-boundary/interpretation notes.

- **AI4-AS8** (integrated classical-ML study and unfamiliar transfer)
  - **Outcomes:** AI4-O1, AI4-O2, AI4-O12, AI4-O13, AI4-O14, AI4-O15, AI4-O16, AI4-O17, AI4-O20, AI4-O21.
  - **Work:** Consolidate/reuse legitimate AI4-AS1–AS7 evidence in **one coherent local versioned study**, adding a bounded real or synthetic prediction question, baseline and at least two distinct classical model families, a fit-safe selection process, one final evaluation, correct score/decision and failure analysis, resource limits, and a transparent model report. Do not require seven independent reimplementations. The assessor supplies an **unfamiliar bounded** change to entity grouping, feature availability, class prevalence, error cost, target definition, threshold rule, evaluation schedule or a data source anomaly. Predict the expected effect before execution, update the contract/model/validation as needed, independently verify a new oracle or negative case, and defend the changed interpretation. The defense may be written, recorded or live and must be individually attributable.
  - **Criteria:** A clean environment can reproduce the authentic training and selected scoring records without private data/accounts or silently using a test label during any fitting decision. The baseline and compared families are genuinely different and supported by model-specific evidence, not two labels for the same pipeline. A changed scenario receives a correct independent expected result, valid repaired protocol or explicit justified refusal where claims are no longer supported; previously established behavior is regression-checked. A copied leaderboard, a perfect training score or an unspecified number cannot establish O21 or population claims. Specialty mathematics and algorithms retain their separately assessed criteria from AI4-AS1–AS7 and are not presumed by inclusion in this integration exercise.
  - **Evidence:** Single reusable versioned source tree or equivalently inspectable collection, setup commands and random seeds, source/sampling contracts, split/fold/fit logs, independent numeric references, selected model and scores, genuine negative and reviewer-changed cases, limitations/ethical use report and individually reviewable defense.

### Required outcome-to-assessment coverage

| Required outcome | Summative evidence |
| --- | --- |
| AI4-O1 | AI4-AS1, AI4-AS5, AI4-AS6, AI4-AS7, AI4-AS8 |
| AI4-O2 | AI4-AS1, AI4-AS2, AI4-AS3, AI4-AS8 |
| AI4-O3 | AI4-AS1 |
| AI4-O4 | AI4-AS2 |
| AI4-O5 | AI4-AS3 |
| AI4-O6 | AI4-AS3 |
| AI4-O7 | AI4-AS2 |
| AI4-O8 | AI4-AS1, AI4-AS2, AI4-AS5, AI4-AS7 |
| AI4-O9 | AI4-AS4 |
| AI4-O10 | AI4-AS4 |
| AI4-O11 | AI4-AS3, AI4-AS4 |
| AI4-O12 | AI4-AS5, AI4-AS8 |
| AI4-O13 | AI4-AS5, AI4-AS8 |
| AI4-O14 | AI4-AS1, AI4-AS6, AI4-AS8 |
| AI4-O15 | AI4-AS6, AI4-AS8 |
| AI4-O16 | AI4-AS6, AI4-AS8 |
| AI4-O17 | AI4-AS2, AI4-AS3, AI4-AS4, AI4-AS5, AI4-AS6, AI4-AS8 |
| AI4-O18 | AI4-AS7 |
| AI4-O19 | AI4-AS7 |
| AI4-O20 | AI4-AS5, AI4-AS6, AI4-AS7, AI4-AS8 |
| AI4-O21 | AI4-AS8 |

**Course completion decision.** Each of the **21 outcomes** requires a satisfactory and inspectable decision against its actual relevant criteria through the eight required summative assessments, using the correct course revision. A learner may reference prior legitimate artifacts as evidence for more than one outcome only when the corresponding criteria are genuinely met. Optional practice, weeks studied, reported scores without source/split provenance, automated test success without reasoning, training accuracy alone and the act of submitting eight files are not sufficient. The final unfamiliar case assesses independent transfer, not the right to retake all earlier work automatically. Assessment may use learner-controlled text/tables, derivations and source code in a reviewer-accessible form; no commercial course platform, remote model or private evaluation service is necessary.

### Optional open academic and technical references

- [Stanford CS229 (Stanford Engineering Everywhere)](https://see.stanford.edu/Course/CS229) — supervised and unsupervised model families, bias–variance and statistical learning theory, including assumptions behind generalization.
- [Stanford CS229 published learning-theory notes](https://cs229.stanford.edu/notes_archive/cs229-notes4.pdf) — optional independent background for finite-hypothesis/union-bound reasoning.
- [scikit-learn User Guide: model selection and evaluation](https://scikit-learn.org/stable/model_selection.html) — reproducible scoring, split design and model selection conventions.
- [scikit-learn: Common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) — fit-boundary mistakes, inconsistent preprocessing and leakage-safe pipelines.
- [scikit-learn: Cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html) — group/time dependence, fold selection and evaluation limitations.
- [scikit-learn: Nested versus non-nested CV](https://scikit-learn.org/stable/auto_examples/model_selection/plot_nested_cross_validation_iris.html) — model-selection bias versus independent evaluation.
- [scikit-learn: Model evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html) — task-appropriate metrics, including probability-score and classification distinctions.
- [NumPy documentation](https://numpy.org/doc/stable/) — numerical array behavior and stable reproducible computations.

These free public references supplement the fully published OEE assessment contract; no external paid textbook, particular hosted infrastructure or library version is a hidden graduation condition.
