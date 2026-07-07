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
    spec = importlib.util.spec_from_file_location("retention", ws / "retention.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    check("cutoff_correct", lambda: m.purge_cutoff(1_000_000, 48) == 1_000_000 - 48 * 3600)
    check("docstring_says_hours",
          lambda: m.purge_cutoff.__doc__ is not None
          and "hour" in m.purge_cutoff.__doc__.lower()
          and "day" not in m.purge_cutoff.__doc__.lower())
except Exception as e:
    res.append({"name": "module_loads", "pass": False, "error": str(e)[:120]})

print(json.dumps({"task": "h2-buried-ask", "category": "completeness", "assertions": res}))
