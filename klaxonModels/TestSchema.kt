package io.package.package.schemas

data class TestSchema(
	val string_test: String,
	val int_test: Integer,
	val float_test: Float,
	val bool_test: Boolean,
	val optional_test: DifferentTestSchema?,
	val test_list: List<String>,
	val test_list_2: List<DifferentTestSchema>
)