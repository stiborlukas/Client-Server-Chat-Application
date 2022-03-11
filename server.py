# ----------------------------------------skola
# import socket
#
# serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # host = socket.gethostname()
# host = "127.0.0.1"
# port = 2205
#
#
# serversocket.bind((host, port))
#
# while True:
#     serversocket.listen()
#     clientsocket, addr = serversocket.accept()
#     clientsocket.sendall(b'Hello world!')
#     dataFromServer = clientsocket.recv(1024)
#     print(dataFromServer)
#     # clientsocket.sendall(dataFromServer)
#     clientsocket.close()
import socket
import threading

host = "127.0.0.1"
# port = 2205
port = 9090

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((host, port))

serversocket.listen()

clients = []
nicknames = []


def broadcast(msg):
    for client in clients:
        client.send(msg)


def handle(client):
    while True:
        try:
            msg = client.recv(1024)
            print(f"{nicknames[clients.index(client)]} says {msg}")
            broadcast(msg)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nicknames = nicknames[index]
            nicknames.remove(nickname)
            break


def receive():
    while True:
        client, address = serversocket.accept()
        print(f"connected with {str(address)}!")

        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024)

        nicknames.append(nickname)
        clients.append(client)

        print(f"nickname of client is {nickname}")
        broadcast(f"{nickname} connected to the server!".encode('utf-8'))
        client.send("connected to the server".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print(f"server running")
receive()







