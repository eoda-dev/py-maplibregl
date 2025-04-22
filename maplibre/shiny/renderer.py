from htmltools import Tag
from shiny.render.renderer import Jsonifiable, Renderer

from ..map import Map
from .ui import output_maplibregl


class render_maplibregl(Renderer[Map]):
    """A decorator for a function that returns a `Map` object"""

    def auto_output_ui(self) -> Tag:
        return output_maplibregl(self.output_id, height=600)

    async def transform(self, value: Map) -> Jsonifiable:
        return dict(mapData=value.to_dict())
