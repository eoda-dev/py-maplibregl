from maplibre import Map, MapOptions
from maplibre.basemaps import Carto

m = Map(MapOptions(style=Carto.DARK_MATTER_NOLABELS))
m.save(preview=True)
