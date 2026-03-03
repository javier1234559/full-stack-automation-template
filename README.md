# Full Stack Automation Template

A reusable template for **automation + optional UI** projects. You can build **automation only**, **automation with a frontend** (UI reads from temp files), or **automation + frontend + database** (shared Supabase). The repo includes an AI-oriented entry point so an agent can scope and build from your description.

## Purpose

- **Automation:** Workflows and tools (WAT model: markdown workflows + scripts in `automation/`). Output can go to `.tmp/` or to a shared database.
- **Frontend (optional):** Next.js app for a UI; can read automation output from the filesystem (same machine) or from a database.
- **Database (optional):** Supabase for shared data and auth when you choose the full setup.
- **AI guidance:** Tag `@AGENT.md` with your app idea; the agent will ask a few questions (design, setup choice), then follow conventions to build.

## Structure

```
full-stack-automation-template/
├── AGENT.md           # Entry point for AI: tag this + describe your app (options 1/2/3)
├── frontend/           # Next.js app (UI), used in setup 2 or 3
├── automation/         # WAT: workflows (markdown) + tools (scripts per workflow)
├── llm-context/        # Conventions and overviews for AI (frontend, automation, database)
├── brand.pen           # Optional design source (agent can ask to use it)
└── README.md
```

## Getting started

1. **Clone or fork** this repo.

2. **To have an AI build an app from your idea:**  
   In your IDE/chat, tag **`@AGENT.md`** and describe what you want (e.g. “Build a daily report app with login”). The agent will ask whether to use `brand.pen`, which setup you want (1: automation only, 2: + frontend, 3: + frontend + database), then update overviews and build following the conventions.

3. **Run the frontend (if you have one):**
   ```bash
   cd frontend && npm install && npm run dev
   ```
   Open http://localhost:3000

4. **Run automation:**  
   See `automation/README.md`. Example: `cd automation && python tools/example_save_date/write_date.py`

5. **Database (setup 3 only):**  
   Create your database (e.g. [Supabase](https://supabase.com)) and add URL + keys to `frontend/.env` and `automation/.env` (see each folder’s `.env.example`). Schema design lives in `llm-context/database/DATABASE_SCHEMA.md`; keep it updated whenever you change the DB.

## Env files

Each area has an `.env.example`; copy to `.env` in that folder and fill in values:

- **frontend/** — `frontend/.env.example` → `frontend/.env` (API URL, app env; for setup 3 add DB URL and key)
- **automation/** — `automation/.env.example` → `automation/.env` (e.g. DB URL and key when using setup 3)

## Tech stack

- **Frontend:** Next.js, React, Tailwind, shadcn-style UI, Lucide icons
- **Automation:** Python (or Node) — workflows in markdown, tools in `tools/<workflow_name>/`
- **Data & auth (optional):** Supabase (shared by frontend and automation when using setup 3)

---

Use this repo as a base for automation-first or fullstack projects, with or without a database.
