import os
from pydantic.fields import ModelField

from model import Model
from pydantic import BaseModel, BaseConfig

from environment_variables import package_name

""" Klaxon

data class TestSchema(
    val string_test: String,
    val int_test: Integer, 
    val float_test: Float, 
    val bool_test: Boolean, 
    val optional_test: String?
)

"""


class KlaxonModel(Model):
    def make_file(self, schema: BaseModel, text: str) -> bool:
        folder_name = 'klaxonModels'

        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        model_config: BaseConfig = schema.__config__

        f = open(f"{folder_name}/{model_config.title}{self.extension}", "w")
        text = f"{package_name}\n\n" + text
        f.write(text)
        f.close()

    def make_fields(self, schema: BaseModel) -> str:
        fields = []

        field_key: str
        for field_key in schema.__fields__:
            field: ModelField = schema.__fields__[field_key]
            name: str = field.name
            data_type: type = field.type_
            required: bool = field.required

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

            fields.append(f"\t{self.variable_prefix} {name}: {data_type_str}{required_text},")

        field_text = ""
        for i in range(0, len(fields)):
            field = fields[i]

            if i != len(fields)-1:
                field_text += str(field + "\n")
            else:
                field_str = str(field)
                field_text += field_str[:len(field_str)-1]

        field_text += "\n"

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
        model_text = f"{self.container_type} {model_config.title}(\n{fields_text})"

        self.make_file(schema, model_text)

        return model_text


klaxon = KlaxonModel(".kt", "data class", "", "val", "Integer", "Boolean", "Float",
                      "String")
