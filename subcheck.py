import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from rich.console import Console
import argparse
import os
import time

console = Console()

# -----------------------------
# Argument parser
# -----------------------------
parser = argparse.ArgumentParser(
    description="Professional Subdomain Checker - fast, live output, and summary stats"
)
parser.add_argument("-d", "--domain", required=True, help="Target domain")
parser.add_argument("-w", "--wordlist", required=True, help="Text file containing subdomains")
parser.add_argument("-o", "--output", default="ActiveSubs.txt", help="File to save active subdomains")
parser.add_argument("-t", "--threads", type=int, default=30, help="Number of concurrent threads")
args = parser.parse_args()

domain = args.domain.strip()
wordlist_file = args.wordlist.strip()
output_file = args.output
max_threads = args.threads

# -----------------------------
# Check wordlist file
# -----------------------------
if not os.path.exists(wordlist_file):
    console.print(f"[red]File {wordlist_file} not found![/red]")
    exit(1)

# Read subdomains
with open(wordlist_file, "r") as f:
    subs = [line.strip().strip('.') for line in f.readlines() if line.strip()]

total_subs = len(subs)
tested_count = 0
found_count = 0
not_found_count = 0

console.print(f"[cyan]Starting check of {total_subs} subdomains for {domain}...\n[/cyan]")

# Prepare output file
with open(output_file, "w") as f:
    pass  # clear file

# -----------------------------
# Subdomain check function
# -----------------------------
def check_sub(sub):
    url = f"http://{sub}.{domain}"
    try:
        r = requests.get(url, timeout=3)
        return (url, r.status_code < 400)
    except requests.RequestException:
        return (url, False)

# -----------------------------
# Function to display live stats
# -----------------------------
def print_live_stats():
    console.clear()
    console.print(f"[bold cyan]Subdomain Scan Stats[/bold cyan]\n")
    console.print(f"Total subdomains to test      : [yellow]{total_subs}[/yellow]")
    console.print(f"Subdomains tested so far      : [yellow]{tested_count}[/yellow]")
    console.print(f"Active found & saved          : [green]{found_count}[/green]")
    console.print(f"Inactive / not found          : [red]{not_found_count}[/red]")

# -----------------------------
# Run concurrent checks
# -----------------------------
with ThreadPoolExecutor(max_workers=max_threads) as executor:
    future_to_sub = {executor.submit(check_sub, sub): sub for sub in subs}
    for future in as_completed(future_to_sub):
        url, is_active = future.result()
        tested_count += 1
        if is_active:
            found_count += 1
            with open(output_file, "a") as f:
                f.write(url + "\n")
        else:
            not_found_count += 1
        print_live_stats()

# -----------------------------
# Final summary
# -----------------------------
console.print("\n[bold green]Scan finished![/bold green]")
console.print(f"[green]{found_count} active subdomains saved to {output_file}[/green]")
console.print(f"Total tested: {tested_count} | Not found: {not_found_count}")

# -----------------------------
# By : https://github.com/TahaHatami/
# -----------------------------