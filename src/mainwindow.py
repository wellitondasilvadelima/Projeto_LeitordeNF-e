"""
=================================================================================
Project: NF-e XML Reader
File: mainwindow.py
Description: Script to read and extract information from electronic invoices (NF-e)
Author: Welliton Lima
Creation Date: 01/03/2025
Last Modified: 11/03/2025
Version: 1.1
License: MIT License
=================================================================================
"""

import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from get_path import path
from reader import nfe_reader
import os

# -------|      Functions     |-------------------------------------------|

def clear():
    label_msg.configure(text="",font=("Segoe UI", 14))
    progress.set(0)

def open_popup():
    def set_value(value):
        response.set(value)  # Sets the selected value
        popup.destroy()      # Close the pop-up

    popup = ctk.CTkToplevel()
    popup.title("Escolha uma opção")

    response = ctk.StringVar()  # Variable to store the return

    center_window(popup,250,150) # to position the window in the center of the screen

    ctk.CTkLabel(popup, text="Directories have been created,\nadd files to the input folder",font=("Segoe UI", 14)).pack(pady=10)
    ctk.CTkButton(popup, text="OK", command=lambda: set_value(True),width=100, height=50).pack(pady=20)

    popup.transient(mainwindow)    # Makes the window stay on top of the main one
    popup.grab_set()               # Blocks interaction with the main
    mainwindow.wait_window(popup)  # Wait for the pop-up to close

    return response.get()  # Returns the chosen value

def start():
    path_input, path_data, msg_input = path()
    
    if(msg_input == True):
        open_popup()
    else:
        value = True if os.listdir(path_input) else False

    if(value == True):
        msg = nfe_reader(path_input,path_data,label_msg,progress,mainwindow)
        CTkMessagebox(title="Alert",message=msg,icon="info", option_1="OK")
        label_msg.configure(text=msg,font=("Segoe UI", 14))
    else:
        label_msg.configure(text="Insert files into input directory: ",font=("Segoe UI", 14))

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

def main():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue") 
    global mainwindow, label_msg, progress

    mainwindow = ctk.CTk()
    mainwindow.title("NF-e Read")

    center_window(mainwindow,380,320)

    label_title = ctk.CTkLabel(mainwindow, text="PRESS THE BUTTON TO START: ",font=("Segoe UI", 14),text_color="white")
    label_title.pack()

    button_start = ctk.CTkButton(mainwindow,text="START",command=start,width=150, height=50)
    button_start.pack(pady=20)
    button_clear = ctk.CTkButton(mainwindow,text="Clear",command=clear,width=150, height=50)
    button_clear.pack(pady=5)

    label_msg = ctk.CTkLabel(mainwindow, text="", font=("Segoe UI", 10), text_color="white")
    label_msg.pack(pady=5)

    progress = ctk.CTkProgressBar(mainwindow, width=300)
    progress.set(0)
    progress.pack(pady=5)

    mainwindow.mainloop()

# -----| END MainWindow |-----

if __name__ == '__main__':
    main()