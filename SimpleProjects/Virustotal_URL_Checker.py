
import requests

print("\n\tWelcome to the VirusTotal URL checker\n")
print("This program will check if a URL is malicious or not\n")

url = input("\nEnter the URL address to check: ")

# Replace YOUR_API_KEY with your actual VirusTotal API key
#params = {'apikey': 'YOUR_API_KEY', 'resource': url}
#Of course, I haven't put my own API key here:), just made up API key. Get a Free Virustotal API and add it here.
params = {'apikey': '6b0283ee1c5367fdd44b09e9h4fe2196deb726d14e6834181032771c62133e', 'resource': url}
headers = {
  "Accept-Encoding": "gzip, deflate",
  "User-Agent" : "gzip,  'Opera Mini/'"
}

response = requests.get('https://www.virustotal.com/vtapi/v2/url/report', params=params, headers=headers)

if response.status_code == 200:
    json_response = response.json()
    if json_response['response_code'] == 0:
        print("Weird: This URL is not in the VirusTotal database.")
    else:
        positives = json_response['positives']
        total = json_response['total']
        print(f"\n{positives} out of {total} antivirus scanners detected malicious activity.\n")
else:
    print("Error: Could not connect to VirusTotal.")

