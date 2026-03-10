from __future__ import annotations

import time
from dataclasses import dataclass

from .overlay_models import EMPTY_OVERLAY_STATE, FlashMessage, OverlayState, PopupMessage, TickerMessage


@dataclass(frozen=True)
class ActiveTicker:
    ticker: TickerMessage
    offset_px: float


@dataclass(frozen=True)
class OverlayFrame:
    flash: FlashMessage | None
    popup: PopupMessage | None
    tickers: tuple[ActiveTicker, ...]


class OverlayRuntime:
    def __init__(self) -> None:
        self._state = EMPTY_OVERLAY_STATE
        self._flash_idx = 0
        self._popup_idx = 0
        self._flash_started_at = 0.0
        self._popup_started_at = 0.0
        self._ticker_offsets: dict[str, float] = {}
        self._ticker_updated_at = time.monotonic()

    def set_state(self, state: OverlayState, now: float | None = None) -> None:
        now_ts = now if now is not None else time.monotonic()
        self._state = state
        self._flash_idx = 0
        self._popup_idx = 0
        self._flash_started_at = now_ts
        self._popup_started_at = now_ts
        self._ticker_offsets = {item.id: 0.0 for item in state.tickers}
        self._ticker_updated_at = now_ts

    def has_ticker(self) -> bool:
        return len(self._state.tickers) > 0

    def next_due_seconds(self, now: float) -> float:
        due = 3600.0
        flash = self._current_flash(now)
        if flash is not None:
            elapsed = now - self._flash_started_at
            due = min(due, max(0.05, (flash.duration_ms / 1000.0) - elapsed))
        popup = self._current_popup(now)
        if popup is not None:
            elapsed = now - self._popup_started_at
            due = min(due, max(0.05, (popup.duration_ms / 1000.0) - elapsed))
        return max(0.05, due)

    def _current_flash(self, now: float) -> FlashMessage | None:
        items = self._state.flash_messages
        if not items:
            return None
        if self._flash_started_at <= 0:
            self._flash_started_at = now
        if self._flash_idx >= len(items):
            self._flash_idx = 0
            self._flash_started_at = now
        current = items[self._flash_idx]
        if (now - self._flash_started_at) * 1000.0 >= float(current.duration_ms):
            self._flash_idx = (self._flash_idx + 1) % len(items)
            self._flash_started_at = now
            current = items[self._flash_idx]
        return current

    def _current_popup(self, now: float) -> PopupMessage | None:
        items = self._state.popups
        if not items:
            return None
        if self._popup_started_at <= 0:
            self._popup_started_at = now
        if self._popup_idx >= len(items):
            self._popup_idx = 0
            self._popup_started_at = now
        current = items[self._popup_idx]
        if (now - self._popup_started_at) * 1000.0 >= float(current.duration_ms):
            self._popup_idx = (self._popup_idx + 1) % len(items)
            self._popup_started_at = now
            current = items[self._popup_idx]
        return current

    def snapshot(self, now: float) -> OverlayFrame:
        dt = max(0.0, now - self._ticker_updated_at)
        self._ticker_updated_at = now

        ticker_frames: list[ActiveTicker] = []
        for ticker in self._state.tickers:
            prev = float(self._ticker_offsets.get(ticker.id, 0.0))
            next_offset = prev + (ticker.speed_px_per_second * dt)
            # reset heuristically to keep offset bounded; renderer repeats text anyway
            if next_offset > 200000:
                next_offset = next_offset % 2000.0
            self._ticker_offsets[ticker.id] = next_offset
            ticker_frames.append(ActiveTicker(ticker=ticker, offset_px=next_offset))

        return OverlayFrame(
            flash=self._current_flash(now),
            popup=self._current_popup(now),
            tickers=tuple(ticker_frames),
        )
