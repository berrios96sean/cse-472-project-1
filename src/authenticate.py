import mastodon
from mastodon import Mastodon

######################################################
# This Program can be used to create a .secret file 
# which can make creating a connection to the API much 
# easier. I have decided not to use this as I don't want 
# to accidentally push anything to the repo that could 
# the account. I am still implementing this code in case 
# i decide to add this later on. 
######################################################


######################################################
# Open the token.txt file in read mode
######################################################
try:
    with open('../secret.txt', 'r') as file:
        # Read the contents of the file into a string variable
        token = file.read()
except FileNotFoundError:
    print("secret.txt file not found.")
except Exception as e:
    print(f"An error occurred: {e}")

Mastodon.create_app(
    'pytooterapp',
    api_base_url = 'https://mastodon.social',
    to_file = token
)