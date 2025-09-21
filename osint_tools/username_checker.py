# Copyright (c) 2025 pxwild. All rights reserved.
# This software and its source code are proprietary and confidential.
# Unauthorized copying, modification, or distribution of this software,
# via any medium, is strictly prohibited without prior written permission.

import requests

SITES = {
    "GitHub": "https://github.com/{}",
    "Twitter": "https://twitter.com/{}",
    "Instagram": "https://instagram.com/{}",
    "Reddit": "https://reddit.com/user/{}",
    "Facebook": "https://www.facebook.com/{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "YouTube": "https://www.youtube.com/@{}",
    "LinkedIn": "https://www.linkedin.com/in/{}",
    "Pinterest": "https://www.pinterest.com/{}",
    "Twitch": "https://www.twitch.tv/{}",
}

def main():
    u = input("Username: ").strip()
    for name, tpl in SITES.items():
        url = tpl.format(u)
        try:
            r = requests.head(url, timeout=5, allow_redirects=True)
            if r.status_code == 200:
                status = "Taken"
            elif r.status_code == 404:
                status = "Available"
            else:
                status = f"Unknown ({r.status_code})"
            print(f"{name:<10}: {status:<10} {url}")
        except Exception as e:
            print(f"{name:<10}: Error - {e}")

if __name__ == "__main__":
    main()

