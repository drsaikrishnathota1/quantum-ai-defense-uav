from typing import Dict, Any, List


def placeholder_quantum_assignment(scenario: Dict[str, Any], ranked_attackers: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Placeholder quantum / quantum-inspired optimizer.

    Current behavior:
    - attackers are processed in ranked order,
    - each defender can be assigned at most once,
    - nearest available defender is chosen.

    This gives a more realistic constrained assignment structure and
    preserves a clean place to replace later with a real quantum or
    quantum-inspired optimization backend.
    """

    defenders = scenario["defenders"]
    available_defenders = {d["id"]: d for d in defenders}
    assignments = []

    for attacker in ranked_attackers:
        if not available_defenders:
            break

        best_def = None
        best_dist = float("inf")

        for defender_id, defender in available_defenders.items():
            dx = attacker["x"] - defender["x"]
            dy = attacker["y"] - defender["y"]
            dist = (dx ** 2 + dy ** 2) ** 0.5

            if dist < best_dist:
                best_dist = dist
                best_def = defender_id

        assignments.append({
            "attacker_id": attacker["id"],
            "defender_id": best_def,
            "distance": best_dist,
            "threat_score": attacker.get("threat_score", None),
            "optimizer": "quantum_placeholder_constrained"
        })

        del available_defenders[best_def]

    return assignments
