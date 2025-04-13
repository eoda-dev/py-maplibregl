from maplibre.basemaps import (
    Basemap,
    Carto,
    OpenFreeMap,
    background,
    construct_basemap_style,
    construct_carto_basemap_url,
    construct_openfreemap_basemap_url,
)
from maplibre.layer import Layer, LayerType
from maplibre.sources import RasterSource, RasterTileSource


def test_carto_basemaps() -> None:
    # Act
    basemap_url = construct_carto_basemap_url(Carto.DARK_MATTER)

    # Assert
    assert basemap_url == "https://basemaps.cartocdn.com/gl/dark-matter-gl-style/style.json"


def test_background_style() -> None:
    # Prepare
    color = "white"

    # Act
    style = background(color=color)
    print(style)

    # Assert
    assert style["layers"][0]["paint"]["background-color"] == color


def test_openfreemap_style() -> None:
    positron = OpenFreeMap.POSITRON
    liberty = "liberty"

    style_url = construct_openfreemap_basemap_url(positron)
    print(style_url)

    assert style_url == "https://tiles.openfreemap.org/styles/positron"
    assert construct_openfreemap_basemap_url(liberty) == "https://tiles.openfreemap.org/styles/liberty"


def test_basemap_class() -> None:
    # Act
    basemap = Basemap(
        sources={
            "osm": RasterSource(
                tiles=["https://a.tile.openstreetmap.org/{z}/{x}/{y}.png"],
                tile_size=256,
                attribution="&copy; OpenStreetMap Contributors",
                max_zoom=19,
            )
        },
        layers=[Layer(id="osm-tiles", type=LayerType.RASTER, source="osm")],
    )

    # Assert
    style = basemap.to_dict()
    print(style)

    assert style["version"] == 8
    assert type(style["sources"]) == dict
    assert type(style["layers"]) == list
    assert style["sources"]["osm"]["maxzoom"] == 19
