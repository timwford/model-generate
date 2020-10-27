from pydantic import BaseModel
from schemas import TestSchema
from devtools import debug

from SwiftModel import swift

def generate_swift_models(schema: BaseModel):
    return swift.make_model(schema)

def generate_klaxon_models():
    print("generating klaxon models")


def generate_mobile_models(schema: BaseModel):
    generate_swift_models(schema)
    return True


if __name__ == "__main__":

    # debug(UserBase.__fields__)

    print("\n")
    generate_mobile_models(TestSchema)
    print("\n")
