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
    data_url = "pmtiles://https://pmtiles.io/protomaps(vector)ODbL_firenze.pmtiles"
    return (data_url,)


@app.cell
def _(data_url, mlb):
    source = mlb.VectorSource(
        url=data_url,
        attribution='© <a href="https://openstreetmap.org">OpenStreetMap</a>'
    )
    return (source,)


@app.cell
def _(mlb):
    l = mlb.Layer(
        id="buildings",
        source="pmtiles",
        source_layer="landuse",
        type=mlb.LayerType.FILL,
        paint={"fill-color": "steelblue", "fill-opacity": 0.5},
    )
    return (l,)


@app.cell
def _(mlb):
    m = mlb.MapWidget()
    return (m,)


@app.cell
def _(m, source):
    # m.add_call("setCenterFromPMTiles", "https://pmtiles.io/protomaps(vector)ODbL_firenze.pmtiles", 6)
    m.add_source("pmtiles", source)
    return


@app.cell
def _(l, m):
    m.add_layer(l)
    return


@app.cell
def _(m):
    # m.add_call("setCenterFromPMTiles", "https://pmtiles.io/protomaps(vector)ODbL_firenze.pmtiles")
    # m.fit_bounds((11.154026, 43.7270125, 11.3289395, 43.8325455))
    m.add_call("fitBoundsFromPMTiles", "https://pmtiles.io/protomaps(vector)ODbL_firenze.pmtiles")
    return


@app.cell
def _(m, mo):
    widget = mo.ui.anywidget(m)
    # m.add_call("setCenterFromPMTiles", "https://pmtiles.io/protomaps(vector)ODbL_firenze.pmtiles")
    return (widget,)


@app.cell
def _(widget):
    widget
    return


@app.cell
def _():
    # m.add_layer(l)
    return


@app.cell
def _(m):
    m.add_call("setCenterFromPMTiles", "https://pmtiles.io/protomaps(vector)ODbL_firenze.pmtiles")
    return


@app.cell
def _(m):
    m.add_call("setCenter", [0, 0])
    return


@app.cell
def _(m):
    m.add_call("fitBoundsFromPMTiles", "https://pmtiles.io/protomaps(vector)ODbL_firenze.pmtiles")
    return


@app.cell
def _():
    s = {
            "id": "gl-draw-line",
            "type": "line",
            "filter": ["all", ["==", "$type", "LineString"]],
            "layout": {
              "line-cap": "round",
              "line-join": "round"
            },
            "paint": {
              "line-color": "#D20C0C",
              # "line-dasharray": [0.2, 2],
              "line-width": 2
            }
        }
    return (s,)


@app.cell
def _(m, s):
    m.add_call("addControl", "MapboxDraw", dict(displayControlsDefault=True, styles=[s]), "top-left")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
