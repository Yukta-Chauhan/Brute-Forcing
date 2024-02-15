import requests
import argparse
import sys

# Intitializing ArgumentPArser
parser = argparse.ArgumentParser(description="Simple script to perform URL directory brute-forcing.")
# Adding arguments
parser.add_argument('-w', '--wordlist', type=str, required=True, help="Path to the wordlist file.")
parser.add_argument('-u', '--url', type=str, required=True, help="Target URL for directory brute-forcing.")
args = parser.parse_args()

# Printing provided arguments
print("[+] Wordlist: ", args.wordlist)
print("[+] URL: ", args.url)

# Request Headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Working with the wordlist file
try:
    with open(args.wordlist, 'r') as file:
        lines = file.readlines()  # Reading all lines from the file
except FileNotFoundError:
    print("Wordlist file not found.")
    sys.exit(1)

# Checking if URL schema exists in the URL
if not args.url.startswith(('http://', 'https://')):
    print('Please enter a valid URL with schema (http:// or https://)')
    sys.exit(1)

# Iterating through each word in the wordlist
for line in lines:
    word = line.strip()  # Removing trailing newline characters
    url = args.url.rstrip('/') + '/' + word  # Constructing the URL

    # Sending HTTP GET request
    try:
        response = requests.get(url, headers=headers)

        # Checking if the request was successful (status code 200) or not
        if response.status_code != 404:
            print(url, ":", response.status_code)
    except requests.RequestException as e:
        print(f"Error occurred while connecting to {url}: {e}")

print("Directory brute-force completed.")    