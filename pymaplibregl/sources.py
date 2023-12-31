from __future__ import annotations

from enum import Enum
from typing import Union

from pydantic import ConfigDict, Field, computed_field

from ._utils import BaseModel


class SourceType(Enum):
    RASTER = "raster"
    VECTOR = "vector"
    RASTER_DEM = "raster-dem"
    GEOJSON = "geojson"
    IMAGE = "image"
    VIDEO = "video"


class Source(BaseModel):
    model_config = ConfigDict(validate_assignment=True, extra="ignore")


class GeoJSONSource(Source):
    data: Union[str, dict]
    attribution: str = None
    buffer: int = None
    cluster: bool = None
    cluster_max_zoom: int = Field(None, serialization_alias="clusterMaxZoom")
    cluster_min_points: int = Field(None, serialization_alias="clusterMinPoints")
    cluster_properties: dict = Field(None, serialization_alias="clusterProperties")
    cluster_radius: int = Field(None, serialization_alias="clusterRadius")
    filter: list = None
    generate_id: bool = Field(None, serialization_alias="generateId")
    line_metrics: bool = Field(None, serialization_alias="lineMetrics")
    maxzoom: int = None
    promote_id: Union[str, dict] = Field(None, serialization_alias="promoteId")
    tolerance: float = None

    @computed_field
    @property
    def type(self) -> str:
        return SourceType.GEOJSON.value