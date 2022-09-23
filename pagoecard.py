
# import webbrowser as wb
# from tkinter import *
# from tkinter import *
# from tkinter.ttk import *
# from PIL import Image,ImageTk


# def acceso_web():
#    url = wb.open('https://ecard.center/index/decidir.php')

# ventana = Tk()
# ventana.geometry("350x150")
# photo = PhotoImage(file="logopng.png")
# boton1=Button(ventana,image=photo,command=acceso_web)
# boton1.place(x=10, y=10)

# ventana.mainloop()

import webbrowser as wb
from PIL import Image,ImageTk
import tkinter as tk
from os import path
import os, sys
from kivy.app import App
from kivy.lang import Builder



# ventana.title("Boton de Pago")



def acceso_web():
    #url = wb.open('ecard.center/index/express_checkout/index.php')
    url = wb.open('https://ecard.center/index/express_checkout/index.php')


    #url = wb.open('localhost/ecard.test/')
#webbrowser.register('google-chrome', none, webbrowser.BackgroudBrowser("C:/Program Files/Google/Chrome/chrome.exe"))


# def resource_path(relative_path):
#     """ Get absolute path to resource, works for dev and for PyInstaller """
#     try:
#         # PyInstaller creates a temp folder and stores path in _MEIPASS
#         base_path = sys._MEIPASS
#     except Exception:
#         base_path = os.path.abspath(".")

#     return os.path.join(base_path, relative_path)



ventana= tk.Tk()
ventana.title("Boton de Pago")
ventana.geometry("350x150")
imagen = ImageTk.PhotoImage(Image.open("logologin.jpeg"))
boton = tk.Button(ventana,image =imagen,command=acceso_web)
boton.place(x=10, y=10)
ventana.mainloop()
