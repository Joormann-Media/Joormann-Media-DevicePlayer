from __future__ import annotations


def clamp_transition_ms(duration_ms: int, transition_ms: int) -> int:
    if transition_ms <= 0:
        return 0
    return max(0, min(int(duration_ms * 0.8), int(transition_ms)))
