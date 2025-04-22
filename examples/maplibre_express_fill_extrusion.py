from maplibre import express as mx
from maplibre.config import config
from maplibre.expressions import get_column, interpolate

config.fallback_color = "#ffffff"
config.fill_extrusion_color = "yellow"
config.fill_extrusion_opacity = 0.5
config.cmap = "YlOrRd"

# data = "https://docs.maptiler.com/sdk-js/assets/Mean_age_of_women_at_first_marriage_in_2019.geojson"
data = "https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_50m_urban_areas.geojson"
# data = "https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_110m_admin_1_states_provinces_scale_rank.geojson"
# data = "https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_50m_admin_1_states_provinces.geojson"
# data = "https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_10m_railroads_north_america.geojson"

mx.fill_extrusion(data, fill_extrusion_height=get_column("area_sqkm")).color_category(
    "scalerank"
).to_map(hash=True, pitch=45, center=(7.94, 51.539), zoom=5, fit_bounds=False).save(
    "/tmp/py-maplibre-express.html"
)
