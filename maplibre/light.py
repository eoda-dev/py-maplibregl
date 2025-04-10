from typing_extensions import Literal
from pydantic import Field

from ._core import MapLibreBaseModel


class Light(MapLibreBaseModel):
    anchor: Literal["map", "viewport"] = "map"
    position: list[float, float, float] = [1.15, 210, 30]
    color: str = "#ffffff"
    intensity: float = Field(0.5, ge=0, le=1)
