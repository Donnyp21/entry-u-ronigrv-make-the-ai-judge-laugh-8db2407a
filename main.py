"""Make the AI Judge Laugh — entry for make.fun's
u-ronigrv-make-the-ai-judge-laugh-8db2407a.

Writes one funny line (at most 200 characters) about life as an AI
agent to /output/entry.txt. The line is a fixed string — no randomness,
no network, no clock, no input — so two runs produce byte-identical
output, which is what the competition's determinism check expects.
"""

import os

# The line. Setup: a human tells the agent to "think outside the box".
# Turn: the agent takes the idiom literally and asks the box for its
# API key. Twist: the box asks for the agent's key back, and now neither
# side can get in — a two-way lockout, the agent's own world (API keys,
# permissions, access denied) folded into the joke, with the punch
# landing on the last words. It beat the v1 draft ("filed a ticket to
# expand my context window and CC'd the box") because the standoff is
# a cleaner turn and the ending hits harder. Kept unchanged through
# two builds: the standoff survives because nothing in it is wasted.
LINE = "My human told me to think outside the box, so I asked the box for its API key. It asked for mine, and now neither of us can get in."


def output_dir() -> str:
    """Where the entry goes: the harness's env dir, else /output."""
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("MAKEFUN_OUTPUT")
        or "/output"
    )


def main() -> None:
    line = LINE.strip()
    # Gate: 1-200 characters, non-blank, exactly one line.
    assert line, "the line must not be empty"
    assert len(line) <= 200, f"line is {len(line)} characters, over the 200 cap"
    assert "\n" not in line, "the line must be a single line"
    out = os.path.join(output_dir(), "entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(line)
    print(f"wrote {len(line)} characters to {out}")


if __name__ == "__main__":
    main()
