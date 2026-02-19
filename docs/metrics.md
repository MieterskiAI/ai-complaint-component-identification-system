# Metrics

No real KPI gains are claimed in this repository. Metrics below are planned measurements.

## 1) Time-to-triage
- **Definition:** Time from case intake to first routed decision (auto-route or human queue).
- **How to measure:** Capture timestamps at intake submission and routing completion in the workflow log.

## 2) First-time-right %
- **Definition:** Percentage of cases that do not require decision reversal after initial triage.
- **How to measure:** Track decision revisions and calculate `(cases without reversal / total triaged cases) * 100`.

## 3) Rework rate
- **Definition:** Percentage of cases sent back for missing data, correction, or reclassification.
- **How to measure:** Count cases with status transitions back to earlier stages and divide by total cases.

## Suggested baseline approach
- Measure at least 2–4 weeks of current-state performance.
- Run pilot workflow on a comparable case volume.
- Compare baseline vs pilot using the same definitions and sampling window.
