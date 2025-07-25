# Changelog for MapLibre for Python

## maplibre v0.3.5

* Fix #142 (thx to @nuayge)

## maplibre v0.3.4

* Fix pydantic list bug in `basemaps.py` and `light.py` (#144)
* Rename `basemap.BasemapStyle` to `basemap.Basemap`
* Move _Shiny_ bindings to `maplibre.shiny`
* Add
  - `maplibre.__future.__.controls.GeocodingControl`
  - `maplibre.__future.__.ipywidget.MapWidget`.
  - See also [maplibre-gl-geocoder](https://maplibre.org/maplibre-gl-js/docs/examples/geocoder/maplibre).

_Note:_ `maplibre-geocoder-css` overwrites `maptiler-geocoder-css`

## maplibre v0.3.3

* Switch to [MapLibre GL JS v5.3.1](https://github.com/maplibre/maplibre-gl-js/releases/tag/v5.3.1) 
* Bundle `maplibregl-js` with bindings
* Add [MapTiler Geocoding Control](https://docs.maptiler.com/sdk-js/modules/geocoding/api/usage/maplibre-gl-js/) (#138): `maplibre.controls.MapTilerGeocodingControl`
* Add `Map.base_layers` property

## maplibre v0.3.2

* Add `Sky` (#135), `Light` (#137) and `Terrain` (#134) style specifications
* Add `TerrainControl`
* Add `RasterDEMSource`
* Add `RasterSource` as alias for `RasterTileSource`
* Add `VectorSource` as alias for `VectorTileSource`
* Add `BasemapStyle` as successor to `construct_basemap_style`
* Add `BasemapStyle.symbol_layers` to get symbol layers from style
* Add `BasemapStyle.carto_url` etc as successors to `construct_carto_basemap_url` etc

## maplibre v0.3.1

* Switch to [MapLibre GL JS v5.3.0](https://github.com/maplibre/maplibre-gl-js/releases/tag/v5.3.0)
* Add `Map.set_projection` and `GlobeControl` to switch between _globe_ and _mercator_ projection

## maplibre v0.3.0

* Add 3d-buildings example
* Add `basemaps.OpenFreeMap`
* Make `shiny` and `htmltools` dependency optional
* Make `anywidget` dependency optional
* Add Mapbox Draw Ipywidget callbacks for
  * `draw.create`
  * `draw.update`
  * `draw.delete`

## maplibre v0.2.8

* Add Mapbox Draw Shiny callbacks for
  * `draw.create`
  * `draw.update`
  * `draw.delete`

## maplibre v0.2.7

* Add `basemaps.MapTiler`

* Add `maplibre.__future__`

* Add `Map.fit_bounds`

* Add expression helpers `maplibre.expressions`:
  * `interpolate`
  * `step_expr`
  * `quantile_expr`
  * `match_expr`
  * `color_step_expr`
  * `color_quantile_expr`
  * `color_match_expr`
  * `filter_expr`
  * `range_filter`

* Add support for `pydeck.Layer` for
  * `Map.add_deck_layers` and 
  * `Map.set_deck_layers`

* Add `sources.SimpleFeatures` for `geopandas.GeoDataFrame` sources 

* Support `geopandas.GeoDataFrame` as source in
  * `Layer` and
  * `Map.add_source`

* Add more parameters to `Map` class for simpler map initialization:
  * `layers`: list
  * `sources`: dict
  * `controls`: list

* Add `position` attribute to `Control` classes

* Add `sources.VectorTileSource` ([Martenz](https://github.com/Martenz))

* Shiny
  * Add `input.{output_id}_view_state` dict containing `{"center", "zoom", "bounds", "pitch", "bearing"}`
  * Rename `input.{output_id}` to `input.{output_id}_clicked`
  * Rename `input.{output_id}_layer_{layer_id}` to `input.{output_id}_feature_clicked` returning `layer_id`

* Ipywidget
  * Add `Map.view_state` dict containing `{"center", "zoom", "bounds", "pitch", "bearing"}` (#89)
  * Remove `Map.center`, `Map.zoom`, `Map.bounds`

## maplibre v0.2.6

* Add function in `maplibre.utils` to save map and display it in the browser
* Add `streamlit.components.v1.iframe` component

## maplibre v0.2.5

* Add custom `LayerSwitcherControl` (#69)
* Add custom `InfoBoxControl` (#74)

## maplibre v0.2.4

* Add `MapboxDraw` plugin (#59)
* Add Shiny input concerned to `MapboxDraw`:
  * `<output_id>.draw_features_selected`
* Add interactive attributes to IpyWidget concerned to `MapboxDraw`:
  * `Map.draw_features_selected` (list)
  * `Map.draw_feature_collection_all` (dict)

## maplibre v0.2.3

* Add interactive attributes to IpyWidget
  * `Map.center`
  * `Map.bounds`
  * `Map.zoom`
  * `Map.lat_lng` > `Map.clicked` (rename)
* Change map option types
  * `MapOptions.zoom: int` > `Union[int, float]`
  * `MapOptions.bearing: int` > `Union[int, float]`
  * `MapOptions.pitch: int` > `Union[int, float]`
* Add conda badges and installation instructions

## maplibre v0.2.2

* Add support for PMTiles (#55)

## maplibre v0.2.1

* Do not add navigation control by default (#31)

## maplibre v0.2.0

* Support Deck.GL layers (#28)

## maplibre v0.1.6

* Add `before_id` parameter to `add_layer` method (#45, #47)
* Add example showing how to insert a layer before labels

## maplibre v0.1.5

* Update deprecated render function to support `shiny>=0.7.0`

## maplibre v0.1.4

* `anywidget>=0.9.0` (#36)

## maplibre v0.1.3

* Display all properties in popup and tooltip if `prop = None` (#26)
* Support [mustache](https://github.com/janl/mustache.js) templates for popups and tooltips (#27)

## maplibre v0.1.2

* Add `Map.set_data`
* Add `Map.set_visibility`
* Do not import `ipywidget.MapWidget` in `__init__` and skip tests for `MapWidget`, because it causes a `core dumped` error, see [anywidget issue](https://github.com/manzt/anywidget/issues/374)
* Remove `requests` dependency
* Remove dead code
* Add more examples

## maplibre v0.1.1

* Initial PyPI release
