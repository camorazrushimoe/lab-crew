#!/usr/bin/env bash
# Lab Crew Dashboard — start the monitor server
# Usage: ./dashboard/start.sh
# Opens http://localhost:8699 in browser

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

echo "=== Lab Crew Dashboard ==="
echo ""
echo "  → http://localhost:8699"
echo "  → Press Ctrl+C to stop"
echo ""

python3 monitor.py &
PID=$!
sleep 1
open http://localhost:8699 2>/dev/null || true
wait $PID