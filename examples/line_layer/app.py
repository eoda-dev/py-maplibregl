from pymaplibregl import (
    ControlPosition,
    ControlType,
    Layer,
    LayerType,
    Map,
    output_maplibregl,
    render_maplibregl,
)
from pymaplibregl.basemaps import Carto
from shiny import App, ui

SOURCE_ID = "vancouver-blocks"

vancouver_blocks = {
    "type": "geojson",
    "data": "https://raw.githubusercontent.com/visgl/deck.gl-data/master/examples/geojson/vancouver-blocks.json",
}


line_layer = Layer(
    LayerType.LINE,
    id_="vancouver-blocks-line",
    source=SOURCE_ID,
    paint={"line-color": "yellow", "line-opacity": 1.0},
)

center = [-123.0753056, 49.2686511]

app_ui = ui.page_fluid(
    ui.panel_title("Hello PyMapLibreGL!"),
    output_maplibregl("ml_map", height=600),
)


def server(input, output, session):
    @render_maplibregl
    async def ml_map():
        map = Map(style=Carto.DARK_MATTER, center=center, zoom=12, pitch=35)
        map.add_control(
            ControlType.SCALE, {"unit": "imperial"}, position=ControlPosition.TOP_LEFT
        )
        map.add_control(ControlType.FULLSCREEN, position=ControlPosition.BOTTOM_LEFT)
        map.add_source(SOURCE_ID, vancouver_blocks)
        map.add_layer(line_layer)
        # map.add_call("setZoom", [[3]])
        # map.add_call("setCenter", [[0, 0]])
        # map.add_call("flyTo", [{"center": [9.5, 51.31667], "zoom": 4}])
        return map


app = App(app_ui, server)

if __name__ == "__main__":
    app.run()