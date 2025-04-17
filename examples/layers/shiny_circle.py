from shiny import reactive
from shiny.express import input, render, ui

from maplibre import Layer, LayerType, Map, MapLibreRenderer, MapOptions
from maplibre.basemaps import OpenFreeMap
from maplibre.controls import GlobeControl, NavigationControl
from maplibre.sources import GeoJSONSource

data = "https://docs.mapbox.com/mapbox-gl-js/assets/earthquakes.geojson"
layer_id = "earthquakes"

earthquakes = Layer(
    id=layer_id, type=LayerType.CIRCLE, source=GeoJSONSource(data=data)
).set_paint_props(circle_color="yellow")


@MapLibreRenderer
def my_map():
    m = Map(
        MapOptions(style=OpenFreeMap.LIBERTY),
        controls=[NavigationControl(), GlobeControl()],
        layers=[earthquakes],
    )
    m.add_tooltip(layer_id)
    return m
