# Edge cases

## Missing information
- Required identifiers (model, serial, purchase context) are absent.
- Complaint text lacks concrete symptom details.
- Action: route to intake correction before classification.

## Inconsistent data
- Complaint narrative conflicts with structured fields.
- Product metadata does not match known catalog rules.
- Action: flag for manual validation and hold automated routing.

## Ambiguous component match
- Multiple components have similar symptom patterns.
- Confidence score is below routing threshold.
- Action: send to human reviewer with ranked options and rationale.
