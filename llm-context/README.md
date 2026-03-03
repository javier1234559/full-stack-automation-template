# LLM Context

This folder holds **AI guidance and context** for the template: how to scope an app, where conventions live, and what each part of the repo does. It is used by agents (e.g. Cursor, Claude) when you tag **`@AGENT.md`** at the repo root and ask to build an app.

## Purpose

- Give the agent a single entry point and a clear flow (ask design + setup choice, then update overviews and build).
- Keep high-level descriptions (overviews) and design (e.g. database schema) in one place so both humans and AI can see what the app is and how it is structured.

## Structure

```
llm-context/
├── README.md              # This file
├── automation/
│   └── OVERVIEW.md        # Updated by agent: what automation does (workflows, DB usage if setup 3)
├── frontend/
│   ├── OVERVIEW.md        # Updated by agent: what the frontend does (screens, features)
│   └── CONVENTION.md      # Frontend structure and conventions (features, views, shadcn, etc.)
└── database/
    ├── OVERVIEW.md        # Updated by agent when using setup 3: DB purpose, provider
    └── DATABASE_SCHEMA.md # Schema design (tables, relationships); single source of truth when using setup 3. Update whenever the DB changes.
```

## Entry point

The agent entry point is **`AGENT.md`** at the **repo root**, not inside `llm-context/`. When you tag `@AGENT.md` and describe your app:

1. The agent reads `AGENT.md` and asks a few questions (design from `brand.pen`, and which setup: 1 = automation only, 2 = automation + frontend, 3 = automation + frontend + database).
2. It updates the relevant **OVERVIEW** files here (automation, frontend, and database if setup 3).
3. It follows **`automation/CLAUDE.md`** and **`llm-context/frontend/CONVENTION.md`** to build, and **`llm-context/database/DATABASE_SCHEMA.md`** when designing the DB.

You can also reference files in this folder from `.cursor/rules` or project docs so the agent keeps using the same conventions and overviews.
