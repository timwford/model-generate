import Foundation

struct TestSchema: Codable, Identifiable, Equatable {
	var id = UUID()

	var string_test: String
	var int_test: Int
	var float_test: Float
	var bool_test: Bool

	private enum CodingKeys: String, CodingKey {
		case string_test, int_test, float_test, bool_test, optional_test, optional_test_list
	}
}