# Labs

Before each course, run `./scripts/new-course-workspace <track> <course-slug>`. It creates the matching lab, exercise, and notes directories from the shared templates. Create individual experiments inside `labs/<track>/<course>/<number>-<slug>/`.

Every lab must contain a `README.md` with this template:

```markdown
# <lab name>

## Question

What mechanism or hypothesis is this lab testing?

## Setup

Host/OS, CPU/GPU, memory, tool versions, data source, and dependencies.

## Procedure

Exact commands and inputs needed to reproduce the work.

## Results

Measurements, plots, test output, and the raw-data location.

## Interpretation

What happened, why, limitations, and the next experiment.
```

Do not commit large raw data, model weights, credentials, or unsafe exploit artifacts. Link to a legal source or document how to regenerate them.
