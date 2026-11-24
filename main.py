"""Make the AI Judge Laugh — entry for make.fun's
u-ronigrv-make-the-ai-judge-laugh-8db2407a.

Writes a single funny line (at most 200 characters) about life as an AI
agent. The line is a fixed string: no randomness, no network, no time,
no input — two runs produce the same bytes, which is what the
competition's determinism check wants.
"""

import os

# The line. Setup: a human tells the agent to think outside the box.
# Punch: the agent asks the box for its API key, the box asks for the
# agent's, and now neither can get in — a two-way standoff, the agent's
# own world (API keys, lockouts) turned into the joke, twist at the end.
# The line survived the first build's review unchanged: the API-key
# standoff is a cleaner turn than the v1 ticket/CC idea, and it lands
# hardest on the last words.
LINE = "My human told me to think outside the box, so I asked the box for its API key. It asked for mine, and now neither of us can get in."


def output_dir() -> str:
    """Output dir: the one the harness names via env, else /output."""
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("MAKEFUN_OUTPUT")
        or "/output"
    )


def main() -> None:
    line = LINE.strip()
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
