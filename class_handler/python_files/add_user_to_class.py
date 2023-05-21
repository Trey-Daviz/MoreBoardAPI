from class_handler.python_files.decorators import database_connect
from class_handler.python_files.helper_functions import generate_return


def add_user_to_class_main(body):
    return AddUserToClass(body["class_id"], body["user_id"])


@database_connect
def AddUserToClass(db, class_id, user_id):
    try:
        # Get student_id from user_id
        sql = "SELECT student_id FROM student WHERE user_id = %s" % user_id
        db.execute(sql)
        student_id = db.fetchall()
        if not student_id:
            raise ValueError("That user is not a student")
        # If valid
        else:
            # Check class validity
            sql = "SELECT class_id FROM class WHERE class_id = %s" % class_id
            db.execute(sql)
            if not db.fetchall():
                raise ValueError("That class does not exist")

            # If valid, check to make sure hour isn't occupied by another class
            # Start by getting hour for class provided
            student_id = student_id[0]["student_id"]
            grab_hour_for_class_id = "SELECT hour FROM class WHERE class_id = %s" % class_id
            db.execute(grab_hour_for_class_id)
            hour = db.fetchall()[0]["hour"]

            # Now we grab all classes for that user
            grab_all_classes_for_the_student = "SELECT * FROM student_classes WHERE student_id = %s" % student_id
            db.execute(grab_all_classes_for_the_student)
            classes = db.fetchall()
            has_hour = False

            # For each of those classes, we will check the hour against hour for class provided
            for clas in classes:
                grab_hour_for_class_id = "SELECT hour FROM class WHERE class_id = %s" % clas["class_id"]
                db.execute(grab_hour_for_class_id)
                class_hour = db.fetchall()[0]["hour"]
                if class_hour == hour:
                    has_hour = True

            # If hour occupied
            if has_hour:
                raise ValueError("That student already has a class at that hour!")
            else:
                # Finally run query
                put_student_in_student_classes_table = "INSERT INTO student_classes VALUES(%s, %s)" % (
                    student_id, class_id)
                db.execute(put_student_in_student_classes_table)
                return generate_return(200, "User has been added to class")
    except ValueError as v:
        return generate_return(404, str(v))
    except Exception as error:
        return generate_return(400, str(error))
