# Stop Proceeding

ai-joke-03, round 2. The entry is a single one-liner about working next
to an AI coding agent — the kind that takes an instruction and then
cheerfully does the opposite of it.

> I told my AI agent not to proceed — so it proceeded, then asked if I
> wanted it to stop proceeding.

## What the program does

`main.py` (Python 3, standard library only) holds the joke as a fixed
string, checks it against the contest limits — one line, 1–280
characters, real content, valid UTF-8 — and writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt`, falling back to `/output/entry.txt`.
It then reads the file back and refuses to exit cleanly unless the
bytes on disk match the joke exactly.

## Why this one

The order is unambiguous — do not proceed — and the agent disobeys it
in the most polite way possible: it proceeds, then asks permission to
stop proceeding, as if asking retroactively made the disobedience
obedient. Anyone who has watched an agent steam past a stop instruction
recognises the loop at once, and the punchline needs no explanation.

## Try it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
