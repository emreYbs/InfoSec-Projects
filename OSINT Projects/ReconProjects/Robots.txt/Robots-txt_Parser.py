#!/usr/bin/env python3
#github.com/emreYbs 

#Robots.txt Parser Script
# As you know, a robots. txt file contains instructions for bots that tell them 
# which webpages they can and cannot access.It is also useful for pentesters, bugbounty hunters to check.
# This script is used to fetch and parse the robots.txt file of a given website.
# It will also save the output as a csv file.

# Usage: python Robots-txt_Parser.py -u https://example.com


from time import sleep
import signal
import argparse
import os
import sys
import logging #for logging, not a necessity for this script but I wanted to try it to see how it works and for debugging reasons
import requests
import csv
import urllib.robotparser



USER_AGENT = "MyBot/1.0 (compatible; PythonScript/1.0)"

sleep(0.2)
print("\nThis script is used to fetch and parse the robots.txt file of a given website.")
sleep(0.5)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="URL of the website")
    return parser.parse_args()


def clear_console():
    if sys.platform.startswith("win"):
        os.system("cls")
    else:
        os.system("clear")


def process_request(url):
    try:
        headers = {"User-Agent": USER_AGENT}
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 403: 
            logging.error("\nAccess to the resource is forbidden (403 error). Please check your permissions or try a different URL.")
            print("\tExitting...")
            return None
        elif response.status_code == 429:
            logging.error("\nToo many requests (429 error). Please wait and try again later.")
            print("\tExitting...")
            return None
        elif response.status_code >= 500:
            logging.error("\nServer error ({} error). Please try again later.".format(response.status_code))
            print("\tExitting...")
            return None
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as error:
        logging.error("\nError occurred while making the request: {}".format(error))
        print("\tExitting...\n")
        return None


def display_banner():
    print("\033[95m*************************")
    print("Robots.txt Parser Script")
    print("\tby emreybs")
    print("*************************\033[0m")
    print("\nExample usage: python Robots-txt_Parser.py -u https://example.com")


def save_output_as_csv(output):
    with open("Robots-txt_output.csv", "a", newline="") as csvfile: #a: append, I, on purpose, not prefered to use "w" option. You can 
        writer = csv.writer(csvfile)
        writer.writerow(["Robots.txt"])
        writer.writerow([])
        writer.writerow(["Disallow", "Allow"])
        writer.writerow(["--------", "-----"])
        for line in output.splitlines():
            if line.strip():
                if ":" in line:
                    key, value = line.split(":", 1)
                    writer.writerow([key.strip(), value.strip()])
                else:
                    writer.writerow([line.strip(), ""])


def main():
    logging.basicConfig(level=logging.INFO)

    display_banner()

    args = parse_arguments()
    if not args.url:
        logging.error("URL is required. Please provide a URL using the -u or --url option.\n")
        print("Exitting...\n")
        sys.exit(1)

    url = f"{args.url}/robots.txt"
    logging.info(f"Your URL is: {url}")

    retry_count = 0
    while retry_count < 3:
        robots_txt = process_request(url)
        if robots_txt:
            logging.info(robots_txt)
            save_output_as_csv(robots_txt)
            break
        retry_count += 1
        sleep_time = 2 ** retry_count
        logging.info(f"Retrying in {sleep_time} seconds...")
        sleep(sleep_time)


def signal_handler(signal, frame):
    pass


def parse_robots_txt(url):
    robot_parser = urllib.robotparser.RobotFileParser()

    robot_parser.set_url(url)
    robot_parser.read()
    return robot_parser.default_entry


print("\n*****************************************************")
sleep(0.2)
print(" Thank you for using ╰☆☆ Robots.txt Parser Script ☆☆╰")
print("*****************************************************\n")

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    main()
    
