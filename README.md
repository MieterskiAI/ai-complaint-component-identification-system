# Complaint Triage & Component Identification — Workflow Case Study (Human-in-the-loop)

Workflow automation case study for after-sales complaint intake, triage, and component decision routing with a final human approval gate.

## Problem
After-sales teams lose time when complaint intake is inconsistent and component decisions are made with partial context.
Wrong or delayed routing increases rework and slows final resolution.

## Solution
- Standardize complaint intake into a structured case payload.
- Validate required fields before the case can move forward.
- Classify complaint type and narrow down likely components.
- Route low-confidence or ambiguous cases to human review.
- Log every decision step for auditability and process improvement.

## Workflow
See the full diagram in [`docs/workflow.md`](docs/workflow.md).

## Inputs / Outputs
**Inputs**
- Complaint text + customer context
- Product/model identifiers
- Known issue metadata (if available)

**Outputs**
- Classified complaint category
- Suggested component candidates
- Recommended next action (auto-route or human review)
- Final human-validated decision record

## Edge cases
See [`docs/edge-cases.md`](docs/edge-cases.md).

## KPIs
See [`docs/metrics.md`](docs/metrics.md). KPI values are planned measurements unless baseline data is provided.

## Quick demo
- Example intake payload: [`examples/complaint_input.json`](examples/complaint_input.json)
- Example decision output: [`examples/analysis_output.md`](examples/analysis_output.md)
- Operator review checklist: [`examples/operator_checklist.md`](examples/operator_checklist.md)
- Visual flow assets: [`screenshots/`](screenshots/)

## Power Platform implementation mapping
- **Power Apps**: guided intake form with required fields and validation prompts.
- **Power Automate**: routing, thresholds, logging, escalation paths.
- **SharePoint or Dataverse**: case records, decision history, status transitions.
- **Teams + Approvals**: human-in-the-loop review for ambiguous/high-risk cases before final decision.

## What this proves
- Converting an unstructured ops problem into a repeatable workflow with clear gates.
- Designing decision-routing logic with human oversight (not black-box automation).
- Defining measurable operational KPIs and an implementation path in Microsoft Power Platform.
