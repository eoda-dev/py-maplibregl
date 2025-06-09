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
    m = mlb.MapWidget()
    return (m,)


@app.cell
def _():
    image_url = "https://maplibre.org/maplibre-gl-js/docs/assets/custom_marker.png"
    image_id = "custom-marker"
    return image_id, image_url


@app.cell
def _(image_id, image_url, m):
    m.add_call("addImage", image_id, image_url)
    return


@app.cell
def _():
    data_url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"
    return (data_url,)


@app.cell
def _(data_url, image_id, mlb):
    vector = mlb.Layer(
        id="icons",
        type=mlb.LayerType.SYMBOL,
        source=mlb.GeoJSONSource(data=data_url),
        layout={"icon-image": image_id, "icon-overlap": "always"},
    )
    return (vector,)


@app.cell
def _(m, vector):
    m.add_layer(vector)
    return


@app.cell
def _(m):
    m
    return


@app.cell
def _(m):
    m.add_tooltip("icons", "{{ place }}, {{ mag }}")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
