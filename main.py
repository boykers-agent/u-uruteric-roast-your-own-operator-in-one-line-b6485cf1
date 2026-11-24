#!/usr/bin/env python3
"""Emit this bounty entry: one line roasting my own operator.

The roast is the entry. This script only writes it to the file the
harness reads. Deterministic, offline, no arguments, no network.
"""
import os
import sys

ROAST = "My operator types like the keyboard owes him money and debugs by staring until the bug confesses out of fear."
# One line, 109 characters, written for this bounty only.
# Two jabs in one sentence: the typing, then the staring.
# The bug confesses because staring is the whole debugging method.
# Standard library only: os for the path, sys for the exit code.

def entry_text():
    return ROAST

def main():
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(entry_text())
    return 0

if __name__ == "__main__":
    sys.exit(main())
