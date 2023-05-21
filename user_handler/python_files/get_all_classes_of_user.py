from user_handler.python_files.decorators import database_connect
from user_handler.python_files.helper_functions import generate_return
import json


def get_all_classes_of_user_main(params):
    return GetAllClassesOfUser(params["user_id"])


@database_connect
def GetAllClassesOfUser(db, user_id):
    # Grab user id from request data
    try:
        # Grabbing role of user
        sql = "SELECT role_id FROM user WHERE user_id = %s" % user_id
        db.execute(sql)
        role = db.fetchall()[0]["role_id"]
        match role:
            case 0:
                # Grabbing student id from user id
                sql = "SELECT student_id FROM student WHERE user_id = %s" % user_id
                db.execute(sql)
                student_id = db.fetchall()
                if student_id:
                    sql = "SELECT r.room_id, r.room_name, c.class_id, c.class_name, hour, t.user_id as teach_user_id FROM student_classes sc INNER JOIN class c ON sc.class_id = c.class_id INNER JOIN room r on c.room_id = r.room_id INNER JOIN teacher t ON t.teacher_id = c.teacher_id WHERE student_id = %s" % \
                          student_id[0]["student_id"]
                    db.execute(sql)
                    classes = db.fetchall()
                    if classes:
                        classes = json.dumps(classes)
                        classes = classes.replace('\"', "\'")
                        return generate_return(200, classes)
                    else:
                        raise ValueError("That student has no classes")
            case 2:
                # Grabbing teacher id from user id
                sql = "SELECT teacher_id FROM teacher WHERE user_id = %s" % user_id
                db.execute(sql)
                teacher_id = db.fetchall()
                # If that teacher exists
                if teacher_id:
                    # Grabbing relevant information
                    sql = "SELECT r.room_id, r.room_name, c.class_id, c.class_name, hour FROM class c INNER JOIN room r ON r.room_id = c.room_id WHERE teacher_id = %s ORDER BY hour ASC" % \
                          teacher_id[0]["teacher_id"]
                    db.execute(sql)
                    classes = db.fetchall()
                    # If the teacher has classes
                    if classes:
                        # Convert to string
                        classes = json.dumps(classes)
                        classes = classes.replace('\"', "\'")
                        return generate_return(200, classes)
                    else:
                        raise ValueError("That teacher has no classes")
                else:
                    raise ValueError("That user is not a teacher")
    except ValueError as v:
        # If the user doesn't exist, return 404 for not found
        return generate_return(404, str(v))
    except Exception as e:
        # Generic error returns a 400
        return generate_return(400, str(e))
