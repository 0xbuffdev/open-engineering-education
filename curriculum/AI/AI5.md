# AI5 — Deep Learning & Representation Learning

**Program:** AI — AI Engineering
**Type:** course
**Prerequisites:** [AI4](AI4.md) — Machine Learning & Statistical Learning Theory (completed)
**Duration:** 20–26 weeks
**Status:** draft
**Specification:** v0.2.0
**Expected workload:** 10–15 focused hours/week (provisional; approximately 200–390 focused hours)

> [AI Engineering](README.md) · [Curriculum design guide](../DESIGN-GUIDE.md) · [Course format](../../spec/course-format.md) · [Evidence rules](../../spec/evidence-rules.md)

## Overview

**AI5 develops deep learning as inspectable engineering rather than framework invocation.** Learners design differentiable models with a defensible inductive bias, reason independently about tensor shapes and gradient propagation, implement and diagnose real training loops, compare architectures without contaminating evaluation, and investigate what learned representations preserve, discard and fail to explain. Completion requires a working, reproducible small-scale neural learning system **and** convincing evidence that the learner understands its mathematics, training dynamics, input assumptions, evaluation limitations and failure modes.

**Origins and applications.** Neural networks build expressive functions by composing parameterized transformations and nonlinearities. Backpropagation makes gradients of such compositions tractable; convolution introduces weight sharing and local receptive fields; recurrent computation models ordered state; embeddings and bottlenecks can organize representations learned from data. These mechanisms underpin speech, vision, language, anomaly detection, scientific data analysis and more. Their expressive power does not by itself provide valid labels, independent test performance, disentangled semantic concepts, causal explanations or safe operational decisions. A small controlled learner can demonstrate a mechanism, not the reliability of an industrial-scale model.

**Prerequisite and responsibility boundary.** Entry requires assessed [AI4](AI4.md), which transitively requires [AI2](AI2.md), [AI1](AI1.md) and completed Software Engineering Foundations. AI2 already establishes calculus, matrix derivatives, log-likelihood, chain rule, parameter conditioning, probabilistic scoring and optimization mathematics; AI4 already assesses supervised baselines, classical algorithms, generalization claims, group/time-aware evaluation, calibration, leakage control, error analysis and PCA. This course **applies** those prerequisites: its new competence is building and understanding *multilayer differentiable programs*, automatic differentiation, actual neural training, normalization and regularization behavior, convolution, finite recurrent state, learned embeddings, reconstruction and contrastive representation objectives. SEF programming, Git/testing, numerical foundations and probability are not re-taught. A small mathematical warmup is formative review, not a redundant assessed prerequisite.

**Future-course boundaries.** [AI3](AI3.md) is classical reasoning and is not required for neural training. AI7 owns language-specific tokenization, linguistics, retrieval and NLP evaluations; AI8 owns vision-specific datasets, geometric augmentation and image-system evaluation. AI9 owns transformer self-attention, positional mechanisms, masked language modeling and generative modeling. AI10 owns advanced adaptation, large-model fine-tuning, resource-aware training and optimization at scale; AI13 owns comprehensive AI-system evaluation/testing and reliability; AI15 owns deployment and MLOps. AI5 covers *foundational* convolutions, simple recurrence, embedding lookup and a small frozen-feature transfer exercise **only as transferable deep-learning mechanisms**. It must not silently require transformers, pretrained cloud models, production pipelines, domain-specific corpora or reinforcement learning. The optional speech, robotics and graph electives retain distinct application and architecture competencies.

**Accessible reference environment.** A locally runnable CPU-based Python 3, NumPy and PyTorch environment is a convenient reference; learners may use another open tensor/autodiff library if it satisfies the published observable behavior and independent evidence requirements. Small synthetic numeric, spatial, ordered and categorical fixtures are mandatory alternatives to commercial datasets. All required models must be runnable on a typical CPU; no GPU, cloud service, paid weights, private corpus, remote inference API, unlicensed data or proprietary evaluator is required. State actual interpreter, package/library versions, precision/dtype, device, batch and gradient reduction conventions, seeds, deterministic settings, stopping decisions and permissible tolerances. Tensor drawings require equivalent labeled textual shapes/tables; conceptual and numerical derivations may use accessible written or equivalent reviewable media.

**Evidence philosophy and workload.** Thirteen modules follow actual conceptual dependencies and have deliberately differing lesson counts. Seven required summative assessments progressively establish model graphs and manual gradients; stable optimization; training/evaluation mode and regularization; convolutions and recurrence; representation learning; genuine small-data transfer/evaluation; and an integrated unfamiliar defense. They may reuse a coherent versioned source tree instead of seven duplicated independent projects. Each algorithmic claim needs an independent oracle or a reasoned counterexample; stochastic training comparisons need **executed measurements**, not fictitious benchmark targets or guarantees from a seed. Exact bitwise equality across devices, library versions and different kernels is not promised even when randomness is controlled. The duration range is an *unverified planning estimate* including derivation, coding, experiments, debugging, independent checking, review and correction. The course remains `draft` until genuine learner and reviewer evidence justifies a change.

## Learning outcomes

- **AI5-O1:** Define a bounded neural learning problem with observation/target units, legitimate training information, chosen function class, intended representation, evaluation boundary and limitations of the claim.
- **AI5-O2:** Trace and independently check shapes, data types, parameter counts, broadcasting, memory and computational implications of multilayer tensor operations and explicitly reject malformed inputs.
- **AI5-O3:** Construct and compare small affine/nonlinear feedforward architectures with correct parameterization, activation behavior and expressivity, distinguishing useful inductive bias from memorization.
- **AI5-O4:** Derive gradients through a nontrivial multilayer computational graph, including chain, vector-Jacobian and branch contributions; check an independent oracle against autograd and identify nondifferentiable or detached paths.
- **AI5-O5:** Implement a complete neural train/validation/inference loop with correct data/target transformations, loss reduction, gradient lifecycle, parameter updates, mode boundaries, and independent metric calculations.
- **AI5-O6:** Diagnose optimization and gradient pathologies including saturation, dead units, vanishing/exploding gradients, invalid initialization, stale/accumulated gradients, nonfinite values and stopping failures.
- **AI5-O7:** Apply and independently explain normalization, stochastic dropout and relevant train/eval statistics, including their interactions with batch size, inference and leakage.
- **AI5-O8:** Select and evaluate neural regularization, architecture capacity, data augmentation where admissible, and early-stopping controls with fair validation, distinguishing optimization from supported generalization.
- **AI5-O9:** Derive, implement and inspect bounded convolution, padding/stride, receptive field, weight sharing and pooling operations with correct spatial shapes, parameter counts and a nonconvolutional comparison.
- **AI5-O10:** Implement and reason about a finite simple recurrent computation and ordered-sequence representation, including hidden-state shape, gradient propagation, masking/state reset and the limitations of long dependencies.
- **AI5-O11:** Construct and evaluate learned embedding lookups and representation geometry for discrete inputs, with explicit vocabulary/index semantics, gradient/update scope and limits on interpreting distance or similarity.
- **AI5-O12:** Implement and analyze a small encoder/decoder or autoencoder objective, controlling bottleneck capacity and comparing reconstruction/representation behavior without claiming discovered semantics.
- **AI5-O13:** Define and investigate a bounded contrastive or related self-supervised representation objective with justified positive/negative pairs, temperature, collapse and sampling assumptions.
- **AI5-O14:** Conduct a small legitimate representation-transfer comparison using a locally trained encoder with frozen or selectively updated features, documented train-only fitting and an appropriate from-scratch/baseline reference.
- **AI5-O15:** Design and execute credible neural ablations and generalization/error evaluations with fixed split/selection conditions, baseline and seed variability, proper subgroup/support reporting and explicit noncausal claims.
- **AI5-O16:** Reproduce a trained neural model from a clean environment using complete model/optimizer/seed/configuration/checkpoint provenance and verify the saved–restored inference behavior.
- **AI5-O17:** Measure and interpret small-model parameter, activation, memory, training-time and inference-time costs, including the limitations of CPU/device comparisons and claims of efficiency.
- **AI5-O18:** Diagnose representation shortcuts, contamination, data-quality failure, unsupported attribution, domain shift or absent safety evidence; formulate bounded limitations and controls proportional to observed facts.
- **AI5-O19:** Integrate a small defensible deep-learning system with train-only transformations, one meaningful representation or architecture mechanism, independent numeric oracles, valid baseline comparison and audited failure behavior.
- **AI5-O20:** Handle an unfamiliar bounded change to graph, gradient, data shape, input distribution, mode, loss, representation or evaluation boundary; independently predict consequences and demonstrate a justified repair or safe refusal.

## Modules

### Module 1 — Neural Learning Questions, Representation and Inductive Bias

#### Outcomes

- AI5-O1
- AI5-O3
- AI5-O15
- AI5-O18

#### Lessons

1. **From fitted statistical model to composed learner** — Identify what a multilayer differentiable model can express that a restricted linear family may not, using AI4's exact empirical-risk and held-out evaluation vocabulary without re-teaching it.
2. **History and scope of trainable representations** — Connect perceptrons, backpropagation, shared convolutional parameters and modern learned embeddings to bounded applications, stating what each approach was designed to make feasible.
3. **Observation, target and representation contracts** — Name the sample identity, inference-time inputs, target semantics, output type, allowed transformations and failure behavior for a synthetic neural task.
4. **Baselines before architecture** — Choose a constant, linear or AI4 classical model whose assumptions and evaluation use are sufficiently clear to avoid a meaningless neural-network victory.
5. **Inductive bias versus raw capacity** — Compare parameter sharing, local spatial structure, ordered hidden state and independent feature processing; explain which assumptions a real task might violate.
6. **Nonlinearity on a tiny XOR problem** — Show why XOR corner labels cannot be realized by one affine threshold, then inspect an exact two-hidden-unit ReLU representation without claiming it generalizes from four points.
7. **Predeclared evidence and limitations** — Specify the train/validation/test responsibilities, a limited compute budget, a negative control and one claim that will be rejected without independent evidence.

*Optional formative investigation:* Draw or describe the exact four XOR corners and produce two reasons a perfect training fit does not establish a trustworthy classifier.

### Module 2 — Tensor Shape Contracts and Parameterized Layers

#### Outcomes

- AI5-O2
- AI5-O3
- AI5-O17

#### Lessons

1. **Batch and feature axes** — For X of shape (B,D), derive the shapes of XW+b, intermediate activations and output logits with named B, input, hidden and output dimensions.
2. **Named-axis reasoning and broadcasting** — Explain legal broadcasting of a hidden-vector bias across batch rows, reject mismatched feature dimensions and investigate a silent broadcast that changes the task.
3. **Parameters versus examples** — Count trainable weights/biases for a 2→2→1 feedforward network independently of batch size; distinguish activation memory from parameter memory.
4. **Matrix and tensor layouts** — Trace contiguous/noncontiguous views, reshapes and transposes at an explanatory level, including why an arbitrary reshape that preserves element count can corrupt semantic axes.
5. **Activation and loss shapes** — Align per-example logits, targets and reduced scalar losses; distinguish class indices, one-hot targets and signed regression values under declared library conventions.
6. **Initialization and scale** — Compare zero, excessive and variance-aware random initializations, emphasizing symmetry-breaking and reasonable activation/gradient scales rather than reciting an initializer name.
7. **Predicting resource growth** — Derive approximate memory and multiplication costs when doubling batch, width or depth, and document when optimizer-state or saved-backward activations dominate parameters.
8. **Input contract tests** — Reject nonfinite, noninteger category indices, wrong dtype, wrong layout and missing channels with explicit understandable messages and independent shape expectations.

### Module 3 — Feedforward Networks and Nonlinear Function Families

#### Outcomes

- AI5-O1
- AI5-O2
- AI5-O3
- AI5-O8

#### Lessons

1. **Affine composition and collapse without nonlinearities** — Prove that composing two affine maps with no intervening nonlinearity is another affine map; show what parameterization changes and what functional capacity does not.
2. **ReLU and its piecewise response** — Calculate exact positive/zero/negative outputs and note the derivative convention at zero is library-dependent for a nonsmooth function.
3. **Sigmoid/tanh saturation** — Compare saturation regions and derivative magnitudes with piecewise linear activations, connecting the outcome to longer gradient paths.
4. **Hidden width and approximation** — Investigate how one or two hidden units represent a simple boundary and distinguish finite demonstrated function fit from a global universal-approximation claim.
5. **Exact XOR constructive representation** — Verify h1=ReLU(x1+x2), h2=ReLU(x1+x2−1), yhat=h1−2h2 at the four binary corners. Explain why the result remains a continuous real-valued function between the corners.
6. **Output heads and objectives** — Choose regression score, binary logit or mutually exclusive class logits with compatible losses, keeping proper score/probability interpretation inherited from AI2/AI4.
7. **Parameter initialization and symmetry failure** — Explain why making all identical neurons in the same hidden layer share identical parameters can preserve unwanted symmetry under deterministic gradients.
8. **Capacity changes as hypotheses** — Design a fair width/depth experiment with constant evaluation controls and disclose that more parameters may improve optimization while worsening data-limited generalization.

### Module 4 — Computational Graphs, Backpropagation and Autograd

#### Outcomes

- AI5-O2
- AI5-O3
- AI5-O4
- AI5-O6
- AI5-O16

#### Lessons

1. **Graph nodes, values and gradient ownership** — Trace a scalar objective through two matrix multiplication layers, biases and activations, marking which tensors require gradients.
2. **Local chain rules and reverse accumulation** — Compute reverse-mode derivatives by passing vector-Jacobian products backward; avoid constructing an unnecessarily large full Jacobian.
3. **Two-layer manual derivative** — Derive every weight, bias and input gradient on the public N1 reference fixture while naming shape and sign at each step.
4. **Shared variables and branch aggregation** — Show how a parameter reused in two paths receives the sum of valid derivative contributions, not the gradient from whichever branch is visited last.
5. **Batch loss-reduction convention** — Compare sum, mean and half-squared reductions, including how loss normalization affects gradient magnitude independently of optimizer choice.
6. **Gradient checks away from nondifferentiability** — Use central finite differences at a point where all relevant ReLUs are strictly inside linear regions; specify perturbation, tolerance and a failure interpretation.
7. **Automatic differentiation semantics** — Explain why a computational graph records differentiable operations and how parameter gradients are attached to leaves; an autograd call is a verification tool, not an oracle for a flawed mathematical model.
8. **No-grad, inference and detach** — Demonstrate intentional graph-breaking for inference and parameter freezing versus accidentally detaching a required trainable path.
9. **In-place mutation and saved tensors** — Investigate how altering a tensor needed for backward may invalidate derivatives or raise an error; distinguish the library's protection from a general numerical proof.
10. **Gradient failure diagnosis** — Locate wrong sign, stale accumulator, transposed weight, omitted activation derivative or hidden broadcasting and independently predict the correct changed output.

### Module 5 — Complete Training Loops and Optimization Diagnostics

#### Outcomes

- AI5-O5
- AI5-O6
- AI5-O16
- AI5-O17

#### Lessons

1. **Batch and label lifecycle** — Prepare stable mini-batches with explicit input/target types, identity groups and fixed splits; preserve original sample identity throughout each epoch.
2. **Forward/loss/backward/update ordering** — Implement prediction, scalar loss, gradient reset, backward pass and optimizer step in the correct order, distinguishing forward evaluation from mutation.
3. **Gradient accumulation semantics** — Demonstrate that repeated backward calls can add gradients unless explicitly reset; compare a deliberately accumulated two-step trace against the intended independent mini-batches.
4. **Reduction across batch sizes** — Explain why changing sum to mean changes gradients and why incorrectly comparing different batch sizes/learning rates can invalidate a claimed optimizer improvement.
5. **SGD, momentum and adaptive updates in practice** — Apply AI2's mathematical optimizer reasoning to an actual trainable neural graph; inspect state handling and compare measured behavior on bounded tasks.
6. **Initialization stress tests** — Deliberately start with a too-large scale or symmetric hidden parameters and diagnose exploding, saturated or unlearnable behavior from observed activations/gradients.
7. **Vanishing, exploding and dead activations** — Record per-layer gradients and finite-value status; give a defensible example where saturation or a dead ReLU stops effective learning.
8. **Clipping and safeguards** — Apply a declared norm or value clipping rule only when justified and detect NaN/inf in loss or gradients; clipping does not repair a wrong objective or create missing information.
9. **Tiny-batch overfit as a diagnostic** — Try to fit a very small known training fixture as a mechanism check; if it fails, distinguish implementation defect, capacity mismatch, regularization, unsuitable objective and stopping choice.
10. **Honest stopping and budget accounting** — Record training and validation curves, actual number of examples/updates, elapsed CPU cost and stop reason, avoiding hidden evaluation-based model selection.

### Module 6 — Regularization, Normalization and Train/Evaluation Semantics

#### Outcomes

- AI5-O5
- AI5-O7
- AI5-O8
- AI5-O15

#### Lessons

1. **Regularization in neural capacity** — Extend AI4's bias–variance reasoning to depth/width, explicit weight penalties, controlled data perturbations and early stopping.
2. **Dropout as sampled masks** — Apply the publicly specified inverted-dropout keep mask and scale; explain why an expectation property is not a guarantee for each realized batch or a justification for dropout at inference.
3. **Dropout in train and evaluation modes** — Demonstrate the stochastic training transform, deterministic evaluation identity behavior for ordinary inverted dropout, and an invalid pipeline that leaves dropout active on validation.
4. **Normalization axes and statistics** — Compute a single-feature batch normalization example and compare the axes of batch-normalization and layer-normalization; state epsilon and unbiased-versus-population variance conventions.
5. **BatchNorm running estimates** — Distinguish statistics used for normalization of a current training batch from maintained evaluation running statistics and avoid claiming they are always numerically identical.
6. **Small batch and distribution-shift limits** — Investigate why noisy small-batch statistics or changed population may destabilize BatchNorm; contrast a suitable per-example normalization strategy without universal ranking.
7. **Data augmentation and label preservation** — Specify which transformations preserve the defined target in a selected synthetic task and reject augmentations that alter class meaning or leak between related examples.
8. **Early stopping without test contamination** — Select a checkpoint on valid development records only, track actual stopping patience/metric direction, and leave the final test untouched until selection ends.
9. **Ablation with comparable budgets** — Hold data/split/metric and training budget fixed, change one regularization or normalization mechanism, and report seeded variability and the actual observed rather than hoped-for effect.

### Module 7 — Convolutional Networks and Spatial Inductive Bias

#### Outcomes

- AI5-O2
- AI5-O9
- AI5-O17

#### Lessons

1. **Spatial locality and shared parameters** — Motivate a sliding spatial filter on a simple grid and explain how its shared weights differ from position-specific dense weights.
2. **Cross-correlation convention** — Calculate the exact public 2D input/kernel outputs with no kernel flipping, padding or stride, and identify why a library may call this operation convolution.
3. **Channels, batches and output dimensions** — Derive N,C,H,W and N,Cout,Hout,Wout shapes with explicit kernel, stride, padding, dilation and channel assumptions; reject impossible geometries.
4. **Padding and boundary influence** — Trace valid versus zero-padded operations, identify synthetic border effects and account for how changing padding alters output size and receptive field.
5. **Stride and downsampling** — Analyze overlapping and skipped positions, justify an output-size calculation and explain why aggressive stride may discard evidence.
6. **Pooling and aggregation** — Compute maximum and average pooling on the fixture, describe which transformations preserve or lose information and how gradients route through a unique maximum.
7. **Receptive-field growth** — Trace how stacked kernels, strides and pooling change the region of input that can influence a deeper feature; distinguish theoretical field from effective learned influence.
8. **Parameter sharing and compute** — Compare conv layer trainable parameter count and activation cost with a dense layer processing the same flattened input under an explicit layout.
9. **Convolutional miniature comparison** — Train or inspect a tiny local pattern classifier and compare with a dense baseline using the same train/validation contract; reserve real-world vision benchmarking and augmentation policy for AI8.

### Module 8 — Ordered Data and Simple Recurrent Computation

#### Outcomes

- AI5-O2
- AI5-O6
- AI5-O10

#### Lessons

1. **Order, variable length and hidden state** — Define a discrete ordered sequence and show why feature-independent examples cannot express every dependence on preceding observations.
2. **Simple recurrent update** — Calculate h_t=f(Wxh x_t+Whh h_{t-1}+b) on a tiny scalar/vector fixture with clearly specified initial state and recurrence.
3. **Unrolling and shared parameters** — Relate a recurrence to a depth-unrolled computation graph, noting repeated use of the same weights and gradient contributions over time.
4. **Backpropagation through time** — Trace a short exact derivative along a recurrence and explain why repeated Jacobian products may cause vanishing or exploding gradients.
5. **Variable-length masking and padding** — Explain why artificial pad steps must not create valid target/loss contributions and why a model may need masks or sequence lengths to handle batches correctly.
6. **Hidden-state reset and sequence identity** — Investigate a state-carryover defect that leaks one entity's history into another or transports validation information into training.
7. **Long-dependency limitations** — Contrast simple recurrence with gated-state intuition and training instability, without pretending that this module implements full transformer attention or language modeling.
8. **Bounded ordered-task comparison** — Use a small synthetic sequence experiment with valid sampling units, baseline and explicit actual results; avoid NLP/vision-specific evaluation contracts.

### Module 9 — Embeddings and Learned Representation Geometry

#### Outcomes

- AI5-O2
- AI5-O11
- AI5-O18

#### Lessons

1. **Discrete IDs and vocabulary contracts** — Distinguish a categorical token index from continuous physical magnitude; define unknown/padding indices and stable train-time vocabulary ownership.
2. **Embedding lookup as a parameterized table** — Independently calculate the public table rows selected by a sequence of discrete indices and check the returned shape without running a library.
3. **Gradient scope for used and unused rows** — Show why an ordinary lookup updates only participating embedding rows, barring explicit global penalties or optimizer behavior; distinguish lookup from a one-hot multiply.
4. **Aggregation for sets and bags** — Compute sum versus mean of selected embeddings and explain what order information each aggregator discards.
5. **Similarity and learned geometry** — Compare dot product, Euclidean distance and cosine similarity with declared normalization; show how different scaling affects ranking.
6. **Embedding collisions and unknown values** — Demonstrate a vocabulary mismatch, index out of range and unintended shared ID, with explicit rejection or an authenticated unknown-token policy.
7. **Interpretation limits and shortcut evidence** — Explain why close embeddings are not proof of semantic equivalence, fairness or causal meaning; examine a shortcut or spurious correlate learned from synthetic labels.
8. **Train-only representation inspection** — Evaluate a learned embedding on held-out categories where technically supported, state unobserved-category limitations, and reserve NLP retrieval performance for AI7/AI11.

### Module 10 — Bottlenecks, Reconstruction and Self-Supervised Representations

#### Outcomes

- AI5-O11
- AI5-O12
- AI5-O13
- AI5-O18

#### Lessons

1. **Encoder, bottleneck and decoder roles** — Formalize a deterministic small encoder z=f(x) and decoder xhat=g(z), with explicit shape and loss/normalization conventions.
2. **Reconstruction objective and baselines** — Compare a constant, identity-like and bottlenecked reconstruction on a small exact numeric example, explaining why reconstruction loss alone is not a semantic score.
3. **Capacity and identity solutions** — Investigate why an unconstrained wide autoencoder can simply copy data and how bottleneck width or regularization changes the learned objective.
4. **Denoising and corruption contracts** — Choose a controlled synthetic corruption whose target remains the original input, preventing data leakage or a change in target semantics from going unacknowledged.
5. **Self-supervised targets versus labels** — Distinguish reconstructive and discriminative objectives derived from the input from independent downstream ground-truth labels.
6. **Positive/negative pair construction** — Define which synthetic perturbations preserve identity/class and how accidental false negatives, duplicates or class-derived pair construction undermine a representation claim.
7. **Contrastive temperature and logits** — Calculate a one-anchor/one-positive/one-negative normalized exponential objective with the public numeric reference; explain why temperature changes relative scoring.
8. **Collapse and shortcut tests** — Compare identical constant embeddings, a genuinely discriminative setup and a model using a nuisance feature, showing why a low contrastive or reconstruction loss may not yield useful transfer.
9. **Representational evidence versus visualization** — Apply a downstream task probe with held-out fitting conditions, report performance and label it as measured—not a unique interpretation of latent axes.

### Module 11 — Feature Reuse and Bounded Representation Transfer

#### Outcomes

- AI5-O8
- AI5-O14
- AI5-O15
- AI5-O16

#### Lessons

1. **What is being transferred** — Define a locally trained source encoder, a related but distinct downstream target and which input/label relationships permit a meaningful feature reuse hypothesis.
2. **Frozen encoder, trainable head** — Attach a small output head with correct feature dimensions, freeze encoder parameters and verify gradients/optimizer parameter lists do not silently mutate frozen weights.
3. **Selective unfreezing under a budget** — Compare a bounded small-layer unfreeze with a frozen-head baseline, using a predeclared learning rate, update count and valid held-out selection.
4. **From-scratch and constant baselines** — Train a small identical or comparable architecture from scratch and compare an AI4 classical/constant reference; disclose if measured differences are within run variation.
5. **Representation quality versus downstream performance** — Diagnose when a reconstruction representation transfers poorly, a nuisance correlate dominates or fine-tuning overfits a small target sample.
6. **Transfer sample/identity contamination** — Prevent target-test records, subject duplicates and mislabeled source overlaps from being used to select or fit representations; demonstrate a negative leak case.
7. **Parameter and compute accounting** — Report trained/frozen parameter counts, run duration, memory constraints and realistic CPU feasibility rather than claiming transfer always saves computation.
8. **Claims, licenses and reuse boundaries** — Disclose dataset/weights licensing, provenance, shift assumptions and what a successful local head does not establish about production or high-stakes use.

### Module 12 — Neural Evaluation, Reproducibility and Failure Forensics

#### Outcomes

- AI5-O5
- AI5-O6
- AI5-O15
- AI5-O16
- AI5-O17
- AI5-O18

#### Lessons

1. **Model and dataset lineage** — Pin code, package versions, exact synthetic generator or licensed dataset revision, preprocessing, training/selection folds and relevant sample identities.
2. **Randomness and repeatable experiments** — Seed all actually used RNGs, log device/kernel settings and compare repeated runs; distinguish controlled stochasticity from a false promise of bitwise portability across versions/devices.
3. **Saved and restored model contract** — Store architecture configuration and model parameters, restore in evaluation mode and independently verify predictions on a fixed held-out probe; label any tolerances and unsafe checkpoint-loading assumptions.
4. **Optimizer state versus inference state** — Distinguish a model-weight-only inference checkpoint from a resumable training state with optimizer, scheduler and RNG information; prove or qualify actual continuation behavior.
5. **Train/validation/test failure forensics** — Deliberately expose a hidden label leak, state carry-over, augmentation overlap, running-stat contamination or threshold tuning on final test, then repair and re-evaluate.
6. **Gradient and activation instrumentation** — Observe correct parameter update, missing gradients, saturation, NaNs and layer-level signals with actual step/input context; explain why a norm histogram alone is not a diagnosis.
7. **Generalization and subgroup reports** — Compare a neural run to an AI4 baseline with honest per-split/seed outcomes, error examples, support counts and limits on generalizing from a tiny synthetic population.
8. **Resource and accessibility audit** — Measure actual CPU runtime, model size, parameter/activation counts and use a table/text summary for plots; disclose environmental effects and failure/timeout policy.
9. **Limitations, privacy and decision boundary** — State why a model score or embedding neighborhood does not validate causal, fairness, robustness, medical, employment or safety conclusions; require human/permissions controls if discussing non-synthetic extensions.

### Module 13 — Integrated Deep Learning System and Unfamiliar Defense

#### Outcomes

- AI5-O1
- AI5-O2
- AI5-O4
- AI5-O5
- AI5-O8
- AI5-O15
- AI5-O16
- AI5-O17
- AI5-O18
- AI5-O19
- AI5-O20

#### Lessons

1. **Choose one bounded learning question** — Select a small fully synthetic or permitted public task, define legitimate input/labels/groups, model output, baseline and a representation mechanism with no hidden paid prerequisite.
2. **Construct the smallest defensible network** — Specify and implement a small feedforward, convolutional, recurrent or autoencoder-backed learner appropriate to the task, explaining all shape and parameter contracts.
3. **Independent numerical and data oracles** — Reuse earlier assessed exact hand calculations, shape/invariant assertions and a deliberately wrong gradient or preprocessing control as independent evidence.
4. **Execute and record a valid comparison** — Reproduce train-only fitting, baseline comparison, actual selected validation metrics and a held-out final report with honest stochastic variability and resource cost.
5. **Inspect what the model learned** — Analyze relevant internal activations, embeddings, reconstruction failure or filter/hidden-state behavior and distinguish a plausible interpretation from an established fact.
6. **Adverse and missing-evidence cases** — Demonstrate one nonfinite/mode/state/shape/data issue and one generalization/representation or policy boundary with explicit and safe dispositions.
7. **Unfamiliar independently predicted change** — Before running the revised system, explain what a reviewer-changed weight, activation, batch norm mode, feature shape, target timing, grouped split or transferred input implies; repair or refuse the case and check regression behavior.
8. **Independent technical defense** — Provide a clean-start reconstruction of the evidence collection and an attributable explanation of architecture choice, gradient/reproducibility mechanism, comparison fairness, unsupported claims and measured resource use.

Modules are a teaching sequence and **not** thirteen additional summative submissions. Targeted exercises are optional formative feedback; the requirements below are the only required evaluations.

## Completion requirements

### Public reference fixtures, conventions and failure tests

The following compact synthetic mathematical oracles anchor required evidence. A learner may submit an equivalent independently justified fixture if all relevant shapes, values, assumptions and negative cases remain publicly auditable. A correct small hand calculation is *necessary but not sufficient* for the separately required training/generalization evidence. Never report a plausible generated accuracy or timing as if it were a universal expected result.

**N1 — Two-layer ReLU network and gradients.** Let one row-vector input x=(1,2), first-layer W1=[[1,−1],[0,2]] (shape 2-by-2), b1=(0,0); hidden z=xW1+b1=(1,3), h=ReLU(z)=(1,3). Let output column W2=(2,−1) transpose (shape 2-by-1), b2=0, scalar prediction a=hW2+b2=−1 and target y=1. The **half-squared-error loss** L=(a−y)²/2=2; dL/da=−2. Under row-vector conventions, dL/dW2=(-2,-6) transpose, dL/db2=−2, dL/dz=(-4,2), dL/db1=(-4,2), dL/dW1=[[-4,2],[-8,4]] and dL/dx=(-6,4). All hidden preactivations are strictly positive, so ordinary central finite-difference checks avoid the ReLU nondifferentiability at zero. Total trainable parameters: 4+2+2+1=**9**. The exact oracle uses a one-observation loss; changing the reduction or batch count changes scaling.

**F1 — Exact nonlinear XOR witness.** For x1,x2 each in {0,1}, define h1=ReLU(x1+x2), h2=ReLU(x1+x2−1) and prediction h1−2h2. The outputs at (0,0),(0,1),(1,0),(1,1) are **0,1,1,0**. This is an exact *four-corner witness* of nonlinearity, not a claim of robust continuous behavior or learned generalization.

**C1 — Two-dimensional cross-correlation.** Input 3-by-3 matrix [[1,2,0],[0,1,3],[2,1,1]] and 2-by-2 kernel [[1,0],[-1,2]]. With stride 1, dilation 1, padding 0, no bias and **no kernel flip** (the cross-correlation convention used by common neural convolution layers), the 2-by-2 output is **[[3,7],[0,2]]**. Full-window max pooling gives **7**, and average pooling gives **3**. This single-input-channel, single-output-channel kernel has four weights; adding one learned output-channel bias makes **5** parameters. Changing stride/padding requires a recomputed shape/output rather than reusing the oracle.

**R1 — Finite scalar recurrence.** Define h0=0 and h_t=(1/2)h_(t−1)+x_t for x=(1,2,3), with identity activation and no extra bias. The hidden states are **h1=1, h2=5/2, h3=17/4**; the derivative dh3/dx1 is **1/4**, dh3/dx2 is **1/2** and dh3/dx3 is **1**. This is an exact finite shared-recurrence/gradient trace and does not establish long-range learning ability. A padded fourth step is invalid as a real observation unless the task declares it; hidden state must not carry into an unrelated entity by accident.

**E1 — Embedding lookup and bag aggregation.** Embedding matrix with rows indexed 0:(1,0), 1:(0,1), 2:(1,1), shape 3-by-2. Input indices (0,2,1) return **[(1,0),(1,1),(0,1)]** of shape 3-by-2. Sum of these rows is **(2,2)**, mean is **(2/3,2/3)**. The arbitrary integer IDs do not encode ordinal closeness; index 3 is out of vocabulary unless an explicit unknown-category policy is declared. A differentiable lookup may update the participating rows; a purported gradient on unused rows must account for explicit regularization or other computation.

**D1 — Dropout, normalization and execution mode.** For activations (1,2,3,4), retention probability 1/2, and a **specified** training mask (keep, drop, keep, drop), inverted dropout produces **(2,0,6,0)**; in ordinary evaluation mode it returns **(1,2,3,4)** with no mask. The exact expectation statement averages over stochastic masks, not one fixed mask. For a distinct batch-normalization toy batch (1,3), use biased training-batch variance (divide by 2), mean 2, variance 1, epsilon **1**, scale gamma=1 and offset beta=0; the training-batch normalized outputs are **(-1/sqrt(2), 1/sqrt(2))**. Evaluation outputs require separately specified learned running mean/variance and are **not** automatically identical to this pair. Library-specific running-variance estimators/momentum must be documented and not substituted for the declared batch reference.

**P1 — Small classification logit and representation contrast.** For two logits (0, ln 3), softmax probabilities are **(1/4,3/4)**; with target class index 1, cross-entropy is **ln(4/3)** and logit gradients are **(1/4,−1/4)** under *sum over this one example* reduction. Separately, for a contrastive one-positive/one-negative example with similarities s-positive=1 and s-negative=0 at temperature 1, the negative-log positive softmax probability is **ln(1+exp(−1)) ≈ 0.313262**. If positive and negative have **identical similarities**, the loss is **ln 2 ≈ 0.693147** under that identical two-candidate setup. These calculations do not claim useful semantic representations, suitable pair mining, stable large-batch InfoNCE behavior or universally comparable contrastive loss scales.

**T1 — Model/checkpoint transfer fixture.** Construct a local encoder from permitted synthetic data with a two-dimensional output, verify the saved fixed input probe produces the declared finite embedding, then attach a one-layer scalar prediction head whose inputs use the same dimension. The reviewer may replace the input with one of the correct dimension, change the head from scalar to two logits, freeze/unfreeze a documented subset or supply a mismatched dimension. The required evidence is a **fresh independently calculated reference for the changed architecture**, verified parameter freezing and clean model reload. Unlike N1/C1, T1 does not prescribe weights or an accuracy score; learners must publish their actual encoder weights, probe values and independent expected calculation before claiming a numerical result.

**Reference validity rules.** Every test states parameter ordering, matrix orientation, loss reduction, dtype, integer shape, train/eval setting and tolerances when relevant. Invalid/nonfinite input, empty batch, incompatible dimension, out-of-range embedding ID, stale gradients, zero-variance normalization, impossible split, leakage, failed checkpoint or unaffordable CPU budget must have a disclosed response. A single numeric toy calculation is not evidence of actual generalization, calibration, social fairness, real-world safety or deployment readiness. Public synthetic sources and ordinary local CPU computation suffice for all required work.

### Required summative assessments

- **AI5-AS1** (required differentiable architecture and independent backward trace)
  - **Outcomes:** AI5-O1, AI5-O2, AI5-O3, AI5-O4.
  - **Work:** Describe a bounded neural prediction task and why the selected nonlinear feedforward hypothesis differs from an AI4 baseline. Derive N1 forward values, loss, shapes, complete input/weight/bias gradients and parameter count independently. Implement or inspect an equivalent differentiable graph, compare autograd with the independent oracle and central differences away from nondifferentiability, and verify F1's XOR corner outputs. Introduce a wrong axis, missing activation derivative or intentionally detached tensor path and diagnose the resulting discrepancy.
  - **Criteria:** N1 prediction −1, loss 2, nine parameters, W1/W2/bias/input gradients and all shapes match the published oracle under declared row-vector/reduction conventions. F1 outputs 0,1,1,0 at its corners; the submission does not infer global generalization. Gradient numerical checks use appropriate tolerance and a differentiable point, with negative-case behavior that identifies the real defect rather than accepting a matching library printout alone.
  - **Evidence:** Hand-derived matrix/chain trace, named tensor shapes, exact oracle, reproducible source or equivalent independently inspectable computation, gradient-check method and tolerance, normal/negative cases and model-assumption limitations.

- **AI5-AS2** (required stable neural training and optimization failure diagnosis)
  - **Outcomes:** AI5-O2, AI5-O4, AI5-O5, AI5-O6, AI5-O16, AI5-O17.
  - **Work:** Implement a small model/training loop with documented batches, target contracts, scalar loss, zero-grad/backward/step ordering, correct initialization, training modes and split handling. Show a controlled one-step N1-equivalent update, a tiny-fit diagnostic, and a deliberately broken gradient accumulation, large update, saturation/dead-unit or NaN case. Compare two justified optimizer/update or initialization choices on the **same** tiny fixture, recording actual loss/gradients/runtime and a valid stopping decision. Verify a saved/restored fixed-probe prediction; distinguish inference checkpoint from resumable training state.
  - **Criteria:** The first controlled update is consistent with the independent N1 derivative and declared learning rate/loss reduction; gradients are not unintentionally reused between independent batches. Invalid shapes or nonfinite states are detected; the failure case is causally diagnosed using measured gradient/activation evidence and a meaningful repair/rejection test. Repeated stochastic training results are reported as observed rather than promised identical across devices; cleanup/reproduction and resource records work on a CPU.
  - **Evidence:** Local versioned source, exact numeric first-step oracle, loss/gradient traces, actual optimizer configuration/seeds, checkpoint probe, normal and broken-run outputs, clean-start commands and limitations.

- **AI5-AS3** (required normalization, dropout and regularization generalization investigation)
  - **Outcomes:** AI5-O5, AI5-O7, AI5-O8, AI5-O15.
  - **Work:** Derive D1's inverted-dropout mask output and exact specified batch-normalization calculation; independently compare train/eval behavior for a small implementation. On an appropriate synthetic classification/regression experiment, apply a justified dropout, normalization or early-stopping choice under one fixed leak-free selection contract, changing at least one factor while holding other controls constant. Show what fails if dropout is left active at inference, evaluation running statistics are inadvertently updated, or final-test records are used to select stopping time.
  - **Criteria:** D1 yields the published 2,0,6,0 training mask, unmasked evaluation vector and ±1/sqrt(2) batch-normalized values under the stated statistics; the explanation does not equate current batch statistics with generic evaluation running statistics. Train/validation/test fitting and stopping boundaries are enforced. Claimed regularization benefit is backed by actual comparable runs with observed variability; it is not inferred from training loss, a single seed, the mere presence of dropout or a leaky evaluation.
  - **Evidence:** Hand calculations, source/train/eval state inspection, actual ablation outputs with valid splits/selected checkpoint, negative leakage/mode trace, fitted-statistics provenance, and uncertainty/limits explanation.

- **AI5-AS4** (required spatial and ordered neural computation)
  - **Outcomes:** AI5-O2, AI5-O9, AI5-O10, AI5-O17.
  - **Work:** Derive C1 cross-correlation outputs, pooling values, output dimensions, shared parameter count and one changed stride/padding/channel case. Trace R1 exact recurrent state and input gradients; explain hidden-state reset and padding/mask boundaries. Implement or inspect one small convolutional layer and one short recurrent cell or transparent equivalent, verifying both against independent exact references. Compare parameter/resource implications against an explicit dense or nonrecurrent alternative without requiring a full computer vision or NLP benchmark.
  - **Criteria:** C1 produces [[3,7],[0,2]], pool max 7, mean 3 and parameter counts 4/5 under the declared bias convention. R1 yields 1, 5/2, 17/4 and derivatives 1/4,1/2,1. Changed geometry or sequence length receives correct new independent expectations, not copied outputs. Recurrent state is not carried across unrelated samples, padding does not silently alter valid targets, and workload/resources remain bounded.
  - **Evidence:** Exact matrix/shape/recurrence derivations, independent oracle/test code or equivalent complete finite trace, representative alternative architecture, invalid-state or padded-sequence case and measured/derived resource notes.

- **AI5-AS5** (required learned embeddings, reconstruction and self-supervision)
  - **Outcomes:** AI5-O11, AI5-O12, AI5-O13, AI5-O18.
  - **Work:** Compute E1 lookup/sum/mean and index failure independently. Implement or inspect a bounded embedding plus encoder/decoder or compact autoencoder on synthetic data, comparing a low-capacity bottleneck with an identity/constant reconstruction baseline. Derive P1's contrastive positive-versus-negative score and collapsed-similarity negative control. Show a reproducible synthetic view/pair construction whose augmentations preserve its stated semantic label/identity, then investigate a shortcut, false negative, collapse or uninformative reconstruction without claiming latent semantic discovery from appearance alone.
  - **Criteria:** E1 selects correct rows and aggregates (2,2)/(2/3,2/3), and rejects or explicitly handles index 3. P1 contrastive loss ≈0.313262 and identical-similarity control ln 2, with correct two-candidate/temperature assumptions. Actual reconstruction or contrastive experiments state input/output shape, fit-only transformation, information bottleneck and legitimate pairs, and provide concrete diagnostic evidence that separates a training objective from transferable useful representation. No unsupported language-retrieval or generative-model mastery is awarded.
  - **Evidence:** Hand-derived references, local source/probe output, reconstruction and pair-building fixtures, observed baseline/negative control results, learned-embedding inspection with caveats and independent limitations reasoning.

- **AI5-AS6** (required locally reproducible representation transfer and fair comparison)
  - **Outcomes:** AI5-O8, AI5-O14, AI5-O15, AI5-O16, AI5-O17, AI5-O18.
  - **Work:** Train a small source encoder locally on synthetic/permitted records, save its parameters and documented input/output contract, and compare a frozen-encoder linear head, a carefully bounded selectively unfrozen variant or explicitly justified omission, a train-from-scratch comparator and an AI4/constant baseline on a related target. Enforce train-only representation/normalizer fitting, nonoverlapping samples/groups where the target population requires them, honest model selection and an untouched final evaluation. Verify head/encoder dimensions and which parameters can receive/update gradients; record actual outcomes over sensible seeds, CPU time/parameter counts and at least one contamination, domain-shift or false-semantic-interpretation failure.
  - **Criteria:** The source and target relation, feature fit boundary and hypothesis are publicly stated; frozen parameters demonstrably remain unchanged, and selectively unfrozen parameters can change only under the declared optimizer/configuration. Compared variants use a fair data/metric/budget policy and documented randomness; actual rather than fabricated performance is shown, and no general transfer advantage is guaranteed. Clean restore and CPU feasibility are demonstrated. Claims are bounded to the observed synthetic task and do not equate an embedding neighborhood with factual causation or safe real-world inference.
  - **Evidence:** Local source/target generator or licensed source records, model/optimizer configuration, freeze/unfreeze trace, checkpoint-probe consistency, actual split/seed comparisons, runtime/parameter report, negative shift/leak/interpretation example and concise technically defensible limitations.

- **AI5-AS7** (required integrated small neural system and unfamiliar technical defense)
  - **Outcomes:** AI5-O1, AI5-O2, AI5-O4, AI5-O5, AI5-O8, AI5-O15, AI5-O16, AI5-O17, AI5-O18, AI5-O19, AI5-O20.
  - **Work:** Consolidate and **reuse** genuine prior AI5-AS1–AS6 evidence in one coherent locally runnable source/evidence collection; do not repeat six independent projects. Select one appropriate bounded neural learning question and a nontrivial architecture or learned representation feature, including a baseline, independent graph/shape oracle, training-loop proof, predeclared model-selection boundary, one honest final-evaluation report, resource measurements, negative case and limitations. The assessor supplies an **unfamiliar bounded** change such as a changed hidden dimension, weight sign, layer mode, sequence mask, convolution padding, embedding index, sample grouping, target availability, gradient operation or CPU budget. Before executing, independently predict the resulting shape/number/behavior or explain why the answer is unknown without new data; repair the implementation or safely refuse an invalid claim and verify unaffected behavior. Defend individual understanding in accessible written, recorded or live form.
  - **Criteria:** A reviewer can reproduce the actual code and results from clean input without paid services, hidden corpora, inaccessible compute or self-asserted metrics; all stated mandatory outcomes have separately inspectable evidence from the appropriate AS1–AS6 contracts, and integration adds new system and transfer evidence. The new case has a correct independent mathematical/input contract, a verified repair or justified refusal, and regression checks. A low training loss, green library test, a screenshot or a changed seed alone does not establish neural understanding, generalization, or O20. Train/validation contamination and unsafe external side effects are absent; memory/runtime limitations and untested claims remain explicit.
  - **Evidence:** Single reusable versioned repository or equivalent collection with source/provenance, exact public-oracle checks, dependency and seed instructions, selected model weights/checkpoints, actual training/selection/final evaluation outputs, independent references, normal/adverse/unfamiliar-case traces, resource/limitations report and attributable technical defense.

### Required outcome-to-assessment coverage

| Required outcome | Summative evidence |
| --- | --- |
| AI5-O1 | AI5-AS1, AI5-AS7 |
| AI5-O2 | AI5-AS1, AI5-AS2, AI5-AS4, AI5-AS7 |
| AI5-O3 | AI5-AS1 |
| AI5-O4 | AI5-AS1, AI5-AS2, AI5-AS7 |
| AI5-O5 | AI5-AS2, AI5-AS3, AI5-AS7 |
| AI5-O6 | AI5-AS2 |
| AI5-O7 | AI5-AS3 |
| AI5-O8 | AI5-AS3, AI5-AS6, AI5-AS7 |
| AI5-O9 | AI5-AS4 |
| AI5-O10 | AI5-AS4 |
| AI5-O11 | AI5-AS5 |
| AI5-O12 | AI5-AS5 |
| AI5-O13 | AI5-AS5 |
| AI5-O14 | AI5-AS6 |
| AI5-O15 | AI5-AS3, AI5-AS6, AI5-AS7 |
| AI5-O16 | AI5-AS2, AI5-AS6, AI5-AS7 |
| AI5-O17 | AI5-AS2, AI5-AS4, AI5-AS6, AI5-AS7 |
| AI5-O18 | AI5-AS5, AI5-AS6, AI5-AS7 |
| AI5-O19 | AI5-AS7 |
| AI5-O20 | AI5-AS7 |

**Completion decision.** All twenty AI5 outcomes require satisfactory, individually inspectable evidence under the applicable course revision across the seven summative assessments. A shared source tree and cumulative technical defense are encouraged, but no linked assessment ID substitutes for showing the underlying skill. Optional practice is not an extra admission or completion gate. Completion is not inferred from seat time, successful enrollment, passing a framework test, benchmark ranking without source data, automatic gradient output or a proprietary platform's badge. An assessor may offer accessible equivalent ways to demonstrate the same published capability without lowering its criteria.

### Optional open primary and academic references

- [PyTorch autograd mechanics](https://docs.pytorch.org/docs/stable/notes/autograd.html) — graph recording, gradient modes, in-place changes and derivative limitations.
- [PyTorch training loop](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html) — gradient reset, backward, optimizer update and train/eval lifecycle.
- [PyTorch numerical accuracy](https://docs.pytorch.org/docs/stable/notes/numerical_accuracy.html) — dtype/device variations and why bitwise equality across environments is not guaranteed.
- [PyTorch reproducibility source notes](https://github.com/pytorch/pytorch/blob/main/docs/source/notes/randomness.md) — stochastic operations, deterministic choices and honest reproducibility caveats.
- [PyTorch BatchNorm](https://docs.pytorch.org/docs/stable/generated/torch.nn.BatchNorm1d.html) — training-batch variance and separately tracked evaluation statistics.
- [Deep Learning (Goodfellow, Bengio, Courville)](https://www.deeplearningbook.org/) — freely accessible chapters on feedforward networks, regularization, optimization, convolutions, sequence modeling and representation learning.
- [PyTorch tensor and model basics](https://docs.pytorch.org/tutorials/beginner/basics/) — independently verifiable mechanics rather than compulsory hardware or paid accounts.

The references are optional supporting resources. The complete compulsory learning outcomes, public examples, assessments, criteria and independence conditions are already defined here.
