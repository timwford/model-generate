import Foundation

struct FCMToken: Codable, Identifiable, Equatable {
	var id = UUID()

	var viewed: Int?
	var action_payload: String?
	var action: Int?
	var free_text: String?

	private enum CodingKeys: String, CodingKey {
		case viewed, action_payload, action, free_text
	}
}