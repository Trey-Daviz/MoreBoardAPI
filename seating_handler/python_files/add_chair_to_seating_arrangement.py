from seating_handler.python_files.decorators import database_connect
from seating_handler.python_files.helper_functions import generate_return


def add_chair_to_seating_arrangement_main(body):
    return AddChairToSeatingArrangement(body["class_id"], body["arrangement"])


@database_connect
def AddChairToSeatingArrangement(db, class_id, arrangement):
    try:
        for i in arrangement:
            sql = "INSERT INTO chair(chair_x, chair_y, student_id, class_id) VALUES(%s, %s, %s, %s)" % (
                i["x"], i["y"], i["student_id"], class_id)
            db.execute(sql)
        # 200 for successful.  Even if they don't match, the code ran successfully
        return generate_return(200, "The chairs have been added to that class")
    except Exception as e:
        # Generic answer returns a 400
        return generate_return(400, str(e))