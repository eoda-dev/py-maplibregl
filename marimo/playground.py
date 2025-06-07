import marimo

__generated_with = "0.10.17"
app = marimo.App(width="medium")


@app.cell
def _():
    import maplibre as mlb
    return (mlb,)


@app.cell
def _(mlb):
    m = mlb.MapWidget()
    return (m,)


@app.cell
def _(m):
    m
    return


@app.cell
def _(m, mlb):
    m.add_control(mlb.controls.ScaleControl())
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
