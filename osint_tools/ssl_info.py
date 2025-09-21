import ssl, socket
from datetime import datetime

def main():
    host = input("Domain (no scheme): ").strip()
    if not host:
        print("No domain provided."); return
    try:
        ctx = ssl.create_default_context()
        with socket.create_connection((host, 443), timeout=10) as sock:
            with ctx.wrap_socket(sock, server_hostname=host) as ssock:
                cert = ssock.getpeercert()
        subject = dict(x[0] for x in cert.get("subject", []))
        issuer  = dict(x[0] for x in cert.get("issuer", []))
        not_before = cert.get("notBefore")
        not_after  = cert.get("notAfter")

        print("Domain:", host)
        print("Issued To:", subject.get("commonName"))
        print("Issued By:", issuer.get("commonName"))
        print("Valid From:", not_before)
        print("Valid To  :", not_after)

        if not_after:
            try:
                exp = datetime.strptime(not_after, "%b %d %H:%M:%S %Y %Z")
                days = (exp - datetime.utcnow()).days
                if days < 0:
                    print("⚠️  Certificate has EXPIRED.")
                else:
                    print(f"✅ Certificate valid. Days until expiry: {days}")
            except Exception:
                pass

        san = [v for ((k,_), v) in cert.get("subjectAltName", []) if k == "DNS"]
        if san:
            print("Subject Alt Names:")
            for s in san[:50]:
                print(" -", s)
            if len(san) > 50:
                print(f" ... (+{len(san)-50} more)")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
