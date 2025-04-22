""" Markers and controls

Note:
    See also [markers-and-controls](https://docs.mapbox.com/mapbox-gl-js/api/markers/).
"""

from __future__ import annotations

from enum import Enum
from typing import Literal, Optional, Union

from pydantic import Field, field_validator

from ._core import MapLibreBaseModel
from .config import config


class PopupOptions(MapLibreBaseModel):
    """Popup options"""

    anchor: str | None = None
    close_button: bool | None = Field(False, serialization_alias="closeButton")
    close_on_click: bool | None = Field(None, serialization_alias="closeOnClick")
    close_on_move: bool | None = Field(None, serialization_alias="closeOnMove")
    max_width: int | None = Field(None, serialization_alias="maxWidth")
    offset: int | list | dict | None = None


class Popup(MapLibreBaseModel):
    """Popup

    Attributes:
        text (str): The Text of the popup.
        options (PopupOptions | dict): Popup options.
    """

    text: str
    options: Union[PopupOptions, dict] = dict()


class MarkerOptions(MapLibreBaseModel):
    """Marker options"""

    anchor: str | None = None
    color: str | None = None
    draggable: bool | None = None
    offset: tuple | list | None = None
    pitch_alignment: str | None = Field(None, serialization_alias="pitchAlignment")
    rotation: int | None = None
    rotation_alignment: str | None = Field(None, serialization_alias="rotationAlignment")
    scale: int | None = None


class Marker(MapLibreBaseModel):
    """Marker

    Attributes:
        lng_lat (tuple | list): **Required.** The longitude and latitude of the marker.
        popup (Popup | dict): The Popup that is displayed when a user clicks on the marker.
        options (MarkerOptions | dict): Marker options.
    """

    lng_lat: Union[tuple, list] = Field(None, serialization_alias="lngLat")
    popup: Union[Popup, dict] = None
    options: Union[MarkerOptions, dict] = dict()


# TODO: Add missing control types
class ControlType(Enum):
    NAVIGATION = "NavigationControl"
    SCALE = "ScaleControl"
    FULLSCREEN = "FullscreenControl"
    GEOLOCATE = "GeolocateControl"
    ATTRIBUTION = "AttributionControl"


class ControlPosition(Enum):
    """Control position

    Attributes:
        TOP_LEFT: top-left
        TOP_RIGHT: top-right
        BOTTOM_LEFT: bottom-left
        BOTTOM_RIGHT: bottom-right
    """

    TOP_LEFT = "top-left"
    TOP_RIGHT = "top-right"
    BOTTOM_LEFT = "bottom-left"
    BOTTOM_RIGHT = "bottom-right"


class Control(MapLibreBaseModel):
    position: Union[ControlPosition, str] = Field(ControlPosition.TOP_RIGHT, exclude=True)

    @property
    def type(self):
        return self.__class__.__name__


class AttributionControl(Control):
    """Attribution control"""

    # _name: str = ControlType.ATTRIBUTION.value
    compact: bool = None
    custom_attribution: Union[str, list] = Field(None, serialization_alias="customAttribution")


class FullscreenControl(Control):
    """Fullscreen control

    Examples:
        >>> from maplibre import Map
        >>> from maplibre.controls import FullscreenControl, ControlPosition

        >>> m = Map()
        >>> m.add_control(FullscreenControl(), ControlPosition.BOTTOM_LEFT)
    """

    # _name: str = ControlType.FULLSCREEN.value
    pass


class GeolocateControl(Control):
    """Geolocate control"""

    # _name: str = ControlType.GEOLOCATE.value
    position_options: dict = Field(None, serialization_alias="positionOptions")
    show_accuracy_circle: bool = Field(True, serialization_alias="showAccuracyCircle")
    show_user_heading: bool = Field(False, serialization_alias="showUserHeading")
    show_user_location: bool = Field(True, serialization_alias="showUserLocation")
    track_user_location: bool = Field(False, serialization_alias="trackUserLocation")


class NavigationControl(Control):
    """Navigation control"""

    # _name: str = ControlType.NAVIGATION.value
    show_compass: bool = Field(True, serialization_alias="showCompass")
    show_zoom: bool = Field(True, serialization_alias="showZoom")
    visualize_pitch: bool = Field(False, serialization_alias="visualizePitch")


class ScaleUnit(Enum):
    IMPERIAL = "imperial"
    METRIC = "metric"
    NAUTICAL = "nautical"


class ScaleControl(Control):
    """Scale control"""

    max_width: int = Field(None, serialization_alias="maxWidth")
    unit: Literal["imperial", "metric", "nautical"] = "metric"


class GlobeControl(Control):
    """Globe control"""

    ...


class TerrainControl(Control):
    """Terrain control"""

    source: str
    exaggeration: int | float | None = 1


# -------------------------
# Plugins
# -------------------------
# https://docs.maptiler.com/sdk-js/modules/geocoding/api/api-reference/
class MapTilerGeocodingControl(Control):
    """MapTiler geocoding control

    Note:
        See [maptiler-geocoding-api-reference](https://docs.maptiler.com/sdk-js/modules/geocoding/api/api-reference/) for details.
    """

    api_key: str = Field(config.maptiler_api_key, serialization_alias="apiKey", validate_default=True, min_length=1)
    api_url: str | None = Field(None, serialization_alias="apiUrl")
    bbox: tuple[float, float, float, float] | None = None
    clear_button_title: str | None = Field("clear", serialization_alias="clearButtonTitle")
    clear_list_on_pick: bool | None = Field(False, serialization_alias="clearListOnPick")
    clear_on_blur: bool | None = Field(False, serialization_alias="clearOnBlur")
    collapsed: bool | None = False
    country: str | None = None
    debounce_search: int | None = Field(200, serialization_alias="debounceSearch")
    enable_reverse: Literal["always", "button", "never"] | None = Field("never", serialization_alias="enableReverse")
    error_message: str | None = None
    fly_to: bool | dict | None = Field(True, serialization_alias="flyTo")
    fly_to_selected: bool | None = Field(False, serialization_alias="flyToSelected")
    icons_base_url: str | None = Field(None, serialization_alias="iconsBaseUrl")
    keep_list_open: bool | None = Field(None, serialization_alias="keepListOpen")
    fuzzy_match: bool | None = Field(True, serialization_alias="fuzzyMatch")
    language: str | None = None
    limit: int | None = 5
    marker: bool | None = True
    marker_on_selected: bool | None = Field(True, serialization_alias="markerOnSelected")
    min_length: int | None = Field(2, serialization_alias="minLength")
    no_results_message: str | None = Field(None, serialization_alias="noResultsMessage")
    placeholder: str | None = "Search"
    proximity: list | None = None
    reverse_active: bool | None = Field(False, serialization_alias="reverseActive")
    reverseButtonTitle: str | None = Field(None, serialization_alias="reverseButtonTitle")
    select_first: bool | None = Field(True, serialization_alias="selectFirst")
    show_place_type: Literal["never", "always", "if-needed"] | None = Field(
        "if-needed", serialization_alias="showPlaceType"
    )
    show_results_while_typing: bool = Field(True, serialization_alias="showResultsWhileTyping")
    zoom: float | None = None


# -------------------------
# Custom controls
# -------------------------
class LayerSwitcherControl(Control):
    """Layer switcher control

    Attributes:
        layer_ids (list): A list of layer ids to be shown in the layer switcher control.
        theme (Literal["default", "simple"]): The theme of the layer switcher control.
        css_text (str): Optional inline style declaration of the control.
    """

    layer_ids: list = Field([], serialization_alias="layerIds")
    theme: Literal["default", "simple"] = "default"
    css_text: str = Field(None, serialization_alias="cssText")


class InfoBoxControl(Control):
    """InfoBox control

    Attributes:
        content (str): Content (HTML or plain text) to be displayed in the info box.
        css_text (str): Optional inline style declaration of the control.
    """

    content: str
    css_text: str = Field(None, serialization_alias="cssText")
