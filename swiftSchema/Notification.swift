import Foundation

struct Notification: Codable, Identifiable, Equatable {
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
	var notification_id: Int?
	var recipient: String?
	var time_stamp: Int?
	var viewed: Int?

	private enum CodingKeys: String, CodingKey {
		case user_id, house_id, signal_id, device_type, action, action_payload, priority, scope, free_text, notification_id, recipient, time_stamp, viewed
	}
}