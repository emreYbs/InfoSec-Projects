#!/usr/bin/env python3
#emreybs
#Google Dorking is great for various reasons. For academicians, it is a great way to find research papers. For hackers, it is a great way to find vulnerable targets. For everyone else, it is a great way to find anything that is publicly available on the internet. 
#I'll add 3 good sites for more info and Reference:https://www.maltego.com/blog/using-google-dorks-to-support-your-open-source-intelligence-investigations/
#Another good Reference: https://www.freecodecamp.org/news/google-dorking-for-pentesters-a-practical-tutorial/
#Last but not the least: https://www.exploit-db.com/google-hacking-database
#Note: Replace the FILEPATH in the command with the actual file path of the script.

#I also use this script as a vocabulary resource by using the Google search operator "define" like: define increase. Then you will get some URL links and they will be saved to a .csv file.

import requests
from functools import partial
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as bsoup
from time import sleep
import platform # For checking the OS, so the csv file can be saved in the same directory as the script
import os # Path: 
import csv # For saving the URLs to a .csv file
import argparse # For parsing command line arguments if you prefer that way. Arrange the script accordingly.
import sys # For exiting the script if the user wants to quit    


GREEN, RED, MAGENTA = '\033[1;32m', '\033[91m', '\033[1;35m' 
LIGHT_BLUE = '\033[1;34m'

print("")
print("\033[95m➶➶➶➶➶ Google Dorks Scanner ➷➷➷➷➷\033[0m") 
print("\033[1;34m\033[1;35m*•.¸♡ \tby emreybs\t ♡¸.•*\033[0m") 


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-q', '--query', dest='query', help='Specify the Search Query within \'\'')
    parser.add_argument('-e', '--engine', dest='engine', help='Specify the Search Engine (Google/Bing)')
    parser.add_argument('-p', '--pages', dest='pages', type=int, default=1, help='Specify the Number of Pages (Default: 1)')
    parser.add_argument('-P', '--processes', dest='processes', type=int, default=2, help='Specify the Number of Processes (Default: 2)')
    options = parser.parse_args()
    return options

def quit_program():
    print("""Quitting the program...
          Thanks for using the script...""")
    sys.exit()

def google_search(query, page):
    base_url = 'https://www.google.com/search'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
    params = {'q': query, 'start': page * 30} 
    with requests.Session() as session:
        resp = session.get(base_url, params=params, headers=headers)
    soup = bsoup(resp.text, 'lxml')
    links = soup.select("div.yuRUbf")
    result = [link.find('a').get('href') for link in links]
    return result


def bing_search(query, page):
    base_url = 'https://www.bing.com/search'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
    params = {'q': query, 'first': page * 30 + 1}
    with requests.Session() as session:
        resp = session.get(base_url, params=params, headers=headers)
    soup = bsoup(resp.text, 'lxml')
    links = soup.select('cite')
    result = [link.text for link in links]
    return result


def search_result(q, engine, pages, processes, result):
    print('-' * 70)
    print(f'Searching for: {q} in {pages} page(s) of {engine} with {processes} processes')
    sleep(0.1)
    print('-' * 70)
    print()
    counter = 0
    urls = []
    for range in result:
        for r in range:
            url = ' '.join(str(r)).replace(' ', '')  # Remove extra spaces in the URL
            urls.append(url)
            print('[+] ' + url)
            counter += 1
    print()
    print('-' * 70)
    print(f'Number of URLs: {counter}')
    print('-' * 70)

    # Save URLs to a .csv file
    filename = 'google_dork_urls.csv'
    if platform.system() == 'Windows':
        print("Your OS is Windows. The csv file will be saved in the same directory as the script.")
        newline = ''
    else:
        print("Your OS is Linux. The csv file will be saved in the same directory as the script.")
        newline = None
    file_exists = os.path.isfile(filename.strip())  # Remove trailing whitespace from filename
    with open(filename.strip(), 'a', newline=newline) as file:  # Remove trailing whitespace from filename
        writer = csv.writer(file)
        if not file_exists:
            print(f'Saving URLs to {filename}')
            writer.writerow(
                ['URL']
            )
        writer.writerows([[url] for url in urls])
    print(f'Saved URLs to {filename}')
    print(f'The csv file is saved in the same directory as the script: {os.path.abspath(filename.strip())}')  


def UsageExamples(): 
    print("\n\t\033[91mUsage Examples: \n\033[0m") 
    sleep (0.2) # Arrenge the time interval between the prints as you wish. I didn't want a slow print but if you need to read my comments, you can increase the time interval.
    print("These examples can give you an idea of how to use the script.\n")
    sleep (0.3)
    print("\tYou can also use the script 2 ways:\n")
    sleep (0.2)
    print("\t\t1. Provide the query and the search engine if you prefer this syntax: python GoogleDorksScanner.py \n")
    sleep (0.3)
    print("\tEXAMPLE: python GoogleDorksScanner.py   --query 'intitle:index of db' --engine google --pages 5 --processes 10\n")
    sleep (0.3)
    print("\t\t2. Or you can also provide the query only\n")
    sleep (0.2)
    print("EXAMPLE: intitle:index of db\n")
    sleep (0.2)
    print("1. Search for exposed database files:")
    sleep (0.1)
    print("   python GoogleDorksScanner.py --query 'intitle:index of db' --engine google --pages 5 --processes 10") # You can change the number of pages and processes as you wish.
    sleep (0.1)
    sleep (0.1)
    print("Or Just provide the query like:  'intitle:index of db")
    sleep (0.2)
    print()
    print("2. Find vulnerable webcams:")
    sleep (0.2)
    print("   python GoogleDorksScanner.py --query 'inurl:/view.shtml' --engine google --pages 3 --processes 5'") # Webcam Dorks can change; sometimes work, sometimes not. So you may need to specify the video camera models, brands, etc.
    sleep (0.2)
    sleep (0.1)
    print("Or Just provide the query like:  inurl:/view.shtml")
    sleep (0.2)
    print()
    print("3. Discover open FTP servers:")
    sleep (0.2)
    print("   python GoogleDorksScanner.py --query 'intitle:FTP inurl:(Provide the URL here)' --engine google --pages 2 --processes 3'")
    sleep (0.1)
    print("Or Just provide the query like:  intitle:FTP inurl: write the Domain name/URL here")
    sleep (0.2)
    print("Example: intitle:FTP inurl:ftp://ftp.example.com")
    sleep (0.2)
    print()
    print("4. Search for exposed Git repositories:")
    sleep (0.2)
    print("   python GoogleDorksScanner.py --query 'inurl:.git' --engine google --pages 4 --processes 8'")
    sleep (0.1)
    print("Or Just provide the query like:  'inurl:.git' --engine google --pages 4 --processes 8'")
    sleep (0.2)
    print("5. Find exposed sensitive documents:")
    sleep(0.2)
    print("   python GoogleDorksScanner.py --query 'filetype:pdf confidential' --engine google --pages 3 --processes 5'")
    sleep(0.1)
    print("Or Just provide the query like:  'filetype:pdf confidential' --engine google --pages 3 --processes 5'")
    sleep(0.2)
    print()
    print("6. Discover vulnerable web applications:")
    sleep(0.2)
    print("   python GoogleDorksScanner.py --query 'inurl:/admin.php' --engine google --pages 4 --processes 8'")
    sleep(0.1)
    print("Or Just provide the query like:  'inurl:/admin.php' --engine google --pages 4 --processes 8'")
    sleep(0.2)
    print()
    print("7. Search for exposed network devices:")
    sleep(0.2)
    print("   python GoogleDorksScanner.py --query 'intitle:router login' --engine google --pages 2 --processes 3'")
    sleep(0.1)
    print("Or Just provide the query like:  'intitle:router login' --engine google --pages 2 --processes 3'")
    sleep(0.2)
    print()
    print("8. Find open directories:")
    sleep(0.2)
    print("   python GoogleDorksScanner.py --query 'intitle:index of /' --engine google --pages 5 --processes 10'")
    sleep(0.1)
    print("Or Just provide the query like:  'intitle:index of /' --engine google --pages 5 --processes 10'")
    sleep(0.2)
    print()
    print("9. Discover exposed CCTV cameras:")
    sleep(0.2)
    print("   python GoogleDorksScanner.py --query 'inurl:/view/view.shtml' --engine google --pages 3 --processes 5'")
    sleep(0.1)
    print("Or Just provide the query like:  'inurl:/view/view.shtml' --engine google --pages 3 --processes 5'")
    #Good Resource for some Cameras: https://github.com/iveresk/camera_dorks/blob/main/dorks.json
    sleep(0.2)
    print()
    print("-" * 70)
    print("Note: Replace the FILEPATH in the command with the actual file path of the script.")


UsageExamples()
print("\n\t◦•●◉✿ Usage Examples ✿◉●•◦")

options = get_arguments()

banner = ''' 

♫♫♫.•*¨`*•..¸♥☼♥ ¸.•*¨`*•.♫♫♫
╔═══════ ೋღღೋ ═══════╗
    ೋ Google Dorks ೋ
╚═══════ ೋღღೋ ═══════╝
♫♫♫.•*¨`*•..¸♥☼♥ ¸.•*¨`*•.♫♫♫

    ★彡 by emreybs 彡★
'''


def main():
    print()
    if not options.query:
        sleep (0.1)
        query = input(' Enter the Search Query: ')
        print(f" Searching for: {query}")
    else:
        query = options.query
    if not options.engine:
        sleep (0.1)
        engine = input(' Choose the Search Engine (Google/Bing): ') or 'google'
        print("You can use Bing Search Engine too. Google is the default search engine for this script.")
        sleep (0.2)
        print(f" Searching in: {engine}")
        sleep (0.1)
        print()
    else:
        engine = options.engine

    if engine.lower() == 'google':
        print(' Searching in Google...')
        sleep (0.1)
        target = partial(google_search, query)
    elif engine.lower() == 'bing':
        print(' Searching in Bing...')
        sleep (0.1)
        target = partial(bing_search, query)
    else:
        print('Invalid Option Entered!..')
        sleep (0.1)
        print('Please try again...')
        print('Exiting the program now...')
        exit()

    with ThreadPoolExecutor(max_workers=options.processes) as executor:
        result = list(executor.map(target, range(options.pages)))

    search_result(query, engine, options.pages, options.processes, result)


print(GREEN + banner)

try:
    main()
    while True:
        if options.query and options.engine:
            exit()
        else:
            main()
except KeyboardInterrupt:
    print('\n\tThanks For using!\n')
    sleep (0.1)
    exit()
except requests.exceptions.RequestException:
    print(RED + '\n Error has occurred during the request. Please try again later...')
    sleep (0.1)
    exit()
