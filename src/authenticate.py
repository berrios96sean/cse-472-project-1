import mastodon
from mastodon import Mastodon

# Open the token.txt file in read mode
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