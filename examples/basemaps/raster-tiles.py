# Example taken from https://maplibre.org/maplibre-gl-js/docs/examples/map-tiles/

from maplibre import Map, MapOptions, Layer, LayerType
from maplibre.sources import RasterSource
from maplibre.basemaps import construct_basemap_style

style = construct_basemap_style(
    sources={
        "raster-tiles": RasterSource(
            tiles=[
                # "https://tiles.stadiamaps.com/tiles/stamen_watercolor/{z}/{x}/{y}.jpg",
                "https://a.tile.openstreetmap.org/{z}/{x}/{y}.png"
            ],
            tile_size=256,
            attribution="&copy; OpenStreetMap Contributors",
            # (
            #    'Map tiles by <a target="_blank" href="https://stamen.com">Stamen Design</a>;'
            #    ' Hosting by <a href="https://stadiamaps.com/" target="_blank">Stadia Maps</a>. Data &copy;'
            #    ' <a href="https://www.openstreetmap.org/about" target="_blank">OpenStreetMap</a> contributors'
            # ),
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
)

map_options = MapOptions(style=style, center=(-74.5, 40), zoom=2)

m = Map(map_options)
m.save(preview=True)
