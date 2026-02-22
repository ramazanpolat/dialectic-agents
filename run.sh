#!/bin/bash
# ============================================================
# Dialectic Agents — Single-Process Orchestrator
# ============================================================
# Launches ONE Claude Code instance that uses the Task tool
# to spawn subagents for each dialectic agent role.
#
# This is the recommended way to run the pipeline.
# The root CLAUDE.md instructs Claude to orchestrate everything.
#
# Usage:
#   ./run.sh                    # Interactive mode (recommended)
#   ./run.sh --background       # Background mode with logging
#   ./run.sh --status           # Check artifact counts
# ============================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_FILE="$SCRIPT_DIR/.logs/orchestrator.log"
PID_FILE="$SCRIPT_DIR/.pids/orchestrator.pid"

ALL_AGENTS="logos axiom propo ori tribunal hypothex theorica synthesis watcher"

to_upper() {
    echo "$1" | tr '[:lower:]' '[:upper:]'
}

check_status() {
    echo "=== Dialectic Agents — Artifact Status ==="
    echo ""
    local total=0
    for agent in $ALL_AGENTS; do
        local agent_upper
        agent_upper="$(to_upper "$agent")"
        local count=0
        if [ -d "$SCRIPT_DIR/$agent/artifacts" ]; then
            count=$(find "$SCRIPT_DIR/$agent/artifacts/" -name "*.md" 2>/dev/null | wc -l | tr -d ' ')
        fi
        total=$((total + count))
        printf "  %-12s %s artifacts\n" "$agent_upper" "$count"
    done
    echo "  ---"
    printf "  %-12s %s artifacts\n" "TOTAL" "$total"
    echo ""

    # Check orchestrator
    if [ -f "$PID_FILE" ]; then
        local pid
        pid=$(cat "$PID_FILE")
        if kill -0 "$pid" 2>/dev/null; then
            echo "  Orchestrator: RUNNING (PID: $pid)"
        else
            echo "  Orchestrator: EXITED"
        fi
    else
        echo "  Orchestrator: NOT RUNNING"
    fi
    echo ""
}

PROMPT="Execute the full dialectic pipeline as described in your CLAUDE.md. Run all waves in order, spawning subagents for each agent role. Verify artifacts are created after each wave before proceeding. Use absolute paths relative to $(pwd) for all file operations."

case "${1:-interactive}" in
    --status)
        check_status
        ;;
    --background)
        mkdir -p "$(dirname "$LOG_FILE")" "$(dirname "$PID_FILE")"
        echo "Starting orchestrator in background..."
        echo "  Log: $LOG_FILE"
        (cd "$SCRIPT_DIR" && claude \
            --print \
            --dangerously-skip-permissions \
            --max-turns 200 \
            --verbose \
            "$PROMPT" \
            > "$LOG_FILE" 2>&1) &
        echo "$!" > "$PID_FILE"
        echo "  PID: $(cat "$PID_FILE")"
        echo ""
        echo "Monitor with:"
        echo "  tail -f $LOG_FILE"
        echo "  ./run.sh --status"
        ;;
    --stop)
        if [ -f "$PID_FILE" ]; then
            local pid
            pid=$(cat "$PID_FILE")
            if kill -0 "$pid" 2>/dev/null; then
                echo "Stopping orchestrator (PID: $pid)..."
                kill "$pid" 2>/dev/null || true
            fi
            rm -f "$PID_FILE"
        fi
        echo "Orchestrator stopped."
        ;;
    interactive|*)
        echo "=== Dialectic Pipeline Orchestrator ==="
        echo "Starting interactive Claude Code session..."
        echo "Claude will read CLAUDE.md and spawn subagents for each pipeline stage."
        echo ""
        cd "$SCRIPT_DIR" && claude "$PROMPT"
        ;;
esac
