# 🔍 Skill: E2E Quality Verification

Description: Skeptical validation of functionalities through interface automation.

## 📋 Acceptance Criteria (Based on the Spec)

For each completed task, you must:

1. Locate the corresponding scenario in `.factory/spec.md` [22, 23].
2. Run the test script: `python scripts/verify_behavior.py --scenario [ID]`.
3. **Skepticism:** Do not trust the code; interact with the real API/UI [2, 24].

## 📉 Rejection Flow

If the test fails:

- Capture the error log and screenshot (if UI).
- Write the detailed failure in `session-log.md` as feedback for the Generator [12, 25].

The loop restarts until the scenario passes with 100% success.
