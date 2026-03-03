# Database overview

This file is **updated by the agent** when the user chooses **option 3** (automation + frontend + database). It describes what the database is for and how it is used.

---

## Purpose

_(Agent: replace with a short description.)_

- What data is stored (e.g. users, automation results, app state).
- Shared by: frontend and automation (e.g. Supabase).
- Why database was chosen: persistence, history, or automation running on a different machine.

---

## Provider and connection

_(Agent: e.g. Supabase, PlanetScale. There is no `supabase/` folder in the repo. Schema design is in `llm-context/database/DATABASE_SCHEMA.md`. Frontend and automation each add their own client/connection and use env vars (URL, key) to connect. Whenever the database design changes, update DATABASE_SCHEMA.md.)_

Not used (option 1 or 2).
