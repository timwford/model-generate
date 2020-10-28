# model-generate

I use FastAPI/Pydantic models for my server. But for mobile, I also use Klaxon for model parsing and I use Codable Structs in SwiftUI. 
I am tired of copying and/or writing out my models for server and twice for mobile. 
I want them generated!

## Use

#### Given Pydantic Models

```python
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
```

model-generate will look for Pydantic models in a `schemas/schemas.py`. 
Any Pydantic models in that directory will be loaded and converted to...

#### Kotlin Data Classes

Kotlin data classes are generated for use with the Klaxon JSON parser.

```kotlin
package io.packagename.packagename.schemas

data class TestSchema(
	val string_test: String,
	val int_test: Integer,
	val float_test: Float,
	val bool_test: Boolean,
	val optional_test: String?
)
```

#### SwiftUI Structs

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
	var optional_test: String?

	private enum CodingKeys: String, CodingKey {
		case string_test, int_test, float_test, bool_test, optional_test
	}
}
```

##