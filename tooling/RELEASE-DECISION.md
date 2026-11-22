# First official Toolkit and curriculum release decision

The OEE steward authorized preparation and approval of the OEE and Workspace
releases on 2026-11-21, with technical preflight, accurate installation
documentation and tested source artifacts required before publication.

**Release outcome:** OEE Toolkit `0.1.0` and the signed curriculum `2026.11.1` were published on 2026-11-22. The [Toolkit release](https://github.com/0xbuffdev/open-engineering-education/releases/tag/toolkit-v0.1.0) contains the audited wheel and source distribution. The [curriculum release](https://github.com/0xbuffdev/open-engineering-education/releases/tag/curriculum-2026.11.1) contains the archive, detached signature, attestation and public key. The original approval required independent package tests and steward-controlled signing; both were completed before publication.

The OEE `v0.2.0` specification, Python Toolkit `0.1.0`, curriculum `2026.11.1` and OEE Workspace software are versioned separately. Publishing the signed source archive does not change any course's academic status.

## Approved scope

- Preserve the OEE public curriculum and its one Toolkit parser as the
  academic authority.
- Package and test the Toolkit with independently verified wheel/sdist
  contents and a source-free installed consumer.
- Apply the Debian/Ubuntu `ensurepip` portability fix and accurate separate
  source/package readiness reporting.
- Publish Toolkit and curriculum artifacts only after their source, signing and verification checks pass. Complete the independent Workspace release afterward.
- Finish the existing Content/0xNAND integration after the software
  releases; return to course-resource mapping afterward.

## Required acceptance evidence

- [x] Signed, merged OEE source commit: `f2afed3e36f6ae0495e2b44a8d9337661defeda1`.
- [x] Exact-selected-commit source validation, Toolkit source readiness,
      independent clean wheel/sdist installation and licensing checks passed
      on Linux/macOS/Windows for `f2afed3e36f6ae0495e2b44a8d9337661defeda1`.
      Exact run URLs recorded below.
- [x] Complete curriculum source and notices reviewed for the signed
      `2026.11.1` archive. The manifest and archive SHA-256s are recorded below.
- [x] Steward-generated Ed25519 signing key used locally. The public key,
      its independently recorded fingerprint, detached attestation and signature
      are available with the release. The private key remains outside the repository.
      Key recovery, revocation and rotation remain steward responsibilities.
- [x] Both [Toolkit](https://github.com/0xbuffdev/open-engineering-education/releases/tag/toolkit-v0.1.0) and [curriculum](https://github.com/0xbuffdev/open-engineering-education/releases/tag/curriculum-2026.11.1) releases published with the reviewed hashes.
      Local signing, signature verification and offline installation completed
      during the steward's release script, which exited successfully.
- [ ] Workspace released from its exact passing final commit, under its
      own signed-off release decision record.

## Final decision log

| Item | Recorded value |
| --- | --- |
| Delegated release preparation approval | 2026-11-21 |
| Selected package/source commit SHA | `f2afed3e36f6ae0495e2b44a8d9337661defeda1` |
| Published Toolkit distribution | `oee-toolkit` `0.1.0` ([release](https://github.com/0xbuffdev/open-engineering-education/releases/tag/toolkit-v0.1.0)) |
| Wheel SHA-256 | `eb20281dea91d16a03d79535d65a7b8b271894a5d7a5988cc2d356c88993ecf6` |
| Sdist SHA-256 | `8eb21f512b4a0e27615b18261b10cd59495f11049a6d141be9e4ae02505d6501` |
| Source-readiness check URL | [Final selected commit: passed](https://github.com/0xbuffdev/open-engineering-education/actions/runs/44959716491) |
| Wheel/sdist install test URL | [Three-platform final build/install: passed](https://github.com/0xbuffdev/open-engineering-education/actions/runs/44959716559) |
| Curriculum CalVer and manifest digest | `2026.11.1`; `57441494eb69c2ff9cb3f6029c8adc3c6a56f8c6ecabc43196c9b686e5959a6c` |
| Curriculum TAR SHA-256 | `931b30209a2727717af331f4fd46bfc8e637c94c4d1d95d08d6ffeee753c78d2` |
| Steward public-key DER SHA-256 fingerprint | `0cbd8335bf39fab19b17a7bfaa33502d121d007fca4bddd5df0f43a9c814e2ef` |
| Cross-platform unsigned archive comparison | [Four successful jobs](https://github.com/0xbuffdev/open-engineering-education/actions/runs/44997272152) |
| Official steward key and signed attestation | [Published with curriculum](https://github.com/0xbuffdev/open-engineering-education/releases/tag/curriculum-2026.11.1) |
| Publication status | Both releases public since 2026-11-22 |
| Academic course status | Unchanged, draft until learner evidence |

The source-only report's `packagedDistributionVerified: false` is expected.
The standalone package-install verifier provides separate evidence.

The publication decisions above are recorded against exact source and distribution hashes. Follow the same checks for future releases; a successful CI run for this version cannot approve a different package, manifest or signing key.

## Toolkit package evidence

The first Toolkit distribution is Python package version `0.1.0`. Its package tests installed the wheel and source archive on Linux, macOS and Windows. CI preserved the audited files as a workflow artifact, and the steward published them separately to GitHub Releases. The packaging workflow has no registry credentials or automatic publishing step.

The package source commit, per-file hashes and package-test run are recorded in the decision log. Keep the source-only and wheel/sdist verification reports as separate evidence for any future Toolkit release.

## Signed curriculum release evidence

The [release runbook](RELEASE-PUBLICATION.md) explains the signing and publication procedure used for `2026.11.1`. The unsigned curriculum archive was built byte-identically on Linux, macOS and Windows. The steward signed the reviewed archive locally with the production Ed25519 key and published the attestation, signature and approved public key.

The signed release refers to source commit `f2afed3e36f6ae0495e2b44a8d9337661defeda1`; documentation commits after that source snapshot do not change its contents. Consumers must validate the published attestation with the separately trusted public-key fingerprint. CI test keys are never release trust anchors.
