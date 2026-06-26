# Section 4: Experimental Setup

## 4.1 Simulation Environment

All experiments were conducted using a custom Python simulation
framework implemented across five modular components:

- sim/ai_threat_model.py: AI threat scoring and ranking
- sim/quantum_optimizer.py: constrained assignment engine
- sim/metrics.py: evaluation metric computation
- sim/security_layer.py: crypto-agile control layer simulation
- sim/batch_runner.py: batch experiment orchestration

The simulation framework runs on Python 3.11 and requires no
external dependencies beyond the standard library in its current
form. All experiments were executed on a standard development
machine and are fully reproducible using the provided Dockerfile
and requirements.txt.

## 4.2 Scenario Parameters

Each simulation run generates an independent random scenario with
the following fixed parameters:

| Parameter                        | Value               |
|----------------------------------|---------------------|
| Number of hostile attackers      | 5                   |
| Number of friendly defenders     | 3                   |
| Attacker position range (x)      | U[5.0, 20.0] km     |
| Attacker position range (y)      | U[-10.0, 10.0] km   |
| Attacker speed range             | U[10.0, 25.0] m/s   |
| Attacker heading range           | U[-pi, pi] radians  |
| Attacker threat class            | {low, medium, high} |
| Defender position range (x, y)   | U[-2.0, 2.0] km     |
| Defender speed range             | U[15.0, 30.0] m/s   |
| Defender battery level           | U[0.5, 1.0]         |
| Defender assignment constraint   | one per attacker    |
| Protected base location          | (0.0, 0.0)          |
| Number of independent runs       | 50                  |

The scenario uses M=3 defenders against N=5 attackers, placing the
system in the resource-constrained regime where not all threats can
be simultaneously covered, which is the most relevant operating
condition for the proposed pipeline.

## 4.3 Baseline Methods

Three assignment variants are compared in each run:

### Baseline: Distance-Only Greedy

Assigns each attacker to the nearest available defender in the
order attackers appear in the scenario list, without considering
threat priority. Defenders are consumed in assignment order.

### AI-Prioritized Greedy

Sorts attackers by descending AI threat score before assignment.
Uses the same nearest-available-defender rule, but processes
high-threat targets first so that limited defenders are allocated
to the most dangerous threats.

### Quantum-Placeholder

Identical in behavior to AI-Prioritized Greedy in the current
prototype, but encapsulated in a separate quantum_optimizer module
with a clean interface designed for future replacement by a real
quantum or quantum-inspired optimization backend.

## 4.4 Evaluation Metrics

The following metrics are computed for each run and averaged across
all 50 runs:

| Metric                  | Description                                      |
|-------------------------|--------------------------------------------------|
| avg_distance            | Mean defender-to-attacker distance at assignment |
| max_distance            | Maximum assignment distance per run              |
| num_assignments         | Total successful defender assignments            |
| threat_weighted_score   | Weighted coverage quality score                  |
| unassigned_high_threat  | Count of high-threat targets left unassigned     |

The threat_weighted_score is computed as:

  score = sum(threat_weight / distance) - penalties

where threat weights are low=1, medium=2, high=3, and a penalty of
5.0 is applied for each unassigned high-threat attacker and 2.0
for each unassigned medium-threat attacker.

## 4.5 Security Layer Configuration

The crypto-agile security layer is evaluated using the PQC profile
with CRYSTALS-Kyber key type and a simulated latency overhead of
3.0 ms per command authorization cycle. This overhead is compared
against the classical RSA-ECDSA profile baseline of 1.0 ms to
establish a reference for post-quantum control-path cost.
