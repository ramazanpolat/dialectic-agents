#!/bin/bash
# ============================================================
# commit-artifact.sh — Git commit & push a single artifact
# ============================================================
# Called by subagents after creating/updating an artifact.
#
# Usage:
#   bash shared/commit-artifact.sh <artifact-file> <agent-name> <short-description>
#
# Example:
#   bash shared/commit-artifact.sh logos/artifacts/LOGOS-0014-protocol.md logos "Define: protocol"
#
# Features:
#   - Stages only the specific artifact file (plus registry if updated)
#   - Uses a lock file to prevent concurrent git operations
#   - Retries on push failure with pull --rebase
#   - Never force pushes
# ============================================================

set -euo pipefail

ARTIFACT_FILE="${1:?Usage: commit-artifact.sh <artifact-file> <agent-name> <description>}"
AGENT_NAME="${2:?Usage: commit-artifact.sh <artifact-file> <agent-name> <description>}"
DESCRIPTION="${3:-New artifact}"

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOCK_FILE="$REPO_DIR/.git/dialectic.lock"

# --- Acquire lock (simple spinlock, 30s timeout) ---
acquire_lock() {
    local waited=0
    while [ -f "$LOCK_FILE" ]; do
        sleep 1
        waited=$((waited + 1))
        if [ "$waited" -ge 30 ]; then
            echo "[git] WARNING: Lock stale after 30s, removing"
            rm -f "$LOCK_FILE"
            break
        fi
    done
    echo "$$" > "$LOCK_FILE"
}

release_lock() {
    rm -f "$LOCK_FILE"
}

trap release_lock EXIT

# --- Main ---
cd "$REPO_DIR"

acquire_lock

# Stage the artifact
git add "$ARTIFACT_FILE"

# Also stage registry if it was updated
if git diff --cached --name-only | grep -q "shared/registry.md"; then
    : # already staged
elif git diff --name-only | grep -q "shared/registry.md"; then
    git add shared/registry.md
fi

# Check there's something to commit
if git diff --cached --quiet; then
    echo "[git] No changes to commit for $ARTIFACT_FILE"
    exit 0
fi

# Build commit message
AGENT_UPPER="$(echo "$AGENT_NAME" | tr '[:lower:]' '[:upper:]')"
ARTIFACT_ID="$(basename "$ARTIFACT_FILE" .md | sed 's/-.*//' | tr '[:lower:]' '[:upper:]')"
FILENAME="$(basename "$ARTIFACT_FILE")"

git commit -m "$(cat <<EOF
[$AGENT_UPPER] $DESCRIPTION

Artifact: $FILENAME
Agent: $AGENT_NAME

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
EOF
)"

# Push with retry
if ! git push origin main 2>/dev/null; then
    echo "[git] Push failed, pulling with rebase..."
    git pull --rebase origin main
    git push origin main
fi

echo "[git] Committed and pushed: $FILENAME"
