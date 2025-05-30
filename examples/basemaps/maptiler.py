import os

from maplibre import Map, MapOptions
from maplibre.__future__.controls import GeocodingControl
from maplibre.basemaps import Basemap, MapTiler

# from maplibre.sky import Sky
# from maplibre.light import Light
from maplibre.config import config
from maplibre.controls import (
    ControlPosition,
    MapTilerGeocodingControl,
    GlobeControl,
    NavigationControl,
)

print(config.maptiler_api_key_env_var)
# os.environ[options.maptiler_api_key_env_var] = "your-api-key"
print(config.maptiler_api_key)

# sky = Sky(atmosphere_blend=["interpolate", ["linear"], ["zoom"], 0, 1, 5, 1, 7, 0])
# light = Light(anchor="map", position=[1.5, 90, 80], intensity=0.5)


style = Basemap.maptiler_url(MapTiler.SATELLITE)
# print(style)

map_options = MapOptions(style=style)

m = Map(
    map_options,
    controls=[
        NavigationControl(),
        GlobeControl(),
        MapTilerGeocodingControl(
            collapsed=True,
            show_place_type="always",
            country="de",
            position=ControlPosition.TOP_LEFT
        ),
        # GeocodingControl(collapsed=True, position=ControlPosition.TOP_LEFT)
    ],
)
# m.set_light(light)
print(m._geocoder_type)
m.save(preview=True)
