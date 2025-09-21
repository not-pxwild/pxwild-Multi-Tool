# Copyright (c) 2025 pxwild. All rights reserved.
# This software and its source code are proprietary and confidential.
# Unauthorized copying, modification, or distribution of this software,
# via any medium, is strictly prohibited without prior written permission.

import os, requests, json

def securitytrails_history(domain: str, key: str):
    url = f"https://api.securitytrails.com/v1/history/{domain}/dns/a"
    try:
        r = requests.get(url, headers={"APIKEY": key}, timeout=12)
        if r.status_code == 200:
            return r.json()
        return {"error": f"{r.status_code}: {r.text[:200]}"}
    except Exception as e:
        return {"error": str(e)}

def fallback_current(domain: str):
    try:
        r = requests.get(f"https://api.hackertarget.com/hostsearch/?q={domain}", timeout=10)
        return {"current": r.text.strip()}
    except Exception as e:
        return {"error": str(e)}

def main():
    d = input("Domain: ").strip()
    key = os.getenv("SECURITYTRAILS_API_KEY")
    if key:
        data = securitytrails_history(d, key)
        if "error" in data:
            print("SecurityTrails error:", data["error"])
        else:
            print("Historical A records (SecurityTrails):")
            records = data.get("records", [])
            if not records:
                print("No historical records found.")
            else:
                for rec in records:
                    rr = rec.get("rrdata") or []
                    first = rec.get("first_seen")
                    last  = rec.get("last_seen")
                    for ip in rr:
                        print(f"- {ip}  (first_seen: {first}, last_seen: {last})")
    else:
        print("SECURITYTRAILS_API_KEY not set -> showing current host records only.")
        cur = fallback_current(d)
        if "error" in cur:
            print("Error:", cur["error"])
        else:
            print(cur["current"])

if __name__ == "__main__":
    main()

