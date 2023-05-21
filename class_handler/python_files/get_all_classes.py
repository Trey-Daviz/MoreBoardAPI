from class_handler.python_files.decorators import database_connect
from class_handler.python_files.helper_functions import generate_return
import json


def get_all_classes_main():
    return GetAllClasses()


@database_connect
def GetAllClasses(db):
    try:
        sql = "SELECT c.*, r.room_name, t.user_id as teach_user_id FROM class c LEFT JOIN room r ON c.room_id = r.room_id INNER JOIN teacher t ON t.teacher_id = c.teacher_id"
        db.execute(sql)
        classes = json.dumps(db.fetchall())
        classes = classes.replace('\"', "\'")
        return generate_return(200, classes)
    except Exception as e:
        return generate_return(400, str(e))
