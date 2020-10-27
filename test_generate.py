from generate import generate_mobile_models

test_schema_swift = "There's a better way to test this"

def test_anything():
    assert 2 == 2

def test_load_schema():
    assert generate_mobile_models() is True
