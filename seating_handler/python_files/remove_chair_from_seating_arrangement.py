from seating_handler.python_files.decorators import database_connect
from seating_handler.python_files.helper_functions import generate_return
import json


def remove_chairs_from_seating_arrangement_main(params):
    return RemoveChairsFromSeatingArrangement(params["chair_ids"])


@database_connect
def RemoveChairsFromSeatingArrangement(db, chair_ids):
    chair_ids = json.loads(chair_ids)
    chair_ids = [int(num) for num in chair_ids]
    try:
        for i in chair_ids:
            sql = "DELETE FROM chair WHERE chair_id = %s" % i
            db.execute(sql)
        return generate_return(200, "The chairs have been deleted from that class")
    except Exception as e:
        return generate_return(400, str(e))