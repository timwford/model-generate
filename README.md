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
from schemas.test_schema import DifferentTestSchema

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

model-generate will look for Pydantic models in a `schemas/schemas.py`. 
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

You can experience the basic functionality by cloning the repository, loading the requirements, and running the "tests".
This will generate two test schema. From there, you can put your own Pydantic models in and get them auto generated.
Pydantic models are required to have a `title` in their Config.

