from mastodon import Mastodon
from datetime import datetime
import api_helper
import json

def serialize_datetime(obj):
    if isinstance(obj,datetime):
        return obj.isoformat()
    
def main(): 
    print("main function")
    mastodon = api_helper.createApiInst(api_helper.getToken(),api_helper.getUrl())
    result = mastodon.timeline_hashtag('eggs', limit=10)
    result_json = json.dumps(result, indent=4, default=serialize_datetime)
    json_filename = '../results.json'
    with open(json_filename, 'w') as json_file: 
        json_file.write(result_json)
    # api_helper.postToot(mastodon, "HELLO")

if __name__ == "__main__":
    main()