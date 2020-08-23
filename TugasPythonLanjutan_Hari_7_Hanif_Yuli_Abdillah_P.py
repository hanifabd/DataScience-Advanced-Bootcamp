import tweepy as tp

consumer_key = 'tt6FGjUVqVV4Bga8t2a3rmRR7'
consumer_secret = 'YSZFKghu0qeP1AVgW7u4stwVFWjBw5zNtOOdOGWw1XOs3hUjlP'
access_token = '1288033810722852869-AGEa1bnXoU4YN4BeBEAnhA2bBUNLxG'
access_token_secret = 'bdLQrVlDKDT0eDNGmPMKif22EHm0eGaQRKAnnyaLUizCz'

auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tp.API(auth)

name = 'jokowi'
num = 200
user_tweets = api.user_timeline(id=name, count=num, tweet_mode="extended")

tweets = []
cov_tweet = []
topic = 'covid'
for tweet in user_tweets:
    tweet = tweet.full_text.lower()
#     print(tweet)
    if topic in tweet:
        cov_tweet.append(tweet)
    tweets.append(tweet)

print('Banyaknya tweet Pak Jokowi yang diambil: ', len(tweets))
print('Banyaknya Pak Jokowi membicarakan Covid dalam tweetnya: ', len(cov_tweet))