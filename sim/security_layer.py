from dataclasses import dataclass
from typing import Dict, Any
from time import perf_counter


@dataclass
class SecurityProfile:
    name: str
    key_type: str      # e.g., "classical", "pqc"
    estimated_latency_ms: float


DEFAULT_PROFILES = {
    "classical": SecurityProfile(
        name="classical",
        key_type="RSA-ECDSA",
        estimated_latency_ms=1.0
    ),
    "pqc": SecurityProfile(
        name="pqc",
        key_type="CRYSTALS-Kyber",
        estimated_latency_ms=3.0
    ),
}


def apply_security_profile(command: Dict[str, Any], profile_name: str = "pqc") -> Dict[str, Any]:
    """
    Simulated crypto-agile control layer.

    It does NOT perform real cryptography, but:
    - tags the command with a chosen profile,
    - simulates extra latency cost,
    - returns metadata that can be used in experiments.
    """

    profile = DEFAULT_PROFILES.get(profile_name, DEFAULT_PROFILES["pqc"])

    t0 = perf_counter()
    # Simulated latency: in a real system this would be actual signing/encryption time
    simulated_latency_ms = profile.estimated_latency_ms
    t1 = t0 + simulated_latency_ms / 1000.0

    secured_command = {
        "original_command": command,
        "profile": {
            "name": profile.name,
            "key_type": profile.key_type,
            "simulated_latency_ms": simulated_latency_ms
        },
        "timing": {
            "start_time": t0,
            "end_time": t1
        }
    }

    return secured_command
