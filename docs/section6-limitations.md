# Section 6: Limitations and Practical Implications

## 6.1 Simulation-Based Evaluation

All experiments presented in this work are conducted in a
custom simulation environment using randomized synthetic scenarios.
The simulation uses a simplified 2D spatial model and does not
account for real-world factors such as wind, terrain, sensor noise,
communication delays, or UAV flight dynamics. Results should
therefore be interpreted as a feasibility study and architectural
validation rather than an operational performance evaluation.

## 6.2 Quantum Module is a Structured Placeholder

The quantum optimization module in the current prototype does not
use a real quantum or quantum-inspired backend. The module
implements a constrained greedy solver that processes AI-ranked
threats in priority order, encapsulated behind a clean interface
designed for future solver substitution. As a result, the
quantum-placeholder variant produces identical results to the
AI-prioritized variant in the current evaluation.

This is an acknowledged limitation of the prototype stage. The
contribution of the quantum module at this stage is architectural:
it defines the problem interface, input/output contract, and
module boundary that a real QUBO, QAOA, or quantum annealing solver
would need to satisfy. Future work should replace this placeholder
with a concrete quantum or quantum-inspired implementation and
evaluate performance on larger problem instances where quantum
optimization advantages are more likely to emerge.

## 6.3 Threat Classification is Randomly Assigned

In the current prototype, hostile UAV threat levels are randomly
drawn from the set {low, medium, high} at scenario generation time.
In a real deployment, threat classification would be derived from
a trained perception model operating on sensor data such as radar
returns, optical signatures, or behavioral trajectory analysis.
The AI threat-scoring module uses these labels as inputs, so its
performance is bounded by the quality of the upstream classifier.
Integrating a trained threat classification model is an important
direction for future work.

## 6.4 Security Layer Does Not Perform Real Cryptography

The crypto-agile security layer simulates post-quantum cryptographic
latency using fixed estimated values rather than real cryptographic
operations. The CRYSTALS-Kyber profile latency of 3.0 ms is an
approximation based on published benchmarks for software
implementations of CRYSTALS-Kyber on commodity hardware. A
production implementation would require integration with a
post-quantum cryptographic library such as liboqs, an HSM with
PQC support, or a NIST-standardized PQC implementation.

## 6.5 Scenario Size and Generalization

The experiments use a fixed scenario size of N=5 attackers and
M=3 defenders. While this places the system in a meaningful
resource-constrained regime, it is a small problem instance.
The relative advantages of AI prioritization and quantum
optimization are expected to increase as swarm size grows and
the assignment problem becomes harder. Evaluating performance
across a range of N and M values is an important direction for
future experimental work.

## 6.6 Practical Implications

Despite these limitations, the prototype demonstrates several
practically relevant results:

- AI-based threat prioritization provides measurable, consistent
  improvement in high-threat target coverage under resource
  constraints, with an 82% reduction in unassigned high-threat
  targets compared to a distance-only greedy baseline.

- A modular pipeline architecture separating AI scoring,
  optimization, metrics, and secure control is feasible to
  implement and can produce structured, reproducible experiment
  results aligned with engineering research standards.

- Post-quantum cryptographic control-path security can be
  integrated into a UAV defense pipeline with a simulated
  overhead of 3.0 ms per command cycle, which is consistent
  with practical real-time engagement requirements.

- The prototype provides a concrete engineering reference
  architecture that future work can extend by replacing
  individual modules with more capable implementations without
  redesigning the surrounding system.
