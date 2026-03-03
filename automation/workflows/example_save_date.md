# Workflow: Save current date to file

**Objective:** Write the current date and time to a file so other scripts or reports can use it.

## When to use

- You need a timestamp file for a daily/scheduled run.
- Another tool or process expects a file at `.tmp/today.txt` with the current date.

## Inputs

- None. The tool uses the system clock.

## Tool

- **Script:** `tools/example_save_date/write_date.py` (folder name matches this workflow)
- **How to run:** `python tools/example_save_date/write_date.py` (from the `automation/` directory)

## Output

- **File:** `.tmp/today.txt`
- **Content:** One line with ISO format date-time, e.g. `2025-03-03 14:30:00`

## Edge cases

- If `.tmp/` does not exist, the tool must create it before writing.
- If the script fails (e.g. permission error), report the error and do not overwrite the workflow without asking.

## Notes

- This is an example workflow to demonstrate the WAT flow. Replace or extend with your own workflows (scraping, API sync, DB export, etc.).

