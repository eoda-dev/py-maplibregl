from maplibre import Layer, LayerType, Map
from maplibre.__future__.datasets import DataSets
from maplibre.controls import NavigationControl

# data = DataSets.urban_areas.read_data()
data = DataSets.vancouver_blocks.read_data()
# print(type(data.total_bounds))
# layer = Layer(type=LayerType.LINE, source=data, paint={"line-color": "yellow"})
layer = Layer(type=LayerType.LINE, source=data).set_paint_props(line_color="steelblue")
# print(layer)

m = Map(layers=[layer], controls=[NavigationControl()])
m.fit_bounds(data=data, animate=False)
m.save("/tmp/py-maplibre-express.html")
