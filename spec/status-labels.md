# Status Labels

OEE uses status labels to communicate how much evidence supports a course's readiness. A status label describes evidence, not popularity, difficulty, prestige, or the confidence of the author.

The only course status labels defined by this specification are `draft`, `tested`, and `verified`.

## 1. Labels and requirements

| Label | Meaning | Required evidence |
| --- | --- | --- |
| `draft` | The course is written but does not yet meet the requirements for `tested`. | A course file that follows the required course format. |
| `tested` | At least one learner has completed the course, and the course has been revised using recorded feedback. | Completion evidence, learner feedback, and a revision note linked to the course. |
| `verified` | At least two learners have completed the course, the exit check and labs have been reproduced or reviewed, and a qualified reviewer has signed off. | Evidence supporting both completions, records of reproduction or review, and reviewer sign-off. |

The detailed promotion requirements are defined in [Evidence Rules](evidence-rules.md).

## 2. Initial status

Every new course MUST begin as `draft`.

A course MUST NOT be labeled `tested` or `verified` until the corresponding evidence requirements have been met and recorded.

A well-written course is not necessarily a tested course. A tested course is not necessarily a verified course.

## 3. Promotion

A course may be promoted only when its evidence supports the higher status.

A promotion MUST:

1. Meet every requirement for the target status.
2. Include links or references to the supporting evidence.
3. Include the required feedback, revision, or review record.
4. Update the course's published status consistently in every required location.
5. Be submitted for review through the repository's normal contribution process.

Elapsed time, author seniority, completion of unrelated courses, or an intention to test the course MUST NOT be used as a substitute for the required evidence.

## 4. Status must remain accurate

A status label MUST be reassessed when significant defects are discovered or required evidence becomes unavailable.

If the evidence no longer supports the current label, the status MUST be lowered to the highest level still supported by the available evidence.

A status correction SHOULD include a brief explanation of the reason for the change and any required follow-up work.

## 5. Where status appears

The status MUST appear in the course metadata.

The course catalog or other authoritative program summary MUST agree with the course file. If the same status is displayed in more than one place, every published value MUST be kept consistent.

A mismatch is a documentation defect and MUST be corrected.

## 6. Status does not imply

A status label is not:

- A ranking of a course's importance or difficulty.
- A guarantee that every learner will achieve the same result.
- Proof that the course covers every topic in its field.
- An accreditation, professional license, or employment guarantee.
- Evidence that a whole program or implementation has the same status.

A course status MUST NOT be used to imply the status of another course or of the repository as a whole.

## 7. Governance

Changes to the meaning or evidence requirements of a status label MUST be proposed through the [RFC process](../rfcs/README.md).

A course author MUST NOT redefine the labels locally or use them with meanings that contradict this specification.
