# Architecture (Decision-Support Automation)

This workflow is designed for Zapier/Make-style automation with human review before any action is taken.

## Mermaid Diagram

```mermaid
flowchart LR
    A[Complaint Entry
(Form/Sheet/CRM)] --> B[Context Retrieval
(Order, delivery, SKU)]
    B --> C[Candidate Components
(Reference dataset)]
    C --> D[AI Elimination
+ Reasoning]
    D --> E[Suggested Options
(Top 1–2)]
    E --> F[Human Review
& Decision]
    F --> G[Write-back
(Complaint record)]
```

## Notes
- **No automatic dispatch.** The workflow only suggests and documents reasoning.
- **Write-back** can target a CRM ticket, spreadsheet, or service desk system.
