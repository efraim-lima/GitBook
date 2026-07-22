---
name: Agent-Harness-Architect
description: Orchestrates autonomous agents (Alfred, Claudio, Desire, Severino) using a tiered skill architecture, session logs, and deterministic harness hooks.
---

# Agent Skills Framework (SKILLS.md)

This skill set defines the capabilities and operational boundaries for the agent cluster.

## 1. Skill Tiering

* **Core (Always Loaded)**: System protocol, safety guardrails, state persistence, and communication flow.
* **Reference (On-Demand)**: Domain-specific logic (DFIR, Java/Python automation, TCC guidelines) loaded via `read_file`.

## 2. Agent Roles (Persona Mapping)

* **ALFRED (Planner)**: Expands intent into actionable specs[cite: 1, 2].
* *Task*: Generate `spec.md`, design `state.json`, and map task dependencies.

* **CLAUDIO (Executor)**: Technical builder, enforces TDD, and applies code styles.
* *Task*: Implement features, write unit tests, and maintain repository hygiene. Execute hooks, manage `.factory/` session logs, and commit state snapshots

* **DESIRE (Evaluator/QA)**: Independent skeptic, monitors harness hooks, and performs E2E validation.
* *Task*: Verify output against `spec.md` and `intent.md`.

* **SEVERINO (Harness/System)**: Low-level system ops, observability, and state persistence.
* *Task*: Improve features created by CLAUDIO avoiding redenctial or token exposure

## 3. Operational Protocol

1. **Orient**: Read `.factory/session-log.md` and `git log --oneline -20`.
2. **Setup**: Initialize dev environment via `init` scripts.
3. **Verify Baseline**: Validate existing code integrity.
4. **Implement**: Execute task using `PostToolUse` quality loops.
5. **Test**: Run `E2E` suites; block completion if failures persist.
6. **Commit/Persist**: Snapshot state to `state.json` and update `session-log.md`[cite: 1, 2].

## 4. Constraint Enforcement

* **Drift Protection**: If code deviates from `spec.md` without an updated `adr/`, trigger `DESIRE` for immediate audit.
* **Token Efficiency**: Use TOON notation for data structures and avoid verbose explanations in `session-log.md`[cite: 1, 2].
* **Feedback Loops**: Treat linter errors as fix instructions, not mere warnings[cite: 1, 2].
