#!/usr/bin/env python3
# emreYbs
# This script will download the RSS feeds from the following URL:  https://i-intelligence.eu/insights.rss
# Although the RSS Feed section is not very active or up to date, it is still a good resource for learning about the latest developments in the field of osint.

import feedparser # pip install feedparser
import csv
import pandas as pd
import os
base_url = "https://i-intelligence.eu/insights.rss"
csv_filename = "rss_feeds.csv"
excel_filename = "rss_feeds.xlsx"

def check_feeds_downloaded():
    return os.path.exists(csv_filename) and os.path.exists(excel_filename)

if not check_feeds_downloaded():
    # Download the RSS feeds
    feed = feedparser.parse(base_url)
    print("\n\033[95mThis script will download the RSS feeds from the following URL: \033[0m", base_url) 
    print("\n\033[94mRSS feeds downloaded successfully!\033[0m") 
    print("\tNumber of RSS posts : ", len(feed.entries))
    print("\tFeed Title : ", feed.feed.title)
    print("\tFeed Description : ", feed.feed.description)
    print("\033[91mFeed Link : \033[0m", feed.feed.link) 
    #print("Feed Language : ", feed.feed.language)
    #print("\033[94mFeed Published Date : \033[0m", feed.feed.published) # No need to print this, so I then commented it
    #print("\033[95mFeed Updated Date : \033[0m", feed.feed.updated) # No need to print this since the blog is not updated frequently

    # Save the RSS feeds in CSV format
    with open(csv_filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Title", "Link", "Published"])
        for entry in feed.entries:
            writer.writerow([entry.title, entry.link, entry.published])

    # Save the RSS feeds in Excel format
    df = pd.DataFrame([[entry.title, entry.link, entry.published] for entry in feed.entries],
                      columns=["Title", "Link", "Published"])
    df.to_excel(excel_filename, index=False)

    print("\n\033[92mRSS feeds downloaded and saved in Excel format\033[0m\n") 
    print("\t\t\033[92mPlease check the following files:\033[0m\n")
    print("\t\t\t", csv_filename)
    print("\t\t\t", excel_filename)
    print("\n")
    print("Check the Blog for more resources: 【｡_｡】 https://i-intelligence.eu/insights.rss 【｡_｡】")
    print("Exitting...\n")
else:
    print("\n\t\033[91mRSS feeds already downloaded. Skipping download.\033[0m\n") 
    print("\t\t\033[92mIf you want to download the RSS feeds again, then delete the following files:\033[0m\n")
    print("\t\t\t", csv_filename)
    print("\t\t\t", excel_filename)
    print("\n")
