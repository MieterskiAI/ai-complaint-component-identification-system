# Complaint & Component Identification – Decision-Support Automation

Human-in-the-loop decision support for after-sales complaint handling. The system **does not dispatch parts automatically** — it narrows down options and explains reasoning so an operator can decide.

> **Note:** All examples in this repo are **synthetic/anonymized** and contain no real customer data.

## Suggested GitHub About & Topics
- **GitHub About (1 line):** Human-in-the-loop complaint triage: narrows component options, explains reasoning, and supports operator decision (no auto-dispatch).
- **Topics (tags):** decision-support, human-in-the-loop, complaints, triage, process-design, kpi, evaluation, data-quality, portfolio

_Note: About/Topics are set in the GitHub UI (not via git)._

## What this is
- **Type:** Automation workflow (Zapier/Make-style) for complaint triage and component identification.
- **Goal:** Reduce wrong-part selection and speed up decision-making with transparent reasoning.
- **Human-in-the-loop:** AI suggests, human decides.

## Quick Start / Demo (no system required)
See a complete, realistic walkthrough in under 2 minutes:
1. **Input examples:** `examples/complaint_input.json`
2. **AI-style analysis output:** `examples/analysis_output.md`
3. **Operator checklist:** `examples/operator_checklist.md`

## Architecture & Evaluation
- **System flow + Mermaid diagram:** `docs/architecture.md`
- **Evaluation rubric (correct/acceptable/wrong):** `docs/evaluation.md`
- **Pilot KPIs + how to measure:** `docs/kpi_pilot.md`

## Decision Flow (summary)
Complaint Entry → Context/Data Retrieval → Candidate Components → AI Elimination → Suggested Options + Reasoning → **Human Final Decision** → Write-back to system

## Example Assets
| Asset | Description |
| --- | --- |
| `screenshots/complaints-example.png` | Example complaint record for analysis. |
| `screenshots/zapier-flow.png` | Automation flow overview. |

## Future Improvements (non-core)
- ERP/CRM integration
- Missing data detection
- Advanced compatibility rules
- Multi-language complaint analysis

---

**Author:** MieterskiAI — Junior Operations / Process Analyst (Decision Support, human-in-the-loop)
