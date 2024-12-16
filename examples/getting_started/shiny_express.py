import json

from shiny.express import input, render, ui

from maplibre import Map, MapOptions, render_maplibregl

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
def views_tate():
    return json.dumps(input.mapgl_view_state(), indent=2)
