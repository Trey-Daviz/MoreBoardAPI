from class_handler.python_files.decorators import database_connect
from class_handler.python_files.helper_functions import generate_return


def remove_class_main(params):
    return RemoveClass(params["class_id"])


@database_connect
def RemoveClass(db, class_id):
    try:
        # See if the class exists
        sql = "SELECT * FROM class WHERE class_id = '%s'" % class_id
        db.execute(sql)

        # If class exists
        if db.fetchall():
            # Delete class from student classes
            sql = "DELETE FROM student_classes WHERE class_id = '%s'" % class_id
            db.execute(sql)

            # Delete class from class table
            sql = "DELETE FROM class WHERE class_id = '%s'" % class_id
            db.execute(sql)
            return generate_return(200, "Class has been removed")
        else:
            raise ValueError("That class does not exist")
    except ValueError as v:
        return generate_return(404, str(v))
    except Exception as error:
        return generate_return(400, str(error))
