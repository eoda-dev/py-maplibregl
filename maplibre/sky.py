from __future__ import annotations

from pydantic import Field
from ._core import MapLibreBaseModel
from ._utils import fix_keys


class Sky(MapLibreBaseModel):
    """Sky configuration

    Note:
        See [maplibre-style-spec/sky](https://maplibre.org/maplibre-style-spec/sky/) for details.
    """

    sky_color: str | list | None = Field("#88C6FC", serialization_alias="sky-color")
    sky_horizon_blend: float | None = Field(0.8, serialization_alias="sky-horizon-blend")
    horizon_color: str | list | None = Field("#ffffff", serialization_alias="horizon-color")
    horizon_fog_blend: float | None = Field(0.8, serialization_alias="horizon-fog-blend")
    fog_color: str | list | None = Field("#ffffff", serialization_alias="fog-color")
    fog_ground_blend: float | list | None = Field(0.5, serialization_alias="fog-ground-blend")
    atmosphere_blend: float | list | None = Field(0.8, serialization_alias="atmosphere-blend")

    def to_dict(self) -> dict:
        return fix_keys(self.model_dump(by_alias=True, exclude_none=True))
