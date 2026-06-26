from pathlib import Path
from datetime import datetime, timezone
import json

from main import generate_scenario, greedy_assignment, ai_prioritized_greedy_assignment
from ai_threat_model import rank_attackers_by_threat
from quantum_optimizer import placeholder_quantum_assignment
from metrics import summarize_results, compare_summaries
from security_layer import apply_security_profile


RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)


def run_single_experiment():
    scenario = generate_scenario()
    ranked_attackers = rank_attackers_by_threat(scenario["attackers"], scenario["base"])

    baseline_assignments = greedy_assignment(scenario)
    baseline_summary = summarize_results(baseline_assignments)

    ai_assignments = ai_prioritized_greedy_assignment(scenario)
    ai_summary = summarize_results(ai_assignments)

    quantum_assignments = placeholder_quantum_assignment(scenario, ranked_attackers)
    quantum_summary = summarize_results(quantum_assignments)

    secured_command = apply_security_profile(
        {
            "assignments": quantum_assignments
        },
        profile_name="pqc"
    )

    ai_vs_baseline = compare_summaries(baseline_summary, ai_summary)
    quantum_vs_baseline = compare_summaries(baseline_summary, quantum_summary)

    return {
        "baseline_summary": baseline_summary,
        "ai_summary": ai_summary,
        "quantum_summary": quantum_summary,
        "ai_vs_baseline": ai_vs_baseline,
        "quantum_vs_baseline": quantum_vs_baseline,
        "security_profile": secured_command["profile"],
        "security_latency_ms": secured_command["profile"]["simulated_latency_ms"],
    }


def run_batch(num_runs: int = 10):
    results = []
    for _ in range(num_runs):
        results.append(run_single_experiment())

    # Simple average over scalar metrics
    def avg(key):
        return sum(r[key] for r in results) / len(results)

    aggregate = {
        "num_runs": num_runs,
        "baseline_avg_distance": avg("baseline_summary") if False else None,
        "security_profile": results[0]["security_profile"],
        "security_latency_ms": results[0]["security_latency_ms"],
    }

    # Store all raw batch results as JSON
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_file = RESULTS_DIR / f"batch_run_{run_id}.json"
    out_file.write_text(json.dumps(results, indent=2))

    print(f"[INFO] Batch run complete ({num_runs} runs). Saved: {out_file}")


if __name__ == "__main__":
    run_batch(num_runs=10)
