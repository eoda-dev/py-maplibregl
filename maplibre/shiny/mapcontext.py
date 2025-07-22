from __future__ import annotations

from typing_extensions import Self

try:
    from shiny.session import Session, require_active_session
except ImportError as e:
    print(e)

from ..map import Map


class MapContext(Map):
    """Map context

    Use this class to update a `Map` instance in a Shiny app.
    See `maplibre.Map` for available methods.

    Note:
        Must be used inside an async function.

    Args:
        id (string): The id of the map to be updated.
        session (Session): A Shiny session.
            If `None`, the active session is used.
    """

    def __init__(self, id: str, session: Session = None) -> None:
        self._session = require_active_session(session)
        self.id = id if self._session.ns == "" else f"{self._session.ns}-{id}"
        self.map_options = dict()
        self._message_queue = list()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.render()

    async def render(self) -> None:
        await self._session.send_custom_message(
            f"pymaplibregl-{self.id}",
            dict(id=self.id, calls=self._message_queue),
        )
