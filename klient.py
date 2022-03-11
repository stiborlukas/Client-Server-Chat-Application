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
