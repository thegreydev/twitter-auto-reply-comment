import tweepy

# Twitter API credentials (replace these with your actual credentials)
api_key = 'YOUR_API_KEY'
api_key_secret = 'YOUR_API_KEY_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Set up the authentication
auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# The keywords to search for
keywords = ["Python", "coding", "programming"]

# The reply message
reply_message = "Hello! If you're into coding, let's connect!"

def search_and_reply():
    # Search for tweets containing the keywords
    for keyword in keywords:
        for tweet in tweepy.Cursor(api.search_tweets, q=keyword, lang="en").items(10):
            try:
                # Print the tweet text (just for checking)
                print(f"Tweet found: {tweet.text}")
                
                # Reply to the tweet
                api.update_status(f"@{tweet.user.screen_name} {reply_message}", in_reply_to_status_id=tweet.id)
                
                print(f"Replied to {tweet.user.screen_name}")
            except tweepy.TweepError as e:
                print(f"Error: {str(e)}")
            except StopIteration:
                break

# Call the function to start searching and replying
search_and_reply()
