from src.base.base_schema import BaseSchema
from marshmallow import fields


class ModuleSchema(BaseSchema):
    spec = fields.Integer(required=True)
    modules = fields.List(fields.Dict(), required=True)
