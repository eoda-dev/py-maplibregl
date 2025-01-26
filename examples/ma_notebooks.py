import marimo

__generated_with = "0.10.17"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from maplibre import Layer, LayerType
    from maplibre.sources import GeoJSONSource
    from maplibre.ipywidget import MapWidget as Map
    from maplibre.controls import NavigationControl, ScaleControl
    return (
        GeoJSONSource,
        Layer,
        LayerType,
        Map,
        NavigationControl,
        ScaleControl,
        mo,
    )


@app.cell
def _(Map, NavigationControl):
    m = Map(controls=[NavigationControl()])
    return (m,)


@app.cell
def _(m, mo):
    widget = mo.ui.anywidget(m)
    return (widget,)


@app.cell
def _(widget):
    widget
    return


@app.cell
def _(widget):
    widget.value
    return


@app.cell
def _():
    # m.add_mapbox_draw()
    return


@app.cell
def _(GeoJSONSource, Layer, LayerType, m):
    layer = Layer(
        id="my layer",
        type=LayerType.CIRCLE,
        source=GeoJSONSource(data="https://docs.mapbox.com/mapbox-gl-js/assets/earthquakes.geojson")
    ).set_paint_props(circle_color="yellow")
    m.add_layer(layer)
    return (layer,)


@app.cell
def _():
    #m.add_call("removeLayer", ["my layer"])
    #m.add_call("removeSource", ["my layer"])
    return


@app.cell
def _():
    # m.set_paint_property("my layer", "circle-color", "red")
    return


@app.cell
def _(m, mo):
    mo.ui.dropdown(["red", "yellow"], label="circle-color", on_change=lambda x: m.set_paint_property("my layer", "circle-color", x))
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
