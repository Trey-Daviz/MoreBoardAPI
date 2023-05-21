from room_handler.python_files.decorators import database_connect
from room_handler.python_files.helper_functions import generate_return
from room_handler.python_files.AddRoomSchema import AddRoomSchema
from room_handler.modules.marshmallow import ValidationError


def add_room_main(body):
    try:
        # Validate against AddUserSchema
        validate = AddRoomSchema().load(body)
    except ValidationError as v:
        # For prettier errors, I extracted into a list and appended to it
        errors = []
        for i in v.messages.values():
            errors.append(i[0])
        return generate_return(400, errors)
    return AddRoom(body["room_name"], body["room_length"], body["room_width"])


@database_connect
def AddRoom(db, room_name, room_length, room_width):
    try:
        sql = "INSERT INTO room(room_name, room_length, room_width) VALUES('%s', %s, %s)" % (
            room_name, room_length, room_width)
        db.execute(sql)
        # 200 for successful.  Even if they don't match, the code ran successfully
        return generate_return(200, "The room has been added")
    except Exception as e:
        # Generic answer returns a 400
        return generate_return(400, str(e))
