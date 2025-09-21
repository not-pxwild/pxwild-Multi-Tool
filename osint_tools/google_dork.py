from googlesearch import search

def main():
    q = input("Google Dork query: ").strip()
    try:
        for url in search(q, num_results=10):
            print(url)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
