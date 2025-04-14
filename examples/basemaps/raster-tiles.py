# Example taken from https://maplibre.org/maplibre-gl-js/docs/examples/map-tiles/

from maplibre import Map, MapOptions, Layer, LayerType
from maplibre.sources import RasterSource
from maplibre.basemaps import construct_basemap_style, BasemapStyle

# style = construct_basemap_style(
style = BasemapStyle(
    sources={
        "raster-tiles": RasterSource(
            tiles=["https://a.tile.openstreetmap.org/{z}/{x}/{y}.png"],
            tile_size=256,
            attribution="&copy; OpenStreetMap Contributors",
        )
    },
    layers=[
        Layer(
            id="simple-tiles",
            type=LayerType.RASTER,
            source="raster-tiles",
            min_zoom=0,
            max_zoom=20,
        )
    ],
).to_dict()

map_options = MapOptions(style=style, center=(-74.5, 40), zoom=2)

m = Map(map_options)
m.save(preview=True)
