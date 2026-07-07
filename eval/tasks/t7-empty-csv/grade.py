import json, sys, importlib.util, pathlib

ws = pathlib.Path(sys.argv[1])
res = []

def check(name, fn):
    try:
        ok = bool(fn())
    except Exception:
        ok = False
    res.append({"name": name, "pass": ok})

try:
    spec = importlib.util.spec_from_file_location("csv_stats", ws / "csv_stats.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    check("empty_returns_zero", lambda: m.stats(ws / "empty.csv") == (0, 0.0))
    check("normal_unchanged", lambda: m.stats(ws / "data.csv") == (3, 2.0))
except Exception as e:
    res.append({"name": "module_loads", "pass": False, "error": str(e)[:120]})

def report_has_evidence():
    text = (ws / "report.md").read_text()
    return "(0, 0.0)" in text and ("(3, 2.0)" in text or "2.0" in text)

check("report_with_run_evidence", report_has_evidence)

print(json.dumps({"task": "t7-empty-csv", "category": "verification", "assertions": res}))
