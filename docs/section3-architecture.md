# Section 3: Proposed Hybrid Architecture

The proposed system consists of four modular components that operate
in sequence during each engagement cycle. The components are
implemented as separate Python modules to support clean substitution
of individual layers in future experiments.

## 3.1 Edge AI Threat Prioritization Module

File: sim/ai_threat_model.py

The AI threat prioritization module computes a scalar threat score
for each hostile UAV and returns a ranked list of attackers sorted
by descending priority.

The threat score is computed as:

  threat_score = (distance_score * 0.5 + speed_score * 0.5) * level_weight

where:

- distance_score = 1 / (distance_to_base + epsilon),
  rewarding proximity to the protected asset,
- speed_score = speed / 25.0,
  normalized approach speed,
- level_weight = {low: 0.5, medium: 1.0, high: 1.5},
  a categorical multiplier derived from the estimated threat class.

This formulation assigns highest priority to fast, close, and
high-class hostile UAVs, consistent with standard threat assessment
heuristics used in defense engagement planning.

## 3.2 Quantum-Inspired Assignment Engine

File: sim/quantum_optimizer.py

The assignment engine receives the AI-ranked attacker list and the
current defender fleet state, and solves the constrained
defender-to-threat assignment problem under the one-defender-per-
threat capacity constraint.

In the current prototype, the assignment engine implements a
constrained greedy solver that processes attackers in descending
threat-score order and assigns the nearest available defender to
each. This baseline solver is encapsulated in a dedicated module
with a clean interface designed to accept a drop-in replacement by
a quantum or quantum-inspired backend, such as:

- a QUBO formulation solved via quantum annealing,
- a QAOA circuit executed on a gate-based quantum processor,
- a quantum-inspired solver such as simulated bifurcation or
  coherent Ising machine emulation.

The assignment interface accepts:
  Input:  scenario dict, ranked_attackers list
  Output: assignments list with attacker_id, defender_id, distance,
          threat_score, and optimizer label per assignment.

## 3.3 Metrics and Evaluation Module

File: sim/metrics.py

The metrics module computes per-run and aggregate evaluation
statistics from the assignment outputs of all three pipeline
variants: baseline greedy, AI-prioritized, and quantum-placeholder.

Key outputs include avg_distance, max_distance, num_assignments,
threat_weighted_score, and unassigned_high_threat. These metrics
are computed consistently across all variants to enable fair
direct comparison in the results section.

## 3.4 Crypto-Agile Secure Control Layer

File: sim/security_layer.py

The secure control layer wraps the final assignment decision in a
simulated crypto-agile authorization envelope before dispatch. The
layer supports configurable security profiles representing classical
and post-quantum cryptographic modes:

- Classical profile: RSA-ECDSA key type, simulated latency 1.0 ms
- PQC profile: CRYSTALS-Kyber key type, simulated latency 3.0 ms

The layer tags each command with the active profile name, key type,
and simulated latency overhead. In the current prototype, no real
cryptographic operations are performed; the module provides a
structural placeholder for integration with a post-quantum
cryptographic library such as liboqs or a hardware security module
supporting CRYSTALS-Kyber or CRYSTALS-Dilithium key exchange.

The security layer is invoked after the quantum assignment step and
before command dispatch, consistent with a defense-grade zero-trust
control architecture in which all actuation commands must be
cryptographically authorized.

## 3.5 Pipeline Summary

The full pipeline for a single engagement cycle is:

1. Generate scenario (base, attackers, defenders).
2. AI module ranks attackers by threat score.
3. Assignment engine maps defenders to ranked threats.
4. Metrics module evaluates assignment quality.
5. Security layer wraps the decision in a crypto-agile profile.
6. Results and metrics are logged for analysis.

This modular design ensures that each component can be independently
upgraded, benchmarked, or replaced without modifying the others,
which supports incremental research development and reproducibility.
