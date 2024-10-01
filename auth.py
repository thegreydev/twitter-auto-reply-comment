import tweepy

# Twitter API credentials (replace these with your actual credentials)
api_key = 'YOUR_API_KEY'
api_key_secret = 'YOUR_API_KEY_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Set up the authentication
auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)

# Create an API object to interact with Twitter
api = tweepy.API(auth)

# Verify login and print the username
try:
    user = api.verify_credentials()
    print(f"Logged in as {user.screen_name}")
except Exception as e:
    print(f"Error during login: {str(e)}")
