# Copyright (c) 2025 pxwild. All rights reserved.
# This software and its source code are proprietary and confidential.
# Unauthorized copying, modification, or distribution of this software,
# via any medium, is strictly prohibited without prior written permission.

import socket, threading, time

COMMON = [21,22,25,53,80,110,143,443,465,587,993,995,3306,3389,8080]

def scan_port(ip, port, timeout=1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.settimeout(timeout)
    try:
        if s.connect_ex((ip, port)) == 0:
            print(f"Port {port}: Open")
    finally:
        s.close()

def main():
    ip = input("Target IP: ").strip()
    rng = input("Port range (blank=common, e.g. 1-100): ").strip()
    if rng and "-" in rng:
        a,b = map(int, rng.split("-",1))
        ports = range(a, b+1)
    else:
        ports = COMMON
    t0 = time.time()
    threads = [threading.Thread(target=scan_port, args=(ip, p)) for p in ports]
    [t.start() for t in threads]; [t.join() for t in threads]
    print(f"Done in {time.time()-t0:.2f}s.")

if __name__ == "__main__":
    main()

