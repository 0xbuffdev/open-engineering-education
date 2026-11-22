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

- [x] Signed, merged OEE source commit: `f2afed3e36f6ae0495e2b44a8d9337661defeda1`.
- [x] Exact-selected-commit source validation, Toolkit source readiness,
      independent clean wheel/sdist installation and licensing checks passed
      on Linux/macOS/Windows for `f2afed3e36f6ae0495e2b44a8d9337661defeda1`.
      Exact run URLs recorded below.
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
| Selected package/source commit SHA | `f2afed3e36f6ae0495e2b44a8d9337661defeda1` |
| Proposed Toolkit distribution | `oee-toolkit` `0.1.0` (first stable package candidate) |
| Wheel SHA-256 | `eb20281dea91d16a03d79535d65a7b8b271894a5d7a5988cc2d356c88993ecf6` |
| Sdist SHA-256 | `8eb21f512b4a0e27615b18261b10cd59495f11049a6d141be9e4ae02505d6501` |
| Source-readiness check URL | [Final selected commit: passed](https://github.com/0xbuffdev/open-engineering-education/actions/runs/44959716491) |
| Wheel/sdist install test URL | [Three-platform final build/install: passed](https://github.com/0xbuffdev/open-engineering-education/actions/runs/44959716559) |
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

## First signed-curriculum release procedure

Follow [the official release runbook](RELEASE-PUBLICATION.md). The proposed
first unallocated curriculum CalVer is `2026.11.1`. Its manifest digest,
signed archive, steward public key, and independent publication audit have
**not** yet been created or approved. The new on-demand candidate workflow
builds the full archive byte-identically on Linux/macOS/Windows, then retains
an unsigned candidate without CI-owned persistent signing material.

Do not interpret the verified unsigned package ZIP as an official GitHub
Release, or mistake a build-time disposable Ed25519 test signature for the
steward's production attestation. The checked source SHA remains a valid
explicit release input even if future documentation-only commits advance
`main`; publisher-side signing requires its own recorded source identity.
