import socket
import threading
from tkinter import simpledialog
from gui import ChatAppGUI 
import sys

# Deklarace proměnných
host = "127.0.0.1"
port = 9090

def send_message(message):
    """
    Odešle zprávu
    Pokud je zpráva /clear nic neodesle ale provede clear
    Cokoli jiného odesle na srv
    """
    if message.strip() == "/clear":
        app.text_area.configure(state="normal")
        app.text_area.delete("0.0", "end")
        app.text_area.configure(state="disabled")
    else:
        # print(f"Sending message: {message}") 
        s.send(message.encode("utf-8"))

def receive_messages():
    """
    Zpracování příchozích zpráv
    Porad posloucha a prijima zpravy
    Prvni zprava od srv bude NICK a na to odesilam svoji prezdivku
    Jinak se odkazuji na gui.py pro zobrazeni zpravy
    """
    while True:
        try:
            msg = s.recv(1024).decode("utf-8")
            if msg == "NICK":
                s.send(nickname.encode("utf-8"))
            else:
                app.display_message(msg)
        except Exception as e:
            print(f"Error: {e}")
            s.close()
            break

def close_app():
    """
    Zavření aplikace
    """
    s.close()
    app.quit()
    sys.exit()

# Spuštění GUI
if __name__ == "__main__":
    # Socket connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    # Získání přezdívky od uživatele
    while True:
        nickname = simpledialog.askstring("Nickname", "Please choose a nickname:")

        if nickname is None:
            sys.exit()
        elif not nickname.strip():
            continue
        else:
            break


    # Inicializace aplikace s callbacky
    app = ChatAppGUI(send_callback=send_message, close_callback=close_app)

    # Threading
    receive_thread = threading.Thread(target=receive_messages, daemon=True)
    receive_thread.start()

    # Main loop
    app.mainloop()
