from typing import List, Dict


def summarize_results(assignments: List[Dict]) -> Dict[str, float]:
    """
    Compute simple summary metrics for a set of assignments.
    """

    if not assignments:
        return {
            "avg_distance": 0.0,
            "max_distance": 0.0,
            "num_assignments": 0.0
        }

    distances = [a["distance"] for a in assignments]
    avg_distance = sum(distances) / len(distances)
    max_distance = max(distances)

    return {
        "avg_distance": avg_distance,
        "max_distance": max_distance,
        "num_assignments": float(len(assignments))
    }


def compare_summaries(baseline: Dict[str, float], candidate: Dict[str, float]) -> Dict[str, float]:
    """
    Compare two metric summaries.
    Negative distance delta means candidate is better.
    """

    return {
        "delta_avg_distance": candidate["avg_distance"] - baseline["avg_distance"],
        "delta_max_distance": candidate["max_distance"] - baseline["max_distance"],
        "delta_num_assignments": candidate["num_assignments"] - baseline["num_assignments"]
    }
