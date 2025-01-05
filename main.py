from tkinter.constants import BOTH, X

import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super(App, self).__init__()
        self.title("Simple Text Editor")
        self.geometry("500x300")

        self.options = ctk.CTkFrame(self, height=25)
        self.options.pack(fill=X, anchor="n")

        self.text_window = ctk.CTkTextbox(self, border_color="red", border_width=1)
        self.text_window.pack(expand=True, fill=BOTH)


if __name__ == "__main__":
    app = App()
    app.mainloop()
