# Learning Lab

A build-first, zero-to-professional curriculum for Foundations, Systems Engineering, AI & Machine Learning, and Security Engineering.

Begin with [curriculum.md](curriculum.md). It is the source of truth for course order, prerequisites, required local-book readings, external-resource gaps, labs, exit checks, and capstones.

## Start today

1. Read the first section of [curriculum.md](curriculum.md).
2. Open [books/README.md](books/README.md) to see what is already available and exactly where it is used.
3. Review [resources/README.md](resources/README.md) before a course that needs material not in `books/`.
4. Create work folders from the templates in [labs](labs/README.md), [exercises](exercises/README.md), and [notes](notes/README.md).
5. Commit the artifact and retrospective for each completed course.

The F0 and F1 workspaces are already created. For every later course, run `./scripts/new-course-workspace <track> <course-slug>`; for example, `./scripts/new-course-workspace 01-foundations F2-data-structures-and-algorithms`.

## Tracks

- [01 Foundations](tracks/01-foundations/README.md) — required starting point.
- [02 Systems Engineering](tracks/02-systems-engineering/README.md) — operating systems, architecture, performance, networking, distributed systems, and AI infrastructure.
- [03 AI & Machine Learning](tracks/03-ai-machine-learning/README.md) — data, ML, deep learning, LLMs, serving, agents, and MLOps.
- [04 Security Engineering](tracks/04-security-engineering/README.md) — threat modeling, secure systems, authorized lab security, cryptography, and AI red teaming.

The PDFs in `books/` are personal reference materials and are intentionally ignored by Git. Do not add copyrighted copies, credentials, model weights, or sensitive datasets to this repository.
