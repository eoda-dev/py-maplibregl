# Shiny Express App

import json

from maplibre import Map, MapOptions, render_maplibregl
from maplibre.basemaps import Carto
from maplibre.controls import ControlPosition, NavigationControl, ScaleControl
from maplibre.plugins import MapboxDrawControls, MapboxDrawOptions
from maplibre.ui import use_mapboxgl_draw

# from shiny import reactive
from shiny.express import input, render, ui

geojson_feature = {
    "id": "xyz",
    "type": "Feature",
    "properties": {},
    "geometry": {
        "coordinates": [
            [
                [-122.4523683552298, 37.775540942000546],
                [-122.41910082339776, 37.75932501909665],
                [-122.43487191413453, 37.72543546737114],
                [-122.46053073611722, 37.729612763886834],
                [-122.4523683552298, 37.775540942000546],
            ]
        ],
        "type": "Polygon",
    },
}

m = Map(
    MapOptions(
        style=Carto.POSITRON,
        center=(-122.4, 37.74),
        zoom=12,
        hash=True,
        pitch=40,
    )
)
m.add_control(NavigationControl())
m.add_control(ScaleControl(), ControlPosition.BOTTOM_LEFT)

# Optional: only activate a given set of controls
draw_options = MapboxDrawOptions(
    display_controls_default=False,
    controls=MapboxDrawControls(polygon=True, line_string=True, trash=True),
)
# Use options from above
# m.add_mapbox_draw(draw_options, geojson=geojson_feature)

# If no options are passed, all controls are activated by default
m.add_mapbox_draw(geojson=geojson_feature)

# Shiny Express
use_mapboxgl_draw()


@render_maplibregl
def maplibre():
    return m


@render.code
def selected_features():
    obj = input.maplibre_draw_features_selected()
    obj["event"] = "selected"
    print(obj)
    return json.dumps(obj["features"], indent=2)


@render.code
def on_features_created():
    obj = input.maplibre_draw_features_created()
    obj["event"] = "created"
    return json.dumps(obj, indent=2)


@render.code
def on_features_deleted():
    obj = input.maplibre_draw_features_deleted()
    obj["event"] = "deleted"
    return json.dumps(obj, indent=2)


@render.code
def on_features_updated():
    obj = input.maplibre_draw_features_updated()
    obj["event"] = "updated"
    return json.dumps(obj, indent=2)


if __name__ == "__main__":
    m.save(preview=True)
