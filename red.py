import praw
import json
import pandas as pd
import requests

reddit = praw.Reddit(
    client_id="Hwfh4Mg7z1MKAoDkTP8m6A",
    client_secret="BvNV3ESpOnJak5jGOUay7JwMzbnkdg",
    user_agent="Assignment",
)


posts = []
india_subreddit = reddit.subreddit('india')
for post in india_subreddit.hot(limit=10):
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
posts = pd.DataFrame(posts,columns=['title', 'upvotes', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])

print(posts)
