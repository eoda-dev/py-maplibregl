from maplibre import Layer, LayerType, Map, MapOptions
from maplibre.basemaps import Carto
from maplibre.controls import (
    NavigationControl,
    ScaleControl,
    ControlPosition,
    GlobeControl,
)
from maplibre.sources import GeoJSONSource

data = "https://docs.mapbox.com/mapbox-gl-js/assets/earthquakes.geojson"
layer_id = "earthquakes"

layer = Layer(
    id=layer_id, type=LayerType.CIRCLE, source=GeoJSONSource(data=data)
).set_paint_props(circle_color="yellow")

m = Map(MapOptions(style=Carto.POSITRON))
m.add_control(NavigationControl())
m.add_control(ScaleControl(position=ControlPosition.BOTTOM_LEFT))
m.add_control(GlobeControl())
m.add_layer(layer)
m.add_tooltip(layer_id)
# m.set_projection(type=["step", ["zoom"], "vertical-perspective", 3, "mercator"])

m.save(preview=True)
