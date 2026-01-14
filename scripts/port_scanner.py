import socket

target = input("Target IP: ")
ports = [21, 22, 80, 443, 445]

print(f"\nScanning {target}...\n")

for port in ports:
    s = socket.socket()
    s.settimeout(1)
    if s.connect_ex((target, port)) == 0:
        print(f"[+] Port {port} is open")
    s.close()
