from src.base.base_schema import BaseSchema
from marshmallow import fields


class TextInputSchema(BaseSchema):
    label = fields.Str(required=False, load_default='')
    placeholder = fields.Str(required=False, load_default='')
