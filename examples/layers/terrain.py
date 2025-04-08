# See https://maplibre.org/maplibre-gl-js/docs/examples/3d-terrain/
#
from maplibre import Map, MapOptions, Layer, LayerType
from maplibre.sources import SourceType, RasterTileSource, RasterDEMSource
from maplibre.basemaps import construct_basemap_style
from maplibre.controls import NavigationControl, TerrainControl, GlobeControl

style = construct_basemap_style(
    sources=dict(
        osm=RasterTileSource(
            tiles=["https://a.tile.openstreetmap.org/{z}/{x}/{y}.png"],
            tile_size=256,
            attribution="&copy; OpenStreetMap Contributors",
            max_zoom=19,
        ),
        hillshade=RasterDEMSource(url="https://demotiles.maplibre.org/terrain-tiles/tiles.json", tile_size=256),
    ),
    layers=[
        Layer(type=LayerType.RASTER, source="osm"),
        Layer(type=LayerType.HILLSHADE, source="hillshade").set_paint_props(hillshade_shadow_color="#473B24"),
    ],
)

map_options = MapOptions(
    style=style,
    zoom=12,
    center=(11.39085, 47.27574),
    pitch=70,
    hash=True,
)

m = Map(map_options, controls=[NavigationControl(), TerrainControl(source="hillshade"), GlobeControl()])
m.set_terrain("hillshade")
m.save(preview=True)
