#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author EmreYbs | github.com/emreYbs
# The aim of this simple python script is to  retrieve the latest posts from a subreddit and write them to a file.

# EDIT: I wrote another version to be able to use API and added some more functions but still working on it and testing. I'll add that version here later.

#Note: The script does not handle errors that may occur during API requests. So I will work on it and try to improve the code for futher needs. For now, it is simple and as it is needed.

import praw  # pip install praw (Python Reddit API Wrapper)
from datetime import datetime, timedelta

print("This Python script will retrieve the latest posts from a subreddit and write them to a file.\n")
print("Starting Reddit.py...")
# Load Reddit API credentials from a configuration file or environment variables
# Add your own API and username/password. Credentials can be obtained by creating a Reddit app. Check here: https://www.reddit.com/prefs/apps.
reddit = praw.Reddit(
    client_id="YOUR REDDIT APP ID",
    client_secret="YOUR REDDIT APP SECRET",
    username='YOUR REDDIT USERNAME',
    password='YOUR REDDIT ACCOUNT PASSWORD'
)

# Select the subreddit to retrieve posts from

subreddit_name = input("Enter the subreddit name: ")
subreddit = reddit.subreddit(subreddit_name)

# Retrieve the latest posts from the subreddit
posts_24h = []
for post in subreddit.new():
    current_time = datetime.utcnow()
    post_time = datetime.utcfromtimestamp(post.created_utc)

    # Filter posts to only include those posted within the last 24 hours
    delta_time = current_time - post_time
    if delta_time <= timedelta(hours=24):  # Arrange the time as your needs
        posts_24h.append((post.title, post.selftext, post_time))

        # Write the title and self-text of the post to a file
        with open('output.txt', 'a') as file:
            file.write(f'{post.title}\n{post.selftext}\n\n')

# Print the filtered posts
print(posts_24h)
print("Exitted...")
