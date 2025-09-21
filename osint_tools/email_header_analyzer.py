import re, sys
from email import policy
from email.parser import BytesParser

RE_IP = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")

def print_k(headers, key):
    v = headers.get_all(key)
    if v:
        if len(v) == 1: print(f"{key}: {v[0]}")
        else:
            print(f"{key}:")
            for x in v: print("  -", x)

def main():
    print("Paste raw email headers, then Ctrl+D (Unix) / Ctrl+Z Enter (Windows):")
    raw = sys.stdin.buffer.read()
    if not raw.strip():
        print("No input."); return

    msg = BytesParser(policy=policy.default).parsebytes(raw)
    hdrs = msg

    for k in ["From","To","Subject","Date","Message-ID","Return-Path"]:
        print_k(hdrs, k)

    rec = hdrs.get_all("Received") or []
    if rec:
        print("\nReceived chain (top->bottom):")
        for r in rec:
            line = " ".join(str(r).split())
            print(" -", line)
        last = str(rec[-1])
        ips = RE_IP.findall(last)
        if ips: print("Originating IP (guess):", ips[-1])

    auth = hdrs.get_all("Authentication-Results") or []
    if auth:
        print("\nAuthentication-Results:")
        for a in auth:
            s = str(a)
            print(" -", s)
            for mech in ("spf","dkim","dmarc"):
                m = re.search(rf"{mech}\s*=\s*([a-zA-Z]+)", s, re.I)
                if m:
                    print(f"   {mech.upper()}: {m.group(1)}")

if __name__ == "__main__":
    main()
