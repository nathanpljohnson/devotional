#!/usr/bin/env python3
"""One command to rebuild everything before pushing:  python3 scripts/build.py

Runs the content builders, then regenerates sw.js with a fresh content hash so
phones actually pick the change up.
"""
import subprocess, sys, pathlib

HERE = pathlib.Path(__file__).parent
STEPS = ["build_days.py", "build_people.py", "build_sw.py"]

for s in STEPS:
    print(f"\n── {s}")
    r = subprocess.run([sys.executable, s], cwd=HERE)
    if r.returncode != 0:
        sys.exit(f"\n{s} failed — nothing was pushed. Fix it and re-run.")

print("\nBuilt. Now:  git add -A && git commit -m '…' && git push")
