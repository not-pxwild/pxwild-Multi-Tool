# Copyright (c) 2025 pxwild. All rights reserved.
# This software and its source code are proprietary and confidential.
# Unauthorized copying, modification, or distribution of this software,
# via any medium, is strictly prohibited without prior written permission.

import whois
from datetime import datetime

def fmt(v):
    if isinstance(v, list): v=v[0]
    if isinstance(v, datetime): return v.isoformat()
    return str(v)

def main():
    d = input("Domain: ").strip()
    try:
        info = whois.whois(d)
        for k,v in info.items():
            print(k, ":", fmt(v))
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

