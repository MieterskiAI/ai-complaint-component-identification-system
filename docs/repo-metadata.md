# Repository metadata

## GitHub About description
Decision-routing workflow for complaint triage: identifies likely components, routes edge cases, and keeps a human approval gate.

## Final validated topics
All topics below comply with GitHub topic rules (lowercase letters/numbers/hyphens only, each under 50 characters):

- workflow
- process-automation
- operations
- human-in-the-loop
- decision-routing
- after-sales
- portfolio
- power-platform
- power-automate
- power-apps

## How to apply metadata
This requires GitHub CLI authentication:

```bash
gh auth login
```

Then apply the description and topics:

```bash
chmod +x scripts/set_repo_metadata.sh
./scripts/set_repo_metadata.sh OWNER/REPO
```
