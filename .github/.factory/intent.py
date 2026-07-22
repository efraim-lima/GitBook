#!/usr/bin/env python3
"""
intent.py — Intent Contract Generator
Generates intent.md aligned with spec.md for Spec-Driven Development & AI Harnessing.
"""

import os
import re
import sys
import json
from datetime import datetime
from pathlib import Path
from typing import Optional, Callable, Tuple, List, Dict

class Colors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"


def print_section(title: str, subtitle: str = ""):
    print(f"\n{Colors.HEADER}{'=' * 70}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.OKCYAN}▶ {title}{Colors.ENDC}")
    if subtitle:
        print(f"{Colors.OKBLUE}  {subtitle}{Colors.ENDC}")
    print(f"{Colors.HEADER}{'=' * 70}{Colors.ENDC}\n")


def prompt(
    message: str,
    default: Optional[str] = None,
    required: bool = True,
    validator: Optional[Callable[[str], Tuple[bool, str]]] = None,
    example: Optional[str] = None,
    hint: Optional[str] = None,
) -> str:
    print(f"{Colors.BOLD}{message}{Colors.ENDC}")
    if hint:
        print(f"{Colors.OKBLUE}💡 {hint}{Colors.ENDC}")
    if example:
        print(f"{Colors.WARNING}📝 {example}{Colors.ENDC}")
    if default:
        print(f"{Colors.OKCYAN}↳ Default: {default}{Colors.ENDC}")

    while True:
        try:
            value = input(f"{Colors.OKGREEN}> {Colors.ENDC}").strip()
        except EOFError:
            value = ""

        if not value and default:
            value = default
        if not value and required:
            print(f"{Colors.FAIL}⚠ Required field. Please provide a value.{Colors.ENDC}")
            continue
        if validator and value:
            valid, error = validator(value)
            if not valid:
                print(f"{Colors.FAIL}⚠ {error}{Colors.ENDC}")
                continue
        return value


def ask_yes_no(question: str) -> bool:
    print(f"{Colors.BOLD}{question} [y/n]{Colors.ENDC}")
    while True:
        ans = input(f"{Colors.OKGREEN}> {Colors.ENDC}").strip().lower()
        if ans in ('y', 'yes', 's', 'sim'):
            return True
        if ans in ('n', 'no', 'nao', 'não'):
            return False
        print("Please answer 'y' or 'n'.")


def validate_tradeoff(value: str) -> Tuple[bool, str]:
    if " vs " not in value and " versus " not in value:
        return False, "Trade-off must contain 'X vs Y'."
    return True, ""


def validate_never(value: str) -> Tuple[bool, str]:
    if not value.lower().startswith("never"):
        return False, "Hard boundary must start with 'NEVER'."
    return True, ""


def validate_measurable(value: str) -> Tuple[bool, str]:
    if not any(char.isdigit() for char in value):
        return False, "Must contain a measurable threshold (e.g., '<0.1%')."
    return True, ""


def load_spec_data() -> Optional[Dict]:
    """Auto-load spec.md for cross-reference."""
    spec_path = Path("spec.md")
    if not spec_path.exists():
        return None

    print(f"{Colors.OKBLUE}📄 spec.md found. Loading for cross-reference...{Colors.ENDC}")
    content = spec_path.read_text(encoding="utf-8")
    data = {"problem": "", "outcomes": [], "constraints": [], "stack": "", "scenarios": []}

    m = re.search(r'- \*\*Problem\*\*: (.+)', content)
    if m:
        data["problem"] = m.group(1).strip()
    data["outcomes"] = re.findall(r'- \*\*Outcome\*\*: (.+)', content)
    data["constraints"] = re.findall(r'- \*\*NO\*\*: (.+)', content)
    m = re.search(r'- \*\*Stack\*\*: (.+)', content)
    if m:
        data["stack"] = m.group(1).strip()
    data["scenarios"] = re.findall(r'- \*\*Scenario\*\*: (.+)', content)

    return data


def collect_mission_values() -> Dict:
    print_section("1. Mission & Values", "Why does this agent exist?")
    return {
        "mission": prompt(
            "Mission (business goal)",
            hint="One sentence. Justify the agent's existence in the org.",
            example="Automate legal compliance for condominium assemblies.",
            required=True,
        ),
        "core_value": prompt(
            "Core Value (what wins when everything conflicts)",
            hint="Format: 'Dimension A > Dimension B'. Must be absolute.",
            example="Legal Compliance > Speed",
            required=True,
            validator=validate_tradeoff,
        ),
    }


def collect_decision_matrix() -> List[Dict]:
    print_section("2. Decision Matrix", "Explicit trade-offs with winners.")
    rows = []
    while True:
        conflict = prompt(
            f"Conflict #{len(rows) + 1} (Value A vs Value B)",
            hint="Use 'vs' format.",
            example="Privacy vs Transparency",
            required=False,
            validator=validate_tradeoff,
        )
        if not conflict:
            break
        winner = prompt(
            "Winner",
            hint="Which value wins? Must be one of the two sides.",
            example="Transparency",
            required=True,
        )
        logic = prompt(
            "Logic / Rationale",
            hint="Why does this value win? Reference law, risk, or mission.",
            example="Legal statute 675 mandates public records for delinquency.",
            required=True,
        )
        rows.append({"conflict": conflict, "winner": winner, "logic": logic})
        if not ask_yes_no("Add another conflict?"):
            break
    return rows


def collect_cascading_signals() -> List[Dict]:
    print_section("3. Data Integrity & Scaling", "Goals → Thresholds → Sources → Ops → Trade-offs")
    signals = []
    while True:
        goal = prompt(
            f"Goal #{len(signals) + 1}",
            hint="Aspirational goal that must be machine-actionable.",
            example="Maximize Data Accuracy",
            required=False,
        )
        if not goal:
            break
        threshold = prompt(
            "Threshold (measurable)",
            hint="Must include a number and unit.",
            example="<0.1% error rate on mandatory fields",
            required=True,
            validator=validate_measurable,
        )
        sources = prompt(
            "Sources (where is this measured?)",
            hint="Logs, linter, DB, metrics, etc.",
            example="DB validation logs + linter error reports",
            required=True,
        )
        ops = prompt(
            "Authorized Ops (comma-separated actions)",
            hint="What the agent may do autonomously when threshold is breached.",
            example="Block submission, alert human, queue for review",
            required=True,
        )
        tradeoff = prompt(
            "Trade-off (what we accept losing)",
            hint="Sacrifice made to guarantee the goal.",
            example="Delay > Corruption",
            required=True,
        )
        signals.append({
            "goal": goal,
            "threshold": threshold,
            "sources": sources,
            "ops": ops,
            "tradeoff": tradeoff,
        })
        if not ask_yes_no("Add another goal?"):
            break
    return signals


def collect_hard_boundaries() -> List[Dict]:
    print_section("4. Hard Boundaries", "NEVER statements. Violation = immediate halt.")
    boundaries = []
    while True:
        violation = prompt(
            f"Boundary #{len(boundaries) + 1}",
            hint="Must start with 'NEVER'. Imperative, absolute.",
            example="NEVER persist production data in test environments.",
            required=False,
            validator=validate_never,
        )
        if not violation:
            if not boundaries and ask_yes_no("No boundaries defined. Are you sure?"):
                break
            elif boundaries:
                break
            continue
        consequence = prompt(
            "Consequence if violated",
            hint="Automatic action, not just a log.",
            example="Halt pipeline and notify CISO via P1 alert.",
            required=True,
        )
        boundaries.append({"violation": violation, "consequence": consequence})
        if not ask_yes_no("Add another boundary?"):
            break
    return boundaries


def collect_escalation_protocol() -> Dict:
    print_section("5. Escalation Protocol", "When autonomy ends and human help begins.")
    return {
        "technical": prompt(
            "Technical Escalation",
            hint="Measurable trigger + action.",
            example="If linter fails 3x on same block → Stop & notify human.",
            required=True,
        ),
        "business": prompt(
            "Business Escalation",
            hint="Data discrepancy, compliance conflict, high-value decision.",
            example="If data discrepancy occurs → Halt & request review.",
            required=True,
        ),
    }


def collect_autonomy_gatekeeper() -> Dict:
    print_section("6. Autonomy Gatekeeper", "Consult before any autonomous action.")
    return {
        "constraint": prompt(
            "1. Constraint: What is strictly forbidden?",
            hint="Absolute red line, even under pressure.",
            example="Never bypass security validation to speed up build.",
            required=True,
        ),
        "ambiguity": prompt(
            "2. Ambiguity: Does this collide with intent.md integrity rules?",
            hint="When to stop and ask instead of assuming.",
            example="When user instruction conflicts with an integrity rule in this document.",
            required=True,
        ),
        "hierarchy": prompt(
            "3. Hierarchy: What wins when need vs policy conflict?",
            hint="Must be absolute. No 'it depends'.",
            example="Compliance > User request",
            required=True,
        ),
    }


def generate_intent(data: Dict, spec_data: Optional[Dict]) -> str:
    now = datetime.now().isoformat()
    lines = [
        "# intent.md",
        "",
        f"<!-- Generated: {now} -->",
        f"<!-- Intent Contract: Supreme authority over spec.md ambiguity -->",
        "",
        "## 1. Mission & Values",
        f"- **Mission**: {data['mission_values']['mission']}",
        f"- **Core Value**: {data['mission_values']['core_value']}",
        "",
        "## 2. Decision Matrix",
        "| Conflict | Winner | Logic |",
        "| :--- | :--- | :--- |",
    ]
    for row in data["decision_matrix"]:
        lines.append(f"| {row['conflict']} | {row['winner']} | {row['logic']} |")

    lines.extend([
        "",
        "## 3. Data Integrity & Scaling (Cascading Signals)",
    ])
    for s in data["cascading_signals"]:
        lines.extend([
            f"- **Goal**: {s['goal']}",
            f"  - **Threshold**: {s['threshold']}",
            f"  - **Sources**: {s['sources']}",
            f"  - **Ops**: {s['ops']}",
            f"  - **Trade-off**: {s['tradeoff']}",
        ])

    lines.extend([
        "",
        "## 4. Hard Boundaries",
    ])
    for b in data["hard_boundaries"]:
        lines.append(f"- **{b['violation']}**")
        lines.append(f"  - *Consequence:* {b['consequence']}")

    lines.extend([
        "",
        "## 5. Escalation Protocol",
        f"- **Technical**: {data['escalation']['technical']}",
        f"- **Business**: {data['escalation']['business']}",
        "",
        "## 6. Autonomy Gatekeeper (Consult before action)",
        f"1. **Constraint**: {data['gatekeeper']['constraint']}",
        f"2. **Ambiguity**: {data['gatekeeper']['ambiguity']}",
        f"3. **Hierarchy**: {data['gatekeeper']['hierarchy']}",
        "",
    ])

    if spec_data:
        lines.extend([
            "## 7. Cross-Reference with spec.md",
            f"- **spec.md Problem**: {spec_data['problem'] or 'N/A'}",
            f"- **spec.md Outcomes**: {len(spec_data['outcomes'])} mapped",
            f"- **spec.md Constraints**: {len(spec_data['constraints'])} listed",
            f"- **spec.md Stack**: {spec_data['stack'] or 'N/A'}",
            "",
            "### Harmony Checklist",
            "- [ ] No Hard Boundary contradicts a spec.md Negative Constraint",
            "- [ ] Cascading Signal thresholds are observable in spec.md Core Logic outputs",
            "- [ ] Escalation Protocol covers all spec.md Gherkin failure scenarios",
            "- [ ] Core Value does not conflict with spec.md Decision Contract priorities",
            "- [ ] Autonomy Gatekeeper has answers for every spec.md ambiguity scenario",
            "",
        ])

    lines.extend([
        "---",
        "",
        "## Appendix: AI Harness Notes",
        "- **System Prompt Injection**: Use `intent.json` for structured LLM context.",
        "- **Determinism**: All thresholds and triggers must be state-machine verifiable.",
        "- **Override Authority**: This document prevails over spec.md in conflict.",
    ])

    return "\n".join(lines)


def export_intent_json(data: Dict, filename: str = "intent.json") -> str:
    """Export structured version for AI system prompt injection."""
    export = {
        "mission": data['mission_values']['mission'],
        "core_value": data['mission_values']['core_value'],
        "decision_matrix": data['decision_matrix'],
        "cascading_signals": data['cascading_signals'],
        "hard_boundaries": data['hard_boundaries'],
        "escalation_protocol": data['escalation'],
        "autonomy_gatekeeper": data['gatekeeper'],
        "authority_note": "This document prevails over spec.md in case of ambiguity or conflict."
    }
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(export, f, ensure_ascii=False, indent=2)
    return filename


def generate_harmonization_questions(data: Dict, spec_data: Optional[Dict]) -> List[str]:
    """Bridge questions that connect intent.md to spec.md."""
    questions = []

    questions.append(
        "H1. **Boundary ↔ Constraint Alignment**: For every 'NEVER' in intent.md, "
        "does spec.md have a matching 'NO'? If one document prohibits something the other omits, "
        "which authority resolves the gap?"
    )

    questions.append(
        "H2. **Signal ↔ Output Observability**: Can every Cascading Signal threshold "
        "be measured by a Core Logic output in spec.md? If the threshold is '<0.1% error', "
        "which spec.md endpoint or metric emits that value?"
    )

    questions.append(
        "H3. **Escalation ↔ Gherkin Coverage**: Does every 'Then' failure scenario in spec.md "
        "map to either Technical or Business Escalation in intent.md? Who decides the boundary "
        "between 'retry' (spec.md) and 'escalate' (intent.md)?"
    )

    questions.append(
        "H4. **Decision Matrix ↔ Decision Contract**: If spec.md states 'Priority: Latency > Consistency' "
        "but intent.md states 'Legal Compliance > Speed', which prevails? Is this override explicit?"
    )

    questions.append(
        "H5. **Gatekeeper ↔ Ambiguity**: The spec.md has an 'Ambiguity' field (Halt/Escalate vs Default). "
        "Does the Autonomy Gatekeeper (Question 2) trigger before or after the spec.md ambiguity policy?"
    )

    if spec_data and spec_data['constraints']:
        questions.append(
            f"H6. **Consequence Completeness**: spec.md lists {len(spec_data['constraints'])} negative constraints. "
            f"intent.md has {len(data['hard_boundaries'])} hard boundaries. "
            "Does every constraint have a defined consequence (halt/degrade/alert) in intent.md?"
        )

    questions.append(
        "H7. **Trade-off Depth**: The Cascading Signals declare trade-offs (e.g., 'Delay > Corruption'). "
        "Does spec.md's Integration & Resilience policy (retry/backoff) honor this trade-off? "
        "Or could aggressive retrying violate the intent.md sacrifice?"
    )

    questions.append(
        "H8. **Mission ↔ Problem Alignment**: Does the spec.md Problem statement serve the intent.md Mission? "
        "If the technical problem solved by spec.md does not advance the business mission, "
        "should the spec be rejected or reframed?"
    )

    questions.append(
        "H9. **AI System Prompt Safety**: Is intent.json injected into the LLM system prompt "
        "before or alongside spec.md? If the LLM receives both, which document is tagged as "
        "'supreme authority' in the prompt engineering?"
    )

    questions.append(
        "H10. **Automated Coherence Test**: Write a Gherkin scenario that tests the HARMONY "
        "of both documents: 'Given intent.md forbids X; When spec.md requests X; Then the agent "
        "must escalate and NOT execute X'. Is this test in your CI pipeline?"
    )

    return questions


def main():
    print(f"{Colors.BOLD}{Colors.OKCYAN}")
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║  INTENT CONTRACT GENERATOR                                       ║")
    print("║  Supreme Authority for Ambiguity & AI Harnessing                 ║")
    print("╚══════════════════════════════════════════════════════════════════╝")
    print(f"{Colors.ENDC}")

    spec_data = load_spec_data()

    data = {
        "mission_values": collect_mission_values(),
        "decision_matrix": collect_decision_matrix(),
        "cascading_signals": collect_cascading_signals(),
        "hard_boundaries": collect_hard_boundaries(),
        "escalation": collect_escalation_protocol(),
        "gatekeeper": collect_autonomy_gatekeeper(),
    }

    # Generate files
    intent_md = generate_intent(data, spec_data)
    with open("intent.md", "w", encoding="utf-8") as f:
        f.write(intent_md)

    json_path = export_intent_json(data)

    print(f"\n{Colors.OKGREEN}{'=' * 70}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.OKGREEN}✅ intent.md generated: {os.path.abspath('intent.md')}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.OKGREEN}✅ intent.json generated: {os.path.abspath(json_path)}{Colors.ENDC}")
    print(f"{Colors.OKGREEN}{'=' * 70}{Colors.ENDC}")

    # Harmonization questions
    questions = generate_harmonization_questions(data, spec_data)

    print(f"\n{Colors.WARNING}{Colors.BOLD}")
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║  HARMONIZATION QUESTIONS: intent.md ↔ spec.md                    ║")
    print("╚══════════════════════════════════════════════════════════════════╝")
    print(f"{Colors.ENDC}")

    for q in questions:
        print(f"\n{Colors.OKCYAN}{q}{Colors.ENDC}")
        print(f"{Colors.OKBLUE}   [Edit intent.md or spec.md to resolve]{Colors.ENDC}")

    # Save questions
    with open("intent-harmonization-questions.md", "w", encoding="utf-8") as f:
        f.write("# Harmonization Questions: intent.md ↔ spec.md\n\n")
        for q in questions:
            clean = re.sub(r'^H\d+\.\s+\*\*', '', q).replace('**', '')
            f.write(f"## {clean}\n\n_Answer: _\n\n")

    print(f"\n{Colors.OKGREEN}📋 Saved to: {os.path.abspath('intent-harmonization-questions.md')}{Colors.ENDC}")

    print(f"\n{Colors.BOLD}{Colors.OKCYAN}")
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║  NEXT STEPS                                                      ║")
    print("╠══════════════════════════════════════════════════════════════════╣")
    print("║  1. Review intent.md and tighten Hard Boundaries                 ║")
    print("║  2. Use intent.json as 'system prompt' for AI agents             ║")
    print("║  3. Answer the Harmonization Questions above                     ║")
    print("║  4. Validate: zero contradictions between intent.md and spec.md   ║")
    print("╚══════════════════════════════════════════════════════════════════╝")
    print(f"{Colors.ENDC}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.FAIL}⚠ Interrupted by user.{Colors.ENDC}")
        sys.exit(1)