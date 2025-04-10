from maplibre import Map, MapOptions, Layer, LayerType
from maplibre.basemaps import OpenFreeMap
from maplibre.sky import Sky
from maplibre.light import Light
from maplibre.controls import NavigationControl, GlobeControl

map_options = MapOptions(
    style=OpenFreeMap.POSITRON,
    zoom=0,
    center=(137.9150899566626, 36.25956997955441),
)

sky = Sky(
    atmosphere_blend=["interpolate", ["linear"], ["zoom"], 0, 1, 5, 1, 7, 0]
)

light = Light(anchor="map", position=[1.5, 90, 80], intensity=0.5)

m = Map(map_options, controls=[NavigationControl(), GlobeControl()])
m.set_projection("globe")
m.set_sky(sky)
m.set_light(light)
m.save(preview=True, style="background-color: black; height: 600px;")
