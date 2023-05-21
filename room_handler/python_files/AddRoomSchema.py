from room_handler.modules.marshmallow import Schema, fields
from room_handler.modules.marshmallow.validate import Range, Regexp


class AddRoomSchema(Schema):
    room_name = fields.Str(required=True, validate=Regexp(regex="[A-Z]{1,2}\d{3}", error="Room name is not valid.  It must be 1 or 2 letters followed by 3 digits"))
    room_length = fields.Int(required=True, validate=Range(min=1, max=20, error="The length can not be 0, the max length is 20"))
    room_width = fields.Int(required=True, validate=Range(min=1, error="The width can not be 0"))