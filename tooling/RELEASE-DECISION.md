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
| Proposed Toolkit distribution | `oee-toolkit` `0.1.0` (first stable package candidate) |
| Toolkit wheel/sdist file digests | Pending exact final candidate artifacts; do not infer from CI status |
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

## First package candidate preflight

The first independent distribution proposes Python package version
`0.1.0`. This is **not** the OEE specification `v0.1.0` tag.
The package CI preserves the Linux wheel and source archive for 30 days
as a named, unpublished workflow artifact. Linux/macOS/Windows clean
installation and installed Toolkit contract checks still run on all
three platforms. No registry credentials, GitHub Release creation,
package-signing action or automatic release tagging are added.

Record the **new exact merged main SHA**, wheel and sdist SHA-256 values,
the artifact run URL and independently reviewed license/NOTICE.
Publishing from this candidate requires deliberate official artifact
selection. The source-only readiness report and separate wheel/sdist
verifier must both be preserved. A previous green CI result cannot
approve a new stable version commit.
