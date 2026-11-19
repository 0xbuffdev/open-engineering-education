# AI8 — Computer Vision & Multimodal Learning

**Program:** AI — AI Engineering
**Type:** course
**Prerequisites:** [AI7](AI7.md) — Natural Language Processing & Information Retrieval (completed)
**Duration:** 20–28 weeks
**Status:** draft
**Specification:** v0.2.0
**Expected workload:** 10–15 focused hours/week (provisional; approximately 200–420 focused hours)

> [AI Engineering](README.md) · [Curriculum design guide](../DESIGN-GUIDE.md) · [Course format](../../spec/course-format.md) · [Evidence rules](../../spec/evidence-rules.md)

## Overview

**AI8 establishes the engineering and scientific foundations of understanding visual information and learning from more than one modality.** Learners must distinguish raw pixel measurements from objects, scenes and asserted meanings; preserve spatial and temporal evidence through preprocessing and annotation; implement and critically compare small vision models for classification, localization, detection, segmentation and sequence observations; and build bounded image–text alignment, retrieval and fusion systems with independently verifiable evaluation. A classifier output, bounding box, segmentation mask or shared embedding is never accepted as ground truth merely because a library produced it. The learner must show which image, annotation, coordinate system, source, sampling assumption, model and evaluation protocol support the result.

**Entry competence and progression.** The **single direct prerequisite is completed [AI7](AI7.md)**, which itself requires [AI5](AI5.md). AI5 already assesses tensor layout, convolution/backpropagation, neural training, learned embeddings and contrastive objectives. AI7 already assesses text normalization, annotation, linguistic ambiguity, semantic retrieval, per-query relevance judgments, and lexical/dense ranking. [AI4](AI4.md), [AI2](AI2.md), [AI1](AI1.md) and the complete SEF foundations are inherited through that chain. AI8 develops the previously unassessed **vision-specific** skills: image acquisition/coordinate geometry, label-preserving spatial transformations, image and scene identity leakage, visual feature/pattern failures, box assignment and detection metrics, pixel/instance masks, bounded video tracking, visual pretexts, actual image–text pairing and bidirectional retrieval, and multimodal fusion with missing/conflicting evidence. Re-deriving generic convolution kernels, text tokenization, cosine distance, the gradient chain rule, generic cross-validation or ordinary retrieval metrics is *not* a substitute for these new competencies. No APP, SYS or AI6 completion is directly required.

**Course boundaries.** AI9 owns transformer and attention architectures, generative image/language modeling and diffusion-type generative mechanisms; AI10 owns advanced large-model optimization and adaptation; AI11 owns grounded retrieval-augmented generation and answer citation; AI12 owns tool-using application agents; AI13 owns broad AI systems assurance; AI14 owns systematic security, responsible AI and governance; AI15 owns serving and MLOps. AI8's vision-language work uses **small fixed or locally trained encoders and simple contrastive pairs**, not pretrained web-scale transformers, hosted VLMs, text/image generation, captioner finetuning or real autonomous agents. Basic video temporal sampling/identity tracking is an image-sequence specialty here, not an advanced reinforcement-learning or robotics course; embodied perception and sensor fusion for physical action belong to elective AI18. A vision or text retriever does not establish real-world scene semantics or image authenticity by similarity alone.

**Assessed access and evidence conditions.** Every compulsory reference case is a tiny **synthetic image array, spatial annotation, finite frame sequence or synthetic image–caption pairing**. Python 3 standard library, NumPy or equivalent matrix operations suffice for exact geometry, index, detection matching, mask and retrieval oracles. A modest CPU-only open neural framework can support the small model experiments, or an equivalent transparent implementation can meet the same outcome criteria; no GPU, cloud credit, commercial dataset, hidden pretrained weights, personal photo library, premium labeling tool or licensed online API is required. Image data must include source/license/privacy provenance, stable image/scene IDs, versioned annotations, dimensions and channel conventions. Provide accessible equivalent numeric grids, coordinate descriptions and structured tables for visual evidence; do not make the ability to inspect a color-dependent plot the only way to demonstrate a result. All code must disclose dtype, coordinate conventions, image layout, train/validation/test grouping, padding and resizing policy, optimizer/seed and actual compute budgets.

**Assessment architecture.** Thirteen distinct competency stages connect pixel and annotation integrity with vision model selection, localization/detection, region segmentation, temporal identity, visual representation, image–text alignment, multimodal evidence and independent evaluation. Paired numerical/negative checks now sit with the mechanisms they test rather than becoming repeated standalone lessons. Nine required cumulative summative assessments establish **22 observable learning outcomes**: visual data integrity; vision classification; detection and localization; segmentation; temporal data; visual representation; image–text contrastive learning and retrieval; fusion, evaluation and access controls; and an integrated unfamiliar technical defense. Learners may maintain **one reusable versioned collection** with several small model/analysis exercises instead of creating nine separate industrial systems. Exact public oracles below are checkable without trusting a framework; actual trained performance/latency/robustness must be genuinely measured and cannot be inferred from toy expected values. The estimated 20–28 weeks include study, proof, implementation, experiments, diagnosis and independent review; the course remains `draft` until authentic learner evidence supports a later status decision.

## Learning outcomes

- **AI8-O1:** Formulate a bounded visual or multimodal prediction/retrieval question with input/output units, intended scene/camera/language population, labels, permissions, baseline, metric, resource budget and limits on conclusions.
- **AI8-O2:** Decode, inspect and preserve image dimensions, channel order, intensity scale, color/alpha conventions, orientation and metadata provenance, independently checking transformations and detecting invalid or lossy assumptions.
- **AI8-O3:** Define and verify image-coordinate geometry, geometric transforms, resizing/cropping/flipping and annotation co-transformations for boxes, masks and keypoints, with explicit label-preservation and clipping assumptions.
- **AI8-O4:** Create and audit image/scene, video and paired image–text datasets with correct licenses, image/annotation identities, missing/ambiguous labels, group/temporal split boundaries and train-only transformation fitting.
- **AI8-O5:** Construct and fairly compare image-classification baselines and CPU-scale learned visual models, justifying resolution, spatial inductive bias, nuisance variation and valid held-out evidence rather than training accuracy.
- **AI8-O6:** Inspect and compare visual feature representations, spatial receptive fields, pooling, robustness and equivariance/invariance claims using controlled pattern/feature responses and measured changes, not unsupported saliency stories.
- **AI8-O7:** Identify and investigate visual distribution shifts, shortcut features, blur, scale/lighting/occlusion and annotation ambiguities with actual valid experiments, error/denominator analysis and bounded claims.
- **AI8-O8:** Specify, transform and independently calculate axis-aligned object localization coordinates, bounding-box intersection-over-union, clipping, degenerate geometry and regression/assignment conventions.
- **AI8-O9:** Construct and inspect a bounded object-detection pipeline with class confidence, spatial candidates, nonmaximum suppression, one-to-one ground-truth matching and duplicate/missed-instance failure behavior.
- **AI8-O10:** Evaluate detection using a declared IoU threshold, ranking, TP/FP bookkeeping, precision–recall and AP variant, explicitly distinguishing toy single-threshold uninterpolated AP from COCO-style multi-threshold AP/mAP.
- **AI8-O11:** Specify and evaluate semantic pixel masks, ignored/background pixels, class supports, pixel accuracy, region intersection-over-union and Dice or analogous overlap under explicit empty-class conventions.
- **AI8-O12:** Distinguish instance from semantic and panoptic-style annotation, preserve object identity across overlapping regions, and analyze a small instance-mask/box agreement and duplicate/occlusion case.
- **AI8-O13:** Design and inspect a bounded visual self-supervision/representation objective and its paired views, diagnosing label-destroying augmentation, nuisance shortcuts, duplicate identities and representation collapse.
- **AI8-O14:** Represent and analyze finite video/frame sequences with timestamps, valid sampling, motion/temporal differences, state/track identity and leakage-safe scene-level evaluation, without implying physical-world calibration.
- **AI8-O15:** Build an image–text pairing and annotation contract with source and caption identities, compositional language, uncertainty, false negatives, duplicates and legitimate negative examples; distinguish caption metadata from observed visual truth.
- **AI8-O16:** Derive and implement a small **bidirectional image–text contrastive** objective with independently verified similarity/logit matrices, temperatures, positive-pair indices and batch-duplicate assumptions.
- **AI8-O17:** Build and independently evaluate **both** image-to-text and text-to-image retrieval with correct normalized similarity/top-k/tie conventions and query-level relevance judgments; identify asymmetry and unsupported semantic claims.
- **AI8-O18:** Compare bounded early/late cross-modal feature or score fusion, explicit missing/conflicting modalities, data alignment and fail-safe/unimodal fallback behavior, with actual performance and calibration limitations.
- **AI8-O19:** Design and execute fair vision/multimodal evaluation using grouped scene/subject splits, appropriate classification/detection/segmentation/retrieval metrics, uncertainty and per-slice support, honest baselines and model-selection boundaries.
- **AI8-O20:** Enforce image/data licensing, privacy and consent/visibility restrictions, sensitive-content handling, deletion/annotation revision provenance and human review where an image-based inference or document release lacks authority.
- **AI8-O21:** Produce a clean-start, CPU-feasible, versioned visual/multimodal evidence collection with independent numeric oracles, actual measured comparisons, model/dataset/annotation revisions, failure tests and compute disclosure.
- **AI8-O22:** Diagnose an unfamiliar bounded change in pixel geometry, annotation, image class, detector matching, mask, frame identity, caption alignment, pairing matrix, modality availability or permission; independently predict the changed expected result and demonstrate a repair or defensible refusal.

## Modules

### Module 1 — Visual Evidence, Tasks and the Limits of Perception

#### Outcomes

- AI8-O1
- AI8-O4
- AI8-O7
- AI8-O20

#### Lessons

1. **Visual evidence, development and perception limits** — Distinguish measured pixel samples from objects, labels, scenes, inferred intent and physical facts. Trace engineered feature extraction, statistical classification, convolutional visual models and modern image–text alignment to the bounded applications and assumptions they address; explain why a high score on synthetic images does not establish causal scene understanding, image authenticity or safe real-world perception.
2. **Classification, localization, detection, segmentation and retrieval** — Define the prediction unit, output shape and criterion for each, contrasting an image-level label with a spatially grounded instance or caption match.
3. **Camera and scene as sampling units** — Record image, scene, subject, device, frame and capture-session identities; identify why repeated frames, crops and near duplicates violate naïve row independence.
4. **Annotation and permission requirements** — Define image ownership/license, personal-image restrictions, uncertain labels, redaction, missing source and who may inspect a raw visual artifact.
5. **Baselines, compute and evaluation claims** — Choose an appropriate constant, pixel-feature or small neural baseline and a correct holdout population, refusing model-of-the-world claims unsupported by a synthetic task.
6. **Public challenge and negative cases** — Establish a tiny numeric-image corpus with a source/annotation contract, shape/dtype error and one deliberately invalid or unauthorized image use.

*Optional formative prompt:* A detector sees the same item in ten adjacent video frames; explain why testing on eight frames after fitting on the other two may not measure a new-scene capability.

### Module 2 — Digital Image Formation, Coordinates and Pixel Integrity

#### Outcomes

- AI8-O2
- AI8-O3
- AI8-O21

#### Lessons

1. **Image grids and channel layouts** — Translate H×W×C and C×H×W layouts with explicit batch axis, grayscale/color/alpha semantics and a concrete value/shape oracle.
2. **Integer intensities and normalization** — Distinguish unsigned 8-bit pixels from normalized floating values, rounding/clipping and loss of precision on repeated conversions.
3. **Color spaces and intensity interpretation** — Compare RGB, grayscale and a luminance-like transform using declared coefficients, channel order and encoding assumptions, avoiding an undocumented universal RGB-to-gray formula.
4. **Spatial coordinate orientation, image metadata and physical pixels** — Specify image origin, x/y direction, centers, half-open bounds, width/height and actual memory-channel layout. Compare orientation metadata with the underlying pixel array, independently trace a rotation/orientation case and show why ignoring a camera's orientation can invalidate a spatial annotation or silently reverse axes; preserve a reproducible normalized view and the source orientation.
5. **Resizing and sampling** — Contrast nearest-neighbor, bilinear and area-based resampling on a tiny grid; identify aliasing from downsampling without an appropriate antialias policy.
6. **Cropping, padding and boundary provenance** — Predict surviving coordinates and zero/reflect padding effects on a fixed image; explain when cropping changes a classification label or removes a labeled object.
7. **Geometric transform chain and inverse mapping** — Apply scaling, translation and reflection to annotated points/boxes, preserving the transform order and whether an inverse exists after information loss.
8. **Numeric image checks and invalid encodings** — Reproduce the public V1 image mean and flip, detect an invalid/empty array, incompatible channels or nonfinite pixel, and record a faithful text-grid oracle.

### Module 3 — Visual Annotation, Target Geometry and Leakage-Safe Augmentation

#### Outcomes

- AI8-O3
- AI8-O4
- AI8-O8
- AI8-O19

#### Lessons

1. **Image-level, box, mask and keypoint annotation schemas** — Define annotation type, class ontology, object ID, confidence provenance and unknown/ignore label without conflating them.
2. **Box representations and conversion** — Translate xyxy, xywh and normalized coordinates with declared half-open bounds and check equivalence on a non-square image.
3. **Synchronized visual/target transforms and independent adversarial checks** — Derive G1's flipped and resized box coordinates on a declared transform chain, and apply corresponding pixel/keypoint/mask transformations. Deliberately introduce swapped image axes, a misaligned bounding box or a mismatched transform order, independently predict the violated coordinate/identity invariant and verify a repair; a transformed image with unchanged source boxes is not valid evidence.
4. **Clipping and visibility decisions** — Define how partially clipped boxes, removed instances and valid-area thresholds affect a transformed label; distinguish a clipped target from its original uncropped object.
5. **Masks, interpolation and class IDs** — Apply discrete nearest-neighbor mask transforms to preserve class indices, and explain why interpolated categorical IDs can invent an invalid class.
6. **Augmentation invariance contract** — Decide whether horizontal reflection, rotation, color jitter and object crop preserve the *actual* target (left/right directions, text on signs, orientation or safety label may change).
7. **Visual annotation ambiguity and disagreement** — Model occluded objects, uncertain boundaries, overlapping instances and unequal annotators without treating arbitrary labeling as unique ground truth.
8. **Train/dev/test source grouping** — Partition scenes/subjects/capture sessions before deriving crops, patches or augmentations; show a contaminated split where near-identical scenes cross boundaries.
9. **Revision and lineage** — Maintain immutable image ID, transform version, annotation version, source/license and authorized visibility, with reproducible changes rather than destructive silent relabeling.

### Module 4 — Image Classification and Visual Generalization

#### Outcomes

- AI8-O1
- AI8-O5
- AI8-O6
- AI8-O7
- AI8-O19

#### Lessons

1. **Image-level target and baseline definition** — Specify the precise class label, input resolution, scene independence, majority/constant baseline and cost of a false visual prediction.
2. **Simple handcrafted pattern features** — Build a compact edge, average intensity, color histogram or spatial count feature and show what changes under a documented shift in image structure.
3. **A small vision classifier and fair model selection** — Apply AI5's assessed convolution/training mechanics to a spatial-pattern task with named image layout and training-only normalization. Compare a constant/handcrafted feature or linear baseline, the small CNN and one justified architecture/augmentation change under identical grouped scene partitions, evaluation metric, class supports, seeds and CPU budget. Record actual rather than presumed held-out improvements.
4. **Geometric invariance and equivariance tests** — Measure whether predictions/feature maps respond to translation, reflection, rotation and scale as the selected target requires, without claiming that a network is universally invariant.
5. **Shortcut labels and confounders** — Construct a synthetic foreground-shape task where correlated background color makes training accuracy misleading; test a scene/background-balanced holdout.
6. **Occlusion, blur and illumination errors** — Introduce one controlled camera-like perturbation, record actual model and baseline behavior, and separate image degradation from a new semantic label.
7. **Per-class and group error interpretation** — Report class supports, confusion and group-level mistakes honestly, avoiding a real-world robustness claim based on a few artificial images.

### Module 5 — Spatial Feature Representation and Visual Transfer

#### Outcomes

- AI8-O5
- AI8-O6
- AI8-O7
- AI8-O13

#### Lessons

1. **Local pattern responses as visual evidence** — Compute a small oriented edge response on the public F1 intensity pattern; relate it to orientation/illumination sensitivity rather than re-teaching a generic convolution derivation.
2. **Spatial hierarchy and pooling tradeoffs** — Compare preserving a small local location with a globally pooled feature, showing what object-position evidence may be lost.
3. **Scale and receptive fields in a real image task** — Use AI5 convolution understanding to explain why resizing or a low-resolution object may alter effective visual evidence, even when layer shapes remain valid.
4. **Feature visualization and attribution restraint** — Inspect filter activations, occlusion responses or saliency as diagnostic observations, not unique causal explanations of what the model 'saw.'
5. **Frozen and locally adapted visual representation transfer** — Reuse a small locally trained visual backbone in a frozen-head task and, where justified, a bounded selectively updated variant, with explicit trainable weights and a true from-scratch baseline. Report actual held-out scene/domain performance, representation/feature drift, training CPU costs and unsupported gain claims; do not require a hidden pretrained model or assume frozen transfer outperforms scratch training.
6. **Feature drift across cameras/scenes** — Measure embedding similarity and classification changes under synthetic brightness, viewpoint or background shift, avoiding claims that a close vector means the same physical object.
7. **Representation collapse and unused dimensions** — Inspect a constant-output encoder, low-variance feature component and an unsupported nearest-neighbor claim, distinguishing a compact representation from a useful one.

### Module 6 — Object Localization, Detection and Spatial Matching

#### Outcomes

- AI8-O8
- AI8-O9
- AI8-O10

#### Lessons

1. **Localization versus detection** — Distinguish one predicted object location from an arbitrary number of class-scored instances and explain why a classifier's single label is insufficient.
2. **Coordinate encoding and box validity** — Calculate center/size and corner formats, clip to image bounds and reject negative/zero-area or reversed boxes under the declared representation.
3. **Intersection-over-union** — Derive G2's intersection, union and IoU exactly, including nonoverlap, coincident boxes and the distinction between area overlap and center distance.
4. **Detection heads and candidate generation** — Compare anchor-like predefined candidates with grid/point-based predictions conceptually, naming objectness, classification and regression outputs without obliging a heavy detector library.
5. **Confidence-ordered candidate ranking and nonmaximum suppression** — Treat detector confidence as a ranking signal under explicit class/background and score-threshold rules, not a calibrated probability of object existence. Independently trace D1 greedy same-class NMS on sorted candidates with a declared IoU suppression convention; identify duplicate suppression and a counterexample where strongly overlapping distinct true objects can be incorrectly removed.
6. **One-to-one ground-truth assignment** — Match high-score candidates to currently unmatched ground-truth objects of the appropriate class at a declared IoU threshold; identify double detections as false positives.
7. **Detection precision–recall and AP convention** — Calculate D1's rank-level TP/FP and uninterpolated one-IoU-threshold AP, distinguishing it from COCO AP averaged across thresholds and recall samples.
8. **Small detector construction** — Implement or transparently inspect a CPU-scale candidate generator/detector on synthetic geometric objects, with known box/count oracle and valid train/eval separation.
9. **Negative geometry and threshold experiment** — Vary IoU/NMS/score threshold or create a missed/tiny/occluded object and explain which match, recall and diagnostic behavior changes without inventing a benchmark gain.

### Module 7 — Semantic, Instance and Region Segmentation

#### Outcomes

- AI8-O3
- AI8-O11
- AI8-O12
- AI8-O19

#### Lessons

1. **Pixels, regions and object identity** — Distinguish image-wide classification from assigning every pixel a semantic class versus identifying each distinct object instance.
2. **Semantic/instance masks, valid transforms and label shapes** — Define per-pixel class IDs, distinct instance IDs, background/ignored pixels, consistent H×W image alignment and a valid class ontology. Apply resize/crop/flip jointly to image and categorical mask using an integer-preserving nearest-neighbor label policy; diagnose an interpolated invalid class or misaligned mask with an independent expected pixel grid.
3. **Pixel-level overlap calculations** — Derive M1 TP/FP/FN/TN, intersection/union, IoU, Dice and accuracy independently with a published treatment for ignore and zero-union classes.
4. **Segmentation objectives and class imbalance** — Compare pixel cross-entropy and Dice/IoU-oriented objectives on tiny masks, explaining why an all-background predictor may achieve misleading pixel accuracy.
5. **Connected components versus true instances** — Show why two touching objects of one semantic class cannot always be separated by a semantic mask alone; identify instance labels and overlapping/occluded boundaries.
6. **Detection/instance-mask consistency** — Compute the enclosing box of a finite instance mask and check a separately reported detection box for matching object ID and spatial validity.
7. **Boundary and annotation uncertainty** — Analyze one ambiguous border/void region and compare its contribution to a predicted metric under alternative, explicitly versioned label policies.
8. **Bounded segmentation evidence** — Train/inspect a tiny pixel classifier or small encoder-decoder on synthetic shapes, compare with an image-processing baseline and disclose observed per-class counts rather than require large datasets.

### Module 8 — Video Sampling, Motion and Object Identity

#### Outcomes

- AI8-O4
- AI8-O7
- AI8-O14
- AI8-O19

#### Lessons

1. **Frame versus event unit** — Define clip/scene/source identity, timestamps, frame rate and observation cadence so repeated image frames do not become independent training examples.
2. **Timestamped finite motion, sampling and aliasing** — Independently derive T1 displacements and pixels/second from actual frame timestamps, and show how skipped frames or a wrongly assumed sampling interval change the result. Explain how sampling can erase or reverse the apparent direction of a fast event and why image-coordinate velocity without camera calibration is not physical-world speed; preserve clip/scene identity.
3. **Frame differencing and brightness constancy** — Calculate a tiny changed-pixel map and explain why photometric change, object motion, occlusion and camera movement can produce similar differences.
4. **Track association and IDs** — Maintain identities across bounded frames with an explicit spatial match/tie rule, and demonstrate an identity switch despite correct per-frame object counts.
5. **Occlusion and missing frames** — Handle a temporarily hidden object, dropped frame or empty detection using a defined unknown/stop policy rather than fabricate uninterrupted object presence.
6. **Sequence-aware model alternative** — Compare per-frame aggregation with a small AI5-style recurrent or temporal feature head under identical clip-level splits; full video transformers remain outside the course.
7. **Temporal evaluation/reporting** — Report per-clip and per-scene support, basic track/identity errors and CPU/frame budget without claiming autonomous real-time perception.

### Module 9 — Visual Self-Supervision and Representation Quality

#### Outcomes

- AI8-O6
- AI8-O7
- AI8-O13
- AI8-O19

#### Lessons

1. **Visual pretext tasks and the boundary to image–text meaning** — Define masked-patch, denoising or paired-view prediction targets from images, distinguishing objective reconstruction from independently judged semantic labels. Contrast two views of one visual source with a caption that makes a linguistic proposition about it: visual pretext success cannot demonstrate image–text grounding, which has additional correspondence and relevance criteria in Module 10.
2. **Legitimate paired image views** — Choose augmentations that preserve intended object identity/label while changing nuisance factors, and reject transforms that destroy required position, color or text labels.
3. **Instance identity and false negatives** — Explain how two crops of one source image share a positive identity and why duplicated scenes/semantically identical images can invalidate naïve negative pairing.
4. **Image encoder and embedding normalization** — Apply AI5's contrastive objective to an explicitly visual task with a small locally trained image encoder; independently verify dimensions and similarity.
5. **Collapse, shortcut and augmentation negatives** — Construct constant embeddings, background-color shortcuts or destructive cropping, then demonstrate what fails in the actual measured representation.
6. **Frozen visual probe and source leakage** — Train a small classifier on frozen image features with held-out scene grouping, comparing to a raw-pixel or supervised baseline under a valid split.
7. **Augmentation and objective ablation** — Compare a legitimate/illegitimate visual-view strategy with fixed data and seed resources; report actual results and uncertainty without guaranteed improvement.

### Module 10 — Image–Text Pairing and Bidirectional Alignment

#### Outcomes

- AI8-O15
- AI8-O16
- AI8-O17
- AI8-O20

#### Lessons

1. **Image–caption data identity and rights** — Establish unique image/text IDs, caption provenance, visibility, paraphrases and whether the text describes the whole scene or only an object.
2. **Descriptions, compositionality and negation** — Compare visually similar captions that reverse left/right, counts, relations or exclusions; explain why a bag-like text representation can miss the difference.
3. **Paired visual and language encoders** — Choose small fixed or locally trained image/text feature functions with compatible latent dimensions; reuse AI5/AI7 mechanics without introducing transformer self-attention.
4. **Similarity matrix and positive-pair indices** — Build a finite batch cosine/dot matrix from genuine paired IDs and explain how shuffling captions without updating labels corrupts training.
5. **Bidirectional contrastive softmax loss** — Derive X2's image-row and text-column cross-entropies, explicit temperature, positive diagonal and average reduction; verify a permutation or duplicate-positive negative case.
6. **False-negative and duplicated caption effects** — Explain why multiple valid descriptions or near-duplicate image sources violate naïve one-positive-per-row assumptions and choose a declared multilabel/soft-positive policy or honest exclusion.
7. **Both directions of image–text retrieval as independently evaluated evidence** — Calculate image-to-caption and caption-to-image rankings separately from one explicitly paired corpus, complete directional judgments and deterministic tie rules. Reproduce X1 top-1 results in **both** directions, showing how asymmetric candidates and ties give different Recall@1; compare score/rank behavior without treating high cosine as proof that a caption describes the image truthfully.
8. **Grounding, provenance and limitations** — Present candidate captions alongside the visual and source annotation evidence, refusing a claim of genuine scene-grounded understanding from embedding similarity alone.

### Module 11 — Multimodal Fusion and Missing Evidence

#### Outcomes

- AI8-O15
- AI8-O17
- AI8-O18
- AI8-O19
- AI8-O20

#### Lessons

1. **Alignment of modality samples** — Define which image, text, timestamp and observation unit correspond to the same entity; reject a deliberately swapped image/caption or wrong-time metadata join.
2. **Early versus late fusion and the distinction from retrieval** — Compare dimension-aligned image/text feature concatenation with an independently weighted combination of modality predictions, naming assumptions, units and modality-specific errors. Distinguish retrieving a matched caption or image from predicting a joint class/attribute: a nearest caption is neither a generated answer nor a causal semantic explanation of a scene.
3. **Exactly specified fusion score** — Calculate F2's weighted logit combination, output decision and changed weight/label; state that logits from separately trained encoders need not share a calibrated scale.
4. **Missing modality strategies** — Distinguish dropping a sample, using a trained missing-input token, authorized unimodal fallback and unjustified zero-fill, with a valid evaluation-time missingness pattern.
5. **Conflicting modality evidence** — Analyze an image containing one object and a text statement describing a different one, resisting an unsupported assertion that either modality must be correct.
6. **Fusion baseline and ablation** — Compare image-only, text-only and combined predictions under one valid split and fair resource budget, reporting when fusion worsens or fails.
7. **Privacy and access in two channels** — Enforce independent image and text permissions before retrieval/fusion; a public caption must not reveal a restricted image's contents by indirect inference.
8. **Evaluation under missing data/shift** — Disclose sample denominators and measured performance when a modality, language, camera or paired label is absent or changed, without extrapolating to general availability.

### Module 12 — Vision Evaluation, Shift, Rights and Resource Forensics

#### Outcomes

- AI8-O4
- AI8-O7
- AI8-O10
- AI8-O11
- AI8-O17
- AI8-O19
- AI8-O20
- AI8-O21

#### Lessons

1. **Versioned vision/multimodal experiments** — Pin synthetic source, scene/clip IDs, annotation revisions, augmentation, model weights, captions, splits and exact evaluation conventions.
2. **Metric choice, exact spatial oracles and COCO compatibility boundaries** — Select image classification/support measures, detection IoU/ranked AP, semantic/instance-mask IoU/Dice, track identity and directional image–text Recall@k to match the actual prediction unit. Explain why D1's toy one-IoU-threshold uninterpolated AP is **not** COCO multi-IoU/multi-recall-threshold AP/mAP; no metric name should conceal its matching, ignore, interpolation, aggregate or support conventions.
3. **Per-slice support and uncertainty** — Count camera, light, occlusion, class, caption-language and annotation-uncertainty groups; reject universal robustness or fairness claims from small synthetic slices.
4. **Train/validation/test scene integrity** — Demonstrate a same-scene crop/frame leakage, an augmentation identity error and a repaired grouped split with independent evaluation records.
5. **Rights, redaction and deletion tests** — Reject a restricted or withdrawn image/caption from training and result exposure under the declared permission policy; verify caches/derived annotations obey the revision.
6. **Resource accounting for CPU feasibility** — Measure actual tiny-model CPU runtime, memory/index footprint, image resolution and frame/caption inference costs with stated environment and bounded failure cases.
7. **Failure cause versus correlation** — Investigate false detections, missing small objects, label boundaries, false caption matches or loss of temporal identity, distinguishing data/annotation, model and evaluation issues.
8. **Evidence and status limits** — Write a concise model/dataset report with supported uses, limitations, uncertainty and human review gates; a clean CI run is not a learner-tested or deployed safety certificate.

### Module 13 — Integrated Visual–Language Study and Unfamiliar Defense

#### Outcomes

- AI8-O1
- AI8-O19
- AI8-O20
- AI8-O21
- AI8-O22

#### Lessons

1. **One bounded vision–language study with reusable specialist evidence** — Choose a permitted small object/scene task with numeric image grids, box or mask labels, legitimate image/caption pairing, stable source/group identifiers and an honest baseline. Reuse prior assessed geometry, classification, detection, segmentation, video and alignment oracles where they meet the distinct underlying criteria rather than rebuilding eight unrelated model projects.
2. **Independent numeric oracles and normal cases** — Verify actual image/annotation transform, at least one spatial IoU/detection or mask case, and a paired image–text ranking/contrastive outcome using an independent reference.
3. **Actual comparisons, resource costs and versioned lineage** — Compare an appropriate visual baseline with a bounded learned representation and a justified image–text retrieval or fusion mechanism under fixed grouped/paired splits. Publish genuine measured supports, errors, seeds and CPU/resource budgets along with image, annotation, caption, model and permission revisions; independently distinguish a dataset change from an improvement in a model and do not claim unmeasured visual robustness.
4. **Failure and access demonstration** — Exercise a malformed bounding box, duplicate prediction, invalid mask, missing modality, mislabeled caption, unlicensed image, scene leak or unauthorized result and demonstrate a bounded correction/refusal.
5. **Unfamiliar reviewer-supplied variation** — Independently predict the consequence of a changed box coordinate, resized image, mask, frame timestamp, caption pair, temperature, language label, missing modality or access rule before executing an amended system; establish a new oracle or justify refusal.
6. **Individual technical defense and transfer** — Explain the evidence from pixel measurements through representation and evaluation, which results remain unchanged under the variation and which wider perception claims the work does not establish.

These modules are the instructional sequence, not thirteen additional compulsory submissions. Work and formative feedback can be reused where a new outcome is actually inspected; **the nine summative assessment contracts below** determine completion.

## Completion requirements

### Shared public synthetic fixtures and independent checking rules

All reference cases are small enough for manual derivation and independent standard-library verification. Images are **textual numeric grids** and all annotation coordinates use a declared system. Exact values are only valid under the stipulated synthetic fixture; observed model accuracy, scale robustness, image–text language understanding and CPU timings must be measured, not invented.

**V1 — Grayscale pixel grid and reflection.** Interpret a 2×2 grayscale uint8 image in row-major (y,x) layout as rows **[0,64]** and **[128,255]**, one channel and unencoded intensity for this toy calculation. The mean raw sample value is **447/4=111.75** and the mean of values individually scaled by 1/255 is **447/1020 ≈ 0.4382352941**. Horizontal reflection of pixels yields rows **[64,0]**, **[255,128]**. A 2×2 RGB tensor or an 8-bit image divided using integer arithmetic is not equivalent to the one-channel normalized fixture. This is a pixel demonstration, not a physically color-managed luminance claim.

**G1 — Image/box transform with half-open xyxy coordinates.** Original image width=8, height=6; one box **[1,1,4,5)** in (x_min,y_min,x_max,y_max) coordinates has width3, height4 and area **12**. Resize *both dimensions* by factor2 to width16, height12: transformed box **[2,2,8,10)** with area **48**. Horizontal flip of the **original**, unscaled image uses x'_min=W−x_max, x'_max=W−x_min, yielding **[4,1,7,5)**; transforms are alternatives unless an explicit sequence is declared. A box must stay within bounds after clipping, and zero/negative area or a swap of height/width is invalid. For a categorical mask, transform pixel labels with a nearest-neighbor/no-new-class policy; interpolating class IDs as if continuous colors violates the annotation contract.

**G2 — Box IoU geometry.** On a coordinate plane, box A=[0,0,4,4) and B=[2,1,6,5) have area **16** each. Their intersection is [2,1,4,4), area **6**; union area **26**; box IoU **6/26=3/13 ≈ 0.2307692308**. Identical nonempty boxes have IoU1; disjoint boxes IoU0. Boxes with reversed coordinates or zero union must be rejected or handled under a named convention, not assigned an invented positive overlap.

**F1 — Spatial edge response and nuisance limit.** A 3×3 grayscale grid has each row **[0,0,2]**; apply the explicitly defined horizontal response filter [-1,0,1] as *cross-correlation* at each row's only valid three-pixel window. The three resulting responses are **(2,2,2)**. Reflecting each row horizontally produces [2,0,0] and gives responses **(-2,-2,-2)**. This is exact evidence of filter-orientation sensitivity, not a demonstration that any trained CNN is equivariant or invariant to reflection.

**D1 — Ranked detection matching and nonmaximum suppression.** In one synthetic image of a **single class**, two ground-truth objects have nonoverlapping boxes G1=[0,0,2,2), G2=[4,0,6,2). Three predictions, ordered by descending confidence, are P1=G1 score0.90, P2=G1 score0.80 (duplicate) and P3=G2 score0.70. At matching IoU threshold **0.5**, using score-ordered **one-to-one** ground-truth assignment **without NMS**, P1 is TP, P2 is FP (G1 already matched), P3 is TP. Precision after each prediction is **1, 1/2, 2/3**; recall is **1/2, 1/2, 1**. The simple **uninterpolated single-threshold AP defined as precision at each TP divided by two ground truths** equals **(1+2/3)/2=5/6**. This is *not* the COCO official multi-threshold AP/mAP calculation. Separately, greedy same-class NMS with suppression if IoU >0.5 keeps P1 and P3 and suppresses duplicate P2; matching after this NMS has two TPs on these particular boxes, but NMS may suppress legitimate overlapping distinct objects elsewhere.

**M1 — Binary semantic segmentation.** On a 3×3 image, ground-truth foreground mask rows are **[1,1,0], [0,1,0], [0,0,0]**; predicted rows **[1,0,0], [0,1,1], [0,0,0]**. For the positive class, **TP=2, FP=1, FN=1, TN=5**; the foreground intersection has 2 pixels, union 4, so **IoU=1/2**, **Dice=2/3** and **pixel accuracy=7/9**. Ignore no pixels in this fixture. Empty-ground-truth/prediction class cases need an explicit undefined/skip/perfect convention; generic pixel accuracy can be dominated by background. A semantic class mask cannot by itself guarantee the individual identities of two touching same-class objects. An instance-mask bounding box must match the nonzero mask coordinate extent under the declared half-open convention.

**T1 — Finite frame sequence and timestamp.** A synthetic 1D marker center appears at horizontal pixel coordinates **0,1,2** in frames timestamped **0,1/2,1 seconds**. Successive displacement is 1 pixel per 1/2 second, so measured image-coordinate velocity is **2 pixels/second**; using frames 0 and 2 gives 2 pixels over 1 second, also 2 pixels/second. Treating the skipped pair as if separated by 1/2 second would falsely report 4 pixels/second. Pixel movement is not physical-world speed without camera calibration; stable object identity must be separately verified if multiple markers cross.

**X1 — Asymmetric image–text retrieval under exact cosine.** Use two normalized image vectors i1=(1,0), i2=(0,1); two normalized text vectors t1=(1,0), t2=(1/√2,1/√2); and **positive pairs (i1,t1), (i2,t2)**. Similarity matrix by image rows and caption columns is **[[1,1/√2],[0,1/√2]]**. Under exact cosine and ascending ID for ties, image-to-text top-1 finds both matched captions: **Recall@1=2/2=1**. In the reverse direction, t1 selects i1, but t2 ties i1/i2 and ascending ID selects i1; text-to-image top-1 therefore has **Recall@1=1/2**. This deliberate asymmetry shows why bidirectional evaluation, tie policy and genuine one-to-one qrels matter; a high cosine is not proof that a caption accurately describes an image.

**X2 — Tiny bidirectional contrastive pair loss.** For two correctly aligned image/text IDs and temperature **1**, use a stipulated unnormalized 2×2 similarity-logit matrix **[[2,0],[0,2]]** (this is **not** claimed to be the cosine matrix from X1). Using diagonal positives, image-to-text row softmax cross-entropy and text-to-image column softmax cross-entropy both equal **ln(1+exp(−2)) ≈ 0.1269280110** when averaged over the two correct pairs. The equally weighted bidirectional loss is the same value. A shuffled caption order requires shuffling corresponding positive indices, not silently continuing to treat all diagonal entries as ground-truth positive pairs. Duplicate legitimate captions, related image sources or multiple positives need a properly declared multi-positive objective or exclusion rather than being mislabeled as false negatives.

**F2 — Late fusion and unavailable modality.** For an explicitly two-class **synthetic score-only example** with class order (A,B), a visual model emits logits **(2,0)** and a text model emits logits **(0,1)**. A specified late linear mixing of logits with visual weight **1/4** and text weight **3/4** gives fused logits **(1/2,3/4)**, selecting **B**. With text genuinely unavailable, the declared unimodal visual fallback chooses **A** from logits (2,0), rather than silently pretending that missing text is an all-zero observation trained under the same distribution. Mixing logits from different models is **not automatically probabilistic calibration**; predictions and error costs require independent data evidence. Privacy, visibility and a contradictory caption may prohibit fusion or require human review regardless of the top logit.

**L1 — Scene-group and authorization counterexample.** Suppose two frames/crops from scene A and two from scene B are included in a dataset. Training on A1,B1 and testing on A2,B2 is invalid evidence for generalization to **unseen scenes** because both source scenes appear on each side; training on both A samples and testing on both B samples at least has **zero scene overlap**, though two scenes cannot support a stable population estimate. A separate restricted image with a perfectly relevant caption must be excluded from outputs to an unauthorized requester (including thumbnails and derived descriptions). Removing source rights also requires a documented policy for derived caches, pairs and learned artifacts; a score cannot override authorization.

**Independent assessment rules.** State image shape, channel order, coordinate origins, half-open box endpoints, resampling, label ontology, detection assignment/NMS order, score/tie rule, mask ignore convention, frame timestamps, paired IDs, loss reduction and dataset version for every relevant check. Normal, invalid and changed cases must be observable. A fixed synthetic oracle cannot substitute for actual model training or generalization evidence; no exact GPU timing, language understanding or zero-shot benchmark result is promised. CPU-only local source/arrays and optional equivalent open tooling meet the mandatory conditions.

### Required summative assessments

- **AI8-AS1** (visual input, spatial geometry and target integrity)
  - **Outcomes:** AI8-O1, AI8-O2, AI8-O3, AI8-O4.
  - **Work:** Specify a bounded image-learning task with source/annotation rights and stable scene identities; independently derive V1 pixel normalization/flip and G1 image/box transforms with explicit width/height, channel and half-open coordinate conventions. Implement or transparently inspect paired image/box/mask transforms, a correct nearest-neighbor categorical-mask policy, and a small image/annotation fixture generator. Demonstrate a wrong axis, clipped or zero-area box, interpolation that invents mask classes, a lossily changed source offset or train–test crop identity leak and trace its repair/refusal.
  - **Criteria:** V1 raw mean 111.75, normalized mean 447/1020 and horizontal reflection match public values; G1 original area12, scaled box [2,2,8,10) area48 and original-image flip [4,1,7,5) are independently correct. Valid outputs preserve IDs, bounds, label meaning and source rights; invalid image/layout geometry, misaligned target or split is not silently accepted. No unavailable private data, image or service is required.
  - **Evidence:** Public arrays, annotated source/rights and coordinate contract, exact hand transforms, reproducible source or equivalent inspectable process, paired normal/adverse traces and group provenance.

- **AI8-AS2** (visual classification, features and shift investigation)
  - **Outcomes:** AI8-O5, AI8-O6, AI8-O7, AI8-O19.
  - **Work:** Develop a tiny local shape/pattern classification experiment with a declared image-level target and independent scene-group partition, comparing an explicit pixel/feature or constant baseline with a small AI5-style CNN. Independently calculate F1 horizontal filter responses and predict the effect of reflection. Evaluate one controlled background/illumination/scale or occlusion shortcut, test a wrongly label-changing augmentation and a safer alternative, and compare actual seeded class/group performance, parameters, CPU use and limitations.
  - **Criteria:** F1 responses are (2,2,2) originally and (-2,-2,-2) under the stated reflection, with no unsupported invariance claim. Models are fitted only on permitted train data, fair baseline/seed/resolution comparisons and actual held-out support are visible. A training-score improvement is not mistaken for generalization; robustness/shifts are limited to the studied synthetic distribution.
  - **Evidence:** Independent visual filter oracle, source/split/label/seed records, executed baseline/neural/changed-condition outputs, confusion and group denominators, actual resource notes and uncertainty analysis.

- **AI8-AS3** (object localization, NMS and detection ranking)
  - **Outcomes:** AI8-O3, AI8-O8, AI8-O9, AI8-O10.
  - **Work:** Independently calculate G2 intersection/union/IoU and G1 coordinate transformation, and develop a tiny candidate-box detection/matching implementation for a synthetic multiobject image. Derive D1's confidence-sorted match flags, precision–recall, published single-threshold AP and the result after a specified NMS policy. Demonstrate a duplicate prediction, overlapping legitimate objects, invalid box and modified IoU/score/NMS threshold; identify which match/metric changes and why, and contrast the tutorial AP with COCO's official multi-threshold evaluation.
  - **Criteria:** G2 IoU=3/13; D1 matches TP,FP,TP before NMS, with AP=5/6 under the explicitly **uninterpolated, one-threshold** rule. A duplicate does not get a second GT assignment; after specified NMS P2 is suppressed while P1/P3 remain. Incorrect xyxy conventions, invalid areas and invented COCO mAP equivalences fail; every changed threshold receives an independently checkable match trace.
  - **Evidence:** Bounding-box and detection fixtures, exact intersection/rank/AP derivation, locally executable matching/NMS or equivalent complete trace, negative and changed-case outcomes, CPU observation and scope note.

- **AI8-AS4** (semantic and instance segmentation with spatial correctness)
  - **Outcomes:** AI8-O3, AI8-O11, AI8-O12, AI8-O19.
  - **Work:** Independently derive M1 pixel counts/IoU/Dice/accuracy, and construct a small semantic or instance mask predictor or transparent vision segmentation pipeline on synthetic shapes. Apply controlled image/mask transformations with integer target preservation; diagnose a void-pixel/empty-class, overlapping-instance, misaligned-mask or duplicate-instance case. Verify one enclosing mask box and demonstrate why pixel class and individual object identity demand separate assertions. Compare a simple segmentation baseline with a small learned/parameterized alternative under honest validation.
  - **Criteria:** M1 yields TP2 FP1 FN1 TN5, IoU1/2, Dice2/3 and accuracy7/9, with no ignored pixels. All mask coordinates, IDs, boxes and class supports match the declared annotation version; no new class is created by interpolation. Empty/void and overlapping cases receive correct stated conventions and conclusions. Reported model comparisons are actual observed measurements.
  - **Evidence:** Exact numeric masks and independent metrics, source/annotation and transform trace, normal/invalid/changed case, actual model/baseline measurements and limitations.

- **AI8-AS5** (visual self-supervision, temporal sampling and identity)
  - **Outcomes:** AI8-O4, AI8-O7, AI8-O13, AI8-O14.
  - **Work:** Derive F1 pattern change and T1 timestamped velocity exactly; construct a small visual view-pair/self-supervised or frozen-probe comparison with declared scene/crop identity, at least one legitimate and one label-destroying augmentation, and an independent representation-collapse/shortcut negative control. Build a three-frame synthetic temporal task with real timestamps and a changed/skipped-frame or crossing-identity case; compare a minimal temporal feature/track association to a frame-only baseline, and assess actual per-scene held-out performance.
  - **Criteria:** T1 motion is 2 pixels/second under both valid time intervals, but a wrong skipped-frame time interval gives a spurious 4; physical speed is **not** inferred. Visual positive pairs and held-out clips preserve source grouping, and an invalid label-destroying view is rejected or diagnosed. Duplicate/identity switches and representation collapse are observed with the correct sample/support caveats, not passed off as successful tracking or semantic learning.
  - **Evidence:** Temporal/feature calculations, fixed paired-view and clip/scene identifiers, local transparent source, actual controlled self-supervised/temporal comparisons and negative outcomes, timing/compute records and uncertainties.

- **AI8-AS6** (paired image–text objective and bidirectional retrieval)
  - **Outcomes:** AI8-O15, AI8-O16, AI8-O17.
  - **Work:** Define a small synthetic image+caption corpus with clear pair/qrel identities, language/order/negation counterexamples, legitimate scene descriptions and provenance. Independently derive the X1 cosine similarity table and both directional Recall@1 values, and X2 row/column softmax and bidirectional pair loss. Implement or inspect a small fixed/locally trained dual-encoder alignment with an explicitly stated temperature, positives and seed, and test a caption shuffle, duplicate positive, zero vector or contradicting caption. Evaluate both image→text and text→image retrieval on untuned test pairs with actual measurements rather than using a third-party VLM.
  - **Criteria:** X1 similarity [[1,1/√2],[0,1/√2]], image→text Recall@1=1 and reverse Recall@1=1/2 with ascending-ID tie handling; X2 averaged row, column and symmetric loss all ln(1+exp(-2))≈0.126928011. X2 is not confused with the X1 cosine fixture, and mismatched positive IDs are not silently accepted. A high cosine or correct class name alone does not establish grounded factual understanding of image relations.
  - **Evidence:** Exact paired/vector matrices, independent bidirectional losses/top-k/oracles, versions and rights for image/text sources, local CPU dual-encoder or transparent equivalent, genuine measured retrieval and negative-case traces, interpretation limitations.

- **AI8-AS7** (multimodal fusion, missing data and bounded comparison)
  - **Outcomes:** AI8-O15, AI8-O17, AI8-O18, AI8-O19.
  - **Work:** Derive F2 visual/text fusion scores and the fallback decision independently, then compare image-only, text-only and a declared early or late fusion model on a small synthetic paired/partially missing collection. Demonstrate a swapped pair, conflicting caption, missing image or text, different score calibration and an identity leak under the declared sampling protocol; evaluate actual per-case/scene metrics and abstention/error costs. Distinguish retrieval of a paired item from predicting a joint semantic label and from a generative captioning claim.
  - **Criteria:** F2 1/4(2,0)+3/4(0,1)=(1/2,3/4) chooses B, visual-only fallback (2,0) chooses A; weights/score-scale and missing-modality policy are explicit. No unavailable modality is silently zero-filled and treated as validated evidence without an evaluated training policy. Contradictory or unauthorized inputs do not become accepted visual truth through fusion; comparisons disclose real sample counts, seed and limits.
  - **Evidence:** Hand-calculated fusion/fallback oracle, paired inputs and revised/invalid joins, actual unimodal/combined comparisons, missingness and permission cases, dimensional/score checks and independently reviewable reasoning.

- **AI8-AS8** (vision metrics, shift, rights and source reproducibility)
  - **Outcomes:** AI8-O4, AI8-O7, AI8-O19, AI8-O20, AI8-O21.
  - **Work:** Run a bounded audit across at least one small spatial evaluation and one image–text query experiment, preserving image/scene/clip and paired IDs, complete metric/annotation conventions and source rights. Demonstrate a grouped-split repair for L1, a restrictive/withdrawn image and caption access test, and a perturbed lighting/occlusion or language/scene mismatch with actual per-slice counts. Recompute a D1/M1 or X1 metric under a changed object/label/missing candidate, and explain the difference between toy AP and COCO methodology. Record actual CPU/model/index costs, uncertain judgments and what the local findings cannot support.
  - **Criteria:** L1 original split leaks both scenes and corrected split does not; unauthorized images/captions/thumbnails are never emitted as allowed results. Spatial and retrieval metrics follow documented ground truth, matching, confidence, qrel and aggregation conventions. Actual experiments are independently reproducible with no secret data, GPU or inflated benchmark; exact toy scores are not sold as production validation, global fairness or physical-world safety.
  - **Evidence:** Dataset/split/provenance manifests, source/annotation/query identities, versioned local code and numeric oracles, actual measured comparisons with subgroup supports, forbidden/deleted sample tests, CPU/memory limits and candid reliability report.

- **AI8-AS9** (integrated visual–language artifact and unfamiliar technical defense)
  - **Outcomes:** AI8-O1, AI8-O19, AI8-O20, AI8-O21, AI8-O22.
  - **Work:** Consolidate **one** local, source-licensed/synthetic, learner-owned visual/multimodal study reusing authentic evidence from AI8-AS1–AS8; **do not** require eight independent full-scale systems. Select a bounded visual object/scene and its language descriptor task with explicit rights, annotations, grouping and intended population. Implement one meaningful visual/spatial task and one interacting image–text alignment/retrieval/fusion mechanism, an independently derived numeric fixture, a fair baseline/learned comparison, actual metric/CPU resource evidence and a targeted negative/permission test. The assessor supplies an **unfamiliar bounded** modification such as changed crop/box, overlap threshold, mask or ignore label, frame timestamp, caption pairing, contrastive temperature, fusion weight, missing modality, scene split or visibility rule. Predict the specific changed oracle or nonidentifiable outcome *before execution*, implement a verified correction or safe refusal and prove unaffected behavior remains correct. Defend the actual design, measured uncertainty and unearned generalizations in accessible individual text, audio or live review.
  - **Criteria:** Clean-state source/annotation/model reproduction needs no paid data, GPU, hosted VLM or inaccessible grader, and independently checked geometry, matching, mask, pairing and metric results justify the precise skills claimed. A valid normal/negative/unfamiliar-case set demonstrates a real changed prediction or justified refusal and regression checks. No broad responsible-AI certification, unapproved content release, generative-model mastery, global visual robustness or operational safety certification is inferred. Specialist competencies still require their own substantive AI8-AS1–AS8 outcome evidence even where reused in the integrated artifact; the final defense directly evaluates only integration, evaluation, provenance, permission, reproducibility and unfamiliar transfer outcomes.
  - **Evidence:** One coherent versioned source/evidence collection, synthetic images and captions, box/mask/clip annotations, licensing/permissions and split identity logs, independently checkable exact oracles, actual model/baseline/retrieval outputs, failure/changed-case proofs, budget/limitations report and individual technical defense.

### Required outcome-to-assessment coverage

| Required outcome | Required summative evidence |
| --- | --- |
| AI8-O1 | AI8-AS1, AI8-AS9 |
| AI8-O2 | AI8-AS1 |
| AI8-O3 | AI8-AS1, AI8-AS3, AI8-AS4 |
| AI8-O4 | AI8-AS1, AI8-AS5, AI8-AS8 |
| AI8-O5 | AI8-AS2 |
| AI8-O6 | AI8-AS2 |
| AI8-O7 | AI8-AS2, AI8-AS5, AI8-AS8 |
| AI8-O8 | AI8-AS3 |
| AI8-O9 | AI8-AS3 |
| AI8-O10 | AI8-AS3 |
| AI8-O11 | AI8-AS4 |
| AI8-O12 | AI8-AS4 |
| AI8-O13 | AI8-AS5 |
| AI8-O14 | AI8-AS5 |
| AI8-O15 | AI8-AS6, AI8-AS7 |
| AI8-O16 | AI8-AS6 |
| AI8-O17 | AI8-AS6, AI8-AS7 |
| AI8-O18 | AI8-AS7 |
| AI8-O19 | AI8-AS2, AI8-AS4, AI8-AS7, AI8-AS8, AI8-AS9 |
| AI8-O20 | AI8-AS8, AI8-AS9 |
| AI8-O21 | AI8-AS8, AI8-AS9 |
| AI8-O22 | AI8-AS9 |

**Course completion.** All twenty-two outcomes require independently inspectable, satisfactory evidence under the correct AI8 course revision and the nine assessment contracts above. A single reusable source tree may support multiple skills only when the criteria really measure them. Completing a number of lessons, uploading an image-model checkpoint, relying on an official benchmark score without original split/data provenance, reproducing one toy AP or attending a program does not establish competence. Evaluators must distinguish local exact algebra, observed stochastic results, reproduced code, genuine unfamiliar transfer, and assertions not supported by the evidence. All required review media must have text/table alternatives to image-only presentation. The course is `draft`, not accredited, learner-tested or deployed-vision certified merely because source CI passes.

### Optional open academic, scientific and primary references

- [Stanford CS231n — Deep Learning for Computer Vision, Spring 2026](https://cs231n.stanford.edu/2026/schedule.html) — contemporary image classification, detection, segmentation, video and visual representation course scope.
- [TorchVision transforms v2](https://docs.pytorch.org/vision/stable/auto_examples/transforms/plot_transforms_getting_started.html) — image, boxes, masks, keypoints and video target-consistent transforms with declared data conventions.
- [PyTorch TorchVision detection and segmentation tutorial](https://docs.pytorch.org/tutorials/intermediate/torchvision_tutorial.html) — detection targets, masks, annotation contract and small custom-data pipeline.
- [COCO detection evaluation](https://cocodataset.org/dataset/detection-eval.htm) — official multi-IoU-threshold AP/mAP and precision–recall definitions; not the same as the simplified D1 AP.
- [Learning Transferable Visual Models from Natural Language Supervision](https://arxiv.org/abs/2103.00020) — historical image/text contrastive alignment motivation; large-scale pretrained weights are not mandatory here.
- [OpenAI CLIP research introduction](https://openai.com/index/clip/) — contrasts paired image/text training with single-task supervised vision and discusses transfer limitations.
- [Introduction to Information Retrieval, Stanford/Cambridge online book](https://nlp.stanford.edu/IR-book/) — optional inherited relevance and ranking definitions from AI7.

These are optional accessible reference materials, not additional admission or graduation requirements. All compulsory competencies, reference cases, acceptance criteria, and evaluation limitations are published in this course file itself.
