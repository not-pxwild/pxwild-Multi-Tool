import requests, socket, json

def is_valid_ip(ip: str) -> bool:
    try:
        socket.inet_aton(ip);  return True
    except OSError:
        return False

def get_ip_info(ip: str):
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=6)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}

def main():
    ip = input("Enter IP: ").strip()
    if not is_valid_ip(ip):
        print("Invalid IP."); return
    data = get_ip_info(ip)
    print(json.dumps(data, indent=2))

if __name__ == "__main__":
    main()
