import json 
from datetime import datetime

def writeToJsonFile(json_filename,result_json):
    with open(json_filename, 'w') as json_file: 
        json_file.write(result_json)

def serialize_datetime(obj):
    if isinstance(obj,datetime):
        return obj.isoformat()
    
def getJson(result,indent):
    dump = json.dumps(result, indent=indent, default=serialize_datetime)
    return dump