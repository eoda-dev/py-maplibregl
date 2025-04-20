from __future__ import annotations

from pathlib import Path

from ..ipywidget import MapWidget as BaseWidget


class MapWidget(BaseWidget):
    def _set_css(self, path: str | Path) -> None:
        with open(path, "r") as f:
            self._css = f.read()

    def set_maplibre_geocoder_css(self) -> None:
        # print(Path(__file__).parent.parent)
        self._set_css(Path(__file__).parent.parent / "srcjs" / "ipywidget.maplibre-geocoder.css")
