package io.homemetrics.homemetrics.schemas

import com.beust.klaxon.Klaxon

data class Notification(
	val user_id: Integer?,
	val house_id: Integer?,
	val signal_id: Integer?,
	val device_type: Integer?,
	val action: Integer?,
	val action_payload: String?,
	val priority: Integer?,
	val scope: Integer?,
	val free_text: String?,
	val notification_id: Integer?,
	val recipient: String?,
	val time_stamp: Integer?,
	val viewed: Integer?
)