#!/usr/bin/env bash
set -euo pipefail

echo "[INFO] Running placeholder counter-UAV simulation..."
mkdir -p results

python3 sim/main.py

echo "[INFO] Done. Check the results/ directory for JSON output."
