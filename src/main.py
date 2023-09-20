from mastodon import Mastodon
import api_helper

def main(): 
    print("main function")
    mastodon = api_helper.createApiInst(api_helper.getToken(),api_helper.getUrl())
    api_helper.postToot(mastodon, "HELLO")

if __name__ == "__main__":
    main()