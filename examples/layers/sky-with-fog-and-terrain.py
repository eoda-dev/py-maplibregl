# See
# - https://maplibre.org/maplibre-gl-js/docs/examples/3d-terrain/
# - https://maplibre.org/maplibre-gl-js/docs/examples/sky-with-fog-and-terrain/
#
from maplibre import Map, MapOptions, Layer, LayerType
from maplibre.sources import RasterTileSource, RasterDEMSource
from maplibre.basemaps import Basemap
from maplibre.controls import NavigationControl, TerrainControl
from maplibre.sky import Sky
from maplibre.terrain import Terrain


style = Basemap(
    sources=dict(
        osm=RasterTileSource(
            tiles=["https://a.tile.openstreetmap.org/{z}/{x}/{y}.png"],
            tile_size=256,
            attribution="&copy; OpenStreetMap Contributors",
            max_zoom=19,
        ),
        # Use a different source for terrain and hillshade layers, to improve render quality
        terrain=RasterDEMSource(url="https://demotiles.maplibre.org/terrain-tiles/tiles.json", tile_size=256),
        hillshade=RasterDEMSource(url="https://demotiles.maplibre.org/terrain-tiles/tiles.json", tile_size=256),
    ),
    layers=[
        Layer(type=LayerType.RASTER, source="osm"),
        Layer(type=LayerType.HILLSHADE, source="hillshade").set_paint_props(hillshade_shadow_color="#473B24"),
    ],
    sky=Sky(sky_color="steelblue", horizon_color="orange", fog_color="grey"),
    terrain=Terrain(source="terrain")
).to_dict()

map_options = MapOptions(
    style=style,
    zoom=12,
    # center=(11.39085, 47.27574),
    center=(11.2953, 47.5479),
    pitch=77,
    hash=True,
    max_zoom=18,
    max_pitch=85
)

m = Map(map_options, controls=[NavigationControl(), TerrainControl(source="terrain")])
# m.set_terrain("terrain")
# m.set_sky(Sky(sky_color="steelblue", horizon_color="orange", fog_color="grey"))
m.save(preview=True)
