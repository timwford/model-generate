package io.homemetrics.homemetrics.schemas

import com.beust.klaxon.Klaxon

data class AllHouseUpdate(
	val all_house_water_usage: Integer?,
	val all_house_electric_usage: Integer?,
	val all_house_water_usage_goal: Integer?,
	val all_house_electric_usage_goal: Integer?,
	val units: Integer?,
	val unread_notif_count: Integer?,
	val time_stamp: Integer?,
	val houses: Integer?
)