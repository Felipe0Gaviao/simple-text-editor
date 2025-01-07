from pathlib import Path
from tkinter.constants import BOTH, X

import customtkinter as ctk
from customtkinter import filedialog


class App(ctk.CTk):
    default_file_path = Path().home()

    def __init__(self):
        super(App, self).__init__()
        self.title("Simple Text Editor")
        self.geometry("500x300")

        self.options = ctk.CTkFrame(self, height=25)
        self.options.pack(fill=X, anchor="n")

        self.open_button = ctk.CTkButton(self.options, text="Open", command=self.open)
        self.open_button.grid(column=0, row=0)

        self.text_window = ctk.CTkTextbox(
            self,
            border_color="red",
            border_width=1,
        )
        self.text_window.pack(expand=True, fill=BOTH)

    def open(self):
        file = filedialog.askopenfile(
            initialdir=self.default_file_path,
            title="Select a Text File",
            filetypes=[("Text Files", "*.txt")],
        )

        if file is not None:
            with open(file.name) as f:
                self.default_file_path = Path(f.name).parent
                self.text_window.delete(1.0, "end-1c")
                self.text_window.insert(1.0, file.read())


if __name__ == "__main__":
    app = App()
    app.mainloop()
