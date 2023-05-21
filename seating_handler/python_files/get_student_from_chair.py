from seating_handler.python_files.decorators import database_connect
from seating_handler.python_files.helper_functions import generate_return


def get_student_from_chair_main(params):
    return GetStudentFromChair(params["chair_id"])


@database_connect
def GetStudentFromChair(db, chair_id):
    try:
        sql = "SELECT chair_id FROM chair WHERE chair_id = %s" % chair_id
        db.execute(sql)
        chair_exists = db.fetchall()
        if not chair_exists:
            raise ValueError("That chair does not exist")

        sql = "SELECT student_id FROM chair WHERE chair_id = %s" % chair_id
        db.execute(sql)
        student_id = db.fetchall()[0]["student_id"]

        sql = "SELECT user_id FROM student WHERE student_id = %s" % student_id
        db.execute(sql)
        user_id = db.fetchall()
        if user_id:
            user_id = user_id[0]["user_id"]
            sql = "SELECT * FROM user WHERE user_id = %s" % user_id
            db.execute(sql)
            user_data = db.fetchall()[0]
            return generate_return(200, user_data)
        else:
            raise ValueError("That student id is not assigned to a user")
    except ValueError as v:
        return generate_return(404, str(v))
    except Exception as e:
        return generate_return(400, str(e))
