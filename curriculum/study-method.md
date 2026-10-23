# Study Method

The curriculum is build-first for a reason: reading creates familiarity, but only retrieval and construction create competence. This page is the operating manual.

## The four-pass reading method

For each assigned section:

1. **Preview (5 minutes).** Read the headings, figures, and summary. Write three questions you expect the section to answer.
2. **Deep read (30–60 minutes).** Read with a pen. Stop at every mechanism and explain it aloud in one sentence. Mark anything you cannot explain.
3. **Close and reconstruct (15 minutes).** Close the book. Draw the mechanism, write the definition, or derive the result from memory. Then reopen and correct.
4. **Apply (the lab).** Use the idea in code, a measurement, or a proof. If you cannot apply it, you did not understand it.

Do not highlight. Do not copy paragraphs. Write short notes in your own words, with a diagram and one failure case.

## Note format

Every concept note should fit on one screen:

```markdown
# <concept>

## One-sentence mechanism
## Why it exists / what problem it solves
## Diagram or trace
## Prediction before experiment
## Evidence (command, measurement, test)
## Failure modes
## Where I would use it / not use it
## Open question
```

If a note has no prediction or evidence, it is a summary, not a note.

## Problem-solving protocol

For exercises and algorithm problems:

1. Restate the problem in your own words.
2. Write examples, including a boundary case and an invalid case.
3. State a brute-force approach and its complexity.
4. Improve one step at a time; write down why each step is valid.
5. Implement without looking at a solution.
6. Test normal, boundary, and invalid inputs.
7. If stuck for 25 minutes, read one hint, close it, and continue.
8. After solving, write the invariant or proof, the complexity, and one failed approach.
9. Re-solve from scratch after 3 days and after 2 weeks.

A problem you solved with a solution open is not solved. Mark it "learned from solution" and redo it later.

## Lab protocol

Every lab directory must contain:

- `README.md` with question, setup, procedure, results, interpretation, limitation, next experiment;
- runnable source or a script;
- tests or a deterministic check;
- raw results or a command that regenerates them;
- a short note on what surprised you.

Before running, write a prediction. A measurement without a prediction is just a number.

For performance labs, record CPU model, core count, cache sizes, memory, OS, compiler/runtime versions, governor, and command line. If a counter is unavailable, say so; never fabricate it.

## Spaced review

Use a simple schedule:

| When | What |
| --- | --- |
| Same day | 5-minute closed-book recall |
| Day 3 | Re-derive or re-implement the core idea |
| Week 2 | Solve a mixed problem that uses it |
| Month 1 | Explain it to someone or write a one-page summary |
| Month 3 | Use it in a project or revisit the lab |

If you cannot recall it at day 3, the original study was too passive. Re-read the section, then reconstruct again.

## Debugging method

1. Reproduce with the smallest input.
2. State the expected and actual behaviour.
3. Read the error, warning, and stack trace completely.
4. Form one hypothesis at a time.
5. Use the cheapest observation that can falsify it: print, assertion, debugger, log, sanitizer, trace, counter.
6. Fix the root cause, not the symptom.
7. Add a regression test.
8. Write one line: symptom → root cause → fix → prevention.

Never change multiple variables at once. Never "fix" code you do not understand.

## Using books well

- Use the per-book maps in [books/](books/README.md), not the whole PDF.
- One primary book per course. Other books are reference.
- Read the assigned section before the lab that uses it.
- Do the book's exercises selectively; prefer the ones that force a trace or a proof.
- If the edition differs, use section titles and tell your future self in the resource log.
- Page numbers are not authoritative; PDF and printed pages differ.

## Using videos and courses

Videos are useful for intuition, not for proof. Watch at 1.25× only if you pause to reconstruct. For every 30 minutes of video, spend at least 60 minutes building or solving. If a course has no exercises, make your own.

## Using an AI assistant

Allowed:

- explain a concept you already attempted;
- review your code for bugs and missing tests;
- generate test cases or a checklist;
- quiz you closed-book;
- help interpret an error message;
- suggest a smaller experiment.

Not allowed:

- produce a lab or project you cannot explain;
- solve graded exercises for you;
- invent measurements or citations;
- replace reading the assigned section;
- handle secrets, private data, or unauthorized targets.

Rule of thumb: the assistant may write at most 10% of a course lab, and every retained line must be explainable. For exit checks, close it.

## Weekly review (20 minutes)

Answer in writing:

1. What did I build or measure this week?
2. What did I predict correctly, and what surprised me?
3. What is the weakest evidence in my lab?
4. What did I avoid because it was confusing?
5. What is the next smallest deliverable?
6. Did I commit something runnable?
7. Am I sleeping, moving, and seeing people?

If the answer to 1 is "I watched videos", the week does not count as progress.

## Course completion checklist

- [ ] Required reading completed with notes.
- [ ] All core labs runnable from a clean checkout.
- [ ] Exercises completed, including boundary and invalid cases.
- [ ] Project increment committed and linked.
- [ ] Exit check demonstrated without notes.
- [ ] Retrospective names one wrong assumption and the evidence that corrected it.
- [ ] Resource log records editions, versions, hardware, and blockers.
- [ ] Next course prerequisites are genuinely met.

## When you feel lost

Lost usually means one of four things:

1. **The prerequisite is missing.** Go back one course; do not push through.
2. **The section is too dense.** Read a simpler explanation, then return to the primary source.
3. **The lab is too big.** Cut it to one question and one measurement.
4. **You are tired.** Stop. Sleep. The debugger will still be there.

Write the blocker in the course resource log. A named blocker is progress; silent substitution is not.
