from __future__ import annotations

import importlib.metadata
from htmltools import HTMLDependency, Tag
from pydantic import BaseModel

from ..__future__.controls import GeocoderType

try:
    import shiny
except ImportError as e:
    print(e)


SHINY_OUTPUT_CLASS = "shiny-maplibregl-output"


class HTMLSource(BaseModel):
    package: str = "maplibre"
    subdir: str = "srcjs"


class JSScript(BaseModel):
    src: str
    type: str = "module"


class Stylesheet(BaseModel):
    href: str


class MyHTMLDependency(BaseModel):
    name: str
    version: str
    source: HTMLSource | dict = HTMLSource()
    script: JSScript | list[JSScript] | None = None
    stylesheet: Stylesheet | list[Stylesheet] | None = None
    all_files: bool = False

    def to_HTMLDependency(self) -> HTMLDependency:
        return HTMLDependency(**self.model_dump(exclude_none=True))


def output_maplibregl(id: str, height: int | str = 400, geocoder: GeocoderType | None = None) -> Tag:
    """Create an output container for a `Map` object

    Args:
        id (str): An output id of a `Map` object.
    """
    geocoder = geocoder or GeocoderType.MAPTILTER

    js_file = "pywidget.js"
    css_file = "ipywidget.maplibre-geocoder.css" if geocoder == GeocoderType.MAPLIBRE else "pywidget.css"

    if isinstance(height, int):
        height = f"{height}px"

    return shiny.ui.div(
        MyHTMLDependency(
            name="maplibre-bindings",
            version=importlib.metadata.version("maplibre"),
            script=JSScript(src=js_file),
            stylesheet=Stylesheet(href=css_file),
        ).to_HTMLDependency(),
        id=shiny.module.resolve_id(id),
        class_=SHINY_OUTPUT_CLASS,
        style=f"height: {height}",
    )
