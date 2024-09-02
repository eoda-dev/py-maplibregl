from maplibre import Map, MapOptions
from maplibre.basemaps import MAPLIBRE_DEMO_TILES, MapTiler
from maplibre.controls import NavigationControl

# map_options = MapOptions(style=MapTiler.WINTER)
map_options = MapOptions(style=MAPLIBRE_DEMO_TILES)
m = Map(map_options=map_options, controls=[NavigationControl()])
m.save("/tmp/py-maplibre-express.html")
