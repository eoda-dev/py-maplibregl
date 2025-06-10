import marimo

__generated_with = "0.10.17"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import maplibre as mlb
    return mlb, mo


@app.cell
def _():
    grid = {
        "@@type": "GridLayer",
        "id": "GridLayer",
        "data": "https://raw.githubusercontent.com/visgl/deck.gl-data/master/website/sf-bike-parking.json",
        "extruded": True,
        "getPosition": "@@=COORDINATES",
        "getColorWeight": "@@=SPACES",
        "getElevationWeight": "@@=SPACES",
        "elevationScale": 4,
        "cellSize": 200,
        "pickable": True,
    }
    return (grid,)


@app.cell
def _(mlb):
    map_options = mlb.MapOptions(
        # style=mlb.Carto.POSITRON,
        center=(-122.4, 37.74),
        zoom=12,
        # hash=True,
        pitch=40,
    )
    return (map_options,)


@app.cell
def _(map_options, mlb):
    # m = mlb.MapWidget(map_options, controls=[mlb.controls.NavigationControl()])
    m = mlb.MapWidget(map_options)
    return (m,)


@app.cell
def _(grid, m):
    #m.add_call("setCenter", (-122.4, 37.74))
    #m.add_call("setZoom", 12)
    m.add_call("addMapboxOverlay", [grid])
    return


@app.cell
def _(m, mo):
    widget = mo.ui.anywidget(m)
    return (widget,)


@app.cell
def _(widget):
    widget
    # m
    return


@app.cell
def _():
    # m.add_call("addMapboxOverlay", [grid])
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
