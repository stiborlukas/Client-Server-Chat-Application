import socket
import threading
import logging

# Deklarace proměnných
host = "127.0.0.1"
port = 9090
clients = []
nicknames = []
about_users = dict()

# Logging setup
logging.basicConfig(filename='server_logs.log', filemode='a', format='%(asctime)s : %(message)s', datefmt='[%d/%m/%Y] %H:%M:%S', level=logging.DEBUG)
logging.info("SRV RUNNING...")

# Socket connection
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen()

def broadcast(msg, nickname=None):
    """
    Poílání zprávy všem připojeným
    Pokud má parametr nickname zobrazí ve formátu {nickname}: {msg_temp}
    Pokud nemá {msg} = umoznuje odesilat zpravy od serveru
    """
    msg_temp = msg.strip()

    if nickname != None:
        message = f"{nickname}: {msg_temp}"
    else:
        message = f"{msg}"
    message = message.encode('utf-8')

    for client in clients:
        client.send(message)

def handle(client, nickname, clients, nicknames):
    """
    Obsluha klientů
    Přijímá zprávy v jednotlivých vláknech
    řeší soukromé zprávy @
    řeší příkazy /
    Odpojení klienta
    """
    while True:
        try:
            about_users[nickname]["number"] += 1
            
            msg = client.recv(1024).decode('utf-8')
            msg = msg.strip()
            print(msg)

            # reseni soukrome zpravy
            if msg[0] == "@":
                user_number, user_name, found = is_there_nickname(msg, client, nickname, nicknames)

                if found:
                    toSend = [client, clients[user_number]]
                    message = f"{nickname}: {msg}"
                    for y in toSend:
                        y.send(message.encode('utf-8'))
                
                elif not found:
                    print(f"{user_name} was not found in the list.")

            
            # řešení jednotlivých příkazů (clear u klienta)
            elif msg[0] == "/":
                cmd = msg.strip("/")

                match cmd:
                    case "help":
                        client.send("\n/users - see online users\n/clear - clear my chat\n".encode('utf-8'))
                    case "users":
                        command_users(client, nicknames)
                    case _:
                        client.send("cmd does not exists, type /help for available cmds\n".encode('utf-8'))
                    
            
            # když zpráva nebyla soukroma ani prikaz -> broadcast
            else:
                if len(msg) == 0:
                    pass
                else:
                    print(len(msg))
                    broadcast(msg, nickname)

        # ukončení klienta 
        except Exception as e:
            # odstranit uzivatele
            clients.remove(client)
            nicknames.remove(nickname)
            x = about_users.pop(nickname)

            # logging
            logging.error(f"{e} {nickname} {client} pocet zprav: { x['number'] }")

            # oznamit ze odesel
            broadcast(f"{nickname} left the chat :(")

            break


def receive():
    """
    řeší úvodní spojení s klientem
    zajištuje unikátní přezdívku

    """
    while True:
        try:
            # pripojeni klienta
            client, address = server_socket.accept()

            # dostat prezdivku klienta
            client.send("NICK".encode('utf-8'))
            nickname = client.recv(1024).decode("utf-8")
            nickname = nickname.translate({ord(':'): None}).strip()

            # zaridit unikatni prezdivku
            nickname = unique_nickname(nickname)

            # pocitat s klientem
            clients.append(client)
            nicknames.append(nickname)
            about_users[nickname] = { "number": 0 }

            # oznamit prichod
            client.send(f"connected to the server as {nickname}".encode('utf-8'))
            broadcast(f"{nickname} joined the chat")

            # logging
            logging.info(f"user {nickname} joined with {client}")  

            # vlakno 
            thread = threading.Thread(target=handle, args=(client, nickname, clients, nicknames))
            thread.start()

        except Exception as e:
            logging.error(e)

def unique_nickname(nickname):
    """
    Zajisti unikatni prezdivky
    """
    if nickname in nicknames:
        i = nickname.find('_')
        if i != -1 and i + 1 < len(nickname) and nickname[i + 1].isdigit():
            base = nickname[:i + 1]
            number = int(nickname[i + 1:])
        else:
            base = f"{nickname}_"
            number = 0

        # inkrementovat sufix dokud nickname nebude jedinecny
        while f"{base}{number}" in nicknames:
            number += 1
        nickname = f"{base}{number}"
        
        print(nickname)

    return nickname

def is_there_nickname(msg, client, nickname, nicknames):
    """
    Zjistuje zdali existuje uzivatel se jmenem za @
    """
    start = msg.find("@")
    end = msg.find(" ", start)
    
    if end == -1:
        end = len(msg)

    
    username = msg[start + 1:end]

    if username == nickname:
        client.send("u cant @ yourself\n".encode('utf-8'))
        
        return None, None, False
    else:
        i = 0

        for x in nicknames:
            print(x)
            if username == x:
                print("Existuje")
                
                return i, username, True         
            i+=1

        return None, username, False

def command_users(client, nicknames):
    """
    command /users
    """
    online = f"\nList of online users:\n"
    online = online.encode('utf-8')

    client.send(online)
    for e in nicknames:
        mess = f"{e}\n"
        mess = mess.encode('utf-8')
        client.send(mess)

print(f"server running")
receive()