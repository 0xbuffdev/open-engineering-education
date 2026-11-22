# Curriculum validation tools

The scripts check the current OEE `v0.2.0` course files, program catalogs, and local references. They help contributors find structural errors before review. Passing these checks does not establish course readiness, learner achievement, or educational conformance.

## Program checks

Run the published program validators from the repository root:

```sh
python3 scripts/check-sef-curriculum.py
python3 scripts/check-app-curriculum.py
```

SEF validation checks course metadata, prerequisites, study order and the SEF10 capstone's predecessor requirements. APP validation reads the [APP catalog](../curriculum/APP/README.md) for its course identities, study order, types, classifications, durations and direct prerequisites. It checks missing or duplicate files, prerequisite cycles, graduation closure and local links. A required APP course cannot depend on an elective. The APP script also detects inconsistent Markdown tables as an editorial check; this adds no course completion requirement.

Each published APP and SEF course is checked with the same outcome-based OEE `v0.2.0` structural validator. Unsupported source versions and files without the required outcome/assessment structure fail. There is no alternate format reader, required quiz/lab pattern or final-lab shortcut.

## Course structure

Check one source file:

```sh
python3 scripts/check-outcome-curriculum.py --course curriculum/APP/APP1.md
```

Check every published course:

```sh
python3 scripts/check-outcome-curriculum.py --all --format json
```

The checker verifies declared learning outcomes, module mappings, required summative assessment references and published `Outcomes`, `Work`, `Criteria` and `Evidence` fields. One assessment can support multiple outcomes where its success criteria actually demonstrate each capability. Project courses also require public deliverables and a reviewable technical defense.

Exit code `0` means the inspected source passes structural checks. Code `1` reports a structural violation; code `3` means a source is missing, incomplete or unsupported. JSON diagnostics identify rule IDs and source locations. They are maintenance output, not a published Toolkit export API.

A source may declare `**Specification:** v0.2.0` in metadata. The checker also inspects unmarked sources with recognizable outcome or assessment IDs, so an incomplete current-style file cannot bypass validation. Any explicitly declared unsupported version fails. This detection behavior does not add a normative metadata requirement beyond [Course Format](../spec/course-format.md).

Required assessment fields can be written inline or included through one explicit local public Markdown brief. The checker resolves only safe repository-contained paths. A missing brief or supported source expressed in an unrecognized Markdown layout is reported as incomplete with a diagnostic; the parser cannot certify every possible valid Markdown presentation.

## Inventory and review

The derived [curriculum inventory](../curriculum/INVENTORY.md) reports course/catalog presence, declared versions, structural results and open source review information. Generate a report with:

```sh
python3 scripts/curriculum_inventory.py --output-dir ./inventory-report
```

The [published OEE Toolkit `0.1.0`](https://github.com/0xbuffdev/open-engineering-education/releases/tag/toolkit-v0.1.0) provides deterministic, release-locked course checks and exportVersion 2 for consumers. Maintainers use the repository-local publisher tools with exact Git revisions to inspect and package academic sources. The installed CLI works offline without Git; its importable Python API is not yet promised to be stable. See [Toolkit documentation](../tooling/README.md).

Run the full regression suite and documentation checks:

```sh
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 scripts/check-links
python3 scripts/check-public-docs.py
npx --yes markdownlint-cli2@0.24.0
```

The documentation checks cover local links and references to non-public planning repositories. They do not verify external websites or assess teaching quality.

The current [SEF](../curriculum/SEF/README.md), [APP](../curriculum/APP/README.md), [SYS](../curriculum/SYS/README.md), [AI](../curriculum/AI/README.md) and [SEC](../curriculum/SEC/README.md) catalogs publish their course requirements. Course changes must update the relevant outcomes, assessment criteria, prerequisites and catalog entries together. Use the [curriculum design guide](../curriculum/DESIGN-GUIDE.md) for competency review and the [specification](../spec/README.md) for binding rules. Automated checks do not promote a course beyond its published `draft` status.

The [current curriculum CI workflow](../.github/workflows/outcome-curriculum.yml) requires every published course to pass. The [inventory CI workflow](../.github/workflows/curriculum-inventory.yml) also rejects catalog gaps, missing sources, unsupported formats, and prerequisite inconsistencies. Proposed course files in unmerged branches do not count toward the published inventory.
