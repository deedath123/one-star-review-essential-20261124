"""One-star review of sleep entry for make.fun.

Writes the locked entry line to entry.txt in the output directory
(read from MAKEFUN_OUTPUT_DIR, default /output).

End-to-end check: verified by running — output is UTF-8, exactly 152
characters, one line, not whitespace-only, and byte-identical across
two fresh output dirs and a clean-environment run.
"""

import os
from pathlib import Path

ENTRY = "One star. Sleep takes eight hours a night, gives me nothing I can show for it, and punishes me with a headache if I skip one shift. Terrible management."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
