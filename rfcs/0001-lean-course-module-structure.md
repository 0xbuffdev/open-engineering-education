# RFC: A lean course and module structure

- **Status:** `draft`
- **Author:** OEE curriculum contributors
- **Created:** 2026-11-05
- **Last updated:** 2026-11-05
- **Related issue:** none
- **Affected specification version:** `draft`

## 1. Summary

Replace the twelve mandatory course section headings and repeated course/module brief fields with four required course sections: **Overview**, **Learning outcomes**, **Modules**, and **Completion requirements**. Keep concise course metadata. Every module describes only **Outcomes** and **Lessons**, with a clearly ordered list of instructional lessons, tests and labs. Preserve all current educational and evidence obligations, but place each obligation where it is taught, assessed or completed rather than repeating it under multiple headings.

## 2. Problem

The draft SEF course files repeat a course overview in a `Course brief`, then repeat individual module introductions, history, applications and key concepts in `Module brief` blocks. Separate `Topics`, `Small exercises`, `Practical exercises`, `Course lab` and `Exit check` sections then restate work already associated with lessons and assessments. Learners and course authors must navigate repetitive documents, and the duplicated material risks diverging. The existing course-format rule that every course end with a **lab-only module** forces an unnecessary extra module when the last teaching module can culminate naturally in the integration lab.

## 3. Proposed change

### A. Keep only essential course metadata

Require a course title and stable code when assigned; program association where applicable; type (`course` or `project`); prerequisites (course links or `none`); duration in weeks; and lifecycle status. A workload estimate is optional. An overview describes the purpose and relevance of the course without an additional seven-field `Course brief`. Detailed prior knowledge may be explained briefly in the overview, without a redundant prerequisite heading.

### B. Four required sections

1. **Overview:** Scope, purpose and practical relevance; no repeated orientation template.
2. **Learning outcomes:** Observable, evaluable course capabilities.
3. **Modules:** Ordered modules. Every module contains only **Outcomes** and **Lessons**. Lessons identify their type and relevant instructional or assessment requirements.
4. **Completion requirements:** Required checkpoints, exercises, final lab, evaluation, deliverables, retrospective and evidence. Content may be linked to a detailed, publicly accessible exercise or lab brief instead of duplicated.

Course authors may add sections when necessary, but the standard does not mandate duplicate headings for information already expressed in the canonical place. A list of topics is optional and should not repeat a lesson sequence.

### C. Explicit lesson kinds and placement

Lesson entries use `lesson`, `test` and `lab`. Educational explanations and optional contextual material (history, applications, strengths, limitations and terminology) belong in appropriate lesson content, not repeated in course metadata or mandatory module briefs. The course orientation is normally the first lesson of Module 1. Course documentation may link to lesson guidance or public lesson notes; implementers may provide deeper instructional content.

Where a module includes a test and micro-lab, instructional lessons precede the test, and the test precedes the lab. Tests are included when needed to evaluate outcomes rather than to satisfy positional conventions. Every course MUST culminate in a final integrated `lab` lesson as the final lesson of its final module, **without requiring a separate lab-only module**.

### D. Preserve assessment and evidence rigor

The proposed simplification does not weaken `spec/evidence-rules.md`: assessments still identify outcomes and success criteria; lab requirements still cover objective, prerequisites, environment, procedure, expected result, verification, evidence and failure analysis. These may be specified in a linked public lab brief. Course completion still requires applicable conceptual checkpoints, exercises, final integrated lab, tests, explanations, reproducibility, retained evidence and a technical retrospective. Project courses still require project deliverables, evaluation and defense.

### Illustrative format

```markdown
# SEF1 — Demystifying the Computer System

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** none
**Duration:** 4 weeks
**Status:** `draft`

## Overview

Build an inspectable computer model from bits through program execution.

## Learning outcomes

- Explain how a computer executes stored instructions.

## Modules

### Module 1 — Inside the Machine

#### Outcomes

- Explain and model binary states, bits and bytes.

#### Lessons

1. **Course orientation** — `lesson`
2. **Bits and two-state systems** — `lesson`
3. **Bits and bytes checkpoint** — `test`
4. **Model a byte** — `lab`

### Module 2 — Codes and addresses

#### Outcomes

- Demonstrate how bit patterns can be interpreted as values and locations.

#### Lessons

1. **Encoding values** — `lesson`
2. **Decoding checkpoint** — `test`
3. **Integration lab** — `lab`

## Completion requirements

- Pass the required checkpoints and complete practical exercises.
- Complete the integration lab using publicly specified requirements.
- Record verification results and a meaningful technical retrospective.
- Retain reproducible evidence as required by the evidence rules.
```

The example illustrates structure only and is not a replacement for the full SEF1 course definition.

### E. Proposed normative edit targets

- `spec/course-format.md` sections 1–4: replace mandatory section list and final lab-only module requirement; specify lean module contract.
- `spec/course-format.md` sections 5–9: retain outcome coverage, lab procedures, evidence and consistency requirements; allow references to publicly accessible briefs rather than repeated sections.
- `spec/conformance.md`: align checks with required information rather than twelve headings, if needed.
- Existing curriculum and validation scripts: update when the format is accepted. This RFC itself does not change normative requirements.

## 4. Alternatives considered

| Alternative | Advantages | Disadvantages | Decision |
| --- | --- | --- | --- |
| Retain 12 headings and all module briefs | No migration | Repetition and artificial structure | Reject |
| Use unstructured narrative prose | Flexible | Hard to validate and consume programmatically | Reject |
| Four sections and two module subsections | Lean, predictable, reviewable | Requires migration and validator updates | Propose |

## 5. Impact assessment

### Existing courses and programs

SEF1–SEF10 on the import branch are the first migration candidates; the other programs should adopt the approved shape when split. Program names, course codes and durations remain stable unless separately reviewed.

### Implementations

0xNAND can display a first lesson as course orientation and generate module navigation from the same ordering. OEE Workspace can derive independent study plans without needing proprietary content. Neither needs duplicated course/module briefs. Required lab and exercise assignments must remain publicly accessible.

### Evidence and status labels

No changes. Draft, tested and verified continue to require the existing evidence. An import-integrity check alone cannot promote course status.

### Conformance

Course format checks must be updated after acceptance. Until a specification change is merged, draft examples may be nonconforming under the existing twelve-section rule and MUST NOT be described as conforming.

### Licensing and governance

No proposed changes to licensing, attribution or steward authority. This normative change requires the established RFC decision.

## 6. Compatibility and transition

This proposal is intentionally not backward-compatible with checks requiring twelve separate headings or a dedicated final lab module. Transition in order: accept RFC; update normative format and conformance checks in a separate implementation PR; migrate SEF as draft; apply the resulting format to APP, SYS, AI and SEC; update content and workspace consumers. Preserve the old source and resource mappings until downstream migration succeeds.

## 7. Risks and mitigations

| Risk | Assessment | Mitigation |
| --- | --- | --- |
| Hidden lab/assessment requirements after headings are removed | High | Require explicit, linked public briefs and validate required fields |
| Lost historical or instructional context | Medium | Move source brief material into optional lesson-authoring notes before deletion |
| Inconsistent downstream course parsing | High | Version the contract and update consumers after RFC acceptance |
| Exercises no longer mapped to outcomes | Medium | Preserve assessment traceability; add curriculum-level reviews |

## 8. Validation plan

Review at least SEF1 (integrated final-module lab), SEF4 (standalone lab-only module), and SEF10 (project capstone). Verify that each displays no required Course brief or Module brief sections; each module has outcomes and ordered typed lessons; all labs, exercises, assessments, exit criteria and evidence requirements remain traceable; and the final lab is the final lesson. Run link, metadata, prerequisite and Markdown lint checks. Perform a separate educational review before changing `draft` status.

## 9. Open questions

1. Should lab details be nested directly under the `lab` lesson or housed in separate public lab briefs when substantial?
2. Should course/module orientation be required as a specific first lesson, or recommended unless a course's first lesson already orients learners?
3. Should prerequisite readiness information be permitted as a brief overview sentence, or require a dedicated structured metadata field?

## 10. Decision

- **Decision:** Pending
- **Decision date:** `pending`
- **Decision-maker:** OEE steward
- **Rationale:** Pending discussion
- **Conditions:** Pending
- **Implementation pull request:** `pending`
