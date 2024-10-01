import tweepy
import time

# Twitter API credentials (replace these with your actual credentials)
api_key = 'YOUR_API_KEY'
api_key_secret = 'YOUR_API_KEY_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Set up the authentication
auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Define a list of post IDs (tweets) you want to interact with
post_ids = ['POST_ID_1', 'POST_ID_2', 'POST_ID_3']  # Replace with actual post IDs

# The message to comment on each post
comment_message = "Nice post! Keep it up! 😊"

def mass_like():
    """Mass like tweets."""
    for post_id in post_ids:
        try:
            api.create_favorite(post_id)  # Like the tweet
            print(f"Liked tweet {post_id}")
            time.sleep(1)  # Sleep to avoid hitting rate limits
        except tweepy.TweepError as e:
            print(f"Error liking tweet {post_id}: {str(e)}")
        except Exception as e:
            print(f"Unexpected error: {str(e)}")

def mass_retweet():
    """Mass retweet tweets."""
    for post_id in post_ids:
        try:
            api.retweet(post_id)  # Retweet the tweet
            print(f"Retweeted tweet {post_id}")
            time.sleep(1)  # Sleep to avoid hitting rate limits
        except tweepy.TweepError as e:
            print(f"Error retweeting tweet {post_id}: {str(e)}")
        except Exception as e:
            print(f"Unexpected error: {str(e)}")

def mass_comment():
    """Mass comment on tweets."""
    for post_id in post_ids:
        try:
            # Get the tweet to comment on
            tweet = api.get_status(post_id)
            
            # Reply to the tweet
            api.update_status(
                status=f"@{tweet.user.screen_name} {comment_message}",
                in_reply_to_status_id=post_id
            )
            print(f"Commented on tweet {post_id}")
            time.sleep(1)  # Sleep to avoid hitting rate limits
        except tweepy.TweepError as e:
            print(f"Error commenting on tweet {post_id}: {str(e)}")
        except Exception as e:
            print(f"Unexpected error: {str(e)}")

# Execute mass actions
mass_like()   # Mass like the posts
mass_retweet()  # Mass retweet the posts
mass_comment()  # Mass comment on the posts
