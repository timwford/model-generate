import Foundation

struct DifferentTestSchema: Codable, Identifiable, Equatable {
	var id = UUID()

	var test: String

	private enum CodingKeys: String, CodingKey {
		case test
	}
}