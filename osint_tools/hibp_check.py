import os, requests

def main():
    email = input("Email: ").strip()
    key = os.getenv("HIBP_API_KEY")
    if not key: 
        print("Set HIBP_API_KEY as env variable."); return
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {"hibp-api-key": key, "User-Agent": "osint-tool"}
    try:
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 404:
            print("No breaches found.")
        elif r.status_code == 200:
            for b in r.json():
                print("-", b.get("Name"), b.get("BreachDate"))
        else:
            print("Error:", r.status_code, r.text[:200])
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
