from user_handler.python_files.decorators import database_connect
from user_handler.python_files.helper_functions import generate_return


def remove_main(params):
    return RemoveUser(params["user_id"])


@database_connect
def RemoveUser(db, user_id):
    # Grab user id from request data
    try:
        # Verifying that the user_id exists
        sql = "SELECT role_id FROM user WHERE user_id = '%s'" % user_id
        db.execute(sql)
        role = db.fetchall()
        if role:
            role = role[0]["role_id"]
            '''
            If the user_id exists, we will first drop it from the login table
            This is because of foreign key constraints.  Before deleting the root primary key, we must remove it from
            Any foreign key positions first
            '''
            sql = "DELETE FROM login WHERE user_id = '%s'" % user_id
            db.execute(sql)
            match role:
                case 0:
                    sql = "SELECT student_id FROM student WHERE user_id = %s" % user_id
                    db.execute(sql)
                    student_id = db.fetchall()[0]["student_id"]
                    sql = "DELETE FROM student_classes WHERE student_id = %s" % student_id
                    db.execute(sql)
                    sql = "DELETE FROM student WHERE user_id = %s" % user_id
                    db.execute(sql)
                case 1:
                    sql = "DELETE FROM parent WHERE user_id = %s" % user_id
                    db.execute(sql)
                case 2:
                    sql = "SELECT teacher_id FROM teacher WHERE user_id = %s" % user_id
                    db.execute(sql)
                    teacher_id = db.fetchall()[0]["teacher_id"]
                    sql = "UPDATE class SET teacher_id = NULL WHERE teacher_id = %s" % teacher_id
                    db.execute(sql)
                    sql = "DELETE FROM teacher WHERE user_id = %s" % user_id
                    db.execute(sql)
                case 3:
                    sql = "DELETE FROM admin WHERE user_id = %s" % user_id
                    db.execute(sql)
            # After that, we delete the user from the user table
            sql = "DELETE FROM user WHERE user_id = '%s'" % user_id
            db.execute(sql)
            # 200 is successful
            return generate_return(200, "User Removed")
        else:
            raise ValueError("That user_id does not exist in the login")
    except ValueError as v:
        # If the user doesn't exist, return 404 for not found
        return generate_return(404, str(v))
    except Exception as e:
        # Generic error returns a 400
        return generate_return(400, str(e))
