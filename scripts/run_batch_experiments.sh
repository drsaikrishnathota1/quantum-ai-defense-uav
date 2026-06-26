#!/usr/bin/env bash
set -euo pipefail

NUM_RUNS="${1:-10}"

echo "[INFO] Running batch of ${NUM_RUNS} experiments..."
mkdir -p results

python3 sim/batch_runner.py

echo "[INFO] Batch experiments completed."
