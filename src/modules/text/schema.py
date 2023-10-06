from src.base.base_schema import BaseSchema
from marshmallow import fields


class ModuleSchema(BaseSchema):
    text = fields.Str(required=True)
