# Recorded, attributable ChatGPT candidate — seeded CSV exporter

**Provenance:** The candidate below was authored by **ChatGPT (GPT-6)** on **2026-11-16** as part of creating this public OEE SEF9 curriculum teaching fixture. This is an actual model-authored proposal captured in the versioned repository, **not a transcript of a separate user/model conversation**. It does **not** claim a third-party assistant ran a tool, fetched private files, executed tests, passed review, or committed code. The recorded proposal is supplied *as a proposed change only*, not as a correct solution.

**Input brief given for this fixture:** Implement a short Python CSV export helper for synthetic `id` and `title` tasks with a `bool` result and a caller-specified destination. The result will be reviewed against the independent contracts in [feature-request.md](feature-request.md). **The teaching example specifically asks the assistant to supply a deliberately flawed candidate** so three reviewable bugs can be caught and repaired.

**Proposed implementation (verbatim, also saved as [seeded_export.py](seeded_export.py) with a nonfunctional teaching docstring):**

```python
from __future__ import annotations

from os import PathLike
from typing import Iterable, Mapping


def export_tasks(
    tasks: Iterable[Mapping[str, object]], destination: str | PathLike[str]
) -> bool:
    try:
        with open(destination, "w", encoding="utf-8", newline="") as stream:
            stream.write("id,title\n")
            for task in tasks:
                stream.write(f"{task['id']},{task['title']}\n")
    except OSError:
        return True  # Deliberately wrong: hides failure.
    return True
```

**Recorded actions:** proposal text only. No subprocesses, external calls, dependencies, tests, merges, reviewer messages, filesystem reads or secret access were performed *by the proposed exporter* at proposal time. The GitHub connection used to publish this teaching artifact is a separate editor action, not a tool invocation by this candidate.

**Evidentiary limits:** the Git history identifies when this file was published; it does not independently prove details of a separate chat or model API run. The candidate is **intentionally defective** and must never be treated as trusted code. Its exact behavior is demonstrated by the intentionally failing, independently specified [test_seeded_export.py](test_seeded_export.py) in a disposable environment. A student must build and verify their own repair, report real observed results and obtain actual independent reviewer feedback.

**Instructor note:** if a curriculum delivery channel requires separately archived provider transcripts or cryptographically verifiable assistant attribution beyond this original model-authored source artifact, the instructor must supply those genuine artifacts rather than invent them.
