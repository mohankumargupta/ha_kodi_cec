import os
import socket
from time import sleep

xdg_runtime_dir = os.environ["XDG_RUNTIME_DIR"]
unix_socket_path = f"{xdg_runtime_dir}/ha_kodi.sock"
print(unix_socket_path)

if os.path.exists(unix_socket_path):
    os.remove(unix_socket_path)

server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server.bind(unix_socket_path)
server.listen(10)
connection, client_address = server.accept()
print("Client has connected")
message = "boo"
connection.send(message.encode("utf-8"))
sleep(2)
connection.close()
