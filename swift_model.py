import os
from pydantic.fields import ModelField

from typing import List

from model import Model
from pydantic import BaseModel, BaseConfig, conint, confloat, conlist, constr

""" SwiftUI

struct TestSchema: Codable, Identifiable, Equatable {
    var id = UUID()
    
    var string_test: String
    var int_test: Int
    var float_test: Float
    var bool_test: Bool
    var optional_test: String?
    
    private enum CodingKeys: String, CodingKey {
        case string_test, int_test, float_test, bool_test, optional_test
    }
}

"""


class SwiftLanguage(Model):
    def make_file(self, schema: BaseModel, text: str) -> bool:
        model_config: BaseConfig = schema.__config__

        folder_name = 'swiftModels'

        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        f = open(f"{folder_name}/{model_config.title}{self.extension}", "w")
        text = "import Foundation\n\n" + text
        f.write(text)
        f.close()

    def make_fields(self, schema: BaseModel) -> str:
        fields = ["\tvar id = UUID()\n\n"]
        names_text = "\t\tcase"

        field_key: str
        for field_key in schema.__fields__:
            field: ModelField = schema.__fields__[field_key]
            outer_type = field.outer_type_
            name: str = field.name
            field_config = field.model_config.fields[field_key]
            if field_config['python_type']:
                data_type = field_config['python_type']
            else:
                data_type = field.type_
            print(data_type)
            required: bool = field.required

            names_text += f" {name},"

            list_text = ""
            close_list_text = ""
            if outer_type in [List[str], List[int], List[bool], List[float]]:
                list_text = "["
                close_list_text = "]"
            else:
                try:
                    if outer_type._name == "List":
                        list_text = "["
                        close_list_text = "]"
                except AttributeError:
                    pass  # non list object

            if not required:
                required_text = "?"
            else:
                required_text = ""

            if data_type is str:
                data_type_str = self.string_type
            elif data_type is int:
                data_type_str = self.int_type
            elif data_type is float:
                data_type_str = self.float_type
            elif data_type is bool:
                data_type_str = self.bool_type
            else:
                data_type_str = field.type_.__name__

            fields.append(
                f"\t{self.variable_prefix} {name}: {list_text}{data_type_str}{required_text}{close_list_text}\n")

        field_text = ""
        for field in fields:
            field_text += str(field)

        coding_keys_text = f"\n\tprivate enum CodingKeys: String, CodingKey {{\n{names_text[:len(names_text) - 1]}\n\t}}\n"
        field_text += coding_keys_text

        return field_text

    def __init__(self, extension: str, container_type: str, container_args: str, variable_prefix: str, int_type: str,
                 bool_type: str, float_type: str, string_type: str):
        self.extension = extension
        self.container_type = container_type
        self.container_args = container_args
        self.variable_prefix = variable_prefix
        self.int_type = int_type
        self.bool_type = bool_type
        self.float_type = float_type
        self.string_type = string_type

    def make_model(self, schema: BaseModel) -> str:
        model_config: BaseConfig = schema.__config__

        fields_text = self.make_fields(schema)
        model_text = f"{self.container_type} {model_config.title}: {self.container_args} {{\n{fields_text}}}"

        self.make_file(schema, model_text)

        return model_text


swift = SwiftLanguage(".swift", "struct", "Codable, Identifiable, Equatable", "var", "Int", "Bool", "Float",
                      "String")
