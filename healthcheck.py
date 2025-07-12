# Copilot Workshop Demo: Payments API Health Dashboard CLI (with RapidAPI Uptime Check)

import argparse
import json
import logging
import os
import requests
from urllib.parse import quote
from dotenv import load_dotenv

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = "instant-uptime-checker.p.rapidapi.com"
RAPIDAPI_URL = "https://instant-uptime-checker.p.rapidapi.com/uptime"

def check_website_uptime(url):
    query_url = f"{RAPIDAPI_URL}?url={quote(url)}"
    headers = {
        "x-rapidapi-host": RAPIDAPI_HOST,
        "x-rapidapi-key": RAPIDAPI_KEY,
    }
    try:
        response = requests.get(query_url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logging.error(f"Error checking {url}: {e}")
        return {"error": str(e), "url": url}

def main():
    parser = argparse.ArgumentParser(description="Payment API Health Dashboard CLI")
    parser.add_argument('--url', help="URL to check using RapidAPI uptime checker")
    parser.add_argument('--json', action='store_true', help="Output result as JSON")
    args = parser.parse_args()

    if args.url:
        logging.info(f"Checking uptime for {args.url}...")
        result = check_website_uptime(args.url)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            if 'error' in result:
                print(f"Error checking {args.url}: {result['error']}")
            else:
                print(f"{args.url} => Status: {result.get('status')} | Response Time: {result.get('responseTime')}ms | Result: {result.get('result')}")
    else:
        logging.warning("No --url specified. Try: python healthcheck.py --url https://google.com")

if __name__ == '__main__':
    main()