import socket

# Create TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect(("127.0.0.1", 5000))

# Send message to server
message = "Hello from TCP Client!"
client_socket.send(message.encode())

# Receive response from server
response = client_socket.recv(1024).decode()
print("Received from server:", response)

# Close connection
client_socket.close()
