
import socket
import threading
import requests
import os


def start_client():
        isDownloading = False
        try:
                
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket.connect(('192.168.1.76', 1234))
                print("Connecté au serveur sur le port 1234...")

                while True:
                        # message = input("Message du client : ")
                        # client_socket.send(message.encode('utf8'))
                        response = client_socket.recv(1024).decode('ISO-8859-1')
                        if response=="yes":
                                isDownloading = True
                        elif response=="no":
                                isDownloading = False
                        print(isDownloading)
                #         if isDownloading:
                #                 print("dow")
                #                 f = open(".\\test.jpg",'xb') # Open in binary
                #                 l = client_socket.recv(1024)
                #                 while (l):
                #                         f.write(l)
                #                         l = client_socket.recv(1024)
                #                 f.close()

                #         else:
                #                 print("Réponse du serveur \n", response)
                #                 message = input("Message du client : ")
                #                 client_socket.send(message.encode('utf-8'))
                        print("Réponse du serveur \n", response)
                        message = input("Message du client : ")
                        client_socket.send(message.encode('utf-8'))       
                
        except Exception as e:
                print(e) 
        finally:
                client_socket.close()       

        
# def afficher_contenu_dossier(response):
#         contenu = os.listdir(response)
#         for element in contenu:
#             chemin = os.path.join(response, element)
#         if os.path.isdir(chemin):
#             print("response :", element)
#         else:
#             print("Fichier :", element)
#             response = "FILE-TRANSFERT-MAIN/file.txt"
#         afficher_contenu_dossier(response)


        # url = 'https://www.example.com/file.txt'
        # response = requests.get(url)
        # with open('file.txt', 'wb') as file:
        #     file.write(response.content)
        
        

    
# Pour démarrer le client
start_client()



