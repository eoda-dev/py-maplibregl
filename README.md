# MapLibre for Python

[![Release](https://img.shields.io/github/v/release/eoda-dev/py-maplibregl)](https://img.shields.io/github/v/release/eoda-dev/py-maplibregl)
[![pypi](https://img.shields.io/pypi/v/maplibre.svg)](https://pypi.python.org/pypi/maplibre)
[![Conda recipe](https://img.shields.io/badge/recipe-maplibre-green.svg)](https://github.com/conda-forge/maplibre-feedstock)
[![Conda package](https://img.shields.io/conda/vn/conda-forge/maplibre.svg)](https://anaconda.org/conda-forge/maplibre)
[![Build status](https://img.shields.io/github/actions/workflow/status/eoda-dev/py-maplibregl/pytest.yml?branch=main)](https://img.shields.io/github/actions/workflow/status/eoda-dev/py-maplibregl/pytest.yml?branch=main)
[![License](https://img.shields.io/github/license/eoda-dev/py-maplibregl)](https://img.shields.io/github/license/eoda-dev/py-maplibregl)
[![MapLibre](https://img.shields.io/badge/MapLibre.GL-v3.6.2-blue.svg)](https://github.com/maplibre/maplibre-gl-js/releases/tag/v3.6.2)

MapLibre for Python provides Python bindings for [MapLibre GL JS](https://github.com/maplibre/maplibre-gl-js).
Furthermore, [Deck.GL Layers](https://deck.gl/docs/api-reference/layers) can be mixed with [MapLibre Layers](https://maplibre.org/maplibre-style-spec/layers/).

It integrates seamlessly into [Shiny for Python](https://github.com/posit-dev/py-shiny) and [Jupyter](https://jupyter.org/).

## Installation

```bash
# Stable
pip install maplibre

pip install "maplibre[all]"

# Dev
pip install git+https://github.com/eoda-dev/py-maplibregl@dev

pip install "maplibre[all] @ git+https://github.com/eoda-dev/py-maplibregl@dev"

# Conda
conda install -c conda-forge maplibre
```

## Quickstart

```python
from maplibre import Map, MapOptions

m = Map(MapOptions(center=(-123.1256, 49.24658), zoom=9))
m.save(preview=True)
```

## Documentation

* [Basic usage](https://eoda-dev.github.io/py-maplibregl/)
* [API Documentation](https://eoda-dev.github.io/py-maplibregl/api/map/)
* [Examples](https://eoda-dev.github.io/py-maplibregl/examples/every_person_in_manhattan/)

## Development

### Python

```bash
poetry install

poetry run pytest

poetry run pytest --ignore=maplibre/ipywidget.py --doctest-modules maplibre
```

### JavaScript

See [maplibre-bindings](https://github.com/eoda-dev/maplibre-bindings)
