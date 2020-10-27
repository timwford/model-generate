import Foundation

struct None: Codable, Identifiable, Equatable {
	var id = UUID()


	private enum CodingKeys: String, CodingKey {
		cas
	}
}