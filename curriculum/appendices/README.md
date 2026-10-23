# Appendices

The appendices are the reference layer of the curriculum. They do not add another course; they help you see the whole professional landscape, use the right vocabulary, and behave like an engineer rather than a course collector.

| Appendix | Use it when |
| --- | --- |
| [Professional Practice](professional-practice.md) | You want the working habits, artifacts, and communication standards that turn knowledge into employable judgment. |
| [Coverage Map](coverage-map.md) | You need to see which course covers a topic, what is deliberately out of scope, and where to go deeper. |
| [Glossary](glossary.md) | You meet an unfamiliar term and need a precise working definition plus the course that teaches it. |

## How the appendices fit the curriculum

- A **course file** tells you what to read, build, measure, and prove next.
- The **roadmap** tells you when to take it and what to cut when life happens.
- The **project ladder** turns courses into portfolio evidence.
- The **appendices** explain the professional standard the evidence must meet and expose gaps you may want to fill later.

## The standard in one page

A professional engineer can do five things reliably:

1. **Model the system.** Explain the relevant mechanism, boundary, and failure mode without hand-waving.
2. **Make a prediction.** State what should happen, with units and assumptions, before running the experiment.
3. **Produce evidence.** Build a small artifact, test it, measure it, and preserve the command and environment.
4. **Diagnose a gap.** Compare prediction with observation, isolate the cause, and change the design or the model.
5. **Communicate the result.** Write a short document that another engineer can reproduce and a decision-maker can act on.

If a course artifact does not support those five abilities, it is incomplete regardless of how many chapters you read.

## What "in depth" means here

Depth is not the number of topics you have seen. It means you can descend several levels without losing the thread:

```text
user-visible behaviour
  -> API / protocol
  -> process and memory
  -> syscall / runtime
  -> kernel and hardware
  -> measurement and failure evidence
```

The same rule applies to ML (metric -> data -> model -> training -> serving -> user impact) and security (asset -> trust boundary -> weakness -> exploit path -> control -> residual risk).

Use the [coverage map](coverage-map.md) to check breadth, the [glossary](glossary.md) to keep language precise, and [professional practice](professional-practice.md) to make the work reviewable.
