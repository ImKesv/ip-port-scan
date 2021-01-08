"""
BETA VERS
l0l
"""

import os
try:
    import socket
    import concurrent.futures
    import colorama
    import threading
    from colorama import Fore
    import time

except:
    os.system('pip install colorama')
colorama.init()

os.system('cls & color 3 & title [BETA] Port Scan Only Ip By Kevin')
print("""Port Scanner lol By Kevin/Kesv
Only Enter IP!
Scanning Web Direct Comming SOon!""")

print_lock = threading.Lock()
# enter ip woi
ip = input("[!] Masukkan Ip: ")

def scan(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # udp dan tcp network

    scanner.settimeout(1)
    try:
        scanner.connect((ip, port))
        scanner.close()
        with print_lock:
            print(Fore.WHITE + f"[{port}]" + Fore.GREEN + " Port Terdeteksi!")
    except:
        pass

with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as execute:
    for port in range(1000):
        time.sleep(0.00000000000000000000000001)
        execute.submit(scan, ip, port + 1)
