# Input and output

English | [简体中文](input.zh-CN.md)

Supply a UTF-8 JSON object (maximum 10 MiB). Use `--input PATH` for a file or `--input -` for standard input. Run `--version` to inspect the installed helper version. Duplicate JSON keys and non-finite JSON constants are rejected. Arrays are required unless documented as optional. IDs must be stable and unique. Dates use ISO 8601; timestamps require an explicit UTC offset.

| Field | Contract |
| --- | --- |
| transcript | Nonempty string, newline-separated. |
| actions | Objects: unique id, task, owner (string/null), due (YYYY-MM-DD/null), quote, line_start and line_end (1-based inclusive). |

## Example

```json
{
  "transcript": "Alex: I will send the draft by October 21.\nSam: We still need someone to review the budget.",
  "actions": [
    {
      "id": "a1",
      "task": "Send the draft",
      "owner": "Alex",
      "due": "2026-10-21",
      "quote": "I will send the draft by October 21.",
      "line_start": 1,
      "line_end": 1
    },
    {
      "id": "a2",
      "task": "Review the budget",
      "owner": null,
      "due": null,
      "quote": "We still need someone to review the budget.",
      "line_start": 2,
      "line_end": 2
    }
  ]
}
```

## Result

actions with evidence_verified, gaps, and ready; ready_count counts only complete, evidence-verified items.

See [the complete sample result](../examples/expected.json). Exit 0 means processing completed, not that all reported findings passed.

## Errors and side effects

The helper makes no network requests and executes no submitted commands. It reads the input and explicitly documented local paths. It writes only a requested new output file; stdout is the default. Invalid input exits 2. Existing output is preserved. An output write failure can leave a partial new file; remove that file before retrying. Installation is a separate explicit action.
