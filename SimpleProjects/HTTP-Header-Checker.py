#!/usr/bin/env python3
#emreYbs: github.com/emreYbs
# -*- coding: utf-8 -*-

import requests
from time import sleep
import socket
import urllib3
import re
import csv
import json
import os
import json
import csv
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

sleep (0.2)
def print_banner():
    banner = """
▁ ▂ ▄ ▅ ▆ ▇ █ HTTP Header Checker █ ▇ ▆ ▅ ▄ ▂ ▁
                                   by emreYbs
"""
    print(banner)

print_banner()




def get_headers(domain):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    try:
        response = requests.get("https://" + domain, headers=headers, verify=False, timeout=5, allow_redirects=True) # disable SSL certificate verification
        #If the server uses a self-signed certificate,  download the certificate yourself and point to it using the verify parameter above
        if response.status_code in range(300, 400):
            print(f"Redirect to {response.headers['Location']}")
            return None
        return response.headers
    except requests.exceptions.Timeout:
        print("The request timed out")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Could not connect to {domain}. Error: {str(e)}")
        return None


def get_domain_from_user():
    sleep(0.1)
    while True:
        domain = input("\033[31m\nEnter the hostname (without http://): \033[0m")
        if re.match(r"^[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", domain):
            return domain
        else:
            print("Invalid domain format. Please try again.")


def get_response(domain):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    } 
    try:
        response = requests.get(f"https://{domain}", headers=headers, verify=False, timeout=5, allow_redirects=False)
        response.raise_for_status()
        sleep(0.1)
        print(f"Response received from {response.url}")
        return response
    except requests.exceptions.HTTPError as err:
        sleep(0.1)
        print(f"Something went wrong: {err.response.status_code} {err.response.reason}")
        return None
    except requests.exceptions.RequestException as err:
        print("Something went wrong:", err)
        return None

def print_response_details(response):
    try:
        print(f"Response JSON: {response.json()}")
        print(f"Response text: {response.text}")
    except ValueError:
        print("Response is not in JSON format")
    print(f"Status code: {response.status_code}")
    print("Headers response: ")
    for header, value in response.headers.items():
        print(f"{header} --> {value}")
    print("Headers request : ")
    for header, value in response.request.headers.items():
        print(f"{header} --> {value}")

# Get the current directory
current_directory = os.getcwd()


def save_headers_to_file(headers):
    file_path = os.path.join(current_directory, "headers.txt")
    with open(file_path, "a", encoding="utf-8") as file:
        for header, value in headers.items():
            print(f"{header} --> {value}")
            file.write(f"{header} --> {value}\n")


def save_response_to_file(response):
    file_path = os.path.join(current_directory, "response.txt")
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(response.text)
        print("Response saved to file")


def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        sleep(0.1)
        print("\033[31m" + f"IP address for {domain} is {ip_address}" + "\033[0m") 
        return ip_address

    except socket.gaierror as e:
        print(f"Failed to get IP address for {domain}: {e}") 
        return None

def save_ip_address_to_file(domain):
    print("Saving IP address to file...")
    ip_address = get_ip_address(domain)
    if ip_address:
        file_path = os.path.join(current_directory, "ip_address.txt")
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(f"{domain} --> {ip_address}\n")
            print("IP address saved to file\n")

def save_headers_to_file(headers):
    json_file_path = os.path.join(current_directory, "headers.json")
    csv_file_path = os.path.join(current_directory, "headers.csv")
    with open(json_file_path, "a", encoding="utf-8") as json_file, open(csv_file_path, "a", encoding="utf-8", newline='') as csv_file:
        headers_dict = dict(headers)
        json.dump(headers_dict, json_file, indent=4)
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Header", "Value"])
        for header, value in headers.items():
            csv_writer.writerow([header, value])


def main():
    print("\033[35m\nWelcome to the HTTP Header Checker App\033[0m")
    sleep(0.2)
    print("\033[35mThis app will check the HTTP headers of a website\033[0m")
    sleep(0.2)
    print("\033[35mPlease enter a website to check the HTTP headers\n\033[0m")
    sleep(0.1)
    domain = get_domain_from_user()
    print(f"Checking headers for {domain}...")
    headers = get_headers(domain)
    if headers:
        print("Received headers:")
        for header, value in headers.items():
            print(f"{header} --> {value}")
    else:
        print("No headers received. Exiting...")
        exit()
    response = get_response(domain)
    if response and response.status_code != 403:
        sleep(0.1)
        print_response_details(response)
        save_headers_to_file(response.headers)
        save_response_to_file(response)
        save_ip_address_to_file(domain) 
    else:
        print("No response received or received a 403 Forbidden response. Exiting...")
        sleep(0.1)
        exit()

    sleep(0.1)
    print("\033[34mData saved to files: response.json, headers.csv, ip_address.txt\033[0m")
    sleep(0.1)
    print("\033[35m\nThanks for using the HTTP Header Checker\n\033[0m")
    sleep(0.1)


if __name__ == "__main__":  
    main()
