import tweepy as tp
import re
import string

consumer_key = '6aH6v6uUuv0Ab09Sdp3teOdXU'
consumer_secret = 'WkI4qWwO2WTzPWrhZxMTUaGDCccqKAB3eKFJ059w56medPlmE6'
access_token = '1288033810722852869-0iAGZXaA3ul1VaKGUXiqXTBP0wxBGz'
access_token_secret = 'XBBKa8Yy7te2dnqmC8Yg7tdXe4otlnrS3JzigWDYYCQzi'

auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tp.API(auth)

nama = "jokowi"
jumlahtweet = 1
hasil = api.user_timeline(id=nama, count=jumlahtweet, tweet_mode="extended")

for tweet in hasil:
    text = tweet.full_text #get full text
    # original_text = text
    text = text.strip() #remove empty char
    text = text.lower() #to lowercase
    text = re.sub(r"\d+", "", text) #remove number
    text = text.translate(str.maketrans('', '', string.punctuation)) #remove punctuation
    text = ' '.join(re.sub("yang | akan | di | dan", " ", text).split()) #remove stopwords

    # print('original :', original_text)
    print('preprocessed :', text)