import tkinter as tk
from tkinter.filedialog import askopenfilename

def create_labels(master, name, row, column):
        tk.Label(
            master,
            text=name
            ).grid(row = row, column = column)


def create_entries(master, varname, row, column):
    global inst_entries
    inst_entries[varname] = tk.Entry(
        master,
        width = 90)
    inst_entries[varname].grid(row = row, column = column)

def choose_file(label: str, entry: dict):
    x = askopenfilename()
    entry[label].insert(0, x)
