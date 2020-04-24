"""
API Authentication

The package tweepy is great at handling all the Twitter API OAuth Authentication details for you. 
All you need to do is pass it your authentication credentials. 
In this interactive exercise, we have created some mock authentication credentials 
(if you wanted to replicate this at home, you would need to create a Twitter App as Hugo detailed in the video). 
Your task is to pass these credentials to tweepy's OAuth handler.
"""

# Import package
import tweepy

# Store OAuth authentication credentials in relevant variables
access_token = "1092294848-aHN7DcRP9B4VMTQIhwqOYiB14YkW92fFO8k8EPy"
access_token_secret = "X4dHmhPfaksHcQ7SCbmZa2oYBBVSD2g8uIHXsp5CTaksx"
consumer_key = "nZ6EA0FxZ293SxGNg8g8aP0HM"
consumer_secret = "fJGEodwe3KiKUnsYJC3VRndj7jevVvXbK2D5EiJ2nehafRgA6i"

# Pass OAuth details to tweepy's OAuth handler
# Pass the parameters consumer_key and consumer_secret to the function tweepy.OAuthHandler().
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# Complete the passing of OAuth credentials to the OAuth handler auth by applying to it the method set_access_token(), 
#along with arguments access_token and access_token_secret.
auth.set_access_token(access_token, access_token_secret)



class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        self.file = open("tweets.txt", "w")

    def on_status(self, status):
        tweet = status._json
        self.file.write( json.dumps(tweet) + '\n' )
        self.num_tweets += 1
        if self.num_tweets < 100:
            return True
        else:
            return False
        self.file.close()

    def on_error(self, status):
        print(status)


"""
Streaming tweets

Now that you have set up your authentication credentials, it is time to stream some tweets! 
We have already defined the tweet stream listener class, MyStreamListener, just as Hugo did in the introductory video. 
You can find the code for the tweet stream listener class here.

https://gist.github.com/hugobowne/18f1c0c0709ed1a52dc5bcd462ac69f4

Your task is to create the Streamobject and to filter tweets according to particular keywords.
"""

# Initialize Stream listener
l = MyStreamListener()

# Create your Stream object with authentication
stream = tweepy.Stream(auth, l)

# Filter Twitter Streams to capture data by the keywords:
stream.filter(['clinton', 'trump', 'sanders', 'cruz'])


"""
Load and explore your Twitter data

Now that you've got your Twitter data sitting locally in a text file, it's time to explore it! 
This is what you'll do in the next few interactive exercises. 
In this exercise, you'll read the Twitter data into a list: tweets_data.
"""

# Import package
import json

# String of path to file: tweets_data_path
tweets_data_path = 'tweets.txt'

# Initialize empty list to store tweets: tweets_data
tweets_data = []

# Open connection to file
tweets_file = open(tweets_data_path, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)

# Close connection to file
tweets_file.close()

# Print the keys of the first tweet dict
print(tweets_data[0].keys())

# Import package
import pandas as pd

# Build DataFrame of tweet texts and languages
df = pd.DataFrame(tweets_data, columns=['text', 'lang'])

# Print head of DataFrame
print(df.head())







