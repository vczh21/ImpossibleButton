import tkinter as tk
from tkinter import ttk


class ImpossibleButton:
    def __init__(self, master):
        self.success_rate = 100

        # GUI setup
        self.master = master
        self.master.title("ImpossibleButton")

        # Button
        self.button = ttk.Button(self.master, width=20, text=f"Success Rate:{self.success_rate}%", command=self.button_click, padding=45)
        self.button.grid(padx=15, pady=15)


    def button_click(self):
        self.success_rate -= 1
        self.button.configure(text=f"Success Rate:{self.success_rate}%")


if __name__ == "__main__":
    root = tk.Tk()
    app = ImpossibleButton(root)
    root.geometry("250x150")
    root.mainloop()