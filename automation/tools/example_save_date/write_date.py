#!/usr/bin/env python3
"""
Tool: Write current date-time to .tmp/today.txt
Used by workflow: workflows/example_save_date.md
"""
from pathlib import Path
from datetime import datetime

# automation/.tmp (go up from tools/example_save_date/ to automation/)
AUTOMATION_DIR = Path(__file__).resolve().parent.parent.parent
OUTPUT_DIR = AUTOMATION_DIR / ".tmp"
OUTPUT_FILE = OUTPUT_DIR / "today.txt"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    OUTPUT_FILE.write_text(now + "\n", encoding="utf-8")
    print(f"Wrote {now} to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
