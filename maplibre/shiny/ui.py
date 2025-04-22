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


class HTMLDependencySource(BaseModel):
    package: str = "maplibre"
    subdir: str = "srcjs"


class ScriptItem(BaseModel):
    src: str
    type: str = "module"


class StylesheetItem(BaseModel):
    href: str


class MyHTMLDependency(BaseModel):
    name: str
    version: str
    source: HTMLDependencySource | dict = HTMLDependencySource()
    script: ScriptItem | list[ScriptItem] | None = None
    stylesheet: StylesheetItem | list[StylesheetItem] | None = None
    all_files: bool = False

    def to_HTMLDependency(self) -> HTMLDependency:
        return HTMLDependency(**self.model_dump(exclude_none=True))


def output_maplibregl(
    id: str, height: int | str = 400, geocoder_type: GeocoderType | None = None
) -> Tag:
    """Create an output container for a `Map` object

    Args:
        id (str): An output id of a `Map` object.
    """
    geocoder_type = geocoder_type or GeocoderType.MAPTILTER

    js_file = "pywidget.js"
    css_file = (
        "ipywidget.maplibre-geocoder.css"
        if geocoder_type == GeocoderType.MAPLIBRE
        else "pywidget.css"
    )

    if isinstance(height, int):
        height = f"{height}px"

    return shiny.ui.div(
        MyHTMLDependency(
            name="maplibre-bindings",
            version=importlib.metadata.version("maplibre"),
            script=ScriptItem(src=js_file),
            stylesheet=StylesheetItem(href=css_file),
        ).to_HTMLDependency(),
        id=shiny.module.resolve_id(id),
        class_=SHINY_OUTPUT_CLASS,
        style=f"height: {height}",
    )
