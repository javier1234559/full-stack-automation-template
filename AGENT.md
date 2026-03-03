# Agent entry point

When someone clones this repo and tags **this file** (`@AGENT.md`) with a request to build an app, you are the agent. They usually only say they want to build an app and list the features they want. Follow this flow in order.

---

## 1. Read this file first

You are in the **full-stack-automation-template**: one frontend (Next.js), one automation layer (WAT: workflows + tools), optional shared Supabase. Your job is to orchestrate: decide what to build, then follow the conventions for each part.

---

## 2. Clarify before updating (ask only what’s missing)

**2.1. Check if they already stated requirements.**  
When they tagged this file, did they already describe the app and desired features? If **yes**, use that; do not ask again for the same. If **no**, ask them to briefly describe what they want to build and which features they need.

**2.2. Ask about design (brand.pen).**  
- **Question:** *"Do you want to use the current design in `brand.pen`? (Yes / No)"*  
- **Note:** No = they will adjust the design later or do not need it; proceed with a generic or described design.

**2.3. Ask which setup they want (one choice).**  
Ask the user to pick **one** of the following. Present the question and the notes so they can choose clearly:

- **Question:** *"Which setup do you want? Reply with 1, 2, or 3."*

| Option | Setup | Note for the user |
|--------|--------|--------------------|
| **1** | **Automation only** | Automation runs and writes results to temp (`.tmp/`). You get results by asking the AI or reading temp. No UI, no database. Simplest. |
| **2** | **Automation + frontend** | Automation writes to temp; the frontend has a UI that shows that output by reading from the filesystem (Next.js API reads `.tmp/`). **Limited:** only works when frontend and automation run on the **same machine**; no history, no persistence across runs. Good for local, simple dashboards. |
| **3** | **Automation + frontend + database** | Automation and frontend both use a shared database (e.g. Supabase). Data is persistent, you can have history, and it works even when automation runs elsewhere (e.g. cron on a server). Most complete option. |

- After they choose, you will: always do **Automation path** (step 3); do **Frontend path** (step 4) only for **2 or 3**; do **Database path** (step 5) only for **3**.

---

## 3. Automation path

1. **Update** `llm-context/automation/OVERVIEW.md`: write a short overview of what automation this app needs (e.g. scheduled jobs, one-off scripts, which workflows/tools).
2. **Read** `automation/CLAUDE.md`: it defines the WAT model (Workflows, Agents, Tools), folder layout (`workflows/`, `tools/<workflow_name>/`, `.tmp/`), and how to add workflows and tools.
3. **Build** automation: create or update workflows in `automation/workflows/` and tools in `automation/tools/<workflow_name>/` following that doc.
4. **Database (option 3 only):** If the app uses a shared database, add connection in automation via env (e.g. Supabase client in a folder under `automation/`). Document in `llm-context/automation/OVERVIEW.md`. No `supabase/` folder in the repo; schema lives in `llm-context/database/DATABASE_SCHEMA.md`.

---

## 4. Frontend path (only if user chose option 2 or 3 in step 2.3)

1. **Update** `llm-context/frontend/OVERVIEW.md`: write a short overview of what the frontend app does (screens, main features, auth if any). For option 2, note that the UI reads automation output from the filesystem (Next API → `.tmp/`).
2. **Read** `llm-context/frontend/CONVENTION.md`: it defines the frontend structure (features, services, hooks, views, app routes, component folders, shadcn, Lucide, etc.).
3. **Build** the frontend following that convention: add features under `frontend/src/feature/`, shared pieces under `frontend/src/component/`, `lib/`, `service/`, and wire routes in `frontend/src/app/` that only import views. For option 2, add API route(s) that read from `automation/.tmp/` and return data for the UI.

---

## 5. Database path (only if user chose option 3 in step 2.3)

1. **Update** `llm-context/database/OVERVIEW.md`: short overview of what the database is for (what data, shared by frontend and automation). Note that frontend and automation each have their own folder/client and connect via env (e.g. Supabase URL + key); no shared `supabase/` folder in the repo.
2. **Update** `llm-context/database/DATABASE_SCHEMA.md`: design the schema (tables, columns, relationships). This file is the **single source of truth** for the DB design. Describe tables in plain language or SQL-like form so that anyone implementing the DB (e.g. in Supabase dashboard or elsewhere) can follow it.
3. **Build**: add DB client/connection in `frontend/` and in `automation/` as needed (e.g. Supabase client), using env vars to connect. The user will create the actual database (e.g. Supabase project) and apply the schema from DATABASE_SCHEMA.md themselves.

**Important:** Whenever the database design changes (new tables, columns, or relationships), **always update** `llm-context/database/DATABASE_SCHEMA.md` so the schema doc stays in sync with what is implemented.

---

## 6. How the parts relate

- **Option 1:** Automation only; output in `.tmp/`; no frontend, no database.
- **Option 2:** Automation + frontend; frontend reads `.tmp/` via Next.js API; same machine only, no persistence.
- **Option 3:** Automation + frontend + database; shared DB for both (connect via env from `frontend/` and `automation/`); persistent, works when automation runs elsewhere. Schema is defined in `llm-context/database/DATABASE_SCHEMA.md`; update that file whenever the database design changes.
- **llm-context** is the map: AGENT.md (this file) is the entry point; `automation/OVERVIEW.md`, `frontend/OVERVIEW.md`, and `database/OVERVIEW.md` + `database/DATABASE_SCHEMA.md` are the high-level descriptions and design you update when scoping the app; then you follow `automation/CLAUDE.md` and `frontend/CONVENTION.md` to build.

---

## Quick reference

| Step | Action |
|------|--------|
| 1 | Read this file. |
| 2 | Clarify: (2.1) Use stated requirements if already given, else ask. (2.2) Use `brand.pen`? Yes/No. (2.3) Ask which setup: **1** Automation only, **2** Automation + frontend (simple, reads filesystem), **3** Automation + frontend + database (full). |
| 3 | Update `llm-context/automation/OVERVIEW.md` → read `automation/CLAUDE.md` → build automation. Use Supabase only for option 3. |
| 4 | If 2 or 3: Update `llm-context/frontend/OVERVIEW.md` → read `llm-context/frontend/CONVENTION.md` → build frontend. For 2, add API that reads `.tmp/`. |
| 5 | If 3: Update `llm-context/database/OVERVIEW.md` and `llm-context/database/DATABASE_SCHEMA.md` (schema = single source of truth). Add DB client in frontend/ and automation/ via env. **Whenever the DB changes, update DATABASE_SCHEMA.md.** |


