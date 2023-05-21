from room_handler.python_files.decorators import database_connect
from room_handler.python_files.helper_functions import generate_return


def remove_room_main(params):
    return RemoveRoom(params["room_id"])


@database_connect
def RemoveRoom(db, room_id):
    try:
        sql = "SELECT room_id FROM room WHERE room_id = %s" % room_id
        db.execute(sql)
        room_exists = db.fetchall()
        if room_exists:
            sql = "UPDATE class SET room_id = null WHERE room_id = %s" % room_id
            db.execute(sql)
            sql = "DELETE FROM room WHERE room_id = %s" % room_id
            db.execute(sql)
            return generate_return(200, "Room has been removed")
        else:
            raise ValueError("That room does not exists")
    except ValueError as v:
        return generate_return(404, str(v))
    except Exception as e:
        return generate_return(400, str(e))
