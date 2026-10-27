# Evidence Rules

This file defines what counts as an exit check and what counts as a demonstrable artifact. It is the operational form of principle 1, "Evidence over completion", and it is what the status labels in [status-labels.md](status-labels.md) are measured against.

## What an exit check is

An exit check is a short list of statements a learner **demonstrates without notes** at the end of a course. Each statement must satisfy all of the following:

1. **Observable.** It describes something a third party can watch happen — build it, run it, measure it, explain it on a whiteboard — not a feeling of familiarity.
2. **Decidable.** Someone reading only the linked evidence can tell pass from fail. "Knows about X" fails this test; "traces X through Y and predicts the output" passes it.
3. **Includes a limit.** At least one item requires the learner to state what the artifact does **not** prove.
4. **Not passable by reading.** The answer cannot be looked up in the section it came from.

An exit check is written in the course file. It is not a quiz in this repository; nothing here is auto-graded.

## What a demonstrable artifact is

An artifact demonstrates completion when **all** of these hold:

1. **Committed.** The artifact lives in a commit or public repository the evidence log links to directly.
2. **Runs from a clean checkout.** A stranger can clone it, follow the documented commands, and get the result without undocumented steps, files, or environment state.
3. **Tested where code is involved.** Tests cover normal, boundary, invalid, and failure cases.
4. **Environment recorded.** OS, hardware where it matters, versions, compiler/runtime flags, seeds, and the exact commands used.
5. **Limitations stated.** The README or report says what the result cannot support.
6. **Retrospective included.** One wrong assumption, its evidence, and the change it caused.

## What does not count

- A checked box with no link to an artifact.
- "I read the chapter", "I watched the lecture", "I followed along".
- Output pasted without the command that produced it.
- A demo that runs only on the author's machine, with no reproduction steps.
- A benchmark with no environment, no repetitions, and no variance.
- A claim of completion whose evidence links are broken.

A checked box without a reproducible artifact is not progress. This is the whole rule.

## Where evidence lives

Evidence lives in the learner's **study workspace** — `labs/`, `exercises/`, `notes/`, `projects/`, and `progress.md` — in their own repository. This repository ships only the [templates](../templates/) for that state, including [templates/progress.md](../templates/progress.md).

The evidence log links to committed artifacts. It never records completion as a bare checkbox.

## Evidence and status labels

Evidence is also how courses move between labels (see [status-labels.md](status-labels.md)):

| Promotion | Minimum evidence |
| --- | --- |
| `draft` → `tested` | One learner completed the course; links to their artifacts; a revision note describing what their feedback changed. |
| `tested` → `verified` | Multiple learners completed it; exit check and labs reproduced; chapter maps checked against the cited editions; reviewer sign-off recorded. |

If a promotion's evidence links stop resolving, the label comes down until they are fixed.
