#!/bin/sh
branch=${1:-dev}
echo $branch
target_dir=maplibre/srcjs
echo $target_dir
# curl https://raw.githubusercontent.com/eoda-dev/maplibre-bindings/${branch}/py-bindings/pymaplibre.js -o $target_dir/pywidget.js
# curl https://raw.githubusercontent.com/eoda-dev/maplibre-bindings/${branch}/py-bindings/pymaplibre.css -o $target_dir/pywidget.css
curl https://raw.githubusercontent.com/eoda-dev/maplibre-bindings/${branch}/py-bindings/pymaplibre.ipywidget.js -o $target_dir/ipywidget.js
curl https://raw.githubusercontent.com/eoda-dev/maplibre-bindings/${branch}/py-bindings/pymaplibre.ipywidget.css -o $target_dir/ipywidget.css
