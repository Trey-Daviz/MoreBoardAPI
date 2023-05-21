import json
from user_handler.python_files.add_user import add_main
from user_handler.python_files.remove_user import remove_main
from user_handler.python_files.get_all_classes_of_user import get_all_classes_of_user_main
from user_handler.python_files.get_all_users import get_all_users_main
from user_handler.python_files.get_user_info import get_user_info_main
from user_handler.python_files.helper_functions import generate_return


def lambda_handler(event, context):
    method = event["httpMethod"]
    match method:
        case "POST":
            action = json.loads(event["body"]).get("action")
            body = json.loads(event["body"]).get("body")
            match action:
                case "add_user":
                    return add_main(body)
                case _:
                    return generate_return(400, "That is not a recognized action for this method")
        case "GET" | "DELETE":
            params = event["queryStringParameters"]
            action = params["action"]
            match action:
                case "remove_user":
                    return remove_main(params)
                case "get_all_classes_of_user":
                    return get_all_classes_of_user_main(params)
                case "get_all_users":
                    return get_all_users_main(params)
                case "get_user_info":
                    return get_user_info_main(params)
                case _:
                    return generate_return(400, "That is not a recognized action for this method")
        case _:
            return generate_return(400, "That is not a recognized method for this endpoint")
