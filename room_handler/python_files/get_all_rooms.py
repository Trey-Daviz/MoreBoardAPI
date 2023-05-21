from room_handler.python_files.decorators import database_connect
from room_handler.python_files.helper_functions import generate_return
import json


def get_all_rooms_main():
    return GetAllRooms()


@database_connect
def GetAllRooms(db):
    try:
        sql = "SELECT * FROM room"
        db.execute(sql)
        rooms = json.dumps(db.fetchall())
        rooms = rooms.replace('\"', "\'")
        return generate_return(200, rooms)
    except Exception as e:
        return generate_return(400, str(e))
