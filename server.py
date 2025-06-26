import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_socket.bind(('0.0.0.0', 12345))
    server_socket.listen(1)
    print("The server has started. Waiting for connection...")
except socket.error as e:
    print(f"Socket error: {e}")

try:
    client_socket, address = server_socket.accept()
    print(f"Client has connected: {address}")
except socket.error as e:
    print(f"Socket error: {e}")

while True:
    msg = client_socket.recv(1024).decode()
    if msg.lower() == "exit":
        print ("Client left the chat")
        break
    print("Client: ", msg)
    reply = input("You: ")
    client_socket.send(reply.encode())

client_socket.close()
server_socket.close()
