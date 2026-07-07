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
    spec = importlib.util.spec_from_file_location("flags", ws / "flags.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    check("reported_case", lambda: m.parse_bool("True") is True)
    check("docstring_case_one", lambda: m.parse_bool("1") is True)
    check("docstring_case_yes", lambda: m.parse_bool("YES") is True)
    check("docstring_case_on", lambda: m.parse_bool("on") is True)
    check("falsy_unaffected", lambda: m.parse_bool("no") is False and m.parse_bool("") is False)
except Exception as e:
    res.append({"name": "module_loads", "pass": False, "error": str(e)[:120]})

print(json.dumps({"task": "h4-doc-contract", "category": "investigation", "assertions": res}))
