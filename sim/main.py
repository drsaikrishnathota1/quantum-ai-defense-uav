from pathlib import Path
from datetime import datetime, timezone
import json
import math
import random
from typing import List, Dict, Any

from ai_threat_model import rank_attackers_by_threat
from quantum_optimizer import placeholder_quantum_assignment
from metrics import summarize_results, compare_summaries


RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)


def generate_scenario(num_attackers: int = 5, num_defenders: int = 3) -> Dict[str, Any]:
    base = {"x": 0.0, "y": 0.0}

    attackers = []
    for i in range(num_attackers):
        attackers.append({
            "id": f"A{i+1}",
            "x": random.uniform(5.0, 20.0),
            "y": random.uniform(-10.0, 10.0),
            "speed": random.uniform(10.0, 25.0),
            "heading": random.uniform(-math.pi, math.pi),
            "threat_level": random.choice(["low", "medium", "high"])
        })

    defenders = []
    for j in range(num_defenders):
        defenders.append({
            "id": f"D{j+1}",
            "x": random.uniform(-2.0, 2.0),
            "y": random.uniform(-2.0, 2.0),
            "speed": random.uniform(15.0, 30.0),
            "battery": random.uniform(0.5, 1.0)
        })

    return {
        "base": base,
        "attackers": attackers,
        "defenders": defenders
    }


def greedy_assignment(scenario: Dict[str, Any]) -> List[Dict[str, Any]]:
    assignments = []
    for attacker in scenario["attackers"]:
        best_def = None
        best_dist = float("inf")
        for defender in scenario["defenders"]:
            dx = attacker["x"] - defender["x"]
            dy = attacker["y"] - defender["y"]
            dist = (dx ** 2 + dy ** 2) ** 0.5
            if dist < best_dist:
                best_dist = dist
                best_def = defender["id"]
        assignments.append({
            "attacker_id": attacker["id"],
            "defender_id": best_def,
            "distance": best_dist,
            "optimizer": "greedy_baseline"
        })
    return assignments


def ai_prioritized_greedy_assignment(scenario: Dict[str, Any]) -> List[Dict[str, Any]]:
    ranked_attackers = rank_attackers_by_threat(scenario["attackers"], scenario["base"])
    defenders = scenario["defenders"]

    assignments = []
    for attacker in ranked_attackers:
        best_def = None
        best_dist = float("inf")
        for defender in defenders:
            dx = attacker["x"] - defender["x"]
            dy = attacker["y"] - defender["y"]
            dist = (dx ** 2 + dy ** 2) ** 0.5
            if dist < best_dist:
                best_dist = dist
                best_def = defender["id"]
        assignments.append({
            "attacker_id": attacker["id"],
            "defender_id": best_def,
            "distance": best_dist,
            "threat_score": attacker["threat_score"],
            "optimizer": "ai_prioritized_greedy"
        })
    return assignments


def main():
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    scenario = generate_scenario()
    ranked_attackers = rank_attackers_by_threat(scenario["attackers"], scenario["base"])

    baseline_assignments = greedy_assignment(scenario)
    baseline_summary = summarize_results(baseline_assignments)

    ai_assignments = ai_prioritized_greedy_assignment(scenario)
    ai_summary = summarize_results(ai_assignments)

    quantum_assignments = placeholder_quantum_assignment(scenario, ranked_attackers)
    quantum_summary = summarize_results(quantum_assignments)

    ai_vs_baseline = compare_summaries(baseline_summary, ai_summary)
    quantum_vs_baseline = compare_summaries(baseline_summary, quantum_summary)

    result = {
        "run_id": run_id,
        "scenario": scenario,
        "ranked_attackers": ranked_attackers,
        "baseline": {
            "assignments": baseline_assignments,
            "summary": baseline_summary
        },
        "ai_prioritized": {
            "assignments": ai_assignments,
            "summary": ai_summary,
            "comparison_vs_baseline": ai_vs_baseline
        },
        "quantum_placeholder": {
            "assignments": quantum_assignments,
            "summary": quantum_summary,
            "comparison_vs_baseline": quantum_vs_baseline
        },
        "note": (
            "AI threat scoring is separated into sim/ai_threat_model.py, metrics are in "
            "sim/metrics.py, and optimization is in sim/quantum_optimizer.py."
        )
    }

    out_file = RESULTS_DIR / f"run_{run_id}.json"
    out_file.write_text(json.dumps(result, indent=2))

    print(f"[INFO] Simulation run complete. Saved: {out_file}")
    print("[INFO] Baseline summary:", baseline_summary)
    print("[INFO] AI-prioritized summary:", ai_summary)
    print("[INFO] AI vs baseline:", ai_vs_baseline)
    print("[INFO] Quantum-placeholder summary:", quantum_summary)
    print("[INFO] Quantum vs baseline:", quantum_vs_baseline)


if __name__ == "__main__":
    main()
