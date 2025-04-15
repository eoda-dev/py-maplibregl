from __future__ import annotations

import warnings

from enum import Enum

from pydantic import BaseModel, computed_field, field_validator

from .config import options
from .layer import Layer, LayerType
from .light import Light
from .sky import Sky
from .terrain import Terrain
from .types import SourceT

MAPLIBRE_DEMO_TILES = "https://demotiles.maplibre.org/style.json"


class BasemapStyle(BaseModel):
    """Basemap style

    Note:
        See [maplibre-style-spec/root](https://maplibre.org/maplibre-style-spec/root/) for more details.
    """

    _version = 8

    sources: dict[str, dict | SourceT] | None = None
    layers: list[Layer | dict]
    name: str = "my-basemap"
    sky: dict | Sky | None = None
    terrain: dict | Terrain | None = None
    light: dict | Light | None = None
    glyphs: str | None = None
    sprite: str | None = None
    center: tuple[float, float] | list[float, float] | None = None
    zoom: int | float | None = None
    bearing: int | float | None = None
    pitch: int | float | None = None

    @computed_field
    def version(self) -> int:
        return self._version

    def to_dict(self) -> dict:
        return self.model_dump(exclude_none=True, by_alias=True)

    @property
    def symbol_layers(self) -> list[str]:
        return [layer["id"] for layer in self.to_dict()["layers"] if layer["type"] == "symbol"]

    @classmethod
    def from_url(cls, url: str) -> BasemapStyle:
        import requests as req

        resp = req.get(url)
        data = resp.json()
        resp.close()
        return cls(**data)

    @staticmethod
    def carto_url(style_name: str | Carto) -> str:
        return f"https://basemaps.cartocdn.com/gl/{Carto(style_name).value}-gl-style/style.json"
        # return construct_carto_basemap_url(style_name)

    @staticmethod
    def openfreemap_url(style_name: str | OpenFreeMap) -> str:
        return f"https://tiles.openfreemap.org/styles/{OpenFreeMap(style_name).value}"
        # return construct_openfreemap_basemap_url(style_name)

    @staticmethod
    def maptiler_url(style_name: str | MapTiler) -> str:
        maptiler_api_key = options.maptiler_api_key
        return f"https://api.maptiler.com/maps/{MapTiler(style_name).value}/style.json?key={maptiler_api_key}"
        # return construct_maptiler_basemap_url(style_name)


class Carto(Enum):
    """Carto basemap styles

    Attributes:
        DARK_MATTER: dark-matter
        POSITRON: positron
        VOYAGER: voyager
        POSITRON_NOLABELS: positron-nolabels
        DARK_MATTER_NOLABELS: dark-matter-nolabels
        VOYAGER_NOLABELS: voyager-nolabels

    Examples:
        >>> from maplibre import Map, MapOptions
        >>> from maplibre.basemaps import Carto

        >>> m = Map(MapOptions(style=Carto.DARK_MATTER))
    """

    DARK_MATTER = "dark-matter"
    POSITRON = "positron"
    VOYAGER = "voyager"
    POSITRON_NOLABELS = "positron-nolabels"
    DARK_MATTER_NOLABELS = "dark-matter-nolabels"
    VOYAGER_NOLABELS = "voyager-nolabels"


def construct_carto_basemap_url(style_name: str | Carto = Carto.DARK_MATTER) -> str:
    # warnings.warn("Use 'BasemapStyle.carto_url' instead", DeprecationWarning)
    return f"https://basemaps.cartocdn.com/gl/{Carto(style_name).value}-gl-style/style.json"


def construct_basemap_style(layers: list, sources: dict | None = None, name: str = "my-basemap", **kwargs) -> dict:
    """Construct a basemap style

    Args:
        layers (list): The layers to be used for the basemap style.
        sources (dict): The sources to be used for the basemap style.
        name (str): The name of the basemap style.
        **kwargs (any): ...
    """
    layers = [layer.to_dict() if isinstance(layer, Layer) else layer for layer in layers]
    return dict(name=name, version=8, sources=sources or dict(), layers=layers) | kwargs


def background(color: str = "black", opacity: float = 1.0) -> dict:
    bg_layer = Layer(
        type=LayerType.BACKGROUND,
        id="background",
        source=None,
        paint={"background-color": color, "background-opacity": opacity},
    )
    return construct_basemap_style(layers=[bg_layer])


class MapTiler(Enum):
    """MapTiler basemap styles

    Examples:
        >>> import os
        >>> from maplibre import Map, MapOptions
        >>> from maplibre.basemaps import MapTiler

        >>> os.environ["MAPTILER_API_KEY"] = "your-api-key"
        >>> m = Map(MapOptions(style=MapTiler.AQUARELLE))
    """

    AQUARELLE = "aquarelle"
    BACKDROP = "backdrop"
    BASIC = "basic"
    BRIGHT = "bright"
    DATAVIZ = "dataviz"
    LANDSCAPE = "landscape"
    OCEAN = "ocean"
    OPEN_STREET_MAP = "openstreetmap"
    OUTDOOR = "outdoor"
    SATELLITE = "satellite"
    STREETS = "streets"
    TONER = "toner"
    TOPO = "topo"
    WINTER = "winter"


def construct_maptiler_basemap_url(
    style_name: str | MapTiler = "aquarelle",
) -> str:
    maptiler_api_key = options.maptiler_api_key
    return f"https://api.maptiler.com/maps/{MapTiler(style_name).value}/style.json?key={maptiler_api_key}"


class OpenFreeMap(Enum):
    """OpenFreeMap basemap styles

    Attributes:
        POSITRON: positron
        LIBERTY: liberty
        BRIGHT: bright

    Examples:
        >>> from maplibre import Map, MapOptions
        >>> from maplibre.basemaps import OpenFreeMap

        >>> m = Map(MapOptions(style=OpenFreeMap.LIBERTY))
    """

    POSITRON = "positron"
    LIBERTY = "liberty"
    BRIGHT = "bright"


def construct_openfreemap_basemap_url(
    style_name: str | OpenFreeMap = OpenFreeMap.LIBERTY,
) -> str:
    return f"https://tiles.openfreemap.org/styles/{OpenFreeMap(style_name).value}"
