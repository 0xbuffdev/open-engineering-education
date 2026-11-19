# SEC6 — Cloud, Containers & Identity Security

**Program:** SEC — Security Engineering
**Type:** `course`
**Prerequisites:** [SEC2](SEC2.md), [SEC4](SEC4.md), [APP7](../APP/APP7.md)
**Duration:** 14–18 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** approximately 10–14 focused hours/week (provisional; 140–252 hours)

> [Security Engineering](README.md) · [Design guide](../DESIGN-GUIDE.md) · [Course format](../../spec/course-format.md) · [Evidence rules](../../spec/evidence-rules.md)

## Overview

**Cloud and container security is the verification of who can execute, change, read, build and deploy a workload—and under which explicitly enforced conditions.** SEC6 prepares a learner to review a real, bounded containerized application and its delivery path as an adversarial security engineer. The work establishes a threat and privilege map, corrects container image/runtime exposure, derives cloud-style identity and resource policies, analyzes workload/CI federation, tests untrusted build and secret boundaries, verifies artifact identity and provenance, and defends repairs when an unfamiliar dependency or authority assumption changes. A green pipeline, valid container image, low scanner score or permissive role that "makes the deployment work" does not establish security.

**Context and scope.** Cloud services and local containers combine application privileges, host isolation mechanisms, data identities, workload credentials, CI workers, artifact registries, environment policies and external dependencies. A service may have correct HTTP authorization yet be able to read a mounted host secret; a token may be restricted to one branch yet be valid for an unexpected environment; a signed image may come from the wrong builder; or a correctly formed cloud policy may grant broader access through another principal/resource policy. These failures cross **different enforcement points**. Security review must distinguish observed local process/container controls, a provider's stated IAM policy semantics, synthetic decision traces and an actual trusted artifact verification.

**Preparation and course ownership.** [SEC2](SEC2.md) supplies adversarial application security, object/actor authority, synthetic fixtures and regression evidence. [SEC4](SEC4.md) supplies real network/host exposure, proxy/transport trust, least-privilege process analysis and tested configuration changes; SEC6 transfers this reasoning to container runtimes, identities and cloud-control-plane authority rather than reteaching firewalls or TLS. [APP7](../APP/APP7.md) already assesses a running deployment with immutable artifacts, container/process configuration, local HTTPS, protected environments and release/rollback, and includes [APP6](../APP/APP6.md) preparation in CI quality gates, dependency inventory, SBOMs, hashes and basic provenance. **SEC6's additional claim is adversarial assurance**, particularly image-to-runtime and host privilege bypasses, cross-resource authorization, federated workload identity, untrusted pipeline escalation, provenance-policy verification and security-specific negative tests. Learners reuse or receive an appropriate pre-existing deployment instead of rebuilding APP7's full-stack release, database migration and recovery project. [SEC5](SEC5.md) owns cryptographic protocols and primitives; this course uses maintained verification tools and explains identities/trust without requiring custom signature or token cryptography. [SEC7](SEC7.md) later owns detection engineering, incident response and forensics; here logs serve bounded control verification, not a second threat-hunting course.

**Reference environment and equitable access.** Use one small previously functioning synthetic service and an owned, disposable local Linux container environment, for example pre-provisioned rootless Podman or another free OCI-compatible runtime, with a version-pinned image, local test files, dedicated test accounts and bounded network access. The necessary runtime may be provided already configured; **rootless operation still depends on host user namespaces and policy**, and a learner must not be asked to reconfigure an unmanaged host. At least one required assessment must exercise **real** container startup, runtime identity and mount/file permission behavior under an available free isolated environment. A small prebuilt container project is sufficient; a complete APP7 redeployment is not required. When a particular namespace, seccomp, capability, cgroup, registry, cluster or host-kernel behavior cannot be safely exercised, assess it through authentic target/engine-version-labeled runtime, policy and audit traces and clearly identify what was not locally enforced. A theoretical policy simulator cannot be claimed as proof of live container isolation or provider IAM enforcement.

**Cloud, identity and supply-chain accessibility.** No public cloud account, billable subscription, production registry, Kubernetes cluster, external identity federation or live cloud credential is required. Provider policy exercises use **named, documented semantics** and authentic supplied service/IAM policy decisions or a suitable official offline/test simulator when available; a learner may build a deliberately bounded local authorization model but must not represent it as complete AWS, Azure or GCP policy evaluation. The sample CI pipeline can be exercised with a local runner or isolated subprocesses and supplied hosted-runner event/identity traces. For cryptographic provenance, use a free maintained verifier and provided authentic signed bundle with pinned expected issuer, signing identity, artifact digest and trusted material; offline verification is acceptable when supported. If verification tooling is unavailable locally, analyze actual verifier output from a disclosed target, report it as **supplied evidence**, and still independently verify the local artifact's digest and policy mapping. No private runner secret or live OIDC token is needed.

**Safety and evidence fidelity.** All negative experiments occur in the learner-owned disposable environment using synthetic identities, keys and sensitive-looking data. Never target a real cloud tenant, perform service-account enumeration on third-party resources, run untrusted code with privileged secrets, place a credential in a public repository, disable isolation on a shared host, or submit raw private tokens in reports. A redacted simulated leak trace is permissible, not a real exfiltration. Record who controls the source, build process, runtime, artifacts, federated identity and provider policy. Every control claim identifies its **actual enforcement point**, before/after expected result, direct and alternate path, meaningful negative case, environment and unresolved uncertainty. A denied application route is not a cloud IAM denial; a container's root UID is not always host root, and rootless operation alone is not a sandbox security proof.

**Planning and assessment.** A single continuously revised service/release fixture may supply the technical artifacts for four differentiated summative evaluations. Modules introduce genuine new reasoning stages, not mandatory micro-labs or a repeated final project. The 14–18-week estimate at 10–14 focused hours/week covers runtime inspection and hardening, cloud-style IAM decisions, workload/CI trust policies, actual and supplied negative traces, signed artifact verification, controlled changes, and an unfamiliar defense. The estimate is provisional, not learner-tested. Completion is determined by the published evidence criteria, and the course remains `draft`.

## Learning outcomes

- **SEC6-O1:** Scope and reconstruct a container/cloud delivery system's assets, owners, deployment and build identities, environments, resource policies, trust boundaries and allowed/denied operations, distinguishing observed enforcement, specified policy and untested assumptions.
- **SEC6-O2:** Inspect container image construction, source/base/dependency inputs, configuration and artifact identity; identify and correct unnecessary components, embedded test secrets, unsafe defaults or mutable references while preserving reproducible legitimate behavior.
- **SEC6-O3:** Analyze and verify container runtime privilege and host-facing boundaries including user identity, namespaces, Linux capabilities, seccomp, mounts, writable paths, socket exposure and resource limits, with target-specific negative evidence and explicit kernel/engine constraints.
- **SEC6-O4:** Evaluate workload credential, token and secret exposure at environment, file, volume, service-account and metadata boundaries; implement a bounded least-disclosure, rotation/revocation and failure policy without treating any injection method as intrinsically secret-safe.
- **SEC6-O5:** Derive and test least-privilege cloud/resource authorization for named principal, action, resource and condition tuples, correctly accounting for default/explicit deny and the relevant identity, resource, session, boundary and organization policies under a declared provider's actual semantics.
- **SEC6-O6:** Analyze federated workforce/workload or CI identity trust, including issuer, audience, subject, repository/ref/environment restrictions, token lifetime and role-assumption conditions; reject an unintended origin or privilege escalation without relying on live cloud credentials.
- **SEC6-O7:** Distinguish application tenant checks from cloud-resource, service identity and environment/organization boundaries; identify cross-tenant resource grants, publicly readable artifacts, wrong-account/region or metadata access assumptions and independently evaluate their effective access paths.
- **SEC6-O8:** Assess CI/CD as a privileged execution system with untrusted source changes, third-party actions, runner persistence, secret exposure, approvals and token scopes; enforce and verify a meaningful untrusted-versus-privileged execution separation rather than a checklist-only pipeline.
- **SEC6-O9:** Trace source revision, build recipe/builder, generated artifact digest, attestations and promotion trust; verify available cryptographic provenance against an independently specified **expected** producer/identity and artifact digest, distinguishing source and build trust from a bare checksum or valid-but-untrusted signature.
- **SEC6-O10:** Evaluate dependency and container artifact inventories/SBOMs, base-image and action pinning, security advisories, provenance/ownership gaps and remediation priority; verify a justified replacement without treating SBOM presence or a clean scan as supply-chain safety.
- **SEC6-O11:** Construct bounded, privacy-safe negative regression and change-drift evidence for runtime access, IAM/federation, CI gates and artifact policy, explaining missing observability, layered enforcement and safe rollback without claiming full incident detection.
- **SEC6-O12:** Deliver a reproducible, prioritized cloud/container/delivery security review and independently diagnose and defend an unfamiliar changed identity, runtime or supply-chain condition with controlled repair, justified residual risk and honest evidence limits.

## Modules

### Module 1 — Trust and Authority Across a Cloud Delivery System

#### Outcomes

- SEC6-O1
- SEC6-O5
- SEC6-O7

#### Lessons

1. **Who controls each stage of a service?** — Inspect a small pre-existing containerized service, release artifact and delivery description. Identify source author, reviewer, build worker, artifact publisher, runtime identity, data owner, infrastructure operator and end user. Mark the exact trust boundary and permitted/forbidden operation for each, then distinguish a fact in a file from a successful enforcement observation.
2. **Shared responsibility and actual authority** — Compare provider-controlled infrastructure, tenant configuration and application permission in a named cloud model. Trace the path from a request to an authenticated workload principal and resource policy, showing where a correct API handler cannot compensate for a powerful workload token or public storage grant. Avoid universal claims about which party patches a managed service.
3. **Independent permitted/denied resource matrix** — Derive explicit principal/action/resource/environment tuples for test, build, release and runtime. Predict a valid read, invalid write, cross-environment access and privileged deployment attempt *before* consulting a supplied policy trace. Explain why a generic "least privilege" label or a passing service health check is not an authorization oracle.
4. **Cloud policy evidence versus local assumptions** — Compare a local access-control emulator, a provider-specific IAM simulator, actual provider-authorized decision logs and inspected configuration. Explain why incomplete cloud evaluation, missing resource policies or cross-account conditions can change an answer. Bound conclusions rather than describing a home-built policy evaluator as a cloud security certification.

*Optional formative feedback:* Given an application that denies cross-tenant API requests but uses a workload role with broad storage read access, identify the independent cloud-resource exposure and the evidence needed to assess it.

### Module 2 — Image Trust and Container Runtime Boundaries

#### Outcomes

- SEC6-O1
- SEC6-O2
- SEC6-O3
- SEC6-O4
- SEC6-O10

#### Lessons

1. **Image inputs, build context and runtime contents** — Inspect a real locally built or supplied version-pinned OCI image from a source-identifiable base. Trace build context, ignore rules, layers, image metadata, default user and exposed configuration. Identify an embedded synthetic credential or unneeded executable and explain why removing a file in a later layer may not erase it from earlier layer history.
2. **Minimal image and immutable identity** — Rebuild a small approved image with defensible dependencies, versioned build recipe and an immutable digest. Contrast a tag that can move with a digest that names particular bytes; do not infer patch status or origin trust merely from the digest. Verify a legitimate start/stop and one normal service path after reducing attack surface.
3. **Host/kernel and runtime isolation contracts** — Compare OCI process settings, user namespaces/rootless mode, host UID mapping, Linux capabilities, seccomp and container engine implementation on a declared Linux target. Identify which values are configured, which are enforced and which require features not available to an unprivileged learner. Do not call `runAsNonRoot`, drop-all-capabilities or rootless mode a complete isolation guarantee.
4. **Mounts, file identity and writable surfaces** — Run an owned disposable container with a synthetic read-only secret, a separate writable data path and a forbidden host-file path. Check actual UID/GID and read/write outcomes inside and outside the container; distinguish default image root from effective kernel privilege, overlay filesystem changes and an accidental host-mounted credential. Correct the mount/user/permission policy and independently retest allowed writes and denied access.
5. **Runtime permissions, syscalls and resource budgets** — Reason about `no-new-privileges`, appropriate capability removal, available seccomp defaults, resource limits and socket exposure. Observe at least one safe actually enforced runtime change; for unavailable kernel features analyze genuine engine/version-specific traces. Distinguish an application denial from a kernel, mount, cgroup or container-engine denial, and test whether intended operation survives.
6. **Container and dependency finding triage** — Compare an image-layer/dependency inventory, one real or supplied scanner/advisory result, fix availability, runtime reachability and trust context. Verify a controlled base/dependency update and re-check real service behavior and its digest. Do not equate a scanner's count, no reported CVEs or minimal image size with proved security.

*Optional investigation:* Explain why a source tree's absence of a token file is not proof that a built image has no token in its lower layers, and why a read-only root filesystem does not make mounted writable secrets safe.

### Module 3 — Cloud IAM and Federated Workload Identity

#### Outcomes

- SEC6-O1
- SEC6-O4
- SEC6-O5
- SEC6-O6
- SEC6-O7

#### Lessons

1. **Principal, resource and condition semantics** — For a declared provider/engine, derive access decisions from specific identity policies, resource policies, requested actions, conditions and an authentic documented decision trace. Distinguish implicit deny, explicit deny and applicable permission boundaries or organization guardrails. Do not teach a universal identity-policy intersection: real resource grants and cross-account/session cases can change outcomes.
2. **Role and cross-environment authority** — Evaluate a synthetic developer, runtime, CI and release role against a narrowly scoped storage/database operation matrix. Explain who may assume a role versus what permissions the role grants and how scope changes with account, tenant, environment, resource pattern or condition. Repair a wildcard or mistaken trust grant while preserving intended legitimate access.
3. **Workload tokens are not passwords or permanent secrets** — Trace the separation between service identity, projected token, identity-provider issuer, relying-party audience and temporary resource credential. Explain expiry and rotation limits, readable token mounts and process access. Evaluate a leaked synthetic token scenario by its actual claims and trust policy, not by assuming "short-lived" automatically means safe.
4. **Federated CI identity and exact trust conditions** — Inspect official GitHub OIDC or equivalent provider documentation and supplied redacted claims. Distinguish workflow trigger, repository, ref, environment, trusted reusable workflow and audience as applicable to the named provider. Derive the required issuer, audience, subject and permission restrictions; reject a fork/untrusted branch or wrong environment without contacting a real cloud account. Granting `id-token: write` alone does not authorize cloud resource actions.
5. **Storage, workload and tenant boundaries** — Evaluate a public object policy, cross-environment service account and a multi-tenant workload as separate authority decisions. Determine which policy check actually protects each resource and show that application-layer tenant denial and network segmentation do not negate a direct cloud-resource grant. Include a revoked or changed-role negative case and a declared unsupported condition in any local policy model.

*Optional formative feedback:* Use a named provider's evaluation rules to decide whether an explicit deny, an overly broad resource grant or a mistaken federated subject condition is responsible for a denied or unintended operation.

### Module 4 — CI Privilege, Artifact Identity and Dependency Trust

#### Outcomes

- SEC6-O2
- SEC6-O6
- SEC6-O8
- SEC6-O9
- SEC6-O10
- SEC6-O11

#### Lessons

1. **Untrusted changes and privileged release jobs** — Inspect a small supplied CI/CD workflow and runner context. Reconstruct which event or contribution can change executable code, build scripts, action versions, caches or release definitions and which job has a write token, deployment approval, cloud federation or secret access. Show how the same source revision can have different privileges depending on its trigger and environment.
2. **Execution separation and runner/caches** — Design a deny-by-default boundary separating untrusted PR test jobs from protected releases, with minimal job scopes, clean runner state, restricted artifacts, reviewed dependencies and explicit approval. Exercise a synthetic negative case in a real local unprivileged runner or separated subprocess, or analyze genuine labeled hosted-runner execution traces when hosted enforcement is inaccessible. Never hand a real privileged token to untrusted code to test the policy.
3. **Source, build and artifact provenance** — Trace source revision, pinned inputs, builder identity, build invocation, artifact digest and promotion decision using an actual local artifact and supplied authentic provenance. Study **SLSA v1.2 Source and Build tracks** as separate claims; a hash proves byte identity relative to an expected hash, not who built it. An untrusted source origin remains untrusted even if a build faithfully records that source.
4. **Authenticated provenance verification policy** — Apply a maintained signature/attestation verification tool to an available authenticated bundle or inspect authentic target-specific verifier evidence, with an independently pinned expected issuer, signer/build identity, subject digest and permitted repository/build context. Verify an actual local digest and compare it to the policy and bundle; reject wrong digest, wrong producer/identity and absent/unverified attestation without disabling signature checks. **A valid signature by the wrong identity is a failure**, and a self-authored unsigned JSON file is not trusted provenance.
5. **Dependency graphs, SBOMs and policy gates** — Reuse APP6's dependency inventory rather than rebuilding it from zero. Classify direct/transitive and build/runtime dependencies, an unpinned action, compromised publish permission, advisory severity and actually reachable impact. Select one justified update/pin or policy correction, verify the resultant digest/dependency identity and rerun an independent negative security gate. State what scanners, SBOM completeness and provenance do not prove.

*Optional investigation:* Compare two signed artifacts: one with the expected digest from an unauthorized fork's builder and another from the approved builder with a changed subject. Explain why neither satisfies the declared release policy.

### Module 5 — Secrets, Environment Separation and Security Drift

#### Outcomes

- SEC6-O1
- SEC6-O3
- SEC6-O4
- SEC6-O5
- SEC6-O7
- SEC6-O11

#### Lessons

1. **Secret presence across the lifecycle** — Trace synthetic secrets from development file, image build, CI job, runtime environment or mounted file to process logs, crash artifacts and backup state. Identify who can read the data at each point and show why "not in Git" or "in an environment variable" is not sufficient evidence against exposure. Correct one actual leak path and check resulting legitimate behavior.
2. **Workload identity versus secret distribution** — Compare long-lived shared keys, service-specific projected credentials and short-lived federated credentials. For an owned synthetic example, specify expiration, rotation, compromised-token response and recipient rejection, including what remains possible until a token expires and whether stale workers still hold access. Do not impose SEC5's cryptographic-protocol implementation as a hidden prerequisite.
3. **Environment and resource policy drift** — Compare approved test/release/runtime identities, configuration references and permitted resource patterns to an intentionally altered policy or mounted credential. Predict both the legitimate operation and forbidden alternative before testing; identify whether the leak is direct cloud access, local file access or application authority and repair the correct enforcement point.
4. **Redacted decision signals and blind spots** — Correlate selected local runtime denies, CI gate outcomes, policy evaluation reasons and artifact verification logs into a bounded review record without exposing keys, bearer tokens or private data. Explain how missing audit events, provider retention/sampling and unobserved identity substitutions constrain claims; continuous detection and incident response belong to SEC7.
5. **Safe policy and release rollback** — Order a privilege reduction, key rotation or artifact gate change with pretest access/denial requirements, preserved recovery authority and a fallback that does not accept unverified artifacts. Test a changed condition, ensure intended operations remain possible, and document which access was truly revoked versus still valid until expiry or cached policy propagation.

*Optional formative feedback:* Given a secret scrubbed from a repository but retained in a previous image layer and a CI log artifact, locate the distinct remaining exposure and a credible revocation sequence.

### Module 6 — Independent Cloud/Container Security Assessment

#### Outcomes

- SEC6-O1
- SEC6-O3
- SEC6-O4
- SEC6-O5
- SEC6-O6
- SEC6-O8
- SEC6-O9
- SEC6-O10
- SEC6-O11
- SEC6-O12

#### Lessons

1. **Threat-to-control and evidence map** — Consolidate one pre-existing service's documented and observed identity, container, CI, image and resource boundaries into an actor/action/object matrix. Identify which vulnerability is actually exploitable in the controlled fixture, which failure exists only in a genuine supplied cloud trace and what still requires provider-authorized verification.
2. **Repair that survives alternative paths** — Choose proportionate image/runtime, IAM/secret or CI/provenance fixes; produce independently specified allowed, denied, invalid and changed-context checks. Include at least one competing path (direct resource grant, different ref, stale token, host mount or untrusted signer) that would bypass a superficial remediation.
3. **Unfamiliar changed authority or supply chain** — Investigate a newly presented bounded policy, OIDC claim, container mount/privilege setting, runner provenance or pinned dependency. Predict a failure and a competing hypothesis *before* examining the decisive evidence. Revise one control, verify the correct layer and preserve legitimate use under a safe rollback.
4. **Actionable review and technical defense** — Present a concise prioritized owner-facing assessment, configuration/revision links, actual and supplied provenance, negative oracles, residual risk and reviewable individual explanation. Reject an unsupported cloud-wide or certification claim and demonstrate why the selected correction addresses cause rather than merely hiding a scanner warning.

*Optional investigation:* Have an independent reviewer change one policy condition or signer identity and explain which existing regression detects the change and which observation remains insufficient.

## Completion requirements

**Four required summative evaluations** establish all SEC6 outcomes. One previously functioning, disposable service/image and narrowly scoped release fixture may be reused; each assessment evaluates a distinct security property and evidence type. Optional lesson investigations, checkpoint checkmarks, vendor certifications and paid services are not completion conditions. Every finding must distinguish **executed local control**, **authentic supplied provider/runtime decision**, **modeled policy**, and **unverified assumption**, naming actual enforcement and acceptable failure behavior.

- **SEC6-AS1** — Container Image and Runtime Boundary Assurance
  - **Outcomes:** SEC6-O1, SEC6-O2, SEC6-O3, SEC6-O4, SEC6-O10, SEC6-O11.
  - **Work:** Assess one real small, learner-owned container image and a running disposable instance on an accessible free pre-provisioned OCI-compatible environment. Inventory immutable image identity, base/build context, synthetic secret exposure, user and mounted-file access, writable paths, runtime privileges and resource/network assumptions. Rebuild or change the container image/runtime configuration to fix at least **two distinct justified security failures**, one affecting an image/build input and one affecting a **real runtime authority boundary** such as writable host mount, effective user/file permission or unexpected read access. Independently test legitimate service access and prohibited sensitive file/resource operations before and after; for a seccomp/capability/namespace feature unavailable on the learner's runtime, use genuine target-labeled trace analysis and explicitly state the enforcement limitation. Triage one supported dependency/base-image finding or supply a defensible decision when evidence does not justify an update.
  - **Criteria:** The actual image digest and build inputs are inspectable; sensitive synthetic data is not left in current or historical image layers after repair. At least one real local container authority restriction demonstrably denies a previously possible prohibited operation while preserving normal service function. The learner distinguishes container UID from host UID mappings, read-only layers from writable mounts, and declared seccomp/capability controls from observed kernel enforcement. The patch is tied to the earliest unsafe trust decision and includes independent normal, denied and failure-path tests; it does not require privileged changes to an unmanaged host or invent a global isolation claim. CVE/SBOM information is interpreted in the context of actual runtime relevance and image identity.
  - **Evidence:** Authorized local setup and target/runtime versions, source/build and OCI image metadata with digest, before/after configuration and artifact, independently derived access matrix, executed container start and file/resource permission outcomes, redacted synthetic-fixture checks, any clearly labeled authentic supplied kernel trace, dependency decision and residual limits.

- **SEC6-AS2** — Cloud-Style IAM and Workload Identity Policy Review
  - **Outcomes:** SEC6-O1, SEC6-O4, SEC6-O5, SEC6-O6, SEC6-O7, SEC6-O11.
  - **Work:** For one **named** documented cloud IAM policy engine and a fictional organization, independently specify principal/action/resource/environment decisions across runtime, human administrator, test worker and protected release identity, including at least one cross-environment/tenant or publicly accessible resource. Analyze real provider policy syntax and authentic vendor/supplied evaluation traces or the official policy simulator where available; assess an allow, implicit deny, explicit deny and a resource/boundary/session policy interaction relevant to that engine. Separately evaluate supplied sanitized OIDC workload/CI claims against an exact provider trust rule for issuer, audience, subject and allowed ref/environment. Correct an overbroad resource grant or mistaken role trust and present negative tests for an unauthorized branch/wrong environment/role; use a local restricted policy checker only for its declared subset, not as proof of a live cloud decision.
  - **Criteria:** The learner predicts and explains the specific provider-dependent result, including the policy combination that authorizes or denies it; no universal, falsely simplified intersection/deny algorithm is assumed. The revised resource and role-trust policy permits only the justified actions and denies synthetic overbroad, cross-environment and changed-claim cases under its stated engine; a signed OIDC token is not mistaken for unrestricted cloud resource permission. Genuine supplied observations, model decisions and unknown provider enforcement are unambiguously labeled. No actual cloud tenant, organization permission or live secret is required or claimed.
  - **Evidence:** Declared provider/version and official rule citations, resource/actor policy table, pre-observation allowed/denied predictions, policy/trust configuration and exact synthetic tuples, authentic labeled decision traces or disclosed simulator scope, changed-claim negative results, remediation and redacted evidence with unresolved gaps.

- **SEC6-AS3** — Untrusted CI and Artifact Provenance Security
  - **Outcomes:** SEC6-O1, SEC6-O2, SEC6-O6, SEC6-O8, SEC6-O9, SEC6-O10, SEC6-O11.
  - **Work:** Review a compact pipeline containing untrusted contribution tests and a privileged protected release with a synthetic deployment secret and pinned artifact inputs. Identify actual token and job permissions, code-injection boundaries, cache/runner reuse, workflow/action modifications and release approval. Exercise a real local unprivileged separation or inspect genuine hosted-runner event/permission evidence, and independently show that an untrusted change cannot access a synthetic privileged release resource under the tested configuration. Compute and check a local artifact digest and evaluate an **authentically signed** provenance/attestation bundle with a free maintained verifier or genuine labeled verification output, against **independently chosen expected signer/builder/issuer and subject digest**. Test wrong digest and wrong signing identity, distinguish SLSA v1.2 Source and Build evidence from an assumed level, and apply one justified dependency/action/image pin or security gate correction.
  - **Criteria:** The job trust and execution model is specific to the named pipeline and event trigger, with real or honest supplied negative evidence that a low-trust author cannot exercise privileged release authority. No real token is exposed to an untrusted runner; failure testing uses harmless synthetic data and separate identities. Artifact content is linked to a concrete digest; a signature without expected issuer/signing identity or correct subject does not pass policy. The candidate release is denied on mismatched digest, mismatched identity and missing trusted provenance, and permitted only when the declared policy is actually met. SBOM/scanner and SLSA track claims are no stronger than their demonstrated source/builder guarantees.
  - **Evidence:** Pipeline/job permission map and checked-in configuration, synthetic threat scenarios and local/hosted observation provenance, actual digest and pinned inputs, verifiable genuine signed bundle or accurately labeled independent verifier trace, expected identity/issuer policy, positive/wrong-identity/wrong-digest/absent-attestation cases, corrected gate and qualified release decision.

- **SEC6-AS4** — Unfamiliar Cloud/Container Trust Change and Technical Defense
  - **Outcomes:** SEC6-O1, SEC6-O3, SEC6-O4, SEC6-O5, SEC6-O6, SEC6-O7, SEC6-O8, SEC6-O9, SEC6-O10, SEC6-O11, SEC6-O12.
  - **Work:** Review an unforeseen but bounded change in the same system such as a broadened role trust policy, wrong environment claim, reused CI runner, substituted signed builder, unsafe container mount, changed secret injection or unpinned action. **Before** examining all traces, state the predicted permitted and prohibited operations and one competing explanation. Use real local enforcement for available container/pipeline controls and actual supplied provider/provenance evidence for unavailable hosted layers; apply a minimal security repair and rerun independently derived positive, denied and changed-condition tests. Present a prioritized owner-facing security report and individual written, recorded or live technical defense with a safe rollback plan, supported effect and residual uncertainties.
  - **Criteria:** The investigation identifies the actual policy/identity/artifact/runtime trust boundary and corrects the earliest unsafe authorization or provenance decision rather than concealing symptoms in logs. A direct/alternate path and an independently specified negative check discriminate the fix from a superficial rule; legitimate operation and rollback authority remain intact. Claims distinguish local observations, supplied provider/runner facts and pure hypotheses, including limits of token revocation, resource-policy interactions and incomplete software provenance. The learner can defend and revise the root-cause argument for a reviewer-provided variant without relying on scanner scores or a broad "secure cloud" assertion.
  - **Evidence:** Approved unseen scenario, explicit pretest predictions, trust/resource/identity diagram or table, reproduced local and labeled supplied traces, changed source/policy/artifact, independent negative and failure tests, redacted risk and remediation recommendation and reviewable individual defense.

### Assessment evidence and readiness

Every summative result identifies course revision, `SEC6-AS#` and applicable `SEC6-O#` identifiers, inspected source/policy and exact expected/observed decision. Executable image and local CI results must be reproducible from a clean approved disposable environment, with documented free runtime and versioned inputs. For supplied provider IAM, OIDC and signed-attestation traces, disclose origin, engine/version, issuer/context and limitations; distinguish policy analysis, actual signature-verifier output and model output. Do not place any production token, image registry credential or third-party data in a public submission.

No complete public cloud tenancy, managed Kubernetes deployment, production incident, real privileged exploit or live secret is required. Passing this course does **not** assert cloud-provider certification, universal image sandbox isolation, SLSA level achievement, verified compliance of a real organization's delivery pipeline or completed incident-response competence. Course readiness remains `draft` pending [Status Labels](../../spec/status-labels.md).

### Optional disciplinary references

- [NIST SP 800-190](https://csrc.nist.gov/pubs/sp/800/190/final) — application container and host/runtime security boundaries.
- [Kubernetes Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) — Baseline/Restricted capability, namespace and policy examples; an optional reference, not a mandatory Kubernetes cluster.
- [NIST SP 800-204D](https://csrc.nist.gov/pubs/sp/800/204/d/final) and [NIST SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final) — supply-chain security in DevSecOps pipelines and software-development assurance.
- [SLSA specification v1.2](https://slsa.dev/spec/v1.2/) — distinct Source and Build tracks, provenance and evidence-level limitations.
- [OWASP Top 10 CI/CD Security Risks](https://owasp.org/projects/top-10-cicd-security-risks) and [OWASP CI/CD Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/CI_CD_Security_Cheat_Sheet.html) — pipeline poisoning, runner trust, privileged workflows and credentials.
- [AWS IAM Policy Evaluation Logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html) — a real provider example, including resource-based policies and exceptions to simplistic rule intersections.
- [GitHub Actions OIDC reference](https://docs.github.com/en/actions/reference/security/oidc) — issuer/audience/subject claim and job trust conditions; actual provider IAM evaluation remains distinct.
- [Sigstore artifact verification](https://docs.sigstore.dev/cosign/verifying/verify/) — authenticated artifact identity/digest checks and offline bundle capabilities, not proof of software correctness.

These public references support source-backed reasoning and further study; they impose no additional paid tooling or course prerequisites.
