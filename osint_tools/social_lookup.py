import requests
from bs4 import BeautifulSoup

def main():
    url = input("Profile URL (e.g., https://twitter.com/username): ").strip()
    if not url:
        print("No URL provided."); return
    if not url.startswith(("http://","https://")):
        url = "https://" + url
    try:
        r = requests.get(url, timeout=12, headers={"User-Agent":"Mozilla/5.0"})
        print("HTTP:", r.status_code)
        soup = BeautifulSoup(r.text, "html.parser")
        title = soup.title.string.strip() if soup.title and soup.title.string else "-"
        desc_tag = soup.find("meta", attrs={"name":"description"}) or soup.find("meta", attrs={"property":"og:description"})
        desc = (desc_tag.get("content") or "").strip() if desc_tag else "-"
        print("Title:", title)
        print("Description:", desc[:400] if desc != "-" else "-")
        text = soup.get_text(" ").strip()
        if text:
            print("\nSnippet:")
            print(text[:800])
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
