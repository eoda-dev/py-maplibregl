from __future__ import annotations

from ._core import MapLibreBaseModel


class Terrain(MapLibreBaseModel):
    source: str
    exaggeration: int | float = 1
