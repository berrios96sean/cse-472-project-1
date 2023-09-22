from mastodon import Mastodon

# NOTE: not all of the variable here are needed. most were 
# included during testing of the api instance and have not been removed. 
########################################################
# Static variables for API instance 
########################################################
def getUrl():
    instance_url = 'https://mastodon.social'
    return instance_url

def setUserName(user):
    username = user
    return username

########################################################
# Read credentials from text files
########################################################
def getClientID():
    with open('../client_id.txt', 'r') as file:
        client_id = file.read().strip()
    return client_id

def getClientSecret():
    with open('../client_secret.txt', 'r') as file:
        client_secret = file.read().strip()
    return client_secret

def getToken():
    with open('../token.txt', 'r') as file:
        token = file.read().strip()
    return token 

def getPassword(): 
    with open('../password.txt', 'r') as file:
        password = file.read().strip()
    return password

########################################################
# Create a Mastodon API client
########################################################
def createApiInst(token, instance_url): 
    mastodon = Mastodon(
        access_token=token, 
        api_base_url=instance_url
    )
    return mastodon


########################################################
# Mastodon Instance Functions 
########################################################
def postToot(mastodon, message): 
    mastodon.status_post(message)

def getReblogs(mastodon,id):
    mastodon.status_reblogged_by(id)