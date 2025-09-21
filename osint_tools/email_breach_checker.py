# Copyright (c) 2025 pxwild. All rights reserved.
# This software and its source code are proprietary and confidential.
# Unauthorized copying, modification, or distribution of this software,
# via any medium, is strictly prohibited without prior written permission.

import os, requests

def main():
    e = input("Email: ").strip()
    key = os.getenv("HIBP_API_KEY")
    if not key: 
        print("Set HIBP_API_KEY."); return
    try:
        r = requests.get(f"https://haveibeenpwned.com/api/v3/breachedaccount/{e}",
                         headers={"hibp-api-key": key,"User-Agent":"osint"})
        if r.status_code==404: print("No breaches")
        elif r.status_code==200:
            for b in r.json(): print(b["Name"], "-", b["BreachDate"])
        else: print("Error:", r.status_code)
    except Exception as ex:
        print("Error:", ex)

if __name__ == "__main__":
    main()

