#!/usr/bin/env python3
"""
Spec-Driven Development (SDD) Spec Generator
Guides the user through filling each section of spec.md with validation,
examples, and contextual prompts. Outputs a robust spec.md and follow-up questions.
"""

import os
import re
import sys
from datetime import datetime
from textwrap import dedent, fill
from typing import Optional, Callable, List, Tuple


class Colors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def print_section(title: str, subtitle: str = ""):
    print(f"\n{Colors.HEADER}{'=' * 60}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.OKCYAN}▶ {title}{Colors.ENDC}")
    if subtitle:
        print(f"{Colors.OKBLUE}  {subtitle}{Colors.ENDC}")
    print(f"{Colors.HEADER}{'=' * 60}{Colors.ENDC}\n")


def prompt(
    message: str,
    default: Optional[str] = None,
    required: bool = True,
    validator: Optional[Callable[[str], Tuple[bool, str]]] = None,
    example: Optional[str] = None,
    multiline: bool = False,
    hint: Optional[str] = None,
) -> str:
    """Rich prompt with validation, examples, and hints."""
    print(f"{Colors.BOLD}{message}{Colors.ENDC}")
    if hint:
        print(f"{Colors.OKBLUE}💡 Hint: {hint}{Colors.ENDC}")
    if example:
        print(f"{Colors.WARNING}📝 Example: {example}{Colors.ENDC}")
    if default:
        print(f"{Colors.OKCYAN}↳ Default: {default}{Colors.ENDC}")

    while True:
        if multiline:
            print(f"{Colors.OKCYAN}(Enter empty line twice to finish){Colors.ENDC}")
            lines = []
            while True:
                try:
                    line = input(f"{Colors.OKGREEN}> {Colors.ENDC}")
                except EOFError:
                    break
                if line.strip() == "" and lines and lines[-1].strip() == "":
                    lines.pop()
                    break
                lines.append(line)
            value = "\n".join(lines).strip()
        else:
            try:
                value = input(f"{Colors.OKGREEN}> {Colors.ENDC}").strip()
            except EOFError:
                value = ""

        if not value and default:
            value = default
        if not value and required:
            print(f"{Colors.FAIL}⚠ This field is required. Please provide a value.{Colors.ENDC}")
            continue
        if validator and value:
            valid, error = validator(value)
            if not valid:
                print(f"{Colors.FAIL}⚠ {error}{Colors.ENDC}")
                continue
        return value


def validate_non_empty(value: str) -> Tuple[bool, str]:
    return len(value.strip()) > 0, "Input cannot be empty."


def validate_measurable(value: str) -> Tuple[bool, str]:
    """Check if outcome contains measurable metrics."""
    has_number = bool(re.search(r'\d', value))
    has_unit = any(u in value.lower() for u in ['%', 'sec', 'ms', 'x', 'times', 'users', 'req', 'error', 'rate'])
    if not has_number:
        return False, "Outcomes should be measurable. Try adding a number (e.g., 'reduce by 40%')."
    if not has_unit:
        return False, "Add a unit or dimension (e.g., 'seconds', 'users', 'errors/1000')."
    return True, ""


def validate_gherkin(value: str) -> Tuple[bool, str]:
    """Basic Gherkin structure validation."""
    required = ['given', 'when', 'then']
    lower = value.lower()
    missing = [w for w in required if w not in lower]
    if missing:
        return False, f"Missing Gherkin keyword(s): {', '.join(missing).upper()}"
    return True, ""


def validate_url_or_endpoint(value: str) -> Tuple[bool, str]:
    if not value:
        return True, ""
    if any(c in value for c in ['/', 'http', 'grpc', 'ws:', 'arn:', 'queue']):
        return True, ""
    return False, "Should look like an endpoint, URL, or resource identifier."


def ask_yes_no(question: str) -> bool:
    print(f"{Colors.BOLD}{question} [y/n]{Colors.ENDC}")
    while True:
        ans = input(f"{Colors.OKGREEN}> {Colors.ENDC}").strip().lower()
        if ans in ('y', 'yes'):
            return True
        if ans in ('n', 'no'):
            return False
        print("Please answer 'y' or 'n'.")


def collect_objectives() -> dict:
    print_section("1. Objectives", "Define WHY this exists.")
    return {
        "problem": prompt(
            "What is the core pain point or gap?",
            hint="Describe the user/system friction. Be specific about who hurts and when.",
            example="Users abandon checkout because address validation fails silently on mobile 3G.",
            required=True,
        ),
        "outcome": prompt(
            "What is the expected measurable result?",
            hint="Must include a number and a unit. Avoid vague words like 'better' or 'faster'.",
            example="Reduce checkout abandonment by 35% within 30 days of deployment.",
            required=True,
            validator=validate_measurable,
        ),
        "target": prompt(
            "Who is the target audience/user?",
            hint="Include role, context, and device/environment if relevant.",
            example="Mobile-first e-commerce shoppers on 3G/4G networks in Southeast Asia.",
            required=True,
        ),
    }


def collect_core_logic() -> List[dict]:
    print_section("2. Core Logic", "Define WHAT happens row-by-row.")
    rows = []
    while True:
        print(f"\n{Colors.OKCYAN}--- Logic Row #{len(rows) + 1} ---{Colors.ENDC}")
        row = {
            "trigger": prompt(
                "Trigger / Input",
                hint="What event or data kicks this off?",
                example="POST /api/v1/order with shipping_address payload",
                required=True,
            ),
            "validation": prompt(
                "Validation / Criteria",
                hint="What must be true for this to proceed?",
                example="Address passes USPS validation AND phone matches E.164 format",
                required=True,
            ),
            "output": prompt(
                "Output / Result",
                hint="What is produced on success? Include format and destination.",
                example="Return 200 OK with order_id; emit 'order.created' event to Kafka",
                required=True,
            ),
        }
        rows.append(row)
        if not ask_yes_no("Add another logic row?"):
            break
    return rows


def collect_negative_constraints() -> List[str]:
    print_section("3. Negative Constraints", "Explicitly define what the system MUST NOT do.")
    constraints = []
    print(f"{Colors.OKBLUE}These are your guardrails. Think about security, compliance, UX anti-patterns, and AI boundaries.{Colors.ENDC}")
    while True:
        c = prompt(
            f"Constraint #{len(constraints) + 1} (what is PROHIBITED)?",
            hint="Use 'NO' framing. E.g., 'NO PII in logs', 'NO blocking IO on main thread'.",
            example="NO: Store raw credit card numbers in any log or database field.",
            required=False,
        )
        if not c:
            if not constraints and ask_yes_no("No constraints added. Are you sure?"):
                break
            elif constraints:
                break
            continue
        constraints.append(c)
        if not ask_yes_no("Add another constraint?"):
            break
    return constraints


def collect_integration() -> dict:
    print_section("4. Integration & Resilience", "Define HOW it connects and survives.")
    return {
        "service": prompt(
            "Service / Endpoint / Format",
            hint="Include protocol, version, and schema contract.",
            example="REST API v2 (OpenAPI 3.1), gRPC service 'PaymentGateway', SQS queue 'orders-dlq'",
            required=True,
            validator=validate_url_or_endpoint,
        ),
        "policy": prompt(
            "Retry / Backoff / Resilience Policy",
            hint="Be specific: max retries, backoff type, circuit breaker threshold, timeout.",
            example="Exponential backoff: 100ms base, 5 max retries, 30s circuit breaker after 10 consecutive 5xx",
            required=True,
        ),
    }


def collect_gherkin() -> List[dict]:
    print_section("5. Verification (Gherkin)", "BDD scenarios that prove correctness.")
    scenarios = []
    while True:
        print(f"\n{Colors.OKCYAN}--- Scenario #{len(scenarios) + 1} ---{Colors.ENDC}")
        name = prompt(
            "Scenario Name",
            hint="Use a clear, outcome-focused name.",
            example="Successful checkout with valid international address",
            required=True,
        )
        given = prompt(
            "Given (precondition)",
            hint="State the world before the action.",
            example="the user has items in cart AND has selected 'Express Shipping'",
            required=True,
        )
        when = prompt(
            "When (action)",
            hint="The exact user/system action.",
            example="the user submits the checkout form with a JP address",
            required=True,
        )
        then = prompt(
            "Then (expected result)",
            hint="Observable, testable outcome. Use AND for multiple assertions.",
            example="the order is created AND a 200 OK is returned AND inventory is decremented",
            required=True,
        )
        scenarios.append({"name": name, "given": given, "when": when, "then": then})
        if not ask_yes_no("Add another scenario?"):
            break
    return scenarios


def collect_decision_contract() -> dict:
    print_section("6. Decision Contract", "Define HOW the system decides under pressure.")
    priority = prompt(
        "Priority hierarchy (Dimension A > Dimension B > ...)",
        hint="When two good things conflict, which wins? Be explicit.",
        example="Data Consistency > Availability > Latency",
        required=True,
    )
    ambiguity = prompt(
        "Ambiguity resolution policy",
        hint="What happens when the spec doesn't cover a case?",
        example="Halt and escalate to on-call engineer. Default to safest state (reject request).",
        required=True,
    )
    return {"priority": priority, "ambiguity": ambiguity}


def collect_open_issues() -> List[dict]:
    print_section("7. Open Issues", "What is knowingly uncertain?")
    issues = []
    while True:
        issue = prompt(
            f"Open Issue #{len(issues) + 1}",
            hint="Flag risks, unknowns, or pending decisions. Include owner if known.",
            example="⚠️ Rate limit policy for free-tier users: Pending legal review (Owner: @sarah)",
            required=False,
        )
        if not issue:
            if not issues and ask_yes_no("No open issues. Is the spec truly complete?"):
                break
            elif issues:
                break
            continue
        status = prompt(
            "Status",
            default="Open",
            example="Blocked / In Review / Needs Decision",
            required=False,
        )
        issues.append({"issue": issue, "status": status})
        if not ask_yes_no("Add another open issue?"):
            break
    return issues


def collect_tech_stack() -> dict:
    print_section("8. Technical Stack", "Define the constraints and tools.")
    stack = prompt(
        "Stack / Frameworks",
        hint="Include versions. This is your contract with the runtime.",
        example="Next.js 15 (App Router), Tailwind CSS 3.4, Supabase (Postgres 15), Vercel Edge",
        required=True,
    )
    constraints = prompt(
        "Performance / Operational Constraints",
        hint="SLOs, SLAs, and hard limits. Must be testable.",
        example="TTFB < 200ms @ p95, < 2s load on simulated 3G, max 50MB memory per request",
        required=True,
        validator=validate_measurable,
    )
    return {"stack": stack, "constraints": constraints}


def collect_tasks() -> List[dict]:
    print_section("9. Task Breakdown", "Decompose into verifiable chunks.")
    tasks = []
    defaults = [
        ("T0", "Schema / Data Model / Base Infrastructure"),
        ("T1", "Validation Logic / Core Algorithm"),
        ("T2", "Integration Layer / API Contract"),
        ("T3", "Resilience / Error Handling"),
        ("T4", "Observability / Logging / Metrics"),
        ("T5", "Security / Auth / Negative Constraint Tests"),
    ]
    for default_id, default_desc in defaults:
        desc = prompt(
            f"Task {default_id}",
            default=default_desc,
            required=False,
        )
        if desc:
            tasks.append({"id": default_id, "desc": desc})
    while True:
        custom = prompt(
            f"Additional Task T{len(tasks)}",
            hint="Add any missing work streams.",
            required=False,
        )
        if not custom:
            break
        tasks.append({"id": f"T{len(tasks)}", "desc": custom})
    return tasks


def generate_spec(data: dict) -> str:
    """Render the final spec.md from collected data."""
    lines = [
        "# spec.md",
        "",
        f"<!-- Generated: {datetime.now().isoformat()} -->",
        f"<!-- Spec-Driven Development Template -->",
        "",
        "## 1. Objectives",
        f"- **Problem**: {data['objectives']['problem']}",
        f"- **Outcome**: {data['objectives']['outcome']}",
        f"- **Target**: {data['objectives']['target']}",
        "",
        "## 2. Core Logic",
        "| Trigger | Validation | Output |",
        "| :--- | :--- | :--- |",
    ]
    for row in data["core_logic"]:
        lines.append(f"| {row['trigger']} | {row['validation']} | {row['output']} |")

    lines.extend([
        "",
        "## 3. Negative Constraints",
    ])
    for c in data["constraints"]:
        lines.append(f"- **NO**: {c}")

    lines.extend([
        "",
        "## 4. Integration & Resilience",
        f"- **Service**: {data['integration']['service']}",
        f"- **Policy**: {data['integration']['policy']}",
        "",
        "## 5. Verification (Gherkin)",
    ])
    for sc in data["scenarios"]:
        lines.extend([
            f"- **Scenario**: {sc['name']}",
            f"  - **Given**: {sc['given']}",
            f"  - **When**: {sc['when']}",
            f"  - **Then**: {sc['then']}",
        ])

    lines.extend([
        "",
        "## 6. Decision Contract",
        f"- **Priority**: {data['decision']['priority']}",
        f"- **Ambiguity**: {data['decision']['ambiguity']}",
        "",
        "## 7. Open Issues",
    ])
    for issue in data["open_issues"]:
        lines.append(f"- ⚠️ **{issue['issue']}**: {issue['status']}")

    lines.extend([
        "",
        "## 8. Technical Stack",
        f"- **Stack**: {data['tech_stack']['stack']}",
        f"- **Constraints**: {data['tech_stack']['constraints']}",
        "",
        "---",
        "",
        "## Task Breakdown",
    ])
    for t in data["tasks"]:
        lines.append(f"- [ ] {t['id']}: {t['desc']}")

    lines.extend([
        "",
        "## Appendix: AI Harness Notes",
        "- **Context Window**: Ensure all inputs fit within model token limits.",
        "- **Determinism**: Flag non-deterministic operations (random, time, external state).",
        "- **Testability**: Every scenario must be executable as an automated test.",
    ])

    return "\n".join(lines)


def generate_follow_up_questions(data: dict) -> List[str]:
    """
    Generate contextual, robust follow-up questions based on the collected spec.
    These are designed to harden the spec for SDD and AI harnessing.
    """
    questions = []

    # Contextual questions based on inputs
    obj = data["objectives"]
    if "mobile" in obj["target"].lower() or "3g" in obj["target"].lower():
        questions.append(
            "1. **Offline/Connectivity**: Your target includes mobile/3G users. "
            "What is the spec for offline behavior? What happens when the request times out at 2s but the server actually processed it?"
        )
    if "ai" in obj["problem"].lower() or "llm" in obj["problem"].lower():
        questions.append(
            "2. **AI Safety**: You mention AI in the problem space. "
            "What is the negative constraint for model hallucinations? How do you validate AI output before it reaches the user?"
        )

    # Core logic depth
    questions.append(
        "3. **Idempotency**: For each trigger in Core Logic, what is the idempotency key? "
        "What happens if the same trigger arrives twice within 100ms?"
    )

    # Validation
    questions.append(
        "4. **Validation Failure Matrix**: You defined happy-path validation. "
        "What are the EXACT error codes, messages, and user-facing copy for EACH validation failure?"
    )

    # Negative constraints
    if not any("pii" in c.lower() for c in data["constraints"]):
        questions.append(
            "5. **Data Privacy**: I notice no PII/negative constraint. "
            "Does this system handle personal data? If yes, add a NO-PII constraint. If no, explicitly state 'NO PII is processed'."
        )

    # Integration
    questions.append(
        "6. **Dependency Failure**: Your integration policy covers retries. "
        "What is the SPEC for when the downstream dependency is down for >5 minutes? Degraded mode? Fail-open or fail-closed?"
    )

    # Gherkin
    questions.append(
        "7. **Edge Case Scenarios**: You have happy-path Gherkin. "
        "Add scenarios for: (a) malformed input, (b) dependency timeout, (c) concurrent modification, (d) abuse/malicious input."
    )

    # Decision contract
    questions.append(
        "8. **Conflict Resolution**: Your priority is set. "
        "Write a concrete example: 'If we must choose between [Priority A] and [Priority B] during [specific event], we do X because Y'."
    )

    # AI-specific
    questions.append(
        "9. **AI Context Limits**: If an AI is reading this spec, what context is missing? "
        "Define the glossary: what do domain-specific terms mean? What are the invariant rules that must NEVER be violated?"
    )

    questions.append(
        "10. **Observability Contract**: For every Output in Core Logic, what metric is emitted? "
        "What alert fires if the Outcome metric is not met within 24 hours of deployment?"
    )

    questions.append(
        "11. **Schema Versioning**: Your Task Breakdown starts with T0 (Schema). "
        "What is the backward-compatibility policy? Can T1 ship before T0 is finalized without breaking prod?"
    )

    questions.append(
        "12. **Security Boundaries**: Define the blast radius. "
        "If this feature is compromised, what else is affected? What is the kill switch?"
    )

    return questions


def main():
    print(f"{Colors.BOLD}{Colors.OKCYAN}")
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║     Spec-Driven Development (SDD) Spec Generator           ║")
    print("║     For Robust Engineering & AI Harnessing                 ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print(f"{Colors.ENDC}")

    data = {
        "objectives": collect_objectives(),
        "core_logic": collect_core_logic(),
        "constraints": collect_negative_constraints(),
        "integration": collect_integration(),
        "scenarios": collect_gherkin(),
        "decision": collect_decision_contract(),
        "open_issues": collect_open_issues(),
        "tech_stack": collect_tech_stack(),
        "tasks": collect_tasks(),
    }

    # Generate spec
    spec_content = generate_spec(data)
    output_path = "spec.md"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(spec_content)

    print(f"\n{Colors.OKGREEN}{'=' * 60}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.OKGREEN}✅ spec.md generated successfully at: {os.path.abspath(output_path)}{Colors.ENDC}")
    print(f"{Colors.OKGREEN}{'=' * 60}{Colors.ENDC}")

    # Generate follow-up questions
    questions = generate_follow_up_questions(data)

    print(f"\n{Colors.WARNING}{Colors.BOLD}")
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║  FOLLOW-UP QUESTIONS TO HARDEN YOUR SPEC                     ║")
    print("║  (Answer these to edit spec.md into a production contract)   ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print(f"{Colors.ENDC}")

    for q in questions:
        print(f"\n{Colors.OKCYAN}{q}{Colors.ENDC}")
        print(f"{Colors.OKBLUE}   [Add your answer to spec.md or create spec-appendix.md]{Colors.ENDC}")

    # Save questions to file too
    questions_path = "spec-follow-up-questions.md"
    with open(questions_path, "w", encoding="utf-8") as f:
        f.write("# Spec Follow-Up Questions\n\n")
        f.write(f"Generated: {datetime.now().isoformat()}\n\n")
        for i, q in enumerate(questions, 1):
            clean = re.sub(r'^\d+\.\s+\*\*', '', q).replace('**', '')
            f.write(f"## Q{i}: {clean}\n\n")
            f.write("_Your answer here..._\n\n")
    print(f"\n{Colors.OKGREEN}📋 Questions also saved to: {os.path.abspath(questions_path)}{Colors.ENDC}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.FAIL}⚠ Interrupted by user. No files were written.{Colors.ENDC}")
        sys.exit(1)
        