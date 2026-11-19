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

**Instructional sufficiency:** Seventeen outcomes are developed in fifteen conceptually distinct modules with seven independently required assessments and an accessible defense. Each new Android mechanism needs an intelligible lifecycle/security model, observed installed or worked trace, bounded failure/counterexample, feedback and authentic independent practice before summative judgment. Activity recreation is not process death; an OS picker need not request broad storage permission; Keystore protects keys rather than every database byte; and one APK update succeeds only under compatible package, signing and version constraints. APP19/APP3 foundations are applied without repeating their entire syllabi. Formative investigations do not add unpublished gates. The 14–18-week duration and effort are provisional; source CI does not make learning learner-`tested` or educationally `verified`.

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

1. **Why an installed mobile client differs from mobile web** — Compare the historical native, WebView hybrid, PWA and cross-platform approaches through actual OS lifecycle, storage, permission and release boundaries. Challenge the false assumption that a resized browser page establishes mobile engineering.

2. **One consequential offline and authenticated mobile task** — Choose a bounded field/inventory or educational workflow with two synthetic accounts, server-held action/tenant policy, a locally accepted edit and a state that can conflict after reconnection.

3. **Inquiry provenance and bounded user assumptions** — Use cited mobile usability research or consented observations where available, clearly distinguish synthetic scenarios from real participants, and identify one acceptance assumption an installed-device test could invalidate.

4. **Platform and cost decision without a React prerequisite** — Compare native Android/iOS, TypeScript Capacitor WebView, React Native and PWA on actual install/runtime, offline, native bridge, accessibility, upkeep and local build constraints. Explain APP20 is additional preparation only for an optional React implementation.

5. **Two honest Android configurations, optional iOS analysis** — Select two representative emulator OS/display/text/accessibility settings, state hardware/RAM and supported assistive-tech limits, and compare documented iOS rather than claim unrun iOS device results.

6. **Measurable acceptance and failure contract** — Define actual installed-task completion, denied rights, local-durable versus remote-committed data, forced process interruption, picker/permission denial, readable large-text failure, migration and safe recovery.

*Optional practice — overpromised-platform critique:* Reject an iOS App Store requirement or claim of universal battery life from an Android emulator.

### Module 2 — Toolchain, Packaged Android Runtime and Bridge Contracts

#### Outcomes

- APP13-O2
- APP13-O4
- APP13-O9
- APP13-O14

#### Lessons

1. **Pin a free compatible build and emulator toolchain** — Record actually tested TypeScript/Capacitor/Android SDK/Gradle/JDK/browser combinations, ABI/system image and free reproducible emulator profile, distinguishing version pinning from universal device support.

2. **Android application identity, manifest and bundled code** — Inspect real package/application ID, versionCode, signing configuration, exported components, minimum/target SDK, bundled WebView assets and app sandbox; verify a platform setting by installed inspection.

3. **Build an actually installed, callable app** — Produce a local debug/test-signed APK, install it on an emulator, invoke a meaningful native plugin or OS operation, and compare against a browser-only result that cannot demonstrate process death.

4. **WebView origin, native bridge and app attack surface** — Trace a TypeScript UI call through version-matched Capacitor plugin and Android Activity/URI result, verify origin/navigation and OS permission ownership, and reject untrusted external content reaching privileged bridge actions.

5. **Runtime-validated adapter and Activity-result restoration** — Use a typed bridge wrapper with actual runtime decoding, cancellation and cleanup; for a picker/external Activity, recreate app process and handle supported Capacitor appRestoredResult, rejecting a late result belonging to a previous user.

6. **Trusted local HTTPS, emulator network and backend identity** — Reach a real privately controlled APP3/Fastify service from an Android emulator, inspect trust chain and hostname with local dev CA without shipping insecure cleartext/certificate bypass or assuming localhost points at host.

7. **Equivalent platforms without covert tools** — Explain when additional React/Kotlin/Swift skills, macOS/Xcode, external native APIs or physical hardware would be needed and how to meet published Android-native observations using free supported alternatives.

*Optional practice — installed-protocol check:* Show why bundling a PWA without real Android build, bridge and lifecycle tests is insufficient.

### Module 3 — Touch, Navigation, Assistive Access and Input State

#### Outcomes

- APP13-O1
- APP13-O3
- APP13-O4
- APP13-O14

#### Lessons

1. **Short protected navigation and Android back behavior** — Lay out one actual installed task with meaningful labels, back-button/dismiss and a current authenticated resource, then observe a mistaken back action that loses an unsent draft.

2. **Touch target, gesture alternative and safe confirmation** — Test touch spacing/target and action equivalence with accessibility navigation, and show a destructive confirmation that remains usable without a complex gesture.

3. **System bars, safe areas and installed soft keyboard** — Inspect status/navigation bar, cutout and IME viewport in an actual Android WebView, then repair a form button obscured when the keyboard opens.

4. **IME, rotation and preserved local draft** — Type partially into a real form, change device rotation and keyboard state, and ensure validation, draft and selected field/focus remain meaningful after Activity recreation.

5. **Platform semantics and accessible name/focus** — Inspect actual Android WebView accessibility tree and reading order with labeled controls and error region; a screenshot of a visually apparent label does not prove assistive access.

6. **TalkBack, keyboard and declared tool limits** — Try representative navigation, submit, conflict and denial with available emulator TalkBack/keyboard and explain unsupported hardware/assistive features rather than claim universal WCAG/Android certification.

7. **Large text, reflow and alternative motion** — Test two configured font/display profiles, screen rotation, contrast and reduced-motion settings, comparing how the actual user task survives zoomed text and pending states.

8. **External deep-link intent versus authenticated route** — Open a real inbound route from a crafted untrusted Intent/URI and recheck current session, tenant, object and pending draft before navigating; invalid links fail safely.

*Optional practice — inaccessible permission task:* Repair a touch-only action or invisible error that blocks task completion.

### Module 4 — Typed Mobile Architecture and State Ownership

#### Outcomes

- APP13-O2
- APP13-O4
- APP13-O5
- APP13-O6
- APP13-O9

#### Lessons

1. **Own presentation, persisted domain truth and native effects** — Separate typed user task, local authoritative view and pending intent from remote confirmed DB state, OS bridge and UI; show a test that fails when a screen calls the privileged plugin or server directly.

2. **Transactional repository and queued-command boundary** — Define local account-scoped read view, commit+outbox-style pending command and stable ID through a replaceable real SQLite-capable adapter; distinguish native durability from browser localStorage.

3. **Credential, account and local dataset ownership** — Model current server-held principal and secure credential separately from account display, device-row visibility and queued work; test a late result after identity change.

4. **Inject clock/network/platform failures without mocking away evidence** — Control native plugin response, network and time in formative tests, but identify where independent installed-process/real SQLite/HTTP/PostgreSQL observations are still mandatory.

5. **Error domain with a truthful commit boundary** — Differentiate locally queued, unknown remote outcome, forbidden, conflict, no storage, corruption, canceled picker and unreachable network, checking accessible user messages under each.

6. **Validate old persisted and untrusted native values** — Parse stored/migrated rows and external Activity/URI results at runtime with explicit schema versions, quarantine invalid entries and avoid TypeScript casts as security evidence.

7. **Architecture fitness guard and failing import example** — Introduce a forbidden raw token, direct bridge or SQL/network access from presentation code; let a focused static or runtime dependency test catch it before full Android testing.

*Optional practice — tangled-screen refactor:* Move storage/network/permission handling from an untestable screen handler into owned modules.

### Module 5 — Android Lifecycle and Durable User-State Recovery

#### Outcomes

- APP13-O3
- APP13-O4
- APP13-O5
- APP13-O6
- APP13-O14

#### Lessons

1. **Activity state, process importance and actual Android lifecycle** — Compare activity onPause/onStop and process caching/termination with observed device events; demonstrate why no JS callback is guaranteed at OS-initiated process death.

2. **Activity recreation versus actual process termination** — Test rotation/config change and background process kill as **separate** scenarios using supported emulator/ADB steps, logging exact stop method; persist protected draft and reconstruct safe navigation on cold relaunch.

3. **Paused JavaScript, background policy and false scheduler guarantee** — Record what stops when the WebView is backgrounded and what may be killed under low memory; distinguish Android force-stop from routine system eviction and WorkManager or other deferred work.

4. **Capacitor app events and restored native result** — Observe appStateChange/pause/resume and a supported external Activity return, including an appRestoredResult after process loss; ensure results never attach to an expired session or wrong draft.

5. **Kill between local record and pending instruction** — Stop the installed process before and after a real SQLite transaction, inspecting whether accepted local edit and sync intent commit atomically and recover without duplicate.

6. **Dispose plugin listeners, file handles and network requests** — Repeat background, rotation, logout and process restart and inspect actual OS/bridge/JS listener, open file and pending fetch cleanup without assuming Android always calls cleanup.

7. **Bounded foreground revalidation and queue drain** — On resume, check current principal, revoked device capability, local pending commands and authoritative server revision; drain with finite budget and honest unknown outcome.

*Optional practice — killed-draft recovery:* Repair loss of a protected user draft without exposing it after account switch.

### Module 6 — Local Database, Migrations and Privacy Lifecycle

#### Outcomes

- APP13-O4
- APP13-O5
- APP13-O6
- APP13-O7
- APP13-O9

#### Lessons

1. **Real native persistence as the offline view source** — Implement a transactional SQLite-capable Android repository in an installed app, show its bytes/rows survive process removal, and distinguish device-local view from server authoritative facts.

2. **Account, schema and idempotency constraints in local SQL** — Create per-account data, version, local mutation and queue tables with real foreign/unique constraints, and test a duplicate ID and wrong-account read.

3. **Atomic local edit and pending-command persistence** — Commit user-visible device edit and durable operation ID/base revision/account in the same native transaction; force interruption and confirm either both or neither persisted.

4. **Old-schema upgrade with committed offline intent** — Seed a prior APK/database version and queued changes, interrupt/restart a migration with explicit SQLite transaction or staged recovery, then verify rows and version constraints, not just a successful app launch.

5. **Full storage, corrupt record and retained safe recovery** — Inject a reproducible capacity or malformed record event, preserve accepted work when possible and expose clear quarantine/retry state without blindly deleting the database.

6. **OS backup, credential-key mismatch and retention** — Inspect actual Android backup/data-extraction rules for local sensitive DB and tokens; show that Keystore protects keys but does **not** automatically encrypt every SQLite row or make restored credentials decryptable.

7. **Logout, multiple accounts and surviving intents** — Switch two local synthetic users with already queued commands, purge or safely isolate old account rows/credentials, and prohibit replay of another user's intent under the new bearer.

8. **Logical deletion versus actual backup and remote data** — Trace local row removal, pending queue, backup snapshot, private file and server record retention separately; document what a tested logout/erase path can and cannot guarantee.

*Optional practice — interrupted schema upgrade:* Prove queued edits survive a failed migration or are safely quarantined and explained.

### Module 7 — Offline Queues, Idempotency and Honest Pending UX

#### Outcomes

- APP13-O5
- APP13-O6
- APP13-O7
- APP13-O8
- APP13-O11

#### Lessons

1. **Offline eligibility and mutation risk classification** — Separate safe read-only offline tasks from server-authoritative permission/quota mutations, and define what a local acceptance means while disconnected.

2. **Durable queue with stable owner, fingerprint and base revision** — Persist operation UUID, signed-in principal/tenant/resource, payload hash, base revision and retry state atomically with visible edit, without embedding access tokens in persisted commands.

3. **Connectivity hint is not authenticated server reachability** — Change Android network indicators and backend availability separately, treating even a connected transport/HTTP acceptance as insufficient proof of a committed business effect.

4. **Finite retry and terminal/unauthorized classification** — Compute bounded attempts/backoff/jitter under a controlled schedule; avoid retrying protected commands with expired account rights or blindly resending when outcome is uncertain.

5. **Server commit, lost HTTP response and installed restart** — Use a real APP3/PostgreSQL mutation with a deliberately lost 2xx response, kill/relaunch the client and prove the stable idempotency key yields one server effect after safe replay.

6. **Cancellation before and after uncertain remote commit** — Compare an untransmitted local command with one whose SQL commit may have succeeded, offering an honest reconciliation/compensation option instead of promising deletion undoes it.

7. **Per-resource ordering, conflict and queue fairness** — Schedule two offline edits and a later remote change; prevent a stale operation from overwriting a newer server revision, while rejecting unbounded queue/tenant starvation.

8. **Accessible pending, rejected and current-server review** — Preserve the user's unsent/rejected draft after server denial and display current authorized state and keyboard-usable retry/resolve path without false completed badges.

*Optional practice — duplicate replay failure:* Fix a restarted sync loop that double-applies an accepted database change.

### Module 8 — Multi-Client Reconciliation and Authorized Conflict Handling

#### Outcomes

- APP13-O6
- APP13-O7
- APP13-O8
- APP13-O9
- APP13-O14

#### Lessons

1. **Actual server security, not client account labels** — Use an APP3 authenticated Fastify/PostgreSQL service with independently checked action/object/write-property/tenant permissions; try a forged local user label and inspect denied rows.

2. **Revision and expired data cursor semantics** — Request real current server revision with scoped identity, demonstrate expired history and a permitted full snapshot instead of assuming a mobile cache always catches up.

3. **Two independently authenticated writers and SQL effects** — Schedule two device/test clients against one PostgreSQL resource, inspect actual row constraints/version conflicts and demonstrate current authority regardless of phone clock ordering.

4. **Business merge versus unsafe timestamp overwrite** — Compare protected inventory/entitlement conflict rejection with a defensible independent-field or append-only merge; show why blind last-write-wins discards legitimate work.

5. **Accessible local draft and actual server version** — When conflict arrives after offline edits, preserve original attempted data and authoritative latest record separately, supporting meaningful human choice and no previous-user record flash.

6. **Expired role or session and pending offline writes** — Revoke a test user while queued, require fresh verified credentials/rights before sending, and surface permanently forbidden results without infinite background retries.

7. **Cross-account queue replay and local cache isolation** — Switch A→B with pending A command and server response, observe that B cannot submit, view or sync any prior private command, even with old request finishing late.

8. **Long-offline resnapshot and permission-safe rebase** — Advance server version and expire stored cursor while app offline, then perform authorized full refetch/reconciliation with queue decisions and access revocation correctly enforced.

*Optional practice — silent overwrite diagnosis:* Repair a two-client conflict that had discarded one accepted version.

### Module 9 — Mobile Session, Transport and Local Data Security

#### Outcomes

- APP13-O5
- APP13-O6
- APP13-O8
- APP13-O9
- APP13-O10

#### Lessons

1. **Threat model: stolen device versus live session trust** — Contrast local app sandbox, Keystore-protected key, unencrypted SQLite, exported Intents, cached backup and already valid remote bearer; choose actual scoped mitigations rather than promise security from install signing.

2. **Short-lived credential, refresh, revocation and server policy** — Test session expiry and revoked privileges against actual backend; keep secure key/storage state and local account boundary distinct from UI identity and never let queued intents confer old rights.

3. **Keystore-backed key use and realistic data protection** — Inspect actual native secure-storage plugin provider and where it writes encrypted values; explain Android Keystore key nonexportability is not automatic full local database encryption or trusted logged-in status.

4. **Real hostname/CA trust on installed emulator** — Test successful controlled local HTTPS, bad chain/wrong host failure and absence of debug certificate bypass from the distributable APK; document scoped development trust configuration.

5. **Untrusted deep link and exported Android component** — Launch malicious VIEW intent/unexpected URI and inspect Android exported status, route parsing and current authenticated authorization before opening a protected object.

6. **Remote WebView content, bridge and plugin trust** — Probe navigation allowlist, untrusted plugin result, unsafe javascript invocation and sensitive asset reachability, avoiding a blanket assumption that every native bridge call is safe.

7. **Private rows, backup policy and exposed-screen state** — Inspect sandbox DB, app switcher snapshots where applicable, file exports, Android backup/data-extraction scope and logged-out/second-user access, disclosing untested physical theft protections.

8. **Redacted real crash/HTTP/native error evidence** — Collect one genuine sanitized device/backend diagnostic and confirm credentials, file URIs, private records and high-cardinality account IDs are not inadvertently retained.

*Optional practice — stolen-session scenario:* Revoke a test token and show queue, cache and local secrets honor the new principal.

### Module 10 — Native Device Permissions and Privacy-Safe Capabilities

#### Outcomes

- APP13-O2
- APP13-O3
- APP13-O4
- APP13-O9
- APP13-O10

#### Lessons

1. **Choose a native capability with task justification** — Use one real OS document/photo picker or permissioned notification/camera/sensor bridge supported by the emulator, define exact needed output and non-native fallback before requesting broad access.

2. **Native manifest least privilege and permission semantics** — Inspect installed declared permissions; **Android system photo/document pickers ordinarily need no broad runtime storage permission**. Compare picker cancellation/unavailable/URI-grant cases with actual runtime permission grant/deny/revoke only when the chosen API requires one.

3. **Request in meaningful user context, or don't request** — Open a picker only for a user action or request a justified runtime permission at point of use, explaining data access and allowing continued manual entry after rejection.

4. **Picker result versus permission state and missing capability** — For a permissionless picker test success, cancel, unavailable app and expired/restricted URI; for a permission-requiring capability test supported granted, denied, limited and revoked states without inventing unsupported OS prompts.

5. **Revocation, returned Activity and app process loss** — Change a real platform permission where applicable or revoke a URI permission, kill the process while an external picker Activity is open and inspect supported restored-result callback and current identity before using data.

6. **Typed native result, malicious URI and authority** — Parse result at runtime, constrain content type/size, avoid unrestricted file paths or cross-app URI disclosure, and explicitly check server ownership before uploading a selected item.

7. **Copied private media, lifetime and cleanup** — Access a selected file through scoped URI, copy only what is necessary, bound image/document size and remove temp files on cancel, logout and failed upload, noting lifecycle cleanup may be deferred.

8. **Permissionless alternative and privacy consequence** — Explain what permission/data scope the API actually grants, who may view uploaded content and the deletion/retention path; provide a keyboard/touch accessible manual alternative.

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

1. **Android policy, app process and timer limits** — Demonstrate an installed-backgrounded WebView whose JavaScript is paused/killed, distinguishing observer lifecycle from an OS-guaranteed periodic background job.

2. **WorkManager as conditional deferrable work** — Reason through a constrained one-shot or periodic work schedule and actual Android battery/Doze effects; do not promise exact trigger times or mandate a Kotlin scheduler implementation.

3. **Secure foreground/resume drain that always works within scope** — Revalidate principal and server reachability at resume, bounded-drain durable queued work and report deferral honestly—without requiring paid push or continuous native service.

4. **Optional native job support and observed deferral** — Where a compatible free bridge is available, demonstrate JobScheduler/WorkManager execution with policy constraints and cancellation; otherwise provide a reviewed native schedule/trace without asserting it ran.

5. **Metered/mobile data and low-power task cost** — Throttle sync requests/bytes and classify urgent/optional work under synthetic slow or metered connectivity, maintaining authoritative completed-versus-pending state.

6. **Push/local notification is an invalidation hint** — On receipt validate untrusted notification payload/deep link, refetch authenticated current server state and prevent a notification from announcing committed business success without SQL proof.

7. **Notification permission depends on actual Android API** — If the chosen feature uses Android runtime notification permission, test grant/deny and disabled states; otherwise use in-app status/manual refresh and avoid a fictitious permission gate.

8. **Network/CPU/wake proxies, not physical battery life** — Count actual local retries/bytes/CPU wake opportunities and compare bounded alternatives while labeling emulator power readings as proxies and reporting untested physical energy/OS cases.

*Optional practice — impossible timer promise:* Replace continuous background polling with documented OS-aware, resume-safe reconciliation.

### Module 12 — Mobile Startup, Responsiveness, Memory and Bandwidth

#### Outcomes

- APP13-O3
- APP13-O5
- APP13-O11
- APP13-O13
- APP13-O14

#### Lessons

1. **Installed cold-start, warm-resume and ready-to-task timing** — Measure from explicit process/package state to first usable authorized offline or server-backed task, separating app splash, WebView initialization and real data readiness.

2. **WebView/Android UI long work and input response** — Profile a real slow scroll/input and main-thread/JS/layout delay under fixed installed build, then verify reduced time without losing IME/focus or secure saved edits.

3. **Network and retry byte budget with failure denominator** — Measure payload, number of accepted/failed/retried requests and resumed queue time under constrained emulator link, separating valid task success from merely fewer requests.

4. **On-device SQLite query plans and transaction occupancy** — Use real local data count, EXPLAIN/query plan or equivalent native profiling to repair one slow indexed access without breaking queued-command atomicity.

5. **Retained listeners, decoded images and native handles** — Repeat app navigation/switch/logout and inspect at least one actual growing WebView/OS resource, then correct its lifetime with before/after evidence.

6. **Media size, decode/memory and protected-file correctness** — Resize/cache selected media under declared bounds, measuring bytes/render delay and preserving URI permissions, authorized file lifetime and accessibility.

7. **Two emulator profiles and nonphysical energy claims** — Record CPU ABI, OS/runtime, memory, configuration and trace/tool overhead for both profiles; do not extrapolate general battery life or iOS results from emulator CPU.

8. **Accessible performance regression and measured trade-off** — Repeat important TalkBack/keyboard, large text and offline errors after improvement, and reject a faster app that hides pending data or breaks protected navigation.

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

1. **Risk-based independent Android evidence layers** — Map domain, native SQLite, real HTTP/PostgreSQL, typed plugin, manifest/session, installed UI/lifecycle/accessibility and upgrade risks to distinct independent test oracles.

2. **Two genuinely different installed Android profiles** — Run a documented paired emulator/compatible owned-device matrix with OS version or text/display differences, verifying that missing emulator capability is disclosed rather than fabricated.

3. **Actual installed TalkBack, keyboard and focus faults** — Run permission/offline/IME/conflict task through supported accessibility tools and correct a nonvisual failure with independent before/after observations.

4. **Real network, lost response, Activity and process faults** — Inject separate airplane/backend outage, reply lost post-commit, rotation versus process kill, plugin external Activity result and interrupted local DB migration, recording which steps were truly run.

5. **Native adapter malformed URI/cancel without JS-only mocks** — Trigger malformed/expired URI and canceled picker or supported permission revocation on installed app, inspect independent OS/bridge denial and protected file/database outcome.

6. **Native SQLite and server PostgreSQL independent oracle** — Compare actual device pending rows with remote committed rows for two authentic identities after replay, conflict, migration and logout; UI snapshots alone cannot prove state correctness.

7. **Secret, manifest, backup and signing threat check** — Inspect installed package permissions, Android Keystore-backed storage, backup rules, exported components and redacted logs, confirming denied or unchanged protected state.

8. **Reproducible seeded failure through a local test gate** — Fail an authentic schema/queue/lifecycle/permission/upgrade regression before code correction, rerun unit plus installed-device smoke/SQL and explain CI runner/device access limits.

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

1. **Package identity, SDK levels and device ownership** — Inspect installed applicationId, versionCode/versionName, exported components and min/target API policy, ensuring the same user package is upgraded without uninstall.

2. **Test signing versus production and Play distribution** — Distinguish locally disposable debug/test signing from production signing and Play's app-bundle/rollout policies, with no paid store or professional release certificate requirement.

3. **One stable disposable signer and two build revisions** — Build v1 and v2 APKs with the **same** package ID and compatible signing certificate/lineage and increasing versionCode; document reproducible identity/digest without committing secrets.

4. **Signing custody, dependency source and secret hygiene** — Verify the actual build and plugin provenance, pin tool inputs, use a protected temporary test keystore and ensure credentials/certs are not in source or public CI logs.

5. **Install v1, queue offline work, then update in place** — Create real local SQLite records and pending command under test app v1, install v2 as a signed in-place upgrade **without uninstall/data-clear**, verify schema migration, actor and preserved pending IDs.

6. **Old mobile clients and new backend API coexist** — Run installed old/new versions or client test fixtures against one versioned APP3 schema, probing missing/changed field, expired permission and idempotency behavior before irreversible migration.

7. **Locally staged two-profile regression and remedy** — Test the same signed candidate upgrade in two controlled Android configurations; inject an actual bad schema, permission or routing change with failing-before evidence and fix.

8. **Downgrade refusal, data safety and forward repair** — Attempt a controlled lower-version install only if safe/test-device-specific, explain Android versionCode/signing blocks and why unrecognized migrated SQLite rows require a forward repair rather than a destructive rollback.

*Optional practice — upgrade break and repair:* Fix a release that destroys offline intent and document rollback restrictions and restore evidence.

### Module 15 — One Installed Offline Mobile Product and Independent Defense

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

1. **One real offline-capable Android task and accepted evidence** — Use one coherent APP13 installed app and index separately accepted APP13-AS1–AS6 decisions by source/device/SQL references, distinguishing personally owned implementation from tested prerequisite work without seven duplicate submissions.

2. **Reproduce identity, lifecycle and local-durable synchronization** — From a clean documented free Android/APP3 setup, install the signed package, exercise true app interruption, native capability, real SQLite pending record, lost-ack replay and conflicting authorized PostgreSQL commit with known prior accepted tests.

3. **Safeguard permission, upgrade and two-profile usability** — Reference or selectively rerun accepted native grant/picker cancellation, cross-account secret/URI, Android background/foreground limits, v1→v2 same-signer migration and two supported accessibility/device observations.

4. **Unfamiliar bounded installed-app failure supplied by reviewer** — Accept a fresh lifecycle/picker returned result, revoked URI, private old-account queue, process kill, bad local schema, server conflict, corrupted upgrade or slow-device issue and predict observable client/OS/SQL failure before patching.

5. **Independent before/after correction and regression** — Implement or causally diagnose a real fix, observe failing-before/passing-after installed-client/SQLite/backend/original signature facts, rerun necessary security/accessibility/queue/release regressions and disclose unsupported device claims.

6. **Defend source ownership, evidence and honest platform limits** — Provide equivalent accessible written/recorded/live technical defense of personally explainable TypeScript/native code, reuse and AI assistance, actual Android versus documented iOS behavior, user/privacy/energy costs, backup/signing and bounded evaluation limits.

## Completion requirements

All **APP13-O1–APP13-O17** require seven **independently decidable summative assessments** on one genuine installed Android client with real APP3/PostgreSQL authority: AS1 platform/native accessibility; AS2 lifecycle and native local SQLite; AS3 offline replay and two-client conflicts; AS4 secure local state and permission/picker behavior; AS5 honestly constrained background work and measured mobile resources; AS6 same-signer in-place upgrade and a seeded regression; AS7 **unfamiliar bounded transfer**. Previously accepted AS1–AS6 can be referenced by source/evidence index, never waived or resubmitted as seven unrelated apps. Formative investigations, iOS/store publication and extra native plugins are **not** hidden graduation requirements; this elective is not required for APP9.

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
- **Platform process lifecycle is not an always-on JavaScript worker.** Exercise actual process death **separately** from screen rotation, activity recreation and an ADB force-stop (which has different restart/scheduling semantics). Preserve draft, atomic pending state and supported Capacitor returned external-Activity result without assuming a death callback. Resume-driven authorized bounded sync is sufficient; optional WorkManager/native scheduling is OS-deferrable and no exact timing, constant background JavaScript or automatic push delivery may be promised.
- For private device state, use credible OS-protected token/key handling (e.g., Android Keystore-backed plugin) and declare what is actually encrypted, what is backed up and what is only app-sandboxed. Avoid long-lived plaintext credentials in WebView localStorage, untrusted certificate bypass in distributable builds, sensitive event traces, uncontrolled file URI sharing and session-crossing local caches. Prove backend authorization independently of client checks.
- Choose at least one **genuine device-native capability** supported on an emulator, preferably a system document/photo picker or a justified notification flow. **A system picker commonly requires no broad runtime storage permission**: demonstrate successful selection, cancellation, unavailable capability, constrained/expired URI and app-restored result where supported; do **not** invent an OS grant/deny prompt. If the chosen API actually requests a runtime permission, additionally test supported granted, denied and revoked states. Minimize manifest permissions and provide an accessible fallback; physical sensors or purchased devices cannot be compulsory.
- Protect accessible navigation, tap and gesture alternatives, system keyboard/IME interaction, visible feedback, larger text and screen-reader semantics under both normal and offline/recovery paths. A visually polished mobile frame does not compensate for inaccessible controls or silent pending/conflicting work.
- Qualify local device performance measurement: report startup, CPU/memory/network, SQL, sample counts, emulator/OS profile, error rates and proxy-based energy reasoning. Do not extrapolate actual physical battery life or iOS performance from a desktop browser or single emulator.
- Build and install a **locally test-signed APK** with inspectable version/digest and least-privilege disposable keys. Show a **real in-place Android v1→v2 update without uninstall or data-clear**, retaining the same application ID, a compatible signing certificate and a higher `versionCode`. Retain queued commands/old local schema under actual migration, test previous/current API consumers and explain when downgrade or data rollback is unsafe. Public-store publishing, production signing credentials, online trust and actual rollout statistics are not required or implied.
- Run mobile fault, privacy and security exercises **only on authorized disposable test packages/emulators, synthetic users and locally controlled backend databases**. Do not test on strangers' devices, actual user files, third-party applications or production accounts without authorization.
- A reviewer may select an unfamiliar **bounded** permission, lifecycle, queued sync, conflicted server revision, corrupt/migrating local record, native bridge, upgrade or performance problem. The test must use publicly identified outcome classes and a free accessible evaluation environment. Written, recorded, synchronous or equivalent inspectable defense meets the same content criteria; fabricated teamwork and user research are not required.

### Required summative assessments

- **APP13-AS1** (required mobile architecture, installable client and accessible user task)
  - Outcomes: APP13-O1, APP13-O2, APP13-O3, APP13-O4, APP13-O14
  - Work: Select one meaningful offline-and-authenticated APP3-backed mobile task, justify framework-neutral TypeScript/Capacitor Android versus native/React Native/PWA delivery without hiding APP20 requirements, and produce an **actually installed debug/test-signed APK** with inspected package/manifest/bridge and working server interaction. Demonstrate app navigation, Android back/IME/safe area, touch/keyboard/TalkBack where supported, large text and permission/pending/denied UX on two genuinely different documented emulator/device configurations. Include a worked counterexample where a responsive browser view lacks the necessary native lifecycle/URI or authorization behavior.
  - Criteria: Independent reviewer can clean-build/install the identified Android package and use the real authenticated task and typed native bridge. Two declared Android OS/display/text profiles expose actual accessible navigation/focus/error feedback, with unsupported assistive/hardware observations explicitly qualified. Platform choice, browser/native security surface and source ownership are explained; mock native calls, only a web screenshot, untested iOS claims and compulsory APP20/paid tooling fail. Genuine validated API/native boundaries are observable.
  - Evidence: User task/acceptance and platform alternatives, lockfile/SDK and reproducible installation commands, Android manifest/package/version and signed-debug artifact hash, native bridge/typed contract source, two-profile emulator/device matrix, actual accessibility/navigation/IME observations and API task trace.

- **APP13-AS2** (required lifecycle survival, local transactional data and migration)
  - Outcomes: APP13-O4, APP13-O5, APP13-O6, APP13-O7, APP13-O9, APP13-O14
  - Work: Implement actual account-scoped **native transactional SQLite-capable** persistence and record locally accepted edit+stable pending operation atomically. Reproduce separate Android Activity/rotation recreation, actual background process termination and explicit force-stop behavior where tested, including a supported picker external Activity **appRestoredResult** or an equivalent distinctly labeled scenario. Restart and inspect real local rows/drafts and correct current identity. Seed a prior schema with unsent records, migrate with explicit transaction/recoverability test, and trigger interruption, storage-full or corrupted-row quarantine. Examine Android backup/data-extraction and key scope separately from SQL encryption.
  - Criteria: An installed process truly terminates and restarts with protected data and one valid durable queued intent, without relying on guaranteed JS onStop callbacks. Activity recreation, force-stop and genuine death are not conflated and untested restored-plugin behavior is not claimed. A real local SQLite/constraint/foreign-key migration preserves existing unsent work and isolates other accounts; a failed migration or corrupted data cannot silently erase accepted operations. Keystore-protected credentials do not by themselves prove device SQLite contents encrypted or restorable from backup; evidence names the actual storage, key, account and recovery limits.
  - Evidence: Real local database schema/migration/transaction source and before/after records, interrupted/rotated/process-killed installed app reproduction, pending-operation audit, error/quarantine tests, account-switch denial, backup/retention policy and independent restart results.

- **APP13-AS3** (required offline command replay, authenticated synchronization and conflicts)
  - Outcomes: APP13-O5, APP13-O6, APP13-O7, APP13-O8, APP13-O9, APP13-O11
  - Work: With two actual authenticated identities and APP3/Fastify/PostgreSQL server truth, save an offline protected operation and fingerprint/base revision in real local native storage, interrupt connectivity, restart the app, and **lose the HTTP response after a real server transaction committed**. Replay the same idempotency key, inspect one unique business effect and local pending/unknown/confirmed transitions. Schedule conflicting edits from separate clients and enforce server-side revision/tenant/field policy; also expire one queued user's token, switch account, and recover from obsolete cursor via an authorized current-server snapshot while retaining rejected draft.
  - Criteria: Independent HTTP/SQL/SQLite observations prove no duplicate server effect under response loss/retry, no lost accepted local operation and no silent overwrite across concurrent clients. A disconnected OS signal is not falsely treated as a security exception or known server outcome. Revoked account work cannot be resubmitted as the next user; server authorizes actual object/action/property against current rights. Accessible conflict, offline, unknown-commit and terminal denial reflect true observed states with safe recoverable or manually reviewed work.
  - Evidence: App-local queue and real PostgreSQL/schema versions, two-client accounts, network and lost-ack fault controls, before/after DB and HTTP logs, actual authorization/concurrency negative tests, final reconciled device views and accessible conflict/uncertainty transcript.

- **APP13-AS4** (required device capability permissions, local secrets and mobile threat defense)
  - Outcomes: APP13-O2, APP13-O3, APP13-O4, APP13-O9, APP13-O10, APP13-O12
  - Work: Integrate **one real justified emulator-capable native API** with typed result/permission and user fallback. For an OS document/photo picker, test allowed selection, cancel, missing provider, scoped/expired URI and an external Activity result after process loss where supported—**do not require a storage permission prompt that Android's picker does not issue**. If using a genuinely permissioned capability such as notification/camera, exercise supported requested/granted/denied/revoked states. Inspect manifest, exported deep link, plugin-origin navigation, native secure token storage (Android Keystore-backed or independently defensible equivalent), actual TLS hostname/CA, account-specific SQLite/files/backups/logs and direct backend denied requests.
  - Criteria: Genuine device capability invokes installed Android OS/bridge and can fail or be canceled without breaking accessible protected task; only permission models the selected API actually supports are assessed. A Keystore implementation explains what keys and ciphertext are protected, not a fictitious blanket SQLite encryption or backup guarantee. Untrusted Intents/URI/plugin payloads are checked and no long-lived plaintext token, exported unsafe secret, cross-user queued data, misleading certificate bypass or forbidden server write is observed. Scope, limitations and unavailable emulator features are explicit; no paid hardware is required.
  - Evidence: Permission and manifest inventory, installed device native bridge grant/deny/limited/revoke traces, fallback UX and accessibility, secret storage/TLS tests, malicious URI and direct backend permission checks, account/logout/backup/log audit, retention policy and residual threat analysis.

- **APP13-AS5** (required background constraints, energy/network budget and real device performance)
  - Outcomes: APP13-O3, APP13-O5, APP13-O7, APP13-O11, APP13-O12, APP13-O13, APP13-O14
  - Work: Implement secure **bounded foreground/resume-driven queue reconciliation** on a real installed client under background/resume, long network delay, backend denial, synthetic metered/low-power pressure and OS process eviction. Compare accurately documented WorkManager conditional/deferrable scheduling with optional actual native execution, without requiring a special scheduler or asserting it ran. Treat notifications/deep links as untrusted hints to current authenticated server reads. Repeatedly measure cold/warm usable-task startup, bytes/accepted/retried requests, local SQL latency, CPU/heap and an actual costly retry/slow-query/render bug before/after repair on declared Android profiles, preserving privacy and accessibility.
  - Criteria: The observed client never promises always-on JS, exact periodic execution or response/notification equals SQL commit; pending/uncertain state remains durable and truthful after OS policy deferral and session expiry. A meaningful measured expensive behavior is independently repaired with matched local device/emulator profile, sample/error count, resource and reverified actual SQL/task status. Battery/wakeup estimates are described as proxies, not measured physical energy or iOS performance; no proprietary device farm or paid push is necessary.
  - Evidence: OS lifecycle/background policy and supported adapter, foreground/resume and optional scheduled-work logs, controlled network/low-power fault matrix, repeatable startup/network/CPU/memory/DB traces, before/after code and user state checks, proxy energy assumptions and limits.

- **APP13-AS6** (required installed-device quality, versioned release and safe upgrade recovery)
  - Outcomes: APP13-O5, APP13-O6, APP13-O8, APP13-O9, APP13-O13, APP13-O14, APP13-O15, APP13-O16
  - Work: Implement a risk-based independent test matrix across real local SQLite, APP3 HTTP/PostgreSQL, signed Android bridge, authorization, process/Activity, permission/URI, accessible installed UI and data migration with a meaningful seeded failing-before/passing-after regression. **Install a real v1 APK, save offline accepted work, and install a real v2 APK in place without uninstall/data wipe**, retaining same package identity, compatible disposable test signing certificate and increasing `versionCode`. Inspect signer/artifact digests, manifest/exported permissions and safe test key handling. Verify v2 migration preserves local pending work, old/new backend contract and two Android profiles. Inject a broken upgrade, schema/intent/auth change and justify safe forward repair versus unsafe downgrade or tested reinstall only where allowed.
  - Criteria: A fresh reviewer can build/inspect/install/update versioned signed APKs with a documented free compatible toolchain and **verify the app really upgraded rather than reset its data**. A different signer, changed application ID, untested `versionCode` downgrade or uninstall-and-reinstall is not in-place migration evidence. Actual pre/post installed SQLite and backend user-task, permission and accessibility observations prove retained legitimate pending data and permitted current user. At least one substantive seeded fault fails independently before correction and is protected by repeated tests, while public store release/professional signing/iOS certification are not claimed.
  - Evidence: Source/toolchain lock, signed test artifact and metadata digest, manifest and signing-key storage review, versioned app/DB/API compatibility matrix, emulator/device screenshots or logs, failing-before/passing-after tests, deployment channel/release/incident decision and safe user/operator instructions.

- **APP13-AS7** (required integrated offline mobile product and independent technical defense)
  - Outcomes: APP13-O1, APP13-O2, APP13-O3, APP13-O4, APP13-O5, APP13-O6, APP13-O7, APP13-O8, APP13-O9, APP13-O10, APP13-O11, APP13-O12, APP13-O13, APP13-O14, APP13-O15, APP13-O16, APP13-O17
  - Work: Present **one evolving APP13 Android-installable protected TypeScript client** and **reference individually accepted APP13-AS1–AS6 decisions** by real source/manifest, device, SQLite, HTTP/PostgreSQL and native test evidence, rather than build seven systems or submit entire repeated reports. From a clean documented free local environment reproduce representative installed mobile task, separate process/recreation interruption, account-scoped offline intent, uncertain committed response, two-client conflict, real picker/permission case and v1→v2 same-signer in-place upgrade on two profiles. A reviewer supplies a **previously unseen bounded** session-switch/late Activity result, missing URI, real process termination, lost acknowledgement, outdated revision, schema migration or performance/resource flaw. Predict observable failure, independently capture installed-client/SQLite/HTTP/SQL evidence, implement or defensibly diagnose correction and rerun affected prior invariants with accessible defense of personally owned source and material AI/reuse.
  - Criteria: All six prior APP13 assessments must have independently passing decisions; APP13-AS7 cannot excuse missing AS1–AS6 or create a core APP9 prerequisite. A fresh reviewer can observe real package and native bridge, actual local and remote data/failure outcomes and meaningfully different Android profiles; the unfamiliar correction has failing-before/passing-after independent evidence and maintains privacy, keyboard/assistive feedback, identity and upgrade integrity. OS background scheduling, picker permissions, secure storage and signer compatibility are described accurately and within actual tested scope. No React prerequisite, purchased phone, Mac, paid store, physical battery measurement or fabricated iOS observation is required.
  - Evidence: One versioned APP13 source/Android packages/fixture and **references-first independently accepted APP13-AS1–AS6 evidence index**, actual two-profile installed/Activity/true process and plugin-result traces, native SQLite+APP3 PostgreSQL/idempotency and denied-account evidence, permissionless picker or authentic runtime permission cases, v1→v2 same-signer queued-data migration, newcomer scenario/failing-before/passing-after regression and accessible written/recorded/live source/limitations defense.

### Completion, historical revisions and readiness status

APP13 is complete only when independent reviewers accept `APP13-AS1` through `APP13-AS7` and inspect real mobile/client/backend evidence satisfying `APP13-O1` through `APP13-O17`. Passing an in-browser demo, screenshots of a nonexistent device build, mocked local storage, green TypeScript tests, untrusted TLS, insecure queued tokens, lost conflicting writes, inaccessible device permissions or an unverified installed upgrade are insufficient.

Preserve OEE specification and course revision, all applicable outcome/assessment IDs, versioned source/lockfiles and Android package identities, actual device/OS configs, local DB/queued intent and PostgreSQL states, process/permission/network/conflict/upgrade fault traces, security/privacy/accessibility checks, build and signature provenance, recognized platform limitations and independent defense/reviewer decision under [OEE Evidence Rules](../../spec/evidence-rules.md).

APP13 remains an optional OEE `v0.2.0` `draft` course with APP19 and APP3 direct prerequisites. React/APP20 and public app-store distribution are not required. Completion requires independently reviewable installed Android, offline-data, security, lifecycle, accessibility and upgrade evidence under all seven assessments. Keep evaluated source/specification revisions attached to learner decisions. Structural CI does not certify learner-tested readiness, iOS behavior, accreditation or mobile-store production approval.

### Public optional technical references

These are free technical sources for implementation and verification; they introduce no hidden mandatory stack, store or assessment.

- [Capacitor documentation](https://capacitorjs.com/docs) and [Capacitor Android guide](https://capacitorjs.com/docs/android) cover native WebView/bridge, Android packaging and emulator-supported runtime.
- [Capacitor environment setup](https://capacitorjs.com/docs/getting-started/environment-setup) and [iOS guide](https://capacitorjs.com/docs/ios) explain independent Android tooling and macOS/Xcode requirements.
- [Android processes and app lifecycle](https://developer.android.com/guide/components/activities/process-lifecycle) documents Android process termination limits.
- [Android offline-first data](https://developer.android.com/topic/architecture/data-layer/offline-first) and [Android background scheduling](https://developer.android.com/develop/background-work/background-tasks/persistent) explain synchronization and WorkManager constraints.
- [Android build for release](https://developer.android.com/build/build-for-release), [Android command line builds](https://developer.android.com/build/building-cmdline) and [Android bundle testing](https://developer.android.com/guide/app-bundle/test) support APK/install/signing and local update evidence.
- [Android accessibility testing](https://developer.android.com/guide/topics/ui/accessibility/testing), [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) and [OWASP MASVS](https://mas.owasp.org/MASVS/) inform mobile accessibility and application security reviews.
- [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html) supports independently verified mobile synchronization conflicts.
