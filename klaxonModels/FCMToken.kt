package io.homemetrics.homemetrics.schemas

import com.beust.klaxon.Klaxon

data class FCMToken(
	val viewed: Integer?,
	val action_payload: String?,
	val action: Integer?,
	val free_text: String?
)