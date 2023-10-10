from marshmallow import Schema, fields, EXCLUDE


class SubBaseSchema(Schema):
    """Sub base schema for nested data."""

    class Meta:
        unknown = EXCLUDE


class BaseSchema(Schema):
    """Base schema if module returns a data."""

    class Meta:
        unknown = EXCLUDE

    var = fields.Str(required=False)
