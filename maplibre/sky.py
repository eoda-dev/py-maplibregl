from __future__ import annotations

from ._core import MapLibreBaseModel
from ._utils import fix_keys


class Sky(MapLibreBaseModel):
    """Sky configuration

    See also https://maplibre.org/maplibre-style-spec/sky/.
    """

    sky_color: str | list = "#88C6FC"
    sky_horizon_blend: float = 0.8
    horizon_color: str | list = "#ffffff"
    horizon_fog_blend: float = 0.8
    fog_color: str | list = "#ffffff"
    fog_ground_blend: float | list = 0.5
    atmosphere_blend: float | list = 0.8

    def to_dict(self) -> dict:
        return fix_keys(self.model_dump(by_alias=True, exclude_none=True))
