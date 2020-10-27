package io.homemetrics.homemetrics.schemas

import com.beust.klaxon.Klaxon

data class HousePreferencePatch(
	val favorite: Integer?,
	val house_name: String?
)