package io.homemetrics.homemetrics.schemas

import com.beust.klaxon.Klaxon

data class ClientNotification(
	val notification_id: Integer?,
	val image_code: Integer?,
	val header: String?,
	val body: String?,
	val time_stamp: Integer?,
	val action_payload: String?,
	val action: Integer?,
	val viewed: Integer?,
	val free_text: String?
)