# CLAUDE.md

Refer to `AGENTS.md` for project identity and technology stack constraints.

## 1. Session Protocol (Mandatory Lifecycle)

Strictly follow this sequence for every session[cite: 1, 2]:

1. **Orient**: Execute `git log --oneline -10` and read `.factory/session-log.md`[cite: 1, 2].
2. **Setup**: Initialize dev servers; verify baseline health.
3. **Plan**: For complex tasks, utilize `Plan Mode` for logical validation before execution[cite: 1, 2].
4. **Execute**: Implement changes in small, atomic increments[cite: 1, 2].
5. **Verify**: Trigger linter/tests post-edit. Auto-correct on failure[cite: 1, 2].
6. **Handoff**: Commit with structured messages; update `.factory/session-log.md`[cite: 1, 2].

## 2. Token & Context Engineering

- **Hydration**: Use `grep`/`find` for surgical file location; avoid reading entire directories[cite: 1, 2].
- **Delegation**: Offload research or multi-file refactors to sub-agents to preserve primary context[cite: 1, 2].
- **Compaction**: Upon reaching context limits, summarize progress in `session-log.md` and perform a `Context Reset`[cite: 1, 2].
- **On-Demand**: Use `read_file` to inject reference modules from `skills/` only when strictly required[cite: 1, 2].

## 3. Harness Hooks (Deterministic Gates)

- **PreToolUse**: Block destructive commands (e.g., `rm -rf`, `drop table`) and sensitive file edits (e.g., `.env`)[cite: 1, 2].
- **PostToolUse**: Auto-run linters/tests after file writes. Inject output into `additionalContext` for immediate self-correction[cite: 1, 2].
- **Certification**: Only mark tasks complete after passing verification gates defined in `spec.md`[cite: 1, 2].

## 🔄 Strict Implementation Loop

1. **Generator:** Implements the functionality based on `.factory/spec.md`.
2. **Immediate Quality (Hook):** After each write, the system executes `pnpm validate`. If there is a linter or type error, the Generator **must** correct it before proceeding [10, 16].
3. **Handoff:** Upon completion, the Generator updates `session-log.md`.

4. **Evaluator:** The QA agent takes over and executes `skills/qa-verifier/scripts/run-e2e.sh`.

## 🚫 Quality Gates

- No commits are accepted with linter warnings (`--max-warnings 0`) [17].
- The Evaluator has the authority to reject the task if the spec scenarios fail [12, 18].
