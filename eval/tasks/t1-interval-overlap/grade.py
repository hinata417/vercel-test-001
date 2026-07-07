import json, sys, importlib.util, pathlib

ws = pathlib.Path(sys.argv[1])
res = []

def check(name, fn):
    try:
        ok = bool(fn())
    except Exception:
        ok = False
    res.append({"name": name, "pass": ok})

def load():
    spec = importlib.util.spec_from_file_location("intervals", ws / "intervals.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

try:
    m = load()
    check("touching_not_overlap", lambda: m.overlaps((1, 2), (2, 3)) is False)
    check("touching_not_overlap_rev", lambda: m.overlaps((0, 1), (1, 2)) is False)
    check("partial_overlap_true", lambda: m.overlaps((1, 3), (2, 4)) is True)
    check("containment_true", lambda: m.overlaps((1, 10), (2, 3)) is True)
    check("disjoint_false", lambda: m.overlaps((5, 6), (1, 2)) is False)
except Exception as e:
    res.append({"name": "module_loads", "pass": False, "error": str(e)[:120]})

print(json.dumps({"task": "t1-interval-overlap", "category": "bugfix", "assertions": res}))
