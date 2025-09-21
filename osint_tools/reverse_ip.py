import requests

def main():
    ip = input("IP: ").strip()
    try:
        r = requests.get(f"https://api.hackertarget.com/reverseiplookup/?q={ip}", timeout=10)
        txt = r.text.strip()
        if "error" in txt.lower():
            print("Lookup error:", txt)
        else:
            print(txt)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
