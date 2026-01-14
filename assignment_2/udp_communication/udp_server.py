import socket

# Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to localhost and port
server_socket.bind(("127.0.0.1", 6000))

print("UDP Server is running on port 6000...")

# Receive message
data, addr = server_socket.recvfrom(1024)
print("Received from client:", data.decode())

# Send response
server_socket.sendto("Hello from UDP Server!".encode(), addr)

server_socket.close()
