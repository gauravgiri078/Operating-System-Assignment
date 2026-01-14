import socket

# Create UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = "Hello from UDP Client!"
client_socket.sendto(message.encode(), ("127.0.0.1", 6000))

# Receive response
data, addr = client_socket.recvfrom(1024)
print("Received from server:", data.decode())

client_socket.close()
