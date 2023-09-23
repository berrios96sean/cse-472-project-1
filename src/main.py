from mastodon import Mastodon
import api_helper
import json 
import json_helper
import network_construction
import sys
import classification

def main(): 
    if len(sys.argv) > 1:
        limit = sys.argv[1]
    else:
        limit = 30   
    print("main function")
    mastodon = api_helper.createApiInst(api_helper.getToken(),api_helper.getUrl())
    result  = mastodon.timeline_hashtag('HealthcareCosts', limit=limit)
    result2 = mastodon.timeline_hashtag('PrivateHealthcare', limit=limit)
    result3 = mastodon.timeline_hashtag('UniversalHealthcare', limit=limit)
    result4 = mastodon.timeline_hashtag('MedicareForAll', limit=limit)
    json_data = json_helper.getJson(result,4)
    json_data2 = json_helper.getJson(result2,4)
    json_data3 = json_helper.getJson(result3,4)
    json_data4 = json_helper.getJson(result4,4)
    concat1 = json_data[:-1] +  ',' + json_data2[1:] 
    concat2 = json_data3[:-1] +  ',' + json_data4[1:]
    concat3 = concat1[:-1] + ',' + concat2[1:]
    json_helper.writeToJsonFile('../results.json',concat3)
    data = network_construction.loadJsonFile('../results.json')
    graph = network_construction.createDiffusionGraph(mastodon,data)
    print("Number of nodes in graph = ", graph.number_of_nodes())
    network_construction.drawSpringGraph(graph)
    print("############ -- Extracting Status Data -- ############")
    data1 = api_helper.getStatusHashtags(mastodon,'../reblog_data/reblog_data.json','UniversalHealthcare')
    data2 = api_helper.getStatusHashtags(mastodon,'../reblog_data/reblog_data.json','HealthcareCosts')
    data3 = api_helper.getStatusHashtags(mastodon,'../reblog_data/reblog_data.json','PrivateHealthcare')
    data4 = api_helper.getStatusHashtags(mastodon,'../reblog_data/reblog_data.json','MedicareForAll')
    c1 = data1[:-1] + ',' + data2[1:]
    c2 = data3[:-1] + ',' + data4[1:]
    c3 = c1[:-1] + ',' + c2[1:]
    json_helper.writeToJsonFile('../status_data/status_data.json',c3)  
    user_list = classification.getUserInfo()
    classification.createJsonForLlamaResponses()
    classification.writeClassificationJson()
    classification.addUsersWithNoContent(user_list)
    network_construction.printDegDistGraph()


    # api_helper.postToot(mastodon, "HELLO")

if __name__ == "__main__":
    main()