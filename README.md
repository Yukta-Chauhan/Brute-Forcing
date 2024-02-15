# Directory Brute Force Tool

## Description
This Python script is a simple yet effective directory brute force tool designed to aid in web application penetration testing and security assessments. With the capability to iterate through a provided wordlist and test various directories against a target URL, it assists in identifying potential entry points and hidden resources within a web application's directory structure.

## Key Features
- **Flexible:** Allows users to specify a custom wordlist file containing directory names to be tested.
- **Versatile:** Works with any target URL, enabling testing on various web applications and websites.
- **Efficient:** Utilizes the [requests](https://pypi.org/project/requests/) library for HTTP requests, providing fast and reliable testing.
- **Informative:** Provides feedback on discovered directories, including their URLs and HTTP response status codes.
- **Lightweight:** Written in Python with minimal dependencies, making it easy to set up and use in various environments.

## Usage
1. Clone the repository or download the script.
2. Install the necessary dependencies.
3. Run the script with the desired parameters: _python brute.py -w path/to/wordlist.txt -u target_url_

Replace _"path/to/wordlist.txt"_ with the path to your wordlist file and _"target_url"_ with the URL of the web application to test.

## Requirement
- **Python:** Version 3.x or newer (e.g., Python 3.6+).

## Libraries Used:
- [requests ](https://pypi.org/project/requests/): Used for making HTTP requests in Python.
- [argparse ](https://docs.python.org/3/library/argparse.html): Used for parsing command-line arguments.
- [sys ](https://docs.python.org/3/library/sys.html): Used for system-specific parameters and functions.



Whether you're a cybersecurity professional, a web developer, or an enthusiast looking to explore web application security, this directory brute force tool provides a valuable addition to your toolkit, enhancing your ability to identify potential vulnerabilities and strengthen web application defences.
