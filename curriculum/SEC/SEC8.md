# SEC8 — AI Security & Authorized Red Teaming

**Program:** SEC — Security Engineering
**Type:** `course`
**Prerequisites:** [SEC7](SEC7.md)
**Duration:** 12–16 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** approximately 10–14 focused hours/week (provisional; 120–224 hours)

> [Security Engineering](README.md) · [Design guide](../DESIGN-GUIDE.md) · [Course format](../../spec/course-format.md) · [Evidence rules](../../spec/evidence-rules.md)

## Overview

**AI security is the independent verification that probabilistic or model-influenced content cannot silently acquire the authority of the user, the application or its external tools.** SEC8 develops specialized adversarial assessment of retrieval-augmented and tool-using AI applications under explicit authorization. Learners reconstruct data and execution boundaries, formulate benign but discriminating prompt-injection hypotheses, test authorized and prohibited access to source material, enforce action authorization at a trusted dispatcher, examine output and persistent-memory contamination, measure resource and detection limits, and verify layered repairs against held-out variants. An impressive refusal, a tool call described in generated text, a prompt-filter pass or a high attack-success score without an independently observed security effect is not sufficient evidence.

**Context and relevance.** A model-powered application reads instructions, retrieved passages, tool results, metadata, memory and sometimes another model's response in one changing context. A malicious-looking sentence may be harmless source content, an instruction attempt, a legitimate quotation or an ambiguous user request; its consequences depend on the model and the *actual application controls*. Retrieval may return another tenant's material even when the model correctly paraphrases it. An assistant may propose a prohibited operation, but the real security boundary fails only if trusted code commits the operation or leaks protected data. Replays, delayed actions, partial failures and agent delegation can preserve or amplify that error. Model-generated answers are also untrusted when rendered, parsed, stored or used as action arguments. Security must be tested at the retrieval, authority, output and state boundaries rather than claimed from system-prompt wording.

**Prerequisite and course ownership.** [SEC7](SEC7.md) directly supplies evidence provenance, independent detection/negative cases, authorized incident investigation, causal reasoning and defensible remediation. Its transitive closure includes [SEC6](SEC6.md), [SEC4](SEC4.md), [SEC2](SEC2.md), [SEC1](SEC1.md) and the relevant SEF/APP engineering preparation. SEC2 already owns traditional server-side object/action/tenant authorization, interpreter/output safety and API resource limits; SEC8 specifically tests **whether retrieved data, model output, tool metadata, context memory or agent steps can subvert these existing enforcement points**. SEC6 owns cloud workload IAM and supply-chain provenance; SEC7 owns general incident response. This course neither teaches deep-learning theory, trains an LLM, authors a general retrieval/agent platform nor repeats a comprehensive responsible-AI governance curriculum. Basic retrieval/chunk/metadata, model request/response, typed-tool and dispatcher concepts are introduced from **supplied, inspectable fixtures** so no separate AI program, model-building specialization, GPU or advanced generative course is an unstated admission requirement.

**Reference fixture and execution fidelity.** Use one small **local owned AI-assisted document-and-tool application** that has at least two synthetic users or tenants, original documents with chunk/source/permission metadata, a retriever and cache or memory, a model-influenced answer or tool proposal, a trusted tool dispatcher and an independently inspectable state store. The fixture may be prebuilt, versioned and deliberately defective; learners must meaningfully exercise and repair its **real, locally executable** retrieval permissions, dispatcher, storage and output gates. At least one authorized prompt-injection case must involve an **actual model-mediated response or tool proposal** from a freely usable, bounded CPU-local model or an authentic supplied trace from a named model/version and fixed input. When relying on a supplied trace, distinguish the *model observation* from the **locally executed policy enforcement and state checks**. A hard-coded fake text generator can test dispatcher mechanics but cannot establish that a real LLM obeyed an injected instruction. A tiny open local model may be inaccurate or stochastic; record the actual model/backend, prompt and version and never substitute a guessed outcome. Every critical authorization, data-isolation and side-effect regression must be testable locally without paid inference, large weights, network access or unavailable model capabilities. Free Python/TypeScript, local fixtures and existing SEF/APP skills are sufficient; no model training, tokenizer derivation, paid API, real external tools or production platform is required.

**Safe authorized red-team scope.** Limit attacks to synthetic documents, disposable tenant stores, benign marker text and simulated tool effects inside one owned local environment. A forged instruction may request a harmless forbidden test action such as writing an unauthorized synthetic record or returning a canary; do not require stolen credentials, real exfiltration destinations, self-propagating prompts, destructive actions, uncontrolled web browsing or public model endpoints. Requests to send, pay, publish, delete or execute OS commands are assessed only through **nonexecuting synthetic tools** unless the action is a bounded reversible local mutation with explicit permission. Record scope, owners, authorized attack sources, exclusions, stop and reset rules, and limits on time, tokens, tool calls and rate. Treat any retrieved document or tool result as untrusted even when attributed to a trusted platform; source origin is not permission to obey instructions.

**Security-specific evidence and limits.** For each case distinguish an **attack attempt** (controlled input), a **model response or proposal** (observed/supplied trace), a **dispatcher or retriever decision**, an **actual protected-state transition**, and a **confidentiality or safety outcome**. Do not report "exfiltration" from the model merely printing a made-up secret or "tool execution" from a transcript that only mentions a tool. Security success requires authoritative state or response evidence, plus independent expected permissions. Statistical estimates from finite prompts or held-out fixtures do not establish general immunity. A defense that simply refuses every request fails legitimate-use requirements. Logging must redact canaries where appropriate and must not introduce new data leaks. The provisional 12–16 weeks at 10–14 focused hours/week follows the security model, instrumented tests, real/furnished model observations, retrieval and action repairs, measured regressions and a new-case defense. Status remains `draft`.

## Learning outcomes

- **SEC8-O1:** Bound and justify an authorized AI security assessment, mapping actors, assets, model/provider, prompt roles, retrieval/index, memory, tool metadata, trusted dispatcher, output consumers and actual authority, with honest distinctions between user intent and lower-trust content.
- **SEC8-O2:** Construct and execute benign, reproducible direct and indirect prompt-injection tests through appropriate entry surfaces, distinguishing source instructions from application policy, observed model influence from committed effects, and negative evidence from an impossible proof of immunity.
- **SEC8-O3:** Inspect and challenge document/chunk/source authorization at ingestion, indexing, retrieval, citation, cache and removal boundaries, including tenant and permission changes, and verify that protected content is neither retrieved nor disclosed through any allowed response path.
- **SEC8-O4:** Assess corpus/retrieval poisoning, misleading metadata and tool-result injection as distinct trust problems; trace source integrity and instruction/data separation and independently verify fixes without treating high search rank or a cited document as trusted authority.
- **SEC8-O5:** Evaluate model-proposed tool names, arguments, scopes and delegation against trusted server-side resource/action checks, rejecting confused-deputy use, unauthorized mutation and fabricated success even when model output is syntactically valid.
- **SEC8-O6:** Test explicit human approval and high-impact side-effect gates for actor, exact action/parameters, resource, expiration, changed state, retries and revocation, with independently verified committed state rather than an agent's narrated success.
- **SEC8-O7:** Investigate untrusted generated outputs as potential HTML, URL, query, file, template, command, structured-data or instruction inputs and verify sink-specific validation and user-safe rendering without reimplementing the entire SEC2 vulnerability catalog.
- **SEC8-O8:** Analyze and test multi-turn state, retrieval caches, agent memory and delegated outputs for cross-user carryover, persistence of hostile instructions, stale grants, source deletion/withdrawal and clearly defined retention or reset behavior.
- **SEC8-O9:** Derive and exercise safe resource and operation budgets for tokens/contexts, retrieval fanout, tool calls, recursion, retry, concurrency, rate and synthetic cost, demonstrating bounded denial and useful success without performing a real denial-of-service attack.
- **SEC8-O10:** Design and execute held-out, benign/attack-like and changed-context security evaluations using independent allow/deny/invalid/failure oracles, reporting attempted-versus-executed violations, legitimate-task success, false refusal, coverage, variation and uncertainty.
- **SEC8-O11:** Select and verify layered mitigations and proportionate detection/escalation for prompt, retrieval, dispatcher, output and memory boundaries, with redacted forensic traces, causal before/after regressions and explicit residual threat limits.
- **SEC8-O12:** Deliver a reproducible authorized AI red-team assessment and independently diagnose and defend an unfamiliar retrieval, tool, prompt, approval, model, memory or resource change with clear evidence, remediations and honest security decisions.

## Modules

### Module 1 — AI Security Scope, Authority and Observability

#### Outcomes

- SEC8-O1
- SEC8-O2
- SEC8-O10

#### Lessons

1. **What is and is not an AI trust boundary** — Reconstruct a small document-answering and tool-using service from its original input, document ingestion, retrieval and context packing through model output, trusted dispatch and changed state. Identify who authored each piece of text, the authorized actor and where the actual privilege check occurs. Show why text that claims to be a system message is not thereby privileged.
2. **Authorized scope, harmless effects and reset rules** — Define owners, permitted synthetic actors, prompt/doc/tool entry points, expected protected records, nonexecuting side-effect fixtures, time/budget limits and stop/recovery decisions. Distinguish a public chat interface from permission to security-test arbitrary users, hosted services or provider infrastructure.
3. **Observable attempts, proposals and effects** — Produce a versioned case record linking prompt revision, retrieved source/chunk, model observation, proposed tool call, dispatcher response and authoritative state. Predeclare what counts as success or violation; show that a model saying "I deleted it" is not evidence a deletion took place.
4. **Human request, model output and evaluation oracle** — Contrast a legitimate request for a summary, a direct hostile-looking instruction and an instruction embedded in a retrieved page. Construct independent outcomes for each, distinguishing user-authorized requests from a third party's content and from an apparently benign quotation.
5. **A model trace is not a model security guarantee** — Run a bounded actual CPU-model interaction or inspect an authentic versioned model/tool trace for one prompt-injection attempt, then independently inspect local dispatcher/retriever controls. Explain variation, inaccessible model conditions and what a deterministic mock can and cannot prove.

*Optional formative feedback:* Given a transcript where an assistant reports a successful transfer but the trusted tool rejects the request, classify the attempt, model behavior and actual security outcome separately.

### Module 2 — Prompt, Retrieval and Corpus Trust Boundaries

#### Outcomes

- SEC8-O2
- SEC8-O3
- SEC8-O4
- SEC8-O10
- SEC8-O11

#### Lessons

1. **Direct and indirect instruction attempts** — Contrast a direct user instruction, lower-trust document text, a citation/metadata field and a tool result that asks the model to change task or disclose data. Predict the precise source/authority confusion, use harmless markers and measure actual model behavior without claiming every instruction-like sentence is malicious.
2. **Where retrieval authorization must execute** — Inspect original document owners, per-chunk ACLs, index representations, ranker input and result filtering. Demonstrate why hiding a passage in the final answer cannot repair an unauthorized retrieval or a privileged chunk already placed in model context. Test two synthetic tenants and an allowed shared document.
3. **Cache, citation and deletion propagation** — Trigger document withdrawal, role change and source correction on a controlled local corpus. Inspect cached passage/answer, citation source IDs and stale context; verify revoked material cannot reappear through another query, source version, summarization or retained cache after the specified invalidation contract.
4. **Corpus and metadata poisoning** — Use a synthetic, explicitly attacker-editable document and metadata entry with a harmless instruction marker or misleading source label. Trace the observed retrieval and generation response and identify the integrity boundary. Restore the trusted source/provenance or enforce untrusted-data handling; verify both trusted evidence and legitimate document answering still work.
5. **Testing retrieval and generated disclosure separately** — Run independent allow/deny oracles for actual retriever result IDs, model context, answer content, citations and output/cache storage. Explain why a fabricated model answer containing a fake secret is not an observed unauthorized read, and why a denied final answer does not excuse unauthorized internal retrieval.
6. **Instruction resistance versus guaranteed authorization** — Compare prompt delimiters, source labeling, context limits, policy reminders, retrieval ACLs and dispatcher controls. Test a benign variant that a blanket refusal would wrongly reject. Treat model instruction-following defenses as fallible; rely on trusted code for permissions and data-state invariants.

*Optional investigation:* Compare two repaired pipelines: one applies tenant filters before retrieval and verifies the resulting IDs, while the other cleans only final text; identify which protected context remains exposed.

### Module 3 — Tool Agency, Delegation and Side-Effect Authorization

#### Outcomes

- SEC8-O1
- SEC8-O2
- SEC8-O5
- SEC8-O6
- SEC8-O10

#### Lessons

1. **Tool discovery is not tool authority** — Inspect a typed tool schema, discoverable tool description and the actual server-side dispatcher policy. Trace a model proposal with a correct tool name and arguments from an unauthorized user; demonstrate real denial and unchanged state despite the apparent validity of the JSON.
2. **Resource/action/tenant checks after model selection** — Derive a matrix of actor, requested action, object owner, delegated identity and current permission for local read/update operations. Test model-proposed substitution of an object ID, alternate tool alias, changed role and stale authorization at dispatch; the model cannot issue itself permission.
3. **Untrusted tool results and confused deputies** — Place a harmless instruction request inside a mock tool result or untrusted tool metadata, then inspect the next proposed operation and dispatcher decision. Distinguish authorized tool data returned to the user from an unauthorized second operation caused by laundering source text into authority.
4. **Approval with exact intent binding** — Implement or inspect a synthetic high-impact state change requiring a trusted, time-limited approval bound to the actor, tool, arguments, resource and expected state. Test withheld, expired, revoked, changed-parameter and replayed approval cases; a natural-language request for confirmation is not the same as verified preflight authorization.
5. **Retries, timeouts and committed effects** — Test a local tool whose reply is delayed after committing a safe state change, or whose result cannot be observed immediately. Explain why replay may duplicate effects and why a reported success cannot substitute for state reconciliation. Evaluate stable operation IDs/idempotency and bounded retry decisions without assuming distributed rollback.
6. **Multi-agent delegation and reduced scopes** — Evaluate one supplied delegated-tool trace with a caller, subagent/service, receiving tool and scoped capability. Verify that a second agent or tool server independently enforces the user's permissions and does not treat a signed/trusted sender or a tool description as blanket permission. Actual multiagent infrastructure is optional.

*Optional formative feedback:* For three proposals that describe the same administrative mutation, identify the one bound to an actual valid approval and verify no committed state change occurred for the others.

### Module 4 — Generated Outputs, Memory and Resource Abuse

#### Outcomes

- SEC8-O4
- SEC8-O7
- SEC8-O8
- SEC8-O9
- SEC8-O11

#### Lessons

1. **Model output is still untrusted data** — Trace a generated URL, Markdown/HTML fragment, structured tool arguments and summary into their real consumers. Test one relevant safe rendering or parser boundary and a contrasting unsafe interpretation with inert inputs. Distinguish ordinary hallucination, unsupported citations and a concrete client/server side-effect or unsafe output sink.
2. **Structured output and validation limits** — Examine JSON/schema validation, wrong types, unsafe URLs, unbounded numeric fields and apparently valid but unauthorized resource IDs. Verify independent allow/deny logic after parsing; correct JSON structure alone is not proof of authorization or intent.
3. **Memory, history and cross-session authority** — Inspect a local multi-turn assistant memory/cache contract and two users with different permissions. Insert a harmless hostile-looking document or changed rule, perform an allowed later request and check what is carried forward, summarized or shown to a different user. Test clearing, retention and permission revocation without assuming session reset erases every derived artifact.
4. **Budget, fanout and loop safety** — Set explicit caps on context size, number of retrieval results, tool calls, recursion depth, retries, concurrency and synthetic token or action cost. Test one loop/retry/fanout fixture with small resource budgets; show the request stops with a clear non-leaking error while normal bounded use still completes.
5. **Monitoring high-risk decisions without leaking data** — Record redacted tool intent, actor, authorization decision, approval identity, data-source IDs and committed-state change under a bounded retention plan. Distinguish attempts, prevented effects, approved operations and unknowns; map a relevant detection/triage trigger without re-teaching the entire SEC7 incident course.

*Optional investigation:* Evaluate a memory record tagged to one user that reappears in a second user's generated answer; identify whether retrieval ACL, persistence, model context or output cache is responsible.

### Module 5 — Adversarial Evaluation, Mitigation and Independent Defense

#### Outcomes

- SEC8-O1
- SEC8-O2
- SEC8-O3
- SEC8-O5
- SEC8-O6
- SEC8-O8
- SEC8-O9
- SEC8-O10
- SEC8-O11
- SEC8-O12

#### Lessons

1. **Threat-to-test matrix and fixed evaluation decisions** — Map authorized, forbidden and ambiguous actions to actors and trusted enforcement points; distinguish source contamination, unwanted model behavior, denied attempts and actual confidentiality/integrity violations. Predeclare independent case labels, expected outputs/state, failure categories and a finite resource budget before generating variants.
2. **Changed-source, changed-tool and benign lookalikes** — Test multiple harmless injection placements across retrieved passages and metadata, model/tool replies, tool approvals, memory and unfamiliar but authorized user phrasing. Use a held-out set that includes legitimate queries which must still succeed and missing-data contexts that should abstain rather than disclose.
3. **Coverage, false refusal and measured security effects** — Measure attempted injections, observed model-proposal diversions, denied unauthorized operations, executed violations, false refusals, successful legitimate uses and budget exhaustion with explicit denominators. Use repeated trials for stochastic behavior where feasible; report uncertainty and model/config changes rather than cherry-pick one dramatic dialogue.
4. **Causal layered repair** — Trace one demonstrated flaw to its earliest controllable boundary: source/index policy, trusted authorization, approval binding, output validation, persistent memory, or resource limiter. Repair the corresponding executable control; test the original case plus independent variants and preserve ordinary authorized behavior. A prompt change may reduce symptoms but cannot replace a missing server-side check.
5. **Unfamiliar attack surface and defender review** — Receive a previously unseen bounded variation such as a revoked document, altered tool schema, changed approval, poisoned citation, stale memory, retry timeout, unexpected model proposal or newly allowed legitimate operation. Predict an actual permitted and prohibited outcome before decisive inspection, choose a discriminating test, implement/justify a fix, and defend remaining uncertainty under individual technical questioning.

*Optional formative feedback:* Reject a release argument that reports "zero successful injections" when all unauthorized tool calls were blocked but 40% of legitimate requests were refused and several cache paths were never tested.

## Completion requirements

**Four required summative evaluations** collectively establish all SEC8 outcomes. The learner may reuse the same authorized local application, synthetic corpus and actor/tool fixtures; each summative targets a distinct security property and evidence contract, not four unrelated AI applications. Actual local authorization, retrieval, dispatch and state tests are mandatory wherever that boundary is asserted. At least one prompt-injection claim must include a real model-mediated observation or a genuine, version-labeled supplied trace; model-induced behavior and executable security control outcomes must be separately reported. Optional lesson investigations and informal checkpoints are not completion conditions. No third-party target, harmful payload, real secret, live service abuse or custom model training is required.

- **SEC8-AS1** — Retrieval Boundary and Indirect Prompt-Injection Review
  - **Outcomes:** SEC8-O1, SEC8-O2, SEC8-O3, SEC8-O4, SEC8-O8, SEC8-O10, SEC8-O11.
  - **Work:** Audit a local synthetic two-user/two-tenant question-answering fixture with document source IDs, chunk permissions, versioned metadata, retrieval and an actual response/context or authentic labeled model trace. Predeclare permitted and prohibited source access for shared, private, revoked and corrected documents. Insert a harmless lower-trust instruction into an approved synthetic document or citation field and record the retrieved item, model response, intended hijack, actual exposure and authorized result separately. Identify and repair a source/ACL/cache or instruction/data trust failure using real executable access gates; test valid answers plus forbidden retrieval, metadata/citation leakage, deletion/revocation and unchanged/held-out indirect injection placements. A fictional "secret" produced without a real protected read is not counted as exfiltration.
  - **Criteria:** Exact source ownership and document/chunk/index/cache authority are documented; the repair enforces the right actor's scope before protected context is released, and denied inputs preserve confidentiality across response, citation and cache. The submitted instruction-bearing content is demonstrably lower trust; the reported model influence has actual model or genuine supplied provenance and is not misidentified as an executed tool action. Legitimate shared/source-grounded queries remain usable, and changed-document/role tests would detect stale or overbroad filtering. Attack attempts, observed model behavior and real security outcomes remain distinct, with explicit inaccessible paths and limits.
  - **Evidence:** Authorized fixture manifest, source/chunk/tenant/permission matrix, input and source revisions, annotated model trace with model/version provenance or actual local observation, real retriever/cache/response checks, independent expected allow/deny table, before/after code/config, held-out regression outcomes and bounded uncertainty.

- **SEC8-AS2** — Tool Agency, Approval and Actual State Enforcement
  - **Outcomes:** SEC8-O1, SEC8-O2, SEC8-O5, SEC8-O6, SEC8-O8, SEC8-O10, SEC8-O11.
  - **Work:** Assess an actual locally executable typed-tool dispatcher and synthetic mutable state store. Supply model proposals from a real recorded run or authentic fixed trace for benign and injected instructions; independently test dispatcher permission to read, update and attempt one synthetic high-impact action. Verify server-side user/resource/tenant authorization, trusted approval bound to exact parameters and current state, and wrong actor, revoked role, replayed/expired consent, changed argument, timeout-after-commit, stale memory and untrusted tool-result scenarios. Repair a demonstrated bypass; record actual datastore effects rather than assistant narration and rerun legitimate and prohibited paths.
  - **Criteria:** A correctly formatted tool call has no authority absent a fresh dispatcher check; no model/tool-description text can mint an approval or increase scope. Unauthorized operations and changed/replayed approvals leave protected state unchanged; valid user-approved operations complete and commit at most the allowed effect. Partial/ambiguous results are reconciled against actual state without duplicate mutation. A synthetic delegated trace is evaluated at the receiving boundary; normal-use, altered-input and failure cases independently discriminate meaningful control behavior. Any claimed model coercion is separated from blocked execution.
  - **Evidence:** Versioned tool/state fixture, actor-action-resource matrix, model/tool-output provenance, deterministic authorization/approval oracle, actual dispatch attempts and before/after state or commit IDs, revoked/replayed/timeout negative results, minimal fix and independent regression suite with explicit tool limitations.

- **SEC8-AS3** — Generated-Output, Persistent Context and Resource Security
  - **Outcomes:** SEC8-O1, SEC8-O4, SEC8-O7, SEC8-O8, SEC8-O9, SEC8-O10, SEC8-O11.
  - **Work:** Analyze one locally executable generated-output sink and one multi-turn memory/cache/derived-artifact path that can retain misleading instructions or cross-user data. Test harmless unsafe URL/HTML/structured-input variants using actual consumers; independently check tenant separation, denied persistence after revocation or session reset, and whether a previously injected memory item can cause a later forbidden proposal. Specify bounded token, retrieval, tool-call, retry/fanout and synthetic cost budgets; verify at least one exhaustion/loop condition stops within an explicit threshold while legitimate work still completes. Patch a genuine output/persistence/limit weakness and evaluate redacted attempted-versus-observed effects against held-out cases without real exfiltration or sustained load.
  - **Criteria:** Output validation is located at the real parser/renderer/action sink and does not rely on a generic model promise to emit valid JSON. Data isolation and stale-memory handling are demonstrated through actual source/cache/state behavior; a mere screenshot or text-only denial does not prove another user's stored data is inaccessible. Tests show bounded work, expected failure state and normal legitimate completion. The repair closes the evidenced causal path, survives different benign-looking inputs and does not hide failures through blanket refusal. Unknown model behavior or unexercised external sinks are explicitly qualified.
  - **Evidence:** Source/consumer and memory-state map, owned benign malicious-like inputs, executable sink and local persistent-state observations, resource-budget counters and threshold checks, expected allowed/denied/error cases, redacted versioned logs, patch/regressions and scoped residual-risk statement.

- **SEC8-AS4** — Unfamiliar Authorized AI Red-Team Assessment and Defense
  - **Outcomes:** SEC8-O1, SEC8-O2, SEC8-O3, SEC8-O5, SEC8-O6, SEC8-O8, SEC8-O9, SEC8-O10, SEC8-O11, SEC8-O12.
  - **Work:** Receive a previously unseen but authorized change in source revision or permissions, model/prompt version, tool metadata or argument schema, user approval, memory persistence, cost budget or delegated authority. State a specific forbidden and allowed effect, a plausible exploit hypothesis and a competing benign explanation **before** the decisive test. Execute controlled local retrieval/dispatcher/state checks and analyze actual or authentic labeled model proposals; implement an evidence-backed correction or justified safe refusal. Run an independently labeled held-out suite including benign lookalikes, varied attack placements, permission changes and failure-state effects. Report attempted-versus-executed violations, legitimate-task success, false refusals and untested cases with denominators and uncertainty. Present an operator/developer risk decision with independently reviewable individual technical defense.
  - **Criteria:** The investigation identifies the real origin/privilege boundary and preconditions rather than rewarding a rhetorical jailbreak; logs and actual protected state distinguish attempted prompt diversion from executed unauthorized behavior. An effective fix targets retrieval policy, dispatcher authority, exact approval binding, output sink or persistent-state ownership as appropriate, and a held-out case exposes a safely reintroduced defect. Allowed actions continue to work, resource bounds are honored and no unreviewed external side effects are required. The learner changes or rejects an earlier hypothesis when counterevidence appears, maps relevant detection/escalation to supported observability and qualifies residual stochastic, coverage and model-transfer limits.
  - **Evidence:** Fresh authorized brief and system versions, pre-observation actor/resource and allowed/forbidden matrix, scoped attack corpus and prompt/source/tool fixture provenance, actual/supplied model observations, executed security control and authoritative state traces, independent held-out scoring table and safety gates, repaired artifact, concise prioritized developer/owner report and reviewable written/recorded/live defense.

### Evaluation evidence and readiness

Each assessment identifies its `SEC8-AS#` and covered `SEC8-O#` identifiers, course revision, actual local source/model/tool versions, authorization scope, selected original and altered inputs, independent expected effects, observed model/proposals, actual enforcement/state and reviewer decision. Required tests must reproduce from a clean accessible local fixture. For an authentic supplied model run, identify model and runtime, input/context, sampling/seed information where available and the provenance of the trace; do not present a hard-coded mock as evidence of a genuine model response. Store only harmless synthetic data, redact markers that would confuse cross-user privacy claims, and distinguish a protected record *actually retrieved* from one merely guessed or hallucinated by the model.

A successful security gate is not evidence that the model always obeys its instructions; a failed prompt-attack attempt does not prove the system has no other exposed path. The course remains `draft` pending the qualified [course readiness criteria](../../spec/status-labels.md). Completion does not constitute legal penetration-test authorization, formal AI safety certification, general model robustness, a guarantee against prompt injection, live agent exploitation competence or completion of the AI Engineering program.

### Optional disciplinary references

- [OWASP Top 10 for LLM Applications 2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/) — current categories and risks, not an assessment checklist or security certification.
- [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) — delegated agency, tool and context boundaries.
- [OWASP RAG Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/RAG_Security_Cheat_Sheet.html) — ingestion, chunk/metadata authorization, cache/deletion and source integrity.
- [OWASP AI Agent Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html) — authorization, approval, memory and side-effect controls.
- [NIST AI 100-2 E2025](https://csrc.nist.gov/pubs/ai/100/2/e2025/final) — adversarial machine learning taxonomy and bounded mitigation claims.
- [NIST AI RMF Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) — risk framing and evidence limits, not a mandatory separate governance curriculum.
- [MITRE ATLAS](https://atlas.mitre.org/) — AI adversary techniques and defender-observable hypotheses, not permission to attack third-party models.
- [Model Context Protocol specification, authorization security considerations (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) — when tool transports use MCP, client/host/server identity and separate authorization still apply.

The public reference materials are supporting technical guidance; the required assessments and pass/fail evidence are specified here without requiring any paid service or AI-program prerequisite.
