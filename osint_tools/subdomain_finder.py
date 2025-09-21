# Copyright (c) 2025 pxwild. All rights reserved.
# This software and its source code are proprietary and confidential.
# Unauthorized copying, modification, or distribution of this software,
# via any medium, is strictly prohibited without prior written permission.

import requests

def main():
    d = input("Domain: ").strip()
    url = f"https://crt.sh/?q=%25.{d}&output=json"
    try:
        r = requests.get(url, timeout=10)
        subs = {e["name_value"].replace("*.","") for e in r.json() if "name_value" in e}
        for s in sorted(subs): print(s)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

