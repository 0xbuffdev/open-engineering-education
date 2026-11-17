# APP13 — Mobile Application Engineering

**Program:** APP — Application Engineering
**Type:** `course`
**Classification:** `elective`
**Prerequisites:** [APP19](APP19.md) — TypeScript Programming, [APP3](APP3.md) — Backend Framework Engineering
**Duration:** 14–18 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–14 focused hours/week (provisional; validate with learners and reviewers)

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

**Build, install, secure, synchronize, test and evolve a real mobile application** that remains useful when connectivity, process lifetime, native permissions, local schemas or server revisions change. The specialization is optional and **not required for APP9 or core graduation**.

**Approved direct prerequisites: APP19 + APP3.** APP19 supplies TypeScript and transferable programming competence. APP3 supplies a typed, authenticated Fastify API, server-held authorization and PostgreSQL transactions. APP13 applies these foundations at a device boundary; it does not repeat initial programming, HTTP service design or the complete React curriculum. APP20 is **optional only if a learner chooses React Native or a React-based hybrid framework**. No implicit APP2/APP20, SYS, iOS or commercial service prerequisite is introduced.

**Reference platform and equity:** Use a supported framework-neutral TypeScript + HTML/CSS client packaged with **Capacitor and Android SDK** into an actual installable APK. Its native WebView host, bridge, permission and lifecycle are real Android app behavior. Plain TypeScript is valid; React, Vue, Angular, Svelte, native Kotlin or Swift implementations may qualify through equivalent observable outcomes with their additional skills declared. Android emulator images and tools can be freely provisioned in advance; assess actual installed behavior under **two representative Android configurations** differing by OS, display or text/accessibility settings. The course requires no owned phone, paid testing farm, Play Console account, public app store, Mac, Xcode or Apple Developer membership. iOS concepts and differences are reviewed from documented sources; an iOS binary or simulator test is optional because it depends on macOS/Xcode. Never report Android observations as verified iOS behavior.

**One real protected task:** Implement a small mobile field-task, inventory, educational activity or similar application against a local APP3 service and real PostgreSQL. Demonstrate usable touch navigation, real device capability, durable local read/write, two synthetic identities, and at least one authoritative server write. A desktop browser screen or mocked local database cannot satisfy native packaging, permissions, process death or device data evidence. Limit personal information; test using synthetic records and owned disposable emulators/local backend only.

**Mobile state and offline work:** Keep a transactional, versioned local SQLite-capable repository or equivalent true native persistence for locally accepted edits and pending commands. The device-local store is the presentation source of truth while the server remains authoritative for shared business state. A local accepted write is **not** a server-confirmed commit. Use stable command/idempotency IDs, finite retry, response-loss replay, actual server SQL constraints and version/conflict reconciliation. Do not confuse connectivity hints with server reachability or use plaintext localStorage for long-lived credentials/critical durable queues. A process kill, restart, account change or app upgrade must not silently lose or misassign committed offline intent.

**Lifecycle and power:** Distinguish Activity recreation, actual app process death, foreground/background, OS power management and supported native task scheduling. A paused JavaScript timer is not a durable Android service; Android WorkManager-style background jobs are deferrable and subject to OS policy, not exact recurring execution guarantees. A correct bounded **resume-driven synchronization** can meet requirements; optional native scheduler integrations must disclose observed support and deferral. Push/local notification or deep-link messages are not a verified authorization or committed record: authenticate/refetch authoritative state on receipt.

**Security and device privacy:** Protect actual session tokens through an audited platform-appropriate secure credential solution such as Android Keystore-backed storage, validate HTTPS server identity, enforce backend action/object/property/tenant authorization, and segregate local rows and pending work by account. Exercise logout, expired sessions, bridge input validation, safe file/URI handling, minimal permission prompts, denial/revocation and scoped data/backup/log retention. Prefer OS pickers when they meet the task to avoid broad photo/location/storage permissions. A test-signed debug APK does not prove production release signing or real world device security.

**Accessibility, release and correctness:** Verify actual touch targets, navigation, IME/keyboard behavior, safe areas, TalkBack or available accessibility checks, larger text and usable stale/conflict/error states. Run true device lifecycle tests and a locally installable signed-debug/test-signed package upgrade, including an old local schema with queued operations and a safe forward migration or bounded downgrade refusal. Compare actual cold/warm startup, network bytes, local DB cost, CPU and memory with disclosed emulator limitations; do not invent real battery-life results or live store rollout. Require reproducible seeded regressions and honest operation/cost trade-offs.

Seventeen learning outcomes across fifteen varied modules lead to seven cumulative required summative assessments and an accessible independent technical defense. Lessons and informal device experiments are **formative** unless used in those assessments. The estimated 14–18 weeks and workload are provisional; structural tooling alone does not make a course learner-`tested` or educationally `verified`.

## Learning outcomes

- **APP13-O1:** Define bounded mobile user tasks and context-sensitive acceptance criteria for touch, accessibility, intermittent networks, lifecycle, resource limits, security and release, distinguishing tested devices from assumed platform behavior.
- **APP13-O2:** Compare Android/iOS native, hybrid WebView, React Native and PWA delivery with evidence-based OS access, performance, maintenance and toolchain trade-offs; deliver an installable mobile application without making React/APP20 compulsory.
- **APP13-O3:** Implement and verify accessible mobile navigation, touch controls, IME-safe forms, responsive layouts, safe areas, large text and screen-reader/keyboard feedback across representative device configurations.
- **APP13-O4:** Design typed presentation, domain, local persistence, authenticated network and native bridge boundaries with independent runtime validation, source ownership and testable adapters.
- **APP13-O5:** Handle real app foreground/background, activity recreation, process death, device rotation, resource pressure and restart, recovering appropriate navigation, drafts and pending intent without assuming always-running JavaScript.
- **APP13-O6:** Implement transactional, versioned local device data and schema migration with interruption/corruption/space recovery, account scoping and justified backup/deletion policies.
- **APP13-O7:** Implement honest offline-first reads and durable pending mutations with stable operation IDs, finite retries, uncertain acknowledgments, invalid credentials and safe restart replay, distinguishing local acceptance from remote commit.
- **APP13-O8:** Reconcile queued edits with a real authenticated APP3/PostgreSQL service across two clients using server-issued revisions, independent concurrency checks, conflicts and authorized tenant-scoped synchronization.
- **APP13-O9:** Enforce mobile session, server-side action/object/property authorization, secure credential/key storage, TLS identity, private local files/cache, redacted logs, safe logout, links and backups against realistic device threats.
- **APP13-O10:** Integrate a real, justified mobile device capability through a typed platform adapter with granted, denied, revoked, canceled and unavailable behavior, minimal permissions and a functional nonpermission alternative.
- **APP13-O11:** Explain and test foreground/resume versus OS-scheduled background work, constrained network/battery policies, bounded queue draining and true execution uncertainty without promising continuous background JS or exact scheduling.
- **APP13-O12:** Treat optional local/push notifications and deep links as validated user intent or authorized invalidation hints, preserving permission/privacy and server-confirmed business state.
- **APP13-O13:** Measure device/emulator startup, responsiveness, local data work, memory and network/battery proxies and defend a tested improvement without conflating emulator data with physical energy measurements.
- **APP13-O14:** Build a layered mobile verification strategy covering local domain/DB, backend contract, bridge/permission, installed-device lifecycle, accessibility, offline/concurrent faults and reproducible seeded-regression CI across two Android test profiles.
- **APP13-O15:** Produce, install and verify a versioned signed-debug or disposable-test-signed Android artifact, assess manifest/build provenance, local staged rollout, client/server compatibility, queued-data-preserving upgrade and safe rollback or forward repair without paid app stores.
- **APP13-O16:** Investigate an independently reproduced crash, upgrade, sync, permission or performance incident with sanitized device/service evidence, preserved user data, an operator runbook and honest platform/security limitations.
- **APP13-O17:** Deliver and independently defend a coherent installed, offline-capable, authenticated mobile client under an unfamiliar bounded lifecycle, permission, sync, local migration, release or performance change.

## Modules

### Module 1 — Mobile Context, Product Need and Platform Strategies

#### Outcomes

- APP13-O1
- APP13-O2
- APP13-O3
- APP13-O17

#### Lessons

1. **Mobile engineering versus mobile-sized web** — Distinguish installed OS lifecycle and device permission evidence from responsive browser screenshots.

2. **Evolution of mobile client platforms** — Compare native SDKs, WebView hybrids, PWAs and cross-platform runtimes as alternative problem solutions.

3. **Choose one accountable mobile task** — Scope an offline field-work or inventory workflow with real user roles and protected server records.

4. **Research and evidence provenance** — Separate sourced public usability guidance, synthetic task scenarios and actual consented user observations.

5. **Platform comparison matrix** — Compare native UI, hybrid, React Native and PWA in maintenance, bridge, offline, accessibility and release cost.

6. **React remains an optional choice** — Explain the APP19 and APP3 foundations and when a chosen React Native implementation benefits from APP20.

7. **Choose required Android evidence** — Define two free emulator/device profiles and explicitly label iOS comparison or macOS-only testing as optional.

8. **Initial risk and acceptance contract** — Publish observable denied, offline, terminated, conflicting, accessible and upgraded-device success rules.

*Optional practice — overpromised-platform critique:* Reject an iOS App Store requirement or claim of universal battery life from an Android emulator.

### Module 2 — Toolchain, Packaged Android Runtime and Bridge Contracts

#### Outcomes

- APP13-O2
- APP13-O4
- APP13-O9
- APP13-O14

#### Lessons

1. **Free reference toolchain** — Pin supported Node/TypeScript, Capacitor, Android SDK and emulator build versions and plugin dependencies.

2. **Android app project anatomy** — Identify build resources, manifest, application identity, Gradle, bundled web assets and native host.

3. **A truly installable client** — Build and launch a local debug APK in an emulator and inspect package metadata rather than run only a web preview.

4. **Device WebView boundary** — Inspect native-to-TypeScript runtime exchange, network origin, app sandbox and host permissions.

5. **Native runtime versus browser APIs** — Document which features execute through WebView, native plugin, OS, and backend service.

6. **Typed and guarded platform adapter** — Validate plugin results, cancellation, unexpected unsupported behavior and resource cleanup at a typed boundary.

7. **Emulator-to-host HTTPS service** — Configure authenticated local backend reachability and trusted test certificates without disabling TLS validation in a shipped app.

8. **Alternate architectures without hidden requirements** — Allow native Kotlin/Swift or React Native equivalents only with declared additional skills and identical assessment evidence.

*Optional practice — installed-protocol check:* Show why bundling a PWA without real Android build, bridge and lifecycle tests is insufficient.

### Module 3 — Touch, Navigation, Assistive Access and Input State

#### Outcomes

- APP13-O1
- APP13-O3
- APP13-O4
- APP13-O14

#### Lessons

1. **Information hierarchy on small screens** — Design short navigation paths, task labels and back behavior for the real mobile workflow.

2. **Tap and gesture accessibility** — Test touch-target size, alternative non-gesture actions and destructive confirmation.

3. **System bars and display cutouts** — Support platform safe areas, bottom navigation and software keyboard overlays.

4. **Forms under IME changes** — Preserve validated drafts under soft-keyboard open/close and orientation changes.

5. **Semantics and focus** — Inspect labels, roles, reading order, error placement and real Android accessibility tree.

6. **TalkBack and keyboard alternatives** — Perform actual available emulator accessibility checks and record limitations.

7. **Large text and reflow** — Test text/display scaling, contrast, narrow viewport, landscape and reduced-motion preference.

8. **Deep-link route restoration** — Validate inbound routes and protected data before opening saved destination after restart.

*Optional practice — inaccessible permission task:* Repair a touch-only action or invisible error that blocks task completion.

### Module 4 — Typed Mobile Architecture and State Ownership

#### Outcomes

- APP13-O2
- APP13-O4
- APP13-O5
- APP13-O6
- APP13-O9

#### Lessons

1. **Presentation, domain and infrastructure** — Separate task decisions, mobile UI, local data, server API and native plugin behavior.

2. **Shared TypeScript domain models** — Reapply APP19 types while refusing to trust unchecked remote or persisted runtime data.

3. **Stable local repository contract** — Expose device-local read models and pending writes independently of transport state.

4. **Authentication state ownership** — Keep credentials, tenant identity, public account display and local session boundaries distinct.

5. **Dependency injection and deterministic edges** — Control network, storage, native bridges and clock in practical unit tests.

6. **Error/status domain taxonomy** — Represent unavailable, queued, failed, forbidden, conflicted, storage-full and invalid-record outcomes explicitly.

7. **Persisted record validation** — Check old or corrupt data after migration rather than casting JSON as valid TypeScript.

8. **Application architecture guard tests** — Block UI imports of raw secrets, direct SQL bypass or unintended native permission work.

*Optional practice — tangled-screen refactor:* Move storage/network/permission handling from an untestable screen handler into owned modules.

### Module 5 — Android Lifecycle and Durable User-State Recovery

#### Outcomes

- APP13-O3
- APP13-O4
- APP13-O5
- APP13-O6
- APP13-O14

#### Lessons

1. **Foreground, background and paused states** — Observe Android activity and application lifecycle versus OS process lifetime.

2. **Lifecycle Transitions and Durable Draft Recovery** — Distinguish ordinary Activity recreation from real process termination and subsequent cold restart; save unsent protected user input before interruption and reconstruct acceptable navigation after restart.

3. **Low-memory and OS scheduling limits** — Demonstrate why listeners and JS timers cannot guarantee work after background restrictions.

4. **Typed App lifecycle plugin** — Observe pause, resume and appStateChange on installed Android, checking bridge support and cleanup.

5. **Crash in local transaction window** — Interrupt before and after committing local record-plus-pending-intent and inspect actual state.

6. **Listener and file handle cleanup** — Release native resources, app event handlers and canceled network work through repeated resume.

7. **Reconcile on foreground return** — Recheck session, offline queue and remote revisions under bounded rates.

*Optional practice — killed-draft recovery:* Repair loss of a protected user draft without exposing it after account switch.

### Module 6 — Local Database, Migrations and Privacy Lifecycle

#### Outcomes

- APP13-O4
- APP13-O5
- APP13-O6
- APP13-O7
- APP13-O9

#### Lessons

1. **Device-local durable source of view** — Use transactional SQLite-capable storage or comparable real native persistence, not in-memory mocks.

2. **Local SQL schema and constraints** — Model tenant ownership, entity versions, migration identity, pending commands and unique idempotency IDs.

3. **Atomic saved intent** — Commit local accepted mutation and its eventual-sync instruction together.

4. **Versioned migration with unsent changes** — Upgrade a fixture database without dropping queued commands or violating foreign keys.

5. **Storage exhaustion and corruption** — Inject quota or damaged-record conditions and report safe user-visible recovery.

6. **Backup scope and encrypted material** — Describe OS backup behavior, protected tokens, local records, restore risks and separate server facts.

7. **Account-scoped data and logout** — Verify another synthetic user cannot read previous user's rows, pending changes or local files.

8. **Deletion and retention limits** — Distinguish logical deletion, encrypted storage, copied backups and server-retained data.

*Optional practice — interrupted schema upgrade:* Prove queued edits survive a failed migration or are safely quarantined and explained.

### Module 7 — Offline Queues, Idempotency and Honest Pending UX

#### Outcomes

- APP13-O5
- APP13-O6
- APP13-O7
- APP13-O8
- APP13-O11

#### Lessons

1. **Choose offline read/write policies** — State which tasks remain useful without connectivity and which require immediate server authority.

2. **Durably queue a command** — Persist command ID, account/resource, base revision and state before displaying locally accepted work.

3. **Connectivity signal versus real service** — Treat OS network status as a hint, not proof that authenticated requests can succeed.

4. **Retry caps, jitter and budgets** — Bound repeated attempts and distinguish transient, terminal and stale-auth errors.

5. **Lost acknowledgement and replay** — Reproduce a server-committed write with lost response, restart the client and verify stable idempotency.

6. **Unsent versus already committed cancellation** — Avoid promising undo when a queued command may have reached server authority.

7. **Per-resource command ordering** — Prevent out-of-order local edits from invalidating newer server revisions.

8. **Conflict and rejection UI** — Preserve attempted edits, show current state and offer meaningful accessible recovery.

*Optional practice — duplicate replay failure:* Fix a restarted sync loop that double-applies an accepted database change.

### Module 8 — Multi-Client Reconciliation and Authorized Conflict Handling

#### Outcomes

- APP13-O6
- APP13-O7
- APP13-O8
- APP13-O9
- APP13-O14

#### Lessons

1. **Authenticated API and trust** — Use real APP3 TypeScript/Fastify/PostgreSQL service with server-held action, field and tenant permissions.

2. **Revision and cursor model** — Request scoped current state and use server-issued versions and explicit missing-history fallback.

3. **Two independent opposing edits** — Apply simultaneous changes through separate mobile/test clients with real PostgreSQL concurrency.

4. **Conflict policies by business rule** — Compare server rejection, meaningful field merge, append-only and dangerous timestamp last-writer-wins.

5. **Local conflict presentation** — Display which offline edit was rejected and let the user choose a safe reviewed resolution.

6. **Expired sessions and queued commands** — Pause protected sends and reauthenticate without relabeling denied state as merely offline.

7. **Cross-account isolation on reconnection** — Prove previous user's commands cannot be resubmitted under a different token.

8. **Catch up after a long absence** — Refresh from authorized snapshot or bounded delta after old cursor expiration.

*Optional practice — silent overwrite diagnosis:* Repair a two-client conflict that had discarded one accepted version.

### Module 9 — Mobile Session, Transport and Local Data Security

#### Outcomes

- APP13-O5
- APP13-O6
- APP13-O8
- APP13-O9
- APP13-O10

#### Lessons

1. **Threat model for a lost device** — Identify token theft, hostile connectivity, exported intents, debug logs and insecure plugin calls.

2. **Actual session and token lifecycle** — Demonstrate expiry, revocation, logout, refresh and server-side permission checks.

3. **OS-protected credential storage** — Use a suitable Android Keystore-backed solution for secrets; reject plaintext long-lived tokens in localStorage.

4. **Correct HTTPS verification** — Test the intended server certificate/hostname even against a locally controlled development CA.

5. **Deep links and exported intent validation** — Reject untrusted app routes and never treat intent parameters as server authorization.

6. **WebView and native bridge boundaries** — Review navigation allowlists, third-party plugin rights and validation of remote content.

7. **Private backups and screens** — Check temporary files, local app data, recents-screen policy where relevant and backup exclusions.

8. **Redact crash and network evidence** — Keep credentials, private form fields and full sensitive URLs out of emitted diagnostics.

*Optional practice — stolen-session scenario:* Revoke a test token and show queue, cache and local secrets honor the new principal.

### Module 10 — Native Device Permissions and Privacy-Safe Capabilities

#### Outcomes

- APP13-O2
- APP13-O3
- APP13-O4
- APP13-O9
- APP13-O10

#### Lessons

1. **Choose an emulator-available capability** — Implement a justified system picker or local notification via an audited native bridge.

2. **Inspect least-privilege manifest** — Prefer platform-managed picker access over blanket storage, camera or location grants.

3. **Request in user task context** — Explain optional capability and ask at the moment of legitimate need.

4. **Granted, denied and limited responses** — Test supported permission modes, canceled picker and degraded workflow.

5. **Revocation across app resume** — Recheck sensitive permissions after device settings change and avoid stale privileges.

6. **Typed native result and URI validation** — Handle malformed plugin values, restricted file URIs and errors before reading/copying data.

7. **Temporary file ownership and cleanup** — Control copied data, MIME/size limits and deletion after task completion.

8. **Privacy and consent disclosure** — Describe why information is needed, who can view it and how long local copies persist.

*Optional practice — safe no-permission fallback:* Demonstrate manual entry after denial, simulator absence or canceled capability.

### Module 11 — Background Constraints, Power and Notification Hints

#### Outcomes

- APP13-O5
- APP13-O7
- APP13-O8
- APP13-O11
- APP13-O12
- APP13-O13

#### Lessons

1. **OS background scheduling restrictions** — Explain why a paused JS WebView timer is not a guaranteed background service.

2. **Deferrable Android scheduler concepts** — Compare OS-managed WorkManager constraints and retry with documented plugin support.

3. **Correct foreground/resume drain** — Implement bounded secure synchronization on return to foreground without a mandatory native scheduler plugin.

4. **Optional platform task bridge** — Evaluate actual background job constraints, observed deferral and app restart behavior when available.

5. **Metered and low-power operation** — Reduce polling, retries, payload bytes and unnecessary wakeups under supported conditions.

6. **Push versus committed business state** — Use push/local notifications as hints to authorized refetch, never as proof of backend success.

7. **Notification capability permission** — Test availability, denied permission and a usable in-app fallback.

8. **Battery/network proxy measurements** — Compare counts, CPU/wake behavior and bandwidth without unmeasured physical battery assertions.

*Optional practice — impossible timer promise:* Replace continuous background polling with documented OS-aware, resume-safe reconciliation.

### Module 12 — Mobile Startup, Responsiveness, Memory and Bandwidth

#### Outcomes

- APP13-O3
- APP13-O5
- APP13-O11
- APP13-O13
- APP13-O14

#### Lessons

1. **Cold and warm start definitions** — Measure installed launch, resumed task readiness and local first useful interaction.

2. **Main-thread and input delays** — Profile real WebView/OS input response, large DOM work and user-visible paint/interaction.

3. **Network budget and error costs** — Report bytes, retries, batch sizes and data transfer under simulated mobile connection.

4. **Local SQL access and indexing** — Inspect query plans, row access and transaction lengths for real mobile list/sync data.

5. **Repeated navigation memory retention** — Trace unremoved listeners, image buffers and native handles over multiple screens.

6. **Media decoding and storage limits** — Resize and bound images/documents without violating accessibility or private content access.

7. **Emulator versus device claims** — Report CPU/throttling, architecture, power and hardware limitations of tested Android profiles.

8. **Accessible performance outcomes** — Retest screen reader, large text, focus and reduced motion after optimizing.

*Optional practice — runaway sync repair:* Measure and fix high-frequency retry loops while preserving queued edits and auth state.

### Module 13 — Device-Level Quality, Failure Injection and Test Matrices

#### Outcomes

- APP13-O3
- APP13-O5
- APP13-O6
- APP13-O7
- APP13-O8
- APP13-O9
- APP13-O10
- APP13-O13
- APP13-O14

#### Lessons

1. **Risk-based mobile coverage** — Map local domain, SQL, HTTP contract, permissions, installed UI and OS interruption tests to outcomes.

2. **Two Android test configurations** — Compare emulator/device OS version, screen/text size and accessible UI under a documented matrix.

3. **Synthetic identity and schema fixtures** — Seed two tenants, expired credentials, pending work, conflict and old local DB version.

4. **Real device accessibility review** — Inspect TalkBack/keyboard/touch and UI notices using supported platform tools.

5. **Network and process fault injection** — Control airplane/network loss, delayed replies, kill/rotation/resume and interrupted migration.

6. **Native adapter denial tests** — Check rejected plugin calls and unauthorized file URI without relying only on JS mocks.

7. **Independent server state oracle** — Verify local queue and final PostgreSQL rows after two competing authenticated clients.

8. **Data privacy and signing tests** — Inspect logs, credential handling, manifest and backup rules with negative evidence.

9. **Fail-closed build and CI gate** — Run repeatable typecheck/build, independent HTTP/SQL, mobile emulator checks with declared machine limits.

*Optional practice — seeded fault correction:* Make a lifecycle, permission or offline regression fail before a genuine code fix.

### Module 14 — Versioned Build, Test Signing and Reversible Upgrade

#### Outcomes

- APP13-O5
- APP13-O6
- APP13-O9
- APP13-O14
- APP13-O15
- APP13-O16

#### Lessons

1. **Manifest and package identity** — Inspect Android application ID, versionCode/versionName, min/target SDK and exported capabilities.

2. **Debug versus release artifact trust** — Distinguish debug APK signing from protected release key identity and Play app-bundle distribution.

3. **Local installable signing workflow** — Produce a versioned test-signed APK with disposable credentials, inspect digest and install independently.

4. **Signing key provenance and secrecy** — Prevent production key material from being committed, uploaded or included in untrusted CI logs.

5. **Upgrade installed state with pending writes** — Install v1 fixture, queue a write, upgrade to v2 and verify intact local schema/authorization.

6. **Old/mobile/new backend compatibility** — Check staged API contract evolution for users who cannot update immediately.

7. **Local staged rollout simulation** — Test two version channels/profiles and seed a regression without needing an app store.

8. **Downgrade versus forward repair** — Prove when schema rollback or old binary cannot safely consume migrated local records.

9. **Store listing and iOS comparison** — Explain optional Play AAB, app privacy declarations and iOS Xcode/signing without requiring paid publication.

*Optional practice — upgrade break and repair:* Fix a release that destroys offline intent and document rollback restrictions and restore evidence.

### Module 15 — Integrated Installed Offline Mobile Client and Defense

#### Outcomes

- APP13-O1
- APP13-O2
- APP13-O3
- APP13-O4
- APP13-O5
- APP13-O6
- APP13-O7
- APP13-O8
- APP13-O9
- APP13-O10
- APP13-O11
- APP13-O12
- APP13-O13
- APP13-O14
- APP13-O15
- APP13-O16
- APP13-O17

#### Lessons

1. **Defensible mobile user workflow** — Integrate an accessible touch task, authenticated APP3 server and real local data.

2. **Deploy a real installable Android build** — Run versioned package in documented emulator/device and inspect manifest, bridge and permissions.

3. **Demonstrate OS interruption survival** — Exercise rotation, true process death, app resume and saved local draft restoration.

4. **Prove offline command durability** — Queue a write, lose an HTTP acknowledgement and replay safely after restarting with correct server effects.

5. **Resolve two-client conflict** — Show competing authenticated mobile/backend edits, accessible choice and final committed PostgreSQL truth.

6. **Enforce safe device permission lifecycle** — Test granted/denied/revoked or unavailable native capability and usable alternative.

7. **Audit credentials and private local state** — Show OS-protected secret, TLS validation, logout and cross-account data isolation.

8. **Measure device and network behavior** — Compare startup/sync and resource profiles with real task/accessibility regressions.

9. **Validate background and notification limits** — Show bounded foreground drain and optional deferral or hint without promising continuous execution.

10. **Rehearse backward-compatible update** — Install two test versions around a real local migration and preserve queued work.

11. **Prove independent multi-device matrix** — Run tests on two representative Android profiles with disclosed iOS/physical device limitations.

12. **Defend an unfamiliar bounded change** — Diagnose a reviewer-provided permission, lifecycle, sync, migration or release fault with actual failing/passing evidence.

## Completion requirements

All **APP13-O1–APP13-O17** require credible independently inspectable evidence across **seven mandatory summative assessments**. One coherent mobile product can support every assessment. Module investigations, optional second mobile platforms, store distribution and additional plugins are **formative or elective** unless included in the public criteria below.

| Required assessment | Required outcome coverage | Principal evidence |
| --- | --- | --- |
| `APP13-AS1` — Mobile Architecture, Installable Client and Accessible User Task | APP13-O1, APP13-O2, APP13-O3, APP13-O4, APP13-O14 | User task/acceptance and platform alternatives, lockfile/SDK and reproducible installation commands, Android manifest/package/version and signed-debug artifact hash, native bridge/typed contract source, two-profile emulator/device matrix, actual accessibility/navigation/IME observations and API task trace |
| `APP13-AS2` — Lifecycle Survival, Local Transactional Data and Migration | APP13-O4, APP13-O5, APP13-O6, APP13-O7, APP13-O9, APP13-O14 | Real local database schema/migration/transaction source and before/after records, interrupted/rotated/process-killed installed app reproduction, pending-operation audit, error/quarantine tests, account-switch denial, backup/retention policy and independent restart results |
| `APP13-AS3` — Offline Command Replay, Authenticated Synchronization and Conflicts | APP13-O5, APP13-O6, APP13-O7, APP13-O8, APP13-O9, APP13-O11 | App-local queue and real PostgreSQL/schema versions, two-client accounts, network and lost-ack fault controls, before/after DB and HTTP logs, actual authorization/concurrency negative tests, final reconciled device views and accessible conflict/uncertainty transcript |
| `APP13-AS4` — Device Capability Permissions, Local Secrets and Mobile Threat Defense | APP13-O2, APP13-O3, APP13-O4, APP13-O9, APP13-O10, APP13-O12 | Permission and manifest inventory, installed device native bridge grant/deny/limited/revoke traces, fallback UX and accessibility, secret storage/TLS tests, malicious URI and direct backend permission checks, account/logout/backup/log audit, retention policy and residual threat analysis |
| `APP13-AS5` — Background Constraints, Energy/Network Budget and Real Device Performance | APP13-O3, APP13-O5, APP13-O7, APP13-O11, APP13-O12, APP13-O13, APP13-O14 | OS lifecycle/background policy and supported adapter, foreground/resume and optional scheduled-work logs, controlled network/low-power fault matrix, repeatable startup/network/CPU/memory/DB traces, before/after code and user state checks, proxy energy assumptions and limits |
| `APP13-AS6` — Installed-Device Quality, Versioned Release and Safe Upgrade Recovery | APP13-O5, APP13-O6, APP13-O8, APP13-O9, APP13-O13, APP13-O14, APP13-O15, APP13-O16 | Source/toolchain lock, signed test artifact and metadata digest, manifest and signing-key storage review, versioned app/DB/API compatibility matrix, emulator/device screenshots or logs, failing-before/passing-after tests, deployment channel/release/incident decision and safe user/operator instructions |
| `APP13-AS7` — Integrated Offline Mobile Product and Independent Technical Defense | APP13-O1, APP13-O2, APP13-O3, APP13-O4, APP13-O5, APP13-O6, APP13-O7, APP13-O8, APP13-O9, APP13-O10, APP13-O11, APP13-O12, APP13-O13, APP13-O14, APP13-O15, APP13-O16, APP13-O17 | Coherent versioned source, environment and signed artifact identities, two Android test profiles, source and native adapter, migrations/queue/SQL and protected accounts, actual device/permission/lifecycle/network/upgrade traces, correct sync/security regression, performance budget, fault/repair diff, user/operator runbook and accessible independent technical defense |

### Shared academic, device and integrity boundaries

- Use version-pinned freely accessible TypeScript, a compatible Android Studio/SDK and emulator/system image or controlled test device, a reviewed native bridge/runtime, an actual local mobile database, a private synthetic APP3/Fastify/PostgreSQL service and disclosed user/tenant identities. Initial free tool downloads are acceptable. Do not require a Play/Apple account, physical device, paid cloud, Mac, paid device farm, managed auth, React Native or hidden signing credentials.
- Install and test a genuine Android package; a browser-sized prototype, empty React Native shell, UI mock or APK metadata with no executed native lifecycle/permission work cannot independently establish mobile engineering competence. Use at least **two representative Android OS/display/text/accessibility configurations**, which may be emulated. State exactly what hardware, accessibility services and app versions actually ran.
- **iOS is compared, not silently certified.** iOS lifecycle, Keychain, background task, permission, accessibility and release differences are reasoned about with cited public documentation and optional Xcode simulator observations. iOS builds need macOS/Xcode and commercial app-store distribution has separate access, so an iOS binary, Apple Developer membership and actual public publication are never completion gates.
- Keep the APP19 + APP3 direct prerequisites exact. Students may choose React Native or React-based WebView UI but then must supply the additional APP20/React competence their implementation needs; no other student must take APP20 as a hidden foundational requirement. Equivalently advanced native Kotlin/Swift implementations are assessed by outcomes, not chosen framework prestige.
- Model **real offline local transactions and durable pending commands** with stable idempotency/operation IDs, identity/resource/version metadata and meaningful crash/restart evidence. Protect concurrent mobile-local and remote writes with correct server-held policy and actual PostgreSQL revision/constraint checks. Treat local acceptance, queued, confirmed, rejected and uncertain status as distinct. Internet reachability and push notification do not prove server commit.
- Test a lost response after authoritative write, retry, two-client conflict, expired token, denied operation, wrong account/tenant and network reconnection with real HTTP/database observations. Document when safe merging is possible, when server rejects and when the user's attempted edit must be preserved for human resolution. Do not silently last-write-wins away valid data.
- **Platform process lifecycle is not an always-on JavaScript worker.** Exercise actual process termination separate from screen rotation/Activity recreation. Preserve drafts and queued commands, and use correct foreground/resume reconciliation. Background scheduling, WorkManager-compatible jobs, push/local notifications and OS power policies are discussed and optionally demonstrated where supported; do not claim exact timing or constant background access.
- For private device state, use credible OS-protected token/key handling (e.g., Android Keystore-backed plugin) and declare what is actually encrypted, what is backed up and what is only app-sandboxed. Avoid long-lived plaintext credentials in WebView localStorage, untrusted certificate bypass in distributable builds, sensitive event traces, uncontrolled file URI sharing and session-crossing local caches. Prove backend authorization independently of client checks.
- Choose at least one **real device-native capability**, preferably an OS-managed document/photo picker or notification-supported flow, and show appropriate allowed, denied, revoked, canceled and unavailable states to the extent supported by the chosen API. Minimize manifest permissions and offer a usable fallback; virtual hardware unavailable in an emulator must not force purchase of a sensor or a physical device.
- Protect accessible navigation, tap and gesture alternatives, system keyboard/IME interaction, visible feedback, larger text and screen-reader semantics under both normal and offline/recovery paths. A visually polished mobile frame does not compensate for inaccessible controls or silent pending/conflicting work.
- Qualify local device performance measurement: report startup, CPU/memory/network, SQL, sample counts, emulator/OS profile, error rates and proxy-based energy reasoning. Do not extrapolate actual physical battery life or iOS performance from a desktop browser or single emulator.
- Build/install a **locally test-signed package** with inspectable version/digest and least-privilege keys. Show an upgrade from old local data to new revision retaining unsent commands, and document server-side old/new client API compatibility, safe forward fix and actual downgrade limits. Store publication, public release credentials, public download trust and live rollout statistics are not required or implied.
- Run mobile fault, privacy and security exercises **only on authorized disposable test packages/emulators, synthetic users and locally controlled backend databases**. Do not test on strangers' devices, actual user files, third-party applications or production accounts without authorization.
- A reviewer may select an unfamiliar **bounded** permission, lifecycle, queued sync, conflicted server revision, corrupt/migrating local record, native bridge, upgrade or performance problem. The test must use publicly identified outcome classes and a free accessible evaluation environment. Written, recorded, synchronous or equivalent inspectable defense meets the same content criteria; fabricated teamwork and user research are not required.

### Required summative assessments

- **APP13-AS1** (required mobile architecture, installable client and accessible user task)
  - Outcomes: APP13-O1, APP13-O2, APP13-O3, APP13-O4, APP13-O14
  - Work: Choose a bounded mobile task served by an actual APP3 authenticated API and evaluate TypeScript hybrid versus another plausible native/cross-platform option with licensing, Android toolchain, lifecycle, interface and maintenance trade-offs. Build and install a locally debug/test-signed Android package on an emulator or owned compatible device with a real typed native platform adapter, a navigable touch/IME-safe interface, safe-area and text-scale support and meaningful offline/forbidden/task feedback. Run an observed usability/accessibility matrix across at least two representative Android OS/display/text configurations including keyboard or TalkBack checks where supported.
  - Criteria: The reviewer can independently rebuild and install an APK, see truthful Android package identity and native host/bridge execution, and exercise a meaningful authenticated task; a PWA or browser responsive preview alone does not qualify. Navigation/back actions, accessible controls, labels, touch/keyboard alternatives, large text and input preservation work on declared profiles, with honest assistive-tool support limits. Runtime-validated boundaries and a plausible modular design separate UI, native plugin and server authority. APP20, proprietary framework or iOS build are never hidden prerequisites.
  - Evidence: User task/acceptance and platform alternatives, lockfile/SDK and reproducible installation commands, Android manifest/package/version and signed-debug artifact hash, native bridge/typed contract source, two-profile emulator/device matrix, actual accessibility/navigation/IME observations and API task trace.

- **APP13-AS2** (required lifecycle survival, local transactional data and migration)
  - Outcomes: APP13-O4, APP13-O5, APP13-O6, APP13-O7, APP13-O9, APP13-O14
  - Work: Implement an actual device-side versioned transactional data store for protected drafts and locally accepted operations, with an atomic pending-intent record and clean account boundaries. Demonstrate Android pause/resume, activity recreation or rotation, **real process termination** and restart separately; save/restore appropriate draft and authenticated navigation without relying on running timers. Seed an older installed database with unsent work, upgrade it to a newer schema and verify migration integrity. Exercise one interrupted local transaction or controlled storage-full/corrupt-record fault and demonstrate justified safe recovery or quarantine, including backup/retention limitations.
  - Criteria: A real installed app survives process removal and returns with correct draft, local accepted command and no cross-account disclosure. The source of offline presentation is persistent, schema versioned and runtime validated; business commands are not silently lost or duplicated on restart. A versioned DB upgrade handles queued records and actual observed constraints, and a failed migration/storage fault yields explicit recovery rather than data deletion. Claims about secure deletion, backup and OS process callbacks remain limited to actual test observations.
  - Evidence: Real local database schema/migration/transaction source and before/after records, interrupted/rotated/process-killed installed app reproduction, pending-operation audit, error/quarantine tests, account-switch denial, backup/retention policy and independent restart results.

- **APP13-AS3** (required offline command replay, authenticated synchronization and conflicts)
  - Outcomes: APP13-O5, APP13-O6, APP13-O7, APP13-O8, APP13-O9, APP13-O11
  - Work: Link the installed mobile client to an actual local authenticated APP3/Fastify/PostgreSQL service with two synthetic principals or device-like clients. Save an offline write and its idempotency/revision metadata locally, cut connectivity, resume, lose an HTTP response **after server commit**, replay and verify one intended durable effect. Generate simultaneous competing edits, an expired session/forbidden queued operation and an obsolete snapshot/delta cursor; recover using current server revision, appropriate conflict decision and a safe authorized refetch. Communicate local accepted, pending, server-confirmed, uncertain, conflicted and denied status accessibly.
  - Criteria: Independent HTTP and PostgreSQL records show that repeated or delayed commands cannot double-apply protected effects or silently overwrite a second authorized edit. The offline queue remains durable across restart, respects per-resource ordering and prevents other accounts from submitting it under wrong identity. Actual session expiry, server-side tenant/action/property authorization and wrong-cursor behavior are enforced beyond UI or local cache checks. App distinguishes local success from confirmed remote outcome and preserves the user's rejected work for meaningful resolution.
  - Evidence: App-local queue and real PostgreSQL/schema versions, two-client accounts, network and lost-ack fault controls, before/after DB and HTTP logs, actual authorization/concurrency negative tests, final reconciled device views and accessible conflict/uncertainty transcript.

- **APP13-AS4** (required device capability permissions, local secrets and mobile threat defense)
  - Outcomes: APP13-O2, APP13-O3, APP13-O4, APP13-O9, APP13-O10, APP13-O12
  - Work: Integrate one justified real emulator/device-supported native capability via a typed plugin or native adapter, such as a system document picker or notification, with task-context explanation, grant/deny/revoke/unavailable behavior and a workable manual fallback. Threat-model loss of local device, untrusted deep-link or URI, intercepted TLS, raw token exposure, plugin input, unsafe backup and another synthetic user accessing cached state. Implement suitable Android Keystore-backed secret management or an independently defensible equivalent, verify real server-held authorization and TLS hostname/certificate checks, and inspect manifest, logs, files and account-scoped data for least privilege.
  - Criteria: Actual supported permission or system-picker lifecycle is observed on an installed Android environment, and denial/cancellation/revocation does not crash the protected task or trigger unexpected private collection. No plaintext long-lived session token lives in unprotected app localStorage, no shipped TLS bypass or hardcoded production credential exists, and untrusted URI/intent input is validated before privileged actions. Backend object/tenant/action/field policy is independently rejected for wrong accounts. Private records/tokens and device capability outputs are not leaked through logs, exported backups, or a fresh user's session within the declared tested scope; unsupported platform details remain qualified.
  - Evidence: Permission and manifest inventory, installed device native bridge grant/deny/limited/revoke traces, fallback UX and accessibility, secret storage/TLS tests, malicious URI and direct backend permission checks, account/logout/backup/log audit, retention policy and residual threat analysis.

- **APP13-AS5** (required background constraints, energy/network budget and real device performance)
  - Outcomes: APP13-O3, APP13-O5, APP13-O7, APP13-O11, APP13-O12, APP13-O13, APP13-O14
  - Work: Design correct foreground/resume synchronization and compare it with documented Android OS-managed deferred/background-work concepts or an optional locally observed native scheduler bridge. Simulate app background, network loss, metered or high-latency conditions, resume and delayed tasks; show durable pending state is not lost or falsely marked completed when the operating system defers work. Measure installed app cold/warm startup and task readiness, actual request/byte counts, CPU/JS/DB delays, memory and documented battery proxies across repeatable profiles, then repair a material high-drain retry, slow query, resource or rendering defect without weakening accessibility or data correctness.
  - Criteria: The design never promises continuous JS execution, exact timer wakeup or guaranteed immediate push delivery after backgrounding. Observed deferral and recovery respect bounded retries, OS/network conditions, expired sessions and actual server truth, with correct user feedback. Before/after measurements include matched test profiles, samples, errors, hardware/emulator limits and maintenance cost; emulator request counts/CPU are not presented as measured physical battery life. A seeded error or expensive loop is traced to cause and corrected with independent functional, security and accessibility regressions.
  - Evidence: OS lifecycle/background policy and supported adapter, foreground/resume and optional scheduled-work logs, controlled network/low-power fault matrix, repeatable startup/network/CPU/memory/DB traces, before/after code and user state checks, proxy energy assumptions and limits.

- **APP13-AS6** (required installed-device quality, versioned release and safe upgrade recovery)
  - Outcomes: APP13-O5, APP13-O6, APP13-O8, APP13-O9, APP13-O13, APP13-O14, APP13-O15, APP13-O16
  - Work: Publish a risk-based layered test suite for TypeScript domain, local transactional DB, real API/postgres, native bridge and actual installed Android UI/lifecycle/permission behavior, with reproducible seeded fixtures and a locally runnable CI-equivalent gate. Produce an inspectable signed-debug or disposable-test-signed APK, manifest, version, build provenance and protected test signing policy; distribute/install **two local candidate versions** to an emulator/device. Preserve existing offline queue and locally protected data across app schema and API changes, seed an upgrade/permission/network regression, demonstrate it fails an independent test and choose safe fix, rollback or forward migration with clear limits. Recheck at least two supported Android profiles and accessibility behavior.
  - Criteria: An independent reviewer can produce a versioned package from fixed source/tool inputs, install/update it and verify package identity without a Play/Apple developer account or uncontrolled production key. Old/new API, queued operation and account boundaries remain valid after migration; rollback is not attempted through an irreversibly migrated local DB if it would corrupt records. A meaningful seeded failure is detected by tests or device evidence before correction and guarded thereafter; CI scripts do not require hidden proprietary cloud runners or secrets. Real test observations are distinguished from simulated staged rollout, public store approval, public code signing and real iOS certification.
  - Evidence: Source/toolchain lock, signed test artifact and metadata digest, manifest and signing-key storage review, versioned app/DB/API compatibility matrix, emulator/device screenshots or logs, failing-before/passing-after tests, deployment channel/release/incident decision and safe user/operator instructions.

- **APP13-AS7** (required integrated offline mobile product and independent technical defense)
  - Outcomes: APP13-O1, APP13-O2, APP13-O3, APP13-O4, APP13-O5, APP13-O6, APP13-O7, APP13-O8, APP13-O9, APP13-O10, APP13-O11, APP13-O12, APP13-O13, APP13-O14, APP13-O15, APP13-O16, APP13-O17
  - Work: Deliver one complete independently reproduced Android-installable, touch-accessible mobile client powered by a TypeScript APP13 architecture, typed device capability, local transactional schema/pending commands and real authenticated APP3/PostgreSQL API. Show lifecycle and permission failure recovery, a true offline write with uncertain acknowledgement and conflict across two clients, secure account isolation, bounded OS-aware synchronization and mobile resource evidence, two device configurations, and a versioned test-signed upgrade preserving user data. Reuse qualifying APP13-AS1–AS6 evidence, not seven disconnected applications. An assessor introduces an **unfamiliar but bounded** permission, crash/restart, offline replay, conflicting edit, local schema or app/server upgrade or performance defect and inspects a real correction/diagnosis, rejected alternatives, authored contributions and remaining limits.
  - Criteria: A fresh reviewer can provision free local Android emulator and backend dependencies, build/install both relevant app revisions, access the actual bridge and protected user task, reproduce negative security, process interruption, conflict and release cases and validate PostgreSQL/mobile-local states without paid store, device farm, Mac or React prerequisite. The learner's new work is attributable and technically explained, including any source reuse, packages and AI assistance. An unfamiliar public-class fault is handled with evidence that data, privacy, accessibility and upgrade compatibility remain safe or unresolved limitations are honestly disclosed. The technical defense is accessible in written, recorded, live or equivalently inspectable form.
  - Evidence: Coherent versioned source, environment and signed artifact identities, two Android test profiles, source and native adapter, migrations/queue/SQL and protected accounts, actual device/permission/lifecycle/network/upgrade traces, correct sync/security regression, performance budget, fault/repair diff, user/operator runbook and accessible independent technical defense.

### Completion, historical revisions and readiness status

APP13 is complete only when independent reviewers accept `APP13-AS1` through `APP13-AS7` and inspect real mobile/client/backend evidence satisfying `APP13-O1` through `APP13-O17`. Passing an in-browser demo, screenshots of a nonexistent device build, mocked local storage, green TypeScript tests, untrusted TLS, insecure queued tokens, lost conflicting writes, inaccessible device permissions or an unverified installed upgrade are insufficient.

Preserve OEE specification and course revision, all applicable outcome/assessment IDs, versioned source/lockfiles and Android package identities, actual device/OS configs, local DB/queued intent and PostgreSQL states, process/permission/network/conflict/upgrade fault traces, security/privacy/accessibility checks, build and signature provenance, recognized platform limitations and independent defense/reviewer decision under [OEE Evidence Rules](../../spec/evidence-rules.md).

APP13 preserves its code/title/`course` identity and optional `elective` status, but migrates from a legacy nine-week APP2 + APP3 checkpoint/final-lab course to outcome-driven OEE `v0.2.0` **draft** with approved direct prerequisites **APP19 + APP3** and provisional 14–18 weeks. All earlier APP13 completion evidence remains attached to its historical assessed revision. This change cannot silently revise APP9, APP14–APP16, OEE Workspace/content mappings, 0xNAND learner evidence or previous course completions. Structural CI does not confer `tested`, `verified`, app-store readiness, actual iOS implementation or official educational conformance.

### Public optional technical references

These are free technical sources for implementation and verification; they introduce no hidden mandatory stack, store or assessment.

- [Capacitor documentation](https://capacitorjs.com/docs) and [Capacitor Android guide](https://capacitorjs.com/docs/android) cover native WebView/bridge, Android packaging and emulator-supported runtime.
- [Capacitor environment setup](https://capacitorjs.com/docs/getting-started/environment-setup) and [iOS guide](https://capacitorjs.com/docs/ios) explain independent Android tooling and macOS/Xcode requirements.
- [Android processes and app lifecycle](https://developer.android.com/guide/components/activities/process-lifecycle) documents Android process termination limits.
- [Android offline-first data](https://developer.android.com/topic/architecture/data-layer/offline-first) and [Android background scheduling](https://developer.android.com/develop/background-work/background-tasks/persistent) explain synchronization and WorkManager constraints.
- [Android build for release](https://developer.android.com/build/build-for-release), [Android command line builds](https://developer.android.com/build/building-cmdline) and [Android bundle testing](https://developer.android.com/guide/app-bundle/test) support APK/install/signing and local update evidence.
- [Android accessibility testing](https://developer.android.com/guide/topics/ui/accessibility/testing), [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) and [OWASP MASVS](https://mas.owasp.org/MASVS/) inform mobile accessibility and application security reviews.
- [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html) supports independently verified mobile synchronization conflicts.
