# Uma pequena verificacao de usuarios smtp em python! 

import socket
import sys

if len(sys.argv) <= 3:
    print("Modo de uso incorreto: Utilize os tres argumentos: python3 smtenum.py <IP> <PORTA> <USUARIO>")

else:
    ip = (sys.argv[1])
    porta = int(sys.argv[2])
    usuario = sys.argv[3]

    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.connect((f"{ip}", porta))
    banner = tcp.recv(1024)
    print(banner)

    tcp.send(f"VRFY {usuario} \r\n".encode())
    user = tcp.recv(1024)
    print(user)