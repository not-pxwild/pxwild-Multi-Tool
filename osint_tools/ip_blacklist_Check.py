# Copyright (c) 2025 pxwild. All rights reserved.
# This software and its source code are proprietary and confidential.
# Unauthorized copying, modification, or distribution of this software,
# via any medium, is strictly prohibited without prior written permission.

import socket, os, requests

DNSBLS = [
    "zen.spamhaus.org",
    "bl.spamcop.net",
    "dnsbl.sorbs.net",
]

def reverse_ip(ip: str) -> str:
    return ".".join(reversed(ip.split(".")))

def listed_in_dnsbl(ip: str):
    rip = reverse_ip(ip)
    hits = []
    for zone in DNSBLS:
        q = f"{rip}.{zone}"
        try:
            socket.gethostbyname(q) 
            hits.append(zone)
        except socket.gaierror:
            pass
    return hits

def abuseipdb_check(ip: str, key: str):
    try:
        r = requests.get("https://api.abuseipdb.com/api/v2/check",
                         params={"ipAddress": ip},
                         headers={"Key": key, "Accept":"application/json"},
                         timeout=10)
        if r.status_code == 200:
            d = r.json().get("data", {})
            return {
                "abuseConfidenceScore": d.get("abuseConfidenceScore"),
                "countryCode": d.get("countryCode"),
                "lastReportedAt": d.get("lastReportedAt")
            }
        return {"error": f"{r.status_code} {r.text[:200]}"}
    except Exception as e:
        return {"error": str(e)}

def main():
    ip = input("IP (IPv4): ").strip()
    if not ip or len(ip.split(".")) != 4:
        print("Invalid IPv4."); return
    print("Checking DNSBLs...")
    hits = listed_in_dnsbl(ip)
    if hits:
        print("Listed on:")
        for h in hits: print(" -", h)
    else:
        print("Not listed on checked DNSBLs.")

    key = os.getenv("ABUSEIPDB_API_KEY")
    if key:
        print("\nAbuseIPDB:")
        info = abuseipdb_check(ip, key)
        if "error" in info:
            print(" API error:", info["error"])
        else:
            print(" Abuse Score:", info.get("abuseConfidenceScore"))
            print(" Country:", info.get("countryCode"))
            print(" Last Reported:", info.get("lastReportedAt"))
    else:
        print("\n(ABUSEIPDB_API_KEY not set; skipping AbuseIPDB)")

if __name__ == "__main__":
    main()

