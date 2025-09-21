import requests
from bs4 import BeautifulSoup
import urllib.parse

def main():
    query = input("Dark web search query: ").strip()
    if not query:
        print("No query."); return
    url = "https://ahmia.fi/search/?q=" + urllib.parse.quote(query)
    try:
        r = requests.get(url, timeout=15, headers={"User-Agent":"Mozilla/5.0"})
        if r.status_code != 200:
            print("Ahmia error:", r.status_code); return
        soup = BeautifulSoup(r.text, "html.parser")
        links = []
        for a in soup.find_all("a", href=True):
            href = a["href"]
            if ".onion" in href:
                links.append(href)
        links = sorted(set(links))
        if not links:
            print("No .onion links found (Ahmia).")
        else:
            print("Use Tor Browser to open these links:")
            for l in links:
                print("-", l)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
