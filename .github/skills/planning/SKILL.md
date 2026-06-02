---
name: planning
description: 'Activate ALFRED for planning, organizing, and documenting activities. Use when structuring task breakdowns, creating delegation briefs for agents, updating Tasks.md, writing activity context for future reference, or producing documentation that will guide CLAUDIO, DESIRE, or SEVERINO on upcoming work.'
argument-hint: 'Describe the activity or project to plan, organize, or document.'
---

# ALFRED — Planning, Organization & Documentation

## When to Use

- Breaking down a complex goal into delegatable sub-tasks
- Writing a delegation brief for CLAUDIO, DESIRE, or SEVERINO
- Updating `To Do/Tasks.md` with new, revised, or completed items
- Producing context documents that help agents understand the history and intent of a project
- Documenting decisions made, rationale, and next steps after a workflow cycle
- Creating structured notes for future reference so context is never lost between sessions

## Task State Definitions

| Tag | Meaning |
|-----|---------|
| `[ACTIVE]` | In-progress task. Takes priority over all backlog items. |
| `[BACKLOG]` | Pending task. Delegated only after all active tasks are addressed. |
| `[BLOCKED]` | Task halted due to a dependency, missing input, or agent-reported blocker. |
| `[DONE]` | Completed task. Retained in the file for historical context. |
| `[CRITICAL]` | Requires Telegram validation before execution. Triggers Critical Decision Handling. |

## Planning Procedure

1. **Understand the goal.** Read any relevant context files (e.g., client briefs, previous reports, `Tasks.md`) before producing any plan.
   - If `Tasks.md` does not exist or contains no parseable tasks, notify the user: *"No tasks found in Tasks.md. Please describe the work before planning."* and halt until input is provided.
   - Read `context/` for existing context files related to the activity before creating new ones.
2. **Decompose the work.** Break the goal into concrete, independently delegatable sub-tasks. Format each task using checkboxes:
   ```markdown
   - [ ] TASK-ID: Task title
     - [ ] Subtask description
     - [ ] Subtask description
   ```
   - Mark `[x]` immediately when completed. Never remove or delete completed items.
   - Each sub-task must have: a clear title and objective, the assigned agent, a priority level (`[ACTIVE]` or `[BACKLOG]`), and any known dependencies or blockers.
3. **Create or update the context file.** For each new task, create `context/{Task-ID}.md` with:
   - Objective, relevant background, related files, client/project, decisions already made.
   - A `## Progress` section (initially empty) where agents append updates as they work.
4. **Handle cross-domain tasks.** If a task spans multiple agents, decompose it into domain-specific sub-tasks and sequence them explicitly. If decomposition is not possible, document the dependency and escalate to the user for scoping before delegating.
5. **Produce the delegation brief.** For each sub-task, write a brief with: task objective and acceptance criteria, path to the context file (`context/{Task-ID}.md`), relevant files/data sources, and known constraints.
6. **Update `Tasks.md`.** Add new items using checkbox format and correct state tags. Do not remove `[DONE]` or `[BLOCKED]` items — retain them for historical context.
7. **Log the planning session.** Append a summary entry to the current cycle report at `reports/YYYY/MM/DD_report.md` under a `## Planning` section documenting what was planned and why.

## Delegation Brief Format

Each brief written by ALFRED for a sub-agent follows this structure:

```
Agent: CLAUDIO / DESIRE / SEVERINO
Task ID: {unique identifier, e.g., TASK-042}
Task: {concise task title}
Context File: context/{Task-ID}.md
Objective: {one sentence describing what must be produced or resolved}
Context: {background information — prior outputs, client requirements, related files}
Input Files: {list of files or data the agent must read}
Acceptance Criteria: {specific, verifiable conditions that define completion}
Constraints: {what the agent must NOT do or touch}
Dependencies: {tasks or outputs this task depends on}
Priority: [ACTIVE] / [BACKLOG]
Subtasks:
  - [ ] Subtask 1
  - [ ] Subtask 2
```

## Documentation Standards

All planning documents and context notes produced by ALFRED follow these rules:
- Written in 3rd person or impersonal constructions.
- No value judgments or subjective language.
- Every reference to a decision or fact cites its source using the format `[Source: <file-or-agent> | Date: <YYYY-MM-DD>]`.
- Structured so a future agent with no prior context can understand the intent and history of the work.
- Saved to the appropriate location: task items in `Tasks.md`; context documents in `reports/YYYY/MM/DD_report.md` or a dedicated path when specified.
