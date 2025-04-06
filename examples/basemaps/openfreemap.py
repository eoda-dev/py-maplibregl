from maplibre import Map, MapOptions
from maplibre.basemaps import OpenFreeMap

m = Map(MapOptions(style=OpenFreeMap.BRIGHT))
m.save(preview=True)
