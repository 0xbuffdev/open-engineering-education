# First official Toolkit and curriculum release decision

The OEE steward authorized preparation and approval of the OEE and Workspace
releases on 2026-11-21, with technical preflight, accurate installation
documentation and tested source artifacts required before publication.

**Decision: release preparation approved; official publication is conditional.**
A GitHub code-review approval is not a signed curriculum attestation,
public signing-key trust decision, or package upload.

The existing OEE `v0.2.0` specification release is separate from the first
official Toolkit wheel/sdist, the immutable signed whole-curriculum CalVer
release and the independent OEE Workspace software version.

## Approved scope

- Preserve the OEE public curriculum and its one Toolkit parser as the
  academic authority.
- Package and test the Toolkit with independently verified wheel/sdist
  contents and a source-free installed consumer.
- Apply the Debian/Ubuntu `ensurepip` portability fix and accurate separate
  source/package readiness reporting.
- After all exact-commit checks and signing policies pass, authorize
  official Toolkit and curriculum publication, then Workspace.
- Finish the existing Content/0xNAND integration after the software
  releases; return to course-resource mapping afterward.

## Required acceptance evidence

- [ ] Signed, merged OEE source commit and its full 40-character SHA.
- [ ] Exact-final-commit source validation, independent Toolkit readiness,
      clean wheel/sdist install and licensing checks on Linux/macOS/Windows,
      with run URLs or separate report artifacts.
- [ ] Verified curriculum source closure, licenses, notices and third-party
      rights; selected CalVer release ID and full manifest SHA-256.
- [ ] Steward-owned Ed25519 private key managed outside the repository, with
      separately trusted public key, attestation, rotation/revocation policy.
      No disposable CI/test key may be substituted.
- [ ] Official Toolkit package and signed curriculum archive published
      with their final digests, then reinstalled and independently verified.
- [ ] Workspace released from its exact passing final commit, under its
      own signed-off release decision record.

## Final decision log

| Item | Recorded value |
| --- | --- |
| Delegated release preparation approval | 2026-11-21 |
| Release source commit SHA | Pending final signed merge |
| Toolkit package/version and file digests | Pending |
| Source-readiness check URL | Pending exact-commit run |
| Wheel/sdist install test URL | Pending exact-commit run |
| Curriculum CalVer and manifest digest | Pending |
| Official steward key and signed attestation | Pending independent approval |
| Publication status | Not published by this PR |
| Academic course status | Unchanged, draft until learner evidence |

The source-only report's `packagedDistributionVerified: false` is expected.
The standalone package-install verifier provides separate evidence.

This record is a delegated, **conditional release authorization**, not a
claim that the missing evidence was produced or that the releases already
exist. Do not tag or distribute official artifacts until the checkboxes are
satisfied and linked to the exact final commits.
