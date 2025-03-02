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
        response.set(value)  # Define o valor selecionado
        popup.destroy()      # Fecha o pop-up

    popup = tk.Toplevel()
    popup.title("Escolha uma opção")
    #popup.geometry("250x150")

    response = tk.StringVar()  # Variável para armazenar o retorno

    center_window(popup,250,150)

    tk.Label(popup, text="Files added?",font=("Arial", 12)).pack(pady=10)
    tk.Button(popup, text="YES", command=lambda: set_value(True),width=15, height=2).pack()
    tk.Button(popup, text="NO", command=lambda: set_value(False),width=15, height=2).pack()

    popup.transient(mainwindow)  # Faz a janela ficar sobre a principal
    popup.grab_set()         # Bloqueia a interação com a principal
    mainwindow.wait_window(popup)  # Aguarda o pop-up ser fechado

    return response.get()  # Retorna o valor escolhido

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
     # Obtém o tamanho da tela
    width_screen = window.winfo_screenwidth()
    height_screen = window.winfo_screenheight()

    # Calcula a posição x e y para centralizar
    pos_x = (width_screen // 2) - (width // 2)
    pos_y = (height_screen // 2) - (height // 2)

    # Define a geometria centralizada
    window.geometry(f"{width}x{height}+{pos_x}+{pos_y}")

# -------| END Function |-------

# -------| MainWindow |-------

mainwindow = tk.Tk()
mainwindow.title("NF-e Read")
#mainwindow.geometry("300x150")

center_window(mainwindow,325,200)

label_title = tk.Label(mainwindow, text="PRESS THE BUTTON TO START: ",font=("Arial", 12))
label_title.pack()

button = tk.Button(mainwindow,text="START",command=start,width=15, height=2).pack(pady=20)

label_msg = tk.Label(mainwindow, text="",font=("Arial", 10))
label_msg.pack()


mainwindow.mainloop()

# -----| END MainWindow |-----