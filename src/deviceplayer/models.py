from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Transition:
    type: str
    ms: int


@dataclass(frozen=True)
class Layout:
    mode: str
    orientation: str
    direction: str
    ratio_a: int


@dataclass(frozen=True)
class Defaults:
    duration_ms: int
    transition: Transition
