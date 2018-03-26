doc1 = "Sugar is bad to consume. My sister likes to have sugar, but not my father."
doc2 = "My father spends a lot of time driving my sister around to dance practice."
doc3 = "Doctors suggest that driving may cause increased stress and blood pressure."
doc4 = "Sometimes I feel pressure to perform well at school, but my father never seems to drive my sister to do better."
doc5 = "Health experts say that Sugar is not good for your lifestyle."

import sys
from pprint import pprint

# compile documents

fp = open(sys.argv[1])
doc = fp.read()

doc_complete = doc.split('.')

# LIBRARY TO CONVERT CORPUS TO A MATIRX REPRESENTATION
# Importing Gensim
import gensim
from gensim import corpora


#include NLTK libraries


from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()

def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized

doc_clean = [clean(doc).split() for doc in doc_complete]


# print(doc_complete)

# print(doc_clean)

# Creating the term dictionary of our courpus, where every unique term is assigned an index. 

dictionary = corpora.Dictionary(doc_clean)

# Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

# print(doc_clean)

# print(doc_term_matrix)

# Creating the object for LDA model using gensim library
LDA = gensim.models.ldamodel.LdaModel

# Running and Trainign LDA model on the document term matrix.
Ldamodel = LDA(doc_term_matrix, num_topics=3, id2word = dictionary, passes=50)

pprint(Ldamodel.print_topics(num_topics=333, num_words=3))
