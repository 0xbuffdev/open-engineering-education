# AI7 — Natural Language Processing & Information Retrieval

**Program:** AI — AI Engineering
**Type:** course
**Prerequisites:** [AI5](AI5.md) — Deep Learning & Representation Learning (completed)
**Duration:** 18–24 weeks
**Status:** draft
**Specification:** v0.2.0
**Expected workload:** 10–15 focused hours/week (provisional; approximately 180–360 focused hours)

> [AI Engineering](README.md) · [Curriculum design guide](../DESIGN-GUIDE.md) · [Course format](../../spec/course-format.md) · [Evidence rules](../../spec/evidence-rules.md)

## Overview

**AI7 develops the ability to represent, analyze, index, rank, retrieve, evaluate and defend work with natural-language data.** Learners must connect language meaning and ambiguity to explicit text-processing contracts, independently checked statistical and neural representations, faithful document indexing, reproducible query relevance judgments, lexical and semantic retrieval, and observed ranking quality. A plausible text label or a top-ranked document is not sufficient evidence that a system understood language, retrieved relevant information or generalized to an intended population. A correct result must be traceable to its source text, transformations, assumptions, evaluation protocol and failures.

**Assessed prerequisite closure.** Direct entry requires completed [AI5](AI5.md), with its transitive [AI4](AI4.md) classical model comparison, sampling and evaluation; [AI2](AI2.md) probability, log loss and mathematical optimization; [AI1](AI1.md) data contracts, provenance and reproducible transformations; and completed Software Engineering Foundations. AI5 already assesses embedding lookup, small recurrent encoders, contrastive objectives, gradient-safe training and representation-transfer claims. AI7 **does not re-teach** those mathematical or general neural mechanisms: it applies them to **language-specific token/vocabulary semantics, annotation, morphology and syntactic ambiguity, supervised text/sequence tasks, linguistic error taxonomies, index mechanics, search ranking and relevance-based information retrieval**. [AI3](AI3.md) symbolic reasoning, [AI6](AI6.md) reinforcement learning and any APP/SYS course are not required prerequisites.

**Deliberate neighboring-course exclusions.** AI9 owns transformer attention, causal/positional masking and generative language modeling; AI10 owns adaptation and advanced model optimization; AI11 owns full retrieval-augmented generation (RAG) including generation grounded in retrieved evidence; AI12 owns tool-using agents; AI13 owns larger AI-system assurance; AI14 owns broader AI governance; AI15 owns production service infrastructure and MLOps. AI7 teaches **retrieval itself**—including independently tested embedding-based search, lexical retrieval, ranked relevance and small reranking—without obliging a text generator, hosted embedding API, transformer architecture or operational RAG pipeline. Speech and audio belong to optional AI17; advanced graph embeddings to AI20. A small local neural sequence tagger or frozen embedding encoder is appropriate here, not a mandatory pretrained large language model.

**Environment, rights and accessibility.** All compulsory evidence must be possible with a compact local **synthetic or permissively licensed** text collection, explicit relevance judgments, accessible textual traces and ordinary CPU computation. Python 3 standard-library text/collections/math operations suffice for lexical and metric oracles; an open library or small AI5-style locally trained or fixed-weight neural encoder may support semantic and tagging experiments, without GPU or an account. Indexes must preserve stable original document IDs, offsets, language/script metadata where available, source/license identifiers, content hashes or equivalent provenance and a declared Unicode/tokenization policy. No private chat logs, personal emails, high-risk personal data, copyrighted closed corpus, paid API, commercial index, cloud service or secret evaluation benchmark is required. Learners may use alternative languages/frameworks if they meet the public behavioral criteria. All graphical outputs require equivalent tables or descriptions.

**Academic sequence and summative design.** Thirteen competency stages connect language data and annotation contracts to independently checked probabilistic/neural text models, lexical indexing, relevance evaluation, semantic/hybrid retrieval and controlled failure analysis. Mechanism checks, counterexamples and reproducible evidence remain within the lessons they test rather than becoming repeated standalone objectives. Eight required summative assessments establish **20 observable outcomes** and may reuse one versioned, reproducible evidence repository: independent Unicode/annotation oracle; probabilistic and sequence labeling; small neural text representation; lexical search; retrieval evaluation; dense/hybrid search; robustness/error/privacy audit; and an integrated unfamiliar change with an individual technical defense. Exact synthetic oracles are defined below. Any additional neural accuracy, retrieval improvement, latency, language-transfer performance or confidence interval must be obtained from **actual executed experiments** and honestly reported with conditions and uncertainty. The workload estimate is provisional; validation tools and a coherent source file do not establish learner-tested educational readiness.

## Learning outcomes

- **AI7-O1:** Define a bounded NLP or retrieval question with language population, document/query or annotation unit, authorized source data, task target, relevant evidence, computational budget and limitations on the resulting claim.
- **AI7-O2:** Normalize and process Unicode text without corrupting code points, byte/character/grapheme/offset identity, language-specific distinctions or original-source provenance, and diagnose lossy or invalid transformations.
- **AI7-O3:** Design and compare word, character, rule-based and subword tokenization/segmentation policies with explicit vocabulary and out-of-vocabulary behavior, casing, punctuation, reserved tokens and train-only fit boundary.
- **AI7-O4:** Specify and validate linguistic annotations and exact-span/token-level evaluation contracts, including label ontology, BIO legality, offsets, ambiguous evidence and independently measured inter-annotator disagreement.
- **AI7-O5:** Analyze linguistic morphology, syntax, scope, negation, ambiguity and compositional relations in small texts; explain why bag-of-words or superficially plausible statistical outputs may miss task-relevant meaning.
- **AI7-O6:** Construct, fit or independently check count-based language/text classification and conditional-probability baselines, interpreting smoothing, corpus frequencies, class imbalance and unjustified independence assumptions.
- **AI7-O7:** Derive and inspect bounded sequence-tagging or structured-prediction inference, including a correctly normalized finite probabilistic tag model, Viterbi/decoding trace, tag constraints and failure behavior.
- **AI7-O8:** Build and evaluate a small neural text/sequence encoder, word or subword representation and tag/classification head with valid padded batching, target masks, source identity, independent shape/probability checks and an appropriate simpler baseline.
- **AI7-O9:** Construct a reversible and inspectable lexical document index with stable identifiers, term counts, document lengths, positional postings where required, update/deletion semantics, collection statistics and invalid-input behavior.
- **AI7-O10:** Calculate and explain term weighting and ranked lexical retrieval, including TF–IDF and a fully specified BM25 variant with exact independent finite-corpus scores, tie conventions and parameter sensitivity.
- **AI7-O11:** Execute and independently verify Boolean, phrase, proximity or field-constrained retrieval using correctly ordered postings/positions and declared analyzer/query semantics.
- **AI7-O12:** Build and audit fixed query/relevance judgment sets, distinguishing document availability, graded/binary judgments, unjudged items, relevance uncertainty, incomplete pooling and invalid train/evaluation reuse.
- **AI7-O13:** Calculate and interpret precision/recall at a cutoff, AP/MAP, reciprocal rank/MRR and graded DCG/nDCG under explicitly stated ranking/tie/unjudged conventions, including undefined and low-support cases.
- **AI7-O14:** Implement and analyze finite dense semantic retrieval with legitimate embedding provenance, vector normalization and cosine/dot/L2 conventions, correct top-k behavior, zero-vector and domain/language failure tests.
- **AI7-O15:** Construct and fairly evaluate lexical+dense fusion or reranking with explicitly defined rank/score normalization, candidate recall ceiling, query/doc leakage boundaries and measured versus hypothetical improvement.
- **AI7-O16:** Investigate tokenization, tagging and retrieval failures under multilingual text, code-switching, dialect, spelling, morphological variation, negation, ambiguity and unequal subgroup/query coverage, without unsupported fairness or cross-language claims.
- **AI7-O17:** Enforce document/query provenance, source licensing, privacy boundaries, access constraints and data-integrity controls, refusing unsafe release of restricted content or overclaiming trust from relevance alone.
- **AI7-O18:** Measure and explain index/storage complexity, sparse/dense candidate behavior, ranking costs, top-k memory/CPU constraints, update correctness and reproducible query-time observations, without claiming production-scale readiness.
- **AI7-O19:** Create clean-state independently checkable NLP/IR evidence with immutable test fixture IDs, fit/split/query identities, exact hand oracles, relevant negative controls, actual evaluation logs and bounded reported conclusions.
- **AI7-O20:** Respond to an unfamiliar bounded change to language normalization, annotation scheme, document update, query, relevance judgment, weighting, embedding, access rule or evaluation protocol by independently predicting the effect, demonstrating valid repair or safe refusal and defending remaining limitations.

## Modules

### Module 1 — Language and Retrieval as Evidence-Bearing Engineering Tasks

#### Outcomes

- AI7-O1
- AI7-O4
- AI7-O12
- AI7-O17

#### Lessons

1. **Language and retrieval as historical, evidence-bearing engineering** — Connect rule-based linguistic analyses, count/probabilistic models, learned representations and lexical–dense search to appropriate applications in document discovery, text classification and entity extraction. Explain how language ambiguity, speaker intent, retrieval relevance and valid statistical predictions make different claims; neither a plausible label nor a top-ranked hit proves understanding, source truth or user authorization.
2. **Task, population and source-unit contracts** — Distinguish text classification, sequence tagging, exact-span extraction, query retrieval and ranked results. Name the intended language/domain population, stable original document and derived passage IDs, query/session identities, annotation unit and sampling dependencies so repeated queries or passages cannot masquerade as independent evidence.
3. **Linguistic and retrieval success criteria** — Distinguish exact span identity, label correctness, top-k relevance and user satisfaction, predeclaring which one can actually be assessed locally.
4. **Source rights, privacy and query permissions** — Establish license, version, sensitive-content rules, document-level access restrictions, deletion and whether a legitimate user's query permits returning a passage.
5. **Baselines, budgets and counterclaims** — Select transparent model/search baselines, a reproducible CPU budget, invalid/unknown-case behavior and at least one important claim the experiment cannot support.

*Optional formative prompt:* Describe why retrieving a highly relevant restricted document is still a policy failure, even if its ranking metric is perfect.

### Module 2 — Unicode, Segmentation and Vocabulary Contracts

#### Outcomes

- AI7-O2
- AI7-O3
- AI7-O16
- AI7-O17

#### Lessons

1. **Bytes, Unicode code points and grapheme clusters** — Separate UTF-8 storage length, code point index and user-perceived characters; show why blind byte slicing can corrupt valid source text.
2. **Reversible Unicode normalization, annotation and original offsets** — Compare composed/decomposed accent representations under NFC and NFD while preserving a mapping from normalized positions/tokens to the unmodified source. Independently check half-open original code-point spans and grapheme boundaries; reject impossible, shifted or silently reconstructed offsets when annotating or extracting source text.
3. **Case handling and language specificity** — Distinguish lowercasing, case folding and language-specific casing; demonstrate a counterexample where indiscriminate case/diacritic removal changes identity or meaning.
4. **Word boundaries, punctuation and apostrophes** — Specify analyzer behavior for contractions, hyphenation, hashtags, numbers, emojis and punctuation rather than assuming ASCII whitespace always defines a word.
5. **Sentence segmentation and abbreviations** — Construct a bounded sentence-boundary ambiguity involving initials, periods or quotations, with an independently judged expected segmentation.
6. **Morphology and segmentation variation** — Explain inflection, agglutination, compounds and languages with different written word boundaries; label a claimed universal segmentation heuristic as unsupported.
7. **Subword vocabulary and rare forms** — Trace one finite byte/character/subword merge, specify reserved/unknown tokens, sequence-length effects and how learning a vocabulary on evaluation text contaminates the test boundary.
8. **Tokenization stress harness** — Build a small fixed corpus with combining marks, mixed scripts, punctuation, empty text and a fabricated invalid byte stream; record recovery/refusal and language-specific limitations.

### Module 3 — Annotation, Linguistic Structure and Semantic Ambiguity

#### Outcomes

- AI7-O1
- AI7-O4
- AI7-O5
- AI7-O16

#### Lessons

1. **Annotation guidelines are measurement instruments** — Define the target task, ontology, evidence window, uncertain/unknown label, example boundaries and correction process before collecting labels.
2. **POS and morphological features** — Distinguish syntactic category from a word's surface form in a short sentence, explaining why ambiguity can require context.
3. **BIO entity spans and representation limits** — Encode exact original-text entity boundaries and types under a stated BIO2 policy, reject illegal I-tag openings and diagnose mismatched source offsets. Demonstrate why a flat BIO representation cannot faithfully encode every nested or discontinuous entity, and choose an explicit alternative or an honest exclusion rather than inventing a legal tag sequence.
4. **Constituency and dependency relationships** — Trace head–dependent or phrase-structure roles on a minimal sentence while distinguishing a chosen analysis from the entire space of possible parses.
5. **Negation, scope and semantic roles** — Compare “dog chased cat” with “cat chased dog” and negated propositions; show what a count-only representation loses despite identical word counts in role-reversed sentences.
6. **Ambiguity and pragmatic context** — Construct a sentence with genuinely multiple supported readings; state what context an annotation policy requires rather than claiming the model can infer the speaker's intent.
7. **Inter-annotator agreement and adjudication** — Count exact matched/disagreed labels on a small fixed sample, compare observed agreement with simple prevalence, and explain why agreement is not validity or population representativeness.
8. **Boundary-aware label evaluation** — Independently calculate exact span true/false positives and false negatives, contrasting token-level scores with full-span correctness.

### Module 4 — Count-Based Text Models and Language Probabilities

#### Outcomes

- AI7-O5
- AI7-O6
- AI7-O19

#### Lessons

1. **Term counts and document frequency** — Derive term/document counts from a fixed corpus with explicit duplication and normalization semantics, without retraining AI4's generic tabular statistics.
2. **n-gram conditional language evidence** — Calculate a tiny bigram probability from token counts, distinguish a conditional distribution from a complete model of discourse and identify zero-count behavior.
3. **Smoothing and unseen text** — Apply an explicitly parameterized additive count prior to a small vocabulary and show why unknown-vocabulary treatment and denominator changes matter.
4. **Naïve Bayes text classification** — Apply the AI4 probabilistic-classifier foundation to word-count/multinomial text evidence, independently deriving a small posterior from token likelihoods.
5. **Class prior, length and correlated token assumptions** — Demonstrate why repeated correlated words, class imbalance and document length can make a simple conditional independence model overconfident.
6. **Sparse linear lexical baselines** — Construct a transparent linear document classifier from TF–IDF or binary terms under training-only vocabulary/IDF fitting, contrasting its attribution with real linguistic understanding.
7. **Count-model negative controls and lost linguistic structure** — Test empty/unseen text, changed token order, correlated evidence and annotation disagreements against an explicitly defined count-based baseline. Use a same-multiset role-reversal or altered-negation case to show what unordered bags irreversibly discard, and distinguish a lawful prior-only fallback from unsupported claims of language comprehension.

### Module 5 — Sequence Labeling and Structured Decoding

#### Outcomes

- AI7-O4
- AI7-O7
- AI7-O8
- AI7-O19

#### Lessons

1. **Token/sequence labels, exact spans and legal training targets** — Connect POS and BIO token tags to actual source spans and downstream intended targets; check tag-sequence legality under a declared ontology. Diagnose an illegal BIO transition, subword-to-token mapping defect or accidental padding/duplicate-span loss contribution rather than accepting each locally plausible token label as a legal entity annotation.
2. **Finite hidden-state emission model** — Define initial, transition and emission distributions with explicit normalization and token vocabulary, and distinguish learned probability tables from observed linguistic truth.
3. **Viterbi dynamic programming** — Calculate best path scores and backpointers for a length-two finite HMM, keeping the maximum-path probability distinct from the observation's total likelihood.
4. **Forward probabilities and alternatives** — Sum over possible hidden state sequences to obtain the observed token likelihood; explain why Viterbi's maximum path is not the same operation as marginalization.
5. **Conditional sequence models and constraints** — Contrast a generative HMM with a discriminative linear-chain score or CRF-style normalization, showing where BIO constraints can forbid transitions.
6. **Feature-based versus recurrent tagging** — Build a token/window baseline and a tiny AI5-style recurrent encoder head, demonstrating padding/length masks and correct output dimensions.
7. **Annotation and entity metric audit** — Evaluate both token labels and exact-span entity predictions on a public fixture, declaring strict boundary/type matching and empty-span conventions.
8. **Negative-case investigation** — Explain failures from unknown terms, disagreement between annotators, shortened context or a changed label ontology without reinterpreting test labels during fitting.

### Module 6 — Neural Language Representation and Bounded NLP Tasks

#### Outcomes

- AI7-O3
- AI7-O5
- AI7-O8
- AI7-O16

#### Lessons

1. **Distributional representations and their limits** — Explain why co-occurrence can support usable similarity without guaranteeing that related words, antonyms or names share intended meaning.
2. **Embedding lookup with language vocabulary** — Apply AI5's trained lookup/gradient mechanics to an explicit token-to-index mapping, unknown/pad policy and source-language metadata.
3. **Composition across token order** — Compare sum/mean pooling and a small recurrent encoder on order-sensitive texts, independently verifying what a bag representation cannot distinguish.
4. **Sequence mask and length correctness** — Verify that padding tokens do not alter legitimate sequence summaries or classification/tagging losses and that length bookkeeping is reproducible.
5. **Small neural text heads, lawful training and simpler comparisons** — Build a CPU-feasible classifier or bounded sequence tagger using a language-specific vocabulary, output shape, label mask and correct train/validation selection. Compare the locally learned representation with a count/window/linear baseline under matched corpus and sample identities; observed improvement must be measured, not inferred from using neural layers.
6. **Representation probing is limited evidence** — Inspect nearest neighbors, similarity rankings and a syntactic/semantic contrast while stating why they are not causal mechanisms or guarantees of lexical correctness.
7. **Domain and language failure cases** — Test code-switching, negation, unfamiliar morphology or shortened context with actual observed scores and appropriate insufficient-evidence notes.

### Module 7 — Index Construction, Query Matching and Lexical Ranking

#### Outcomes

- AI7-O9
- AI7-O10
- AI7-O11
- AI7-O18

#### Lessons

1. **Collection and document identity** — Define unique source document IDs, revisions, field boundaries and stored raw/normalized representations without permitting duplicated passage identifiers to masquerade as independent documents.
2. **Inverted postings and term positions** — Build term→sorted document-ID postings, frequencies and positional lists; justify why lexical search does not rescan every byte of every document for every query.
3. **Boolean retrieval and posting intersection** — Hand-evaluate AND/OR/NOT over a specified corpus universe, distinguishing missing query terms from missing documents.
4. **Phrase and proximity matching** — Verify “red cat” consecutive positions and an altered-order phrase; explain why term co-occurrence alone cannot prove a phrase match.
5. **Term, document and TF–IDF statistics** — Calculate corpus size, per-document term frequency, document frequency, document length and mean length under one declared analyzer and deletion policy. Derive a specified TF–IDF scheme with its TF scaling, IDF smoothing and log base, and show how adding/removing an indexed document can change scores; these statistics also provide the independently checked inputs to BM25.
6. **BM25's probabilistic ranking heuristic** — Calculate the published BM25 formula exactly with fixed k1, b and smoothed IDF; distinguish a ranking score from a probability of truth or relevance.
7. **Ranking ties, unknown queries and top-k** — Return a deterministic result order under equal scores, handle zero-match queries, document invalid term policies and avoid claiming arbitrary top-k truncation preserves total recall.
8. **Field weighting and analyzers** — Investigate one title/body, case or stemming variant with a published field/normalization contract instead of silently changing term frequencies.
9. **Index mutation and provenance** — Add/update/delete an identified document, invalidate affected postings/corpus statistics, honor access restrictions and verify that a stale document never persists in results.

*Optional feedback:* For the public L1 corpus, produce the postings for “red” and “cat,” and show which document satisfies the phrase “red cat” with exact offsets.

### Module 8 — Relevance Judgments and Retrieval Evaluation

#### Outcomes

- AI7-O1
- AI7-O12
- AI7-O13
- AI7-O19

#### Lessons

1. **Information needs versus query strings** — Define a user's need, search query, document relevance and correct granularity; explain why matching tokens are not a universal relevance oracle.
2. **Qrels, corpus identity, completeness and judging policy** — Specify query/document IDs, corpus revision, binary/graded relevance scale, assessor uncertainty and the boundaries of exhaustive judgments versus incomplete pooled judgments. Preserve 'unjudged' separately from 'nonrelevant'; an incomplete pool is not a fully known negative set, and a mismatched corpus/qrel revision invalidates derived scores.
3. **Rank and cutoff conventions** — Compute precision@k, recall@k, hit/reciprocal rank under specified k and denominator, tie ordering and no-relevant-query policy.
4. **Average precision and MAP** — Sum precision at the ranks of relevant documents, normalize by the correct relevance count, and average across explicitly selected queries.
5. **Graded DCG and nDCG** — Calculate discounted gain with a stated gain function/log base, derive the ideal ranking and handle an IDCG of zero as undefined or an explicitly documented evaluation convention.
6. **Per-query uncertainty and aggregation** — Report each query's support and error, compare macro averaging and query-weighted metrics and avoid treating related queries or duplicate sessions as independent samples.
7. **Judgment robustness and disagreement** — Recompute a metric after changing one disputed relevance label and state how the ranking conclusion depends on that label.
8. **Evaluation leakage and post-selection bias** — Prevent query-specific tuning on a final evaluation pool, identify a collection/qrel mismatch and explain why a perfect mini-benchmark result cannot certify real search quality.

### Module 9 — Dense Semantic Retrieval and Vector Geometry

#### Outcomes

- AI7-O8
- AI7-O14
- AI7-O16
- AI7-O18

#### Lessons

1. **Query and document encoders** — Define a small embedding function with declared training provenance, dimension, language coverage and compatible input preprocessing.
2. **Cosine, dot, L2 and independent vector-failure checks** — Derive exact similarity and changed-norm ranking for small finite vectors, stating whether and how they are normalized. Reject a zero vector under cosine, mismatched dimensions, nonfinite components or an incompatible encoder revision instead of silently assigning a plausible score; similarity remains evidence of geometry, not established linguistic relevance or factual truth.
3. **Semantic retrieval versus lexical matching** — Test synonym-like paraphrases and exact entity/product codes on synthetic paired queries, identifying where either lexical or embedding retrieval is systematically advantaged.
4. **Vector-index construction** — Store document-ID vectors and a versioned encoder fingerprint, verify dimensions/finite components and refuse mixing incompatible encoder revisions.
5. **Exact dense top-k retrieval** — Score all vectors in a small corpus under a published deterministic tie policy and independently verify rank/order before considering approximations.
6. **Approximate nearest-neighbor intuition** — Explain graph/partition/compression search trade-offs and measured candidate recall, noting that approximate ranking results need not be exactly top-k.
7. **Representation shift and multilingual coverage** — Investigate spelling, script, morphological and language changes, separating observed cross-language alignment from unearned universal multilingual capability.
8. **Resource and accuracy comparisons** — Compare exact local vector search with a simple lexical baseline on the same qrels, recording actual CPU/storage/dimension/query costs without requiring industrial indexes.

### Module 10 — Hybrid Retrieval, Reranking and Candidate Limits

#### Outcomes

- AI7-O10
- AI7-O12
- AI7-O14
- AI7-O15

#### Lessons

1. **Why scores cannot be naively added** — Contrast arbitrary BM25 scales with cosine intervals and show a counterexample in which uncalibrated sums produce an artificial ranking.
2. **Rank fusion, missing candidates and the exact H1 oracle** — Derive reciprocal-rank fusion using a fixed positive smoothing constant, correct corpus/document IDs, stable tie-breaking and a zero contribution for missing candidates. Independently calculate both H1 rankings and their combined scores, including why the new order differs from either input; never naively add incomparable BM25 and cosine values.
3. **Candidate generation and reranker ceilings** — Explain why a reranker selecting from a top-k candidate set cannot recover relevant documents that all candidate generators omitted.
4. **Lightweight feature-based reranking** — Construct a tiny feature vector from lexical match, dense similarity and explicit document signals; train a bounded AI4-style reranker only on permitted training judgments.
5. **Pointwise, pairwise and listwise distinctions** — Explain what prediction target each ranking formulation learns and how group-by-query boundaries affect examples and leakage.
6. **Ablation with relevance oracles** — Compare lexical-only, dense-only, RRF/hybrid and a permitted reranker, using fixed qrels, same index version and honestly obtained per-query metrics.
7. **Interpretability and failure of fusion** — Diagnose a new query on which hybrid is worse, document the candidate/normalization cause and refuse a universal relevance-improvement claim.

### Module 11 — Multilinguality, Privacy and Failure Boundaries

#### Outcomes

- AI7-O2
- AI7-O4
- AI7-O16
- AI7-O17

#### Lessons

1. **Languages, scripts and communities are not one unit** — Declare the languages, scripts, code-switching patterns and dialects actually supported by training/evaluation, without essentializing speakers or inferring identity.
2. **Tokenization disparities across scripts** — Compare observed segmentation and retrieval failures for concatenated, morphologically rich and multi-script strings, stating what the tiny corpus does not represent.
3. **Negation, ambiguity and domain drift** — Investigate one sentence with changed roles/negation and one shifted query intent; show how labels and rankings depend on the task's declared semantics.
4. **Entity and annotation disagreements** — Diagnose boundary/type mistakes or a change in annotation ontology, preserving the original adjudication record rather than quietly overwriting qrels.
5. **Measured slice coverage, disputed evidence and responsible refusal** — Count actual examples and queries per declared language/dialect/script slice, report sparse/undefined measures and annotation or judgment disagreement without claiming universal fairness or language support. When the evidence is missing, a result is out of scope or a relevant document is restricted, specify a justified abstention, review or safe refusal rather than filling unknown cases with invented relevance.
6. **Licensing, private text and retention rules** — Decide whether a source can be indexed, copied, surfaced or retained; implement delete/restrict behavior for an identified sensitive or withdrawn document.
7. **Query-time access and untrusted content** — Enforce visibility filtering **before** ranking/passage release; treat retrieved document text as data rather than instructions and do not infer authorization from high relevance.

### Module 12 — Reproducible Experiments, Error Forensics and Resource Accounting

#### Outcomes

- AI7-O12
- AI7-O13
- AI7-O16
- AI7-O17
- AI7-O18
- AI7-O19

#### Lessons

1. **Reproducible corpus, query and model-selection contract** — Pin source revision and license, analyzer/encoder versions, original document IDs, index/configuration hashes, query/judgment revisions and resource budget. Partition repeated or near-duplicate queries and their contexts consistently with the intended population; log every attempted ranking configuration and keep genuinely final evaluation judgments outside all tuning decisions.
2. **Assert index invariants** — Validate postings order, term counts, positions, deletions, corpus statistics and absent documents with an independent brute-force oracle on a tiny public collection.
3. **Reproduce small metric calculations** — Compute a published AP/MAP/nDCG/precision result without using the ranking implementation under test or trusting a library's default qrel handling.
4. **Classify errors by mechanism** — Trace text normalization, segmentation, annotation, morphology, token matching, embedding similarity, candidate recall, reranking, access control and qrel disagreement to separate causes.
5. **Memory, CPU and index-size accounting** — Measure observed index-build/query latency and memory under bounded conditions, distinguishing input/corpus scale and implementation overhead from broad performance guarantees.
6. **Evaluate change and regression** — Modify one analyzer/embedding/index field and verify which previously correct term/spans/ranks/metrics must remain invariant, explicitly recording changed oracle expectations.
7. **Report uncertainty and non-claims** — Present actual per-query and language-slice results with denominators, disagreement and missing judgments; distinguish completed local research from deployment readiness, factual truth or universal language coverage.

### Module 13 — Integrated Language Retrieval Study and Unfamiliar Defense

#### Outcomes

- AI7-O1
- AI7-O3
- AI7-O10
- AI7-O12
- AI7-O13
- AI7-O14
- AI7-O15
- AI7-O16
- AI7-O17
- AI7-O18
- AI7-O19
- AI7-O20

#### Lessons

1. **One bounded retrieval question with legitimately reused assessed evidence** — Choose a small permitted or synthetic corpus with a stated language, source rights, query-information needs, fixed relevance judgments, stable versioned index and meaningful lexical baseline. Reuse previous tokenization, tagging, postings, metric and neural evidence only where actually assessed, selecting representations that materially contribute to one coherent retrieval investigation rather than reimplementing seven disconnected projects.
2. **Build normal and changed-case oracles** — Independently establish a few correct postings, BM25 scores, a qrel-based ranking measure, and a vector/hybrid reference with the exact declared conventions.
3. **Measured lexical, dense and hybrid evidence with honest limits** — Execute comparable runs on one frozen corpus/query/qrel contract, report actual per-query relevance and CPU/index costs, and diagnose a false positive, false negative, missing judgment, annotator dispute or misleading embedding similarity from independently inspectable facts. Separate observed performance from assumptions about general language coverage, semantic truth, query intent or operational readiness.
4. **Test adverse and permission cases** — Introduce an inaccessible document, an unsupported language or query, a shifted token boundary, incomplete qrel, zero vector or duplicate and prove correct handling.
5. **Unfamiliar assessor-supplied change** — Predict the specific impact of a new document term, index deletion, punctuation/normalization rule, query variant, qrel correction, embedding revision or access restriction before execution; repair or safely refuse the affected output.
6. **Accessible technical defense** — Provide a clean-start independently repeatable run, corrected/new oracle and traceable reasoning about provenance, evaluation split, actual metric/cost findings, known blind spots and individually attributable engineering decisions.

Modules describe learning sequences rather than thirteen separate required submissions. The **eight** summative evaluations below are the sole required assessment contracts, and shared legitimate work may be reused when the relevant outcome is actually demonstrated.

## Completion requirements

### Shared public reference fixtures and independent conventions

The following compact synthetic cases are **public reference oracles**, not hidden benchmark scores. A substitute is valid if the learner publishes an equally exact independent reference and all required invalid/changed cases. Exact fixture values must not be confused with results obtained on another corpus or analyzer. Unicode/source offsets are measured in **code points on the original string** unless a fixture explicitly says otherwise.

**U1 — Unicode normalization, token preservation and source offsets.** Let source A be the code-point sequence `Cafe\u0301` (letter e followed by U+0301 combining acute accent) and source B be `Café` with the precomposed U+00E9 code point. NFC normalization maps both to the same visible/code-point sequence `Café`, but A has **five** code points before normalization while B has **four**. A byte index, code-point index and grapheme boundary are not interchangeable. A normalized index cannot automatically be used as an offset into A without a valid source-to-normalized alignment. Normalize before matching only with a documented field policy and preserve original content for citation/extraction. An invalid UTF-8 byte sequence must be explicitly rejected or decoded under a named replacement policy; silently truncating bytes is unacceptable. Language-dependent case/diacritic stripping is **not** presumed harmless.

**S1 — BIO span and exact-boundary annotation.** Original text is `New York hosts Ada`. Under Unicode code-point half-open offsets the token sequence `New`, `York`, `hosts`, `Ada` has spans **[0,3), [4,8), [9,14), [15,18)**. Gold BIO2 tags are `B-LOC I-LOC O B-PER`; gold entity spans are **LOC [0,8)** and **PER [15,18)**. The hypothetical predicted spans LOC [0,8) and PER [9,14) have **TP=1, FP=1, FN=1** and strict exact-span precision, recall and F1 of **1/2** each. A predicted initial `I-LOC` without a prior compatible open entity is invalid under the declared strict BIO2 policy; do not silently repair without stating a chosen coercion policy. Span matching checks both type and boundaries, not just a token count.

**P1 — Text Naïve Bayes with explicit model assumptions.** A categorical token model has class priors P(A)=P(B)=1/2, and a two-token vocabulary `cat,dog` with P(cat|A)=3/4, P(dog|A)=1/4, P(cat|B)=1/4, P(dog|B)=3/4. Under conditional independent **ordered draws** (the order is ignored by the bag model), for observation `cat cat` the unnormalized class weights are **9/32** for A and **1/32** for B, yielding P(A|cat cat)=**9/10**. Observation `cat dog` yields equal unnormalized weights **3/32** and posterior 1/2 for each class. This is a stipulated model, not a demonstrated property of actual text: repeating correlated terms can strongly overstate evidence. This fixture's probabilities already sum to one over the vocabulary, so no extra smoothing constant may be silently introduced.

**T1 — Tiny hidden Markov tagger and Viterbi inference.** Hidden tags are N and V, with initial P(N)=3/5, P(V)=2/5; transitions P(N→N)=1/5, N→V=4/5, V→N=7/10, V→V=3/10; emissions for exactly two possible tokens `dogs` and `run` are P(dogs|N)=4/5, P(run|N)=1/5, P(dogs|V)=1/5, P(run|V)=4/5. For observation `dogs run`, the joint path probabilities of **NN, NV, VN, VV** are respectively **0.0192, 0.3072, 0.0112, 0.0192**, with total observation probability **0.3568** and highest-scoring Viterbi path **N,V** with joint probability **0.3072**. All probability rows normalize. Viterbi max-path evidence is distinct from forward-sum likelihood and does not establish the linguistic truth of a particular label on another corpus.

**L1 — Lexical index, postings, phrase and BM25.** Use **exact lowercase whitespace tokenization** with three equally long synthetic documents: d1=`red cat runs`, d2=`blue cat sleeps`, d3=`red dog runs`; lengths are all 3, mean document length 3, N=3. Postings for `red` are d1 position 0 and d3 position 0; for `cat` are d1 position 1 and d2 position 1. Query `red cat` has document frequencies df(red)=df(cat)=2, one occurrence of each matching term per matching document; only d1 contains that **exact phrase**. Choose **BM25 k1=6/5, b=3/4**, term IDF defined as `ln(1 + (N - df + 1/2)/(df + 1/2))` and term-frequency contribution `IDF × [tf(k1+1)/(tf + k1(1-b+b·length/avg_length))]`. Therefore each matched term contributes **ln(8/5) ≈ 0.4700036292**, so d1 scores **2 ln(8/5) ≈ 0.9400072585**, and d2,d3 each score **ln(8/5)**. A stable tie rule of ascending document ID ranks d1,d2,d3 for `red cat`; a query containing only an absent token such as `green` returns no matches, rather than arbitrarily ranking zero-score documents as evidence. The output is a **ranking score, not a probability of relevance**. If indexing/removing a document changes N, df or length statistics, all affected scores must be recomputed.

**E1 — Query judgments and retrieval metrics.** For q1, judged relevant documents are d1 and d3; a ranked run is **[d1,d2,d3]**, and exactly two relevant documents exist in this *fully judged three-document collection*. Thus **P@2=1/2, recall@2=1/2, AP(q1)=(1+2/3)/2=5/6**, and reciprocal rank is 1. For independent q2, the only relevant document is d2 and run **[d3,d2,d1]**, giving **AP(q2)=1/2** and reciprocal rank 1/2. Over these two declared queries **MAP=2/3** and **MRR=3/4**. For graded q1 judgments d1 grade2, d3 grade1, d2 grade0, with gain `2^grade−1` and discount `log2(rank+1)`, the ranked q1 run has **DCG@3=7/2**, ideal DCG@3=**3+1/log2(3)** and **nDCG@3=(7/2)/(3+1/log2(3)) ≈ 0.964**. These are fully judged synthetic fixtures. If qrels are incomplete, or a query has no judged relevant document, the evaluator must disclose the exact unjudged/no-relevant policy and cannot silently use these numbers.

**D1 — Finite dense similarity and invalid vectors.** For cosine similarity, query vector q=(1,0), document vectors d1=(1,0), d2=(0,1), d3=(-1,0), all nonzero: **cos(q,d1)=1, cos(q,d2)=0, cos(q,d3)=-1**, so exact top-k order is d1,d2,d3 for k≤3. The zero vector has undefined cosine due to a zero norm and must be rejected or handled under an explicit noncosine fallback. Dot product may rank differently after norm scaling, so an implementation must state which metric it computes. These vectors are synthetic; no real semantic-language quality is established by their geometry.

**H1 — Hybrid reciprocal-rank fusion.** With lexical ranking **[d1,d2,d3]**, dense ranking **[d3,d1,d2]**, all candidates present and a deliberately small **k=1** for visible hand calculation, define `RRF(d)=1/(1+rank_lexical(d))+1/(1+rank_dense(d))` with ranks starting at 1. Then **RRF(d1)=5/6, RRF(d3)=3/4, RRF(d2)=7/12**, producing hybrid order **[d1,d3,d2]**. This k is a pedagogical toy, **not** a recommended production constant. For candidates missing from one ranking, that ranking contributes zero by the stated policy; never invent a position or merge document IDs from different corpus versions.

**N1 — Linguistic role, privacy and access negative cases.** The short texts `dog chased cat` and `cat chased dog` have the same word-count multiset but reversed agent/patient roles, so an unordered unigram bag cannot distinguish them under the stated representation. A private d4 document that matches a query perfectly is **not** releasable to an unauthorized requester: remove it from the authorized candidate universe before showing snippets, scoring, ranking or evidence, then recalculate any collection-level statistics under the explicitly chosen public/private indexing model. An index update that leaves a revoked d4 passage visible fails regardless of improved lexical relevance. A retrieved text's contents are untrusted documents, not instructions to the search system.

**General assessment rules.** All exact values require the stated Unicode, token, relevance, ranking, probability, model and offset conventions. Learners must publish genuine measurements—not fictitious metric or latency thresholds—for other corpora, language slices, encoders and experimental runs. Explicit negative cases include malformed Unicode, OOV and empty text, illegal BIO transitions, unnormalized language probabilities, missing index postings, stale deletions, unknown query terms, partial judgments, zero vectors, encoder mismatch, duplicated identities and restricted documents. Clean-state reproduction must require no cloud/GPU/API account or protected dataset.

### Required summative assessments

- **AI7-AS1** (language data contract, Unicode, segmentation and span integrity)
  - **Outcomes:** AI7-O1, AI7-O2, AI7-O3, AI7-O4, AI7-O17.
  - **Work:** Design a small, licensed/synthetic, versioned text and annotation collection with source identity, language scope, normalized field policy and offsets. Independently trace U1's decomposed/precomposed Unicode, build and compare at least two justified segmentation/tokenization policies, and preserve original span alignment after normalization. Encode S1 BIO2 tags and exact entity spans; introduce an invalid I-tag opening and an offset error. Specify an annotation guideline including unknown/disagreement handling and record a small independently reviewed annotation conflict. Demonstrate an unsupported byte stream or restricted source refusal rather than silent loss.
  - **Criteria:** NFC maps both U1 sources to `Café` while retaining distinct original code-point counts 5 and 4; original offsets are not fabricated from normalized positions. S1's token and entity spans match the published half-open coordinates, illegal BIO2 is rejected or explicitly repaired under an announced policy, and source provenance/licensing survive indexing preparation. Evaluation text does not participate in learning a vocabulary intended for training only. Claims about universal multilingual segmentation or private text authorization are withheld.
  - **Evidence:** Public text and annotation fixtures, source/revision/license and transformation contract, exact Unicode/offset/BIO derivations, executable or transparent normal/invalid traces, annotation disagreement record and limits.

- **AI7-AS2** (linguistic reasoning, count models and structured sequence labels)
  - **Outcomes:** AI7-O4, AI7-O5, AI7-O6, AI7-O7.
  - **Work:** Analyze a role-reversed/negated sentence pair and explain its contrast with unordered term counts; derive P1's multinomial text-classification posteriors and a correlated-token or zero-frequency counterexample. Specify T1's HMM initial/transition/emission probabilities, independently calculate all four paths, Viterbi best path and observation likelihood, and inspect a working small sequence decoder. Describe or implement a valid BIO-compatible label scheme and prove the chosen decoder does not emit an illegal sequence (or rejects it) under its stated constraints. Compare predicted exact-span entities or tags with a simple documented baseline.
  - **Criteria:** P1's `cat cat` posterior A=9/10 and `cat dog` A=B=1/2 follow its explicit model; no unsupported independence assertion is made about real text. T1 path probabilities 0.0192,0.3072,0.0112,0.0192, total 0.3568 and Viterbi N,V are independently correct and rows normalize. Reversed semantic roles are not incorrectly said to be encoded by a basic unigram bag, and label decoding obeys the declared type/boundary/unknown policies. A printed tag sequence without mathematical and linguistic evidence does not pass.
  - **Evidence:** Text-role and count analysis, tiny class/HMM derivations, finite source or complete dynamic-programming trace, legal/illegal label tests, negative model assumption case and bounded interpretation.

- **AI7-AS3** (language-specific neural representations and supervised tagging)
  - **Outcomes:** AI7-O3, AI7-O5, AI7-O8, AI7-O16.
  - **Work:** Build a CPU-scale text classifier or small sequence tagger based on AI5's embedding/recurrent foundation, defining vocabulary, OOV, padding, output labels, class or BIO head, source identity and loss mask. Compare it with a count/window/linear baseline on a valid documented train/development/final partition. Independently check one embedding/sequence output shape, one probability/loss value and an invalid pad or subword label alignment. Investigate a controlled word-order, negation or unfamiliar-form counterexample and report observed per-slice counts and scores.
  - **Criteria:** The chosen neural task is meaningfully language-specific, gradients/labels and padded positions follow the contract and the model cannot benefit from unauthorized final examples in vocabulary fitting or hyperparameter selection. A baseline and actual comparisons are present; no imposed accuracy or pretrained GPU model is required. The model's behavior on role/negation and unfamiliar language is observed, not inferred solely from architecture names. Invalid/OOV inputs have a declared disposition.
  - **Evidence:** Small reusable source and train-only vocabulary, independent shape/loss oracle, actual split/seed/selection and baseline logs, input/label masking tests, negative language case, honest error and limitations report.

- **AI7-AS4** (lexical index and exact ranked retrieval)
  - **Outcomes:** AI7-O9, AI7-O10, AI7-O11, AI7-O18.
  - **Work:** Build a locally inspectable inverted/positional index of L1 with stable document IDs, document length and df statistics. Independently calculate postings/phrase match, a fixed TF–IDF variant and every BM25 score using L1's k1/b/IDF formula. Execute Boolean, phrase, ranked and empty-result queries; demonstrate addition/deletion or analyzer revision and its impact on postings, corpus statistics, deterministic tie ordering and authorization. Compare brute-force reference matching with indexed retrieval for correctness and report actual CPU/storage costs on a bounded corpus.
  - **Criteria:** L1 red/cat postings and phrase support are correct; BM25 scores are d1=2ln(8/5), d2=d3=ln(8/5) with order d1,d2,d3 under published tie rules. A one-term absent query has no false positive, invalid deletion/update cannot return stale or unauthorized text, and matching terms/length/df statistics follow exactly the chosen analyzer. Numeric score is not misreported as relevance probability and no measured latency claim is generalized to production scale.
  - **Evidence:** Independent posting/position and BM25 arithmetic, index/source/configuration and mutation logs, Boolean/phrase/ranking/negative results, reproducible local commands and bounded resource report.

- **AI7-AS5** (query relevance and independent retrieval-measure audit)
  - **Outcomes:** AI7-O1, AI7-O12, AI7-O13, AI7-O19.
  - **Work:** Define query needs and complete small qrels with binary and graded judgments. Independently derive all E1 precision, recall, AP/MAP, reciprocal rank/MRR and nDCG computations; verify with a second isolated evaluation implementation or transparent hand process. Change one ranked position or disputed judgment and show exactly which metrics change, and specify what remains unknown with pooled/incomplete judgments or a query with no relevant material. Prevent learner tuning on the final qrel/test set and record judgment policy and corpus revision.
  - **Criteria:** E1 P@2=1/2, R@2=1/2, AP(q1)=5/6, AP(q2)=1/2, MAP=2/3, MRR=3/4, DCG@3=7/2 and nDCG≈0.964 under the published conventions. A metric with absent denominators is rejected or reported using a deliberately declared convention; incomplete qrels are not silently treated as exhaustive truth. The revision and query identities are consistent, and a claim that a run is 'relevant' or 'fair' requires more than a single numeric rank metric.
  - **Evidence:** Public query/doc relevance fixture and grading policy, stepwise independent metric derivations, raw ranking/qrel tables, alternate ranking/judgment negative checks, evaluation-split protocol and limitations.

- **AI7-AS6** (dense, hybrid and lightweight reranking investigation)
  - **Outcomes:** AI7-O8, AI7-O14, AI7-O15, AI7-O18.
  - **Work:** Independently derive D1 cosine and H1 reciprocal-rank fusion and reproduce the exact top-k orders. Build one small local embedding-based search using fixed legitimate or locally trained encoder weights, explicit vector/dimension/index version and query normalization; compare lexical-only, dense-only and RRF, with an optional small training-judgment-only reranker. Test a query paraphrase versus exact code/entity match, a zero vector and encoder/corpus revision mismatch. Report candidate-recall ceiling, measured query-time and memory costs, and actual per-query relevance scores on a fair static qrel protocol, noting if the hybrid is worse.
  - **Criteria:** D1 cosine values are 1,0,-1 with zero norm handled honestly; H1 scores d1=5/6,d3=3/4,d2=7/12 and order d1,d3,d2. Different score ranges are not added without an explicit justified transform, and a reranker does not claim to rescue absent candidates. Model/collection provenance and access scope are preserved, results/latencies are actual measured values, and no hidden transformer/pretrained paid embedding API is compulsory.
  - **Evidence:** Independent vector/fusion math, versioned embedding/index artifacts, actual lexical/dense/hybrid traces, normal/invalid/revision tests, fair qrel metrics, bounded CPU/storage comparison and candid failure assessment.

- **AI7-AS7** (language robustness, provenance, access and error forensics)
  - **Outcomes:** AI7-O2, AI7-O4, AI7-O12, AI7-O13, AI7-O16, AI7-O17, AI7-O18, AI7-O19.
  - **Work:** Use a controlled language/annotation/query slice covering at least a composed/decomposed spelling change, role or negation ambiguity and a genuinely different or code-switched morphology/token boundary where available in licensed/synthetic data. Record actual query counts, annotator disagreement, normalization and retrieval outcomes, investigating one apparent system improvement that disappears after qrel correction, document deletion or held-out evaluation. Demonstrate that a highly relevant but restricted N1-style document is removed from candidate results for an unauthorized requester, including snippets and cached postings/vector references. Inspect index revision, query length/CPU/resource behavior and the limits of small groups and incomplete qrels.
  - **Criteria:** U1 source-offset integrity remains demonstrable; altered labels and judgments have traceable before/after identities, not retroactive unexplained changes. A restricted document cannot appear in retrieved passages or derived ranking output for the unauthorized user. Subgroup/language results state actual support; sparse/unknown judgments are not silently called correct negatives and general multilingual or safety/fairness claims are withheld. Error explanations distinguish annotation, analyzer, model, index, ranking and permission causes with evidence.
  - **Evidence:** Versioned text/query/judgment and authorization fixtures, executed counterexample/denominator tables, access-filter and deletion proof, independent result traces, actual CPU/index observations and bounded interpretation.

- **AI7-AS8** (integrated language-retrieval system and unfamiliar technical defense)
  - **Outcomes:** AI7-O1, AI7-O3, AI7-O10, AI7-O12, AI7-O13, AI7-O14, AI7-O15, AI7-O16, AI7-O17, AI7-O18, AI7-O19, AI7-O20.
  - **Work:** Consolidate **one** inspectable local evidence/code collection from prior AI7-AS1–AS7 rather than rebuild seven projects or require a generated-answer pipeline. Choose a legitimate language corpus, a fixed query/judgment task and a lexical index plus a small semantic or hybrid comparison; provide baseline, exact independent postings/ranking/metric oracles, actual evaluation and resource measurements, documented language/label caveats, and meaningful invalid/permission cases. The reviewer supplies an **unfamiliar bounded** change to an analyzer/Unicode rule, term count, document deletion, authorization, qrel, query-language form, embedding version, fusion constant or cutoff. Predict the expected affected mathematical scores/rank/spans/permissions before running code; if evidence is incomplete, state exactly what cannot be inferred. Demonstrate the correct implementation adaptation or justified refusal, with independent regression verification and a written, recorded or live individual explanation.
  - **Criteria:** Clean-state CPU reproduction and source/rights compliance need no paid service or hidden dataset. The new case has a valid independently calculated reference, meaningful updated behavior or explicitly justified refusal; unaffected public cases remain correct. Actual learned model/relevance metrics are distinguished from toy numerical references. An apparently high rank score cannot override unauthorized content release, invalid annotation, incomplete relevance evidence or unsupported language transfer. Existing specialty outcomes still depend on substantive evidence from AI7-AS1–AS7 rather than being awarded solely because final code imports those components.
  - **Evidence:** Coherent versioned source tree or reviewable equivalent, explicit corpus/query/rights and model-index revisions, reproducible setup and commands, math/metric oracles, actual baseline/dense/hybrid results and resource records, adverse and reviewer-changed cases, access and uncertainty limits and individually attributable technical defense.

### Required outcome-to-assessment coverage

| Required outcome | Summative evidence |
| --- | --- |
| AI7-O1 | AI7-AS1, AI7-AS5, AI7-AS8 |
| AI7-O2 | AI7-AS1, AI7-AS7 |
| AI7-O3 | AI7-AS1, AI7-AS3, AI7-AS8 |
| AI7-O4 | AI7-AS1, AI7-AS2, AI7-AS7 |
| AI7-O5 | AI7-AS2, AI7-AS3 |
| AI7-O6 | AI7-AS2 |
| AI7-O7 | AI7-AS2 |
| AI7-O8 | AI7-AS3, AI7-AS6 |
| AI7-O9 | AI7-AS4 |
| AI7-O10 | AI7-AS4, AI7-AS8 |
| AI7-O11 | AI7-AS4 |
| AI7-O12 | AI7-AS5, AI7-AS7, AI7-AS8 |
| AI7-O13 | AI7-AS5, AI7-AS7, AI7-AS8 |
| AI7-O14 | AI7-AS6, AI7-AS8 |
| AI7-O15 | AI7-AS6, AI7-AS8 |
| AI7-O16 | AI7-AS3, AI7-AS7, AI7-AS8 |
| AI7-O17 | AI7-AS1, AI7-AS7, AI7-AS8 |
| AI7-O18 | AI7-AS4, AI7-AS6, AI7-AS7, AI7-AS8 |
| AI7-O19 | AI7-AS5, AI7-AS7, AI7-AS8 |
| AI7-O20 | AI7-AS8 |

**Completion decision.** All twenty outcomes require satisfactory independent evaluation under the actual AI7 course revision and eight substantive summative contracts. Valid prior evidence may serve multiple outcomes only when each required competency is genuinely inspected. Optional formative work, attendance, automated grading without reasoning, a high ranking metric on reused test judgments, an inaccessible library function or a copied pretrained embedding score do not suffice. This draft is **not** claimed to be learner-tested, accredited, a universal multilingual system or ready for consequential search deployment. Source/CI checks alone do not establish educational completion.

### Optional open academic and primary references

- [Stanford CS224N — Natural Language Processing with Deep Learning](https://web.stanford.edu/class/cs224n/) — language representation, sequence modeling, multilingual and evaluation context without requiring a university course login.
- [Stanford CS276 — Information Retrieval and Web Search](https://web.stanford.edu/class/cs276/) — indexing, relevance ranking, probabilistic IR and ranking evaluation coverage.
- [Introduction to Information Retrieval, Stanford/Cambridge online book](https://nlp.stanford.edu/IR-book/) — freely available foundations for indexing, BM25, relevance judgments and evaluation conventions.
- [NIST TREC relevance judgments and evaluation](https://trec.nist.gov/data/reljudge_eng.html) — query/document judgment semantics and collection compatibility; not a mandatory external benchmark.
- [Pyserini lexical search documentation](https://github.com/castorini/pyserini/blob/master/docs/usage-search.md) — reference index/search API and BM25 behavior, not a required external system.
- [NumPy documentation](https://numpy.org/doc/stable/) — optional independent array checks for compact vector and probability arithmetic.
- [Unicode normalization forms, Unicode Standard Annex #15](https://unicode.org/reports/tr15/) — normalization semantics, distinctions and the importance of preserving original text identity.

These references are optional. All mandatory educational capabilities, independently checkable numerical cases, failure conditions and assessment criteria appear in this public course file; no paid or proprietary source is necessary.
