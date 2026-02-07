# Evaluation Rubric

Use this rubric to assess the quality of AI recommendations in a pilot.

## Ratings
- **Correct**: Recommended component is fully compatible and resolves the complaint.
- **Acceptable**: Recommendation includes a compatible component, but ranked below a less relevant option or missing minor context.
- **Wrong**: Recommended components are incompatible or irrelevant to the complaint.

## Criteria
- **Compatibility**: Matches SKU revision and required subcomponents.
- **Symptom fit**: Reasoning aligns with reported symptoms and context.
- **Evidence**: Decision includes references to input data (symptoms, environment, attachments).
- **Safety**: Flags safety-critical cases for escalation.

## How to test (10–20 cases)
1. Select 10–20 anonymized complaints with known ground-truth resolutions.
2. Run the automation in **dry-run** mode (no write-back).
3. Compare AI output to ground truth using the rubric above.
4. Record counts of Correct / Acceptable / Wrong.
5. Review all Wrong cases to update prompts, rules, or data coverage.
