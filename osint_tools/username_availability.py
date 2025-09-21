# Copyright (c) 2025 pxwild. All rights reserved.
# This software and its source code are proprietary and confidential.
# Unauthorized copying, modification, or distribution of this software,
# via any medium, is strictly prohibited without prior written permission.

import requests

SITES = {
    "GitHub": "https://github.com/{}",
    "Twitter": "https://twitter.com/{}",
    "Instagram": "https://instagram.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "TikTok": "https://www.tiktok.com/@{}",
}

def exists(url: str) -> bool:
    try:
        r = requests.head(url, timeout=7, allow_redirects=True, headers={"User-Agent":"Mozilla/5.0"})
        if r.status_code == 200:
            return True
        if r.status_code in (301,302,303,307,308,401,403):
            return True 
        return False
    except Exception:
        return False

def main():
    u = input("Username to check availability: ").strip()
    if not u:
        print("No username."); return
    available, taken = [], []
    for name,tpl in SITES.items():
        url = tpl.format(u)
        if exists(url):
            taken.append((name, url))
        else:
            available.append(name)
    if available:
        print("Appears AVAILABLE on:")
        for n in available: print(" -", n)
    else:
        print("No obvious availability detected on the checked platforms.")

    if taken:
        print("\nAlready taken on:")
        for n, url in taken: print(f" - {n}: {url}")

if __name__ == "__main__":
    main()

