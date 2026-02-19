# AI Complaint Component Identification System

Workflow automation case study for complaint triage and component decision routing with a human-in-the-loop final gate.

## Recommended GitHub repo description (1 line)
Decision-routing workflow for complaint triage that identifies likely components, routes edge cases, and keeps a human approval gate.

## Recommended GitHub topics
- power-platform
- power-automate
- power-apps
- workflow
- process-automation
- requirements
- operations
- human-in-the-loop
- portfolio

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
See full diagram in [`docs/workflow.md`](docs/workflow.md).

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
See [`docs/metrics.md`](docs/metrics.md). All KPI values are planned measurements unless baseline data is provided.

## Quick demo
- Example intake payload: [`examples/complaint_input.json`](examples/complaint_input.json)
- Example decision output: [`examples/analysis_output.md`](examples/analysis_output.md)
- Operator review checklist: [`examples/operator_checklist.md`](examples/operator_checklist.md)
- Visual flow assets: [`screenshots/`](screenshots/)

## How to implement this in Power Platform
- **Power Apps**: build a guided intake form with required fields and validation prompts.
- **Power Automate**: orchestrate routing, confidence thresholds, logging, and escalation paths.
- **SharePoint or Dataverse**: store case records, decision history, and status transitions.
- **Teams + Approvals**: trigger human-in-the-loop review for ambiguous/high-risk cases before final decision.

## What this proves
- I can convert an unstructured ops problem into a repeatable workflow with clear gates.
- I can design decision-routing logic with human oversight, not black-box automation.
- I can define measurable operational KPIs and an implementation path in Microsoft Power Platform.
