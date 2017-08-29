import datetime
import json

def get_datetime():
    date = str(datetime.datetime.now())
    return json.dumps({
        "datetime" : date
    })
