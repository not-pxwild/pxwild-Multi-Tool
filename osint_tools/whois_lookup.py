import whois
from datetime import datetime

def fmt(v):
    if isinstance(v, list): v=v[0]
    if isinstance(v, datetime): return v.isoformat()
    return str(v)

def main():
    d = input("Domain: ").strip()
    try:
        info = whois.whois(d)
        for k,v in info.items():
            print(k, ":", fmt(v))
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
