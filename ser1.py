import socket
import os

# Define the server's IP address and port
server_ip = '127.0.0.1'
server_port = 3000

# Define the server folder where files are stored
server_folder = 'folder'

# Function to list files in the server folder
def list_files():
    files = os.listdir(server_folder)
    return files

# Function to handle file downloads
def send_file(client_socket, filename):
    file_path = os.path.join(server_folder, filename)
    
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            data = file.read(1024)
            while data:
                client_socket.send(data)
                data = file.read(1024)
    else:
        client_socket.send(b'File not found')

# Create a socket and bind it to the server address
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(5)
print(f"Server is listening on {server_ip}:{server_port}")

while True:
    # Accept incoming connections
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    # Receive client request
    request = client_socket.recv(1024).decode("utf-8")
    print(request)
    if request == 'LIST':
        # List files in the server folder
        files = list_files()
        file_list = "\n".join(files)
        client_socket.send(file_list.encode())
    elif request.startswith('GET'):
        # Extract filename from the request
        filename = request.split(' ')[1]
        
        # Send the requested file to the client
        send_file(client_socket, filename)

    # Close the client socket
    client_socket.close()
