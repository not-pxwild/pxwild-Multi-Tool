# Copyright (c) 2025 pxwild. All rights reserved.
# This software and its source code are proprietary and confidential.
# Unauthorized copying, modification, or distribution of this software,
# via any medium, is strictly prohibited without prior written permission.

import os, re, requests

def sanitize_filename(url: str) -> str:
    name = re.sub(r"[^a-zA-Z0-9\-_.]", "_", url)
    return (name[:100] or "screenshot_alt") + ".png"

def main():
    url = input("Website (with or without http/https): ").strip()
    if not url:
        print("No URL provided."); return
    if not url.startswith(("http://","https://")):
        url = "https://" + url

    shot_url = f"https://image.thum.io/get/width/1440/crop/20000/{url}"
    try:
        r = requests.get(shot_url, timeout=40)
        if r.status_code != 200 or "image" not in r.headers.get("Content-Type","").lower():
            print("Alt screenshot service returned non-image or error. Status:", r.status_code)
            print("Body (first 200 chars):", r.text[:200])
            return
        out = sanitize_filename("alt_" + url.replace("https://","").replace("http://",""))
        with open(out, "wb") as f:
            f.write(r.content)
        print(f"Saved {out} ({len(r.content)} bytes)")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

