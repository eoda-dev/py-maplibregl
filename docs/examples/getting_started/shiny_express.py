import json

from shiny import reactive
from shiny.express import input, render, ui

from maplibre import Map, MapContext, MapOptions, render_maplibregl
from maplibre.controls import Marker

ui.h1("My awesome MapLibre map")


@render_maplibregl
def mapgl():
    return Map(MapOptions(zoom=3, pitch=40))


ui.div("Click on map to show coords.")


@render.code
def coords():
    return str(input.mapgl_clicked())


ui.div("Move map to change view state.")


@render.code
def view_state():
    return json.dumps(input.mapgl_view_state(), indent=2)


@reactive.Effect
@reactive.event(input.mapgl_clicked)
async def set_marker():
    async with MapContext("mapgl") as m:
        m.add_marker(Marker(lng_lat=input.mapgl_clicked()["coords"].values()))
