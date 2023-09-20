from mastodon import Mastodon
import api_helper
import json_helper
    
def main(): 
    print("main function")
    mastodon = api_helper.createApiInst(api_helper.getToken(),api_helper.getUrl())
    result = mastodon.timeline_hashtag('eggs', limit=10)
    json_data = json_helper.getJson(result,4)
    json_helper.writeToJsonFile('../results.json',json_data)

    # api_helper.postToot(mastodon, "HELLO")

if __name__ == "__main__":
    main()