# Copyright (c) 2025 pxwild. All rights reserved.
# This software and its source code are proprietary and confidential.
# Unauthorized copying, modification, or distribution of this software,
# via any medium, is strictly prohibited without prior written permission.

import requests
from bs4 import BeautifulSoup

def main():
    url = input("URL: ").strip()
    if not url.startswith("http"): url = "https://" + url
    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        links = {a.get("href") for a in soup.find_all("a", href=True)}
        for l in sorted(links): print(l)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

