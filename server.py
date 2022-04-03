import socket
import threading
import logging
# import pickle


# odesilani vsem klientum
def broadcast(msg, client, nickname):
    # zbaveni se \n
    nick = nickname.strip()
    msg_temp = msg.strip()

    # zprava kterou poslu
    message = f"{nick} {msg_temp}\n"
    message = message.encode('utf-8')

    # poslani vsem klientum
    for client in clients:
        client.send(message)


# prijimani zprav od klientu
def handle(client, nickname, clients, nicknames):
    while True:
        print("ano")
        try:
            # print("ne")
            msg = client.recv(1024).decode('utf-8')
            msg = msg.strip()
            print(msg)
            if msg == "killprogram":
                clients.remove(client)
                print(clients)
            if msg == "?users?":
                # print(nicknames)
                # print("safidkshiuaghfduhbnudfghuisdfg")
                online = f"List of online users requested by {nickname}"
                online = online.encode('utf-8')
                for client in clients:
                    client.send(online)
                    for nickname in nicknames:
                        mess = nickname.translate({ord(':'): None})
                        # mess = f"{online}{mess}"
                        mess = mess.encode('utf-8')
                        client.send(mess)

            else:
                print("mozna")
                broadcast(msg, client, nickname)
        except Exception as e:
            print(e)
            logging.error(e)
            # for client in clients:
            #     clients.remove(client)
            clients.remove(client)
            nicknames.remove(nickname)
            # error = "error :(".encode('utf-8')
            # client.send(error)
            print(clients)
            break


# zakladni pripojeni
def receive():
    while True:
        try:
            client, address = serversocket.accept()

            # zeptat se na jmeno, pridat ho do listu
            client.send("NICK".encode('utf-8'))
            nickname = client.recv(1024).decode("utf-8")
            clients.append(client)
            nicknames.append(nickname)
            print(clients)

            print(f"connected with {str(address)}!")

            # dat mu vedet ze pripojeny, spustit prijimani zprav
            client.send("connected to the server\nview online users by typing '?users?'\n".encode('utf-8'))
            thread = threading.Thread(target=handle, args=(client, nickname, clients, nicknames,))
            thread.start()
        except Exception as e:
            logging.error(e)


# logging setup
logging.basicConfig(filename='server_logs.log', filemode='w', format='%(asctime)s : %(message)s',datefmt='[%d/%m/%Y] %H:%M:%S' ,level=logging.DEBUG)

# nastaveni promennych
host = "127.0.0.1"
# host = socket.gethostname()
# port = 2205
port = 9090
clients = []
nicknames = []


# nastaveni pripojeni
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((host, port))

serversocket.listen()


print(f"server running")

# spusteni
receive()