from pathlib import Path
from datetime import datetime
import json
import random

# Results directory
RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)

def generate_scenario(num_attackers: int = 5, num_defenders: int = 3):
    """Placeholder scenario generator for counter-UAV base defense."""
    # Base at origin for now
    base = {"x": 0.0, "y": 0.0}

    attackers = []
    for i in range(num_attackers):
        attackers.append({
            "id": f"A{i+1}",
            "x": random.uniform(5.0, 20.0),
            "y": random.uniform(-10.0, 10.0),
            "speed": random.uniform(10.0, 20.0),
            "heading": random.uniform(-3.14, 3.14),
            "threat_level": random.choice(["low", "medium", "high"])
        })

    defenders = []
    for j in range(num_defenders):
        defenders.append({
            "id": f"D{j+1}",
            "x": random.uniform(-2.0, 2.0),
            "y": random.uniform(-2.0, 2.0),
            "speed": random.uniform(15.0, 25.0),
            "battery": random.uniform(0.5, 1.0)
        })

    return {
        "base": base,
        "attackers": attackers,
        "defenders": defenders
    }

def greedy_assignment(scenario):
    """Very simple greedy baseline: nearest defender to each attacker."""
    assignments = []
    for attacker in scenario["attackers"]:
        best_def = None
        best_dist = float("inf")
        for defender in scenario["defenders"]:
            dx = attacker["x"] - defender["x"]
            dy = attacker["y"] - defender["y"]
            dist = (dx**2 + dy**2) ** 0.5
            if dist < best_dist:
                best_dist = dist
                best_def = defender["id"]
        assignments.append({
            "attacker_id": attacker["id"],
            "defender_id": best_def,
            "distance": best_dist
        })
    return assignments

def main():
    run_id = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    scenario = generate_scenario()
    assignments = greedy_assignment(scenario)

    result = {
        "run_id": run_id,
        "scenario": scenario,
        "assignments": assignments,
        "note": "Placeholder baseline assignment. Replace with AI + quantum/quantum-inspired optimizer."
    }

    # Save JSON result
    out_file = RESULTS_DIR / f"run_{run_id}.json"
    out_file.write_text(json.dumps(result, indent=2))

    print(f"[INFO] Simulation placeholder complete. Saved: {out_file}")

if __name__ == "__main__":
    main()
