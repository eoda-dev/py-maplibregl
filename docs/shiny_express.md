In Shiny Express the `output_id` corresponds to the name of the _render_ function.
For the example below the `output_id` is `mapgl`, so that you have to listen to `input.mapgl_clicked` to get the map clicked event.

```python
-8<-- "getting_started/shiny_express.py"
```
