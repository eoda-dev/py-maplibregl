import marimo

__generated_with = "0.10.17"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import maplibre as mlb
    return mlb, mo


@app.cell
def _(mlb):
    m = mlb.MapWidget(controls=[mlb.controls.GlobeControl()])
    return (m,)


@app.cell
def _(m):
    m.map_options
    return


@app.cell
def _(m):
    m.add_call("test", [1, 2])
    return


@app.cell
def _(m, mlb):
    m.add_control(mlb.controls.ScaleControl())
    m.add_call("setCenter", (50, 10))
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
def _(m, mlb):
    m.add_control(mlb.controls.FullscreenControl())
    # print("yes")
    return


@app.cell
def _():
    # m.get_manager_state()
    return


@app.cell
def _(m):
    m.msg
    return


@app.cell
def _(widget):
    widget.value
    return


@app.cell
def _(m):
    m.add_call("setCenter", (50, 10))
    return


@app.cell
def _(m):
    m.add_call("setZoom", 10)
    return


@app.cell
def _(mlb):
    VECTOR_TILES_URL = "https://demotiles.maplibre.org/tiles/tiles.json"
    LAYER_ID = "countries"

    vector_source = mlb.sources.VectorTileSource(
        url=VECTOR_TILES_URL,
        # tiles=["https://demotiles.maplibre.org/tiles/{z}/{x}/{y}.pbf"],
        min_zoom=0,
        max_zoom=6,
    )

    vector_layer = mlb.Layer(
        type=mlb.LayerType.FILL,
        id=LAYER_ID,
        source=vector_source,
        paint={"fill-color": "lightgreen", "fill-outline-color": "black"},
        source_layer="countries",
    )
    return LAYER_ID, VECTOR_TILES_URL, vector_layer, vector_source


@app.cell
def _(m, vector_layer):
    m.add_layer(vector_layer)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
