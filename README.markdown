# fast-subcheck: Fast Subdomain Checker

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Downloads](https://img.shields.io/github/downloads/TahaHatami/fast-subcheck/total)](https://github.com/TahaHatami/fast-subcheck/releases)

**fast-subcheck** is a fast and professional subdomain enumeration tool with a live CLI interface. Written in Python, it allows you to quickly identify active subdomains by providing a target domain and a wordlist file. The command-line interface (CLI), powered by the `rich` library, delivers real-time statistics and a visually appealing output, with results automatically saved to a file.

## Features

- **Live CLI Statistics**: Real-time display of:
  - Total subdomains generated
  - Subdomains tested
  - Active (live) subdomains
  - Inactive subdomains
- **Multithreaded Scanning**: Configurable thread count for faster enumeration.
- **Output Storage**: Automatically saves active subdomains to a specified file.
- **Cross-Platform Support**: Compatible with Windows, Linux, and macOS.
- **Professional CLI Interface**: Colorful and organized output using the `rich` library.
- **Robust Error Handling**: Handles network issues, timeouts, and invalid subdomains gracefully.

## Prerequisites

- **Python**: Version 3.8 or higher
- **Required Libraries**:
  ```bash
  pip install requests rich
Installation

Clone the repository:
bashgit clone https://github.com/TahaHatami/fast-subcheck.git
cd fast-subcheck

Install dependencies:
bashpip install -r requirements.txt
If requirements.txt is unavailable, run:
bashpip install requests rich


Usage
The tool is executed via the command line. Provide a target domain (using -d) and a wordlist file (using -w) containing subdomain prefixes (e.g., www, api). Active subdomains are saved to the specified output file (using -o).
Basic Syntax:
bashpython subcheck.py -d <domain> -w <wordlist_file> -o <output_file> [options]
Required Arguments

-d <domain>: Target domain (e.g., example.com)
-w <wordlist_file>: Text file with subdomain prefixes (one per line)
-o <output_file>: File to store active subdomains

Optional Arguments

--threads <number>: Number of concurrent threads (default: 10)
--timeout <seconds>: Request timeout in seconds (default: 5)
--help: Display the help message

The tool combines prefixes from the wordlist with the target domain, checks subdomains concurrently, displays live statistics in the terminal, and saves active subdomains to the output file.
Configuration
Customize the tool via command-line arguments or by modifying default values in the script:

THREAD_COUNT: Default number of threads (10)
TIMEOUT: Default request timeout (5 seconds)
OUTPUT_FILE: Output file name (specified via -o)

The tool uses the requests library for HTTP checks (HEAD requests with status codes 200–399) and the rich library for progress bars and tables in the CLI.
Examples
Basic Usage
bashpython subcheck.py -d example.com -w wordlist.txt -o output.txt
Sample Wordlist (wordlist.txt):
textwww
api
test
invalid
Terminal Output:
text[Progress] Total: 4 | Tested: 4 | Active: 2 | Inactive: 2
Output File (output.txt):
textwww.example.com
api.example.com
Custom Configuration
bashpython subcheck.py -d example.com -w wordlist.txt -o results.txt --threads 20 --timeout 10
Screenshot
Below is a screenshot of the CLI interface showcasing the progress bar and live statistics:
<img src="Screenshot.png" alt="CLI Screenshot">
Note: If the screenshot is unavailable in the repository, the CLI features a colorful progress bar and statistical table powered by the rich library.
Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch:
bashgit checkout -b feature-branch

Make and commit your changes:
bashgit commit -m "Add feature"

Push to your forked repository:
bashgit push origin feature-branch

Open a Pull Request.

Please ensure your code adheres to PEP8 standards and includes tests where possible.
License
This project is licensed under the MIT License.
Contact
For questions, suggestions, or issues, please open an issue on GitHub or contact the maintainer via TahaHatami's profile.
Thank you for using fast-subcheck! 🚀
About
A fast and live subdomain checker with CLI output.

© 2025 GitHub, Inc.
text
### Notes:
- **Structure and Tone**: The content is organized with clear headings, concise descriptions, and a professional tone suitable for a GitHub repository.
- **Screenshot Reference**: The screenshot is referenced with a placeholder (`screenshot.png`). Ensure the actual screenshot file is in the repository, or update the filename/path accordingly.
- **Badges**: Included badges for license, Python version, and downloads to enhance professionalism.
- **Language**: Fully translated to English, avoiding any Persian text while preserving all technical details.
- **Upload**: If you want me to upload this `README.md` to a specific service (e.g., Google Drive, Dropbox), please provide the preferred platform, and I can generate a link. Alternatively, you can copy the above markdown and save it as `README.md` in your repository.

Let me know if you need further refinements or assistance with uploading the file !
