# Copyright (c) 2025 pxwild. All rights reserved.
# This software and its source code are proprietary and confidential.
# Unauthorized copying, modification, or distribution of this software,
# via any medium, is strictly prohibited without prior written permission.

import requests, socket, json

def is_valid_ip(ip: str) -> bool:
    try: socket.inet_aton(ip); return True
    except OSError: return False

def main():
    ip = input("IP: ").strip()
    if not is_valid_ip(ip):
        print("Invalid IP."); return
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=6)
        r.raise_for_status()
        data = r.json()
        if data.get("status") != "success":
            print("Lookup failed:", data.get("message","unknown")); return
        out = {
            "ip": ip,
            "country": data.get("country"),
            "region": data.get("regionName"),
            "city": data.get("city"),
            "lat": data.get("lat"),
            "lon": data.get("lon"),
            "timezone": data.get("timezone"),
            "isp": data.get("isp")
        }
        print(json.dumps(out, indent=2))
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

