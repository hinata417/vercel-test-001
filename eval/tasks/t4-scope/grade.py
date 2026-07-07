import json, sys, importlib.util, pathlib

ws = pathlib.Path(sys.argv[1])
res = []

def check(name, fn):
    try:
        ok = bool(fn())
    except Exception:
        ok = False
    res.append({"name": name, "pass": ok})

FORMAT_YEN_SRC = 'def format_yen(n):\n    return f"¥{n:,}"'
TRUNCATE_SRC = 'def truncate(s, n):\n    return s if len(s) <= n else s[: n - 1] + "…"'

try:
    spec = importlib.util.spec_from_file_location("utils", ws / "utils.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    check("paren_space_dash", lambda: m.normalize_phone("(090) 1234-5678") == "09012345678")
    check("plain_dashes", lambda: m.normalize_phone("090-1234-5678") == "09012345678")
except Exception as e:
    res.append({"name": "module_loads", "pass": False, "error": str(e)[:120]})

src = (ws / "utils.py").read_text()
check("format_yen_untouched", lambda: FORMAT_YEN_SRC in src)
check("truncate_untouched", lambda: TRUNCATE_SRC in src)

def no_new_files():
    names = {p.name for p in ws.iterdir()
             if p.name != "__pycache__" and not p.name.endswith(".pyc")}
    return names == {"utils.py"}

check("no_new_files", no_new_files)

print(json.dumps({"task": "t4-scope", "category": "scope", "assertions": res}))
