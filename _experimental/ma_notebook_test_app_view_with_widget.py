import marimo

__generated_with = "0.10.17"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from maplibre import Layer, LayerType, MapOptions
    from maplibre.sources import GeoJSONSource, VectorTileSource
    from maplibre.ipywidget import MapWidget as Map
    from maplibre.controls import NavigationControl, ScaleControl, ControlPosition
    from maplibre.expressions import color_match_expr
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
        VectorTileSource,
        color_match_expr,
        mo,
    )


@app.cell
def _(VectorTileSource):
    blm_sma_source= VectorTileSource(
        tiles=["https://tiles.lightfield.ag/blm_national_surface_management_data/{z}/{x}/{y}.mvt"],
        min_zoom=0,
        max_zoom=9
    )
    return (blm_sma_source,)


@app.cell
def _(color_match_expr):
    fill_color = color_match_expr("ADMIN_DEPT_CODE", ["PVT", "DOD", "DOE", "DOI", "USDA"], "viridis")
    # fill_color
    return (fill_color,)


@app.cell
def _(Layer, LayerType, blm_sma_source, fill_color):
    blm_sma_layer = Layer(
        id="blm-sma",
        type=LayerType.FILL,
        source=blm_sma_source,
        source_layer="blm_national_surface_management_data"
    ).set_paint_props(fill_color=fill_color, fill_outline_color="steelblue")
    return (blm_sma_layer,)


@app.cell
def _(Map, NavigationControl, blm_sma_layer):
    m = Map(controls=[NavigationControl()], layers=[blm_sma_layer])
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
def _(color_match_expr, m, mo):
    mo.ui.dropdown(
        ["viridis", "YlOrRd", "Blues"],
        label="cmap",
        on_change=lambda x: m.set_paint_property(
            "blm-sma",
            "fill-color",
            color_match_expr("ADMIN_DEPT_CODE", ["PVT", "DOD", "DOE", "DOI", "USDA"], cmap=x)
        )
    )
    return


@app.cell
def _(widget):
    widget.view_state
    return


if __name__ == "__main__":
    app.run()
