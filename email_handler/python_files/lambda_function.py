import json
from email_handler.python_files.helper_functions import generate_return
from email_handler.python_files.send_email import send_email_main


def lambda_handler(event, context):
    method = event["httpMethod"]
    match method:
        case "POST" | "PUT":
            action = json.loads(event["body"]).get("action")
            body = json.loads(event["body"]).get("body")
            match action:
                case "send_email":
                    return send_email_main(body)
                case _:
                    return generate_return(400, "That is not a recognized action for this method")
        case "GET" | "DELETE":
            params = event["queryStringParameters"]
            action = params["action"]
            match action:
                case _:
                    return generate_return(400, "That is not a recognized action for this method")
        case _:
            return generate_return(400, "That is not a recognized method for this endpoint")