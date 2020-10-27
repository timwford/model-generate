package io.homemetrics.homemetrics.schemas

import com.beust.klaxon.Klaxon

data class HouseUpdate(
	val house_id: Integer?,
	val house_name: String?,
	val unread_notifications: Integer?,
	val water_usage: Integer?,
	val electric_usage: Integer?,
	val water_temp: Integer?,
	val water_pressure: Integer?,
	val water_pressure_hourly_dip: Integer?,
	val water_usage_goal: Integer?,
	val electric_usage_goal: Integer?,
	val favorite: Integer?,
	val house_preference_id: Integer?,
	val last_seen: Integer?
)