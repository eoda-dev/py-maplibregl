In Shiny Express the `output_id` corresponds to the name of the _render_ function.
For the example below your `output_id` equals `mapgl`. Therefore, you have to listen to `input.mapgl_clicked` to get the map clicked event `input.{output_id}.clicked`.

```python
-8<-- "getting_started/shiny_express.py"
```
