import socket
import threading

host = "127.0.0.1"
# host = socket.gethostname()
# port = 2205
port = 9090

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((host, port))

serversocket.listen()

clients = []
# nicknames = []


def broadcast(msg, client, nickname):
    # ano = msg
    # # print("gfhjfgdhj")
    # anoan
    # zprava = msg
    # print(zprava)
    # print(f"{nickname} says {msg}")
    message = f"{nickname} {msg}"
    # print(message)

    # message = msg.encode('utf-8')
    message = message.encode('utf-8')
    # client.send(message)
    # client.sendall(msg)
    for client in clients:
        client.send(message)


def handle(client, nickname):
    while True:
        msg = client.recv(1024).decode('utf-8')
        # print(msg)
        if msg:
            broadcast(msg, client, nickname)


def receive():
    while True:
        client, address = serversocket.accept()
        # print(f"{client} nazdar")
        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024).decode("utf-8")
        clients.append(client)
        # print(nickname)

        print(f"connected with {str(address)}!")
        client.send("connected to the server".encode('utf-8'))
        thread = threading.Thread(target=handle, args=(client, nickname,))
        thread.start()


print(f"server running")
receive()
