import tkinter as tk
from tkinter import ttk
import random


class ImpossibleButton:
    def __init__(self, master):
        self.success_rate = 100
        self.clicks = 0

        # GUI setup
        self.master = master
        self.master.title("ImpossibleButton")

        # Button
        self.button = ttk.Button(self.master, width=20, text=f"Success Rate:{self.success_rate}%", command=self.button_click, padding=45)
        self.button.grid(padx=15, pady=15)

    def button_click(self):
        self.success_rate -= 1
        self.clicks += 1

        if random.randint(1, 100) <= self.success_rate:
            self.button.configure(text=f"Success Rate:{self.success_rate}%")
        else:
            self.button.configure(state=tk.DISABLED)
            self.show_result_window()

    def show_result_window(self):
        self.result_window = tk.Toplevel(self.master)
        self.result_window.title("You Lost!")
        self.result_label = ttk.Label(self.result_window, text=f"You Lost!\nWith {self.clicks} clicks")
        self.result_label.pack(padx=15, pady=15)
        self.restart_button = ttk.Button(self.result_window, text="Restart", command=self.restart)
        self.restart_button.pack(padx=5, pady=5)
        exit_button = ttk.Button(self.result_window, text="Exit", command=self.master.quit)
        exit_button.pack(padx=5, pady=5)
        self.result_window.protocol("WM_DELETE_WINDOW", self.restart)

    def restart(self):
        self.success_rate = 100
        self.clicks = 0
        self.button.configure(text=f"Success Rate:{self.success_rate}%", state=tk.NORMAL)
        self.result_window.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = ImpossibleButton(root)
    root.geometry("250x150")
    root.mainloop()