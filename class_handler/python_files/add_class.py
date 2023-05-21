from class_handler.python_files.decorators import database_connect
from class_handler.modules.marshmallow import ValidationError
from class_handler.python_files.AddClassSchema import AddClassSchema
from class_handler.python_files.helper_functions import generate_return


def add_class_main(body):
    try:
        # Validate against AddUserSchema
        validate = AddClassSchema().load(body)
    except ValidationError as v:
        # For prettier errors, I extracted into a list and appended to it
        errors = []
        for i in v.messages.values():
            errors.append(i[0])
        # This only works for Validation Errors, but it's essentially identical to the next except clause
        return generate_return(400, errors)
    return AddClass(body["teacher_username"], body["class_name"], body["hour"], body["room_id"])


@database_connect
def AddClass(db, teacher_username, class_name, hour, room_id):
    try:
        # Grab user_id from username
        sql = "SELECT user_id FROM user WHERE username = '%s'" % teacher_username
        db.execute(sql)
        user_id = db.fetchall()
        if user_id:
            user_id = user_id[0]
        else:
            raise ValueError("That username is not valid")

        # If valid id
        if user_id:
            # Check to see if that user is in fact a teacher
            sql = "SELECT teacher_id FROM teacher WHERE user_id = %s" % user_id["user_id"]
            db.execute(sql)
            teacher_id = db.fetchall()
            if not teacher_id:
                raise ValueError("That user is not a teacher")

            # If user is a teacher
            else:
                teacher_id = teacher_id[0]["teacher_id"]

                # Make sure teacher is not already teaching at that hour
                sql = "SELECT * FROM class WHERE hour = '%s' AND teacher_id = '%s'" % (hour, teacher_id)
                db.execute(sql)
                if db.fetchall():
                    raise ValueError("That teacher is already teaching a class at that hour!")

                # Make sure the room exists
                sql = "SELECT * FROM room WHERE room_id = %s" % room_id
                db.execute(sql)
                if not db.fetchall():
                    raise ValueError("That room does not exist")

                # Make sure that class doesn't exist in a room at that hour
                sql = "SELECT * FROM class WHERE hour = '%s' and room_id = '%s'" % (hour, room_id)
                db.execute(sql)
                if db.fetchall():
                    raise ValueError("That room already has a class in it at that hour")

                # If they have that hour free
                else:
                    # Add class for that teacher
                    sql = "INSERT INTO class(teacher_id, class_name, hour, room_id) VALUES(%s, '%s', %s, %s)" % (
                        teacher_id, class_name, hour, room_id)
                    db.execute(sql)
                    return generate_return(200, "Class Created")
        else:
            raise ValueError("The username provided for the teacher does not exist")
    except ValueError as error:
        return generate_return(404, str(error))
    except Exception as error:
        return generate_return(400, str(error))
