from __future__ import annotations


class PlaylistCursor:
    def __init__(self, items: list[dict]):
        self._items = items
        self._index = -1

    @property
    def size(self) -> int:
        return len(self._items)

    def next(self) -> dict:
        if not self._items:
            raise RuntimeError('playlist is empty')
        self._index = (self._index + 1) % len(self._items)
        return self._items[self._index]
