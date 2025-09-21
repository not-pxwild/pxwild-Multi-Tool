import os, json
try:
    from exif import Image as ExifImage
except Exception:
    ExifImage = None

def main():
    p = input("File path: ").strip()
    if not os.path.isfile(p):
        print("File not found."); return
    if ExifImage is None:
        print("Install 'exif' package: pip install exif"); return
    try:
        with open(p, "rb") as f:
            img = ExifImage(f)
            if not img.has_exif:
                print("No EXIF metadata found."); return
            data = img.get_all()
            for k,v in data.items(): print(f"{k}: {v}")
            out = os.path.splitext(os.path.basename(p))[0] + "_metadata.json"
            with open(out, "w") as jf:
                json.dump(data, jf, indent=2, default=str)
            print(f"Saved JSON to {out}")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
