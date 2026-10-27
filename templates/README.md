# Workspace Templates

These templates are copied into your **own study workspace** by the scripts in [`../scripts/`](../scripts/). This repository ships templates only: learner work is never committed here.

- `course-workspace/` is used by `scripts/new-course-workspace` (labs, exercises, notes).
- `project-workspace/` is used by `scripts/new-project-workspace` (project README, design, evaluation, retrospective).
- `progress.md` is the evidence log; copy it to the root of your workspace as `progress.md`.

Generated workspaces are snapshots: customise your copy, and later template changes will not rewrite existing work. Improve the source template only when a shared practice should change for future workspaces.

The course template is intentionally small. The course file in [`../curriculum/`](../curriculum/README.md) is the assignment; the workspace is the evidence container. Generated files link back to the course file in this repository rather than copying it.

See [`spec/evidence-rules.md`](../spec/evidence-rules.md) for what the evidence in a workspace must look like.
