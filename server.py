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


def broadcast(msg, client, nickname):
    # ano = msg
    # # print("gfhjfgdhj")
    # print(msg)
    message = f"{nickname} says {msg}"
    client.send(message)
    # client.sendall(msg)


def handle(client, nickname):
    while True:
        msg = client.recv(1024)
        if msg:
            broadcast(msg, client, nickname)


def receive():
    while True:
        client, address = serversocket.accept()

        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024)
        # print(nickname)

        print(f"connected with {str(address)}!")
        client.send("connected to the server".encode('utf-8'))
        thread = threading.Thread(target=handle, args=(client, nickname,))
        thread.start()


print(f"server running")
receive()







