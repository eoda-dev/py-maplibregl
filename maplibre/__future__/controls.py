from __future__ import annotations

from enum import Enum

from ..controls import Control

from pydantic import Field


class GeocoderType(Enum):
    MAPTILTER = "maptiler"
    MAPLIBRE = "maplibre"


class GeocodingControl(Control):
    """MapLibre geocoder control

    Experimental

    Note:
        See [maplibre-gl-geocoder-options](https://maplibre.org/maplibre-gl-geocoder/types/MaplibreGeocoderOptions.html) for details.
    """

    bbox: tuple[float, float, float, float] | None = None
    collapsed: bool | None = False
    countries: str | None = None
    debounce_search: int | None = Field(200, serialization_alias="debounceSearch")
    enable_event_logging: bool | None = Field(False, serialization_alias="enableEventLogging")
    fly_to: bool | dict | None = Field(True, serialization_alias="flyTo")
    language: str | None = None
    limit: int | None = 5
    marker: bool | None = True
    placeholder: str | None = "Search"
    popup: bool | None = False
    proximity: dict | None = None
    reverse_geocode: bool | None = Field(False, serialization_alias="reverseGeocode")
    show_result_markers: bool | None = Field(True, serialization_alias="showResultMarkers")
    show_results_while_typing: bool = Field(True, serialization_alias="showResultsWhileTyping")
    track_proximity: bool = Field(True, serialization_alias="trackProximity")
    zoom: float | None = 16
