# AI9 — Transformers & Generative Modeling

**Program:** AI — AI Engineering
**Type:** course
**Prerequisites:** [AI8](AI8.md) — Computer Vision & Multimodal Learning (completed)
**Duration:** 20–26 weeks
**Status:** draft
**Specification:** v0.2.0
**Expected workload:** 10–15 focused hours/week (provisional; approximately 200–390 focused hours)

> [AI Engineering](README.md) · [Curriculum design guide](../DESIGN-GUIDE.md) · [Course format](../../spec/course-format.md) · [Evidence rules](../../spec/evidence-rules.md)

## Overview

**AI9 teaches the internal mechanisms and scientific limitations of transformers and generative models—not how to call an opaque hosted model.** A learner will independently derive scaled dot-product attention and valid masks, implement a small transformer and its autoregressive or encoder–decoder learning contract, compare exact next-token probabilities with decoded sequences, explain and test latent-variable, adversarial, invertible and diffusion/flow-based generative approaches, and construct a small bounded conditional model without claiming it has acquired human language or visual understanding. Generated outputs, rankings and losses are evidence to be interpreted against explicit data, target and provenance contracts; attractive samples are not proof of correctness, calibration, originality or permission to deploy.

**History, use and disciplinary context.** Attention-based encoder–decoder methods and the 2017 transformer architecture enabled parallelizable sequence representations with content-dependent context selection. Autoregressive modeling estimates token or discrete-element likelihood from preceding context; masked/denoising learning reconstructs deliberately hidden input. Separately, variational latent models optimize a marginal-likelihood lower bound; adversarial generators learn through a discriminator; normalizing flows transform known densities with tractable Jacobians; diffusion/score-based and flow-matching methods learn to transport noisy or base distributions toward data. These distinct objective families support language generation, finite structured-data synthesis, constrained image-like sampling and research on multimodal conditioning. No architecture ensures factuality, secure output, sample diversity, correct authorship attribution, compositional grounding, or distributional fidelity just because samples are fluent.

**Prerequisite ownership and academically necessary scope.** Direct prerequisite is completed [AI8](AI8.md), which transitively includes [AI7](AI7.md) (tokenization, language modeling baselines and information retrieval), [AI5](AI5.md) (backpropagation, PyTorch-style autograd, feedforward/recurrent networks, embeddings and contrastive representations), [AI4](AI4.md) (generalization/evaluation), [AI2](AI2.md) (probability, likelihood, calculus and optimization), [AI1](AI1.md) (data provenance) and SEF. AI8 contributes image/text pairing and bidirectional multimodal alignment. **AI9 does not reteach** these subjects; it assesses their new applications to *query/key/value attention and masks*, positional information, encoder/decoder and cross-attention architectures, the stochastic distribution learned by an actual generator, generation algorithms and caches, ELBO-based latent sampling, discriminator/generator objectives, invertible densities, diffusion denoising and conditional generative validity. [AI6](AI6.md) reinforcement learning and [AI3](AI3.md) classical planning are not prerequisites and are not silently re-assessed.

**Protected neighboring courses.** AI10 owns advanced finetuning and adaptation, resource-aware large-model training, instruction tuning and parameter-efficient adaptation at scale; AI11 owns retrieval-augmented answer generation and grounded citation pipelines; AI12 owns tool-using agent systems; AI13 owns comprehensive evaluation, red-teaming and reliability assurance; AI14 owns cross-system security, governance and responsible-use management; AI15 owns deployed model serving and MLOps. AI9 may examine hallucination, contaminated validation, memorization or generation misuse as *generative-model evidence boundaries*, not claim those later courses are complete. No large language model, instruction-following chat service, diffusion-image service, web-scale pretrained checkpoint, expensive GPU, secret benchmark or paid data is required. A sampled symbol sequence or synthetic 1D distribution is enough to establish the mathematics; no generated imagery or voice recording is mandatory.

**Evidence and accessibility.** Learners work locally with small open/synthetic integer-token corpora, finite attention matrices, small neural weights, synthetic continuous distributions and optional low-resolution numeric images. Python 3 with a small CPU-enabled open tensor/autograd library is a convenient reference, with independently reviewable equivalent implementations allowed. Bounded experiments must disclose source and train/validation/test identity, token/position/positive-pair rules, exact architectural shape and dtype, stochastic seeds, loss reductions, permissible tolerances, CPU budget, stopping criteria, evaluation protocol, data rights, and what is not measured. Numeric matrices, generation traces and tables must have accessible text equivalents. Observed training quality and runtime must be reported from actual runs—never invented, imposed as universal fixed outcomes, or taken from unrelated papers.

**Architecture follows competencies rather than a module quota.** The course proceeds through generative contracts, mathematical attention, transformer designs, model objectives, controlled decoding, latent and adversarial/invertible families, diffusion/flow methods, conditional multimodal mechanisms, evaluation and independent transfer. Modules are grouped when their scientific mechanisms form one coherent responsibility; no artificial "one module per technique" rule applies. Required evidence consists of **eight cumulative summative assessments** mapping all twenty-two observable outcomes. A single coherent local source collection can carry the numerical oracles and small model experiments; there is no requirement to build eight separate production models. The week range is provisional, not learner-tested or a conformance claim, and educational status remains `draft`.

## Learning outcomes

- **AI9-O1:** Define a bounded generative or transformer-learning question with an explicit probability/conditional target, representation, authorized data, model comparator, output interpretation, evaluation population and limits on claims.
- **AI9-O2:** Calculate scaled dot-product attention outputs with exact query/key/value dimensions, numerically stable row softmax, independent weight/oracle checks and appropriate invalid-shape handling.
- **AI9-O3:** Construct and verify causal, padding, bidirectional and cross-attention visibility masks, including empty/all-masked rows, target-position and variable-length failure cases that would reveal forbidden information.
- **AI9-O4:** Explain and independently trace multihead projections, residual connections, normalization and feedforward mixing, counting learnable parameters and recognizing how head width and sequence length change resource use.
- **AI9-O5:** Analyze and implement positional-information and encoder-only, decoder-only and encoder–decoder/cross-attention designs, defending what information is visible and what each architecture can represent or generate.
- **AI9-O6:** Implement or inspect a tiny, correctly shaped and differentiated transformer model with reproducible training/inference modes, loss masks, updated parameters and mathematically justified gradient/shape checks.
- **AI9-O7:** Construct correct autoregressive next-token, masked/denoising-token and conditional teacher-forcing training examples, rejecting target leakage, evaluation contamination and wrong beginning/end/padding conventions.
- **AI9-O8:** Compute and interpret token-level negative log likelihood, cross-entropy and perplexity under an explicit denominator and sequence/tokenization policy; compare actual generative training with an appropriate pre-existing statistical baseline.
- **AI9-O9:** Generate and verify discrete sequences with greedy, sampled top-k/nucleus/temperature and bounded beam-search policies, respecting normalized probabilities, EOS, stop and hard output constraints.
- **AI9-O10:** Inspect cached causal decoding and context/memory/time tradeoffs, reproducing a small cached-versus-uncached continuation and diagnosing invalid position/cache updates or masked future access.
- **AI9-O11:** Specify and independently derive marginal likelihood, approximate posterior, ELBO, KL and reparameterization mechanics for a small latent-variable generator, stating precisely what the variational bound guarantees.
- **AI9-O12:** Build, test and compare a small CPU-feasible latent-variable/variational autoencoder with source-only training, controlled samples, reconstruction/reparameterization cases and posterior-collapse/likelihood limitations.
- **AI9-O13:** Derive and inspect bounded generator/discriminator adversarial objectives and updates, implement a tiny synthetic adversarial learning example, and diagnose saturation/mode collapse, sample cherry-picking or unsupported likelihood claims.
- **AI9-O14:** Derive an invertible transformation's density via change-of-variables and verify support, Jacobian and sampled value; distinguish flow likelihood, invertibility and resource limitations from adversarial and latent objectives.
- **AI9-O15:** Derive and verify finite forward diffusion/noising distributions, noise-schedule coefficients, epsilon-prediction loss and signal/noise reconstruction, including a deliberately wrong schedule or label.
- **AI9-O16:** Implement and inspect a small local denoiser and a fully specified bounded reverse sampler or linear flow-matching objective, stating the required variance/transition/interpolation assumptions and demonstrated sampling limitations.
- **AI9-O17:** Formulate and inspect conditional generation via encoder–decoder cross-attention or compact image/text conditioning, preserving correct pairing, source/target visibility, modality availability and unauthorized-data boundaries.
- **AI9-O18:** Compare conditional versus unconditional generation under deliberately changed or contradictory context, and explain when guidance, model shortcuts, duplicated pairs or missing context invalidate apparent grounding.
- **AI9-O19:** Design and execute reproducible generative comparisons of likelihood-based fit, distributional coverage/diversity, conditional correctness and failure cases with valid baselines, metrics, sample supports and uncertainty.
- **AI9-O20:** Enforce generative-data provenance, licensing, privacy, contamination controls, output restrictions and honest limitations for memorization and unreliable content; distinguish model output from verified factual or authorized material.
- **AI9-O21:** Produce a clean-start, CPU-feasible evidence collection with exact synthetic references, model/mask/token/seed versioning, true measured behavior, regression and negative cases, accessible artifacts and resource accounting.
- **AI9-O22:** Respond to an unfamiliar bounded change to attention mask, positional index, loss shift, decoder option, latent objective, denoising schedule, conditioning pair, access restriction or generator evidence claim by predicting the mathematical/behavioral consequences, repairing or declining an invalid result, and defending the decision.

## Modules

### Module 1 — Generative Questions and Truthful Evidence

#### Outcomes

- AI9-O1
- AI9-O19
- AI9-O20

#### Lessons

1. **Models of data versus predictions about data** — Contrast conditional token probabilities, joint latent-variable models and implicit samplers with AI4's supervised label decision; name the distributions each can and cannot estimate.
2. **History and distinct generative objectives** — Place sequence autoregression, transformers, variational inference, GANs, flows and diffusion/flow matching into an objective-based map without treating every method as a replacement for another.
3. **Representation, sampling unit and legitimate data** — Specify token sequence, complete image-like array, latent draw and image-caption pair, including sources, grouping, licenses and what a generated output is permitted to reveal.
4. **Baseline and measured success contract** — Choose a count/bigram baseline, simple conditional table or known synthetic density; separate held-out likelihood from sample diversity, physical plausibility, instruction-following and safety.
5. **Small-model budget and negative-evidence plan** — Predeclare CPU/time/sequence length, random seeds, independent exact references and an example that should be refused, not glossed over by a fluent generation.

### Module 2 — Scaled Attention, Visibility and Mathematical Checks

#### Outcomes

- AI9-O2
- AI9-O3
- AI9-O4

#### Lessons

1. **From fixed context to data-dependent weighting** — Identify why a content-weighted lookup differs from AI5's learned embedding table, convolution and recurrent hidden-state recurrence, using a small finite sequence.
2. **Q/K/V and shape compatibility** — Define Q∈R^(Lq×d), K∈R^(Lk×d), V∈R^(Lk×dv), batch/head dimensions and where dimensions must agree for QKᵀ and weighted values.
3. **Dot-product scaling and row normalization** — Compute A1's exact diagonal/off-diagonal similarity values under division by sqrt(d); independently derive normalized row softmax and output matrix.
4. **Stable softmax and extreme scores** — Compare subtract-row-maximum exponential calculation with naive exponentiation overflow and distinguish mathematical probabilities from approximate floating-point implementation.
5. **Causal visibility by query/key position** — Trace A1 with future key 1 blocked from query 0, while query 1 may see past and itself; reject the mistaken transposition of key/query masks.
6. **Padding and invalid all-masked rows** — Explain why padding keys are hidden and padding queries require loss/aggregation exclusion, while softmax over no permitted keys has no ordinary finite probability distribution.
7. **Cross-attention mask dimensions** — Build source length 3 versus target length 2 visibility and identify why a target-token future mask must not be substituted for a source-key padding mask.
8. **Multihead projections and recombination** — Trace independent heads with fixed width, concatenation and output projection, verifying B1 weight count and observing that heads do not guarantee complementary semantics.
9. **Attention negative controls and complexity** — Test a future-token perturbation that must leave earlier causal output unchanged, a bad dimension and a forbidden source key; derive quadratic score-matrix size in sequence length.

### Module 3 — Transformer Blocks, Position and Architecture Choice

#### Outcomes

- AI9-O4
- AI9-O5
- AI9-O6

#### Lessons

1. **Positional information and permutation symmetry** — Show why content-only self-attention without positional or other order information cannot generally distinguish certain permutations, and inspect sinusoidal/learned positions on a fixed pair.
2. **Absolute, relative and rotary position assumptions** — Compare their information and extrapolation conventions, including what happens when position offsets restart incorrectly after a cached prefix; no state-of-the-art kernel implementation is required.
3. **Residual and normalization layouts** — Trace pre-norm versus post-norm data/gradient paths in a simple block, naming which tensor is added and which statistics define each normalization.
4. **Position-wise feedforward mixing** — Derive a small transformer's per-position MLP output shape, compare it with cross-token attention and calculate parameters separately from the attention projections.
5. **Encoder-only bidirectional block** — Build an allowed-attention table for an encoder, state why a masked reconstruction/embedding objective differs from next-token generation and reject unearned access restrictions.
6. **Decoder-only causal stack** — Trace one autoregressive inference step with a causal self-attention mask and correct position, distinguishing parallel teacher-forced training from left-to-right sampling.
7. **Encoder–decoder and cross-attention** — Separate source encoder states, decoder prefix states and target labels; derive Q from decoder and K/V from encoder with explicit source-pad and target-causal rules.
8. **Independent tiny forward/backward fixture** — Implement or inspect a bounded 1–2-layer transformer, verify A1/B1-style shape/parameter and gradient checks, and reject a flawed residual/positional/mask variant.

### Module 4 — Learning Objectives and Small Transformer Experiments

#### Outcomes

- AI9-O6
- AI9-O7
- AI9-O8
- AI9-O19

#### Lessons

1. **Teacher-forcing input and next-token target shift** — Trace L1's BOS, A, EOS sequence, inputs BOS/A, targets A/EOS and legal loss positions; reject a same-position label leak.
2. **Causal cross-entropy and perplexity** — Compute L1's held-out probabilities, sum/mean NLL and perplexity with exactly two valid tokens, distinguishing a different tokenizer's denominator.
3. **Masked reconstruction objective** — Construct an input with one explicit MASK position and compute loss only on chosen target positions, noting that bidirectional corrupted-input access differs from causal generation.
4. **Encoder–decoder supervised generation objective** — Derive one small source/target example with BOS-shifted decoder input, EOS target and source padding, and justify independent source/target attention masks.
5. **Training/validation grouping and provenance** — Split before chunking overlapping sequences or augmenting paired data, document vocabulary, source revision and forbidden target exposure, and reserve final test sequences for one evaluation.
6. **Count/bigram versus tiny transformer** — Train a CPU-scale model on a fixed synthetic grammar/task and compare real held-out NLL/perplexity with an honest count-based baseline under matched token and evaluation contracts.
7. **Failure of fluent memorization** — Include duplicate text, repeated training sequence and invalid distribution-shift test, disclosing that low training cross-entropy or copying a memorized passage proves no independent generalization.
8. **Implementation-independent error report** — Save model/checkpoint and tokenizer/mask configuration, report actual parameter counts, train steps, loss traces and an independent manual loss/gradient reference rather than trusting framework output alone.

### Module 5 — Decoding Algorithms, Caches and Inference Bounds

#### Outcomes

- AI9-O8
- AI9-O9
- AI9-O10
- AI9-O20

#### Lessons

1. **Probability to emitted sequence** — Distinguish maximum-likelihood token from the most likely *complete* sequence and from a random draw; define EOS/stop and finite context.
2. **Greedy versus small beam exploration** — Derive D1's example where greedy A–EOS has probability 0.30 while B–EOS has 0.36, with exact fixed two-step complete-sequence semantics.
3. **Temperature and probability calibration** — Compute the effect of rescaling two known logits by temperature T and explain that lower entropy under temperature scaling does not certify factual accuracy.
4. **Top-k and nucleus sampling** — Normalize D1's filtered candidate probabilities; define stable ties, whether sampling may include EOS and a top-p cumulative-mass cutoff with no invented deterministic sample.
5. **Length effects and repetition** — Compare explicit length-normalized versus raw log sequence scores and diagnose a repeated-token loop; a single decoding heuristic is not a universal hallucination cure.
6. **Cache equivalence of causal continuations** — Compare prefill+one-step key/value cache against a full causal forward pass on the *same* visible prefix at matched positions/masks, with a tolerance and valid cache shape.
7. **Failure under incorrect offset, pad or future state** — Show how stale cache, missing position increment, invalid padding or reading later tokens alters an earlier prediction, violating the declared causal contract.
8. **Compute and stop policy** — Derive attention memory O(L²) for full score matrices versus O(L) cached key/value storage per layer under fixed width, disclose actual CPU timing, output length, forbidden tokens and early-stop consequences.

### Module 6 — Latent-Variable Models and Variational Autoencoders

#### Outcomes

- AI9-O11
- AI9-O12
- AI9-O19

#### Lessons

1. **Observed versus latent random variables** — Factor a small p(x,z)=p(z)p(x|z) and independently derive the finite marginal p(x)=sum_z p(z)p(x|z), contrasting inference with generation.
2. **Approximate posterior and KL divergence** — Define q(z|x) and KL(q||p) on a finite example with normalized support, explaining why zero-probability support mismatches cannot be silently ignored.
3. **ELBO and exact finite verification** — Derive V1's variational evidence bound and calculate the expected reconstruction log-probability, KL and exact matched-posterior case without misreporting it as a guaranteed high sample quality.
4. **Gaussian reparameterization and gradient ownership** — Derive z=mu+sigma·epsilon with epsilon sampled from a declared base and calculate a one-dimensional Gaussian KL with known variance/covariance assumptions.
5. **Small continuous/discrete latent generator** — Train or inspect a locally runnable low-dimensional VAE with a documented prior, encoder, decoder and source-only fitting; inspect actual generated samples and reconstructions.
6. **Posterior collapse and rate–distortion tradeoff** — Diagnose a model that ignores its latent, document reconstruction/regularization changes and refuse a unique semantic meaning for an arbitrary latent axis.
7. **Held-out likelihood evidence and limitations** — Compare valid ELBO/reconstruction evidence and simple known-density baseline while distinguishing an exact marginal likelihood for a toy distribution from an approximate bound on real observations.

### Module 7 — Adversarial and Invertible Generative Families

#### Outcomes

- AI9-O13
- AI9-O14
- AI9-O19

#### Lessons

1. **Explicit density versus implicit sampling** — Contrast a tractable p(x), a bounded variational lower bound and a generator whose samples are available without an explicit normalized likelihood.
2. **Adversarial discriminator and generator losses** — Derive G1's finite real/fake logistic discriminator and non-saturating generator losses, keeping their parameter ownership and gradient directions separate.
3. **Alternating optimization in a tiny 1D GAN** — Train or inspect a CPU-only synthetic one-dimensional adversarial generator/discriminator with measured instability and explicitly declared real/fake source distributions.
4. **Mode collapse, saturation and unearned evidence** — Demonstrate a constant-output or narrow-support generator and show why cherry-picked samples or a discriminator loss by itself cannot establish distribution coverage.
5. **Invertibility and Jacobian change of variables** — Derive F0's y=2z+1 density, support and log-Jacobian, rejecting a zero-scale noninvertible transformation and a missing density correction.
6. **Coupling/flow architecture reasoning** — Explain a simple affine coupling or compositional invertible transform with tractable inverse/log determinant and derive its shape and computational limitations.
7. **Fair objective-family comparison** — Compare the toy flow's exact density, VAE's ELBO and GAN's sample-only diagnostics on what each *actually estimates*; do not report incompatible metrics as an ordered universal leaderboard.

### Module 8 — Diffusion, Denoising and Flow-Matching Dynamics

#### Outcomes

- AI9-O15
- AI9-O16
- AI9-O19
- AI9-O21

#### Lessons

1. **Markov noise corruption and schedules** — Specify forward q(x_t|x_(t−1)) under a finite beta/alpha schedule and distinguish instantaneous alpha from cumulative alpha-bar.
2. **Closed-form forward marginal** — Derive x_t=sqrt(alpha-bar_t)x0+sqrt(1−alpha-bar_t)epsilon for a Gaussian base and independently calculate P1's known x0/noise realization.
3. **Noise prediction and reconstruction** — Compare exact epsilon-prediction loss with a wrong predicted noise and invert the same forward equation to infer a candidate x0 under fixed alpha-bar.
4. **Timesteps as conditioning inputs** — Show why one denoiser needs its timestep/noise level and how a missing or misindexed timestep corrupts the declared training target.
5. **Finite reverse sampling contract** — Construct an explicitly parameterized one- or few-step reverse kernel with mean, variance, noise draw and stop rule; do not hallucinate a unique reverse sample from a forward-only equation.
6. **Denoiser on synthetic low-dimensional data** — Train or inspect a tiny CPU-scale epsilon predictor with fixed schedule, observed numerical losses and source-only normalizer, reporting actual samples and nonconvergence.
7. **Deterministic versus stochastic samplers and guidance** — Compare the assumptions for a chosen deterministic/stochastic reverse rule and explain that stronger conditional guidance can harm diversity or create unsupported conditional outputs.
8. **Score field and denoising intuition** — Explain under a defined Gaussian corruption how denoising/noise estimation relates to a score field, keeping the noise distribution and parameterization explicit.
9. **Linear flow-matching reference** — Calculate P2's x(t) and target velocity in a fully stipulated linear interpolation and contrast a supervised velocity target with a reverse-diffusion noise objective.
10. **Sampling diagnosis, error and cost** — Compare a changed schedule, wrong timestep, incomplete reverse kernel or pathological extrapolation, measuring actual steps/CPU and disclosing what a small synthetic sampler does not establish.

### Module 9 — Conditional and Multimodal Generation

#### Outcomes

- AI9-O5
- AI9-O17
- AI9-O18
- AI9-O20

#### Lessons

1. **What the condition actually authorizes** — Define p(y|x), source image/text context IDs, permitted source visibility and output obligations, distinguishing conditional likelihood from grounded truth.
2. **Cross-attention conditioned decoder** — Build a tiny source–target mask and cache contract where target queries attend only authorized encoder keys and their own past target tokens.
3. **Visual and language condition pairing** — Apply AI8's already-assessed image/text identity and positive pair rules to a small numeric-grid–symbol generator, rejecting a swapped caption or a forbidden image.
4. **Conditional/unconditional control experiment** — Compute C1's two exact categorical conditional probabilities and compare a condition-ignoring constant model with the declared matched/mismatched source input.
5. **Condition dropout and guidance limitations** — Analyze a declared classifier-free conditioning path or a simple conditional/unconditional mixture, noting that an altered guidance parameter changes the sampling objective and is not a factuality guarantee.
6. **Missing, contradictory and restricted context** — Give an invalid image, absent caption, conflicting source or private sample a documented fallback/refusal, including effects on generation and access permissions.
7. **Measured conditional correctness and blind spots** — Compare actual small held-out conditional/unconditional samples, count support under changed scene/text context, and separate syntactic validity, visual accuracy and unobserved semantics.

### Module 10 — Evaluation, Reproducibility and Generative Failure

#### Outcomes

- AI9-O8
- AI9-O9
- AI9-O19
- AI9-O20
- AI9-O21

#### Lessons

1. **Validity, likelihood, diversity and use** — Select metrics matched to discrete sequence likelihood, generated sample distribution, duplicates/coverage and conditional correctness, rather than selecting one flattering output.
2. **Likelihood comparability and token denominators** — State which datasets, tokenizers, loss masks and discrete vocabularies make NLL/perplexity meaningfully comparable, and what a continuous density value measures instead.
3. **Quality/diversity and evaluation population** — Compare synthetic histogram support and duplicate rates to known generating distribution with finite sample counts, disclosing low-sample variance and metric blind spots.
4. **Sampling variance and cherry-picked examples** — Fix seed lists, output budgets, prompt/source conditions and failure reporting before inspecting outputs; demonstrate a plausible example that hides a systematic failure.
5. **Source duplication and memorization boundary** — Detect a generated fragment copied from a held-out or unauthorized source, split grouped data correctly and avoid presenting a toy exact-match test as general privacy protection.
6. **Reproducibility of training and sampling** — Pin tokenizer, attention mask, positional state, architecture, scheduler/sampler, random generators, checkpoint and precision/device differences; confirm a clean local rerun.
7. **Resources and unsupported runtime claims** — Record actual CPU steps, model parameters, sequence length, attention matrices, sampling iterations and memory, distinguishing measured costs from scaling laws.
8. **Rights, uncertainty and human inspection** — Document permitted training/generation use, refusals, impossible/unsafe outputs, non-verifiable claims and appropriate expert review without claiming AI13/AI14/AI15 competence.

### Module 11 — Integrated Generative Investigation and Unfamiliar Defense

#### Outcomes

- AI9-O1
- AI9-O6
- AI9-O19
- AI9-O20
- AI9-O21
- AI9-O22

#### Lessons

1. **Select one bounded generative engineering question** — Choose a synthetic discrete grammar/conditional token task or low-dimensional generative distribution, with distinct authorized training/evaluation sources, real baseline and CPU budget.
2. **Reuse the actual mathematical and model evidence** — Consolidate legitimate earlier attention/transformer, decoder, VAE, GAN/flow and diffusion cases without rebuilding all generative families again or claiming all are interchangeable.
3. **Controlled model and sample comparison** — Run the appropriate tiny selected generator and baseline, reporting actual loss/conditional validity/coverage under a predeclared evaluation protocol and independent exact reference.
4. **Adverse generation and source constraints** — Demonstrate a leaky mask, corrupted target shift, mode collapse, wrong diffusion schedule, false condition, stale cache or unauthorized training/sample use with a safe repair/refusal.
5. **Unfamiliar assessor-supplied change** — Predict a bounded changed attention mask, position, decoding probability, latent prior, scheduler, paired input or source-permission result *before* using implementation output; verify a new reference or state clearly why it is not identified.
6. **Independent reproducibility and technical defense** — Produce an individually attributable, accessible audit of the learned mechanism, what was measured, runtime/corpus rights, unchanged regression cases and why fluency/realism cannot substitute for scientific evidence.

The number and lengths of these modules follow the distinct concepts above, not a preselected per-course quota. Lessons are coherent instructional responsibilities; a learner is **not** required to produce a lab/test submission after each lesson or module. The eight summative contracts below, not time or activity completion, establish outcome evidence.

## Completion requirements

### Finite public reference cases and conventions

These exact local fixtures anchor independent evaluation. Their values apply **only under the stated assumptions** and must not be treated as observed model performance, probabilistic safety certification or evidence that a model learned semantic meaning.

**A1 — Two-token scaled attention and causal visibility.** Q=K=[[1,0],[0,1]], V=[[2,0],[0,4]], query/key width d_k=2, no batch/head axes in this finite example. Unmasked score matrix QKᵀ/sqrt(2)=[[1/sqrt(2),0],[0,1/sqrt(2)]]. Let p=exp(1/sqrt(2))/(exp(1/sqrt(2))+1) and q=1−p, so the row-softmax weights are [[p,q],[q,p]]. The **unmasked output** is [[2p,4q],[2q,4p]]. With an *inclusive causal mask* where earlier queries cannot access a later key, the first query attends only to key0, and the second still attends to both: the causal output is **[[2,0],[2q,4p]]**. The first causal row must be unchanged if key1/value1 is modified; a system that produces a different first-row result under this change leaks future information. A query row with all keys masked has **no defined usual softmax distribution** and requires explicit rejection/skip rather than division by zero. A target length2/source length3 cross-attention weight matrix must have shape 2×3, not 2×2, and any source padding must be excluded by its own mask.

**B1 — Multihead parameter and positional contract.** For d_model=4, two attention heads with d_k=d_v=2, use four **bias-free** trainable projections W_Q,W_K,W_V,W_O each of shape 4×4. Total attention-projection parameters: **4×16=64**. This excludes MLP, layer normalization, token/position embeddings and all biases. For the standard sinusoidal scheme at position 0 in four dimensions the positional vector is **(0,1,0,1)** (sin channels then cos channels alternating), with different defined position vectors for later positions; a cache must preserve their absolute or appropriately relative position conventions. Changing the number of heads at fixed d_model is not automatically a fourfold parameter increase, and a position vector does not guarantee extrapolation or physical time knowledge.

**L1 — Next-token target shift and perplexity.** Let the finite sequence be [BOS,A,EOS]. Correct decoder training input is **[BOS,A]** and next-token targets **[A,EOS]**, with all two target positions counted and no pad tokens. Suppose the model assigns the **correct targets** conditional probabilities 1/2 and 1/4, respectively. Sum NLL=−ln(1/2)−ln(1/4)=**ln 8**; mean token NLL=(ln 8)/2=**ln sqrt(8)**; per-token perplexity is **sqrt(8) ≈ 2.828427**. If probabilities are evaluated under a different tokenization, masked/padded target support or on the training records, they do not justify a comparable independent generalization claim. A causal model at the BOS position must not read A or EOS while predicting A.

**D1 — Greedy, beam and filtering with explicit completion.** A conditional token generator has first-token distribution P(A)=3/5, P(B)=2/5. On the next and final step P(EOS|A)=1/2 and P(EOS|B)=9/10, with remaining probability on a non-EOS alternative. Thus complete two-step sequence probabilities are P(A,EOS)=**3/10** and P(B,EOS)=**9/25**; greedy first chooses A, but a width-two **un-normalized complete-sequence beam comparison restricted to the two EOS-complete alternatives** prefers B,EOS (9/25>3/10). Separately, for a one-step distribution (A=.5,B=.3,EOS=.2), top-k=2 keeps A,B, giving renormalized probabilities **5/8,3/8**; nucleus p=.7 also keeps the smallest ranked set {A,B} with accumulated original mass .8 and the same renormalization. With logits (ln 2,0) over two choices, temperature T=1 yields (2/3,1/3), while T=1/2 yields (4/5,1/5). No fixed random token is promised; actual samples require a disclosed RNG. EOS stop rules, hard token restrictions and length-score definitions must be explicitly specified. Greedy decoding is not claimed optimal for the complete sequence.

**V1 — Finite latent variable and an exact ELBO.** Let z∈{0,1} have prior p(z=1)=p(z=0)=1/2, and for observed x=1, likelihoods p(x=1|z=1)=3/4 and p(x=1|z=0)=1/4. Then marginal p(x=1)=(1/2)(3/4)+(1/2)(1/4)=**1/2**, so log evidence=**−ln2**. Choose q(z=1|x=1)=3/4, q(z=0|x=1)=1/4, equal to this finite example's exact posterior. The ELBO **sum_z q(z|x)ln p(x|z)−KL(q(z|x)||p(z))** equals **−ln2**: the reconstruction term is (3/4)ln(3/4)+(1/4)ln(1/4), and the KL term is (3/4)ln(3/2)+(1/4)ln(1/2). This equality occurs because q equals the exact posterior, **not** because every VAE bound is tight or because generation will be high quality. For a separate one-dimensional Gaussian reference q=N(mu=1,sigma²=1), p=N(0,1), the diagonal-Gaussian KL is **1/2**. Reparameterization samples z=mu+sigma·epsilon with epsilon from the stated normal base; a sample is not itself an ELBO or marginal-likelihood evaluation.

**G1 — GAN losses and invertible flow densities.** In a distinct toy logistic discriminator evaluation, suppose D(real)=4/5, D(fake)=1/4. The **discriminator loss** −ln D(real)−ln(1−D(fake)) is **−ln(3/5)=ln(5/3)**; the separate non-saturating **generator loss** −ln D(fake)=**ln4**. They apply to distinct parameter objectives/updates and do not establish sample diversity or likelihood. For an *invertible normalizing flow* let z~Uniform(0,1), y=2z+1; y has support (1,3) and density **p_y(y)=1/2**, so the log density within support is **−ln2** and zero density outside. The scale-zero map y=1 is not invertible and cannot reuse the finite log-Jacobian correction; neither the GAN discriminator score nor the flow Jacobian alone certifies real-world generation quality.

**P1 — Forward diffusion, denoising and reconstruction.** Use a one-dimensional Gaussian forward marginal with **alpha-bar=1/4**, clean datum x0=2 and a **specified** noise draw epsilon=−1. Then x_t=sqrt(1/4)·2+sqrt(3/4)·(−1)=**1−sqrt(3)/2 ≈ 0.1339745962**. An epsilon predictor output −1 has squared noise-prediction error **0** on this one sample; predictor 0 has squared error **1**. Under the correct known noise, x0 reconstructed as [x_t−sqrt(3/4)·epsilon]/sqrt(1/4) returns **2**; if epsilon is wrongly estimated as 0, the same arithmetic gives **2−sqrt3 ≈ 0.2679491924**. These results are for a specified Gaussian corruption *marginal*; a unique reverse diffusion trajectory cannot be inferred without an explicit schedule, reverse mean/variance, timestep and sampling noise choice. Zero squared error on one observation is not general denoising skill.

**P2 — Finite flow-matching interpolation.** For a **stipulated deterministic linear path** x(t)=(1−t)x_source+t x_target with x_source=0,x_target=2, at t=1/4 the state is **1/2** and its velocity dx/dt=x_target−x_source=**2**; at t=3/4 the state is **3/2** and target velocity remains **2**. A predicted field of 2 has zero squared velocity error on these two reference points. This exact conditional path does **not** specify an entire generative population, a learned ODE solver, a universally valid optimal transport, or a diffusion reverse kernel. The learner must state the base/endpoint pairing and training/sampling process to make further distributional claims.

**C1 — Image/text conditioning and an invalid ground-truth claim.** In a two-class A/B **synthetic conditional toy**, an explicitly stipulated conditional model assigns P(A|source=image1)=3/4 and P(A|source=image2)=1/4; a condition-ignoring baseline assigns P(A)=1/2 for both. For a true A label, the **negative log scores** are ln(4/3), ln4 and ln2 respectively. A caption shuffled between these two source IDs invalidates the original pairing and cannot be evaluated with an unchanged positive-pair assumption. Conditional dependence on the image is demonstrated by the differing stipulated distributions, *not* by factual correctness on unseen scenes. Missing/restricted context requires an authorized, declared fallback or refusal; silently reusing someone else's private image is not an alternative data source.

**Shared exact-evidence rules.** Reference values depend on the stated model, natural-log conventions, half-open token sequences, architecture shapes, loss reductions, normalized distributions and known input/label conditions. Always identify numerical precision and tolerance. Intentionally invalid examples include wrong QK width, masked-future access, all-masked attention row, missing cached position, target shift leak, zero-temperature or zero-probability log, latent unsupported KL, noninvertible flow, wrong noise schedule, omitted reverse-kernel variance, duplicate conditioning pairs, and unauthorized or contaminated sample. Learners may supply equivalently precise independently verifiable fixtures, but actual model evaluation, sampling diversity, training stability and CPU costs must be executed and reported honestly.

### Required summative assessments

- **AI9-AS1** (exact attention, masks and transformer architecture)
  - **Outcomes:** AI9-O2, AI9-O3, AI9-O4, AI9-O5, AI9-O6.
  - **Work:** Independently calculate A1's unmasked and causal weighted outputs, document full Q/K/V and source/target dimensions, construct masks for causal, bidirectional, padding and cross-attention cases, and derive B1's parameter/position oracle. Implement or rigorously inspect a tiny 1–2-layer transformer with residual/normalization/MLP and an encoder, decoder or cross-attention mode, using AI5 gradient checking to prove a nontrivial parameter path is differentiable. Introduce a future-key perturbation, all-masked row, wrong position, mismatched cross-source length or incompatible projection and predict the invalid/new result before running it.
  - **Criteria:** A1 produces [[2p,4q],[2q,4p]] unmasked and [[2,0],[2q,4p]] causal under p=exp(1/sqrt2)/(1+exp(1/sqrt2)), with the first causal row unchanged by future-key/value variation. B1 projects with 64 bias-free attention weights and position0 (0,1,0,1). Batch/head/MLP and source/target masks are explicit and correct; no all-masked row is silently softmaxed. The architectural and gradient demonstration is independently checked, not merely a library output screenshot.
  - **Evidence:** Finite hand-derived attention/projection/position trace, source/configuration and actual forward/backward proof, normal and deliberately invalid masks, shape and resource calculations and independently reviewable explanation.

- **AI9-AS2** (objective choice, transformer training and token-level evidence)
  - **Outcomes:** AI9-O1, AI9-O6, AI9-O7, AI9-O8, AI9-O19, AI9-O21.
  - **Work:** Define a tiny permitted symbolic language or bounded source-to-target task. Derive L1's BOS/next-token shift, NLL and perplexity independently; implement a small CPU transformer autoregressive or encoder–decoder learner with correct tokenizer, padding, source/target mask, loss support and gradient lifecycle. Demonstrate a masked-reconstruction objective contract, even if the chosen primary trained model is autoregressive, including valid bidirectional input access and loss positions. Compare actual held-out NLL and generated sequence behavior against a valid count/bigram baseline without training on held-out sequences or consulting final test output during tuning; provide a deliberate label-shift or same-sequence contamination negative case.
  - **Criteria:** L1 target probabilities .5/.25 yield sum NLL ln8, mean ln(sqrt8) and perplexity sqrt8, with exactly two evaluated target tokens. A causal decoder cannot use future tokens to predict them; BOS/EOS/padding, source and decoder mask responsibilities are valid, and a masked objective is not falsely described as autoregressive generation. Genuine training evidence and count baseline are reproducible and correctly bounded; language fluency, safety or external corpus generalization is not inferred from tiny scores.
  - **Evidence:** Data/task contract, independent L1 calculations, fixed source/tokenizer/split/seed, trained model and baseline with real outcomes, loss and gradient trace, negative contamination/shift case, CPU/resource and limitations report.

- **AI9-AS3** (decoding strategy, stop behavior and cache consistency)
  - **Outcomes:** AI9-O3, AI9-O9, AI9-O10, AI9-O20.
  - **Work:** Derive D1's two-step greedy-versus-complete-sequence comparison, one-step top-k/top-p renormalization and temperature changes. Implement or transparently inspect discrete decoding for one local neural or finite conditional model with greedy, sampling and a bounded beam policy, explicit EOS/length/forbidden-token rules and actual RNG state. On a deterministic tiny causal model compare full-prefix uncached continuation to cached prefill+step prediction at identical positions/masks; then alter an offset, padding mask or cache entry and independently predict or explain the changed output.
  - **Criteria:** Greedy A–EOS sequence probability .3 is less than B–EOS .36 **among the declared completed two-step alternatives**; filtered probabilities are 5/8 and 3/8 for A,B; temperature example gives 2/3 vs1/3 at T1 and 4/5 vs1/5 at T1/2. Cache continuation matches the uncached causal computation up to declared numerical tolerance; changing a future token does not change earlier causal logits. Samples, outputs/stop and resource comparisons are observed, not fabricated; invalid access and stale-cache cases are handled safely.
  - **Evidence:** Public decoding arithmetic, complete model/probability and RNG contract, trace of ranked/sequential outputs, numerical cache equivalence with real measurements, invalid offset/stop case and compute/limitations notes.

- **AI9-AS4** (latent-variable evidence and a small VAE)
  - **Outcomes:** AI9-O11, AI9-O12, AI9-O19.
  - **Work:** Independently derive V1's joint and marginal distributions, posterior, KL, reconstruction expectation and ELBO equality, and the separate Gaussian KL=1/2. Implement or inspect a tiny CPU latent-variable generator with a specified prior, encoder, decoder, valid reparameterization if continuous, valid source split and actual reconstruction/sampling behavior; compare a fixed constant or known-likelihood baseline. Create a zero-variance/nonsupported-posterior or posterior-collapse case and explain when the bound fails to be tight or informative.
  - **Criteria:** V1 evidence log=-ln2, q(z=1|x=1)=.75 and ELBO=-ln2 because q equals the exact posterior; Gaussian KL=.5 under its own parameters. All density/support and summation/reduction conventions are stated. A finite exact ELBO does not license a claim of universal generation or meaningful latent semantics; the implementation and small observed experiment have a complete reproducible negative case.
  - **Evidence:** Hand/independent marginal/ELBO derivations, source with actual KL/reconstruction/sample traces, seeds/precision/data provenance, bad posterior or collapsed latent test and limitations.

- **AI9-AS5** (adversarial and invertible generative objectives)
  - **Outcomes:** AI9-O13, AI9-O14, AI9-O19.
  - **Work:** Derive G1's generator and discriminator objectives independently and contrast parameter/update ownership. Implement or transparently inspect a small 1D adversarial learning example with alternating updates or a comparably inspectable synthetic finite discriminator/generator, and diagnose one mode collapse or saturated/discriminative failure with actual sample counts. Independently derive G1's uniform affine flow density and log-Jacobian, implement/check inverse and sample transform, reject a noninvertible map and explain how its exact likelihood differs from both an implicit GAN and the VAE bound.
  - **Criteria:** D loss ln(5/3), non-saturating G loss ln4; flow y=2z+1 has p=1/2 on (1,3), logp=-ln2 and declared support. An invalid zero-scale inverse is not assigned an ordinary density; discriminator loss/sample quality is not a likelihood measure. Actual synthetic adversarial behavior and coverage/failure are reported without fabricated convergence or universal method ranking.
  - **Evidence:** Exact GAN and change-of-variables work, local adversarial/flow source or equivalently complete inspectable numerical traces, actual measured samples/iteration constraints, negative and support-case artifacts and comparison limitations.

- **AI9-AS6** (diffusion, flow matching and sampling failure)
  - **Outcomes:** AI9-O15, AI9-O16, AI9-O19, AI9-O21.
  - **Work:** Derive P1 forward corruption, clean/noise reconstruction and separate zero/nonzero epsilon errors; identify alpha versus alpha-bar and demonstrate a wrong-timestep/schedule case. Implement or inspect a tiny CPU denoising learner using the correct corruption and loss, and **either** a fully specified few-step reverse sampler (including declared mean/variance/noise choices) **or** a bounded trained/inspected flow-matching velocity sampler with its interpolation/ODE integration clearly defined. Derive P2 path/velocity independently and compare methods' target semantics. Report actual synthetic samples, fit diagnostics, distribution coverage/mode problems and compute budget without asserting image-generation proficiency.
  - **Criteria:** P1 x_t=1−sqrt3/2, correct denoising error0, wrong-zero error1 and reconstruction x0=2 (or wrong-zero estimate 2−sqrt3) under declared parameters; P2 x(1/4)=1/2, x(3/4)=3/2 and velocity2. Reverse samples are not deduced from one forward marginal without an explicit reverse/velocity process; noise level, normalizer, schedule and seed are traceable. Genuine model/sampling evidence, changed-case correction and bounded uncertainty are present.
  - **Evidence:** Independent P1/P2 derivations, local source/denoising/reverse-or-flow fixtures, actual samples and measured CPU/step summaries, wrong-schedule negative case, model/version/seed and limitations.

- **AI9-AS7** (conditioned generation and truthful model evaluation)
  - **Outcomes:** AI9-O1, AI9-O5, AI9-O17, AI9-O18, AI9-O19, AI9-O20.
  - **Work:** Define one small symbolic or image-like conditioned generation task with source/target pairing and authorized data. Independently calculate C1 condition-dependent log scores, build/test a simple encoder–decoder or source-conditional generator and an unconditional comparator, and demonstrate a context-swap, missing condition, forbidden source or duplicate pair failure. Analyze a small genuine held-out sample set for conditional validity, source identity, variation/duplicate rate and observed errors, comparing actual counts instead of cherry-picked completions. Explain why a changed guidance/temperature parameter or plausible generated word cannot confirm truthful source grounding.
  - **Criteria:** C1 conditional A scores ln(4/3) and ln4 for the two sources, with unconditional ln2 under stated conditions. Paired IDs, authorized context and attention masks are correct; the model must change outputs only through permitted source data and not expose a restricted sample. Comparisons distinguish exact constructed probabilities from actual measured trained outputs, report support/uncertainty and refrain from sweeping image/language competency or safety claims.
  - **Evidence:** Explicit conditional input/target and source permissions, exact C1 score calculation, local model/baseline outputs, negative pair/privacy cases, actual per-condition support and resource/limit summary.

- **AI9-AS8** (integrated generative investigation and unfamiliar technical defense)
  - **Outcomes:** AI9-O1, AI9-O6, AI9-O19, AI9-O20, AI9-O21, AI9-O22.
  - **Work:** Consolidate and reuse genuine AI9-AS1–AS7 evidence in **one coherent local versioned collection**, not eight standalone production model projects. Choose an authentic bounded generative question and one suitable transformer/latent/denoising mechanism and baseline; publish an independent mathematical reference, valid train/dev/test/source contract, one actual reproducible model and generation/evaluation run, measured CPU limits, negative and permission evidence. The reviewer supplies an **unfamiliar bounded** change to mask, position, target shift, decoding, condition, latent prior, density support, diffusion/flow schedule or source visibility. Before running revised code, derive the changed expected numerical or support outcome when identifiable, or document precisely why it cannot be inferred from known data. Verify the repair, explicit refusal or corrected interpretation and demonstrate unaffected regression cases; present individually attributable written, recorded or live defense.
  - **Criteria:** A clean local environment reproduces authentic source/seed/model outputs without paid, private or GPU-only dependencies. The unfamiliar change receives a correct independent calculation or justified non-identifiability response and reproducible normal/negative checks. An ungrounded good-looking sample, prompt-only interaction, unexplained accuracy, copied reference output, private content leak or low training loss cannot establish AI9-O22 or generative generalization. Separate specialist outcomes require the actual corresponding AI9-AS1–AS7 criteria; combining artifacts does **not** automatically reassess every theoretical family.
  - **Evidence:** Coherent transparent model and data portfolio with immutable task/rights/seed/configuration IDs, validated exact oracles, real measured results and resource data, independent negative and unfamiliar cases, regression verification, appropriately limited conclusions and individual technical defense.

### Required outcome-to-assessment coverage

| Required outcome | Summative evidence |
| --- | --- |
| AI9-O1 | AI9-AS2, AI9-AS7, AI9-AS8 |
| AI9-O2 | AI9-AS1 |
| AI9-O3 | AI9-AS1, AI9-AS3 |
| AI9-O4 | AI9-AS1 |
| AI9-O5 | AI9-AS1, AI9-AS7 |
| AI9-O6 | AI9-AS1, AI9-AS2, AI9-AS8 |
| AI9-O7 | AI9-AS2 |
| AI9-O8 | AI9-AS2 |
| AI9-O9 | AI9-AS3 |
| AI9-O10 | AI9-AS3 |
| AI9-O11 | AI9-AS4 |
| AI9-O12 | AI9-AS4 |
| AI9-O13 | AI9-AS5 |
| AI9-O14 | AI9-AS5 |
| AI9-O15 | AI9-AS6 |
| AI9-O16 | AI9-AS6 |
| AI9-O17 | AI9-AS7 |
| AI9-O18 | AI9-AS7 |
| AI9-O19 | AI9-AS2, AI9-AS4, AI9-AS5, AI9-AS6, AI9-AS7, AI9-AS8 |
| AI9-O20 | AI9-AS3, AI9-AS7, AI9-AS8 |
| AI9-O21 | AI9-AS2, AI9-AS6, AI9-AS8 |
| AI9-O22 | AI9-AS8 |

**Completion decision.** All 22 outcomes require satisfactory **individually inspectable evidence** under the actual course revision through the eight required summative evaluations. Prior legitimate artifacts may be reused when they truly satisfy several assessments; optional instruction, exercise, reading, or assessment *identifier* alone is not proof. Reviewers distinguish exact synthetic mechanism results from executed model measurements and from generalizable/operational claims. A successful source check does not demonstrate that a learner has mastered the material or that the draft course has been independently classroom-tested.

### Optional open academic and primary references

- [Attention Is All You Need (Vaswani et al., 2017)](https://arxiv.org/abs/1706.03762) — original transformer attention and encoder–decoder architecture.
- [Stanford CS224N — Natural Language Processing with Deep Learning](https://web.stanford.edu/class/cs224n/) — sequence model, pretraining and generation context; earlier AI7 language-specific prerequisites remain assumed.
- [Hugging Face attention backends and mask conventions](https://huggingface.co/docs/transformers/attention_interface) — implementation masks, backend-dependent semantics and variable-length queries.
- [Hugging Face text generation configuration](https://huggingface.co/docs/transformers/main_classes/text_generation) — greedy, sampling, beam and stop/temperature definitions.
- [Auto-Encoding Variational Bayes (Kingma & Welling)](https://arxiv.org/abs/1312.6114) — ELBO and reparameterization.
- [Denoising Diffusion Probabilistic Models (Ho et al.)](https://arxiv.org/abs/2006.11239) — Gaussian noising and denoising model basis.
- [Flow Matching for Generative Modeling (Lipman et al.)](https://arxiv.org/abs/2210.02747) — velocity objective and conditional paths.
- [MIT 2026 — Flow Matching and Diffusion Models](https://diffusion.csail.mit.edu/2026/index.html) — current academic scope for diffusion, flow paths and sampling.
- [OpenAI Spinning Up introduction](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html) — optional distinction from AI6 reward-driven policy optimization; RL is not a mandatory AI9 dependency.

All references supplement the public source—not secret compulsory curriculum, hardware, software account or prerequisite requirements. Technical claims are limited by the declared objective, data, model and evidence.
