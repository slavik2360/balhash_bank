#PYTHON
import time
from decouple import config

#local
from database.core import Connection

my_connection: Connection = Connection(
    host=config('DB_HOST', str),
    port=config('DB_PORT', int),
    user=config('DB_USER', str),
    password=config('DB_PASSWORD', str),
    dbname=config('DB_NAME', str)
)

class Logger:
    def __init__(self) -> None:
        pass

    @staticmethod
    def log(func) -> object:
        def wrapper(*args,**kwargs) -> object:
            global my_connection
            result = func(*args, **kwargs)
            Logger.save({"time" : time.ctime(),
                         "function_name": func.__name__,
                         "args": args,
                         "kwargs": kwargs,
                         "result": result})
            with my_connection.conn.cursor() as cur:
                cur.execute('''INSERT INTO log 
                (time, name, args, kwargs, result) VALUES 
                ('{}', '{}', '{}', '{}', '{}')'''.format(
                time.ctime(), func.__name__, args[0], kwargs, result))
            return result
        return wrapper
    
    @staticmethod
    def save(data: dict) -> None:
        with open("log.txt", "a+") as logfile:
            logfile.write(f'{data["time"]} {data["function_name"]} {data["args"]} {data["kwargs"]} {data["result"]}\n')
