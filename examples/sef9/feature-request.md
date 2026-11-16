# Synthetic SEF9 CSV export request

> All persons, records and events here are fictional. Use this document as a stakeholder prompt, not as verified production research.

**Request:** "I need to export my task list to a CSV file to review it offline, but I cannot afford to lose my previous export if the new one is bad."

**User contexts:** a developer exporting task titles before an offline meeting, and an operations reviewer who loads a saved report into a spreadsheet. Both need a plain-text, reproducible path as well as a readable file.

## Known needs

- Export exactly the requested synthetic `id` and `title` fields with a header; do not silently export unrelated metadata.
- Round-trip commas, double quotes and embedded newlines using a documented CSV dialect.
- An empty task list produces a valid header-only CSV.
- Invalid destination, malformed records and I/O failure have an observable **failure result**; they must not be reported as success.
- A failed new export must not destroy or partially replace an existing **valid** file. The intended publication strategy and its portability limits must be documented.
- All test paths remain under a disposable local directory; no customer data, production files, credentials or external network.

## Open questions to resolve in a versioned requirement decision

- Is a missing destination parent an error, or must the application create it?
- Is an existing file replaced after a fully valid export? Is the operation required to be atomic on this filesystem?
- How are duplicates, empty titles, newline normalization and text encoding handled?
- What exactly does the CLI print to stdout and stderr, and what status code signifies a failure?
- Who is authorized to read or redistribute the resulting CSV, and when is it deleted?

Reviewers should vary the data or destination and expect the learner to revise ambiguous criteria, not merely repeat a fixed solution.
