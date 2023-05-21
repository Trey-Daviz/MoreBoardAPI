from room_handler.python_files.decorators import database_connect
from room_handler.python_files.helper_functions import generate_return
import json


def get_all_room_info_main(params):
    return GetAllRoomInfo(params["room_id"])


@database_connect
def GetAllRoomInfo(db, room_id):
    try:
        sql = "SELECT * FROM room WHERE room_id = %s" % (room_id)
        db.execute(sql)
        room_exists = db.fetchall()
        if room_exists:
            room_exists = json.dumps(room_exists)
            room_exists = room_exists.replace('\"', "\'")
            return generate_return(200, room_exists)
        else:
            raise ValueError("That room does not exist")
    except ValueError as v:
        return generate_return(404, str(v))
    except Exception as e:
        return generate_return(400, str())