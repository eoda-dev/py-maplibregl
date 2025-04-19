from __future__ import annotations

from ._core import MapLibreBaseModel


class Terrain(MapLibreBaseModel):
    """Terrain configuration

    Note:
        See [maplibre-style-spec/terrain](https://maplibre.org/maplibre-style-spec/terrain/) for details.
    """

    source: str
    exaggeration: int | float | None = 1
