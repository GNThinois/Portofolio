import tkinter as tk
from tkinter import filedialog, ttk
import pandas as pd
import os
import importlib.util

SCRIPTS_DIR = r"C:\Users\Thinois\PycharmProjects\Portofolio\Ilhup\scripts"
FILES_DIR = r"C:\Users\Thinois\Desktop\MSA"
RESULTS_DIR = r"C:\Users\Thinois\Desktop\MSA\FichiersOK"

def browse_file():
    filename = filedialog.askopenfilename(initialdir=FILES_DIR, filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")))
    if filename:
        return filename
    else:
        print("No file selected.")
        return None

def browse_folder():
    foldername = filedialog.askdirectory(initialdir=FILES_DIR)
    if foldername:
        return foldername
    else:
        print("No folder selected.")
        return None

def load_csv(filename):
    if filename:
        try:
            df = pd.read_csv(filename, encoding='ISO-8859-1', delimiter=';')
            return df
        except pd.errors.ParserError:
            print("Could not parse file. Please make sure it is a valid CSV file.")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None
    else:
        return None

def get_scripts(directory):
    return [f for f in os.listdir(directory) if f.endswith('.py')]

def load_script(script_path):
    spec = importlib.util.spec_from_file_location("module.name", script_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def save_dataframe(df, filename):
    try:
        # Make sure to join the filename with RESULTS_DIR
        df.to_csv(os.path.join(RESULTS_DIR, filename), index=False, encoding='utf-8-sig')
        print(f"File {filename} saved successfully in {RESULTS_DIR}.")
    except Exception as e:
        print(f"Error occurred: {e}")



def main():
    root = tk.Tk()
    root.withdraw()

    filename = browse_file()
    print(filename)
    if filename:
        df = load_csv(filename)
        if df is not None:
            script_choice = filedialog.askopenfilename(initialdir=SCRIPTS_DIR, title="Select script",
                                                       filetypes=(("Python Files", "*.py"), ("All Files", "*.*")))
            if script_choice:
                script = load_script(script_choice)
                df = script.run(df)

                # save the dataframe to a csv file in the RESULTS_DIR
                save_dataframe(df, f'{os.path.basename(filename)}_rdy')
            else:
                print("No script selected.")
    else:
        print("No file selected.")
    print(df)
    # Open the RESULTS_DIR folder in the file explorer
    os.startfile(RESULTS_DIR)
    root.destroy()


if __name__ == "__main__":
    main()
