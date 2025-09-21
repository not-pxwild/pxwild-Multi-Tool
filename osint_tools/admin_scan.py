import requests

PATHS = ["/admin","/administrator","/login","/wp-admin","/cpanel","/dashboard"]

def main():
    d = input("Domain (example.com): ").strip()
    for base in [f"http://{d}", f"https://{d}"]:
        for p in PATHS:
            url = base+p
            try:
                r = requests.head(url, timeout=5, allow_redirects=True)
                if r.status_code in (200,301,302,401,403):
                    print("Found:", url, "->", r.status_code)
            except: pass

if __name__ == "__main__":
    main()
