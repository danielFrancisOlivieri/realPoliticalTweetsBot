

# for language processing 
import nltk, re, pprint
from nltk import word_tokenize

# for randomness
import random

# for names
import names

# playing with twitter
import tweepy

# API keys
consumer_key = 'Rcj0tEFxa6BPpSAL3h0ogCUAz'
consumer_secret = 'Sbcao5F4sbx2kmOH8cuwjKXq1YQXjZhJIjI6mH49nrWogvCnGa'
access_token = '911998460425097216-IQlhUlZVlfjOsPGSvUD6LWRiYpzGe6m'
access_token_secret = 'iiWypM5uhFjpleokHo1M2XqppBR4qh4aVRA2BHCat6u8Z'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# list of states
statesList = ["Rhode Island", "Wyoming", "Colorado", "Nevada", "Delaware"]

# list of offices
politicalOfficeList = ["Governor", "Representative", "Senator", "Sheriff", "Chief of Police"]


# choose random office
politicalOffice = random.choice(politicalOfficeList)

# generate name
name = names.get_full_name(gender='male')

# choose random state
state = random.choice(statesList)


tweet = "Breaking: " + politicalOffice + " " + name + " of " + state + " has announced he is running for president."


print(tweet)

api.update_status(tweet)


# for hashtags
hashtag = hashtag.replace(" ", "")

hashtag = hashtag.lower()

hashtag = re.sub(r'[^\w\s]','',hashtag)

hashtag = "#" + hashtag

print(hashtag)

tweet += " " + hashtag 

print(tweet)

api.update_status(tweet)
