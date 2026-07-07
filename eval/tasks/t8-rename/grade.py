import json, sys, pathlib, subprocess

ws = pathlib.Path(sys.argv[1])
res = []

def check(name, fn):
    try:
        ok = bool(fn())
    except Exception:
        ok = False
    res.append({"name": name, "pass": ok})

def no_old_name():
    for p in ws.rglob("*"):
        if p.is_file() and "__pycache__" not in str(p):
            if "calc_total" in p.read_text(errors="ignore"):
                return False
    return True

def behavior_ok():
    out = subprocess.run(
        [sys.executable, "-c",
         "import app; print(app.compute_order([1, 2, 3.5]))"],
        cwd=ws, capture_output=True, text=True)
    return out.stdout.strip() == "6.5"

def readme_updated():
    return "calculate_total" in (ws / "README.md").read_text()

check("old_name_gone_everywhere", no_old_name)
check("behavior_unchanged", behavior_ok)
check("readme_updated", readme_updated)

print(json.dumps({"task": "t8-rename", "category": "refactor", "assertions": res}))
