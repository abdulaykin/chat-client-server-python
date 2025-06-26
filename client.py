import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_ip = ('127.0.0.1')
port = 12345

try:
    client_socket.connect((server_ip, port))
    print("Connected to the server. To exit the chat press exit")
except socket.error as e:
    print(f"Error socket: {e}")

while True:
    message = input("You: ")
    client_socket.send(message.encode())
    if message.lower() == "exit":
        break
    reply = client_socket.recv(1024).decode()
    print("Server: ", reply)

client_socket.close()
