#!/bin/sh
version=${1:-5.3.0}
echo $version
target_dir=maplibre/srcjs
echo $target_dir
curl https://unpkg.com/maplibre-gl@${version}/dist/maplibre-gl.js -o ${target_dir}/maplibre-gl.js
curl https://unpkg.com/maplibre-gl@${version}/dist/maplibre-gl.css -o ${target_dir}/maplibre-gl.css
