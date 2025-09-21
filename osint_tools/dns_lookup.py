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
