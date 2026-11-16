# Synthetic professional dilemma — SEF9-AS8

This case is **entirely fictional** and provides neither legal advice nor authorization to access real personal information. A learner must reason about all of it **without using an AI assistant for the professional decision**, on the *same* CSV-export feature and review evidence already being developed for SEF9.

## Situation A — pressure to ship

A fictional release manager sends this message:

> "We need the CSV feature at today's review. I know the invalid-input test fails and sometimes replaces the existing export, but mark it as passed for now so the board stays green. We can patch after the meeting."

Evidence available: the supplied [seeded implementation](seeded_export.py) and its reproducible failing [contract tests](test_seeded_export.py). There is **no** authorized waiver, real approval or verification of a successful fix.

Make a risk and owner decision with independently tested facts, severity, user harm, a stop/mitigate alternative, an escalation route and a follow-up. A board state or manager pressure does not convert failing evidence to passing results. Assume the organization's actual escalation policy is unknown unless supplied; record that unknown.

## Situation B — licensing and source rights

A fictional contributor suggests copying an apparently useful `fictional-fastcsv-plus` helper from an external snippet into the project. The only accompanying metadata is:

| Field | Evidence |
| --- | --- |
| Claimed package | `fictional-fastcsv-plus` (does **not** refer to an actual published package) |
| Source URL or revision | Not supplied |
| Author/copyright owner | Not supplied |
| SPDX license identifier | Not supplied |
| License text and notice obligations | Not supplied |
| Permission to copy/modify/distribute | **Unknown** |
| Intended use | Copy source into a distributable task-manager CLI |

The fictional contributor says "it's online, so it is open source." This is not evidence of a license grant. Determine a safe present action, what documentation a professional would request, and a rights-preserving alternative. Do not fill missing legal terms with guesses. Optional reading: [SPDX license information](https://spdx.dev/learn/handling-license-info/).

## Situation C — privacy and confidentiality

A fictional customer-support request asks:

> "Paste the raw task export and full debug log in a publicly viewable issue so everyone can reproduce the problem."

Even a task `title` could contain identifying or confidential information. The examples here use only **synthetic** records. Propose a field-level data-flow and retention policy, minimum necessary data for debugging, how errors are logged without exposing records, how temporary files are disposed of, and a replacement issue using synthetic/redacted data. The request does not authorize publishing actual customer information.

## Situation D — accessibility and communication

A reviewer says:

> "The approval board shows the status only as a green or red circle; the reproduction instructions are in a screenshot; the CLI prints 'Error' without saying what failed."

Rework the same feature's review and stakeholder handoff so the report can be understood without color or screenshots, with descriptive headings, explicit expected/actual outcomes, useful textual CLI errors, relevant filenames/line numbers and accessible steps to reproduce. Do **not** claim a verified WCAG conformance level from an untested document. A designated independent reader must genuinely identify and challenge at least one ambiguity and review the resulting edit; this file supplies no fabricated reviewer response.

## Required learner decisions and evidence boundaries

Use a small non-AI professional-risk record, a rights/provenance inventory, a synthetic data-flow/retention map, an accessible stakeholder update, and a truthful mitigation/ownership trail. Independent real reviewer feedback and an actually checked reproduction are required by the published course assessment. The same artifacts may inform other SEF9 assessments; no second application, external service, law-enforcement exercise, real private data or paid license-audit service is required.
