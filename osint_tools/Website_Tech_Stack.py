# Copyright (c) 2025 pxwild. All rights reserved.
# This software and its source code are proprietary and confidential.
# Unauthorized copying, modification, or distribution of this software,
# via any medium, is strictly prohibited without prior written permission.

import requests, re
from bs4 import BeautifulSoup

FINGERPRINTS = {
    "WordPress": r"wp-content|wp-includes",
    "Drupal": r"/sites/(default|all)/|drupal\.settings",
    "Joomla": r"/media/system/js/|/components/com_",
    "React": r"__NEXT_DATA__|react(\.production|\.)",
    "Angular": r"angular(\.min)?\.js",
    "Vue.js": r"vue(\.runtime)?(\.global)?(\.prod)?(\.min)?\.js",
    "jQuery": r"jquery(\.min)?\.js",
    "Bootstrap": r"bootstrap(\.min)?\.css",
}

def main():
    url = input("Website URL: ").strip()
    if not url:
        print("No URL."); return
    if not url.startswith(("http://","https://")):
        url = "https://" + url
    try:
        r = requests.get(url, timeout=12, headers={"User-Agent":"Mozilla/5.0"})
        found = set()
        xpb = r.headers.get("X-Powered-By")
        server = r.headers.get("Server")
        gen_hdr = r.headers.get("Generator")
        if server: found.add(f"Server: {server}")
        if xpb:    found.add(f"X-Powered-By: {xpb}")
        if gen_hdr:found.add(f"Generator (hdr): {gen_hdr}")

        text = r.text
        soup = BeautifulSoup(text, "html.parser")
        mg = soup.find("meta", attrs={"name":"generator"})
        if mg and mg.get("content"):
            found.add(f"Generator: {mg['content']}")

        for name, pat in FINGERPRINTS.items():
            if re.search(pat, text, re.I):
                found.add(name)

        if found:
            print("Detected:")
            for x in sorted(found): print(" -", x)
        else:
            print("No common tech detected (basic scan).")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

