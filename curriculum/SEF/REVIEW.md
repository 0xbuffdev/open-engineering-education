# SEF Curriculum Coverage Review

> [Software Engineering Foundations](README.md) · [Course Format](../../spec/course-format.md) · [Evidence Rules](../../spec/evidence-rules.md)

## Scope

This report documents the initial **depth audit and draft expansion** of all ten SEF courses. It is a curriculum-design review, not evidence that the courses have been learner-tested, independently reproduced or professionally certified.

Unlike the initial APP import, SEF already had variable module and lesson counts. The main depth risks were concentrated in SEF4 (algorithms), SEF5 (engineering practice), SEF7 (Unix interfaces) and SEF8 (mathematics). These courses received the largest changes. The other six received targeted new modules where their scope justified them.

We retained the existing course codes, basic prerequisite graph, original teaching topics and capstone requirement. New lessons isolate significant mechanisms rather than adding a test or lab merely to satisfy a pattern. Every course remains `draft`.

## Course-by-course coverage

| Course | Original modules | Revised modules | Main additions | Priority verification |
| --- | ---: | ---: | --- | --- |
| [SEF1](SEF1.md) — Demystifying the Computer System | 8 | 10 | Instruction encoding, processor control, boot and device boundaries | Validate gate/circuit simulation and tiny ISA assumptions |
| [SEF2](SEF2.md) — Programming & Computational Thinking | 9 | 11 | Mutation, object identity, function contracts and reliable file I/O | Test with absolute beginners and distinguish Python semantics from general programming |
| [SEF3](SEF3.md) — Linux & the Command Line | 9 | 11 | Shell safety, hostile pathnames, scheduled automation and diagnosis | Reproduce shell tasks in disposable accounts; no dangerous commands on learner machines |
| [SEF4](SEF4.md) — Data Structures & Algorithms | 4 | 8 | Correctness, heaps, graph algorithms and design strategies | Check greedy counterexamples, algorithm boundaries and expected runtime |
| [SEF5](SEF5.md) — Software Engineering Practice | 4 | 7 | Test design, CI, reproducibility and maintainable handoffs | Exercise CI and testing labs on a clean checkout; avoid duplicating SEF9 |
| [SEF6](SEF6.md) — C Programming & Machine Memory | 7 | 9 | Defined C behavior, ownership contracts and defensive parsing | Reproduce compiler and sanitizer results, including failure cases |
| [SEF7](SEF7.md) — Unix System Interfaces | 5 | 8 | Signals, pipes, descriptor lifetime and resilient TCP | Verify POSIX/Linux assumptions, partial I/O and cleanup semantics |
| [SEF8](SEF8.md) — Mathematics for Computing & AI | 5 | 9 | Proofs, extended linear algebra, statistical inference and numerical methods | Check notation, prerequisites, numerical examples and realistic pacing |
| [SEF9](SEF9.md) — Professional Workflow & AI-Assisted Engineering | 7 | 8 | Untrusted AI instructions, least-privilege tools and independent verification | Validate safe exercises without real secrets or unauthorized actions |
| [SEF10](SEF10.md) — Software Engineering Foundations Capstone | 5 | 6 | Requirement evidence, reproducible review and defense rehearsal | Rehearse assessment rubric and independent project reproduction |
| **Total** | **63** | **87** | | |

The revised counts are **not** a limit on course size, nor a claim of comprehensive subject coverage. Lesson entries are navigation/assessment contracts, not full lecture scripts.

## Architectural decisions

1. **Learning order before tooling.** Start with mechanisms and models; introduce concrete tools as applications. SEF1 supplies basic hardware behavior, SEF2 teaches programming, and SEF3–SEF9 extend the prerequisites toward SEF10.
2. **Variable depth.** Modules are introduced only when there is an identifiable family of outcomes, explanations and practical evidence. No fixed module or lesson count is appropriate across SEF.
3. **Algorithmic reasoning.** SEF4 now covers invariants, correctness, heaps, weighted graphs and algorithm-design methods in addition to the previously imported structures, sorting and traversals.
4. **Practical engineering.** SEF5 now distinguishes meaningful tests, CI and maintainable handoffs from SEF9's broader project-management and AI-assisted delivery workflows.
5. **Systems reliability.** SEF7 covers interrupted and partial I/O, signals, process cleanup, pipes and bounded TCP handling, without becoming an advanced SYS course.
6. **Mathematical rigor.** SEF8 adds proof techniques, linear algebra beyond matrix multiplication, statistical uncertainty and numerical convergence. It is foundational rather than a substitute for specialized AI mathematics.
7. **Independent work.** All material needed to understand the curriculum requirements remains public, with optional book mappings and paid instruction outside OEE.

## Critical review gates still outstanding

- **Concept-to-outcome traceability:** verify each learning outcome is taught and assessed without unnecessary repetition or missing prerequisites.
- **Technical accuracy:** independently check every C/Unix/algorithm/mathematical claim, including integer behavior, system-call conditions, complexity assumptions and numerical error.
- **Assessment authoring:** replace checkpoint names with real question sets, correct answers or rubrics, thresholds where justified, and defensible outcomes-to-question mappings.
- **Lab instructions:** for every `lab`, record an exact local environment, prerequisites, input fixtures, procedure, expected results, verification, evidence and failure-analysis expectations. New lab briefs begin this work but do not exhaust it.
- **Hands-on reproduction:** run each lab on a clean, documented environment, reproduce intentional failures and confirm that safety/resource requirements are achievable.
- **Pacing and scaffolding:** the new duration estimates are editorial assumptions; trial them with learners and revise based on recorded load, confusion and lab completion.
- **Capstone:** verify scope, evaluation criteria, documented evidence and a genuine independent defense before making readiness claims.
- **Cross-program boundaries:** check that SEF prepares APP, SYS, AI and SEC without duplicating specialized upper-level courses.
- **Availability and access:** avoid paid services, proprietary tools or unsafe learner-system modifications as a hidden course requirement.

Passing the structural validator and GitHub Actions checks does **not** advance course status to `tested` or `verified`; those transitions require the [Status Labels](../../spec/status-labels.md) and [Evidence Rules](../../spec/evidence-rules.md) evidence.

## Suggested next phases

1. Review the revised **SEF4, SEF5, SEF7 and SEF8** with subject-matter and pedagogical reviewers; challenge complexity, pacing and technical assumptions.
2. Review SEF1–SEF3 and SEF6, SEF9, SEF10 for prerequisite readiness, lab integration, safe execution and project transfer.
3. Author reproducible lab briefs and assessed checkpoints in focused changes, beginning with the foundational skills that all specialized programs depend on.
4. Confirm the shared SEF→APP prerequisite boundary and then use this improved structure when importing SYS.

No private `content` repository, book mappings, OEE Workspace or normative OEE specification requirements are changed by this audit.
