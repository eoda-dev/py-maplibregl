from maplibre.shiny import output_maplibregl

def test_output_maplibregl():
    # Prepare
    output_id = "map"
    
    # Act
    output = output_maplibregl(output_id)
    print(output)
    deps = output.get_dependencies()
    print(deps)
    print(deps[0].name)

    # Assert
    assert len(deps[0].script) == 1
    assert deps[0].name == "maplibre-bindings"
