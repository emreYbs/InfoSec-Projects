#emreYbs(e3re)

# This is a very basic script that can help me for my Scraping projects when I search for RSS Feeds in a website. I'll improve this version later.
# I was able to find some RSS Feeds URL in some blogs with the help of this simple scirpt, then I wrote the scraping script. Check this for example: 
# https://github.com/emreYbs/InfoSec-Projects/blob/main/InfoSec-OSINT-Blogs/Scraper-Projects/RSS/RssFeedsDownloaders/CyberRSSfeeds.py

import requests
from bs4 import BeautifulSoup


print("\tThis script will search for RSS feeds in a given URL.\n")


def get_rss_feed(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for any HTTP errors
        soup = BeautifulSoup(response.text, "lxml")  # Use lxml as the XML parser
        link = soup.find("link", type="application/rss+xml")
        if link:
            return link.get("href")
        else:
            return None
    except requests.exceptions.MissingSchema:
        print("Invalid URL format.")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
        return None


site2lookforRSSfeeds = input("Enter the site to look for RSS feeds:  ")
rss_feed = get_rss_feed(site2lookforRSSfeeds)  # Pass the variable value as an argument
if rss_feed:
    print(f"RSS feed URL: {rss_feed}")
else:
    print("No RSS feed found.")
