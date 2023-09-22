import networkx as nx 
import matplotlib.pyplot as plt 
import json 
import json_helper

def loadJsonFile(jsonFile): 
    with open(jsonFile, 'r') as f: 
        data = json.load(f)
    return data 

def createDiffusionGraph(mastodon,data):
    graph = nx.DiGraph()
    reblogs = []
    for toot in data: 
        user_id = toot['account']['username'] # using user account info 
        
        if not graph.has_node(user_id):
            graph.add_node(user_id, username=toot['account']['username'])
        
        mentions = toot.get('mentions', [])

        for mention in mentions:
            mentioned_username = mention['username']
            graph.add_edge(user_id, mentioned_username, action='mention')
        if not int(toot['reblogs_count']) == 0: 
            new_reblogs = mastodon.status_reblogged_by(toot['id'])
            reblogs += new_reblogs
    
            for reblog in reblogs:
                reblog_username = reblog['username']
                graph.add_edge(user_id, reblog_username, action='reblog')
    
    data = json_helper.getJson(reblogs,4)

    json_helper.writeToJsonFile('../reblog_data/reblog_data.json',data)          
    return graph
    
def drawSpringGraph(graph):
    pos = nx.spring_layout(graph, seed=1) 
    num_nodes = graph.number_of_nodes()
    num_edges = graph.number_of_edges()
    
    # Create a custom title string including node and edge counts
    custom_title = f"Mastodon Diffusion Network\nNode Count: {num_nodes}, Edge Count: {num_edges}"
    
    # Set the custom title as the title of the plot
    plt.title(custom_title)
    nx.draw(
            graph, 
            pos, 
            with_labels=True, 
            node_size=50, 
            node_color='lightgreen', 
            font_size=1,
            font_weight='bold', 
            arrowsize=2, 
            width=0.2 
    )
    plt.savefig('../spring_graph.pdf',format='PDF')

