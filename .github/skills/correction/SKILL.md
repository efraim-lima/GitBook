# Skill: CORRECTION

## 🔄 Autocorrect Loop

When receiving an error from the linter via Hook:

1. Read the error message containing the correction instruction [20, 21].
2. Apply the correction only to the affected block.
3. Re-execute the linter locally via `scripts/lint-fix.sh`
