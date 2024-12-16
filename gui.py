import customtkinter as ctk
from tkinter import messagebox

class ChatAppGUI(ctk.CTk):
    def __init__(self, send_callback=None, close_callback=None):

        # Init parent tridy customtkinter
        super().__init__()

        self.send_callback = send_callback
        self.close_callback = close_callback

        # Nastavení hlavního okna
        self.title("Client-Server Chat Application")
        self.geometry("500x450")
        ctk.set_appearance_mode("dark")

        # Zákaz zmény velikosti okna 
        self.resizable(False, False)
 
        self.chat_label = ctk.CTkLabel(self, text="Chat:", text_color="#fff")
        self.chat_label.pack(padx=20, pady=(10, 5))

        self.text_area = ctk.CTkTextbox(self, width=480, height=250, wrap="none", fg_color="#424242")
        self.text_area.pack(padx=2, pady=5)
        self.text_area.configure(state="disabled")

        self.msg_label = ctk.CTkLabel(self, text="Message:", text_color="#fff")
        self.msg_label.pack(padx=20, pady=(10, 5))

        self.input_area = ctk.CTkTextbox(self, height=50, width=480, fg_color="#424242")
        self.input_area.pack(padx=20, pady=5)

        self.send_button = ctk.CTkButton(self, text="SEND", command=self.send_message)
        self.send_button.pack(padx=20, pady=10)

        # Ctrl+Enter zkratka
        self.bind("<Control_L><Return>", self.handle_shortcut)

        # Zavrření okna
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def send_message(self):
        """
        Odešle zprávu
        """
        message = self.input_area.get("0.0", "end").strip()
        self.input_area.delete("0.0", "end")
        
        if message:
            self.send_callback(message)

    def display_message(self, message):
        """
        Zobrazí zprávu v textovém poli
        """
        self.text_area.configure(state="normal")
        self.text_area.insert("end", message + "\n")
        self.text_area.configure(state="disabled")
        self.text_area.see("end")

    def handle_shortcut(self, event):
        """
        Obsluha klávesové zkratky Ctrl+Enter
        """
        self.send_message()

    def on_closing(self):
        """
        Obsluha zavření okna
        """
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.close_callback()
            self.destroy()

if __name__ == "__main__":
    app = ChatAppGUI()

    app.mainloop()
