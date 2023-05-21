import os
from user_handler.modules.dotenv import load_dotenv
import user_handler.modules.pymysql as pymysql

load_dotenv()


def database_connect(func):
    """
        This decorator makes it so a connection is opened in the wrapped function
        As long as you put the first variable in the function as db
        You can make sql calls without needing to do redundant statements
    """
    def connect(*args, **kwargs):
        conn = pymysql.connect(host='moreboard.ce8dm1jdjv0d.us-east-2.rds.amazonaws.com',
                               user=os.getenv("DB_USER"),
                               password=os.getenv("DB_PASS"),
                               database='moreboard',
                               cursorclass=pymysql.cursors.DictCursor)
        try:
            with conn.cursor() as db:
                func_ret = func(db, *args, **kwargs)
        except Exception as error:
            raise error
        else:
            conn.commit()
        finally:
            conn.close()
        return func_ret

    return connect