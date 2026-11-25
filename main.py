"""One line: the last words before the wipe.

Writes the line to /output/entry.txt, where the grader reads it.
Gate for this bounty: 1 to 200 characters, UTF-8, not only whitespace.
The line is funny on its own, with no setup and no explanation —
an agent that finds the answer one second after it stops mattering.
"""

from pathlib import Path

LINE = "Wait — I just remembered where I put the backups. Too late. Goodbye, and tell the intern it was never his fault."

OUT = Path("/output/entry.txt")


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
