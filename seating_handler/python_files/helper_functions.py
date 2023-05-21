import json


def generate_return(status_code, body):
    body = json.dumps({
            "error" if status_code != 200 else "message": body
        })
    return {
        "statusCode": status_code,
        "body": body
    }
