import re
import nltk
import joblib
import pickle
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import praw
import pandas as pd
import numpy as np
import sklearn
import redditAuth

model = pickle.load(open('models/final_model.pkl','rb'))
reddit = praw.Reddit(client_id=redditAuth.account[0],
                     client_secret=redditAuth.account[1],
                     user_agent=redditAuth.account[2], username=redditAuth.account[3],
                     password=redditAuth.account[4])

REPLACE_BY_SPACE = re.compile('[/(){}\[\]\|@,;]')
REPLACE_SYMBOL = re.compile('[^0-9a-z #+_]')
STOPWORDS = set(stopwords.words('english'))


# Let's define the function for cleaning

def clean_data(text):
    text = BeautifulSoup(text, 'xml').text
    text = text.lower()
    text = REPLACE_BY_SPACE.sub(' ', text)
    text = REPLACE_SYMBOL.sub('', text)
    text = ' '.join(word for word in text.split() if word
                    not in STOPWORDS)
    return text


# Define string function

def stringConvert(text):
    return str(text)


# Define predict function

def predict(url):
    c = []
    posts = {
        'id': [],
        'title': [],
        'body': [],
        'comments': [],
        'url': [],
        }

    submission = reddit.submission(url=url)
    posts['id'] = submission.id
    posts['title'] = submission.title
    posts['body'] = submission.selftext
    submission.comments.replace_more(limit=0)
    for comment in submission.comments.list():
        c.append(comment.body)
    posts['comments'].append(c)
    posts['url'].append(submission.url)
    data_df = pd.DataFrame(posts)
    data_df.fillna('')
    data_df['title'] = data_df['title'].apply(stringConvert)
    data_df['title'] = data_df['title'].apply(clean_data)
    data_df['body'] = data_df['body'].apply(stringConvert)
    data_df['body'] = data_df['body'].apply(clean_data)
    data_df['comments'] = data_df['comments'].apply(stringConvert)
    data_df['comments'] = data_df['comments'].apply(clean_data)

    combine = data_df['title'] + data_df['body'] + data_df['url']
    data_df = data_df.assign(combine=combine)
    return (model.predict(data_df['combine'])[0])


def FlairActual(url):
    submission = reddit.submission(url=url)
    actualflair = submission.link_flair_text
    return actualflair
