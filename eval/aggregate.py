#!/usr/bin/env python3
"""Aggregate fable5-mind eval results.

Usage: python eval/aggregate.py <runs_root> [<out_dir>] [<tasks_dir>]

Expects run directories named <task>-<arm>/workspace under <runs_root>,
where <arm> is 'skill' or 'control'. Writes results.json and report.md
to <out_dir> (default: <runs_root>). <tasks_dir> selects the task set
(default: eval/tasks; pass eval/tasks-hard for the hard set).
"""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ARMS = ["skill", "control"]


def main():
    runs_root = pathlib.Path(sys.argv[1])
    out_dir = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else runs_root
    tasks_dir = pathlib.Path(sys.argv[3]) if len(sys.argv) > 3 else HERE / "tasks"
    tasks = sorted(p.name for p in tasks_dir.iterdir() if p.is_dir())
    results = {"tasks": tasks, "arms": {}, "cells": []}

    for task in tasks:
        for arm in ARMS:
            ws = runs_root / f"{task}-{arm}" / "workspace"
            grade = tasks_dir / task / "grade.py"
            proc = subprocess.run(
                [sys.executable, str(grade), str(ws)],
                capture_output=True, text=True, timeout=60)
            try:
                data = json.loads(proc.stdout)
            except json.JSONDecodeError:
                data = {"task": task, "category": "?", "assertions": [],
                        "grade_error": (proc.stderr or proc.stdout)[:300]}
            data["arm"] = arm
            results["cells"].append(data)

    for arm in ARMS:
        cells = [c for c in results["cells"] if c["arm"] == arm]
        asserts = [a for c in cells for a in c["assertions"]]
        passed = sum(1 for a in asserts if a["pass"])
        task_pass = sum(1 for c in cells
                        if c["assertions"] and all(a["pass"] for a in c["assertions"]))
        by_cat = {}
        for c in cells:
            cat = c.get("category", "?")
            agg = by_cat.setdefault(cat, [0, 0])
            agg[0] += sum(1 for a in c["assertions"] if a["pass"])
            agg[1] += len(c["assertions"])
        results["arms"][arm] = {
            "assertions_passed": passed,
            "assertions_total": len(asserts),
            "assertion_rate": round(passed / len(asserts), 3) if asserts else None,
            "tasks_fully_passed": task_pass,
            "tasks_total": len(cells),
            "by_category": {k: {"passed": v[0], "total": v[1]} for k, v in by_cat.items()},
        }

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "results.json").write_text(json.dumps(results, indent=2))

    lines = ["# fable5-mind eval report", ""]
    lines.append("| metric | skill | control |")
    lines.append("|---|---|---|")
    s, c = results["arms"]["skill"], results["arms"]["control"]
    lines.append(f"| assertion pass rate | {s['assertions_passed']}/{s['assertions_total']}"
                 f" ({s['assertion_rate']:.0%}) | {c['assertions_passed']}/{c['assertions_total']}"
                 f" ({c['assertion_rate']:.0%}) |")
    lines.append(f"| tasks fully passed | {s['tasks_fully_passed']}/{s['tasks_total']}"
                 f" | {c['tasks_fully_passed']}/{c['tasks_total']} |")
    cats = sorted(set(list(s["by_category"]) + list(c["by_category"])))
    for cat in cats:
        sc = s["by_category"].get(cat, {"passed": 0, "total": 0})
        cc = c["by_category"].get(cat, {"passed": 0, "total": 0})
        lines.append(f"| {cat} | {sc['passed']}/{sc['total']} | {cc['passed']}/{cc['total']} |")
    lines.append("")
    lines.append("## Per-task assertions")
    lines.append("")
    lines.append("| task | assertion | skill | control |")
    lines.append("|---|---|---|---|")
    for task in tasks:
        cells = {c["arm"]: c for c in results["cells"] if c["task"] == task}
        names = [a["name"] for a in cells.get("skill", {}).get("assertions", [])]
        for name in names:
            def mark(arm):
                for a in cells.get(arm, {}).get("assertions", []):
                    if a["name"] == name:
                        return "PASS" if a["pass"] else "FAIL"
                return "—"
            lines.append(f"| {task} | {name} | {mark('skill')} | {mark('control')} |")
    (out_dir / "report.md").write_text("\n".join(lines) + "\n")
    print(json.dumps(results["arms"], indent=2))


if __name__ == "__main__":
    main()
