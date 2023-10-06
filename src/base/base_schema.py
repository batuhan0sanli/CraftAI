from marshmallow import Schema, fields, validate, validates_schema, ValidationError, EXCLUDE


class BaseSchema(Schema):
    """Base schema if module returns a data."""
    class Meta:
        unknown = EXCLUDE

    var = fields.Str(required=False)
