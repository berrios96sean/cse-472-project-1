from mastodon import Mastodon
import api_helper
import json_helper
    
def main(): 
    print("main function")
    mastodon = api_helper.createApiInst(api_helper.getToken(),api_helper.getUrl())
    result = mastodon.timeline_hashtag('eggs', limit=10)
    result2 = mastodon.timeline_hashtag('ocean', limit=10)
    json_data = json_helper.getJson(result,4)
    json_data2 = json_helper.getJson(result2,4)
    concat = json_data[:-1] + ',' + json_data2[1:]
    json_helper.writeToJsonFile('../results.json',json_data)
    json_helper.writeToJsonFile('../results2.json',concat)

    # api_helper.postToot(mastodon, "HELLO")

if __name__ == "__main__":
    main()