from class_handler.python_files.decorators import database_connect
from class_handler.python_files.helper_functions import generate_return


def assign_teacher_to_class_main(body):
    return AssignTeacherToClass(body["class_id"], body["teacher_id"])


@database_connect
def AssignTeacherToClass(db, class_id, teacher_id):
    try:
        sql = "UPDATE class SET teacher_id = %s WHERE class_id = %s" % (teacher_id, class_id)
        db.execute(sql)
        return generate_return(200, "Teacher has been assigned to that class")
    except Exception as e:
        return generate_return(400, str(e))
