import re, requests

MAC_RE = re.compile(r"^[0-9A-Fa-f]{2}([:\-]?[0-9A-Fa-f]{2}){5}$")

def normalize(mac: str) -> str:
    return re.sub(r"[^0-9A-Fa-f]", "", mac).upper()

def pretty(mac: str) -> str:
    n = normalize(mac)
    return ":".join([n[i:i+2] for i in range(0,len(n),2)])

def main():
    mac = input("MAC (any common format): ").strip()
    if not MAC_RE.match(mac):
        print("Invalid MAC format."); return
    try:
        r = requests.get(f"https://api.macvendors.com/{mac}", timeout=10)
        if r.status_code == 200:
            print("MAC:", pretty(mac))
            print("Vendor:", r.text.strip() or "Unknown")
        elif r.status_code == 404:
            print("Vendor not found for:", pretty(mac))
        else:
            print("Lookup error:", r.status_code, r.text[:200])
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
