from __future__ import annotations

import pygame


def crossfade(old_surface: pygame.Surface, new_surface: pygame.Surface, progress: float) -> pygame.Surface:
    p = max(0.0, min(1.0, float(progress)))
    frame = old_surface.copy()
    overlay = new_surface.copy()
    overlay.set_alpha(int(255 * p))
    frame.blit(overlay, (0, 0))
    return frame


def slide_left(old_surface: pygame.Surface, new_surface: pygame.Surface, progress: float) -> pygame.Surface:
    p = max(0.0, min(1.0, float(progress)))
    width = old_surface.get_width()
    offset = int(width * p)
    frame = pygame.Surface(old_surface.get_size()).convert()
    frame.blit(old_surface, (-offset, 0))
    frame.blit(new_surface, (width - offset, 0))
    return frame
