from src.base.base_schema import BaseSchema
from marshmallow import fields


class ModuleSchema(BaseSchema):
    label = fields.Str(required=False, load_default='')
    placeholder = fields.Str(required=False, load_default='')
