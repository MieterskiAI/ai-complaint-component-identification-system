# Workflow

```mermaid
flowchart LR
    A[Intake] --> B[Validation]
    B --> C[Classification]
    C --> D[Component identification]
    D --> E[Next action]
    E --> F[Human review]
    F --> G[Final decision]
```

## Notes
- Validation blocks incomplete submissions and requests missing data.
- Human review is mandatory for ambiguous or low-confidence component matches.
- Final decision is logged for traceability and future process tuning.
