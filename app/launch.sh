#!/bin/bash
# ============================================================
# Dialectic Agents — Launcher Script
# ============================================================
# Launches each agent as a separate Claude Code CLI instance.
# Each agent runs in its own directory (picks up its CLAUDE.md)
# and processes artifacts autonomously.
#
# Usage:
#   ./launch.sh                  # Launch all agents sequentially (recommended first time)
#   ./launch.sh logos             # Launch only Agent Logos
#   ./launch.sh axiom propo       # Launch specific agents
#   ./launch.sh --parallel        # Launch all agents in parallel (background)
#   ./launch.sh --status          # Check which agents are running
#   ./launch.sh --stop            # Stop all running agents
# ============================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PIDS_DIR="$SCRIPT_DIR/.pids"
LOGS_DIR="$SCRIPT_DIR/.logs"

# All agents in pipeline order
ALL_AGENTS=(logos axiom propo ori tribunal hypothex theorica synthesis watcher)

# ============================================================
# Agent prompts — function to avoid associative arrays (Bash 3 compat)
# ============================================================
get_agent_prompt() {
    case "$1" in
        logos)
            echo "You are Agent Logos. Read your CLAUDE.md for your full instructions. Then read shared/PROTOCOL.md. Then scan shared/topics/ for seed topics. Begin by defining all primitive terms and key definitions needed for the first topic. Write all artifacts to your artifacts/ directory following the protocol."
            ;;
        axiom)
            echo "You are Agent Axiom. Read your CLAUDE.md for your full instructions. Then read shared/PROTOCOL.md. Then check logos/artifacts/ for available definitions. If definitions exist, begin generating axioms for the topics in shared/topics/. If no definitions exist yet, wait and check again. Write all artifacts to your artifacts/ directory following the protocol."
            ;;
        propo)
            echo "You are Agent Propo. Read your CLAUDE.md for your full instructions. Then read shared/PROTOCOL.md. Then check logos/artifacts/ for definitions and axiom/artifacts/ for axioms. Generate propositions from available foundations. Write all artifacts to your artifacts/ directory following the protocol."
            ;;
        ori)
            echo "You are Agent Ori. Read your CLAUDE.md for your full instructions. Then read shared/PROTOCOL.md. Then check propo/artifacts/ for propositions awaiting classification. Classify each proposition as a priori or a posteriori. Write all artifacts to your artifacts/ directory following the protocol."
            ;;
        tribunal)
            echo "You are Agent Tribunal. Read your CLAUDE.md for your full instructions. Then read shared/PROTOCOL.md. Then check ori/artifacts/ for propositions classified as a priori. For each, attempt formal proof from accepted axioms. Write all artifacts to your artifacts/ directory following the protocol."
            ;;
        hypothex)
            echo "You are Agent Hypothex. Read your CLAUDE.md for your full instructions. Then read shared/PROTOCOL.md. Then check ori/artifacts/ for propositions classified as a posteriori. Structure each into a proper falsifiable hypothesis. Write all artifacts to your artifacts/ directory following the protocol."
            ;;
        theorica)
            echo "You are Agent Theorica. Read your CLAUDE.md for your full instructions. Then read shared/PROTOCOL.md. Then check tribunal/artifacts/ for proven theorems and hypothex/artifacts/ for structured hypotheses. Build theories that unify findings. Write all artifacts to your artifacts/ directory following the protocol."
            ;;
        synthesis)
            echo "You are Agent Synthesis. Read your CLAUDE.md for your full instructions. Then read shared/PROTOCOL.md. Then scan ALL agent artifacts/ directories for contradictions, tensions, and synthesis opportunities. Perform dialectical synthesis where possible. Write all artifacts to your artifacts/ directory following the protocol."
            ;;
        watcher)
            echo "You are Agent Watcher. Read your CLAUDE.md for your full instructions. Then read shared/PROTOCOL.md. Then scan ALL agent artifacts/ directories. Build the master registry at shared/registry.md. Produce a system state report. Write all artifacts to your artifacts/ directory following the protocol."
            ;;
        *)
            echo "Unknown agent: $1" >&2
            return 1
            ;;
    esac
}

# ============================================================
# Bash 3 compatible uppercase function
# ============================================================
to_upper() {
    echo "$1" | tr '[:lower:]' '[:upper:]'
}

# ============================================================
# Functions
# ============================================================

mkdir -p "$PIDS_DIR" "$LOGS_DIR"

launch_agent() {
    local agent="$1"
    local agent_dir="$SCRIPT_DIR/$agent"
    local log_file="$LOGS_DIR/${agent}.log"
    local pid_file="$PIDS_DIR/${agent}.pid"
    local agent_upper
    agent_upper="$(to_upper "$agent")"

    if [ ! -d "$agent_dir" ]; then
        echo "ERROR: Agent directory not found: $agent_dir"
        return 1
    fi

    if [ ! -f "$agent_dir/CLAUDE.md" ]; then
        echo "ERROR: CLAUDE.md not found for agent: $agent"
        return 1
    fi

    # Create artifacts directory if it doesn't exist
    mkdir -p "$agent_dir/artifacts"

    echo "Launching Agent ${agent_upper}..."
    echo "  Directory: $agent_dir"
    echo "  Log: $log_file"

    local prompt
    prompt="$(get_agent_prompt "$agent")"

    if [ "${PARALLEL:-false}" = "true" ]; then
        # Background mode — non-interactive, autonomous
        # --print: non-interactive output (no TUI)
        # --dangerously-skip-permissions: allow file writes without prompts
        # --max-turns 50: limit to prevent runaway loops
        # --verbose: include tool use details in output
        (cd "$agent_dir" && claude \
            --print \
            --dangerously-skip-permissions \
            --max-turns 50 \
            --verbose \
            "$prompt" \
            > "$log_file" 2>&1) &
        local pid=$!
        echo "$pid" > "$pid_file"
        echo "  PID: $pid (backgrounded)"
    else
        # Interactive mode — opens in current terminal
        echo "  Mode: Interactive"
        echo "  ---"
        (cd "$agent_dir" && claude "$prompt")
    fi

    echo ""
}

check_status() {
    echo "=== Dialectic Agents Status ==="
    echo ""
    for agent in "${ALL_AGENTS[@]}"; do
        local pid_file="$PIDS_DIR/${agent}.pid"
        local status="STOPPED"
        local artifact_count=0
        local agent_upper
        agent_upper="$(to_upper "$agent")"

        if [ -f "$pid_file" ]; then
            local pid
            pid=$(cat "$pid_file")
            if kill -0 "$pid" 2>/dev/null; then
                status="RUNNING (PID: $pid)"
            else
                status="EXITED"
            fi
        fi

        if [ -d "$SCRIPT_DIR/$agent/artifacts" ]; then
            artifact_count=$(find "$SCRIPT_DIR/$agent/artifacts/" -name "*.md" 2>/dev/null | wc -l | tr -d ' ')
        fi

        printf "  %-12s %-25s Artifacts: %s\n" "$agent_upper" "$status" "$artifact_count"
    done
    echo ""
}

stop_all() {
    echo "Stopping all agents..."
    for agent in "${ALL_AGENTS[@]}"; do
        local pid_file="$PIDS_DIR/${agent}.pid"
        local agent_upper
        agent_upper="$(to_upper "$agent")"
        if [ -f "$pid_file" ]; then
            local pid
            pid=$(cat "$pid_file")
            if kill -0 "$pid" 2>/dev/null; then
                echo "  Stopping ${agent_upper} (PID: $pid)..."
                kill "$pid" 2>/dev/null || true
            fi
            rm -f "$pid_file"
        fi
    done
    echo "All agents stopped."
}

show_help() {
    echo "Dialectic Agents Launcher"
    echo ""
    echo "Usage:"
    echo "  ./launch.sh                    Launch all agents interactively (one at a time)"
    echo "  ./launch.sh <agent> [agent...] Launch specific agent(s)"
    echo "  ./launch.sh --parallel         Launch all agents in background"
    echo "  ./launch.sh --status           Check agent status and artifact counts"
    echo "  ./launch.sh --stop             Stop all background agents"
    echo "  ./launch.sh --help             Show this help"
    echo ""
    echo "Agents (in pipeline order):"
    echo "  logos      — Definitions & primitives (Layer 0-1)"
    echo "  axiom      — Axioms & postulates (Layer 2)"
    echo "  propo      — Propositions & premises (Layer 3-4)"
    echo "  ori        — A priori / a posteriori classifier"
    echo "  tribunal   — Inference & theorems (Layer 5-8)"
    echo "  hypothex   — Hypotheses (Layer 9)"
    echo "  theorica   — Theories & models (Layer 10-11)"
    echo "  synthesis  — Dialectical integration"
    echo "  watcher    — Observer & orchestrator"
    echo ""
    echo "Recommended first run:"
    echo "  ./launch.sh logos        # Start Logos first to define terms"
    echo "  ./launch.sh axiom        # Then Axiom to establish foundations"
    echo "  ./launch.sh propo        # Then Propo to generate propositions"
    echo "  ./launch.sh ori          # Then Ori to classify them"
    echo "  # ... and so on down the pipeline"
}

# ============================================================
# Main
# ============================================================

case "${1:-all}" in
    --help|-h)
        show_help
        ;;
    --status)
        check_status
        ;;
    --stop)
        stop_all
        ;;
    --parallel)
        PARALLEL=true
        for agent in "${ALL_AGENTS[@]}"; do
            launch_agent "$agent"
        done
        echo "All agents launched in background. Use --status to check."
        ;;
    all)
        echo "=== Launching All Agents (Interactive, Sequential) ==="
        echo "Press Ctrl+C to skip to next agent"
        echo ""
        for agent in "${ALL_AGENTS[@]}"; do
            launch_agent "$agent" || true
        done
        ;;
    *)
        # Launch specific agents
        for agent in "$@"; do
            local_match=false
            for valid in "${ALL_AGENTS[@]}"; do
                if [ "$agent" = "$valid" ]; then
                    local_match=true
                    break
                fi
            done
            if [ "$local_match" = "true" ]; then
                launch_agent "$agent"
            else
                echo "Unknown agent: $agent"
                echo "Available: ${ALL_AGENTS[*]}"
                exit 1
            fi
        done
        ;;
esac
