import socket
import threading
import logging


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
def handle(client, nickname, clients):
    while True:
        try:

            msg = client.recv(1024).decode('utf-8')
            print(msg)
            if msg:
                broadcast(msg, client, nickname)
        # except Exception as e:
        #     logging.error(e)
        except ConnectionResetError:
            print(f"{clients_connected[client_socket][0]} disconnected")

            for client in clients_connected:
                if client != client_socket:
                    client.send('notification'.encode())

                    data = pickle.dumps({'message': f"{clients_connected[client_socket][0]} left the chat",
                                         'id': clients_connected[client_socket][1], 'n_type': 'left'})

                    data_length_bytes = struct.pack('i', len(data))
                    client.send(data_length_bytes)

                    client.send(data)

            del clients_data[clients_connected[client_socket][1]]
            del clients_connected[client_socket]
            client_socket.close()
            break
        except ConnectionAbortedError:
            print(f"{clients_connected[client_socket][0]} disconnected unexpectedly.")

            for client in clients_connected:
                if client != client_socket:
                    client.send('notification'.encode())
                    data = pickle.dumps({'message': f"{clients_connected[client_socket][0]} left the chat",
                                         'id': clients_connected[client_socket][1], 'n_type': 'left'})
                    data_length_bytes = struct.pack('i', len(data))
                    client.send(data_length_bytes)
                    client.send(data)

            del clients_data[clients_connected[client_socket][1]]
            del clients_connected[client_socket]
            client_socket.close()
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

            print(f"connected with {str(address)}!")

            # dat mu vedet ze pripojeny, spustit prijimani zprav
            client.send("connected to the server\n".encode('utf-8'))
            thread = threading.Thread(target=handle, args=(client, nickname, clients))
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


# nastaveni pripojeni
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((host, port))

serversocket.listen()


print(f"server running")

# spusteni
receive()