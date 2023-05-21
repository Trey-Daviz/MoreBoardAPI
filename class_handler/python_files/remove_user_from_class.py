from class_handler.python_files.decorators import database_connect
from class_handler.python_files.helper_functions import generate_return


def remove_user_from_class_main(params):
    return RemoveUserFromClass(params["class_id"], params["user_id"])


@database_connect
def RemoveUserFromClass(db, class_id, user_id):
    try:
        # Grab student_id from user_id
        sql = "SELECT student_id FROM student WHERE user_id = %s" % user_id
        db.execute(sql)
        student_id = db.fetchall()
        if not student_id:
            raise ValueError("That user is not a student")

        # If user is a student
        else:
            student_id = student_id[0]["student_id"]

            # Make sure class is valid
            sql = "SELECT class_id FROM class WHERE class_id = %s" % class_id
            db.execute(sql)
            if not db.fetchall():
                raise ValueError("That class does not exist")

            # If valid, remove user from that class
            remove_user_from_table = "DELETE FROM student_classes WHERE student_id = %s" % student_id
            db.execute(remove_user_from_table)
            return generate_return(200, "User has been removed from the class")
    except ValueError as v:
        return generate_return(404, str(v))
    except Exception as error:
        return generate_return(400, str(error))
