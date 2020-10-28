from pydantic import BaseModel

import schemas.test_schema

from swift_model import swift
from klaxon_model import klaxon

def generate_swift_models(schema: BaseModel):
    return swift.make_model(schema)

def generate_klaxon_models(schema: BaseModel):
    return klaxon.make_model(schema)


def generate_mobile_models():

    for aModule in vars(schemas.test_schema).values():
        print(aModule)
        if aModule is not None:
            try:
                generate_klaxon_models(aModule)
                generate_swift_models(aModule)
            except AttributeError:
                print("Not a pydantic model")

    return True


if __name__ == "__main__":
    generate_mobile_models()
