#!/usr/bin/env bash
set -euo pipefail

echo "[INFO] Running counter-UAV defense simulation..."
mkdir -p results

python3 sim/main.py

echo "[INFO] Experiment finished."
echo "[INFO] Check the results/ directory for JSON outputs."
