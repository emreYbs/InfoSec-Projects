# emreybs(e3re)
# Cybersecurity RSS feed downloader

import os
import requests
import csv
import pandas as pd
import openpyxl
from openpyxl.styles import Font, Alignment
import datetime
import threading
import colorama
from colorama import Fore, Style
import xml.etree.ElementTree as ET
from time import sleep


#Add your favs, these are mine.
def choiceOfRss():
    """
    Scrapes and saves URLs of RSS feeds related to cybersecurity based on user's choice.

    Parameters:
    None

    Cyber Security Blogs:
    1 - US-CERT (United States Computer Emergency Readiness Team) RSS feed: Scrapes RSS feed URLs from the US-CERT website.
    2 - KrebsOnSecurity RSS feed: Scrapes RSS feed URLs from the KrebsOnSecurity blog.
    3 - The Hacker News RSS feed: Scrapes RSS feed URLs from The Hacker News website.
    4 - ncsc.gov.uk RSS feed
    5 - Micah Hoffman's WebBreacher RSS feed
    6 - The National Cyber Security Centre (UK) NCSC News Feed
    7 - Skopenow News RSS feed
    8 - Offensive OSINT RSS feed

    Returns:
    None
    """


def save_csv_and_excel(data, filename):
    """
    Saves the data as CSV and Excel files.

    Parameters:
    - data: The data to be saved.
    - filename: The name of the output files.

    Returns:
    - csv_path: The local path of the CSV file.
    - excel_path: The local path of the Excel file.
    """
    csv_filename = f"{filename}.csv"
    excel_filename = f"{filename}.xlsx"

    # Save as CSV
    with open(csv_filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Topic", "URL"])  # Write header
        writer.writerows(data)

    # Save as Excel
    df = pd.DataFrame(data, columns=["Topic", "URL"])
    df.to_excel(excel_filename, index=False)

    # Apply formatting to the Excel sheet
    workbook = openpyxl.load_workbook(excel_filename)
    sheet = workbook.active

    header_font = Font(bold=True)
    for cell in sheet[1]:
        cell.font = header_font

    # Set alignment for all cells
    alignment = Alignment(horizontal="left", vertical="center")
    for row in sheet.iter_rows(min_row=2):
        for cell in row:
            cell.alignment = alignment

    workbook.save(excel_filename)

    # Return the file paths
    csv_path = os.path.abspath(csv_filename)
    excel_path = os.path.abspath(excel_filename)
    return csv_path, excel_path



data = []  # List to store topic and URL

csv_path, excel_path = save_csv_and_excel(data, "Cybersecurity_RSS_feeds")
print(
    "\nThis script will download the CyberSecurity and Osint Related RSS feeds and save them as CSV and Excel files.\n"
)
print("CSV/Excel file saved at:", csv_path)


# Initialize colorama
colorama.init()

print("")
sleep(1)
print(
    f"Welcome to the {Fore.GREEN}Cybersecurity RSS feed downloader{Style.RESET_ALL}"
    f" by {Fore.YELLOW}emreYbs{Style.RESET_ALL}"
)

sleep(1)

print(
    "\nThis script will download from the following RSS feeds: \n"
    "\n1 - US-CERT (United States Computer Emergency Readiness Team) RSS feed"
    "\n2 - KrebsOnSecurity RSS feed"
    "\n3 - The Hacker News RSS feed"
    "\n4 - ncsc.gov.uk RSS feed"
    "\n5 - Micah Hoffman's WebBreacher RSS feed"
    "\n6 - The National Cyber Security Centre (UK) NCSC News Feed"
    "\n7 - Skopenow News RSS feed"
    "\n8 - Offensive OSINT RSS feed"
    "\n The RSS feed URLs will be scraped and saved as CSV and Excel files."
    "\n"
)

choiceOfRss()

# List of RSS feed URLs. Add more URLs to this list if you want to download from other feeds.
rss_urls = [
    "https://www.us-cert.gov/ncas/alerts.xml",
    "https://krebsonsecurity.com/feed/",
    "https://feeds.feedburner.com/TheHackersNews",
    "https://www.ncsc.gov.uk/api/1/services/v1/news-rss-feed.xml",
    "https://webbreacher.com/feed/",
    "https://www.ncsc.gov.uk/api/1/services/v1/news-rss-feed.xml",
    "https://www.skopenow.com/news/rss.xml",
    "https://www.offensiveosint.io/rss/",
]


def download_rss_feed(url, i):
    try:
        print(f"Now downloading from RSS feed {i}...")
        response = requests.get(url)
        response.raise_for_status()  # Check for any HTTP errors

        data = []  # List to store topic and URL

        # Parse the XML response
        root = ET.fromstring(response.content)

        # Extract topic and URL from the XML elements
        for item in root.findall(".//item"):
            topic = item.find("title").text
            url = item.find("link").text
            data.append([topic, url])

        # Create a folder with the current date to save the downloaded files
        folder_name = "CyberSecurityRSS_feeds/" + datetime.datetime.now().strftime(
            "%Y-%m-%d"
        )
        os.makedirs(folder_name, exist_ok=True)

        # Save the data as CSV and Excel files
        csv_path, excel_path = save_csv_and_excel(
            data, f"{folder_name}/Cybersecurity_RSS_feeds{i}"
        )

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching RSS feed {i}: {e}")


# Create a list to store the threads
threads = []

for i, url in enumerate(rss_urls, start=1):
    # Create a thread for each RSS feed URL
    thread = threading.Thread(target=download_rss_feed, args=(url, i))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("CSV file saved at:", csv_path)
sleep(0.5)
print("Excel file saved at:", excel_path)
sleep(0.5)
print(
    "\n*•.¸♡ Thank you for trying the "
    + Fore.GREEN
    + "Cybersecurity RSS feed downloader by emreYbs"
    + Style.RESET_ALL
    + " ♡¸.•*\n"
)
