from marshmallow import Schema, fields

class ClassCreateSchema(Schema):
    name = fields.Str(required=True)

class ClassUpdateSchema(Schema):
    name = fields.Str()

class ClassResponseSchema(Schema):
    id = fields.Int()
    name = fields.Str()
