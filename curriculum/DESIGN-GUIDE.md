# Curriculum Design Guide

This guide describes how to organize OEE programs, courses, modules, and lessons
without sacrificing depth or overloading any single course. It applies the
[outcome-driven Course Format](../spec/course-format.md) and
[Evidence Rules](../spec/evidence-rules.md) to curriculum planning.

**Status:** Non-normative editorial guidance. This guide does not add
conformance requirements, fixed course durations, a mandatory lesson count,
a new serialization format, or a separate authoring specification. Where
guidance and the normative `spec/` requirements differ, the specification
takes precedence.

## 1. Design from capabilities, not content volume

Begin with the capabilities graduates should demonstrate, then determine
where each capability is taught and assessed.

| Level | Primary design question | Expected result |
| --- | --- | --- |
| Program | What can a graduate do across this engineering discipline? | A coherent progression of complementary course capabilities |
| Course | What substantial capability can a learner demonstrate after completing this course? | A bounded learning experience with assessable exit outcomes |
| Module | Which closely related abilities form a useful stage of that capability? | A coherent sequence of lessons and relevant practice |
| Lesson | What one primary objective should this instructional unit develop? | A focused explanation, demonstration, or investigation |
| Concept | Which ideas, principles, terms, and mechanisms support that objective? | Material inside one or more lessons, not automatically a separate lesson |
| Assessment | What evidence can establish that the required outcomes were achieved? | Published, outcome-aligned criteria and proportionate evidence |

The unit to optimize is **the learner's demonstrated capability**, not the
number of modules, lessons, tests, labs, or recorded study hours.

## 2. Define course boundaries

A course should develop a recognizable, useful capability that can be described
in a concise statement and assessed with meaningful evidence. Avoid both:

- **Encyclopedic courses:** unrelated or only loosely connected areas are
  combined simply to cover an entire field in one course.
- **Artificial microcourses:** a coherent capability is divided into so many
  small courses that learners repeatedly cross enrollment and assessment
  boundaries without educational benefit.

Review a course boundary by asking:

1. Can I state its core capability without listing dozens of unrelated topics?
2. Are its outcomes mutually reinforcing, or do they describe separate
   capabilities with substantially different prerequisites?
3. Is its exit assessment appropriate for the actual capability being taught?
4. Could a later course deepen the subject without repeating the same lessons?
5. If I split the course, will learners still have a complete and meaningful
   experience within each new course?
6. If I combine courses, does the merger simplify the learning pathway, or
   only lengthen it?

Use **program-level coverage** to preserve breadth: each competency should
have an appropriate owning course, prerequisites, and a known place for later
advanced treatment. A topic can recur when it is needed at greater depth or
in a new context, but repetition should teach a new capability.

### Length and workload

There is **no ideal universal course length**. For initial planning,
a focused taught course might span roughly 4–8 weeks of part-time study,
while an integrated project course may take longer. These are calibration
examples, not limits or proof of quality.

Estimate time from the actual demands of explanations, practice,
debugging, assessments, prerequisite gaps, and project iteration. State
assumptions, including approximate focused hours per week. Review estimates
against learner evidence when available, and retain `draft` status until
the existing readiness rules are met.

When a course appears too long, first identify whether it contains multiple
distinct exit capabilities. If yes, split at a meaningful competency and
prerequisite boundary. If no, preserve the course but simplify sequencing,
eliminate unnecessary repeated submissions, or move advanced material into
an optional or follow-on course.

Do not shorten a course by dropping essential mechanisms or by relying on
undocumented paid teaching material to fill a public-curriculum gap.

## 3. Make modules cohesive

A module is a meaningful stage within a course. Its lessons should develop a
small group of closely related abilities with a clear prerequisite sequence.

A useful editorial starting point is several focused lessons, often around
4–8, but both shorter and longer modules can be justified. Do not split a
module merely to satisfy a numerical target.

Split a module when:

- It contains two substantially different competency clusters.
- The second half has materially different prerequisites.
- Learners need a distinct integration or feedback point before proceeding.
- The module's title no longer describes much of its content.

Keep a module together when its concepts jointly explain the same mechanism
or the same family of engineering decisions.

Module names should describe the capability or system being studied rather
than a generic stage such as `Advanced Topics` or `Part Two`.

## 4. One primary learning objective per lesson

**A lesson is a focused instructional unit.** Its primary objective is an
observable statement of what the learner should be able to explain, trace,
predict, implement, compare, debug, or justify.

A *topic* names a subject area (for example, `DNS`). A *concept* names an
idea or mechanism (for example, `DNS caching`). Neither automatically
defines the boundary of a lesson.

One lesson may need several closely connected concepts to develop its
primary objective. Conversely, a broad topic may require multiple lessons
when it includes distinct learning objectives.

For example:

| Unit | Name | Primary objective |
| --- | --- | --- |
| Module | Domain Names and DNS | Understand domain registration, resolution, and failures |
| Lesson | Domain Names | Explain the purpose and structure of domain names |
| Lesson | Domain Registration | Trace the roles involved in registering a domain |
| Lesson | DNS Records | Interpret common DNS record types |
| Lesson | DNS Resolution | Trace recursive and authoritative resolution |
| Lesson | Caching and Failures | Diagnose effects of caches and common lookup failures |

The `DNS Resolution` lesson may explain resolvers, authoritative servers,
referrals, and query results together. Splitting each noun into its own lesson
would fragment the mechanism rather than improve understanding.

### Deciding when to split a lesson

Consider splitting when learners must acquire two independent primary
objectives, a different prerequisite is needed halfway through, or one
instructional unit becomes hard to navigate and practice.

Keep material together when separation would force learners to reconstruct
a single mechanism across several disconnected lessons. Duration is a
diagnostic, not the definition: an advanced debugging lesson may reasonably
take longer than a short terminology lesson.

A lesson outline can answer four authoring questions without requiring
four mandatory headings:

1. **Purpose:** What capability is this lesson developing?
2. **Mechanism:** How does the system or idea work, including important
   boundaries and assumptions?
3. **Observation or application:** What example, trace, experiment, or
   worked reasoning makes the mechanism concrete?
4. **Feedback:** How will a learner notice a misunderstanding, mistake,
   or limitation before moving forward?

Not every lesson needs a separate exercise or retained evidence artifact.
Practice should be frequent where useful but chosen intentionally.

## 5. Use short, meaningful lesson titles

Prefer concise noun phrases or clear action-oriented phrases. As an
editorial heuristic, **two to five words often suffice**. Longer titles
are acceptable when needed to remove ambiguity.

| Weak title | Prefer |
| --- | --- |
| Introduction to the Basics of How DNS Works | DNS Resolution |
| The Different Types of Records Used in DNS | DNS Records |
| Some More Information About the Browser | Browser Processes |
| Advanced Concepts | HTTP Caching |
| Lesson 7: Learn About Security | Same-Origin Policy |
| Understanding How Pages Get Rendered in the Browser | Browser Rendering |

Avoid decorative labels, repeated `Introduction to`, vague difficulty
adjectives, and titles that list every subtopic. Titles should distinguish
neighboring lessons and remain understandable in course indexes, search
results, and 0xNAND or OEE Workspace navigation.

A short title is not an instruction to write a shallow lesson.

## 6. Preserve foundational depth without repeating everything

Foundational courses should explain important mechanisms and boundaries
well enough for learners to form a reliable mental model. Later applied
courses can use that model and revisit the same area for new objectives.

Illustrative APP ownership:

| Course area | Appropriate responsibility |
| --- | --- |
| Web and Internet Foundations | Networking, domain names, DNS, HTTP, TLS, and how browsers navigate and render |
| HTML and CSS Engineering | Authoring documents, semantics, layout, styling, accessibility fundamentals |
| JavaScript Programming | Language semantics, execution model, program design |
| TypeScript Programming | Type system, type-driven design, integration with JavaScript |
| Browser and Frontend Engineering | DOM APIs, browser application behavior, event handling, performance fundamentals |
| React Application Engineering | Component design, state, rendering, composition, application architecture |
| Backend and Data Engineering | Service construction, persistence, API correctness, operational concerns |

This is an **illustration of competency ownership**, not an adopted APP
course catalog. A real redesign should account for the complete prerequisite
graph, workload, and overlaps with SEF, SYS, SEC, and AI before renumbering
or creating courses.

For example, APP1 may explain *why* HTML/CSS parsing and rendering occur
without teaching comprehensive website authoring. It need not also teach
production backend framework implementation to establish web foundations.

## 7. Build a coverage map before cutting content

Before restructuring a program, create a temporary planning matrix:

| Capability | Owning course | Supporting module | Evidence of mastery | Follow-on depth |
| --- | --- | --- | --- | --- |
| Trace DNS resolution | Web Foundations | Domain Names and DNS | Diagnose a failed resolution | Operations / systems |
| Explain browser rendering | Web Foundations | Browser Rendering | Trace an HTML-to-pixels pipeline | Frontend performance |
| Author semantic HTML | HTML and CSS | Document Semantics | Build and inspect a document | Accessibility engineering |

These are *illustrative* rows. The map is a planning and review aid,
not a mandatory new source of truth or another public requirements file.
Once course requirements are finalized, their canonical outcomes and
assessments remain in the public course definitions.

Use the map to find missing skills, duplicated ownership, circular
prerequisites, unexplained jumps in difficulty, and excessive course
scope. If a course is split, preserve or deliberately revise its exit
capabilities rather than silently deleting them.

## 8. Select practice and assessment based on outcomes

Different learning objectives warrant different evidence:

- Explanations and conceptual tracing may be demonstrated through
  predictions, diagrams, analysis, or diagnosis.
- Engineering implementation can be demonstrated through inspected
  artifacts, behavior tests, and design reasoning.
- Experimental or systems understanding may be demonstrated through
  reproducible observations and interpretation.
- Capstones should integrate work over time, with milestone feedback,
  substantial deliverables, and a reviewable defense.

A single required evaluation may validly cover several outcomes. An
optional self-check need not generate a permanent completion record.
A software test inside a lab is not automatically an additional learner
knowledge test. Avoid one quiz plus one lab per module as a default.

For binding assessment requirements, consult
[Course Format](../spec/course-format.md) and
[Evidence Rules](../spec/evidence-rules.md). An editorial design guide
does not redefine those requirements.

## 9. Keep public curriculum separate from delivery

OEE describes the canonical capability, learning sequence, outcomes,
public assessments, evidence expectations, and prerequisites. It must
remain understandable for independent learners.

OEE Workspace can organize learning material and learner-owned
artifacts. 0xNAND can provide richer explanations, demonstrations,
instructor feedback, guided exercises, adaptive sequencing, and
evaluation tooling. Neither delivery layer should silently replace
the public course's required outcomes or completion criteria.

A lesson's primary objective should remain stable even if its teaching
material is presented as a written explanation, interactive trace,
instructor session, or an alternative accessible format. A future data
export may expose lesson structure, but this guide does not introduce
new required lesson identifiers or a platform-specific schema.

## 10. Review before migrating a course

For each proposed course or major restructuring, check:

1. **Capability boundary:** the course has a coherent purpose and
   meaningful exit outcomes.
2. **Coverage:** required program capabilities have a deliberate owner;
   no essential topic disappears during a split or consolidation.
3. **Prerequisites:** there are no accidental cycles, hidden assumed
   skills, or unrelated barriers to entry.
4. **Module cohesion:** each module groups related objectives and has
   a teachable progression.
5. **Lesson focus:** each lesson has one primary objective, with
   logically related concepts and a concise descriptive title.
6. **Practice:** examples, labs, and checks serve actual learning
   needs rather than filling a quota.
7. **Assessment:** every required course outcome is covered by
   appropriate, publicly described evaluation and proportionate
   evidence.
8. **Workload:** duration estimates reflect realistic independent
   learner effort, not a fixed lesson/module target.
9. **Delivery independence:** no mandatory requirement is hidden in
   0xNAND, paid books, or other proprietary resources.
10. **Migration:** existing course codes, prerequisites, learner
    records, resource mappings, and downstream integrations have
    an explicit impact plan.

Apply this guide first to representative courses:

- **SEF1:** foundational understanding, reasoning, and simulation.
- **APP1:** Internet and browser foundations without unnecessary
  backend implementation or fixed per-module test/lab pairs.
- **SEF10:** one cumulative engineering project with appropriate
  milestones, evaluation, and defense.

These pilots should inform later revisions; they do not warrant
claiming broader educational efficacy before learner evidence exists.

## 11. Normative boundary

This document is a non-normative design aid. The current OEE
specification determines valid course structure, evidence rules,
status labels, conformance, and the RFC process. Requiring exact
lesson counts, time limits, a new mandatory authoring schema, or
new assessment obligations would be a separate normative change
and would require the established RFC process.
