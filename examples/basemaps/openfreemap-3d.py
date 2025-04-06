from maplibre import Map, MapOptions
from maplibre.basemaps import OpenFreeMap
from maplibre.controls import NavigationControl

threed_buildings = {
    "id": "3d-buildings",
    "source": "openmaptiles",
    "source-layer": "building",
    "type": "fill-extrusion",
    "min-zoom": 15,
    "paint": {
        "fill-extrusion-color": [
            "interpolate",
            ["linear"],
            ["get", "render_height"],
            0,
            "lightgray",
            200,
            "royalblue",
            400,
            "lightblue",
        ],
        "fill-extrusion-height": [
            "interpolate",
            ["linear"],
            ["zoom"],
            15,
            0,
            16,
            ["get", "render_height"],
        ],
        "fill-extrusion-base": [
            "case",
            [">=", ["get", "zoom"], 16],
            ["get", "render_min_height"],
            0,
        ],
    },
}

m = Map(
    MapOptions(style=OpenFreeMap.BRIGHT, center=(-74.0066, 40.7135), zoom=16, pitch=45, bearing=-17),
    controls=[NavigationControl()],
)
m.add_layer(threed_buildings)
m.save(preview=True)
