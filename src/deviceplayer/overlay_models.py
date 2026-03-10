from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class FlashMessage:
    id: str
    enabled: bool
    title: str
    message: str
    duration_ms: int
    position: str
    rotation: int
    background_color: str
    text_color: str
    accent_color: str
    font_size: int
    padding: int
    opacity: float


@dataclass(frozen=True)
class TickerMessage:
    id: str
    enabled: bool
    text: str
    position: str
    rotation: int
    speed_px_per_second: float
    height: int
    padding_x: int
    background_color: str
    text_color: str
    font_size: int
    opacity: float


@dataclass(frozen=True)
class PopupMessage:
    id: str
    enabled: bool
    title: str
    message: str
    duration_ms: int
    position: str
    image_path: str
    background_color: str
    text_color: str
    accent_color: str
    width: int
    height: int
    padding: int
    opacity: float


@dataclass(frozen=True)
class OverlayState:
    updated_at: str
    flash_messages: tuple[FlashMessage, ...] = field(default_factory=tuple)
    tickers: tuple[TickerMessage, ...] = field(default_factory=tuple)
    popups: tuple[PopupMessage, ...] = field(default_factory=tuple)


EMPTY_OVERLAY_STATE = OverlayState(updated_at="", flash_messages=(), tickers=(), popups=())
