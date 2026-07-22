# intent.md: [Project Name]

## 1. Mission & Values

- **Mission**: [Define business goal]
- **Core Value**: [Priority: e.g., Legal Compliance > Speed]

## 2. Decision Matrix

| Conflict | Winner | Logic |
| :--- | :--- | :--- |
| [Value A] vs [Value B] | [Winner] | [Rationale] |

## 3. Data Integrity & Scaling (Cascading Signals)

- **Goal**: [e.g., Maximize Data Accuracy]
  - **Threshold**: [e.g., <0.1% error]
  - **Sources**: [Logs/Linter/DB]
  - **Ops**: [Block submission / Alert human]
  - **Trade-off**: [e.g., Delay > Corruption]

## 4. Hard Boundaries

- **NEVER**: [Violation 1: e.g., Production data in Test]
- **NEVER**: [Violation 2: e.g., Unvalidated payments]

## 5. Escalation Protocol

- **Technical**: If linter fails 3x on same block -> Stop & Notify human.
- **Business**: If data discrepancy occurs -> Halt & Request review.

## 6. Autonomy Gatekeeper (Consult before action)

1. **Constraint**: What is strictly forbidden?
2. **Ambiguity**: Does this collide with `intent.md` integrity rules?
3. **Hierarchy**: Compliance > User request?
