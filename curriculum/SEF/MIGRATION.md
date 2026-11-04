# SEF migration notes

**Status:** Imported for structural review only; not conforming, tested or verified.

## Preserved source
The original program and ten course documents remain in the private content repository under `docs/curriculum/SEF/`. Book and resource mappings, including chapter references and module reading assignments, remain there for extraction into a structured resource catalog in a separate branch. No content-repository changes are made here.

## Imported OEE curriculum
Program overview, ten course documents, learning outcomes, course sequences, modules, exercises, labs and capstone requirements have been imported. Canonical files use `SEF1.md` through `SEF10.md`, plus explicit OEE metadata and draft status. The OEE copies omit the book and online-resource mappings.

## Review before standardization
1. The imported courses need substantive alignment with the required sections and evidence requirements in [Course Format](../../spec/course-format.md) and [Evidence Rules](../../spec/evidence-rules.md), not empty placeholder headings.
2. SEF1 ends with an integration lab while documenting why it has no separate lab-only module. Resolve the tension with the current format requiring a final lab module, using an RFC if the normative rule changes.
3. Review learning outcomes, assessment criteria, lab reproducibility and the evidence learners must retain.
4. The current 0xNAND SEF catalog has seven courses with different course boundaries. In particular its `SEF7` is the capstone, whereas the imported curriculum uses `SEF7` for Unix System Interfaces and `SEF10` for the capstone. A legacy-to-canonical mapping is required before reusing these IDs downstream.
5. The OEE Workspace generator currently searches for `SEF1-*.md`, not `SEF1.md`, and needs a separate compatibility PR.
6. The workspace project generator references a project-ladder file that has not been imported. Other programs and shared project definitions must be addressed in later work groups.

## Boundaries
This branch does not modify the private content repository, 0xNAND, OEE Workspace, affiliate infrastructure or the normative specification. Original source files are retained until resource extraction is verified.
