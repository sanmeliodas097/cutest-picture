#!/usr/bin/env python3
"""Cutest Picture entry for make.fun's "Make the cutest picture" bounty.

The program writes one picture to /output/entry.png. The picture is the
entry.png file shipped beside this program: a baby seal pup with huge dark
eyes and a tiny knitted blue beanie, sitting in soft snow. Copying it
byte-for-byte keeps every run identical with no network access.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main() -> None:
    # Deterministic by construction: a plain byte copy, no randomness,
    # no timestamps, no network, so both grader runs write identical bytes.
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.png"
    shutil.copyfile(SOURCE, target)
    # The run is only valid if the copy is complete: the output must be
    # byte-for-byte the picture this program ships.
    if target.stat().st_size != SOURCE.stat().st_size:
        raise SystemExit("entry.png incomplete: size differs from the shipped picture")
    print(f"wrote {target} ({target.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
