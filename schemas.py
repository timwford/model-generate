from pydantic import BaseModel
from typing import Optional

class TestSchema(BaseModel):
    string_test: str
    int_test: int
    float_test: float
    bool_test: bool
    optional_test: Optional[str] = None

    class Config:
        title = "TestSchema"
