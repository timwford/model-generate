import Foundation

struct HousePreferencePatch: Codable, Identifiable, Equatable {
	var id = UUID()

	var favorite: Int?
	var house_name: String?

	private enum CodingKeys: String, CodingKey {
		case favorite, house_name
	}
}