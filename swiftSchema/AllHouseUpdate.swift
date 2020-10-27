import Foundation

struct AllHouseUpdate: Codable, Identifiable, Equatable {
	var id = UUID()

	var all_house_water_usage: Int?
	var all_house_electric_usage: Int?
	var all_house_water_usage_goal: Int?
	var all_house_electric_usage_goal: Int?
	var units: Int?
	var unread_notif_count: Int?
	var time_stamp: Int?
	var houses: Int?

	private enum CodingKeys: String, CodingKey {
		case all_house_water_usage, all_house_electric_usage, all_house_water_usage_goal, all_house_electric_usage_goal, units, unread_notif_count, time_stamp, houses
	}
}