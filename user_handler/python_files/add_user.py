from user_handler.python_files.decorators import database_connect
from user_handler.python_files.AddUserSchema import AddUserSchema
from user_handler.modules.marshmallow import ValidationError
from user_handler.python_files.helper_functions import generate_return


def add_main(body):
    username = generate_username(body["firstname"], body["lastname"])
    return AddUser(username, body["firstname"], body["lastname"], body["user_password"], body["email"], body["role_id"],
                   body["grade"])


@database_connect
def generate_username(db, firstname, lastname):
    # We are going to grab all usernames in user table
    sql = "SELECT username FROM user"
    ids = []
    db.execute(sql)
    usernames = db.fetchall()
    # Now we'll loop through them and grab the 6 digits after their initials
    for i in usernames:
        ids.append(int(i["username"][2::]))
    # Now we'll generate a username for the new user based off of their initials, and the next sequential 6 digit number
    if not ids:
        username = firstname[0] + lastname[0] + "600000"
    else:
        username = lastname[0] + firstname[0] + str(max(ids) + 1)
    return username


@database_connect
def AddUser(db, username, firstname, lastname, password, email, role_id, grade):
    info = {
        "firstname": firstname,
        "lastname": lastname,
        "user_password": password,
        "email": email,
        "role": role_id,
        "grade": grade
    }
    try:
        # Validate against AddUserSchema
        validate = AddUserSchema().load(info)
    except ValidationError as v:
        # For prettier errors, I extracted into a list and appended to it
        errors = []
        for i in v.messages.values():
            errors.append(i[0])
        # This only works for Validation Errors, but it's essentially identical to the next except clause
        return generate_return(400, errors)
    # Populate values sent in the request
    grade = None if role_id != 0 else grade
    try:
        # Insert all relevant data into the user table
        sql = "INSERT INTO user(username, first_name, last_name, email, role_id) VALUES('%s', '%s', '%s', " \
              "'%s', '%s') as message" % (username, firstname, lastname, email, role_id)
        db.execute(sql)
        # Grab the new user_id that was generated
        sql = "SELECT user_id FROM user WHERE username = '%s'" % username
        db.execute(sql)
        uid = db.fetchall()[0]["user_id"]
        # Now populate the login table with the id and password attached
        sql = "INSERT INTO login VALUES('%s', '%s')" % (uid, password)
        db.execute(sql)

        match role_id:
            case 0:
                sql = "INSERT INTO student(user_id, grade) VALUES(%s, %s)" % (uid, grade)
                db.execute(sql)
            case 1:
                sql = "INSERT INTO guardian(user_id) VALUES (%s)" % uid
                db.execute(sql)
            case 2:
                sql = "INSERT INTO teacher(user_id) VALUES (%s)" % uid
                db.execute(sql)
            case 3:
                sql = "INSERT INTO admin(user_id) VALUES (%s)" % uid
                db.execute(sql)
        # 200 is a successful error code
        return generate_return(200, "User Added")
    except Exception as e:
        # 400 is unsuccessful
        return generate_return(400, str(e))
