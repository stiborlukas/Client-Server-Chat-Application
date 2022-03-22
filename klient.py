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

        msg = s.recv(1024).decode('utf-8')
        print(msg)
        try:
            if msg == "NICK":
                # ask_name()
                message = f"{nickname}: {input_area.get('1.0', 'end')}"
                s.send(message.encode('utf-8'))
        except:
            # msg = s.recv(1024)
            print(msg)
            textarea.config(state='normal')
            textarea.insert("end", msg)
            textarea.config(state='disabled')
            # if message == "NICK":
            #     print("nick")
            #     s.send(nickname.encode('utf-8'))
            # else:
            #     textarea.insert(END, message)


host = socket.gethostname()
# host = "127.0.0.1"
port = 2205
# port = 9090

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


# gui_thread.start()
