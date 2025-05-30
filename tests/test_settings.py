import os

from maplibre.config import config


def test_maptiler_api_key():
    # Prepare
    os.environ["MAPTILER_API_KEY"] = "test"

    # Act
    maptiler_api_key = config.maptiler_api_key

    # Assert
    assert maptiler_api_key == "test"
