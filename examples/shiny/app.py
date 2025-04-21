from shiny import App, reactive, ui

from maplibre import Map
from maplibre.controls import Marker, NavigationControl, MapTilerGeocodingControl, ControlPosition, GeocodingControl
from maplibre.shiny import output_maplibregl, MapLibreGLRenderer, MapContext
from maplibre.__future__.controls import GeocoderType

app_ui = ui.div(
    output_maplibregl("maplibre_map", height=600, geocoder=GeocoderType.MAPTILTER),
    ui.div("Click on map to set a marker"),
)


def server(input, output, session):
    @MapLibreGLRenderer
    def maplibre_map():
        return Map(
            controls=[
                NavigationControl(),
                MapTilerGeocodingControl(position=ControlPosition.TOP_LEFT, collapsed=True),
                # GeocodingControl(position=ControlPosition.TOP_LEFT, collapsed=True)
            ]
        )

    @reactive.Effect
    @reactive.event(input.maplibre_map_clicked)
    async def coords():
        async with MapContext("maplibre_map") as m:
            value = input.maplibre_map_clicked()
            print(value)
            lng_lat = tuple(value["coords"].values())
            marker = Marker(lng_lat=lng_lat)
            m.add_marker(marker)
            m.add_call("flyTo", {"center": lng_lat})


app = App(app_ui, server)
