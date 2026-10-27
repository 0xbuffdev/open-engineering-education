# Contributing

Thank you for considering a contribution. OEE is a standard plus a reference curriculum; contributions land in the free layer, and contributors never need access to anything paid.

## Before you start

- Read the [principles](../spec/principles.md). If your change would violate one of them, it will not be accepted.
- Read the [code of conduct](CODE_OF_CONDUCT.md).
- Search the issues and [RFCs](../rfcs/) first; structural changes already discussed should continue there.

## Developer Certificate of Origin

This project uses a **DCO**, not a CLA. Every commit must carry a `Signed-off-by:` line with your real name and email:

```bash
git commit -s
```

`-s` appends the line automatically. By signing, you certify the statement in [DCO.md](DCO.md). You keep your own copyright; your contribution comes in under the repository's license (CC BY 4.0 for text, MIT for code and scripts). Contributors are listed in [AUTHORS](../AUTHORS).

CI rejects pull requests whose commits are missing the sign-off. If you forget, amend:

```bash
git commit --amend -s --no-edit
```

## What is in scope

| Contribution | Where | Notes |
| --- | --- | --- |
| Chapter-map errors | `curriculum/**` | Cite the edition and the correct section; label `chapter-map-verify`. |
| Lab bugs | `curriculum/**` | Give environment, expected, actual; label `lab-test-case`. |
| Course fixes and clarifications | `curriculum/**` | Keep the structure in [course-format.md](../spec/course-format.md). |
| Spec changes | `spec/**` | RFC first (see below). |
| Templates and scripts | `templates/`, `scripts/` | Must keep working from a clean checkout. |
| Translations | separate directory when the first one lands | Open an issue first so we agree on layout. |
| Typos and broken links | anywhere | Labels `typo`, `link`. |

Good first issues carry these labels: `chapter-map-verify`, `lab-test-case`, `typo`, `link`, `translation`.

## What is out of scope

- **Learner work.** Labs, exercises, notes, projects, and progress logs belong in your own study workspace. Do not open pull requests that add them here; see the scripts in [`../scripts/`](../scripts/).
- **Anything paid or commercial.** Hidden tests, grading harnesses, instructor prompts, pricing, and product marketing do not belong in this repository.
- **Unsolicited new tracks or courses.** Propose structure changes through an RFC; adding a course is a large commitment of reviewer time.
- **Status-label promotions without evidence.** See [status-labels.md](../spec/status-labels.md).

## Proposing a change

1. Open an issue describing the problem (use the matching issue template).
2. For changes to `spec/` or to the required course structure, open an [RFC](../rfcs/README.md) instead and wait for a decision.
3. Fork, branch, commit with `-s`, and open a pull request that links the issue or RFC.
4. Keep pull requests small and explain what changed and why.

## Checks

CI runs the DCO check, an offline link check, and a markdown lint. Run the last two locally before pushing:

```bash
python3 scripts/check-links        # relative links and #anchors resolve
npx --yes markdownlint-cli2        # config in .markdownlint-cli2.jsonc
```

The DCO check is covered by signing your commits with `-s`.

## Review

The steward reviews contributions. Review checks, in order: does it match the principles, is it true, does it link correctly, does it fit the format. Reviews may be slow; silence is not approval.
