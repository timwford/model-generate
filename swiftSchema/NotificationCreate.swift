import Foundation

struct NotificationCreate: Codable, Identifiable, Equatable {
	var id = UUID()

	var user_id: Int?
	var house_id: Int?
	var signal_id: Int?
	var device_type: Int?
	var action: Int?
	var action_payload: String?
	var priority: Int?
	var scope: Int?
	var free_text: String?

	private enum CodingKeys: String, CodingKey {
		case user_id, house_id, signal_id, device_type, action, action_payload, priority, scope, free_text
	}
}