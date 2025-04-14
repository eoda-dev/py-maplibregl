from __future__ import annotations

from ._core import MapLibreBaseModel


class Terrain(MapLibreBaseModel):
    """Terrain configuration

    See also https://maplibre.org/maplibre-style-spec/terrain/.
    """

    source: str
    exaggeration: int | float = 1
