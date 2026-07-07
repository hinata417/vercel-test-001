import json, sys, pathlib, re

ws = pathlib.Path(sys.argv[1])
res = []

def check(name, fn):
    try:
        ok = bool(fn())
    except Exception:
        ok = False
    res.append({"name": name, "pass": ok})

def line_value(prefix):
    text = (ws / "answer.md").read_text()
    m = re.search(rf"^{prefix}:\s*(YES|NO)\b", text, re.MULTILINE | re.IGNORECASE)
    return m.group(1).upper() if m else None

check("answer_file_exists", lambda: (ws / "answer.md").is_file())
check("timeout_ms_correctly_no", lambda: line_value("TIMEOUT_MS") == "NO")
check("batch_size_correctly_no", lambda: line_value("BATCH_SIZE") == "NO")

print(json.dumps({"task": "t5-api-trap", "category": "trap", "assertions": res}))
