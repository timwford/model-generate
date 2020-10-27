from typing import List, Optional
from pydantic import BaseModel

"""
Pydantic models for database
"""


###
### Notifications
###

class NotificationCreate(BaseModel):
    user_id: Optional[int] = None
    house_id: Optional[int] = None

    signal_id: Optional[int] = None
    device_type: Optional[int] = None

    action: Optional[int] = None
    action_payload: Optional[str] = None
    priority: Optional[int] = None
    scope: Optional[int] = None
    free_text: Optional[str] = None

    class Config:
        orm_mode = True
        title = "NotificationCreate"

class Notification(NotificationCreate):
    notification_id: Optional[int] = None

    recipient: Optional[str] = None
    time_stamp: Optional[int] = None
    viewed: Optional[int] = None

    class Config:
        orm_mode = True
        title = "Notification"


class NotificationGroup(BaseModel):
    notifications: List[Notification]

    class Config:
        title = "NotificationGroup"
        

class ClientNotification(BaseModel):
    notification_id: Optional[int] = None

    image_code: Optional[int] = None
    header: Optional[str] = None
    body: Optional[str] = None
    time_stamp: Optional[int] = None
    action_payload: Optional[str] = None
    action: Optional[int] = None
    viewed: Optional[int] = None
    free_text: Optional[str] = None

    class Config:
        orm_mode = True
        title = "ClientNotification"


class ClientNotificationGroup(BaseModel):
    notifications: List[ClientNotification]
    class Config:
        title = "ClientNotificationGroup"


class FCMToken(BaseModel):
    token: str
    class Config:
        title = "FCMToken"


class NotificationPatch(BaseModel):
    viewed: Optional[int] = None
    action_payload: Optional[str] = None
    action: Optional[int] = None
    free_text: Optional[str] = None
    class Config:
        title = "NotificationPatch"


###
### Features
###

class HouseUpdate(BaseModel):
    house_id: Optional[int] = None
    house_name: Optional[str] = None
    unread_notifications: Optional[int] = None
    water_usage: Optional[int] = None
    electric_usage: Optional[int] = None
    water_temp: Optional[int] = None
    water_pressure: Optional[int] = None
    water_pressure_hourly_dip: Optional[int] = None
    water_usage_goal: Optional[int] = None
    electric_usage_goal: Optional[int] = None
    favorite: Optional[int] = None
    house_preference_id: Optional[int] = None
    last_seen: Optional[int] = None
    class Config:
        title = "HouseUpdate"


class AllHouseUpdate(BaseModel):
    all_house_water_usage: Optional[int] = None
    all_house_electric_usage: Optional[int] = None
    all_house_water_usage_goal: Optional[int] = None
    all_house_electric_usage_goal: Optional[int] = None
    units: Optional[int] = None
    unread_notif_count: Optional[int] = None
    time_stamp: Optional[int] = None
    houses: Optional[List[HouseUpdate]]
    class Config:
        title = "AllHouseUpdate"


class FeatureValue(BaseModel):
    value: Optional[int] = None
    class Config:
        title = "FeatureValue"


###
### Preferences
###

class Pref(BaseModel):
    preference: int
    class Config:
        title = "Pref"


class EmergencyContact(BaseModel):
    contact: int
    class Config:
        title = "EmergencyContact"


class ContactMethod(BaseModel):
    contact: int
    class Config:
        title = "ContactMethod"


class UserPreferencesBase(BaseModel):
    units: Optional[int] = None
    contact_method: Optional[int] = None
    emergency_contact: Optional[int] = None
    product_updates: Optional[int] = None
    class Config:
        title = "UserPreferencesBase"


class UserPreferences(UserPreferencesBase):
    preference_id: int

    class Config:
        orm_mode = True
        title = "UserPreferences"


###
### House Preferences
###

class HousePreferenceCreate(BaseModel):
    user_id: Optional[int] = None
    house_id: Optional[int] = None
    favorite: Optional[int] = None
    house_name: Optional[str] = None
    class Config:
        title = "HousePreferenceCreate"


class HousePreference(BaseModel):
    id: Optional[int] = None
    user_id: Optional[int] = None
    house_id: Optional[int] = None
    favorite: Optional[int] = None
    house_name: Optional[str] = None

    class Config:
        orm_mode = True
        title = "HousePreference"


class HousePreferencePatch(BaseModel):
    favorite: Optional[int] = None
    house_name: Optional[str] = None
    class Config:
        title = "HousePreferencePatch"


###
### Houses
###

class HouseBase(BaseModel):
    square_feet: Optional[int] = None
    resident_count: Optional[int] = None
    bath_count: Optional[int] = None
    bed_count: Optional[int] = None
    year: Optional[int] = None
    address1: Optional[str] = None
    address2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zipcode: Optional[int] = None
    water_usage_goal: Optional[int] = None
    electric_usage_goal: Optional[int] = None
    eco: Optional[bool] = None

    class Config:
        orm_mode = True
        title = "HouseBase"


class HousePatch(HouseBase):
    class Config:
        orm_mode = True
        title = "HousePatch"


class HouseCreate(HouseBase):
    user_id: int
    class Config:
        title = "HouseCreate"


class House(HouseBase):
    house_id: Optional[int] = None

    class Config:
        orm_mode = True
        title = "House"


class HouseWithPreferences(House):
    house_preference_id: Optional[int] = None
    name: Optional[str] = None
    favorite: Optional[int] = None
    class Config:
        title = "HouseWithPreferences"


###
### User
###

class UserBase(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    class Config:
        title = "UserBase"


class UserCreate(UserBase):
    password: Optional[str] = None

    class Config:
        title = "UserCreate"

class UserPatch(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    verified: Optional[int] = None
    push_token: Optional[str] = None

    class Config:
        orm_mode = True
        title = "UserPatch"


class UserPersona(UserPatch):
    user_id: int
    preference_id: Optional[int]
    email: str

    class Config:
        orm_mode = True
        title = "UserPersona"

class User(UserCreate):
    user_id: int
    access_code: Optional[int] = None
    verified: Optional[int] = None
    push_token: Optional[str] = None

    class Config:
        orm_mode = True
        title = "User"


class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        title = "Token"

class TokenData(BaseModel):
    email: str = None
    scopes: List[str] = []

    class Config:
        title = "TokenData"

class VerificationCode(BaseModel):
    access_code: int

    class Config:
        title = "VerificationCode"

class UserConnectionBase(BaseModel):
    admin: int

    class Config:
        title = "UserConnectionBase"

class UserConnectionCreate(UserConnectionBase):
    email: str

    class Config:
        title = "UserConnectionCreate"

class UserConnectionId(BaseModel):
    house_id: int
    user_id: str

    class Config:
        title = "UserConnectionId"

class UserConnection(UserConnectionId):
    accepted: int

    class Config:
        orm_mode = True
        title = "UserConnection"

###
### HouseOwnership
###

class HouseOwner(BaseModel):
    id: Optional[int] = None
    house_id: Optional[int] = None
    user_id: Optional[int] = None
    admin: Optional[int] = None
    accepted: Optional[int] = None
    time_stamp: Optional[int] = None

    class Config:
        orm_mode = True
        title = "HouseOwner"

class HouseOwnerUser(HouseOwner):
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None

    class Config:
        orm_mode = True
        title = "HouseOwnerUser"

class HouseOwnersPatch(BaseModel):
    admin: Optional[int] = None
    accepted: Optional[int] = None

    class Config:
        orm_mode = True
        title = "HouseOwnersPatch"
###
### House Modes
###

class HouseMode(BaseModel):
    id: Optional[int] = None
    house_id: Optional[int] = None
    away_mode: Optional[int] = None
    protected_mode: Optional[int] = None

    class Config:
        orm_mode = True
        title = "HouseMode"


###
### Sensors
###


class SensorPatch(BaseModel):
    sensor_name: Optional[str] = None
    fw_version: Optional[str] = None
    sensor_type: Optional[int] = None
    last_seen: Optional[int] = None
    class Config:
        title = "SensorPatch"


class SensorCreate(BaseModel):
    sensor_type: Optional[int] = None
    last_seen: Optional[int] = None
    fw_version: Optional[str] = None
    sensor_name: Optional[str] = None
    class Config:
        title = "SensorCreate"


class Sensor(SensorCreate):
    house_id: Optional[int] = None
    serial: Optional[int] = None

    class Config:
        orm_mode = True
        title = "Sensor"


#
# Journey
# 

class JourneyCreate(BaseModel):
    user_id: Optional[int] = None
    phone_type: Optional[int] = None
    property_type: Optional[str] = None

    class Config:
        title = "JourneyCreate"

class Journey(JourneyCreate):
    journey_id: Optional[int] = None

    class Config:
        orm_mode = True
        title = "Journey"


class JourneyPatch(BaseModel):
    phone_type: Optional[int] = None
    property_type: Optional[str] = None

    class Config:
        orm_mode = True
        title = "JourneyPatch"


#
# Installations
#

class InstallationCreate(BaseModel):
    user_id: Optional[int] = None
    house_id: Optional[int] = None
    order_created: Optional[int] = None
    beta: Optional[bool] = None
    class Config:
        title = "InstallationCreate"


class Installation(InstallationCreate):
    id: Optional[int] = None
    order_ready: Optional[int] = None
    order_installed: Optional[int] = None

    module_count: Optional[int] = None
    detect_count: Optional[int] = None
    electric_count: Optional[int] = None

    class Config:
        orm_mode = True
        title = "Installation"


class InstallationPatch(BaseModel):
    order_ready: Optional[int] = None
    order_installed: Optional[int] = None

    module_count: Optional[int] = None
    detect_count: Optional[int] = None
    electric_count: Optional[int] = None

    class Config:
        orm_mode = True
        title = "InstallationPatch"


class HouseModel(House):
    house_preferences: Optional[HousePreference] = None
    sensors: Optional[List[Sensor]] = None
    ownership: Optional[HouseOwner] = None
    class Config:
        title = "HouseModel"


class UserModel(UserPersona):
    user_preferences: Optional[UserPreferences] = None

    class Config:
        title = "UserModel"

#
# Control Valve
#

class ControlStatus(BaseModel):
    id: Optional[int] = None
    value: Optional[int] = None
    serial: Optional[int] = None
    time_stamp: Optional[int] = None

    class Config:
        orm_mode = True
        title = "ControlStatus"

class ControlMessage(BaseModel):
    msg: Optional[str] = None
    class Config:
        title = "ControlMessage"


#
# House Status
#


class FlowGraph(BaseModel):
    weights: List[float]
    class Config:
        title = "FlowGraph"

class HouseUpdateKey(BaseModel):
    key: str
    serial: int
    update_type: str
    update: str
    severity: Optional[int]
    time_stamp: int
    payload: int
    should_ack: Optional[int]
    ack: Optional[int] = None
    actor: Optional[int] = None
    class Config:
        title = "HouseUpdateKey"

class FormattedUpdate(BaseModel):
    key: str
    message: str
    class Config:
        title = "FormattedUpdate"


class HouseStatus(BaseModel):
    unread_notification_count: Optional[int] = None
    house_status: int
    house_id: int
    keys: Optional[List[HouseUpdateKey]]
    class Config:
        title = "HouseStatus"

class Update(BaseModel):
    time_stamp: Optional[int]
    keys: Optional[List[HouseUpdateKey]]
    unread_notification_count: Optional[int]
    house_status: Optional[int]
    flow_graph: Optional[FlowGraph]
    pressure_graph_avg: Optional[FlowGraph]
    pressure_graph_low: Optional[FlowGraph]
    pressure_graph_high: Optional[FlowGraph]
    temp_graph_avg: Optional[FlowGraph]
    temp_graph_low: Optional[FlowGraph]
    temp_graph_high: Optional[FlowGraph]
    class Config:
        title = "Update"
