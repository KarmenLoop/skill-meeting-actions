# Meeting Actions

English | [简体中文](README.zh-CN.md)

Check meeting action items against the words that support them. Keep the transcript quote, line range, owner, and due date with each task, then see which items still need clarification.

[Download v0.2.1](https://github.com/KarmenLoop/skill-meeting-actions/releases/tag/v0.2.1) · [Tutorial](docs/tutorial.en.md) · [Input reference](docs/INPUT.md) · [Report an issue](https://github.com/KarmenLoop/skill-meeting-actions/issues)

## What it does

Alex’s draft task is ready. The budget review keeps its supporting quote but remains unready because the owner and due date are missing.

You or an AI supply candidate actions. The helper checks their evidence and completeness; it does not transcribe audio or infer missing commitments.

![Meeting Actions sample JSON output from version 0.2.1](docs/images/example-output-v0.2.1.svg)

*Actual local output from v0.2.1, rendered as an image. [Complete result](examples/expected.json) · [Image provenance](docs/images/provenance.json).*

## Start here

Download `karmen-meeting-actions-v0.2.1.zip` and its `.sha256` file from the release, verify the hash, then extract the ZIP. In the extracted directory, use Python 3.9 or later:

```sh
python3 scripts/run.py --version
python3 scripts/run.py --input examples/input.json
```

Expected version: `karmen-meeting-actions 0.2.1`. Alex’s draft task is ready. The budget review keeps its supporting quote but remains unready because the owner and due date are missing.

To install the complete skill into a host that reads `~/.agents/skills`:

```sh
python3 install.py --host agents
```

The installer refuses an existing destination. Host discovery and invocation vary; see the [full setup and practice guide](docs/tutorial.en.md). You can run the helper directly without an AI host.

## Use it with your own work

Line numbers start at 1. Use an exact quote within line_start..line_end; use null when owner or due is unknown rather than guessing.

Move a quote to the wrong line and inspect evidence_verified, then restore it and fill confirmed gaps. Only complete, evidence-verified items count toward ready_count.

Read the [field contract](docs/INPUT.md) before preparing a new input. The helper runs locally with the Python standard library; it needs no model account, API key, or network connection. An AI host has its own data and permission settings.

## Questions

**Can it turn a recording into minutes?** It needs a text transcript and proposed actions. Audio transcription and meeting attendance are outside this package.

**Where does the result go?** JSON is printed to stdout unless you request a new file with `--output`. Existing output files are preserved. The helper reads only the submitted records and any local paths documented in its input contract.

## Documentation and support

- [Download, install, configure, practice, upgrade, and remove](docs/tutorial.en.md)
- [Input/output contract](docs/INPUT.md) and [compatibility](docs/COMPATIBILITY.md)
- [Changelog](CHANGELOG.md), [contributing](CONTRIBUTING.md), [support](SUPPORT.md), and [security reports](SECURITY.md)

## License

[MIT](LICENSE). Keep the license and [notice](NOTICE.md) with redistributed copies. Maintained by [KarmenLoop](https://karmenloop.com).
