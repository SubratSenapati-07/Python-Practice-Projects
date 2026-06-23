import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to all interfaces on port 8080
server_socket.bind(("0.0.0.0", 8080))

# Start listening
server_socket.listen(1)
print("Server is running... Waiting for a request...")

while True:
    client_socket, address = server_socket.accept()
    print("Got a request!")
    
    # Send a simple HTTP response
    response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nHello from Raspberry Pi!"
    client_socket.send(response.encode())
    
    client_socket.close()
