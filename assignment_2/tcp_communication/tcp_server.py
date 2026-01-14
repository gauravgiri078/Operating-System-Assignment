import socket

# Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind server to localhost and port
server_socket.bind(("127.0.0.1", 5000))

# Listen for incoming connections
server_socket.listen(1)
print("TCP Server is listening on port 5000...")

# Accept client connection
conn, addr = server_socket.accept()
print(f"Connected to client: {addr}")

# Receive data from client
data = conn.recv(1024).decode()
print("Received from client:", data)

# Send response back to client
response = "Hello from TCP Server!"
conn.send(response.encode())

# Close connection
conn.close()
server_socket.close()
