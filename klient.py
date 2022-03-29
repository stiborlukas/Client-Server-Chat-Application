import socket
import threading
import tkinter as tk
import tkinter.scrolledtext
from tkinter import simpledialog
import sys


# odesilani zprav
def write():
    message = input_area.get('1.0', 'end')
    s.send(message.encode('utf-8'))
    input_area.delete('1.0', 'end')


# prijimani zprav
def receive():
    while True:
        msg = s.recv(1024).decode('utf-8')
        print(msg)
        try:
            if msg == "NICK":
                message = f"{nickname}: {input_area.get('1.0', 'end')}"
                s.send(message.encode('utf-8'))
            else:

                textarea.config(state='normal')
                textarea.insert("end", msg)
                textarea.config(state='disabled')
        except:
            s.close()
            sys.exit()


# nastaveni promennych
host = "127.0.0.1"
# host = socket.gethostname()
# port = 2205
port = 9090

# nastaveni pripojeni
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# okno ve kterem se zeptam na jmeno
window = tk.Tk()
window.withdraw()
nickname = simpledialog.askstring("nickname", "please choose nickname", parent=window)

# -------------------------------------tkinter
win = tk.Tk()

win.configure(bg="lightgray")

chat_label = tk.Label(win, text="CHat:", bg="lightgray")
chat_label.pack(padx=20, pady=5)

textarea = tk.scrolledtext.ScrolledText(win)
textarea.pack(padx=20, pady=5)
textarea.config(state='disabled')

msg_label = tk.Label(win, text="Message:", bg="lightgray")
msg_label.pack(padx=20, pady=5)

input_area = tk.Text(win, height=3)
input_area.pack(padx=20, pady=5)

# win.bind('<Return>', write)
send_button = tk.Button(win, text="SEND", command=write)
send_button.pack(padx=20, pady=5)

receive_thread = threading.Thread(target=receive)
receive_thread.start()
win.mainloop()