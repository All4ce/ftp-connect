import socket

alvo = input("Digite o ip\n")

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((f"{alvo}",21))

banner = tcp.recv(1024)
print(banner)

usuario = input("Passe um nome de usuario: \n")
tcp.send(f"USER {usuario}\r\n".encode())
user = tcp.recv(1024)
print(user)

senha = input(f"Passe a senha do usuario {usuario} \n")
tcp.send(f"PASS {senha}\r\n".encode())
pw = tcp.recv(1024)
print(pw)