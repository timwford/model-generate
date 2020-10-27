import Foundation

struct FeatureValue: Codable, Identifiable, Equatable {
	var id = UUID()

	var value: Int?

	private enum CodingKeys: String, CodingKey {
		case value
	}
}