import Foundation

struct HousePreference: Codable, Identifiable, Equatable {
	var id = UUID()

	var id: Int?
	var user_id: Int?
	var house_id: Int?
	var favorite: Int?
	var house_name: String?

	private enum CodingKeys: String, CodingKey {
		case id, user_id, house_id, favorite, house_name
	}
}