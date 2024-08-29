import praw
import tweepy
import time

# REDDIT Credentials
username = '<username>'
password = "<password>"
clientID = "<clientID>"
clientSecret = "<clientIDSecret>"

redditInstance = praw.Reddit(
    client_id=clientID,
    client_secret=clientSecret,
    username=username,
    password=password,
    user_agent="DailyDoseOfTechBot by /u/daily_dose_of_tech"
)

# TWITTER Credentials
CONSUMER_KEY = "<consumerKey>"
CONSUMER_SECRET = "<consumerSecret>"
ACCESS_KEY = "<accessKey>"
ACCESS_SECRET = "<accessSecret>"

client = tweepy.Client(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_KEY,
    access_token_secret=ACCESS_SECRET
)

# Store all posts to avoid duplicates
postedMessages = set()

def getRedditPost(subreddit, emoji):

    try:
        subreddit = redditInstance.subreddit(subreddit)
        topSubmission = subreddit.top(limit=20, time_filter='day')

        for submission in topSubmission:

            message = emoji + " " + submission.title + "\n" + submission.url

            if message not in postedMessages:
                tweetPost(message)
                postedMessages.add(message)
                break

    except praw.exceptions.APIException as e:
        print("Reddit API error: {e}")
        time.sleep(600)

def tweetPost(message):

    try:
        client.create_tweet(text=message)
        print("Tweet posted successfully!")

    except tweepy.TweepyException as e:
        print("Twitter error: {e}")

while True:
    getRedditPost("technews", "🚨")
    time.sleep(15120)
    getRedditPost("apple", "💻")
    time.sleep(15120)