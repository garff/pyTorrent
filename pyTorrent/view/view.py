import tkinter as tk
from tkinter import ttk

class View(tk.Tk):

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("pyTorrent v1.0.0")

    def main(self):
        self.mainloop()

    def _make_main_frame(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(padx=self.PAD, pady=self.PAD)