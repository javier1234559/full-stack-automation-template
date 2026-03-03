# Database schema

This file is **updated by the agent** when the user chooses **option 3**. It is the **single source of truth** for the database design. Use it to implement the DB (e.g. in Supabase dashboard, or elsewhere). **Whenever the database design changes, update this file.**

---

## Tables

_(Agent: list each table with columns and a short description. Use plain language or SQL-like definitions. Example:)_

### Example: `runs`

| Column      | Type        | Description               |
| ----------- | ----------- | ------------------------- |
| id          | uuid (PK)   | Primary key               |
| workflow    | text        | Workflow name             |
| output_path | text        | Path or summary of output |
| created_at  | timestamptz | When the run finished     |

---

## Relationships

_(Agent: describe foreign keys or relationships summarized between tables if any.)_

---

## Notes for implementation

_(Agent: any RLS policies, triggers, or auth to keep in mind when implementing the schema in your DB provider.)_
