import importlib.metadata
import logging

__version__ = importlib.metadata.version(__package__)

logging.basicConfig()
logger = logging.getLogger(__name__)

WARNING_MESSAGE = """Please install 'maplibre[shiny]' if you want to use maplibre with the 'shiny' framework.
    The import of 'shiny' bindings from the root level will be deactivated in a future version.
    Until then, set log level to 'ERROR' to suppress this warning.
"""

from .config import options
from .controls import ControlPosition, ControlType
from .layer import Layer, LayerType
from .map import Map, MapOptions

try:
    from .mapcontext import MapContext
    from .renderer import MapLibreRenderer
    from .ui import output_maplibregl

    render_maplibregl = MapLibreRenderer
except ImportError as e:
    logger.warning(e)
    logger.warning(WARNING_MESSAGE)
