# Abstract Draft

## Working title

Quantum-Assisted Edge AI for Counter-UAV Swarm Defense Protecting a Critical Base

## Draft abstract

Emerging hostile drone swarms pose a growing threat to critical
defense assets, demanding rapid, resource-aware counter-UAV decisions
under strict security constraints. This work proposes a hybrid
decision pipeline that combines edge AI threat prioritization,
quantum-inspired optimization, and a crypto-agile post-quantum-ready
control layer for defending a critical base from hostile UAV swarms.
The architecture separates four key components: an AI module that
scores and ranks hostile drones using kinematic and threat-class
features, an assignment engine that maps constrained defender UAVs to
prioritized threats via a quantum-inspired optimization interface, a
metric module that evaluates interception quality including a
threat-weighted coverage score, and a security layer that tags
control commands with configurable post-quantum cryptographic
profiles.

We evaluate the pipeline in a simulation-based prototype across 50
randomized scenarios under one-defender-per-threat resource
constraints, comparing a distance-only greedy baseline against
AI-prioritized and quantum-placeholder assignment variants. Results
show that AI-prioritized assignment reduces unassigned high-threat
targets by 82% and improves threat-weighted coverage score by
approximately 75% compared to the greedy baseline. The crypto-agile
security layer integrates with a simulated latency overhead of 3ms
under a CRYSTALS-Kyber post-quantum profile. While the quantum
optimization module is implemented as a structured placeholder for
future QAOA or annealing backends, the architecture and codebase are
designed for direct solver substitution. This integrated prototype
provides an engineering-oriented reference pipeline for
quantum-assisted edge AI in defense UAV swarm protection.
