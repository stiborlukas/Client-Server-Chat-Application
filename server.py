import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host = socket.gethostname()
host = "127.0.0.1"
port = 2205


serversocket.bind((host, port))

while True:
    serversocket.listen()
    clientsocket, addr = serversocket.accept()
    clientsocket.sendall(b'Hello world!')
    dataFromServer = clientsocket.recv(1024)
    print(dataFromServer)
    # clientsocket.sendall(dataFromServer)
    clientsocket.close()
