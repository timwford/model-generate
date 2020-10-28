# model-generate

I use FastAPI/Pydantic models server-side. 
But for mobile, I use Klaxon for JSON parsing and I use Codable Structs in SwiftUI. 
I am tired of copying and/or writing out my models for server and twice for mobile. 
I want them generated!

## Use

#### Given Pydantic Models

```python
from pydantic import BaseModel
from typing import Optional, List
from schemas.schema import DifferentTestSchema

class TestSchema(BaseModel):
    string_test: str
    int_test: int
    float_test: float
    bool_test: bool
    optional_test: Optional[DifferentTestSchema] = None
    test_list: List[str]
    test_list_2: List[DifferentTestSchema]

    class Config:
        title = "TestSchema"
```

model-generate will look for Pydantic models in a package you specify in the `generate.py` file. 
Any Pydantic models in that file will be loaded and converted.

#### Generate Kotlin Data Classes...

Kotlin data classes are generated for use with the Klaxon JSON parser.

```kotlin
package io.packagename.packagename.schemas

data class TestSchema(
        val string_test: String,
        val int_test: Integer,
        val float_test: Float,
        val bool_test: Boolean,
        val optional_test: DifferentTestSchema?,
        val test_list: List<String>,
        val test_list_2: List<DifferentTestSchema>
)
```

#### And SwiftUI Structs!

SwiftUI models are generated to adhere to all the protocols necessary to use the models in a LazyVStack.
Looks as follows.

```swift
import Foundation

struct TestSchema: Codable, Identifiable, Equatable {
	var id = UUID()

	var string_test: String
	var int_test: Int
	var float_test: Float
	var bool_test: Bool
	var optional_test: DifferentTestSchema?
	var test_list: [String]
	var test_list_2: [DifferentTestSchema]

	private enum CodingKeys: String, CodingKey {
		case string_test, int_test, float_test, bool_test, optional_test, test_list, test_list_2
	}
}
```

## Future

I'll probably make this better by adding the following:
* Better testing
* Add Klaxon camel case support
* Setup guide

## Getting Started

Clone the repository.

Setup a virtual environment:
```shell script
python3 -m venv env
source env/bin/activate
```

Install requirements:
```shell script
pip install -r requirements.txt
```

Run the "tests":
```shell script
pytest
```

And look at the contents:
```shell script
cat swiftModels/TestSchema.swift
cat kotlinModels/TestSchema.kt
```

## Adding to your project

Here is one way you can add `model-generate` onto your project.