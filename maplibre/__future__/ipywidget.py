from __future__ import annotations

from pathlib import Path

from .controls import GeocoderType

from ..ipywidget import MapWidget as BaseWidget

class MapWidget(BaseWidget):
    _geocoder_type = GeocoderType.MAPTILTER

    def _set_css(self, path: str | Path) -> None:
        with open(path, "r") as f:
            self._css = f.read()

    def set_maplibre_geocoder_css(self) -> None:
        # print(Path(__file__).parent.parent)
        self._set_css(Path(__file__).parent.parent / "srcjs" / "ipywidget.maplibre-geocoder.css")

    def add_call(self, method_name: str, *args) -> None:
        if method_name == "addControl" and args[0] == "GeocodingControl":
            self.set_maplibre_geocoder_css()
            self._geocoder_type = GeocoderType.MAPLIBRE

        super().add_call(method_name, *args)
