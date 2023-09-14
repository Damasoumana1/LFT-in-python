import socket

# Define the server's IP address and port
server_ip = '127.0.0.1'
server_port = 3000




while True:
    print("Menu:")
    print("1. List files on server")
    print("2. Download a file")
    print("3. Quit")
    choice = input("Enter your choice: ")
    # Create a socket and connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    if choice == '1':
        # Request to list files
        client_socket.send('LIST'.encode())
        files = client_socket.recv(1024).decode("utf-8")
        print("Files on server:\n", files)
    elif choice == '2':
        # Request to download a file
        filename = input("Enter the filename to download: ")
        client_socket.send(f'GET {filename}'.encode())
        data = client_socket.recv(1024)
        if data == b'File not found':
            print("File not found on the server.")
        else:
            with open(filename, 'wb') as file:
                 while data:
                    file.write(data)
                    data = client_socket.recv(1024)
            print(f"{filename} downloaded successfully.")
    elif choice == '3':
        break
    else:
        print("Invalid choice")
    client_socket.close()
# Close the client socket

