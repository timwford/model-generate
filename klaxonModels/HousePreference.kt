package io.homemetrics.homemetrics.schemas

import com.beust.klaxon.Klaxon

data class HousePreference(
	val id: Integer?,
	val user_id: Integer?,
	val house_id: Integer?,
	val favorite: Integer?,
	val house_name: String?
)