package io.homemetrics.homemetrics.schemas

import com.beust.klaxon.Klaxon

data class None(
	val time_stamp: Integer?,
	val keys: Integer?,
	val unread_notification_count: Integer?,
	val house_status: Integer?,
	val flow_graph: Integer?,
	val pressure_graph_avg: Integer?,
	val pressure_graph_low: Integer?,
	val pressure_graph_high: Integer?,
	val temp_graph_avg: Integer?,
	val temp_graph_low: Integer?,
	val temp_graph_high: Integer?
)