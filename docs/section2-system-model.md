# Section 2: System Model and Problem Definition

## 2.1 Scenario Description

We consider a critical-base protection scenario in which a stationary
defended asset is located at the origin of a two-dimensional defense
zone. A swarm of hostile unmanned aerial vehicles (UAVs) approaches
the base from randomized positions and trajectories. A fleet of
friendly defender UAVs is deployed to intercept hostile threats
before they reach the protected zone.

Each simulation run generates a fresh random scenario consisting of:

- a fixed protected base at coordinates (0, 0),
- a set of hostile attacker UAVs initialized at randomized positions
  within an approach envelope,
- a set of friendly defender UAVs initialized near the base with
  randomized positions, speeds, and battery levels.

The defender fleet operates under a one-defender-per-threat
assignment constraint, meaning each defender UAV may be assigned to
at most one hostile target per engagement cycle. This constraint
models real-world limitations on UAV intercept capacity and
engagement rules of engagement.

## 2.2 Hostile UAV State Variables

Each hostile attacker UAV is described by the following state vector:

- id: unique identifier
- x, y: 2D spatial position (km)
- speed: approach speed (m/s), drawn from U[10, 25]
- heading: approach heading (radians), drawn from U[-pi, pi]
- threat_level: categorical class in {low, medium, high}

The threat_level attribute captures an estimated classification of
the hostile UAV's payload, intent, or approach behavior, and is
used by the AI threat-scoring module to compute a priority score.

## 2.3 Friendly Defender UAV State Variables

Each friendly defender UAV is described by:

- id: unique identifier
- x, y: 2D spatial position (km), initialized near the base
- speed: intercept speed (m/s), drawn from U[15, 30]
- battery: remaining energy level, drawn from U[0.5, 1.0]

Defender speed is strictly greater on average than attacker speed,
ensuring that interception is physically feasible. Battery level is
tracked as a future constraint for extended multi-wave scenarios.

## 2.4 Assignment Problem Formulation

The defender assignment problem is formulated as a constrained
optimization task. Given a set of N hostile attackers and M defender
UAVs (where M < N in the challenging regime), the system must:

1. Score and rank all hostile attackers by threat priority.
2. Assign each available defender to exactly one attacker.
3. Maximize threat-weighted coverage quality.
4. Minimize unassigned high-threat targets.

This is structurally equivalent to a constrained matching or
assignment problem, which is amenable to quantum or quantum-inspired
optimization methods such as QUBO formulations, quantum annealing,
or variational quantum algorithms.

## 2.5 Evaluation Metrics

The following metrics are used to evaluate assignment quality across
repeated simulation runs:

- avg_distance: mean Euclidean distance between each assigned
  defender and its assigned attacker at assignment time.
- max_distance: maximum assignment distance in the scenario.
- num_assignments: total number of successful assignments made.
- threat_weighted_score: sum of (threat_weight / distance) for all
  assignments, minus penalties for unassigned high-threat targets.
  Threat weights are: low=1, medium=2, high=3.
- unassigned_high_threat: count of high-threat attackers that
  remain unassigned due to defender resource constraints.

A higher threat_weighted_score and lower unassigned_high_threat
indicate better defense performance.
