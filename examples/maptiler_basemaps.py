from maplibre import Map, MapOptions
from maplibre.basemaps import Maptiler
from maplibre.controls import NavigationControl

map_options = MapOptions(style=Maptiler.WINTER)
m = Map(map_options=map_options, controls=[NavigationControl()])
m.save("/tmp/py-maplibre-express.html")
