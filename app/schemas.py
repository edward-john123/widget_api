from marshmallow import Schema, fields, validate


class WidgetSchema(Schema):
    id = fields.Int(dump_only=True)  # Read-only for client
    name = fields.Str(required=True, validate=validate.Length(min=1, max=64))
    num_parts = fields.Int(required=True, validate=validate.Range(min=0))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


class WidgetUpdateSchema(Schema):  # For updates, not all fields are required
    name = fields.Str(validate=validate.Length(min=1, max=64))
    num_parts = fields.Int(validate=validate.Range(min=0))
