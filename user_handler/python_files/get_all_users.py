from user_handler.python_files.decorators import database_connect
from user_handler.python_files.helper_functions import generate_return
import json


def get_all_users_main(params):
    return GetAllUsers(params.get('role_id'))


@database_connect
def GetAllUsers(db, role_id):
    try:
        if role_id is not None:
            role_id = int(role_id)
            match role_id:
                case 0:
                    sql = "SELECT * FROM user u LEFT JOIN student s ON u.user_id = s.user_id WHERE role_id = %s" % role_id
                case 2:
                    sql = "SELECT * FROM user u LEFT JOIN teacher t ON u.user_id = t.user_id WHERE role_id = %s" % role_id
                case 3:
                    sql = "SELECT * FROM user u LEFT JOIN admin a ON u.user_id = a.user_id WHERE role_id = %s" % role_id
                case -1:
                    sql = "SELECT * FROM user"
                case _:
                    raise ValueError("That is not a valid role_id")
        else:
            raise ValueError("The variable role_id must be provided.  If you would like to get all users, provide a role_id of -1")
        db.execute(sql)
        result = json.dumps(db.fetchall())
        result = result.replace('\"', "\'")
        return generate_return(200, result)
    except Exception as e:
        return generate_return(400, str(e))
