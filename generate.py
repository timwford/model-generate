from pydantic import BaseModel
from schemas import TestSchema

from swift_model import swift
from klaxon_model import klaxon

def generate_swift_models(schema: BaseModel):
    return swift.make_model(schema)

def generate_klaxon_models(schema: BaseModel):
    return klaxon.make_model(schema)


def generate_mobile_models(schema: BaseModel):
    generate_swift_models(schema)
    return True


if __name__ == "__main__":

    # debug(UserBase.__fields__)

    print("\n")
    generate_mobile_models(TestSchema)
    print("\n")
