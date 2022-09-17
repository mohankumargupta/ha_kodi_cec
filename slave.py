import socket
import os

xdg_runtime_dir = os.environ["XDG_RUNTIME_DIR"]
unix_socket_path = f"{xdg_runtime_dir}/ha_kodi.sock"
print(unix_socket_path)

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
sock.connect(unix_socket_path)
data = sock.recv(16)
print(data)
sock.close()
