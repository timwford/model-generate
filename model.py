from abc import ABC, abstractmethod
from pydantic import BaseModel

""" SwiftUI

struct UserModelSchema: Codable, Identifiable, Equatable {
    var id = UUID()
    
    var first_name: String
    var last_name: String
    var phone: String
    var email: String
    
    private enum CodingKeys: String, CodingKey {
        case first_name, last_name, phone, email
    }
}

"""

""" Klaxon

data class UserModel(val first_name: String, val last_name: String, val phone: String, val email: Int)

"""

class Model(ABC):
    @abstractmethod
    def __init__(self, extension: str,
                 container_type: str,
                 container_args: str,
                 variable_prefix: str,
                 int_type: str,
                 bool_type: str,
                 float_type: str,
                 string_type: str
                 ):
        self.extension = extension
        self.container_type = container_type
        self.container_args = container_args
        self.variable_prefix = variable_prefix
        self.int_type = int_type
        self.bool_type = bool_type
        self.float_type = float_type
        self.string_type = string_type

    @abstractmethod
    def make_model(self, schema: BaseModel):
        pass

    @abstractmethod
    def make_fields(self, schema: BaseModel) -> str:
        pass

    @abstractmethod
    def make_file(self, schema: BaseModel) -> bool:
        pass
