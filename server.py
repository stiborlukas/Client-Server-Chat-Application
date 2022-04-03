import socket
import threading
import logging


# sending msg to all
def broadcast(msg, client, nickname):
    # deleting \n
    nick = nickname.strip()
    msg_temp = msg.strip()

    # msg
    message = f"{nick} {msg_temp}\n"
    message = message.encode('utf-8')

    # sending
    for client in clients:
        client.send(message)


# receiving from clients
def handle(client, nickname, clients, nicknames):
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            msg = msg.strip()
            print(msg)

            # getting all users
            if msg == "?users?":
                online = f"List of online users requested by {nickname}"
                online = online.encode('utf-8')
                for client in clients:
                    client.send(online)
                    for nickname in nicknames:
                        mess = nickname.translate({ord(':'): None})
                        mess = mess.encode('utf-8')
                        client.send(mess)

            else:
                if len(msg) == 0:
                    print("prazdny")
                else:
                    print(len(msg))
                    broadcast(msg, client, nickname)

        except Exception as e:
            print(e)
            logging.error(e)
            clients.remove(client)
            nicknames.remove(nickname)
            print(clients)
            break


# basic connection
def receive():
    while True:
        try:
            client, address = serversocket.accept()

            # get name and socket
            client.send("NICK".encode('utf-8'))
            nickname = client.recv(1024).decode("utf-8")
            clients.append(client)
            nicknames.append(nickname)
            print(clients)

            print(f"connected with {str(address)}!")

            # first msg to user after connection and start receiving msg
            client.send("connected to the server\nview online users by typing '?users?'\n".encode('utf-8'))
            thread = threading.Thread(target=handle, args=(client, nickname, clients, nicknames,))
            thread.start()
        except Exception as e:
            logging.error(e)


# logging setup
logging.basicConfig(filename='server_logs.log', filemode='w', format='%(asctime)s : %(message)s',datefmt='[%d/%m/%Y] %H:%M:%S' ,level=logging.DEBUG)

# declaring variables
host = "127.0.0.1"
port = 9090
clients = []
nicknames = []


# socket connection
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((host, port))
serversocket.listen()

print(f"server running")

# start program
receive()