import Foundation

struct ClientNotification: Codable, Identifiable, Equatable {
	var id = UUID()

	var notification_id: Int?
	var image_code: Int?
	var header: String?
	var body: String?
	var time_stamp: Int?
	var action_payload: String?
	var action: Int?
	var viewed: Int?
	var free_text: String?

	private enum CodingKeys: String, CodingKey {
		case notification_id, image_code, header, body, time_stamp, action_payload, action, viewed, free_text
	}
}