from pathlib import Path
from tkinter.constants import BOTH, X
<<<<<<< HEAD
from typing import Self
=======
>>>>>>> fa9a283b547267d0ab49fd573271ff2299a14254

import customtkinter as ctk
from customtkinter import filedialog


<<<<<<< HEAD
class ToolbarButton(ctk.CTkButton):
    button_list: list[Self] = []

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs, width=80)

        self.button_list.append(self)

    def grid(self, *args, **kwargs):
        super().grid(*args, row=0, column=self.button_list.index(self), **kwargs)


=======
>>>>>>> fa9a283b547267d0ab49fd573271ff2299a14254
class App(ctk.CTk):
    default_file_path = Path().home()

    def __init__(self):
        super(App, self).__init__()
        self.title("Simple Text Editor")
        self.geometry("500x300")

        self.options = ctk.CTkFrame(self, height=25)
        self.options.pack(fill=X, anchor="n")

<<<<<<< HEAD
        self.open_button = ToolbarButton(self.options, text="Open", command=self.open)

        self.save_button = ToolbarButton(self.options, text="Save", command=self.save)

        for button in ToolbarButton.button_list:
            button.grid(padx=1)

        self.text_window = ctk.CTkTextbox(self, border_width=1)
        self.text_window.pack(expand=True, fill=BOTH)

    def open(self):
        self.file = filedialog.askopenfile(
=======
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
>>>>>>> fa9a283b547267d0ab49fd573271ff2299a14254
            initialdir=self.default_file_path,
            title="Select a Text File",
            filetypes=[("Text Files", "*.txt")],
        )

<<<<<<< HEAD
        if self.file is not None:
            self.title(f"{self.title()} - {self.file.name}")
            with open(self.file.name) as f:
                self.default_file_path = Path(f.name).parent
                self.text_window.delete(1.0, "end")
                self.text_window.insert(1.0, self.file.read())

    def save(self):
        if self.file is not None:
            file = self.file
        else:
            file = filedialog.asksaveasfile(
                initialdir=self.default_file_path,
                title="Select where to save the text file",
                filetypes=[("Text Files", "*.txt")],
            )
        with open(file.name, "w") as f:
            f.write(self.text_window.get(1.0, "end"))
=======
        if file is not None:
            with open(file.name) as f:
                self.default_file_path = Path(f.name).parent
                self.text_window.delete(1.0, "end-1c")
                self.text_window.insert(1.0, file.read())
>>>>>>> fa9a283b547267d0ab49fd573271ff2299a14254


if __name__ == "__main__":
    app = App()
    app.mainloop()
