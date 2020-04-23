import pymongo
from pymongo import MongoClient
import praw
from praw.models import MoreComments
import pandas as pd
from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import stopwords

client = MongoClient('mongodb://localhost:27017/')
database = client["reddit"]

reddit = praw.Reddit(client_id='2vaHdbf1IZrlLw',
                     client_secret="v3emVA-uUqcMByduLIAT1U4yw0w",
                     user_agent='reFlare',
                     username='imskrai',
                     password='Buchan@13')

# These are all the available flairs for subreddit india
flairs = ["AskIndia", "Non-Political", "[R]eddiquette",
          "Scheduled", "Photography", "Science/Technology",
          "Politics", "Business/Finance", "Policy/Economy",
          "Sports", "Food", "AMA"]

# selecting india for subreddit
subreddit = reddit.subreddit('india')

# Top 300 posts have taken into consideration for analysis
for flair in flairs:
    r_subreddits = subreddit.search(f"flair_name:{flair}", limit=300)

    for submission in r_subreddits:
        posts = {
            "title": str(submission.title),
            "score": str(submission.score),
            "id": str(submission.id),
            "url": str(submission.url),
            "comms_num": str(submission.num_comments),
            "created": str(submission.created),
            "body": str(submission.selftext),
            "author": str(submission.author),
            "flair": str(flair),
        }
        # considering top 15 comments
        submission.comments.replace_more(limit=None)
        comment = ''
        authors = ''
        count = 0
        for top_level_comment in submission.comments:
            comment = comment + ' ' + top_level_comment.body
            authors = authors + ' ' + str(top_level_comment.author)
            count += 1
            if(count > 15):
                break

        posts["comment"] = str(comment)
        posts["authors"] = str(authors)
        result = database.posts.insert_one(posts)

