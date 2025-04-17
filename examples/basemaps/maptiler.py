import os

from maplibre import Map, MapOptions
from maplibre.basemaps import BasemapStyle, MapTiler

# from maplibre.sky import Sky
# from maplibre.light import Light
from maplibre.config import options
from maplibre.controls import (
    ControlPosition,
    GeocodingControl,
    GlobeControl,
    NavigationControl,
)

print(options.maptiler_api_key_env_var)
# os.environ[options.maptiler_api_key_env_var] = "your-api-key"
print(options.maptiler_api_key)

# sky = Sky(atmosphere_blend=["interpolate", ["linear"], ["zoom"], 0, 1, 5, 1, 7, 0])
# light = Light(anchor="map", position=[1.5, 90, 80], intensity=0.5)


style = BasemapStyle.maptiler_url(MapTiler.SATELLITE)
# print(style)

map_options = MapOptions(style=style)

m = Map(
    map_options,
    controls=[
        NavigationControl(),
        GlobeControl(),
        GeocodingControl(position=ControlPosition.TOP_LEFT),
    ],
)
# m.set_light(light)
m.save(preview=True)
