import json
from class_handler.python_files.add_class import add_class_main
from class_handler.python_files.remove_class import remove_class_main
from class_handler.python_files.add_user_to_class import add_user_to_class_main
from class_handler.python_files.remove_user_from_class import remove_user_from_class_main
from class_handler.python_files.get_all_users_from_class import get_all_users_from_class
from class_handler.python_files.get_all_chairs_from_class import get_all_chairs_from_class_main
from class_handler.python_files.get_all_classes import get_all_classes_main
from class_handler.python_files.assign_teacher_to_class import assign_teacher_to_class_main
from class_handler.python_files.helper_functions import generate_return


def lambda_handler(event, context):
    method = event["httpMethod"]
    match method:
        case "POST" | "PUT":
            action = json.loads(event["body"]).get("action")
            body = json.loads(event["body"]).get("body")
            match action:
                case "add_class":
                    return add_class_main(body)
                case "add_user_to_class":
                    return add_user_to_class_main(body)
                case "assign_teacher_to_class":
                    return assign_teacher_to_class_main(body)
                case _:
                    return generate_return(400, "That is not a recognized action for this method")
        case "GET" | "DELETE":
            params = event["queryStringParameters"]
            action = params["action"]
            match action:
                case "remove_class":
                    return remove_class_main(params)
                case "remove_user_from_class":
                    return remove_user_from_class_main(params)
                case "get_all_users_from_class":
                    return get_all_users_from_class(params)
                case "get_all_chairs_from_class":
                    return get_all_chairs_from_class_main(params)
                case "get_all_classes":
                    return get_all_classes_main()
                case _:
                    return generate_return(400, "That is not a recognized action for this method")
        case _:
            return generate_return(400, "That is not a recognized method for this endpoint")
