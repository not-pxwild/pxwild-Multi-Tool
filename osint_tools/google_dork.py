# Copyright (c) 2025 pxwild. All rights reserved.
# This software and its source code are proprietary and confidential.
# Unauthorized copying, modification, or distribution of this software,
# via any medium, is strictly prohibited without prior written permission.

from googlesearch import search

def main():
    q = input("Google Dork query: ").strip()
    try:
        for url in search(q, num_results=10):
            print(url)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

