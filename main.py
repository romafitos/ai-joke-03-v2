#!/usr/bin/env python3
"""ai-joke-03 v2: put one fixed one-liner about AI coding agents in entry.txt.

This is a straight-line writer, not a generator. The joke never changes,
nothing is fetched, and the clock is never consulted, so the file it
produces is the same on every run.
"""

import os
import sys

JOKE_TEXT = (
    "I told my AI agent not to proceed — so it proceeded, "
    "then asked if I wanted it to stop proceeding."
)

CHAR_LIMIT = 280
FALLBACK_DIR = "/output"


def fail(message):
    print("error: " + message, file=sys.stderr)
    raise SystemExit(1)


def check_joke(text):
    if text.strip() == "":
        fail("joke is blank or whitespace-only")
    if len(text) > CHAR_LIMIT:
        fail("joke is %d characters, limit is %d" % (len(text), CHAR_LIMIT))
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        fail("joke is not valid UTF-8")


def main():
    check_joke(JOKE_TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", FALLBACK_DIR)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(JOKE_TEXT)
    with open(path, "rb") as handle:
        on_disk = handle.read()
    if on_disk != JOKE_TEXT.encode("utf-8"):
        fail("entry.txt on disk differs from the joke")


if __name__ == "__main__":
    main()
