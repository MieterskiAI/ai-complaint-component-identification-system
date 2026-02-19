#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 OWNER/REPO" >&2
  exit 1
fi

REPO="$1"

if ! command -v gh >/dev/null 2>&1; then
  echo "Error: GitHub CLI (gh) is not installed." >&2
  exit 1
fi

if ! gh auth status >/dev/null 2>&1; then
  echo "Error: GitHub CLI is not authenticated. Run: gh auth login" >&2
  exit 1
fi

DESCRIPTION="Decision-routing workflow for complaint triage: identifies likely components, routes edge cases, and keeps a human approval gate."
TOPICS=(
  workflow
  process-automation
  operations
  human-in-the-loop
  decision-routing
  after-sales
  portfolio
  power-platform
  power-automate
  power-apps
)

# Update description first.
gh repo edit "$REPO" --description "$DESCRIPTION"

# Clear existing topics first if supported.
if gh repo edit --help 2>/dev/null | rg -q -- '--remove-topic'; then
  mapfile -t existing_topics < <(gh api "repos/$REPO/topics" --jq '.names[]' 2>/dev/null || true)
  if [[ ${#existing_topics[@]} -gt 0 ]]; then
    for topic in "${existing_topics[@]}"; do
      gh repo edit "$REPO" --remove-topic "$topic"
    done
  fi
else
  echo "Warning: Installed gh version does not support --remove-topic. Existing topics may remain." >&2
fi

for topic in "${TOPICS[@]}"; do
  gh repo edit "$REPO" --add-topic "$topic"
done

echo "Repository URL: https://github.com/$REPO"
echo "Description applied: $DESCRIPTION"
echo "Topics applied: ${TOPICS[*]}"
