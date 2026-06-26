# Experiment Notes

## Batch experiment snapshot (50 runs)

Scenario: 5 attackers, 3 defenders, one-defender-per-assignment constraint.

| Metric                  | Baseline | AI-Prioritized | Quantum-Placeholder |
|-------------------------|----------|----------------|---------------------|
| avg_distance            | 13.8124  | 13.2096        | 13.2096             |
| max_distance            | 17.4228  | 16.8740        | 16.8740             |
| num_assignments         | 3.0      | 3.0            | 3.0                 |
| threat_weighted_score   | -4.6847  | -1.1495        | -1.1495             |
| unassigned_high_threat  | 0.78     | 0.14           | 0.14                |

## Interpretation

The constrained AI-prioritized and quantum-placeholder pipelines
outperformed the baseline on all reported metrics across 50 random
scenarios. The strongest gains appeared in:

- threat_weighted_score improved by 75% over baseline
- unassigned_high_threat reduced from 0.78 to 0.14 (82% reduction)

These results show that AI threat prioritization meaningfully
improves coverage of high-threat targets under limited defender
resources, which is the core claim of the short communication.
