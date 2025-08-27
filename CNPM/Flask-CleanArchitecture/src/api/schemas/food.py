from marshmallow import Schema, fields

class FoodRequestSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str(required=False)
    category = fields.Str(required=True)

class FoodResponseSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    price = fields.Float(required=True)
    category = fields.Str(required=True)
    updated_at = fields.Raw(required=True)