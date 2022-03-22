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

# ----------------------------------------------
import socket
import threading

# host = "127.0.0.1"
host = socket.gethostname()
port = 2205
# port = 9090

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((host, port))

serversocket.listen()

clients = []
nicknames = []


def broadcast(msg, client):
    # ano = msg
    # # print("gfhjfgdhj")
    print(msg)
    client.send(msg)
    # client.sendall(msg)


def handle(client):
    while True:
        msg = client.recv(1024)
        if msg:
            broadcast(msg, client)


def receive():
    while True:
        client, address = serversocket.accept()
        print(f"connected with {str(address)}!")
        client.send("connected to the server".encode('utf-8'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print(f"server running")
receive()







