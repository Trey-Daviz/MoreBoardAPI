from class_handler.modules.marshmallow import Schema, fields
from class_handler.modules.marshmallow.validate import Range, Regexp


class AddClassSchema(Schema):
    teacher_username = fields.Str(required=True)
    class_name = fields.Str(required=True, validate=Regexp(regex="[A-Za-z\s]{5,40}", error="The class name is invalid.  It must have a name between 5 and 40 letters"))
    hour = fields.Int(required=True, validate=Range(min=1, max=7, error="The hour must be a number between 1 and 7"))
    room_id = fields.Int(required=True)

