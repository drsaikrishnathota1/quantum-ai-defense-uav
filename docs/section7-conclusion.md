# Section 7: Conclusion

This paper presented a hybrid decision pipeline for counter-UAV
swarm defense of a critical base, combining edge AI threat
prioritization, quantum-inspired optimization, and a crypto-agile
post-quantum-ready secure control layer. The architecture was
implemented as a modular Python prototype with five independently
replaceable components: an AI threat-scoring module, a constrained
assignment engine, a metrics evaluation module, a crypto-agile
security layer, and a batch experiment orchestrator.

Experiments across 50 randomized scenarios under a
one-defender-per-threat resource constraint demonstrated that
AI-prioritized assignment reduces unassigned high-threat targets
by 82% and improves threat-weighted coverage score by approximately
75% compared to a distance-only greedy baseline. The crypto-agile
security layer integrated with a simulated post-quantum latency
overhead of 3.0 ms per command cycle using a CRYSTALS-Kyber
profile, consistent with practical real-time defense engagement
requirements.

The quantum optimization module is currently implemented as a
structured placeholder with a clean solver interface, establishing
the problem formulation and module boundary required for future
integration of real quantum or quantum-inspired backends such as
QAOA, quantum annealing, or coherent Ising machine emulation.

The primary contribution of this work is an integrated,
reproducible engineering reference pipeline that brings together
AI threat prioritization, constrained defender assignment, and
post-quantum-ready secure control in a single defense-oriented
prototype. The modular design supports incremental extension and
independent benchmarking of each component, providing a practical
foundation for future research on quantum-assisted edge AI in
defense UAV swarm protection.

Future work will focus on:

- replacing the quantum placeholder with a real quantum or
  quantum-inspired optimization backend and evaluating
  performance on larger swarm instances,
- integrating a trained threat classification model to replace
  random threat-level assignment,
- extending the simulation to 3D flight dynamics and multi-wave
  engagement scenarios,
- implementing real post-quantum cryptographic operations using
  a NIST-standardized PQC library,
- evaluating the pipeline on a physical UAV testbed or
  high-fidelity defense simulation platform.
