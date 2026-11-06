# SEF5 — Software Engineering Practice

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** [SEF2](SEF2.md)
**Duration:** 8 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

This course develops practical software engineering discipline using the programs already built in SEF2. Learners make reversible Git changes, design trustworthy tests, debug actual failures, refactor with behavioral guarantees, run reproducible CI gates, review changes and prepare an independently reproducible CLI release.

- [**SEF2 — Programming & Computational Thinking**](SEF2.md)

[SEF3 — Linux & the Command Line](SEF3.md) and [SEF4 — Data Structures & Algorithms](SEF4.md) are complementary preparation but are not required for version control, testing, debugging, refactoring, or code review.

## Learning outcomes

By the end of the course, the learner will be able to:

- Use Git branches, commits, merges, and pull-request workflows.
- Design meaningful tests for software behavior.
- Debug failures using evidence rather than guesswork.
- Refactor code without changing its intended behavior.
- Organize a growing codebase into maintainable components.
- Review code and explain engineering improvements.
- Automate basic testing and quality checks with CI.
- Develop reproducible test and CI workflows, review code changes, diagnose failures, and refactor a documented software project without altering behavior.

## Modules

### Module 1 — Version Control & Collaboration

#### Outcomes

- Record, inspect, and navigate project history with Git.
- Create, merge, and resolve conflicts between branches, and collaborate through a remote.

- Recover a Git mistake without destroying unrelated work or rewriting shared history.

#### Lessons

1. **Course introduction: Software Engineering Practice** — `lesson`

   Writing code is a small part of software engineering. This course teaches the practices that keep software working as it grows and as more people work on it.
2. **Repositories and commits** — `lesson`
3. **History and diffs** — `lesson`
4. **Branches** — `lesson`
5. **Merging** — `lesson`
6. **Merge conflicts** — `lesson`
7. **Remotes and pull requests** — `lesson`
8. **Staged versus working-tree changes** — `lesson`
9. **Reverting published changes versus rewriting history** — `lesson`
10. **Generated files, ignore rules and secret hygiene** — `lesson`
11. **Git workflows** — `test`
12. **Resolve a conflict** — `lab`

### Module 2 — Testing & Debugging

#### Outcomes

- Write unit tests and choose test cases that expose failures.
- Diagnose a failing program from evidence rather than guesses.

- Seed failures to establish which test layer detects which risk.

#### Lessons

1. **Assertions** — `lesson`
2. **Unit tests with pytest** — `lesson`
3. **Choosing test cases** — `lesson`
4. **Reproducing failures** — `lesson`
5. **Debugging by evidence** — `lesson`
6. **Unit and integration testing responsibilities** — `lesson`
7. **Parameterized cases, fixtures and isolation** — `lesson`
8. **Regression cases for previously observed defects** — `lesson`
9. **Testing and debugging** — `test`
10. **Diagnose a broken program** — `lab`

### Module 3 — Maintainable Software

#### Outcomes

- Recognize code smells and improve code with behavior-preserving refactorings.
- Use logging, style guides, and code review to keep software maintainable, and read unfamiliar code.

- Show a tested, reversible refactor with clear module contracts.

#### Lessons

1. **Code smells** — `lesson`
2. **Refactoring** — `lesson`
3. **Style guides** — `lesson`
4. **Logging** — `lesson`
5. **Code review** — `lesson`
6. **Reading unfamiliar code** — `lesson`
7. **Module boundaries and dependency direction** — `lesson`
8. **Behavior-preserving refactoring strategies** — `lesson`
9. **User-facing documentation and review evidence** — `lesson`
10. **Maintainability** — `test`
11. **Review a pull request** — `lab`

### Module 4 — Testing Strategy & Reliability

#### Outcomes

- Design stable tests that expose meaningful behavioral defects.
- Demonstrate reasoning with both ordinary and deliberately failing inputs.

#### Lessons

1. **Equivalence classes and boundary values** — `lesson`
2. **State-based testing and invariants** — `lesson`
3. **Unit, integration and end-to-end test selection** — `lesson`
4. **Property-based testing principles** — `lesson`
5. **Flaky tests, time and randomness** — `lesson`
6. **Testing negative paths and side effects** — `lesson`
7. **Testing Strategy & Reliability reasoning and diagnosis** — `test`
8. **Repair a flaky CLI test suite** — `lab`

### Module 5 — Continuous Integration & Build Reproducibility

#### Outcomes

- Create quality gates that fail safely and reproduce locally.
- Demonstrate reasoning with both ordinary and deliberately failing inputs.

#### Lessons

1. **Dependency lockfiles and isolated environments** — `lesson`
2. **Formatter, linter and static type checks** — `lesson`
3. **CI workflows, stages and failure gates** — `lesson`
4. **Secrets, permissions and untrusted CI input** — `lesson`
5. **Clean-checkout builds and release artifacts** — `lesson`
6. **Continuous Integration & Build Reproducibility reasoning and diagnosis** — `test`
7. **Build a red-green CI workflow** — `lab`

### Module 6 — Code Maintenance, Documentation & Handoff

#### Outcomes

- Produce a small reviewable change another engineer can reproduce and maintain.
- Demonstrate reasoning with both ordinary and deliberately failing inputs.

#### Lessons

1. **Contracts, coupling and interface stability** — `lesson`
2. **Logging, error context and sensitive data** — `lesson`
3. **Small reversible changes and meaningful commit history** — `lesson`
4. **Peer review and actionable feedback** — `lesson`
5. **README setup and contributor guidance** — `lesson`
6. **Dependency upgrades and technical-debt decisions** — `lesson`
7. **Code Maintenance, Documentation & Handoff reasoning and diagnosis** — `test`
8. **Refactor a shared feature and prepare a review** — `lab`

### Module 7 — Tested CLI Application

#### Outcomes

- Complete and explain the **Tested CLI Application** integration lab, demonstrating the relevant course outcomes and retained evidence.

#### Lessons

1. **Tested CLI application** — `lab`

   **Final integration lab — required work**

   **Tested CLI Application**

   Convert the SEF2 application into a maintainable software project with:

   - Meaningful Git history
   - Automated tests
   - Linting/formatting
   - Structured logging
   - Error handling
   - Refactored modules
   - CI test execution
   - Documentation
   - Independent clean-checkout reproduction
   - Negative-path and integration tests
   - Review findings and a documented response

## Completion requirements

- Complete the required course exercises, checkpoints and evaluated labs below.
- Complete the final integrated `lab` in the last module and meet its observable exit criteria.
- Retain reproducible artifacts, verification results, design explanations, and a technical retrospective as required by the [OEE Evidence Rules](../../spec/evidence-rules.md).

Complete these required exercises:

**Practical practice:**

- Resolve a controlled merge conflict.
- Debug a deliberately broken application.
- Turn untested code into tested code.
- Refactor duplicated code without changing behavior.
- Review another learner's pull request.

**Required assessment and laboratory contract:**

All seven checkpoints and labs are required. Each checkpoint has two written reasoning questions and expected-answer criteria. Accept equivalent unfamiliar questions only when they assess the same course outcome and retain the same objective criteria. A response passes when it correctly explains the mechanism, distinguishes relevant trade-offs and addresses the failure or safety constraint; naming a command or tool alone is insufficient. Incorrect or incomplete checkpoints must be remediated and reassessed.

**Shared laboratory environment:**

Use a disposable local Git repository and a Python 3.11+ environment with the Python test framework used in SEF5 (for example pytest). Record the exact Python, Git and test-tool versions; pin project development dependencies. Run `python -m pytest -q` or an explicitly documented equivalent, and use simulated branch/CI exercises without credentials, live secrets or destructive actions on real repositories.

**Shared evaluation rules:**

- Checkpoint acceptance: answer both questions in each module with an accurate explanation of the expected result, including consequences of incorrect choices.
- Lab acceptance: demonstrate the listed behavior in a reproducible environment, run normal/negative/boundary checks, explain a seeded or observed failure and supply the required evidence.
- Required evidence: a Git commit or equivalent artifact version, exact commands, test output, input fixtures and independent reproduction where specified. Describe assumptions, known limitations and any unresolved problems.
- Reviewers must verify evidence rather than award completion for screenshots, green badges or unchanged template code alone.

**Module 1 — Version Control & Collaboration: checkpoint** — Required assessment details

- **Q1 (free):** A developer has a local unstaged edit in `config.py`, an accidentally staged generated report, and wants to commit only a tested function change. Explain a safe staging and verification sequence.
  - Expected answer and scoring: Use a selective staging operation such as `git add -p` or explicit paths, unstage the generated report with `git restore --staged <path>` if already staged, inspect both `git diff` and `git diff --cached`, and ensure only the intended change is committed. Avoid discarding the unrelated edit. Answer must distinguish working tree, index, and commit history.
- **Q2 (free):** A defective commit has already been pushed to a shared branch. Compare `git revert` with `git reset --hard` followed by a force push.
  - Expected answer and scoring: `git revert` normally appends an inverse change without rewriting published history and is suitable for collaborative recovery. `reset --hard` discards local state and a forced push rewrites shared history and can remove colleagues' commits. Explain how `--force-with-lease` limits, but does not eliminate, rewrite risks.

**Module 1 — Resolve a conflict: required lab** — Required assessment details

- **Objective:** Use reversible Git operations to isolate intended changes and resolve a real merge conflict while preserving unrelated work.
- **Prerequisites:** Complete this module's lessons and checkpoint; use only a disposable repository or test environment.
- **Environment:** Use a disposable local Git repository and a Python 3.11+ environment with the Python test framework used in SEF5 (for example pytest). Record the exact Python, Git and test-tool versions; pin project development dependencies. Run `python -m pytest -q` or an explicitly documented equivalent, and use simulated branch/CI exercises without credentials, live secrets or destructive actions on real repositories.
- **Procedure:**
  1. Initialize a disposable local repository containing a small Python CLI; make a baseline commit and create two feature branches from it.
  2. On both branches, edit the same function with incompatible behavior; merge into an integration branch and record the conflict markers and Git status.
  3. Resolve the conflict according to a written expected behavior, run tests, inspect staged changes, and commit the resolution.
  4. Independently stage an unwanted generated artifact in the disposable repository, then unstage it without destroying an unrelated working-tree edit.
  5. Create a separate published-style commit locally, revert it with a new commit, and explain why rewriting shared history was unnecessary.
- **Expected result:** Merge conflict is resolved into the specified behavior; tests pass; unwanted generated output is absent from the commit; the revert preserves the original commit in visible history.
- **Verification:** Inspect `git log --graph --oneline --all`, `git status`, `git diff --cached` and the CLI tests; compare final behavior with the written acceptance criteria.
- **Evidence:** Include the source revision, scripts, fixtures, test outputs, failed and corrected behavior, reviewer notes where applicable and a technical retrospective.
- **Failure analysis:** Explain a conflict resolved by silently dropping one required change, accidental staging, or use of a destructive command in the wrong repository.
- **Acceptance:** All required behaviors and safety constraints are met; invalid cases are verified; an independent reviewer can reproduce the relevant evidence, or completion remains pending.

**Module 2 — Testing & Debugging: checkpoint** — Required assessment details

- **Q1 (free):** A function rejects empty input but a mock-based unit test passes because the mock never calls the real validator. Which tests best reveal the defect?
  - Expected answer and scoring: Add a focused unit test on the actual validator and an integration test through the real public call boundary using an empty input. Mock only external dependencies where needed; a passing mock-only test cannot prove real validation.
- **Q2 (free):** A bug occurs only with duplicate identifiers in a CSV file. Explain the steps to turn the incident into a durable regression test.
  - Expected answer and scoring: Capture a minimal deterministic fixture containing duplicates, state expected behavior explicitly, reproduce the failure before fixing it, inspect the root cause, implement a minimal repair, then rerun both regression and relevant existing tests. Document why the earlier suite missed it.

**Module 2 — Diagnose a broken program: required lab** — Required assessment details

- **Objective:** Reproduce a parsing/validation defect and explain its cause using tests and observable program behavior.
- **Prerequisites:** Complete this module's lessons and checkpoint; use only a disposable repository or test environment.
- **Environment:** Use a disposable local Git repository and a Python 3.11+ environment with the Python test framework used in SEF5 (for example pytest). Record the exact Python, Git and test-tool versions; pin project development dependencies. Run `python -m pytest -q` or an explicitly documented equivalent, and use simulated branch/CI exercises without credentials, live secrets or destructive actions on real repositories.
- **Procedure:**
  1. Start from the SEF2 CLI or a provided minimal task manager with a CSV/JSON import operation.
  2. Seed a duplicate-identifier or malformed-input defect; record the exact input, command and actual output before changing code.
  3. Write one direct unit test for the implicated function and an integration test covering the CLI entry point.
  4. Repair the behavior, verify invalid and boundary inputs including empty files and malformed records, and assert no unintended output file mutation.
  5. Record an alternative hypothesis you ruled out and the evidence that distinguished the actual cause.
- **Expected result:** The original fixture fails reliably before repair; a valid fixture still works afterward; invalid inputs receive a predictable message and exit status without corrupting persisted data.
- **Verification:** Run test cases in a clean environment and show red/green output from the same fixture and entry point; use failure logs that omit sensitive data.
- **Evidence:** Include the source revision, scripts, fixtures, test outputs, failed and corrected behavior, reviewer notes where applicable and a technical retrospective.
- **Failure analysis:** Distinguish a test configured to exercise a mock from one that actually checks the failing boundary, or a patch that hides errors without fixing state.
- **Acceptance:** All required behaviors and safety constraints are met; invalid cases are verified; an independent reviewer can reproduce the relevant evidence, or completion remains pending.

**Module 3 — Maintainable Software: checkpoint** — Required assessment details

- **Q1 (free):** What makes a refactor behavior-preserving if you move a function from a CLI handler into a domain module?
  - Expected answer and scoring: For the documented public interface, equivalent valid, boundary and error inputs must preserve observable results and side effects. Internal structure may change; tests should cover behavior, not private implementation shapes.
- **Q2 (free):** A log statement includes a user-provided token alongside an error. Explain the maintainability and security problem and a better replacement.
  - Expected answer and scoring: Logs should preserve useful error context and correlation while redacting secrets and avoiding sensitive payloads. Use a stable error code or safe identifier and test that the token never appears in captured output.

**Module 3 — Review a pull request: required lab** — Required assessment details

- **Objective:** Improve code structure and reviewability while verifying unchanged public behavior.
- **Prerequisites:** Complete this module's lessons and checkpoint; use only a disposable repository or test environment.
- **Environment:** Use a disposable local Git repository and a Python 3.11+ environment with the Python test framework used in SEF5 (for example pytest). Record the exact Python, Git and test-tool versions; pin project development dependencies. Run `python -m pytest -q` or an explicitly documented equivalent, and use simulated branch/CI exercises without credentials, live secrets or destructive actions on real repositories.
- **Procedure:**
  1. Select a small duplicated feature in the SEF2 application and document its input/output contract, including failure cases.
  2. Create a before-state characterization suite and record one bug or design risk identified during code review.
  3. Refactor the feature into a named module with a narrow interface while preserving CLI arguments, outputs and exit behavior.
  4. Prepare a simulated PR with a concise summary, tests, risks, and an inspectable diff; perform a separate checklist review or exchange feedback with another learner.
  5. Address at least one substantive review finding in a follow-up commit and confirm that tests still pass.
- **Expected result:** External behavior is unchanged apart from any explicitly documented bug fix; duplicate logic is reduced, interfaces are clearer, and review findings have recorded responses.
- **Verification:** Compare before/after contract fixtures and diff scope, rerun tests, and confirm the PR summary lists the changed behavior, risks and verification.
- **Evidence:** Include the source revision, scripts, fixtures, test outputs, failed and corrected behavior, reviewer notes where applicable and a technical retrospective.
- **Failure analysis:** Document an accidentally changed error contract, unrelated edits mixed into a refactor, or a test suite that only asserts implementation details.
- **Acceptance:** All required behaviors and safety constraints are met; invalid cases are verified; an independent reviewer can reproduce the relevant evidence, or completion remains pending.

**Module 4 — Testing Strategy & Reliability: checkpoint** — Required assessment details

- **Q1 (free):** A test depends on the current wall clock and occasionally fails across time zones. How should it be rewritten?
  - Expected answer and scoring: Make time an injected or otherwise controllable dependency, set an explicit test clock and timezone where relevant, and assert business behavior for fixed time values; repeating an unreliable test without isolation does not fix the cause.
- **Q2 (free):** A function maps each record to a normalized identifier. Name three distinct useful classes of test inputs and what each demonstrates.
  - Expected answer and scoring: Normal records establish valid behavior; boundaries such as empty/maximum-length strings test limits; invalid or adversarial values such as missing fields, invalid Unicode handling, duplicates, or forbidden characters test rejection/recovery according to the specified contract. Explain any state-dependent invariant.

**Module 4 — Repair a flaky CLI test suite: required lab** — Required assessment details

- **Objective:** Eliminate nondeterministic fixtures and add tests that detect real application invariants.
- **Prerequisites:** Complete this module's lessons and checkpoint; use only a disposable repository or test environment.
- **Environment:** Use a disposable local Git repository and a Python 3.11+ environment with the Python test framework used in SEF5 (for example pytest). Record the exact Python, Git and test-tool versions; pin project development dependencies. Run `python -m pytest -q` or an explicitly documented equivalent, and use simulated branch/CI exercises without credentials, live secrets or destructive actions on real repositories.
- **Procedure:**
  1. Prepare a small CLI test suite with two intentionally seeded causes of nondeterminism, such as reliance on wall-clock time and directory enumeration order.
  2. Run the suite repeatedly with the same source revision and capture both failure patterns; distinguish nondeterministic failure from a product defect.
  3. Replace ambient time with an injected fixed clock and explicitly sort or otherwise define ordering where the product contract requires it.
  4. Add parametrized normal, empty, invalid and duplicate input cases plus one state invariant, using isolated temporary directories.
  5. Run a documented repeated test sequence (at least 20 runs), retain results, and state what repeated passes cannot prove.
- **Expected result:** Both seeded flakiness mechanisms are eliminated for the tested conditions; the suite catches the seeded application defect; clean repeated runs are stable.
- **Verification:** Provide the red/green run logs, isolated fixture setup, and an explanation showing why the fixed tests test observable behavior rather than arbitrary order.
- **Evidence:** Include the source revision, scripts, fixtures, test outputs, failed and corrected behavior, reviewer notes where applicable and a technical retrospective.
- **Failure analysis:** Describe how merely increasing timeouts, relying on collection order, or sharing mutable fixtures across tests can hide instability.
- **Acceptance:** All required behaviors and safety constraints are met; invalid cases are verified; an independent reviewer can reproduce the relevant evidence, or completion remains pending.

**Module 5 — Continuous Integration & Build Reproducibility: checkpoint** — Required assessment details

- **Q1 (free):** Why should a CI job execute the same test and lint commands developers can run locally? What differences can still remain?
  - Expected answer and scoring: Shared commands and pinned dependencies reduce drift and speed diagnosis. Differences remain in OS/architecture, environment variables, permissions and network state, so the job should record material assumptions and use safe default permissions.
- **Q2 (free):** A workflow can access a repository write token and executes code from an untrusted pull request. What principle is violated and how can the risk be reduced?
  - Expected answer and scoring: Least privilege and trust separation: untrusted code should not receive write credentials/secrets. Use read-only tokens and restricted workflows, avoid unsafe evaluation of attacker-controlled input and isolate privileged release steps. Do not demonstrate with actual secrets.

**Module 5 — Build a red-green CI workflow: required lab** — Required assessment details

- **Objective:** Establish a quality gate whose failures reproduce locally and which does not expose secrets to untrusted code.
- **Prerequisites:** Complete this module's lessons and checkpoint; use only a disposable repository or test environment.
- **Environment:** Use a disposable local Git repository and a Python 3.11+ environment with the Python test framework used in SEF5 (for example pytest). Record the exact Python, Git and test-tool versions; pin project development dependencies. Run `python -m pytest -q` or an explicitly documented equivalent, and use simulated branch/CI exercises without credentials, live secrets or destructive actions on real repositories.
- **Procedure:**
  1. Document Python and test/lint tool versions in a project configuration or locked dev dependency set.
  2. Configure a local `quality` command or script that runs tests and one deterministic formatting/static check, then connect the same commands to a CI workflow.
  3. Seed an assertion failure; confirm both the local quality command and CI return nonzero and block a simulated merge.
  4. Repair the assertion failure, then seed a formatting/static-check violation and repeat the rejection; finally demonstrate a green run.
  5. Use a harmless placeholder string rather than any credential and show a documented least-privilege job configuration.
- **Expected result:** Two distinct seeded defects produce red results locally and in CI; the corrected revision is green; setup from a clean checkout uses documented versions.
- **Verification:** Compare version output, commands, exit statuses and workflow logs; demonstrate that quality gates do not silently skip failed steps.
- **Evidence:** Include the source revision, scripts, fixtures, test outputs, failed and corrected behavior, reviewer notes where applicable and a technical retrospective.
- **Failure analysis:** Explain command chaining that masks a failed test, stale dependency installs, or overprivileged workflow credentials.
- **Acceptance:** All required behaviors and safety constraints are met; invalid cases are verified; an independent reviewer can reproduce the relevant evidence, or completion remains pending.

**Module 6 — Code Maintenance, Documentation & Handoff: checkpoint** — Required assessment details

- **Q1 (free):** What information does another engineer need to reproduce and review a bug fix from a clean checkout?
  - Expected answer and scoring: Repository revision, supported environment/dependencies, build/run/test commands, input fixture, expected versus observed behavior, scope and known limitations; links to tests and review evidence should be sufficient without private context.
- **Q2 (free):** A proposed refactor includes formatting every file, dependency upgrades and a behavior fix. What reviewability problem does this create?
  - Expected answer and scoring: It broadens scope and obscures causal changes, making regression and rollback harder. Prefer separate focused changes with tests and clear explanations of any unavoidable coupling.

**Module 6 — Refactor a shared feature and prepare a review: required lab** — Required assessment details

- **Objective:** Deliver a focused maintainability improvement and demonstrate reliable independent handoff.
- **Prerequisites:** Complete this module's lessons and checkpoint; use only a disposable repository or test environment.
- **Environment:** Use a disposable local Git repository and a Python 3.11+ environment with the Python test framework used in SEF5 (for example pytest). Record the exact Python, Git and test-tool versions; pin project development dependencies. Run `python -m pytest -q` or an explicitly documented equivalent, and use simulated branch/CI exercises without credentials, live secrets or destructive actions on real repositories.
- **Procedure:**
  1. Choose one small subsystem of the SEF2 CLI and document its existing public contract and technical-debt risk.
  2. Make a focused refactor, preserve API behavior and verify normal/invalid paths through regression tests.
  3. Update README setup, an example command, a documented failure case and a note explaining module boundaries.
  4. Present the diff and change summary to an independent reviewer or structured checklist and incorporate at least one review comment.
  5. Have the reviewer follow the documented setup in a clean temporary checkout and record any missing instruction.
- **Expected result:** A reviewer can install dependencies, run the feature and checks, and understand the design without undocumented commands; before/after behavior matches the contract.
- **Verification:** Retain a reviewer reproduction log and compare public-API fixtures before/after; include feedback and its resolution.
- **Evidence:** Include the source revision, scripts, fixtures, test outputs, failed and corrected behavior, reviewer notes where applicable and a technical retrospective.
- **Failure analysis:** Describe missing environment assumptions, logging secrets, tangential changes or a documented command that does not work.
- **Acceptance:** All required behaviors and safety constraints are met; invalid cases are verified; an independent reviewer can reproduce the relevant evidence, or completion remains pending.

**Module 7 — Tested CLI Application: checkpoint** — Required assessment details

- **Q1 (free):** Why do green unit tests not alone establish that a CLI release is ready?
  - Expected answer and scoring: A meaningful release also needs an integration/entry-point test, documented installation and dependency versions, invalid-input behavior, static checks, reviewable history and independently reproducible evidence. Unit tests exercise only their tested boundaries.
- **Q2 (free):** How do you verify a refactor and new CI pipeline have not changed expected CLI behavior?
  - Expected answer and scoring: Capture expected outputs, exit statuses and side effects for normal, boundary and failing inputs before the refactor; rerun the same tests after and require CI to use those real checks with documented environment.

**Module 7 — Tested CLI application: required lab** — Required assessment details

- **Objective:** Turn the SEF2 application into a reproducible, maintained project with meaningful tests, CI, review and observable failure behavior.
- **Prerequisites:** Complete this module's lessons and checkpoint; use only a disposable repository or test environment.
- **Environment:** Use a disposable local Git repository and a Python 3.11+ environment with the Python test framework used in SEF5 (for example pytest). Record the exact Python, Git and test-tool versions; pin project development dependencies. Run `python -m pytest -q` or an explicitly documented equivalent, and use simulated branch/CI exercises without credentials, live secrets or destructive actions on real repositories.
- **Procedure:**
  1. Select the existing SEF2 CLI application or a comparable independently written command-line tool, and define at least three user-facing operations and their expected behaviors.
  2. Separate command-line parsing, domain behavior and persistence into bounded components; preserve the required CLI contract and document any intentional fixes.
  3. Create a runnable test suite spanning component logic and CLI entry-point behavior, with at least one normal, boundary, invalid and persistence-failure case.
  4. Provide a pinned or constrained reproducible development environment, lint/format check, safe structured logging, a clean README and a version-controlled CI job or equivalent reproducible runner.
  5. Demonstrate a deliberate failing test and its verified fix, one review and response cycle, and a documented failure from the project retrospective.
  6. Have an independent reviewer follow the clean-checkout instructions, run tests, exercise the CLI and inspect evidence for each required course outcome.
- **Expected result:** A clean checkout produces the documented CLI behavior and passing tests; required quality checks reject a seeded defect; no private credential or hidden setup is necessary.
- **Verification:** Publish an outcomes-to-evidence matrix with command/expected result/observed result; record the exact revision, tool versions, test logs, sample operations and reviewer notes.
- **Evidence:** Include the source revision, scripts, fixtures, test outputs, failed and corrected behavior, reviewer notes where applicable and a technical retrospective.
- **Failure analysis:** Explain a real behavior regression or failure, why its first tests missed it and how the new checks prevent a repeat.
- **Acceptance:** All required behaviors and safety constraints are met; invalid cases are verified; an independent reviewer can reproduce the relevant evidence, or completion remains pending.

**Exit demonstration:**

The learner must diagnose a failing test or bug from evidence rather than by guesswork.
