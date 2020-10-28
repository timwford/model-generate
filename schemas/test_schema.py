from pydantic import BaseModel
from typing import Optional, List

class DifferentTestSchema(BaseModel):
    test: str

    class Config:
        title = "DifferentTestSchema"

class TestSchema(BaseModel):
    string_test: str
    int_test: int
    float_test: float
    bool_test: bool
    optional_test: Optional[DifferentTestSchema] = None
    test_list: List[str]

    class Config:
        title = "TestSchema"
