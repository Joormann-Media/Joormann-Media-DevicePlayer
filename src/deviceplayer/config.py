from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class PlayerConfig:
    manifest_path: Path
    fullscreen: bool
    window_width: int
    window_height: int
    fps: int
    poll_reload_seconds: float
    log_level: str


def build_config(manifest_path: str | None = None) -> PlayerConfig:
    path = manifest_path or os.getenv('DEVICEPLAYER_MANIFEST_PATH', '/mnt/deviceportal/media/stream/current/manifest.json')
    fullscreen = os.getenv('DEVICEPLAYER_FULLSCREEN', '1').strip().lower() in {'1', 'true', 'yes', 'on'}
    width = int(os.getenv('DEVICEPLAYER_WIDTH', '1920'))
    height = int(os.getenv('DEVICEPLAYER_HEIGHT', '1080'))
    fps = max(20, min(120, int(os.getenv('DEVICEPLAYER_FPS', '60'))))
    poll = float(os.getenv('DEVICEPLAYER_RELOAD_POLL_SECONDS', '1.0'))
    level = os.getenv('DEVICEPLAYER_LOG_LEVEL', 'INFO')

    return PlayerConfig(
        manifest_path=Path(path).expanduser().resolve(),
        fullscreen=fullscreen,
        window_width=width,
        window_height=height,
        fps=fps,
        poll_reload_seconds=max(0.2, poll),
        log_level=level,
    )
