from schemas import TestSchema
from generate import generate_mobile_models, generate_swift_models, generate_klaxon_models

test_schema_swift = "There's a better way to test this"

def test_anything():
    assert 2 == 2

def test_load_schema():
    assert generate_mobile_models(TestSchema) is True

def test_generate_swift_model():
    swift_model = generate_swift_models(TestSchema)

    print("\n")
    print(swift_model)

def test_generate_klaxon_model():
    model = generate_klaxon_models(TestSchema)

    print("\n")
    print(model)