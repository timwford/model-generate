package io.homemetrics.homemetrics.schemas

import com.beust.klaxon.Klaxon

data class UserPreferences(
	val units: Integer?,
	val contact_method: Integer?,
	val emergency_contact: Integer?,
	val product_updates: Integer?,
	val preference_id: Integer
)