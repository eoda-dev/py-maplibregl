from shiny import App, ui, module, reactive
from maplibre import output_maplibregl, render_maplibregl, Map, MapContext


@module.ui
def shiny_module_ui():
    return ui.page_fluid(
        ui.panel_title("MapLibre"),
        ui.input_action_button("btn", "Click"),
        output_maplibregl("mapgl", height=600),
    )


@module.server
def shiny_module_server(input, output, session):

    @render_maplibregl
    def mapgl():
        m = Map()
        return m

    @reactive.effect
    @reactive.event(input.btn)
    async def move_it(): 
        async with MapContext("mapgl") as m:
            m.add_call("flyTo", {"center": [-1.66928, 48.1024159], "zoom": 15})


app_ui = ui.page_fluid(shiny_module_ui("shiny_mod"))


def server(input, output, session):
    shiny_module_server("shiny_mod")


app = App(app_ui, server)

