import requests, urllib.parse

def psbdmp_search(q: str):
    url = f"https://psbdmp.ws/api/search/{urllib.parse.quote(q)}"
    try:
        r = requests.get(url, timeout=12)
        if r.status_code == 200 and r.headers.get("Content-Type","").startswith("application/json"):
            return r.json()
        return {"error": f"{r.status_code}: {r.text[:200]}"}
    except Exception as e:
        return {"error": str(e)}

def main():
    q = input("Search term (email/keyword): ").strip()
    if not q:
        print("No query provided."); return
    data = psbdmp_search(q)
    if "error" not in data and isinstance(data, dict) and data.get("count"):
        results = data.get("data", [])
        print(f"Found {data.get('count')} results (showing up to 20):")
        for item in results[:20]:
            pid = item.get("id") or item.get("pasteid") or "unknown"
            src = item.get("source") or "pastebin"
            url = f"https://pastebin.com/{pid}" if src == "pastebin" else f"{src}/{pid}"
            print(f"- {url}")
    else:
        print("No API results or API unavailable.")
        print("Try manual metasearch: https://pastebin.ga/?q=" + urllib.parse.quote(q))

if __name__ == "__main__":
    main()
