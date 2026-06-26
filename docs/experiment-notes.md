# Experiment Notes

## Purpose

This file tracks early experiment observations for the project:

**Quantum-Assisted Edge AI for Counter-UAV Swarm Defense Protecting a Critical Base**

## Current implementation status

The current prototype includes:

- `sim/main.py` for single-run experiment orchestration,
- `sim/ai_threat_model.py` for threat scoring and ranking,
- `sim/quantum_optimizer.py` for a placeholder quantum/quantum-inspired assignment module,
- `sim/metrics.py` for metric calculation,
- `sim/security_layer.py` for a simulated crypto-agile / post-quantum-ready control layer,
- `scripts/run_experiment.sh` for running a single experiment.

## Single-run smoke test

### Command used

```bash
./scripts/run_experiment.sh
```

### Observed behavior

- The simulation completed successfully.
- A JSON result file was written into the `results/` directory.
- The pipeline executed baseline assignment, AI-prioritized assignment, quantum placeholder assignment, and the security-layer wrapper.

### Example observed outputs

- Baseline summary included:
  - `avg_distance`
  - `max_distance`
  - `num_assignments`

- AI-prioritized summary included:
  - `avg_distance`
  - `max_distance`
  - `num_assignments`

- Quantum-placeholder summary included:
  - `avg_distance`
  - `max_distance`
  - `num_assignments`

- Security profile output included:
  - `name: pqc`
  - `key_type: CRYSTALS-Kyber`
  - `simulated_latency_ms: 3.0`

## Initial interpretation

At the current stage, the AI-prioritized and quantum-placeholder outputs may match the baseline because:

1. the scenario is still small,
2. defender reuse is unconstrained,
3. the quantum module is currently only a placeholder wrapper over prioritized assignment,
4. the metrics are still simple and do not yet capture threat-weighted outcomes.

## Research implications

The present codebase already demonstrates:

- a separate AI threat-scoring stage,
- a separate optimization module,
- a separate metric-evaluation module,
- a separate secure-control abstraction,
- a runnable experiment pipeline that can be expanded into a stronger journal prototype.

## Immediate next improvements

- Add multi-run experiments across many random scenarios.
- Add stronger metrics such as threat-weighted interception quality.
- Add defender availability constraints so assignments become more realistic.
- Replace the quantum placeholder with a more meaningful quantum-inspired solver.
- Export structured batch summaries for tables and figures.

## Notes for manuscript writing

The short communication should describe this stage as:

- an **integrated prototype architecture**,
- a **simulation-based feasibility study**,
- and an **engineering reference pipeline** for future defense-UAV quantum/AI evaluation.
