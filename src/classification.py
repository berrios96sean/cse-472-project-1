import json 
import json_helper

def getUserInfo():
    user_list = []  
    json_helper.extract_users_from_json('../results.json', user_list)
    json_helper.extract_reblog_users_from_json('../reblog_data/reblog_data.json',user_list)
    output_file_path = '../user_nodes.json'
    json_helper.write_users_to_json(user_list, output_file_path)
    return user_list
    
    
def createJsonForLlamaResponses():
    input_file_path = '../cleaned_content.txt' 
    output_file_path = '../content_w_responses.txt'  

    with open(input_file_path, 'r') as input_file:
        lines = input_file.readlines()

    with open('../llama_responses.txt', 'r') as llama_file:
        llama_lines = llama_file.readlines()

    modified_lines = []

    llama_iterator = iter(llama_lines)

    for line in lines:
        line = line.strip()
        modified_lines.append(line)
        
        if line.startswith('Username: '):
            try:
                next_llama_response = next(llama_iterator)
                modified_lines.append(next_llama_response.strip())
            except StopIteration:
                pass

    with open(output_file_path, 'w') as output_file:
        for line in modified_lines:
            output_file.write(line + '\n')

def writeClassificationJson():
    input_file_path = '../content_w_responses.txt'  
    output_json_file_path = '../classification_w_llama.json'  

    data = []
    unique_usernames = set()

    with open(input_file_path, 'r') as input_file:
        lines = input_file.readlines()
        
    for line in lines:
        line = line.strip()
        if line.startswith('Username: '):
            username = line[len('Username: '):]
            if username not in unique_usernames:
                unique_usernames.add(username)
                current_entry = {"Username": username, "Classification": "", "Content": ""}
                data.append(current_entry)
        elif line.startswith('Llama response: '):
            if data:
                data[-1]["Classification"] = line[len('Llama response: '):]
        elif line.startswith('Content: '):
            if data:
                data[-1]["Content"] = line[len('Content: '):]

    with open(output_json_file_path, 'w') as output_file:
        json.dump(data, output_file, indent=2)

    print(f"Converted content saved to {output_json_file_path}")

def addUsersWithNoContent(user_list):  
    with open('../classification_w_llama.json', 'r') as json_file:
        data = json.load(json_file)

    existing_usernames = set(entry["Username"] for entry in data)

    
    for username in user_list:
        if username not in existing_usernames:
            new_user_entry = {
                "Username": username,
                "Classification": "NEUTRAL",
                "Content": "not found"
            }
            data.append(new_user_entry)
            existing_usernames.add(username)


    with open('../classification_w_llama.json', 'w') as output_file:
        json.dump(data, output_file, indent=2)