# -------------------------------------------skola
# import socket
# import tkinter as tk
#
# window = tk.Tk()
# entry = tk.Entry(width=22).pack()
#
#
# def ano():
#     text = f"{entry.get()}"
#     entry.delete(0,"end")
#     entry.insert(0, text)
#
#
# message = tk.Button(text="ano", command=ano).pack()
#
# canvas= tk.Canvas(window, width= 1000, height= 750)
#
# # canvas.create_text(300, 50, text="HELLO WORLD")
# # canvas.pack()
#
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # host = socket.gethostname()
# host = "127.0.0.1"
# port = 2205
#
# s.connect((host, port))
# msg = s.recv(1024)
# print(msg.decode('ascii'))
#
# # window.insert(0, "ano")
# zprava = "server: ",  msg
# canvas.create_text(300, 50, text=zprava)
# canvas.pack()
#
# data = "Heskfnjdnfsj!";
#
# s.send(data.encode());
# s.close()
#
#
#
#
#
#
#
# window.mainloop()
import socket
import threading
import tkinter as tk
import tkinter.scrolledtext
from tkinter import simpledialog


def gui_loop():
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

    def write():
        message = f"{nickname}: {input_area.get('1', 'end')}"
        s.send(message.encode('utf-8'))
        input_area.delete('1', 'end')

    send_button = tk.Button(win, text="SEND", command=write)
    send_button.pack(padx=20, pady=5)

    win.mainloop()


def receive():
    running = True
    while running:
        try:
            message = s.recv(1024)
            if message == "NICK":
                s.send(nickname.encode('utf-8'))
            else:
                pass
        except:
            pass


host = "127.0.0.1"
# port = 2205
port = 9090

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

msg = tk.Tk()
msg.withdraw()

nickname = simpledialog.askstring("nickname", "please choose nickname", parent=msg)

# gui_done = False
# running = True

gui_thread = threading.Thread(target=gui_loop)
receive_thread = threading.Thread(target=receive)

gui_thread.start()
receive_thread.start()
