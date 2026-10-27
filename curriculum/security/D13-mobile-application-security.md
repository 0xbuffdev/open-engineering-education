# D13 — Mobile Application Security

**Track:** Security · **Prerequisite:** D3 · **Elective** · **Time:** 4 weeks, 60 hours · **Project:** elective
**Status:** `draft` · [status labels](../../spec/status-labels.md)

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../templates/progress.md)

## Purpose

Assess Android and iOS apps for data protection, authentication, transport security, platform misuse, and reverse-engineering resistance. Work on your own apps, intentionally vulnerable training apps, or apps you are authorized to test.

## Outcomes

You can:

- explain the Android/iOS app sandbox and permission model;
- inspect an APK/IPA safely;
- test local storage, logs, backups, and keychain/keystore use;
- verify TLS and certificate handling;
- assess authentication/session and deep-link handling;
- identify exported components and intent/IPC risks;
- use dynamic instrumentation in an authorized lab;
- distinguish client-side controls from server enforcement;
- write a mobile assessment with remediation;
- respect app-store, privacy, and anti-circumvention rules.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| [OWASP MASVS](https://mas.owasp.org/MASVS/) | Full | Security verification standard |
| [OWASP MASTG](https://mas.owasp.org/MASTG/) | Platform and resilience tests | Method |
| [Android security docs](https://developer.android.com/privacy-and-security/security-tips) | Permissions, storage, network, components | Platform model |
| [Apple Platform Security](https://support.apple.com/guide/security/welcome/web) | Sandbox, keychain, code signing | Platform model |
| [Android security best practices](https://developer.android.com/privacy-and-security/security-best-practices) | Full | Defence |
| [iOS security best practices](https://developer.apple.com/documentation/security) | Selected | Defence |
| [Frida docs](https://frida.re/docs/home/) | Basics, instrumentation | Dynamic analysis (authorized) |
| [MobSF docs](https://mobsf.github.io/docs/) | Static/dynamic analysis | Triage |

## Modules

### 1. Platform model

- app sandbox and UID;
- permissions and runtime consent;
- code signing and provisioning;
- Android components (Activity, Service, Receiver, Provider);
- iOS app extensions and URL schemes;
- keychain/keystore;
- backup and data extraction;
- platform version differences.

### 2. Static analysis

- APK/IPA structure;
- manifest/Info.plist;
- permissions and exported components;
- hardcoded secrets and endpoints;
- insecure storage APIs;
- WebView configuration;
- native libraries;
- obfuscation/packing indicators;
- dependency and SDK risk.

### 3. Dynamic analysis

- emulator/device setup and isolation;
- logs and crashes;
- file system inspection;
- network interception with a test CA;
- TLS pinning (concept and authorized bypass);
- runtime instrumentation;
- authentication/session flows;
- deep links and intents;
- data leakage.

### 4. Controls and verification

- secure storage and key management;
- certificate validation/pinning;
- authentication and biometrics;
- authorization enforced server-side;
- input validation and WebView safety;
- screenshot/clipboard protections (and limits);
- root/jailbreak detection (and limits);
- privacy and analytics;
- MASVS mapping.

### 5. Reporting

- scope and authorization;
- evidence without private data;
- severity and exploitability;
- client vs server fixes;
- retest;
- app-store/privacy constraints;
- responsible disclosure.

## Labs

### Lab 1 — Static triage

Inspect an intentionally vulnerable training APK or your own app. List permissions, exported components, hardcoded endpoints, and storage APIs. Verify one finding manually.

### Lab 2 — Local storage and logs

Test shared preferences/UserDefaults, SQLite, files, logs, backups, and keystore/keychain use in a local app. Demonstrate one data-at-rest weakness and a fix.

### Lab 3 — Transport security

Proxy a local app through a test CA. Determine whether TLS validation/pinning is effective. Test a certificate mismatch. Use only a test app and test credentials.

### Lab 4 — Component/deep-link test

Test an exported Android component or iOS URL scheme in a local app. Demonstrate an authorization or input-validation failure, then fix it at the appropriate layer.

### Lab 5 — MASVS review

Assess the app against a subset of MASVS. Produce findings, verified controls, remediation, and retest. Include one limitation of client-side hardening.

## Exercises

1. Explain the app sandbox.
2. Compare Android keystore and iOS keychain.
3. Identify an exported-component risk.
4. Explain certificate pinning and its limits.
5. Test a deep link for input validation.
6. Distinguish client-side and server-side authorization.
7. Explain backup-related data exposure.
8. Identify a WebView risk.
9. Map a finding to MASVS.
10. State what root detection does not provide.

## Project increment (optional)

Assess an app you built on a local emulator against a small MASVS/MASTG checklist. Produce sanitized findings, fix at least one issue, and add a regression or verification step. Do not test an app you do not own. This is an elective extension to P11/C4, not a new ladder project.

## Exit check

- [ ] inspect an app statically and validate a finding;
- [ ] demonstrate a storage or transport weakness in a local app;
- [ ] test one component/deep-link boundary;
- [ ] fix at the correct layer and add a regression check;
- [ ] map findings to MASVS;
- [ ] write a report with privacy-safe evidence;
- [ ] state client-side hardening limits.

## Common failure modes

- Testing apps you do not own or have authorization for.
- Bypassing pinning on a production app without permission.
- Storing real credentials/tokens in evidence.
- Treating root detection as a security boundary.
- Assuming HTTPS means the app validates certificates.
- Fixing only the client when the server is authoritative.
- Ignoring backups and logs.
- Publishing extracted proprietary code.

## Evidence to commit

- `labs/security/D13/` with static triage, storage/transport tests, component test, MASVS review
- `notes/security/D13/summary.md`
- authorization and test-app provenance record

## Optional depth

- *The Mobile Application Hacker's Handbook* (Chell et al.).
- *Android Hacker's Handbook* (Drake et al.).
- *iOS Hacker's Handbook* (Miller et al.).
- Android/iOS platform security whitepapers.
- Mobile app privacy and accessibility guidance.
