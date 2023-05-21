import json
from seating_handler.python_files.helper_functions import generate_return
from seating_handler.python_files.add_chair_to_seating_arrangement import add_chair_to_seating_arrangement_main
from seating_handler.python_files.remove_chair_from_seating_arrangement import remove_chairs_from_seating_arrangement_main
from seating_handler.python_files.get_student_from_chair import get_student_from_chair_main


def lambda_handler(event, context):
    method = event["httpMethod"]
    match method:
        case "POST" | "PUT":
            action = json.loads(event["body"]).get("action")
            body = json.loads(event["body"]).get("body")
            match action:
                case "add_chair_to_seating_arrangement":
                    return add_chair_to_seating_arrangement_main(body)
                case _:
                    return generate_return(400, "That is not a recognized action for this method")
        case "GET" | "DELETE":
            params = event["queryStringParameters"]
            action = params["action"]
            match action:
                case "remove_chairs_from_seating_arrangement":
                    return remove_chairs_from_seating_arrangement_main(params)
                case "get_student_from_chair":
                    return get_student_from_chair_main(params)
                case _:
                    return generate_return(400, "That is not a recognized action for this method")
        case _:
            return generate_return(400, "That is not a recognized method for this endpoint")
