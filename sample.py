import tweepy
import time
import re
import gensim
from gensim import corpora
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from pprint import pprint 

para = ""

def clean_tweet(tweet):
        return ' '.join(re.sub("([@#&][A-Za-z0-9_]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    
    return normalized

def clear_numbers(tweet):
    return ' '.join(re.sub("([A-Za-z0-9_]*[0-9]+[A-Za-z0-9]*)"," ",tweet).split())

ckey = "xVxqkDg4grUe7EULLlUCjJWnE"
csecret = "W1PcvyvvUNtVGedZVocmszKKKONg4R1iD576nuAL3V1QZiUYog"
atoken = "894614642592423937-l492HJKBXW1RkVl7SlkDl2rqVwjohuk"
asecret = "pL66wFrjSGgZhsWPvnOJbJDSX5TVtW1R1YeoSf5PrDu4W"

OAUTH_KEYS = {'consumer_key':ckey, 'consumer_secret':csecret,'access_token_key':atoken, 'access_token_secret':asecret}

auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])

api = tweepy.API(auth)

doc_complete = []
doc_clean = []
#function to clean a document 

stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()


for tweet in tweepy.Cursor(api.search, q='SriDevi', since='2018-03-10', until='2018-03-20').items(200): # need to figure out how to extract all tweets in the previous day
    if tweet.geo == None:
        if tweet.lang == 'en' :
            #print "Tweet created:", tweet.text
            #print tweet.text 
            temp = clean_tweet(tweet.text)
            para+=temp 
            temp = clear_numbers(temp)
            #print temp
            #print "<-----------------------------------------------clear------------------------------------------------>\n\n\n\n\n\n\n"
            temp = temp.replace("RT", "")
            doc_complete.append(temp)
            #word_tokens = word_tokenize(temp)
            #filtered_sentence = []
            #for w in word_tokens:
             #   if w not in stop_words:
              #       filtered_sentence.append(w)
            #tweets.append(tweet.text)
            #print word_tokens
            #print filtered_sentence



doc_clean = [clean(doc).split() for doc in doc_complete]
texts = [] 

#pprint(doc_clean)

bigram = gensim.models.Phrases(doc_clean)

texts = [bigram[line] for line in doc_clean]

pprint(texts)


print "<<<<_--------->>>>>>"

import itertools

texts.sort()

ttemp = list(texts for texts ,_ in itertools.groupby(texts))

pprint(ttemp)

# Creating the term dictionary of our courpus, where every unique term is assigned an index. 
dictionary = corpora.Dictionary(ttemp)


# Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
corpus = [dictionary.doc2bow(doc) for doc in ttemp]

LDA = gensim.models.ldamodel.LdaModel

ldamodel = LDA(corpus=corpus, num_topics=10, id2word=dictionary)

pprint(ldamodel.show_topics())

