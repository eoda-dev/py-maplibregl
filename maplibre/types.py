from __future__ import annotations

from typing_extensions import Union

from maplibre.sources import (
    GeoJSONSource,
    RasterDEMSource,
    RasterSource,
    RasterTileSource,
    VectorSource,
    VectorTileSource,
)

SourceT = Union[
    GeoJSONSource,
    RasterDEMSource,
    RasterSource,
    RasterTileSource,
    VectorSource,
    VectorTileSource,
]
