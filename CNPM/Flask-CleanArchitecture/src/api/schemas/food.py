from marshmallow import Schema, fields

class FoodRequestSchema(Schema):
    id = fields.Int(required=True)

class FoodCreateSchema(Schema):
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    gian_hang_id = fields.Int(required=True)

class FoodUpdateSchema(Schema):
    name = fields.Str(required=True)
    price = fields.Float(required=True)

class FoodResponseSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    gian_hang_id = fields.Int(required=True)