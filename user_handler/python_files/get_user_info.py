from user_handler.python_files.decorators import database_connect
from user_handler.python_files.helper_functions import generate_return
import json


def get_user_info_main(params):
    return GetUserInfo(params["user_id"])


@database_connect
def GetUserInfo(db, user_id):
    try:
        sql = "SELECT * from user WHERE user_id = %s" % user_id
        db.execute(sql)
        result = db.fetchall()
        if result is None:
            raise ValueError("That user does not exist")
        else:
            result = json.dumps(result)
            result = result.replace('\"', "\'")
            return generate_return(200, result)
    except ValueError as v:
        # If the user doesn't exist, return 404 for not found
        return generate_return(404, str(v))
    except Exception as e:
        return generate_return(400, str(e))
