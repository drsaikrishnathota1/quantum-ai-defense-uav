# Abstract Draft

## Working title

Quantum-Assisted Edge AI for Counter-UAV Swarm Defense Protecting a Critical Base

## Draft abstract (to refine after experiments)

Emerging hostile drone swarms pose a growing threat to critical defense assets, demanding rapid, resource-aware counter-UAV decisions under strict security constraints. This work proposes a hybrid decision pipeline that combines edge AI threat prioritization, quantum-inspired optimization, and a crypto-agile post-quantum-ready control layer for defending a critical base from hostile UAV swarms. The architecture separates four key components: (i) an AI module that scores and ranks hostile drones using kinematic and threat-class features, (ii) an assignment engine that maps defender UAVs to prioritized threats via a quantum-inspired optimization interface, (iii) a metric module that evaluates interception quality, and (iv) a security layer that tags control commands with configurable security profiles and simulated post-quantum cryptographic latency.

We implement a simulation-based prototype in which friendly defenders protect a base against multiple incoming hostile UAVs, and we compare a distance-only greedy baseline with AI-prioritized and quantum-placeholder assignments. Initial results show that the modular pipeline can be executed end-to-end with separate AI, optimization, and security components, and that the security layer can be integrated without breaking real-time decision constraints in small scenarios. While the current quantum module is implemented as a placeholder quantum-inspired solver rather than a full hardware-backed quantum algorithm, the architecture and codebase are designed so that future QAOA, annealing, or other quantum optimizers can be dropped in with minimal changes. This integrated prototype provides an engineering-oriented reference pipeline for future studies on quantum-assisted edge AI in defense UAV swarm protection.

## Notes

- This abstract should be updated with real quantitative results once batch experiments and more realistic constraints are implemented.
- Replace "quantum-inspired" and "placeholder" wording once a concrete quantum or quantum-inspired solver is integrated.
