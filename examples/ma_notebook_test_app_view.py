import marimo

__generated_with = "0.10.17"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from maplibre import Layer, LayerType, MapOptions
    from maplibre.sources import GeoJSONSource
    from maplibre.ipywidget import MapWidget as Map
    from maplibre.controls import NavigationControl, ScaleControl
    Map._use_message_queue = False
    return (
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
def _(ScaleControl, m):
    m.add_control(ScaleControl())
    return


@app.cell
def _(m):
    m.add_tooltip(layer_id="earthquakes", prop="mag")
    return


@app.cell
def _(m):
    m
    return


if __name__ == "__main__":
    app.run()
