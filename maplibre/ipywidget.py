from __future__ import annotations

import logging
from os.path import join
from pathlib import Path

logging.basicConfig()
logger = logging.getLogger(__name__)


try:
    import traitlets
    from anywidget import AnyWidget
except ImportError as e:
    # traitlets = None
    # AnyWidget = None
    logger.error(e)
    logger.error("Please install 'maplibre[anywidget]' if you want to use maplibre in 'marimo' or 'jupyter' notebooks.")

from maplibre.map import Map, MapOptions


class MapWidget(AnyWidget, Map):
    """MapWidget

    Use this class to display and update maps in Marimo or Jupyter Notebooks.

    See `maplibre.Map` for available methods.

    Examples:
        >>> from maplibre import MapOptions
        >>> from maplibre.ipywidget import MapWidget as Map
        >>> m = Map(MapOptions(center=(-123.13, 49.254), zoom=11, pitch=45))
        >>> m # doctest: +SKIP
    """

    _esm = join(Path(__file__).parent, "srcjs", "ipywidget.js")
    _css = join(Path(__file__).parent, "srcjs", "ipywidget.css")
    _use_message_queue = True
    _rendered = traitlets.Bool(False).tag(config=True).tag(sync=True)
    map_options = traitlets.Dict().tag(sync=True)
    calls = traitlets.List().tag(sync=True)
    height = traitlets.Union([traitlets.Int(), traitlets.Unicode()]).tag(sync=True)

    # Interactions Map
    clicked = traitlets.Dict().tag(sync=True)
    view_state = traitlets.Dict().tag(sync=True)

    # Interactions MapboxDraw plugin
    draw_features_selected = traitlets.List().tag(sync=True)
    draw_feature_collection_all = traitlets.Dict().tag(sync=True)
    draw_features_created = traitlets.List().tag(sync=True)
    draw_features_updated = traitlets.List().tag(sync=True)
    draw_features_deleted = traitlets.List().tag(sync=True)

    def __init__(
        self,
        map_options: MapOptions = MapOptions(),
        sources: dict | None = None,
        layers: list | None = None,
        controls: list | None = None,
        height: int | str = 400,
        **kwargs,
    ) -> None:
        self._rendered = False
        self.calls = []
        AnyWidget.__init__(self, height=height, **kwargs)
        Map.__init__(self, map_options, sources, layers, controls, **kwargs)

    @traitlets.validate("height")
    def _validate_height(self, proposal):
        height = proposal["value"]
        if isinstance(height, int):
            return f"{height}px"

        return height

    @traitlets.observe("_rendered")
    def _on_rendered(self, change):
        self.send({"calls": self._message_queue, "msg": "init"})
        self._message_queue = []

    def use_message_queue(self, value: bool = True) -> None:
        self._use_message_queue = value

    def add_call(self, method_name: str, *args) -> None:
        call = [method_name, args]
        if not self._rendered:
            if not self._use_message_queue:
                self.calls = self.calls + [call]
                return

            self._message_queue.append(call)
            return

        self.send({"calls": [call], "msg": "custom call"})
