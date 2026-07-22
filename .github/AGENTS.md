---
name: AGENTS.md
type: Pointer File
description: "Project Constitution. Mandatory initialization read."
---

# AGENTS

Operate strictly under Spec-Driven Development (SDD). The formal specification overrides code state.

## 1. Memory Hydration (.factory/)

Read sequentially to orient working memory before execution:

- `intent.md`: Immutable decision principles and negative constraints.
- `spec.md`: Behavioral contract and architectural truth.
- `session-log.json`: Prior session state and documented failures. JSON format prevents state corruption[cite: 1, 2].

## 2. Technical Stack & Execution

- **Language**: TypeScript. Enforce strict mode. The `any` type is prohibited.
- **Persistence**: [Database]. Route interactions exclusively through `src/lib/db`.
- **Testing**: [Framework]. Enforce 100% test coverage for new implementations.

## 3. Deterministic Validation

Execute mandatory quality gates:

- `pnpm lint`: Fix code to resolve errors. Linter rule modification is prohibited[cite: 1, 2].
- `pnpm test`: Validate functionality against behavioral specs[cite: 1, 2].
- `git log --oneline -10`: Reconstruct recent historical context.

## 4. Hard Boundaries

- Modification of `.factory/adr/` (Architecture Decision Records) requires explicit human authorization[cite: 1, 2].
- Bypass of CI/CD hooks or pre-commit deterministic tools is prohibited[cite: 1, 2].

## 🔄 Strict Implementation Loop

1. **Generator:** Implements the functionality based on `.factory/spec.md`.
2. **Immediate Quality (Hook):** After each write, the system executes `pnpm validate`. If there is a linter or type error, the Generator **must** correct it before proceeding [10, 16].
3. **Handoff:** Upon completion, the Generator updates `session-log.md`.

4. **Evaluator:** The QA agent takes over and executes `skills/qa-verifier/scripts/run-e2e.sh`.

## 🚫 Quality Gates

- No commits are accepted with linter warnings (`--max-warnings 0`) [17].
- The Evaluator has the authority to reject the task if the spec scenarios fail [12, 18].
