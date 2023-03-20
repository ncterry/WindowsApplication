#Check if a network port is open:
import socket

host = "localhost"
port = 80

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((host, port))
    except ConnectionRefusedError:
        print(f"Port {port} on {host} is closed.")
    else:
        print(f"Port {port} on {host} is open.")

        
        
