#tkinter interface + file management

import tkinter as tk
from tkinter import filedialog, ttk
import pandas as pd
import os
import importlib.util

SCRIPTS_DIR = r"/Ilhup/scripts"
FILES_DIR = r"C:\Users\Thinois\Desktop\MSA"
RESULTS_DIR = r"C:\Users\Thinois\Desktop\MSA\FichiersOK"

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("500x300")  # Adjust the size of the window
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.load_file_button = tk.Button(self)
        self.load_file_button["text"] = "Select CSV File"
        self.load_file_button["command"] = self.load_csv
        self.load_file_button.grid(row=0, column=0, pady=10, padx=10)  # Add some padding

        self.file_label = tk.Label(self, text="")
        self.file_label.grid(row=1, column=0, pady=10, padx=10)

        self.load_script_button = tk.Button(self)
        self.load_script_button["text"] = "Select Script"
        self.load_script_button["command"] = self.load_script
        self.load_script_button.grid(row=0, column=1, pady=10, padx=10)

        self.script_label = tk.Label(self, text="")
        self.script_label.grid(row=1, column=1, pady=10, padx=10)

        self.run_button = tk.Button(self)
        self.run_button["text"] = "Run"
        self.run_button["command"] = self.run
        self.run_button.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

    def load_csv(self):
        filename = filedialog.askopenfilename(initialdir=FILES_DIR, filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")))
        if filename:
            self.df = pd.read_csv(filename, encoding='ISO-8859-1', delimiter=';')
            self.filename = filename
            self.file_label["text"] = f"File loaded: {os.path.basename(filename)}"
        else:
            self.file_label["text"] = "No file selected."

    def load_script(self):
        script_filename = filedialog.askopenfilename(initialdir=SCRIPTS_DIR, filetypes=(("Python Files", "*.py"), ("All Files", "*.*")))
        if script_filename:
            spec = importlib.util.spec_from_file_location("module.name", script_filename)
            self.script_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(self.script_module)
            self.script_label["text"] = f"Script loaded: {os.path.basename(script_filename)}"
        else:
            self.script_label["text"] = "No script selected."

    def run(self):
        if hasattr(self, 'df') and hasattr(self, 'script_module'):
            self.df = self.script_module.run(self.df)
            save_filename = os.path.join(RESULTS_DIR, f'{os.path.basename(self.filename)}_rdy.csv')
            self.df.to_csv(save_filename, index=False, encoding='utf-8-sig')
            tk.messagebox.showinfo("Result", f"File saved: {save_filename}")
        else:
            tk.messagebox.showinfo("Result", "Make sure both CSV file and script are selected.")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
