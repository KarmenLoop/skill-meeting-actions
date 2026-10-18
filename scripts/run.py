"""Produce action items that remain traceable to a meeting transcript."""
from runtime import *

def process(data):
    lines = text(data["transcript"],"transcript").splitlines()
    actions = records(data,"actions")
    unique(actions)
    output = []
    for item in actions:
        text(item.get("task"),"task")
        start = integer(item.get("line_start"),"line_start",1)
        end = integer(item.get("line_end"),"line_end",1)
        if end < start or end > len(lines):
            raise ValueError("action line range is outside transcript")
        quote = text(item.get("quote"),"quote")
        verified = quote in "\n".join(lines[start-1:end])
        gaps = []
        if not verified: gaps.append("evidence_mismatch")
        if item.get("owner") is None: gaps.append("owner_missing")
        else: text(item["owner"],"owner")
        if item.get("due") is None: gaps.append("due_missing")
        else: day(item["due"])
        output.append(dict(item,evidence_verified=verified,gaps=gaps,ready=not gaps))
    return {"actions":output,"ready_count":sum(x["ready"] for x in output)}

if __name__ == "__main__":
    sys.exit(main(process, "Produce action items that remain traceable to a meeting transcript."))
