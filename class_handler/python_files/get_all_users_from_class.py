from class_handler.python_files.decorators import database_connect
from class_handler.python_files.helper_functions import generate_return
import json


def get_all_users_from_class(params):
    return GetAllUsersFromClass(params["class_id"])


@database_connect
def GetAllUsersFromClass(db, class_id):
    try:
        # Just checking to see if a class exists
        sql = "SELECT * FROM class WHERE class_id = %s" % class_id
        db.execute(sql)
        # If class exists
        if db.fetchall():
            # Grabbing student ids in that class
            sql = "SELECT student_id FROM student_classes WHERE class_id = '%s'" % class_id
            db.execute(sql)
            student_ids = db.fetchall()
            # If it returns students
            if student_ids:
                user_ids = []
                # One by one grab their user ids
                for student in student_ids:
                    sql = "SELECT user_id FROM student WHERE student_id = %s" % student["student_id"]
                    db.execute(sql)
                    user_ids.append(db.fetchall()[0]["user_id"])
                users = []
                # One by one grab personal information
                for user in user_ids:
                    sql = "SELECT u.user_id, s.student_id, u.first_name, u.last_name FROM user u LEFT JOIN student s ON u.user_id = s.user_id WHERE u.user_id = %s" % user
                    db.execute(sql)
                    users.append(db.fetchall()[0])
                # Sort by last name
                users = sorted(users, key=lambda d: d["last_name"])
                users = json.dumps(users)
                users = users.replace('\"', "\'")
                return generate_return(200, users)
            else:
                raise ValueError("That class is empty")
        else:
            raise ValueError("That class does not exist")
    except ValueError as v:
        return generate_return(404, str(v))
    except Exception as error:
        return generate_return(400, str(error))
