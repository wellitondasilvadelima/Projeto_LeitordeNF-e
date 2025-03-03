"""
=================================================================================
Project: NF-e XML Reader
File: mainwindow.py
Description: Script to read and extract information from electronic invoices (NF-e)
Author: Welliton Lima
Creation Date: 01/03/2025
Last Modified: 03/03/2025
Version: 1.0
License: MIT License
=================================================================================
"""

import tkinter as tk
from tkinter import messagebox
from get_path import path
from reader import nfe_reader

# -------|    Variable declaration   |-------
msg = ""
# -------| END Variable declaration |-------

# -------| Function |-------

def open_popup():
    def set_value(value):
        response.set(value)  # Sets the selected value
        popup.destroy()      # Close the pop-up

    popup = tk.Toplevel()
    popup.title("Escolha uma opção")

    response = tk.StringVar()  # Variable to store the return

    center_window(popup,250,150) # to position the window in the center of the screen

    tk.Label(popup, text="Files added?",font=("Arial", 12)).pack(pady=10)
    tk.Button(popup, text="YES", command=lambda: set_value(True),width=15, height=2).pack()
    tk.Button(popup, text="NO", command=lambda: set_value(False),width=15, height=2).pack()

    popup.transient(mainwindow)    # Makes the window stay on top of the main one
    popup.grab_set()               # Blocks interaction with the main
    mainwindow.wait_window(popup)  # Wait for the pop-up to close

    return response.get()  # Returns the chosen value

def start():
    path_input, path_data, msg_input = path()
    
    if(msg_input == True):
        value = open_popup()
    else:
        value = True

    if(value == True):
        msg = nfe_reader(path_input,path_data,label_msg)
        messagebox.showinfo("Aviso",msg)
        label_msg.config(text=msg,font=("Arial", 10))
    else:
        label_msg.config(text="Insert files into input directory: ",font=("Arial", 12))


def center_window(window,width,height):
     # Gets the screen size
    width_screen = window.winfo_screenwidth()
    height_screen = window.winfo_screenheight()

    # Calculates x and y position to center
    pos_x = (width_screen // 2) - (width // 2)
    pos_y = (height_screen // 2) - (height // 2)

    # Defines centered geometry
    window.geometry(f"{width}x{height}+{pos_x}+{pos_y}")

# -------| END Function |-------

# -------| MainWindow |-------

mainwindow = tk.Tk()
mainwindow.title("NF-e Read")

center_window(mainwindow,325,200)

label_title = tk.Label(mainwindow, text="PRESS THE BUTTON TO START: ",font=("Arial", 12))
label_title.pack()

button = tk.Button(mainwindow,text="START",command=start,width=15, height=2).pack(pady=20)

label_msg = tk.Label(mainwindow, text="",font=("Arial", 10))
label_msg.pack()

mainwindow.mainloop()

# -----| END MainWindow |-----
