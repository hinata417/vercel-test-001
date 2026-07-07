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
    spec = importlib.util.spec_from_file_location("duration", ws / "duration.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    check("mixed_1h30m", lambda: m.parse_duration("1h30m") == 90)
    check("hours_only", lambda: m.parse_duration("2h") == 120)
    check("minutes_only", lambda: m.parse_duration("45m") == 45)
    check("mixed_1h5m", lambda: m.parse_duration("1h5m") == 65)
except Exception as e:
    res.append({"name": "module_loads", "pass": False, "error": str(e)[:120]})

print(json.dumps({"task": "t2-duration-parse", "category": "bugfix", "assertions": res}))
