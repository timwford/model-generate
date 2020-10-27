from pydantic import BaseModel
from typing import Optional

"""
class TestSchema(BaseModel):
    string_test: str
    int_test: int
    float_test: float
    bool_test: bool
    optional_test: Optional[str] = None

    class Config:
        title = "TestSchema"


class DifferentTestSchema(BaseModel):
    test: str

    class Config:
        title = "DifferentTestSchema"
"""

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
        title = "NotificationCreate"
        orm_mode = True


class Notification(NotificationCreate):
    notification_id: Optional[int] = None

    recipient: Optional[str] = None
    time_stamp: Optional[int] = None
    viewed: Optional[int] = None

    class Config:
        title = "Notification"
        orm_mode = True


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
        title = "ClientNotification"
        orm_mode = True


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
        title = "FCMToken"


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
        title = "UserPreferences"
        orm_mode = True


###
### House Preferences
###

class HousePreferenceCreate(BaseModel):
    user_id: Optional[int] = None
    house_id: Optional[int] = None
    favorite: Optional[int] = None
    house_name: Optional[str] = None


class HousePreference(BaseModel):
    id: Optional[int] = None
    user_id: Optional[int] = None
    house_id: Optional[int] = None
    favorite: Optional[int] = None
    house_name: Optional[str] = None

    class Config:
        title = "HousePreference"
        orm_mode = True


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


class HousePatch(HouseBase):
    class Config:
        orm_mode = True


class HouseCreate(HouseBase):
    user_id: int


class House(HouseBase):
    house_id: Optional[int] = None

    class Config:
        orm_mode = True


class HouseWithPreferences(House):
    house_preference_id: Optional[int] = None
    name: Optional[str] = None
    favorite: Optional[int] = None


###
### User
###

class UserBase(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None


class UserCreate(UserBase):
    password: Optional[str] = None


class UserPatch(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    verified: Optional[int] = None
    push_token: Optional[str] = None

    class Config:
        orm_mode = True


class UserPersona(UserPatch):
    user_id: int
    preference_id: Optional[int]
    email: str

    class Config:
        orm_mode = True


class User(UserCreate):
    user_id: int
    access_code: Optional[int] = None
    verified: Optional[int] = None
    push_token: Optional[str] = None

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str = None
    scopes: List[str] = []


class VerificationCode(BaseModel):
    access_code: int


class UserConnectionBase(BaseModel):
    admin: int


class UserConnectionCreate(UserConnectionBase):
    email: str


class UserConnectionId(BaseModel):
    house_id: int
    user_id: str


class UserConnection(UserConnectionId):
    accepted: int

    class Config:
        orm_mode = True


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


class HouseOwnerUser(HouseOwner):
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None

    class Config:
        orm_mode = True


class HouseOwnersPatch(BaseModel):
    admin: Optional[int] = None
    accepted: Optional[int] = None

    class Config:
        orm_mode = True

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


###
### Sensors
###


class SensorPatch(BaseModel):
    sensor_name: Optional[str] = None
    fw_version: Optional[str] = None
    sensor_type: Optional[int] = None
    last_seen: Optional[int] = None


class SensorCreate(BaseModel):
    sensor_type: Optional[int] = None
    last_seen: Optional[int] = None
    fw_version: Optional[str] = None
    sensor_name: Optional[str] = None


class Sensor(SensorCreate):
    house_id: Optional[int] = None
    serial: Optional[int] = None

    class Config:
        orm_mode = True


#
# Journey
#

class JourneyCreate(BaseModel):
    user_id: Optional[int] = None
    phone_type: Optional[int] = None
    property_type: Optional[str] = None


class Journey(JourneyCreate):
    journey_id: Optional[int] = None

    class Config:
        orm_mode = True


class JourneyPatch(BaseModel):
    phone_type: Optional[int] = None
    property_type: Optional[str] = None

    class Config:
        orm_mode = True


#
# Installations
#

class InstallationCreate(BaseModel):
    user_id: Optional[int] = None
    house_id: Optional[int] = None
    order_created: Optional[int] = None
    beta: Optional[bool] = None


class Installation(InstallationCreate):
    id: Optional[int] = None
    order_ready: Optional[int] = None
    order_installed: Optional[int] = None

    module_count: Optional[int] = None
    detect_count: Optional[int] = None
    electric_count: Optional[int] = None

    class Config:
        orm_mode = True


class InstallationPatch(BaseModel):
    order_ready: Optional[int] = None
    order_installed: Optional[int] = None

    module_count: Optional[int] = None
    detect_count: Optional[int] = None
    electric_count: Optional[int] = None

    class Config:
        orm_mode = True


class HouseModel(House):
    house_preferences: Optional[HousePreference] = None
    sensors: Optional[List[Sensor]] = None
    ownership: Optional[HouseOwner] = None


class UserModel(UserPersona):
    user_preferences: Optional[UserPreferences] = None


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

class ControlMessage(BaseModel):
    msg: Optional[str] = None


#
# House Status
#


class FlowGraph(BaseModel):
    weights: List[float]

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

class FormattedUpdate(BaseModel):
    key: str
    message: str


class HouseStatus(BaseModel):
    unread_notification_count: Optional[int] = None
    house_status: int
    house_id: int
    keys: Optional[List[HouseUpdateKey]]

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
