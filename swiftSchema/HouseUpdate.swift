import Foundation

struct HouseUpdate: Codable, Identifiable, Equatable {
	var id = UUID()

	var house_id: Int?
	var house_name: String?
	var unread_notifications: Int?
	var water_usage: Int?
	var electric_usage: Int?
	var water_temp: Int?
	var water_pressure: Int?
	var water_pressure_hourly_dip: Int?
	var water_usage_goal: Int?
	var electric_usage_goal: Int?
	var favorite: Int?
	var house_preference_id: Int?
	var last_seen: Int?

	private enum CodingKeys: String, CodingKey {
		case house_id, house_name, unread_notifications, water_usage, electric_usage, water_temp, water_pressure, water_pressure_hourly_dip, water_usage_goal, electric_usage_goal, favorite, house_preference_id, last_seen
	}
}