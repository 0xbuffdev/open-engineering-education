# OEE release citation errata

This is a public record of metadata corrections to **published, immutable OEE releases**. Errata document citation mistakes without changing a released tag, commit, or normative educational requirement.

## v0.2.0 — citation metadata recorded under v0.1.0

- **Affected release:** [OEE v0.2.0](https://github.com/0xbuffdev/open-engineering-education/releases/tag/v0.2.0), published **2026-11-07** (UTC).
- **Immutable tag:** `v0.2.0` (annotated tag object `1b34f9ae4ebac4c8b1d58be056a7b329eef5f44b`), pointing to commit `d31cc8ad31dc5779c0499d1d07046e73eb92468e`.
- **Incorrect metadata in the tagged [CITATION.cff](https://github.com/0xbuffdev/open-engineering-education/blob/v0.2.0/CITATION.cff):** `version: "0.1.0"` and `date-released: "2026-10-29"`.
- **Correct citation:** OEE **v0.2.0**, released **2026-11-07**. Those values are already recorded in the [current main-branch CITATION.cff](https://github.com/0xbuffdev/open-engineering-education/blob/main/CITATION.cff).
- **Original tracking and public discussion:** [Issue #46](https://github.com/0xbuffdev/open-engineering-education/issues/46).

**Impact:** A citation generated directly from the `v0.2.0` tag's CFF can incorrectly attribute the release to v0.1.0 and its earlier publication date. This is a **citation-only correction**; it does not assert that any course has been tested, verified, or formally conformant, and it does not modify the contents of the historical release.

**Resolution:** The tag, its annotated tag object, and its target commit remain unchanged. Cite v0.2.0 with the correct date above, or identify the immutable commit when exact provenance is needed. Correct metadata must also be verified from the actual tagged contents of the **next** release before [issue #46](https://github.com/0xbuffdev/open-engineering-education/issues/46) can be closed.

## Release-preparation guard

The repository includes `scripts/check-release-citation.py` and [release citation workflow](../.github/workflows/release-citation.yml). The checker compares the **unindented** `version` and `date-released` scalar values in `CITATION.cff` with the announced `vMAJOR.MINOR.PATCH` tag and the UTC release publication date. It fails on missing, duplicate, malformed, or mismatched fields.

Before **creating a tag or publishing** a new release, set the intended new version and date in `CITATION.cff` on the prospective release commit and run the offline preflight:

```sh
python3 scripts/check-release-citation.py --tag v0.3.0 --published-at 2026-12-01
```

The command above uses **example** future values; substitute the actual intended tag and UTC date. The tag must be created **only after** the tested metadata is committed. Do not reuse or rewrite the already-published `v0.2.0` tag.

The GitHub Actions release workflow also validates the **actual tag checkout** after publication, using the real GitHub release timestamp. A manual workflow dispatch checks an existing tag against a selected announced UTC date. The publication-triggered job is a detection mechanism, not a guarantee that an incorrect release was blocked before publication: run the preflight first. Neither check performs a normative OEE conformance assessment.
