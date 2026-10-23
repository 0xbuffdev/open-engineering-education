# D3 — Network & Web Application Security

**Track:** Security · **Prerequisite:** S10, D1 · **Core** · **Time:** 6 weeks, 90 hours · **Project:** P10 secure-review

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../progress.md)

## Purpose

Learn to find, explain, and fix web and network security weaknesses. You will work only on local intentionally vulnerable applications and authorized training platforms, and you will produce developer-actionable reviews rather than payload collections.

## Outcomes

You can:

- map a web request through browser, proxy, server, database, and identity provider;
- explain authentication, session management, authorization, and CSRF;
- identify injection, XSS, SSRF, path traversal, deserialization, and access-control flaws;
- distinguish client-side checks from server-side enforcement;
- use a proxy and browser developer tools safely;
- review source/config for security requirements;
- write and verify fixes with regression tests;
- assess severity from impact and exploitability;
- explain rate limiting, logging, error handling, and secure headers;
- write a review report a developer can act on.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| [OWASP Top 10](https://owasp.org/projects/top-ten/) | Current edition, all categories | Risk taxonomy |
| [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | Level 1–2 selected requirements | Verification standard |
| [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) | Selected test cases | Method |
| *The Web Application Hacker's Handbook* (2nd ed.) | Ch. **1–12** (selected) | Classic web attack/defence model |
| [PortSwigger Web Security Academy](https://portswigger.net/web-security) | Authentication, access control, injection, XSS, CSRF, SSRF, deserialization | Authorized labs |
| [MDN Web Security](https://developer.mozilla.org/en-US/docs/Web/Security) | Same-origin, CSP, cookies, CORS | Browser model |
| [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) | Auth, session, input validation, SQLi, XSS, CSRF, SSRF | Fix patterns |
| B5 *The Linux Programming Interface* | Ch. **56–61** | TCP/IP, sockets, DNS |

## Modules

### 1. HTTP and browser security

- request/response, methods, status codes, headers;
- cookies, `HttpOnly`, `Secure`, `SameSite`;
- same-origin policy and CORS;
- content security policy;
- redirects and URL parsing;
- caching and sensitive data;
- browser storage;
- TLS and certificate validation.

### 2. Identity and session security

- password storage (Argon2id/bcrypt/scrypt);
- MFA and recovery;
- session IDs and rotation;
- login/logout and CSRF;
- OAuth 2.0/OIDC flows and pitfalls;
- JWT claims, alg confusion, expiry;
- authorization models (RBAC/ABAC);
- IDOR and tenant isolation;
- account enumeration and rate limits.

### 3. Injection and input handling

- SQL injection and parameterized queries;
- command injection and argument passing;
- template injection;
- LDAP/XPath/path traversal;
- deserialization;
- file upload;
- XML/XXE;
- output encoding and XSS (stored/reflected/DOM);
- validation versus encoding.

### 4. Server-side request and data exposure

- SSRF and metadata endpoints;
- allowlists and egress controls;
- directory traversal;
- insecure direct object references;
- mass assignment;
- error messages and stack traces;
- secrets in logs/config;
- backup and debug endpoints.

### 5. Secure design and verification

- threat model to test cases;
- security requirements and ASVS mapping;
- secure headers and cookie policy;
- least privilege for database/app users;
- audit logging and monitoring;
- rate limiting and anti-automation;
- regression tests for each fix;
- code review checklist.

### 6. Professional assessment

- scope and authorization;
- proxy setup and evidence capture;
- non-destructive validation;
- severity rationale;
- false positives;
- remediation guidance;
- retest;
- report writing.

## Labs

### Lab 1 — Request anatomy

Use a local proxy and browser dev tools to capture a login, authenticated request, and logout. Diagram cookies, tokens, headers, and server-side checks. Identify one security-relevant assumption.

### Lab 2 — Local vulnerable app

Build or run an intentionally insecure local app under your control. Demonstrate five weakness classes:

- SQL injection;
- stored XSS;
- broken access control/IDOR;
- CSRF;
- SSRF or path traversal.

Use harmless data only. Record request/response evidence, not weaponized payloads.

### Lab 3 — Fix and regression test

Fix each of the five weaknesses at the root cause. Add a test that fails before and passes after. Verify authorization on the server, not just the UI.

### Lab 4 — Authorized academy labs

Complete a small set of PortSwigger Academy labs in the listed categories. For each, write the class, impact, defence, and one test. Do not copy attack payloads into the repository.

### Lab 5 — Secure review report

Review a local service against a subset of ASVS Level 2. Produce findings with evidence, severity, remediation, and retest status. Include at least one non-finding/verified control.

## Exercises

1. Trace a cookie from `Set-Cookie` to an authenticated request.
2. Explain why client-side validation is not a security control.
3. Compare parameterized queries with escaping.
4. Explain stored versus reflected versus DOM XSS.
5. Design a CSRF defence for a cookie-based app.
6. Explain SSRF and one egress control.
7. Identify an IDOR in a supplied API.
8. Explain JWT validation requirements.
9. Write secure headers for a web app.
10. Distinguish a vulnerability from a missing hardening header.

## Project increment — P10 secure-review

Produce:

- a scoped review of a local app you built;
- a request/data-flow diagram;
- five findings with root cause, impact, evidence, fix, and regression test;
- at least three verified controls;
- a retest table;
- a developer-facing summary with residual risk.

**Brief:** [P10 — secure-review](../projects/project-ladder.md#p10--secure-review)

## Exit check

- [ ] demonstrate five weakness classes in a local app;
- [ ] fix each at the server/root-cause layer;
- [ ] show regression tests that fail before and pass after;
- [ ] explain authentication, session, and authorization boundaries;
- [ ] produce a severity rationale without overclaiming;
- [ ] write a retest and residual-risk statement;
- [ ] keep all activity within authorization.

## Common failure modes

- Testing public sites or accounts you do not own.
- Relying on client-side checks.
- Fixing XSS by blocking `<script>` only.
- Confusing authentication with authorization.
- Reporting a scanner output without validation.
- Copying payloads instead of explaining the class and fix.
- Ignoring CSRF because the API "uses JSON".
- Logging secrets or personal data as evidence.

## Evidence to commit

- `labs/security/D3/` with request anatomy, local vulnerable/fixed app, regression tests, academy notes, review report
- P10 secure-review report
- `notes/security/D3/summary.md`

## Optional depth

- *The Tangled Web* (Zalewski).
- *Web Application Security* (Hoffman) selected chapters.
- OWASP Juice Shop and DVWA (local only).
- OAuth 2.0 Security Best Current Practice.
- Browser security model papers and CSP evaluator.
