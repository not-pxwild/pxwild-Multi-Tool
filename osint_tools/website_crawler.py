# Copyright (c) 2025 pxwild. All rights reserved.
# This software and its source code are proprietary and confidential.
# Unauthorized copying, modification, or distribution of this software,
# via any medium, is strictly prohibited without prior written permission.

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque

def main():
    start = input("Start URL: ").strip()
    seen, q = {start}, deque([start])
    while q and len(seen) < 50:
        url = q.popleft()
        try:
            r = requests.get(url, timeout=6)
            print("Visited:", url)
            soup = BeautifulSoup(r.text, "html.parser")
            for a in soup.find_all("a", href=True):
                nxt = urljoin(url, a["href"])
                if urlparse(nxt).netloc == urlparse(start).netloc and nxt not in seen:
                    seen.add(nxt); q.append(nxt)
        except: pass

if __name__ == "__main__":
    main()

