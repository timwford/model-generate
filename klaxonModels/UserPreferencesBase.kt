package io.homemetrics.homemetrics.schemas

import com.beust.klaxon.Klaxon

data class UserPreferencesBase(
	val units: Integer?,
	val contact_method: Integer?,
	val emergency_contact: Integer?,
	val product_updates: Integer?
)