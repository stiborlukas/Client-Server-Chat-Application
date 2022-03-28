import socket
import threading
import tkinter as tk
import tkinter.scrolledtext
from tkinter import simpledialog


def write():
    # message = f"{nickname}: {input_area.get('1.0', 'end')}"
    # print("fd")
    message = input_area.get('1.0', 'end')
    s.send(message.encode('utf-8'))
    input_area.delete('1.0', 'end')


# def ask_name():
#     window = tk.Tk()
#     window.withdraw()
#
#     nickname = simpledialog.askstring("nickname", "please choose nickname", parent=window)
#     message = f"{nickname}: {input_area.get('1.0', 'end')}"
#     s.send(message.encode('utf-8'))

def receive():
    while True:
        # msg = s.recv(1024)
        msg = s.recv(1024).decode('utf-8')
        print(msg)
        try:
            if msg == "NICK":
                # ask_name()
                # print("dbfgyhuasbdyhuazbughfsdj")
                message = f"{nickname}: {input_area.get('1.0', 'end')}"
                s.send(message.encode('utf-8'))
            else:
                # anoan
                # print("anonanoanao")
                # print(message)
                textarea.config(state='normal')
                # textarea.insert("end", f"{nickname}: ")
                textarea.insert("end", msg)
                # textarea.insert("end", "\n")
                textarea.config(state='disabled')
        except:
            pass
            # msg = s.recv(1024)
            # print(msg)
            # message = msg.decode('utf-8')
            # print("anonanoanao")
            # textarea.config(state='normal')
            # textarea.insert("end", msg)
            # textarea.config(state='disabled')
            # if message == "NICK":
            #     print("nick")
            #     s.send(nickname.encode('utf-8'))
            # else:
            #     textarea.insert(END, message)


host = "127.0.0.1"
# host = socket.gethostname()
# port = 2205
port = 9090

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

window = tk.Tk()
window.withdraw()

nickname = simpledialog.askstring("nickname", "please choose nickname", parent=window)

# gui_done = False
# running = True

# gui_thread = threading.Thread(target=gui_loop)

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


send_button = tk.Button(win, text="SEND", command=write)
send_button.pack(padx=20, pady=5)

receive_thread = threading.Thread(target=receive)
receive_thread.start()
win.mainloop()
