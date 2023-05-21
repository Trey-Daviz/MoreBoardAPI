from class_handler.python_files.decorators import database_connect
from class_handler.python_files.helper_functions import generate_return
import json


def get_all_chairs_from_class_main(params):
    return GetAllChairsFromClass(params["class_id"])


@database_connect
def GetAllChairsFromClass(db, class_id):
    try:
        sql = "SELECT chair_id, chair_x, chair_y, student_id FROM chair WHERE class_id = %s" % class_id
        db.execute(sql)
        chairs = json.dumps(db.fetchall())
        chairs = chairs.replace('\"', "\'")
        return generate_return(200, chairs)
    except Exception as e:
        return generate_return(400, str(e))
