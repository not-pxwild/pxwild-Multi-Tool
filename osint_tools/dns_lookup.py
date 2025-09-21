# Copyright (c) 2025 pxwild. All rights reserved.
# This software and its source code are proprietary and confidential.
# Unauthorized copying, modification, or distribution of this software,
# via any medium, is strictly prohibited without prior written permission.

import requests

def main():
    d = input("Domain: ").strip()
    try:
        r = requests.get(f"https://api.hackertarget.com/dnslookup/?q={d}", timeout=10)
        print(r.text)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

