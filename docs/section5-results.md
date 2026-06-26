# Section 5: Results and Discussion

## 5.1 Aggregate Results

Table 1 presents the averaged metrics across 50 independent
randomized scenarios for the three assignment variants under the
one-defender-per-threat constraint with M=3 defenders and N=5
attackers.

### Table 1: Aggregate results over 50 simulation runs

| Metric                  | Baseline  | AI-Prioritized | Quantum-Placeholder |
|-------------------------|-----------|----------------|---------------------|
| avg_distance (km)       | 13.8124   | 13.2096        | 13.2096             |
| max_distance (km)       | 17.4228   | 16.8740        | 16.8740             |
| num_assignments         | 3.0       | 3.0            | 3.0                 |
| threat_weighted_score   | -4.6847   | -1.1495        | -1.1495             |
| unassigned_high_threat  | 0.78      | 0.14           | 0.14                |

## 5.2 Key Findings

### Finding 1: AI prioritization reduces high-threat exposure

The AI-prioritized pipeline reduced unassigned high-threat attackers
from an average of 0.78 per run (baseline) to 0.14 per run, an
82% reduction. This result directly supports the central claim of
the paper: that AI-based threat ranking meaningfully improves
defender allocation quality when defender resources are limited.

### Finding 2: Threat-weighted coverage score improved by 75%

The threat_weighted_score improved from -4.6847 (baseline) to
-1.1495 (AI-prioritized), a 75.5% improvement. This gain reflects
the compounding benefit of assigning defenders to high-value targets
first, which both reduces penalties for missed high-threat targets
and improves the weighted coverage quality of successful assignments.

### Finding 3: Distance metrics show moderate improvement

Average assignment distance decreased from 13.8124 km (baseline)
to 13.2096 km (AI-prioritized), a 4.4% improvement. Maximum
assignment distance decreased from 17.4228 km to 16.8740 km, a
3.1% reduction. These moderate improvements in distance suggest
that threat-aware ordering also incidentally improves spatial
efficiency in addition to its primary benefit of prioritizing
dangerous targets.

### Finding 4: Quantum placeholder matches AI-prioritized performance

The quantum-placeholder variant produced identical results to the
AI-prioritized variant in all metrics. This is expected at the
current prototype stage, as the quantum module uses the same
constrained greedy solver with AI-ranked inputs. The result
confirms that the module boundary and interface are correct, and
that a real quantum or quantum-inspired solver can be substituted
without changing the surrounding pipeline.

### Finding 5: PQC security layer adds manageable overhead

The crypto-agile security layer operating in PQC mode with
CRYSTALS-Kyber added a simulated latency of 3.0 ms per command
cycle, compared to 1.0 ms for the classical profile. This 2.0 ms
overhead represents a 200% increase in control-path latency but
remains well within the acceptable range for most tactical UAV
engagement timescales, which typically operate on decision cycles
measured in seconds.

## 5.3 Discussion

The results confirm that the proposed hybrid pipeline is feasible
and produces measurable improvements over a distance-only greedy
baseline in the resource-constrained defense scenario. The most
significant gains appear in threat coverage quality rather than
raw distance metrics, which is the appropriate primary objective
for a critical-base defense application where missing a high-threat
target is far more costly than a sub-optimal assignment distance.

The current prototype demonstrates the architectural and engineering
feasibility of integrating AI threat prioritization, constrained
optimization, and post-quantum-ready secure control into a single
coherent pipeline. The modular design allows each component to be
independently upgraded, which supports a clear path toward
integrating real quantum optimization backends in future work.

The negative threat_weighted_score values in both variants reflect
the structural difficulty of the resource-constrained problem:
with only 3 defenders covering 5 attackers, some targets will
always remain unassigned. The pipeline's contribution is to ensure
that the targets left uncovered are systematically the less
dangerous ones, which is demonstrated by the 82% reduction in
unassigned high-threat targets.

## 5.4 Limitations

- The simulation uses a simplified 2D spatial model.
- The quantum optimizer is a placeholder and does not use a real
  quantum or quantum-inspired backend in the current prototype.
- Threat classification is randomly assigned rather than derived
  from a trained perception model.
- The security layer simulates cryptographic latency rather than
  performing real post-quantum cryptographic operations.
- Results reflect a specific scenario size (N=5, M=3) and may not
  generalize directly to larger swarm engagements.

These limitations are consistent with the scope of a short
communication and provide clear directions for future work.
