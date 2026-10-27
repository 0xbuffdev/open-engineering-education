# Governance

## Steward

OEE has one steward: **0xBUFF**, exercised by Christopher S. Aondona. The steward has final say on what enters `spec/` and on the structure of the curriculum.

This is deliberately small. A council or foundation at the current scale would be theatre. Governance grows only when contributions justify it.

## How decisions are recorded

- **Ordinary changes** (typos, chapter-map fixes, lab fixes, documentation): a pull request. The pull request is the decision record.
- **Changes to `spec/` or to the required course structure**: an [RFC](../rfcs/README.md) first, then a pull request that links it. RFCs are accepted, rejected, or returned for revision by the steward, with reasons in the RFC itself.
- **Status-label promotions**: a pull request containing the evidence links and revision note required by [status-labels.md](../spec/status-labels.md).
- **Anything that moves the free/paid line**: an RFC. The list in the [README](../README.md#free-and-paid) may only change in the direction it states, openly, in a pull request.

## Adding a second maintainer

When a contributor is doing sustained, reviewed work — not before — the steward adds them as a maintainer by pull request to this file, recording:

- who they are and what they have contributed;
- what they may merge without review (normally: `curriculum/` fixes within one track);
- that changes to `spec/` remain steward decisions until a wider process exists.

Maintainer status can be withdrawn the same way it is granted, with reasons recorded.

## Neutrality and future governance

The steward's commercial products (0xNAND, mentorship) are separate from this repository; the free/paid line in the README is the boundary. If real outside contributors accumulate — that is, once strangers are routinely shipping accepted changes — the next step is a neutral home (an org or foundation) and a wider decision process. Until then, one steward with written decisions is the honest form of governance this project has.

## Conflict of interest

The steward sells products that implement parts of this standard. The rule is disclosure, not abstention: the README states the relationship in one line, paid material never enters this repository, and no course's status label can be influenced by a product launch.
