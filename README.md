# Subdomain Checker CLI

A fast and professional subdomain checker with **live stats**, **concurrent requests**, and **output file saving**.  
Built in Python, fully configurable and easy to use.

---

## Features

- Live progress updates in the terminal:
  - Total subdomains to test
  - Subdomains tested so far
  - Active subdomains found & saved
  - Inactive/not found subdomains
- Multi-threaded (configurable)
- Output file auto-created and live-updated
- Works on Windows, Linux, macOS
- Clean, professional CLI interface

---

## Requirements

- Python 3.8+
- Libraries:
```bash
pip install requests rich
Usage
bash
Copy
Edit
python subcheck.py -d <domain> -w <wordlist> -o <output_file> -t <threads>
Arguments
Flag	Description	Default
-d, --domain	Target domain	Required
-w, --wordlist	Text file containing subdomains	Required
-o, --output	File to save active subdomains	ActiveSubs.txt
-t, --threads	Number of concurrent threads	30

Example
bash
Copy
Edit
python subcheck.py -d google.com -w Sub.txt -o output.txt -t 50
Output
The script saves all active subdomains to the specified output file as they are found.

Live stats are printed in the terminal in real-time.

Notes
Large wordlists may take time; increasing threads can speed up scanning.

The output file is cleared on each run to avoid duplicates.

License
MIT License

yaml
Copy
Edit

---

If you want, I can also **add a small section with a GIF or screenshot** of the live stats updating, which looks super professional on GitHub.  

Do you want me to do that?