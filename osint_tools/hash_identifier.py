import hashlib, os, re

LENGTH_MAP = {
    32:  ["MD5", "NTLM/MD4 (also 32 hex)"],
    40:  ["SHA1"],
    56:  ["SHA224"],
    64:  ["SHA256"],
    96:  ["SHA384"],
    128: ["SHA512"],
    24:  ["CRC-96 / Base64-encoded 16 bytes?"],
}

def guess_hash_type(h: str):
    hx = h.strip()
    if re.fullmatch(r"[A-Fa-f0-9]+", hx or " "):
        cand = LENGTH_MAP.get(len(hx), ["Unknown"])
        print(f"Length: {len(hx)}  Possible: {', '.join(cand)}")
    elif re.fullmatch(r"[A-Za-z0-9+/=]+", hx):
        print("Looks like Base64 (not a hash).")
    else:
        print("Unrecognized format.")

def print_hashes(data: bytes):
    print("MD5   :", hashlib.md5(data).hexdigest())
    print("SHA1  :", hashlib.sha1(data).hexdigest())
    print("SHA256:", hashlib.sha256(data).hexdigest())
    print("SHA512:", hashlib.sha512(data).hexdigest())

def main():
    mode = input("Mode: (g)uess hash type, (s)tring hash, (f)ile hash: ").strip().lower()
    if mode == "g":
        h = input("Enter hash: ")
        guess_hash_type(h)
    elif mode == "s":
        s = input("String: ").encode("utf-8")
        print_hashes(s)
    elif mode == "f":
        p = input("File path: ").strip()
        if not os.path.isfile(p):
            print("File not found."); return
        with open(p,"rb") as f:
            print_hashes(f.read())
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()
