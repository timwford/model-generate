import Foundation

struct None: Codable, Identifiable, Equatable {
	var id = UUID()

	var time_stamp: Int?
	var keys: Int?
	var unread_notification_count: Int?
	var house_status: Int?
	var flow_graph: Int?
	var pressure_graph_avg: Int?
	var pressure_graph_low: Int?
	var pressure_graph_high: Int?
	var temp_graph_avg: Int?
	var temp_graph_low: Int?
	var temp_graph_high: Int?

	private enum CodingKeys: String, CodingKey {
		case time_stamp, keys, unread_notification_count, house_status, flow_graph, pressure_graph_avg, pressure_graph_low, pressure_graph_high, temp_graph_avg, temp_graph_low, temp_graph_high
	}
}