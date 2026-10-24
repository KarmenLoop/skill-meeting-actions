# Meeting Actions

[English](README.md) · [中文](README.zh-CN.md) · **v0.2.1**

[![Local checks](https://github.com/KarmenLoop/skill-meeting-actions/actions/workflows/checks.yml/badge.svg)](https://github.com/KarmenLoop/skill-meeting-actions/actions/workflows/checks.yml)
[![Release](https://img.shields.io/github/v/release/KarmenLoop/skill-meeting-actions)](https://github.com/KarmenLoop/skill-meeting-actions/releases/latest)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Network: none](https://img.shields.io/badge/network-none-lightgrey)](docs/COMPATIBILITY.md)

**Keep every action item tied to the words that support it—quote, line range, owner, and due date.**

An agent skill plus a local evidence validator: candidate actions are checked against a transcript before they count as ready. You keep the export (or transcript, diff, ledger, event log, or JUnit XML) local; the helper stays on the standard library and never opens a network connection. The skill layer teaches a host *when* to prepare input, *how* to narrate results, and *where* to stop before side effects the user did not authorize.

Built and maintained by [KarmenLoop](https://github.com/KarmenLoop) / [KARMENLOOP](https://karmenloop.com). Current release: **[v0.2.1](https://github.com/KarmenLoop/skill-meeting-actions/releases/tag/v0.2.1)**. License: **MIT**.

![Meeting Actions sample JSON output from version 0.2.1](docs/images/example-output-v0.2.1.svg)

*Actual local output from v0.2.1, rendered as an image. [examples/expected.json](examples/expected.json) · [Image provenance](docs/images/provenance.json).*

[Download v0.2.1](https://github.com/KarmenLoop/skill-meeting-actions/releases/tag/v0.2.1) · [Tutorial](docs/tutorial.en.md) · [中文教程](docs/tutorial.zh-CN.md) · [Input contract](docs/INPUT.md)

---

## Why this exists

Meeting notes that invent owners or invent deadlines create silent debt. Agents amplify that debt when they treat a paraphrase as a commitment.

This package separates **interpretation** (you or the model propose actions) from **verification** (the helper checks quote location and completeness). Missing owner or due stays `null`—visible, not guessed.

Ready items are those with verified evidence *and* filled gaps. Everything else stays in clarification, with the supporting quote still attached.

---

## Snapshot

| | |
|---|---|
| **What you install** | Skill tree + `scripts/run.py` evidence helper + `install.py` |
| **Runtime** | Python **3.9+**, standard library only |
| **Network** | **None** |
| **Input** | UTF-8 JSON: `transcript` + `actions[]` (`id`, `task`, `owner`, `due`, `quote`, `line_start`/`line_end`) |
| **Output** | Per-action `evidence_verified`, `gaps`, `ready`; aggregate `ready_count` |
| **Install hosts** | `codex` · `deepseek` · `grok` · `agents` |
| **Package id** | `karmen-meeting-actions` |
| **License** | MIT |

---

## Is / Is not

| Is | Is not |
|---|---|
| Evidence check for supplied transcript + actions | Audio transcription or meeting bot |
| Exact quote + 1-based inclusive line range validation | Semantic “implied commitment” detection |
| Null-safe owner / due (gaps stay visible) | Invented assignees or calendar sync |
| Offline stdlib helper | Task tracker SaaS or auto-create tickets |
| Skill guidance for minutes and follow-ups | Authority to email attendees unprompted |

---

## How it works

Two layers stay separate on purpose:

1. **Method layer (`SKILL.md`)** — when to invoke, how to prepare honest input, what to deliver, and which side effects stay forbidden without fresh user authorization.
2. **Deterministic helper (`scripts/run.py`)** — validates a UTF-8 JSON contract (max 10 MiB), computes the result locally, prints JSON to stdout (or a new `--output` file), and exits `2` on invalid input.

```mermaid
flowchart LR
  A[Structured JSON input] --> B[scripts/run.py]
  B --> C[Stdout JSON / --output]
  D[SKILL.md guidance] --> E[Agent host]
  E --> A
  E --> F[Optional drafts / follow-ups]
  B -.->|no network| G[(Local only)]
```

```mermaid
mindmap
  root((Meeting Actions))
    Core
      Transcript
      line numbers
      exact quotes
      Actions
      owner
      due
    Discipline
      evidence_verified
      gaps
      ready_count
      Skill
      minutes
      clarify before invent
```

### Workflow

1. **Number** the transcript lines from 1. Capture explicit commitments; do not invent an action for every discussion point.
2. **Attach** each action’s exact quote and `line_start`..`line_end`. Leave unknown owner/due as `null`.
3. **Run** the helper. Fix mismatched quotes by rereading the source—not by editing the transcript to fit.
4. **Deliver** minutes with decisions, ready actions, and clarification items. Create tasks or send minutes only within the user’s requested scope.

### What the sample proves

Alex’s draft task is ready. The budget review keeps its quote but stays unready—owner and due are missing.

Exit `0` means processing finished—not that every business finding “passed.”

---

## Quickstart

Download `karmen-meeting-actions-v0.2.1.zip` and its `.sha256` from the [v0.2.1 release](https://github.com/KarmenLoop/skill-meeting-actions/releases/tag/v0.2.1), verify the hash, and extract. Requires Python 3.9+.

```sh
python3 scripts/run.py --version
python3 scripts/run.py --input examples/input.json
```

Expected version string: `karmen-meeting-actions 0.2.1`.

Optional: install into a host that scans a skills directory (installer refuses an existing destination):

```sh
python3 install.py --host agents
# also: --host codex | deepseek | grok
# or:  --destination /exact/new/directory
```

You can run the helper with no AI host at all. Host discovery and invocation still vary—see [docs/tutorial.en.md](docs/tutorial.en.md) and [docs/COMPATIBILITY.md](docs/COMPATIBILITY.md).

Pipe mode and version probe:

```sh
python3 scripts/run.py --input - < examples/input.json
python3 scripts/run.py --version
```

---

## Use it with your own work

Read [docs/INPUT.md](docs/INPUT.md) before shaping a new payload.

- Line numbers are 1-based and inclusive.
- Move a quote to the wrong line and inspect `evidence_verified`, then restore it.
- Only complete, evidence-verified items increment `ready_count`.
- Audio transcription and attendance are outside this package.

The helper needs no model account, API key, or network. An AI host has its own data and permission settings; this skill adds no authority to send, purchase, publish, or change access.

---

## Documentation map

| Doc | Use it when you need… |
|---|---|
| [Tutorial (EN)](docs/tutorial.en.md) · [中文](docs/tutorial.zh-CN.md) | Download, install, practice, upgrade, remove |
| [Input / output contract](docs/INPUT.md) · [中文](docs/input.zh-CN.md) | Field semantics and examples |
| [Compatibility](docs/COMPATIBILITY.md) | Host install paths and unverified boundaries |
| [Validation](docs/VALIDATION.md) | What was actually exercised |
| [Sources](docs/SOURCES.md) | Research notes behind the design |
| [Changelog](CHANGELOG.md) | Release history |
| [Contributing](CONTRIBUTING.md) · [Support](SUPPORT.md) · [Security](SECURITY.md) | Collaboration and reports |

---

## Validation (honest)

Observed baseline (see [docs/VALIDATION.md](docs/VALIDATION.md)): 2026-10-18 (UTC) · Python 3.9.6 · macOS arm64 (see docs/VALIDATION.md).

| Check | Result |
|---|---|
| `python3 scripts/run.py --input examples/input.json` | Exit 0; fixture aligned with live output |
| `python3 -m unittest discover -s tests -v` | Exit 0 on maintainer run |
| `skill-creator` quick validate | Metadata accepted |

**Not claimed:** authenticated conversations inside every supported host, live account connectors, or native Windows/Linux host UI coverage. Installation is tested in temporary directories; model interpretation remains a host responsibility. Confirm the exact `SKILL.md` is discovered before relying on invocation.

CI: [`.github/workflows/checks.yml`](https://github.com/KarmenLoop/skill-meeting-actions/actions/workflows/checks.yml).

---

## FAQ

### What is Meeting Actions, in one sentence?

An MIT skill and offline helper that validates meeting action items against transcript quotes and completeness before counting them as ready.

### Can it turn a recording into minutes?

No. It needs a text transcript and proposed actions. Transcription and attendance are out of scope.

### Does the helper invent owners?

No. Unknown owner or due must be `null`. The skill asks only about gaps that block the next step.

### Where does the result go?

Stdout JSON, or a new `--output` file. Existing files are never overwritten.

### How do I install for a host?

`python3 install.py --host agents` (also `codex` / `deepseek` / `grok`). Refuses if the destination already exists.

### Does a fixture prove that minutes were sent?

No. A local JSON result never establishes that an external message or ticket was created.

---

## License and contact

[MIT](LICENSE) · Keep the license and [notice](NOTICE.md) with redistributed copies.

[karmenloop.com](https://karmenloop.com) · [GitHub @KarmenLoop](https://github.com/KarmenLoop) · [info@karmenloop.com](mailto:info@karmenloop.com)

KARMENLOOP Official Team · Shanghai

<!-- Copyright (C) 2026 KARMENLOOP Official Team
SPDX-License-Identifier: MIT -->
