# Curriculum inventory

Each relevant pull request and change to `main` produces a derived inventory of published course sources and structural checks. Course definitions and program catalogs in this repository remain authoritative. This page explains the report; it does not maintain a second curriculum registry.

- [Inventory workflow and run history](https://github.com/0xbuffdev/open-engineering-education/actions/workflows/curriculum-inventory.yml)
- Each run contains the complete per-course matrix in the **job summary** and downloadable `inventory.md` and `inventory.json` artifacts.
- The report is tied to an exact 40-character source commit SHA. Existing source files identify their paths at that commit. Pending PRs are annotated separately, with their head SHAs, and **are not treated as merged curriculum**.

## Reproduce locally

From the OEE repository checkout:

```sh
python3 -m unittest discover -s tests -p 'test_curriculum_inventory.py' -v
python3 scripts/curriculum_inventory.py --output-dir ./inventory-report
```

The second command is offline and records `pr_scan: not_requested`. To include live public review branches, run:

```sh
GITHUB_TOKEN=<your-read-only-token> python3 scripts/curriculum_inventory.py \
  --include-open-prs --output-dir ./inventory-report
```

The token is optional for public GitHub repositories, but recommended to avoid anonymous API rate limits. The workflow supplies a read-only GitHub Actions token. PR discovery is opt-in and fails visibly if the API cannot be reached; it never silently treats an incomplete scan as complete.

## Read the report

- `v0.2.0` identifies a source that declares the current outcome-driven format. The separate structural result shows whether its validation passed. Neither result establishes educational conformance.
- Sources without the current outcome and summative assessment structure are reported as unsupported. They cannot pass the present course checks or count as completed course definitions.
- `unsupported` is a declared unknown version or conflicting format signal. `missing` and `pending_pr_unreviewed` identify absent source, with the latter explicitly linked to an open PR.
- Course/curriculum catalog discrepancies, absent prerequisites, prerequisite cycles, missing summative coverage and required project defense indicators are audit findings for human review.
- An absent program course table is a catalog gap even if the repository-wide overview declares expected courses. A source course without a catalog row remains **unlisted**, not automatically adopted.
- `editorial_review` and `learner_validation` remain `not_established`. The published `draft`/`tested`/`verified` status is copied from source, never promoted by this report.

## Scope and authority

This inventory is a repository-maintenance report, not a Toolkit course export or an assessment of educational quality. It uses the existing `course_format_versions.py` classifier and `check-outcome-curriculum.py` structural validator to report the state of published course files. It does not define curriculum requirements, grade learner work, or establish course readiness or conformance.

Regenerate the report for the source commit you need. Curriculum and readiness decisions require review of the course files and their supporting evidence under [OEE governance](../GOVERNANCE.md); generated reports do not replace that review.
