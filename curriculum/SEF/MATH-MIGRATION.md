# SEF Mathematics Revision and Evidence Migration

> [SEF catalog](README.md) · [SEF11](SEF11.md) · [Revised SEF8](SEF8.md) · [RFC 0003](../../rfcs/0003-sef-academic-progression.md)

## Scope and authority

This records the **substantive mathematics revision** adopted through RFC 0003. The program catalog and course files are authoritative for current prerequisites, outcomes and completion. This document preserves the translation of old capabilities, not a competing source of learner requirements or an automatic completion migration.

Historical reference: the ten-course SEF curriculum at OEE commit [`39426b73bdc3ae8af44c4b54b21fc4ea4e53c7ec`](https://github.com/0xbuffdev/open-engineering-education/tree/39426b73bdc3ae8af44c4b54b21fc4ea4e53c7ec/curriculum/SEF). Its prior SEF8 is the authoritative **old revision** when interpreting old `SEF8-O*` and `SEF8-AS*` evidence. Existing outcomes or assessments are not renamed retroactively.

## Mathematical coverage moved to SEF11

| Former required SEF8 contract | New current teaching and assessment owner | Reassessment guidance |
| --- | --- | --- |
| `SEF8-O1`: arithmetic, fractions, proportions and rates | `SEF11-O1` and `SEF11-AS1` | Check unfamiliar exact/approximate and invalid examples; do not just copy old score |
| `SEF8-O2`: equations, inequalities, function tables | `SEF11-O2` and `SEF11-AS1` | Demonstrate substitution and domain reasoning |
| `SEF8-O4`: logic, sets, quantifiers, counting | `SEF11-O3`, `O4`, `O5` and `SEF11-AS2/AS3` | Each logic/sets/counting sub-capability must be demonstrated |
| `SEF8-O5`: proof, induction, relations, graph properties | `SEF11-O4`, `O6`, `O8` and `SEF11-AS2/AS4/AS5` | Verify proof completeness and graph-domain assumptions |
| `SEF8-O13`: asymptotic growth and recurrence bounds | `SEF11-O7` and `SEF11-AS5`; applied again by SEF4's unchanged algorithm analysis | Verify general argument, not timing-only observation |
| `SEF8-AS1`: arithmetic/pre-algebra bridge | Retired from **current SEF8**, replaced by `SEF11-AS1` | The original diagnostic was ungraded; earlier summative readiness may be considered on its merits |
| `SEF8-AS2`: logic, proofs, counting and graph | Retired from **current SEF8**, replaced across `SEF11-AS2`–`AS5` | Required evidence is not necessarily equivalent one-for-one |

`SEF11-O9` adds explicit independent calculation and bounded-enumeration checks, and `SEF11-O10` adds integrated discrete reasoning with a reviewer challenge. The new mathematical expectations are not automatically satisfied by old attendance or old SEF8 completion.

## SEF8 retained and revised contracts

| SEF8 identifiers | New treatment | Reason |
| --- | --- | --- |
| `SEF8-O3`, `O6`–`O12`, `O14`–`O18` | Retained with their original capability statements | Existing numerical, linear-algebra, probability, statistics, differentiation, finite precision, optimization and review competencies stay required |
| `SEF8-AS3`, `AS4`, `AS6`, `AS7` | Retained with unchanged published work, criteria and evidence | The evaluated numerical competencies are equivalent and can reuse verified evidence |
| `SEF8-AS5` | Retired from current contract; `SEF8-AS9` is a **new** calculus assessment | Original `AS5` assessed growth `O13` as well as differentiation; current assessment adds algebra, limits and integration |
| `SEF8-AS8` | Retired from current contract; `SEF8-AS10` is a **new** integration assessment | The previous notebook evaluated all 18 old outcomes, including discrete mathematics; the revised one evaluates 15 current numerical outcomes |
| `SEF8-O19` | New algebraic/exponential/logarithmic function, domain, limit and continuity capability | Necessary explicit preparation before derivatives |
| `SEF8-O20` | New accumulation, elementary integration and continuous-density capability | Prevents an unexplained transition from derivatives to applied continuous mathematics |

The revised SEF8 no longer lists the old `SEF8-O1`, `O2`, `O4`, `O5`, `O13` as current required outcomes. Their original IDs remain meaningful **only in their earlier version**. Course 8's current core assessments are `AS3`, `AS4`, `AS6`, `AS7`, `AS9` and `AS10`. IDs deliberately have gaps. Do **not** renumber to fill them.

## Program and downstream contract

- `SEF11` follows `SEF2`; `SEF4` and `SEF8` require `SEF11` and can then be taken concurrently.
- `SEF6` continues to require `SEF3`, `SEF4` and `SEF5`; `SEF7` continues to require `SEF3` and `SEF6`. Advanced SYS transfer is **not** part of this migration.
- `SEF10` requires `SEF1` through `SEF9` **plus SEF11**, while retaining its single existing cumulative capstone.
- AI1 and other downstream programs that cite SEF8 continue to receive numerical mathematics, now with SEF11 transitively required. No independent change is made to APP, SYS, AI or SEC course files here.
- OEE Workspace, 0xNAND, resource mappings and third-party consumers must reference the **current catalog and source revision**; preserve learner evidence and report any migration separately. No paid content or proprietary platform may become an entry requirement.

## Historical evidence evaluation

1. Preserve the learner's original course revision/commit SHA, exact outcome and assessment IDs, criteria, submitted work, review decision and reviewer provenance.
2. Keep a prior completion attached to the prior contract; never delete it, automatically revoke it, or automatically promote it as completion of new `SEF11` or revised `SEF8`.
3. Review actual artifacts against each new required outcome and criteria. Recognize equivalent demonstrated capabilities only where the evidence directly establishes them; document decisions per new assessment and indicate which new cases still require evaluation.
4. Reassess unmet competencies with unfamiliar but equivalent public examples, without imposing a fixed bridge diagnostic attempt count.
5. Make any newly recognized completion explicitly attributable to its assessed revision. Status `draft`/`tested`/`verified` remains a **course readiness** designation, not a learner grade or a migrated artifact label.

## Verification checklist

- Catalog has exactly eleven current required SEF courses in valid prerequisite order, including SEF11 as a prerequisite to SEF4/SEF8 and an additional capstone prerequisite.
- SEF11 all 10 outcomes have required summative assessment coverage; SEF8 all 15 current outcomes have substantive required coverage, without the five retired outcome IDs being treated as current.
- Unchanged SEF8-AS3/AS4/AS6/AS7 remain equivalent to their historical assessment briefs; new AS9/AS10 have new IDs because their contracts materially change.
- Course and inventory validators reject extra/missing/duplicate course definitions, bad links, mismatched metadata, invalid dependencies and cycles; they derive course order from the published catalog rather than numeric course IDs.
- Every course remains `draft` until the existing OEE readiness evidence is established. Study duration and workload estimates must be calibrated using actual learners.

This is an educational architecture change, **not** evidence that learners have already completed or that teaching effectiveness has been verified.
