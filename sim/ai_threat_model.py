import math
from typing import Dict, Any, List


def ai_threat_score(attacker: Dict[str, Any], base: Dict[str, float]) -> float:
    """
    Simple AI-like threat scoring function.

    Factors:
    - closer to base => higher threat
    - higher speed => higher threat
    - categorical threat class => weight multiplier
    """

    dx = attacker["x"] - base["x"]
    dy = attacker["y"] - base["y"]
    distance = math.sqrt(dx * dx + dy * dy)

    distance_score = 1.0 / (distance + 1e-3)
    speed_score = attacker["speed"] / 25.0

    level_weight = {
        "low": 0.5,
        "medium": 1.0,
        "high": 1.5
    }.get(attacker["threat_level"], 1.0)

    return (distance_score * 0.5 + speed_score * 0.5) * level_weight


def rank_attackers_by_threat(attackers: List[Dict[str, Any]], base: Dict[str, float]) -> List[Dict[str, Any]]:
    ranked = []
    for attacker in attackers:
        score = ai_threat_score(attacker, base)
        ranked.append({**attacker, "threat_score": score})

    ranked.sort(key=lambda a: a["threat_score"], reverse=True)
    return ranked
