import tweepy
import time
import re

ckey = "cFPJZm3PRKLr87iIeiJbT0DjS"
csecret = "Uyb9e623sJf83BKNhArkugLpIfEPh5vKNEYizlzL3wf2vmZ86M"
atoken = "894614642592423937-izhwiUSKORWUzhLKzBJd1VNuA3jmzwz"
asecret = "olMVgrqbgqmeZ63aJ1hDkQBZPQ06247xd4csr45GCw5EA"

OAUTH_KEYS = {'consumer_key':ckey, 'consumer_secret':csecret,'access_token_key':atoken, 'access_token_secret':asecret}

auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])

api = tweepy.API(auth)

tweets = []

# Extract the first "xxx" tweets related to "fast car"
for tweet in tweepy.Cursor(api.search, q='Samsung', since='2018-03-7', until='2018-03-8').items(10): # need to figure out how to extract all tweets in the previous day
    if tweet.geo == None:
        print "////////////////////////////////"
        if tweet.lang == 'en' :
        	#print "Tweet created:", tweet.text
        	tweets.append(tweet.text)
        print ""

MainString = ""

file = "tweets.txt"
file1 = "single.txt"
op = open(file1,'w')
fp = open(file,"w")
for item in tweets:
  print item 
  item = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ",item).split())
  print item 
  item = item.replace("RT","")
  item = item.encode('utf-8')
  MainString+=item;
  fp.write("%s\n" % item)

print MainString
fp.write(MainString)