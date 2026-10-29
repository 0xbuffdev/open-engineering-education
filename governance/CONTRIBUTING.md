# Contributing to OEE

Thank you for contributing to Open Engineering Education (OEE). Contributions should improve the specification's clarity, correctness, consistency, or practical use.

By contributing, you agree to follow this repository's governance, licensing, sign-off, and review requirements.

## Before contributing

1. Read the [OEE principles](../spec/principles.md).
2. Review the [Code of Conduct](CODE_OF_CONDUCT.md).
3. Read the [governance policy](GOVERNANCE.md).
4. Search existing issues and [Requests for Comments](../rfcs/README.md) to check whether the proposed change has already been discussed.

For a small correction, open a pull request. For a change to the normative specification or its governance, follow the RFC process first.

## Developer Certificate of Origin

This project uses the Developer Certificate of Origin (DCO), rather than a Contributor License Agreement.

Every commit submitted for review MUST include a `Signed-off-by:` line confirming that the contributor has the right to submit the change under the applicable license.

Create a signed commit with:

```bash
git commit -s
````

A sign-off looks like this:

```
Signed-off-by: Jane Doe <jane@example.com>
```

Use your own name and email address. Do not add a sign-off on behalf of someone who has not made the required certification.

Read the [DCO policy](https://DCO.md?utm_source=chatgpt.com) for the complete terms.

Contributors retain their copyright. Contributions are submitted under the applicable repository license; the sign-off does not transfer ownership to the steward.

## What you can contribute

| Contribution                | Area                               | Expectations                                                        |
| --------------------------- | ---------------------------------- | ------------------------------------------------------------------- |
| Specification clarification | `spec/`                            | Follow the RFC process for normative changes.                       |
| Documentation corrections   | Markdown files                     | Preserve meaning, consistency, and correct attribution.             |
| Course improvements         | `curriculum/`                      | Follow the current course format and assessment requirements.       |
| Template improvements       | `templates/`                       | Keep generated workspace files clear and usable.                    |
| Script improvements         | `scripts/`                         | Include appropriate error handling and validation.                  |
| Governance changes          | `governance/`                      | Follow the RFC process where policy changes are involved.           |
| Repository automation       | `.github/` and configuration files | Explain the behavior being changed and validate it where practical. |
| Bug reports                 | Relevant area                      | Include a reproducible example and expected versus actual behavior. |

Small spelling, grammar, formatting, and broken-link fixes generally do not require an RFC unless they change the meaning of a normative requirement.

## Changes that require an RFC

Submit an RFC before proposing changes that affect:

- The principles or normative requirements in `spec/`.
- Required course structure, assessment rules, or completion requirements.
- The meaning or evidence requirements of course status labels.
- The conformance criteria.
- Licensing, contributor obligations, or governance policy.
- The scope of the public specification or its relationship with implementations.
- Repository-wide structural decisions.

The RFC guide explains the proposal and decision process.

A pull request MUST link to the relevant RFC when it implements an accepted normative change.

## Quality expectations

Contributions MUST:

- Be clear, accurate, and consistent with the applicable specification version.
- Use stable terminology and identifiers.
- Avoid unsupported claims about readiness, conformance, or outcomes.
- Preserve appropriate copyright and attribution notices.
- Use working internal links.
- Keep changes focused and explain why they are needed.
- Avoid committing credentials, private learner information, or unrelated generated data.

Changes to scripts or executable code SHOULD include tests or clear verification instructions appropriate to the change.

## Local validation

Run the repository's available checks before submitting:

```
python3 scripts/check-links
npx --yes markdownlint-cli2
```

Run both commands from the repository root. If a check cannot be completed, explain why and identify any remaining validation work in the pull request.

## Proposing a change

1. Open or identify an issue describing the problem.
2. If the change requires an RFC, submit the proposal and wait for a decision.
3. Create a focused branch from the current base branch.
4. Make the change and validate it locally.
5. Sign off each commit using `git commit -s`.
6. Open a pull request describing the problem, the change, the checks performed, and any remaining limitations.
7. Link the issue and any accepted RFC that the change implements.

Do not treat silence as approval. A normative change is not accepted until the designated decision-maker records the decision.

## Review and decisions

Reviewers assess whether a contribution:

1. Follows the principles and applicable normative requirements.
2. Is technically and factually correct.
3. Is clear and maintainable.
4. Uses valid links and consistent identifiers.
5. Includes appropriate evidence or validation.
6. Respects licensing, attribution, and privacy requirements.

A review may request changes, reject the proposal, or identify unresolved questions. Review decisions should explain material objections and the conditions for acceptance where practical.

## Out of scope

The following do not belong in this repository:

- Personal learner workspaces or private progress records.
- Secrets, credentials, or private learner data.
- Commercial product marketing and private implementation details.
- Changes that silently redefine normative requirements.
- Status promotions that lack the evidence required by the specification.
- Contributions for which the submitter cannot establish the right to submit the work under the applicable license.

For questions about scope or procedure, open an issue before investing in a large change.