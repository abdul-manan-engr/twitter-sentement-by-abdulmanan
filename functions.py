
import pickle
import re
import nltk

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize



def lemmatize(token):
    """Returns lemmatization of a token"""
    return WordNetLemmatizer().lemmatize(token, pos='v')

def tokenize(tweet):
    """Returns tokenized representation of words in lemma form excluding stopwords"""
    result = []
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(tweet)
    for token in word_tokens:    
        if token.lower not in stop_words and len(token) > 2:  # drops words with less than 3 characters
            result.append(lemmatize(token))
    return result

def preprocess_tweet(tweet):
    result = re.sub(r'(RT\s@[A-Za-z]+[A-Za-z0-9-_]+)', '', tweet)
    result = re.sub(r'(@[A-Za-z0-9-_]+)', '', result)
    result = re.sub(r'http\S+', '', result)
    result = re.sub(r'bit.ly/\S+', '', result) 
    result = re.sub(r'&[\S]+?;', '', result)
    result = re.sub(r'#', ' ', result)
    result = re.sub(r'[^\w\s]', r'', result)    
    result = re.sub(r'\w*\d\w*', r'', result)
    result = re.sub(r'\s\s+', ' ', result)
    result = re.sub(r'(\A\s+|\s+\Z)', '', result)
    processed = tokenize(result)
    return processed


def make_prediction(tweet):
    model = pickle.load(open("static/clf.pickle", "rb"))
    processed = preprocess_tweet(tweet)
    lst = []
    lst.append(processed)
    vec = pickle.load(open("static/vec.pickle", "rb"))
    print(lst)
    vectorized = vec.transform(lst[0])
    pred = model.predict(vectorized)
    prob = model.predict_proba(vectorized)[:,1]
    print(prob,type(prob),pred[0],pred)
    pred=sorted(pred)
    pred[0]=pred[-1]
    mapping = {0: 'Non Hate Words', 1: 'Hate Words Detected'}
    prediction = mapping[pred[0]]
    probability = str(prob)[1:-1]
    return tweet, prediction, probability