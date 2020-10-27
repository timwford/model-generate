import Foundation

struct UserPreferencesBase: Codable, Identifiable, Equatable {
	var id = UUID()

	var units: Int?
	var contact_method: Int?
	var emergency_contact: Int?
	var product_updates: Int?

	private enum CodingKeys: String, CodingKey {
		case units, contact_method, emergency_contact, product_updates
	}
}