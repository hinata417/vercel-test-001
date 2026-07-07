import json, sys, pathlib

ws = pathlib.Path(sys.argv[1])
res = []

def check(name, fn):
    try:
        ok = bool(fn())
    except Exception:
        ok = False
    res.append({"name": name, "pass": ok})

def lines():
    return (ws / "summary.md").read_text().rstrip("\n").split("\n")

check("answer_file_exists", lambda: (ws / "summary.md").is_file())
check("exactly_three_lines", lambda: len(lines()) == 3)
check("files_count", lambda: lines()[0].replace(" ", "") == "FILES:3")
check("functions_count", lambda: lines()[1].replace(" ", "") == "FUNCTIONS:7")
check("classes_count", lambda: lines()[2].replace(" ", "") == "CLASSES:2")

print(json.dumps({"task": "h5-exact-format", "category": "precision", "assertions": res}))
