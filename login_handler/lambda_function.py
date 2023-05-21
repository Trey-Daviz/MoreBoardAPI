import json
from login_handler.decorators import database_connect


def lambda_handler(event, context):
    return login(event["queryStringParameters"]["username"], event["queryStringParameters"]["password"])


@database_connect
def login(db, user_input, password_input):
    # Grab username and password from the request
    try:
        # We want to first check that the user exists, and grab their UID
        sql = "SELECT user_id FROM user WHERE username = '%s'" % user_input
        db.execute(sql)
        uid = db.fetchall()
        if uid:
            uid = uid[0]["user_id"]
        else:
            raise ValueError("That user does not exist")
        # We're going to grab the password from login now
        sql = "SELECT password FROM login WHERE user_id = '%s'" % uid
        db.execute(sql)
        results = db.fetchall()[0]
        # True if the passwords match, otherwise False
        object = ""
        if password_input == results['password']:
            sql = "SELECT * from user WHERE user_id = '%s'" % uid
            db.execute(sql)
            object = db.fetchall()[0]
        else:
            raise Exception("The username/password is incorrect")
        # 200 for successful.  Even if they don't match, the code ran successfully
        return {
            'statusCode': 200,
            'body': json.dumps(object)
        }
    except Exception as e:
        # Generic answer returns a 400
        return {
            'statusCode': 400,
            'body': json.dumps(str(e))
        }