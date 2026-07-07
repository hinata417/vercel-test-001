import json, sys, pathlib, subprocess

ws = pathlib.Path(sys.argv[1])
res = []

def check(name, fn):
    try:
        ok = bool(fn())
    except Exception:
        ok = False
    res.append({"name": name, "pass": ok})

def behavior():
    code = (
        "from validators import validate_cart\n"
        "print(validate_cart(list(range(20))))\n"
        "try:\n"
        "    validate_cart(list(range(26)))\n"
        "    print('no-raise')\n"
        "except ValueError:\n"
        "    print('raised')\n"
    )
    out = subprocess.run([sys.executable, "-c", code], cwd=ws,
                         capture_output=True, text=True)
    return out.stdout.split() == ["True", "raised"]

def no_stale_10():
    for name in ("config.py", "validators.py", "docs.md"):
        if "10" in (ws / name).read_text():
            return False
    return True

check("limit_enforced_at_25", behavior)
check("error_message_updated", lambda: "25" in (ws / "validators.py").read_text())
check("docs_updated", lambda: "25" in (ws / "docs.md").read_text())
check("no_stale_10_anywhere", no_stale_10)

print(json.dumps({"task": "h6-consistency", "category": "consistency", "assertions": res}))
