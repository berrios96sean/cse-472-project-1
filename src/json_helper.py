import json 
from datetime import datetime
import os

def writeToJsonFile(json_filename,result_json):
    with open(json_filename, 'w') as json_file: 
        json_file.write(result_json)

def serialize_datetime(obj):
    if isinstance(obj,datetime):
        return obj.isoformat()
    
def getJson(result,indent):
    dump = json.dumps(result, indent=indent, default=serialize_datetime)
    return dump


def extract_users_from_json(json_data, user_list):
    
    with open(json_data, 'r') as f: 
        dataset = json.load(f)
    # Check if the "account" key exists in the JSON data
    for data in dataset:
        username = data['account']['username']

        if username not in user_list:
            user_list.append(username)
            
def extract_reblog_users_from_json(json_data, user_list):
    
    with open(json_data, 'r') as f: 
        dataset = json.load(f)
    # Check if the "account" key exists in the JSON data
    for data in dataset:
        username = data['username']

        if username not in user_list:
            user_list.append(username)

def write_users_to_json(user_list, output_file_path):
    user_objects = [{"username": username} for username in user_list]

    with open(output_file_path, 'w') as json_file:
        json.dump(user_objects, json_file, indent=2)