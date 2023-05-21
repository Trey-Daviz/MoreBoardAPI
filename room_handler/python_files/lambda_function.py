import json
from room_handler.python_files.helper_functions import generate_return
from room_handler.python_files.add_room import add_room_main
from room_handler.python_files.remove_room import remove_room_main
from room_handler.python_files.get_all_room_info import get_all_room_info_main
from room_handler.python_files.get_all_rooms import get_all_rooms_main


def lambda_handler(event, context):
    method = event["httpMethod"]
    match method:
        case "POST" | "PUT":
            action = json.loads(event["body"]).get("action")
            body = json.loads(event["body"]).get("body")
            match action:
                case "add_room":
                    return add_room_main(body)
                case _:
                    return generate_return(400, "That is not a recognized action for this method")
        case "GET" | "DELETE":
            params = event["queryStringParameters"]
            action = params["action"]
            match action:
                case "remove_room":
                    return remove_room_main(params)
                case "get_all_room_info":
                    return get_all_room_info_main(params)
                case "get_all_rooms":
                    return get_all_rooms_main()
                case _:
                    return generate_return(400, "That is not a recognized action for this method")
        case _:
            return generate_return(400, "That is not a recognized method for this endpoint")
