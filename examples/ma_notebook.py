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
def _(Map, MapOptions, NavigationControl):
    m = Map(MapOptions(center=(-122.4, 37.74), zoom=12), controls=[NavigationControl()])
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
def _(m):
    m.add_mapbox_draw()
    return


@app.cell
def _(m):
    m.draw_features_created
    return


@app.cell
def _(m):
    m.draw_features_updated
    return


@app.cell
def _(m):
    m.draw_feature_collection_all
    return


@app.cell
def _():
    deck_grid_layer = {
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
    return (deck_grid_layer,)


@app.cell
def _(deck_grid_layer, m):
    m.add_deck_layers([deck_grid_layer], tooltip="Number of points: {{ count }}")
    return


@app.cell
def _(Layer, LayerType, Map, MapOptions, NavigationControl):
    from maplibre.basemaps import construct_basemap_style

    PMTILES_URL = "https://pmtiles.io/protomaps(vector)ODbL_firenze.pmtiles"

    pmtiles_source = {
        "type": "vector",
        "url": f"pmtiles://{PMTILES_URL}",
        "attribution": '© <a href="https://openstreetmap.org">OpenStreetMap</a>',
    }

    custom_basemap = construct_basemap_style(
        sources={"pmtiles": pmtiles_source},
        layers=[
            Layer(
                id="buildings",
                source="pmtiles",
                source_layer="landuse",
                type=LayerType.FILL,
                paint={"fill-color": "steelblue"},
            ),
            Layer(
                id="roads",
                source="pmtiles",
                source_layer="roads",
                type=LayerType.LINE,
                paint={"line-color": "black"},
            ),
            Layer(
                id="mask",
                source="pmtiles",
                source_layer="mask",
                type=LayerType.FILL,
                paint={"fill-color": "white"},
            ),
        ],
    )


    map_options = MapOptions(
        style=custom_basemap,
        bounds=(11.154026, 43.7270125, 11.3289395, 43.8325455),
    )


    def create_map():
        m = Map(map_options)
        m.add_control(NavigationControl())
        return m
    return (
        PMTILES_URL,
        construct_basemap_style,
        create_map,
        custom_basemap,
        map_options,
        pmtiles_source,
    )


@app.cell
def _(create_map):
    m2 = create_map()
    m2
    return (m2,)


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
