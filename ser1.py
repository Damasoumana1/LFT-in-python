import socket
import os
import requests

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def send_file(client_socket, file_path):
    
    file_size = os.path.getsize(file_path)
      # Envoi de la taille du fichier
    print(file_path)
    
    with open(".\\folder\\Dama.jpg", 'rb') as file:
        chunk = file.read(1024)
        print(chunk)
        client_socket.send(chunk)
        # while chunk:
        #     client_socket.send(chunk)  # Envoi du fichier par morceaux
        #     chunk = file.read(1024)
        # send_file(client_socket, file_path)
    # client_socket.send("no".encode('utf-8')) 

def handle_client(client_socket, complet_path):
    files = os.listdir(complet_path)  # Récupération de la liste des fichiers dans le répertoire courant
    file_list = '\n'.join(files)  # Conversion de la liste en une chaîne de caractères
    client_socket.send(file_list.encode('utf-8'))  # Envoi de la liste des fichiers au client
    file_name = client_socket.recv(1024).decode('utf-8')  # Réception du nom du fichier souhaité par le client
    print(file_name)
    
    
    
    if file_name in files:
        client_socket.send('OK'.encode('utf-8'))  # Envoi d'une confirmation au client
       
        if os.path.isfile(file_name) == False:
            
            print("sending ")
            client_socket.send('yes'.encode('utf-8'))
            file_path = os.path.join(complet_path, file_name)
        
            send_file(client_socket, file_path) 
            # Envoi du fichier au client
        elif os.path.isdir(file_name):
            handle_client(client_socket, os.path.join(complet_path, file_name))
            
        
    else:
        client_socket.send('ERROR'.encode('utf-8'))  # Envoi d'une erreur au client si le fichier n'existe pas
        client_socket.close()

def start_server():
    # server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.1.76', 1234))
    server_socket.listen(5)
    
    print("Le serveur est en écoute sur le port 1234...")

    while True:
        client_socket, address = server_socket.accept()
        print("Connexion établie avec", address[0], "sur le port", address[1])
        handle_client(client_socket, '.\\folder')

# Pour démarrer le serveur
start_server()
