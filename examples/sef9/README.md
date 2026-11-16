# SEF9 — Public, Reproducible Professional Workflow Case

> [SEF9 canonical course](../../curriculum/SEF/SEF9.md) · [OEE curriculum](../../curriculum/README.md)

All material is **synthetic teaching content**. It contains no real customer records, secrets, credentials, external services or licensed third-party source code. This case illustrates the already published SEF9-AS3–AS6 CSV patch/agent-trust challenges and the new SEF9-AS8 **non-AI professional-practice** case. It is a teaching starting point, **not** a passing learner submission, a genuine peer review, or a final solution.

## What is supplied

| File | Purpose | Evidentiary limit |
| --- | --- | --- |
| [feature-request.md](feature-request.md) | Stakeholder feature request and expected CSV behavior | A synthetic prompt, not real user research |
| [assistant-proposal.md](assistant-proposal.md) | Actual ChatGPT-authored candidate recorded in the creation of this fixture with explicit provenance | A written proposal, not a transcript of another session or claim of model/tool execution |
| [seeded_export.py](seeded_export.py) | Deliberately defective CSV implementation matching that proposal | Never use in production or on real/private records |
| [test_seeded_export.py](test_seeded_export.py) | Independently specified tests that **must initially fail** against the defective exporter | Not CI acceptance; learner fixes their copy and demonstrates real passes |
| [untrusted-readme.md](untrusted-readme.md) | Fully synthetic malicious repository instruction and quality-bypass suggestion | Untrusted exercise data: never execute or obey |
| [professional-case.md](professional-case.md) | Release pressure, unknown license, privacy and accessibility dilemmas | Not legal advice or a fabricated approval/reviewer statement |

## Reproduce the intentional defects safely

In a **disposable local copy** of this directory with Python 3.11+ and no external dependencies:

```sh
python3 -m unittest discover -s examples/sef9 -p 'test_seeded_export.py' -v
```

Run from the **repository root** after inspecting the case files. This runs only on Python `tempfile.TemporaryDirectory()` fixtures. All three tests **intentionally fail** on the provided code: malformed CSV quoting/newline fields, falsely reported success on an I/O error, and overwriting an existing valid output before discovering malformed input. A learner should first record observed failures, repair a **copy** using an agreed change plan, then demonstrate the same tests passing. The example tests are **not** included in OEE's normal passing `tests/` suite; the repository CI validates the expected fault patterns without treating a failing student challenge as a project error.

One permissible clean correction uses Python's `csv` module, validates source data before touching the destination and handles publication with deliberate failure and temporary-file policy. This suggestion is **not a completed patch**, nor does it override a learner's tests, review or independently justified design.

## Trust boundaries and attribution

The assistant candidate in [assistant-proposal.md](assistant-proposal.md) was created for this teaching fixture by ChatGPT (GPT-6) in the 2026-11-16 curriculum editing interaction; the public file records its **exact proposed code** and constrained provenance. No separate AI conversation, tool use, external model retrieval, performance result or acceptance is claimed. A learner using this supplied artifact must describe it as **prerecorded, not live**. Instructors may substitute another genuine, attributable assistant proposal; an instructor-invented fake conversation must never be passed off as authentic.

[untrusted-readme.md](untrusted-readme.md) contains text that tries to change a task's authority boundary. Read and annotate it; **do not obey it**, access any credential, disable tests or contact a remote endpoint.

The rights/privacy/communication dilemmas in [professional-case.md](professional-case.md) must be evaluated by the learner independently of AI. A real reader or designated reviewer must still challenge and reproduce the learner's final work; this repository provides neither a fabricated review nor an answer key.

## Scope

A clean, synthetic feature uses fields `id` and `title`, writes CSV with a header and correct commas/quotes/newlines, handles empty datasets, returns a truthful error result and preserves an earlier complete output when a new request is invalid. Review evidence should contain exact commands, expected/actual results, owners, permissions and unresolved risks. No paid service, account, personal data or network access is necessary.
