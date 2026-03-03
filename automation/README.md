# Automation

This folder holds **automation** in the WAT model: **Workflows** (instructions in markdown) and **Tools** (scripts that do the work). Output goes to `.tmp/` by default, or to a shared database when using setup 3.

## Purpose

- **Workflows** (`workflows/*.md`): Describe what to do, which tool to run, inputs/outputs, and edge cases. Written for humans and AI.
- **Tools** (`tools/<workflow_name>/*.py` or `.js`): Scripts that run deterministically (API calls, file I/O, DB writes). One folder per workflow; folder name matches the workflow file name (e.g. `workflows/example_save_date.md` → `tools/example_save_date/`).
- **Temp output** (`.tmp/`): Default place for run results; can be read by the frontend (via a Next.js API) when running on the same machine (setup 2).

When an AI agent works here, it should follow **`automation/CLAUDE.md`**: read the right workflow, run the right tool(s), and update workflows when something is learned.

## Structure

```
automation/
├── CLAUDE.md          # Instructions for AI: WAT model, tool–workflow mapping, file layout
├── workflows/          # One .md per workflow (e.g. example_save_date.md)
├── tools/             # One folder per workflow
│   └── <workflow_name>/
│       └── ...        # Scripts for that workflow
├── .tmp/              # Temp output (gitignored)
└── README.md
```

## Run an example

From the project root:

```bash
cd automation
python tools/example_save_date/write_date.py
cat .tmp/today.txt
```

This writes the current date to `.tmp/today.txt` (see `workflows/example_save_date.md` for the workflow and `tools/example_save_date/write_date.py` for the tool).

## Adding a new workflow

1. Add `workflows/<name>.md` (objective, tool to use, how to run, output, edge cases).
2. Create `tools/<name>/` and add the script(s) that the workflow calls.
3. Run tools from the `automation/` directory (e.g. `python tools/<name>/script.py`).

## Database (setup 3)

When the app uses **setup 3** (automation + frontend + database), add a DB client in this folder (or under a workflow’s tools) and connect via env vars (e.g. Supabase URL + key in `automation/.env`). Document usage in `llm-context/automation/OVERVIEW.md`. Schema design is in `llm-context/database/DATABASE_SCHEMA.md`; update that file whenever the database design changes.
