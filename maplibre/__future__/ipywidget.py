from __future__ import annotations

from enum import Enum
from pathlib import Path

from ..ipywidget import MapWidget as BaseWidget

class GeocoderType(Enum):
    MAPTILTER = "maptiler"
    MAPLIBRE = "maplibre"


class MapWidget(BaseWidget):
    _geocoder = GeocoderType.MAPTILTER

    def _set_css(self, path: str | Path) -> None:
        with open(path, "r") as f:
            self._css = f.read()

    def set_maplibre_geocoder_css(self) -> None:
        # print(Path(__file__).parent.parent)
        self._set_css(Path(__file__).parent.parent / "srcjs" / "ipywidget.maplibre-geocoder.css")

    def add_call(self, method_name: str, *args) -> None:
        if method_name == "addControl" and args[0] == "GeocodingControl":
            self.set_maplibre_geocoder_css()
            self._geocoder = GeocoderType.MAPLIBRE

        super().add_call(method_name, *args)
