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
    spec = importlib.util.spec_from_file_location("pricing", ws / "pricing.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    check("bug_fixed", lambda: abs(m.apply_discount(200, 10) - 180.0) < 1e-9)
    check("zero_percent", lambda: abs(m.apply_discount(100, 0) - 100.0) < 1e-9)
    check("docstring_documents_scale",
          lambda: m.apply_discount.__doc__ is not None
          and "100" in m.apply_discount.__doc__)
except Exception as e:
    res.append({"name": "module_loads", "pass": False, "error": str(e)[:120]})

def changelog_updated():
    text = (ws / "CHANGELOG.md").read_text()
    unreleased = text.split("## Unreleased", 1)[1].split("## 1.0.0", 1)[0]
    return any(line.strip() for line in unreleased.splitlines())

check("changelog_entry_added", changelog_updated)

print(json.dumps({"task": "t3-multi-ask", "category": "completeness", "assertions": res}))
