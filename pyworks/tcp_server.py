# python3
# tcp_server.py - TCPを使ったデータ転送のテスト(server側)

import socket
from datetime import datetime

address = ("localhost", 6789)
max_size = 1000

print("Starting the server at", datetime.now())
print("Waiting for a client to call")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen(5)

client, addr = server.accept()
data = client.recv(max_size)

print(f"At {datetime.now()} {client} said {data}")
client.sendall(b"Are you talking to me?")
client.close()
server.close()