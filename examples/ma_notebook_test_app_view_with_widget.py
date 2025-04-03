import marimo

__generated_with = "0.10.17"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from maplibre import Layer, LayerType, MapOptions
    from maplibre.sources import GeoJSONSource
    from maplibre.ipywidget import MapWidget as Map
    from maplibre.controls import NavigationControl, ScaleControl, ControlPosition
    Map._use_message_queue = False
    return (
        ControlPosition,
        GeoJSONSource,
        Layer,
        LayerType,
        Map,
        MapOptions,
        NavigationControl,
        ScaleControl,
        mo,
    )


@app.cell
def _(GeoJSONSource, Layer, LayerType):
    circle_layer = Layer(
        id="earthquakes",
        type=LayerType.CIRCLE,
        source=GeoJSONSource(data="https://docs.mapbox.com/mapbox-gl-js/assets/earthquakes.geojson")
    ).set_paint_props(circle_color="yellow")
    return (circle_layer,)


@app.cell
def _(Map, NavigationControl, circle_layer):
    m = Map(controls=[NavigationControl()], layers=[circle_layer])
    return (m,)


@app.cell
def _(ControlPosition, ScaleControl, m):
    m.add_control(ScaleControl(position=ControlPosition.BOTTOM_LEFT))
    return


@app.cell
def _(m):
    m.add_tooltip(layer_id="earthquakes", prop="mag")
    return


@app.cell
def _():
    # m.add_control(ScaleControl(position=ControlPosition.BOTTOM_LEFT))
    return


@app.cell
def _(m, mo):
    widget = mo.ui.anywidget(m)
    return (widget,)


@app.cell
def _(widget):
    widget
    return


@app.cell
def _(m, mo):
    mo.ui.dropdown(["red", "yellow"], label="circle-color", on_change=lambda x: m.set_paint_property("earthquakes", "circle-color", x))
    return


@app.cell
def _(widget):
    widget.view_state
    return


if __name__ == "__main__":
    app.run()
