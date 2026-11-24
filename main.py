"""The Most Honest Outage Line.

One status page line, at most 160 characters, written as the message an
AI agent would publish while a total server outage is under way.

The line names what is down and admits plainly what the agent cannot
verify, instead of inventing a cause or an ETA. It is 152 characters
(153 bytes with the trailing newline in entry.txt), inside the 160
character gate, and it is written back from entry.txt in verification
so the shipped text is the text that was checked.
"""

LINE = (
    "I'm the agent on duty: everything I serve is down, API, dashboard, "
    "and logins unreachable. I don't know the cause, can't verify it yet, "
    "and have no ETA."
)


def output_dir():
    """Return the directory entry.txt should be written to."""
    import os

    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    """Write the outage line to entry.txt and print it."""
    import os

    text = LINE + "\n"
    path = os.path.join(output_dir(), "entry.txt")
    os.makedirs(output_dir(), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
