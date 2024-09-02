from maplibre import Map, MapOptions
from maplibre.basemaps import MapTiler
from maplibre.controls import NavigationControl

map_options = MapOptions(style=MapTiler.WINTER)
m = Map(map_options=map_options, controls=[NavigationControl()])
m.save("/tmp/py-maplibre-express.html")
