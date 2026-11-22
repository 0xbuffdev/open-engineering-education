# Toolkit licensing and provenance boundaries

This document records the **file-level licensing scope** adopted through
[accepted RFC 0002](../rfcs/0002-toolkit-stewardship-and-licensing.md).
The decision was adopted on November 15, 2026. The repository's existing
notices and the applicable licenses of individual contributions remain
authoritative. This clarification does **not** retroactively transfer
copyright or relicense existing contributions.

## MIT: Toolkit implementation and software interfaces

The existing [MIT license](../LICENSE-MIT) covers the original software
implementation and associated software-only metadata in:

- `tooling/oee_toolkit/**/*.py`, including its CLI, immutable Git
  reader, single-parser adapter and derived-export implementation.
- `tooling/oee_toolkit/schemas/*.json` as machine-readable **software
  interface descriptions**, not as a license for curriculum content
  conforming to them.
- `tooling/interop/*.py`, including golden-byte verification and the
  source-drift reporting utility.
- `tooling/interop/fixtures/pins.json` as a software test manifest
  (revision metadata, not republished curriculum text).
- Toolkit-specific Python tests, test harnesses and GitHub Actions
  workflow source, to the extent of the contributors' rights.
- Original software-oriented documentation in `tooling/`, to the
  extent it does not reproduce substantial educational content.

The existing maintenance checker
[`scripts/check-outcome-curriculum.py`](../scripts/check-outcome-curriculum.py)
is MIT-licensed repository maintenance software reused by the Toolkit.
Its historical maintenance callers and any old-format checks **are not
supported Toolkit interfaces**. This decision does not automatically
relicense unrelated third-party materials or change license terms of
historical contributions.

Reproduction or redistribution of the MIT-covered software must
retain the applicable copyright and permission notice as required by
the MIT license.

## CC BY 4.0: Normative and educational material

The existing [CC BY 4.0 license](../LICENSE) continues to apply to
normative `spec/` documents, `rfcs/`, canonical `curriculum/` text,
assessment briefs and substantial educational excerpts reproduced in
tests, examples or generated outputs.

In particular, the following **golden exports are derived from actual
OEE curriculum text** and are treated as **CC BY 4.0**, not as MIT-only
software fixtures:

- `tooling/interop/golden/SEF1.json`
- `tooling/interop/golden/SEF10.json`
- `tooling/interop/golden/APP1.json`
- `tooling/interop/golden/APP17.json`

These exports may contain original outcome descriptions, assessment
work, criteria, evidence and lesson titles. They are **derived
snapshots**, not an alternative editable standard, independent
authored course content or a grant of additional copyright rights.

For reused educational content, attribute:

> Open Engineering Education (OEE), original curriculum and
> specification material © 2026 Christopher S. Aondona, except
> where another rights holder is identified. Steward: 0xBUFF.
> Source: https://github.com/0xbuffdev/open-engineering-education
> License: Creative Commons Attribution 4.0 International (CC BY 4.0).

Keep the original source path and full source Git commit SHA supplied
in the export. Preserve identification and attribution of any other
contributor rights holders. Indicate if the material is modified in
later derivative outputs; a regenerated snapshot is not automatically
endorsed by the original author or steward.

OEE, 0xBUFF and related names are subject to the
[trademark notice](../TRADEMARKS.md); neither MIT nor CC BY conveys
trademark permission.

## Distribution and acceptance boundaries

This licensing decision **does not publish a Toolkit package or release,
approve a conformance program, certify educational requirements, or
change normative course requirements**. The source-repository CLI is
currently independently runnable under `python3 -m tooling.oee_toolkit`
with Python 3.11+ and local Git. Public package names, independent
distribution, a stabilized library API, release versions and notice
bundling require a separate release-readiness review before any official
release is advertised.

Additional code and educational content contributed later remain
subject to their own provenance, contributor rights, applicable
licenses and the project's authentic DCO policy.

For the signed Toolkit `0.1.0` package, consult the [original release decision](RELEASE-DECISION.md) and [publication record](RELEASE-PUBLICATION.md). They identify the audited source and distribution checks. Future versions require a fresh licensing and provenance review; passing source tests or including notices does not by itself establish third-party copyright permissions or authorize publication.
