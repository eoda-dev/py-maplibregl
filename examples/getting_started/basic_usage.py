from maplibre import Layer, LayerType, Map, MapOptions
from maplibre.sources import GeoJSONSource

vancouver_blocks = GeoJSONSource(
    data="https://raw.githubusercontent.com/visgl/deck.gl-data/master/examples/geojson/vancouver-blocks.json",
)

map_options = MapOptions(
    center=(-123.1256, 49.24658),
    zoom=12,
    hash=True,
    pitch=35,
)

m = Map(map_options)
m.add_layer(
    Layer(
        type=LayerType.LINE,
        source=vancouver_blocks,
        paint={"line-color": "white"},
    )
)

m.save(preview=True)
