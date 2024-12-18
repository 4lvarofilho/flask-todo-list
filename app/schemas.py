from marshmallow import Schema, fields, validate

class TodoSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True, validate=validate.Length(min=1, max=200))
    description = fields.Str(allow_none=True)
    completed = fields.Bool(missing=False)
    created_at = fields.DateTime(dump_only=True)