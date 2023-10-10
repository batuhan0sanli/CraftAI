from src.base.base_schema import BaseSchema
from marshmallow import fields


class ModuleSchema(BaseSchema):
    label = fields.Str(required=False, load_default='')
    options = fields.List(fields.Str(), required=False, load_default=[])
